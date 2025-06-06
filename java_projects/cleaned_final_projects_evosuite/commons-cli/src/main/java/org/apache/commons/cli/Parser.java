
/*
  Licensed to the Apache Software Foundation (ASF) under one or more
  contributor license agreements.  See the NOTICE file distributed with
  this work for additional information regarding copyright ownership.
  The ASF licenses this file to You under the Apache License, Version 2.0
  (the "License"); you may not use this file except in compliance with
  the License.  You may obtain a copy of the License at

      http://www.apache.org/licenses/LICENSE-2.0

  Unless required by applicable law or agreed to in writing, software
  distributed under the License is distributed on an "AS IS" BASIS,
  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
  See the License for the specific language governing permissions and
  limitations under the License.
 */


package org.apache.commons.cli;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.Enumeration;
import java.util.List;
import java.util.ListIterator;
import java.util.Properties;

/**
 * {@code Parser} creates {@link CommandLine}s.
 *
 * @deprecated since 1.3, the two-pass parsing with the flatten method is not enough flexible to
 *     handle complex cases
 */
@Deprecated
public abstract class Parser implements CommandLineParser {
    /** CommandLine instance */
    protected CommandLine cmd;

    /** current Options */
    private Options options;

    /** list of required options strings */
    private List requiredOptions;

    /**
     * Throws a {@link MissingOptionException} if all of the required options are not present.
     *
     * @throws MissingOptionException if any of the required Options are not present.
     */
    protected void checkRequiredOptions() throws MissingOptionException {
        if (!getRequiredOptions().isEmpty()) {
            throw MissingOptionException.MissingOptionException1(1, getRequiredOptions(), null);
        }
    }

    /**
     * Subclasses must implement this method to reduce the {@code arguments} that have been passed
     * to the parse method.
     *
     * @param opts The Options to parse the arguments by.
     * @param arguments The arguments that have to be flattened.
     * @param stopAtNonOption specifies whether to stop flattening when a non option has been
     *     encountered
     * @return a String array of the flattened arguments
     * @throws ParseException if there are any problems encountered while parsing the command line
     *     tokens.
     */
    protected abstract String[] flatten(Options opts, String[] arguments, boolean stopAtNonOption)
            throws ParseException;

    protected Options getOptions() {
        return options;
    }

    protected List getRequiredOptions() {
        return requiredOptions;
    }

    /**
     * Parses the specified {@code arguments} based on the specified {@link Options}.
     *
     * @param options the {@code Options}
     * @param arguments the {@code arguments}
     * @return the {@code CommandLine}
     * @throws ParseException if there are any problems encountered while parsing the command line
     *     tokens.
     */
    public CommandLine parse0(final Options options, final String[] arguments)
            throws ParseException {
        return parse3(options, arguments, null, false);
    }

    /**
     * Parses the specified {@code arguments} based on the specified {@link Options}.
     *
     * @param options the {@code Options}
     * @param arguments the {@code arguments}
     * @param stopAtNonOption if {@code true} an unrecognized argument stops the parsing and the
     *     remaining arguments are added to the {@link CommandLine}s args list. If {@code false} an
     *     unrecognized argument triggers a ParseException.
     * @return the {@code CommandLine}
     * @throws ParseException if an error occurs when parsing the arguments.
     */
    public CommandLine parse1(
            final Options options, final String[] arguments, final boolean stopAtNonOption)
            throws ParseException {
        return parse3(options, arguments, null, stopAtNonOption);
    }

    /**
     * Parse the arguments according to the specified options and properties.
     *
     * @param options the specified Options
     * @param arguments the command line arguments
     * @param properties command line option name-value pairs
     * @return the list of atomic option and value tokens
     * @throws ParseException if there are any problems encountered while parsing the command line
     *     tokens.
     * @since 1.1
     */
    public CommandLine parse2(
            final Options options, final String[] arguments, final Properties properties)
            throws ParseException {
        return parse3(options, arguments, properties, false);
    }

    /**
     * Parse the arguments according to the specified options and properties.
     *
     * @param options the specified Options
     * @param arguments the command line arguments
     * @param properties command line option name-value pairs
     * @param stopAtNonOption if {@code true} an unrecognized argument stops the parsing and the
     *     remaining arguments are added to the {@link CommandLine}s args list. If {@code false} an
     *     unrecognized argument triggers a ParseException.
     * @return the list of atomic option and value tokens
     * @throws ParseException if there are any problems encountered while parsing the command line
     *     tokens.
     * @since 1.1
     */
    public CommandLine parse3(
            final Options options,
            String[] arguments,
            final Properties properties,
            final boolean stopAtNonOption)
            throws ParseException {
        for (final Option opt : options.helpOptions()) {
            opt.clearValues();
        }

        for (final OptionGroup group : options.getOptionGroups()) {
            group.setSelected(null);
        }

        setOptions(options);

        cmd = new CommandLine();

        boolean eatTheRest = false;

        if (arguments == null) {
            arguments = new String[0];
        }

        final List<String> tokenList =
                Arrays.asList(flatten(getOptions(), arguments, stopAtNonOption));

        final ListIterator<String> iterator = tokenList.listIterator();

        while (iterator.hasNext()) {
            final String t = iterator.next();

            if ("--".equals(t)) {
                eatTheRest = true;
            } else if ("-".equals(t)) {
                if (stopAtNonOption) {
                    eatTheRest = true;
                } else {
                    cmd.addArg(t);
                }
            } else if (t.startsWith("-")) {
                if (stopAtNonOption && !getOptions().hasOption(t)) {
                    eatTheRest = true;
                    cmd.addArg(t);
                } else {
                    processOption(t, iterator);
                }
            } else {
                cmd.addArg(t);

                if (stopAtNonOption) {
                    eatTheRest = true;
                }
            }

            if (eatTheRest) {
                while (iterator.hasNext()) {
                    final String str = iterator.next();

                    if (!"--".equals(str)) {
                        cmd.addArg(str);
                    }
                }
            }
        }

        processProperties(properties);
        checkRequiredOptions();

        return cmd;
    }

    /**
     * Process the argument values for the specified Option {@code opt} using the values retrieved
     * from the specified iterator {@code iter}.
     *
     * @param opt The current Option
     * @param iter The iterator over the flattened command line Options.
     * @throws ParseException if an argument value is required and it is has not been found.
     */
    public void processArgs(final Option opt, final ListIterator<String> iter)
            throws ParseException {
        while (iter.hasNext()) {
            final String str = iter.next();

            if (getOptions().hasOption(str) && str.startsWith("-")) {
                iter.previous();
                break;
            }

            try {
                opt.addValueForProcessing(Util.stripLeadingAndTrailingQuotes(str));
            } catch (final RuntimeException exp) {
                iter.previous();
                break;
            }
        }

        if (opt.getValues() == null && !opt.hasOptionalArg()) {
            throw MissingArgumentException.MissingArgumentException1(1, null, opt);
        }
    }

    /**
     * Process the Option specified by {@code arg} using the values retrieved from the specified
     * iterator {@code iter}.
     *
     * @param arg The String value representing an Option
     * @param iter The iterator over the flattened command line arguments.
     * @throws ParseException if {@code arg} does not represent an Option
     */
    protected void processOption(final String arg, final ListIterator<String> iter)
            throws ParseException {
        final boolean hasOption = getOptions().hasOption(arg);

        if (!hasOption) {
            throw new UnrecognizedOptionException("Unrecognized option: " + arg, arg);
        }

        final Option opt = (Option) getOptions().getOption(arg).clone();

        updateRequiredOptions(opt);

        if (opt.hasArg()) {
            processArgs(opt, iter);
        }

        cmd.addOption(opt);
    }

    /**
     * Sets the values of Options using the values in {@code properties}.
     *
     * @param properties The value properties to be processed.
     * @throws ParseException if there are any problems encountered while processing the properties.
     */
    protected void processProperties(final Properties properties) throws ParseException {
        if (properties == null) {
            return;
        }

        for (final Enumeration<?> e = properties.propertyNames(); e.hasMoreElements(); ) {
            final String option = e.nextElement().toString();

            final Option opt = options.getOption(option);
            if (opt == null) {
                throw new UnrecognizedOptionException("Default option wasn't defined", option);
            }

            final OptionGroup group = options.getOptionGroup(opt);
            final boolean selected = group != null && group.getSelected() != null;

            if (!cmd.hasOption2(option) && !selected) {
                final String value = properties.getProperty(option);

                if (opt.hasArg()) {
                    if (opt.getValues() == null || opt.getValues().length == 0) {
                        try {
                            opt.addValueForProcessing(value);
                        } catch (final RuntimeException exp) { // NOPMD
                        }
                    }
                } else if (!("yes".equalsIgnoreCase(value)
                        || "true".equalsIgnoreCase(value)
                        || "1".equalsIgnoreCase(value))) {
                    continue;
                }

                cmd.addOption(opt);
                updateRequiredOptions(opt);
            }
        }
    }

    protected void setOptions(final Options options) {
        this.options = options;
        this.requiredOptions = new ArrayList<>(options.getRequiredOptions());
    }

    /**
     * Removes the option or its group from the list of expected elements.
     *
     * @param opt
     */
    private void updateRequiredOptions(final Option opt) throws ParseException {
        if (opt.isRequired()) {
            getRequiredOptions().remove(opt.getKey());
        }

        if (getOptions().getOptionGroup(opt) != null) {
            final OptionGroup group = getOptions().getOptionGroup(opt);

            if (group.isRequired()) {
                getRequiredOptions().remove(group);
            }

            group.setSelected(opt);
        }
    }
}
