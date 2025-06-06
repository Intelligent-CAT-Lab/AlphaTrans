
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

import java.io.Serializable;
import java.util.ArrayList;
import java.util.Collection;
import java.util.Iterator;
import java.util.LinkedList;
import java.util.List;
import java.util.Properties;

/**
 * Represents list of arguments parsed against a {@link Options} descriptor.
 *
 * <p>It allows querying of a boolean {@link #hasOption(String opt)}, in addition to retrieving the
 * {@link #getOptionValue(String opt)} for options requiring arguments.
 *
 * <p>Additionally, any left-over or unrecognized arguments, are available for further processing.
 */
public class CommandLine implements Serializable {
    /**
     * A nested builder class to create {@code CommandLine} instance using descriptive methods.
     *
     * @since 1.4
     */
    public static final class Builder {
        /** CommandLine that is being build by this Builder. */
        private final CommandLine commandLine = new CommandLine();

        /**
         * Add left-over unrecognized option/argument.
         *
         * @param arg the unrecognized option/argument.
         * @return this Builder instance for method chaining.
         */
        public Builder addArg(final String arg) {
            commandLine.addArg(arg);
            return this;
        }

        /**
         * Add an option to the command line. The values of the option are stored.
         *
         * @param opt the processed option.
         * @return this Builder instance for method chaining.
         */
        public Builder addOption(final Option opt) {
            commandLine.addOption(opt);
            return this;
        }

        public CommandLine build() {
            return commandLine;
        }
    }

    /** The serial version UID. */
    private static final long serialVersionUID = 1L;

    /** The unrecognized options/arguments */
    private final List<String> args = new LinkedList<>();

    /** The processed options */
    private final List<Option> options = new ArrayList<>();

    /** Creates a command line. */
    protected CommandLine() {}

    /**
     * Add left-over unrecognized option/argument.
     *
     * @param arg the unrecognized option/argument.
     */
    protected void addArg(final String arg) {
        args.add(arg);
    }

    /**
     * Add an option to the command line. The values of the option are stored.
     *
     * @param opt the processed option.
     */
    protected void addOption(final Option opt) {
        options.add(opt);
    }

    /**
     * Retrieve any left-over non-recognized options and arguments
     *
     * @return remaining items passed in but not parsed as a {@code List}.
     */
    public List<String> getArgList() {
        return args;
    }

    /**
     * Retrieve any left-over non-recognized options and arguments
     *
     * @return remaining items passed in but not parsed as an array.
     */
    public String[] getArgs() {
        final String[] answer = new String[args.size()];

        args.toArray(answer);

        return answer;
    }

    /**
     * Return the {@code Object} type of this {@code Option}.
     *
     * @deprecated due to System.err message. Instead use getParsedOptionValue(char)
     * @param opt the name of the option.
     * @return the type of opt.
     */
    @Deprecated
    public Object getOptionObject0(final char opt) {
        return getOptionObject1(String.valueOf(opt));
    }

    /**
     * Return the {@code Object} type of this {@code Option}.
     *
     * @param opt the name of the option.
     * @return the type of this {@code Option}.
     * @deprecated due to System.err message. Instead use getParsedOptionValue(String)
     */
    @Deprecated
    public Object getOptionObject1(final String opt) {
        try {
            return getParsedOptionValue2(opt);
        } catch (final ParseException pe) {
            System.err.println(
                    "Exception found converting " + opt + " to desired type: " + pe.getMessage());
            return null;
        }
    }

    /**
     * Retrieve the map of values associated to the option. This is convenient for options
     * specifying Java properties like <code>-Dparam1=value1
     * -Dparam2=value2</code>. The first argument of the option is the key, and the 2nd argument is
     * the value. If the option has only one argument ({@code -Dfoo}) it is considered as a boolean
     * flag and the value is {@code "true"}.
     *
     * @param option name of the option.
     * @return The Properties mapped by the option, never {@code null} even if the option doesn't
     *     exists.
     * @since 1.5.0
     */
    public Properties getOptionProperties0(final Option option) {
        final Properties props = new Properties();

        for (final Option processedOption : options) {
            if (processedOption.equals(option)) {
                final List<String> values = processedOption.getValuesList();
                if (values.size() >= 2) {
                    props.put(values.get(0), values.get(1));
                } else if (values.size() == 1) {
                    props.put(values.get(0), "true");
                }
            }
        }

        return props;
    }

    /**
     * Retrieve the map of values associated to the option. This is convenient for options
     * specifying Java properties like <code>-Dparam1=value1
     * -Dparam2=value2</code>. The first argument of the option is the key, and the 2nd argument is
     * the value. If the option has only one argument ({@code -Dfoo}) it is considered as a boolean
     * flag and the value is {@code "true"}.
     *
     * @param opt name of the option.
     * @return The Properties mapped by the option, never {@code null} even if the option doesn't
     *     exists.
     * @since 1.2
     */
    public Properties getOptionProperties1(final String opt) {
        final Properties props = new Properties();

        for (final Option option : options) {
            if (opt.equals(option.getOpt()) || opt.equals(option.getLongOpt())) {
                final List<String> values = option.getValuesList();
                if (values.size() >= 2) {
                    props.put(values.get(0), values.get(1));
                } else if (values.size() == 1) {
                    props.put(values.get(0), "true");
                }
            }
        }

        return props;
    }

    /**
     * Gets an array of the processed {@link Option}s.
     *
     * @return an array of the processed {@link Option}s.
     */
    public Option[] getOptions() {
        final Collection<Option> processed = options;

        final Option[] optionsArray = new Option[processed.size()];

        return processed.toArray(optionsArray);
    }

    /**
     * Retrieve the first argument, if any, of this option.
     *
     * @param opt the character name of the option.
     * @return Value of the argument if option is set, and has an argument, otherwise null.
     */
    public String getOptionValue0(final char opt) {
        return getOptionValue4(String.valueOf(opt));
    }

    /**
     * Retrieve the argument, if any, of an option.
     *
     * @param opt character name of the option
     * @param defaultValue is the default value to be returned if the option is not specified.
     * @return Value of the argument if option is set, and has an argument, otherwise {@code
     *     defaultValue}.
     */
    public String getOptionValue1(final char opt, final String defaultValue) {
        return getOptionValue5(String.valueOf(opt), defaultValue);
    }

    /**
     * Retrieve the first argument, if any, of this option.
     *
     * @param option the name of the option.
     * @return Value of the argument if option is set, and has an argument, otherwise null.
     * @since 1.5.0
     */
    public String getOptionValue2(final Option option) {
        if (option == null) {
            return null;
        }
        final String[] values = getOptionValues1(option);
        return values == null ? null : values[0];
    }

    /**
     * Retrieve the first argument, if any, of an option.
     *
     * @param option name of the option.
     * @param defaultValue is the default value to be returned if the option is not specified.
     * @return Value of the argument if option is set, and has an argument, otherwise {@code
     *     defaultValue}.
     * @since 1.5.0
     */
    public String getOptionValue3(final Option option, final String defaultValue) {
        final String answer = getOptionValue2(option);
        return answer != null ? answer : defaultValue;
    }

    /**
     * Retrieve the first argument, if any, of this option.
     *
     * @param opt the name of the option.
     * @return Value of the argument if option is set, and has an argument, otherwise null.
     */
    public String getOptionValue4(final String opt) {
        return getOptionValue2(resolveOption(opt));
    }

    /**
     * Retrieve the first argument, if any, of an option.
     *
     * @param opt name of the option.
     * @param defaultValue is the default value to be returned if the option is not specified.
     * @return Value of the argument if option is set, and has an argument, otherwise {@code
     *     defaultValue}.
     */
    public String getOptionValue5(final String opt, final String defaultValue) {
        return getOptionValue3(resolveOption(opt), defaultValue);
    }

    /**
     * Retrieves the array of values, if any, of an option.
     *
     * @param opt character name of the option.
     * @return Values of the argument if option is set, and has an argument, otherwise null.
     */
    public String[] getOptionValues0(final char opt) {
        return getOptionValues2(String.valueOf(opt));
    }

    /**
     * Retrieves the array of values, if any, of an option.
     *
     * @param option string name of the option.
     * @return Values of the argument if option is set, and has an argument, otherwise null.
     * @since 1.5.0
     */
    public String[] getOptionValues1(final Option option) {
        final List<String> values = new ArrayList<>();

        for (final Option processedOption : options) {
            if (processedOption.equals(option)) {
                values.addAll(processedOption.getValuesList());
            }
        }

        return values.isEmpty() ? null : values.toArray(new String[values.size()]);
    }

    /**
     * Retrieves the array of values, if any, of an option.
     *
     * @param opt string name of the option.
     * @return Values of the argument if option is set, and has an argument, otherwise null.
     */
    public String[] getOptionValues2(final String opt) {
        return getOptionValues1(resolveOption(opt));
    }

    /**
     * Return a version of this {@code Option} converted to a particular type.
     *
     * @param opt the name of the option.
     * @return the value parsed into a particular object.
     * @throws ParseException if there are problems turning the option value into the desired type
     * @see PatternOptionBuilder
     * @since 1.5.0
     */
    public Object getParsedOptionValue0(final char opt) throws ParseException {
        return getParsedOptionValue2(String.valueOf(opt));
    }

    /**
     * Return a version of this {@code Option} converted to a particular type.
     *
     * @param option the name of the option.
     * @return the value parsed into a particular object.
     * @throws ParseException if there are problems turning the option value into the desired type
     * @see PatternOptionBuilder
     * @since 1.5.0
     */
    public Object getParsedOptionValue1(final Option option) throws ParseException {
        if (option == null) {
            return null;
        }
        final String res = getOptionValue2(option);
        if (res == null) {
            return null;
        }
        return TypeHandler.createValue1(res, option.getType());
    }

    /**
     * Return a version of this {@code Option} converted to a particular type.
     *
     * @param opt the name of the option.
     * @return the value parsed into a particular object.
     * @throws ParseException if there are problems turning the option value into the desired type
     * @see PatternOptionBuilder
     * @since 1.2
     */
    public Object getParsedOptionValue2(final String opt) throws ParseException {
        return getParsedOptionValue1(resolveOption(opt));
    }

    /**
     * jkeyes - commented out until it is implemented properly
     *
     * <p>Dump state, suitable for debugging.
     *
     * @return Stringified form of this object.
     */

    /*
     * public String toString() { StringBuilder buf = new StringBuilder();
     *
     * buf.append("[ CommandLine: [ options: "); buf.append(options.toString()); buf.append(" ] [ args: ");
     * buf.append(args.toString()); buf.append(" ] ]");
     *
     * return buf.toString(); }
     */

    /**
     * Tests to see if an option has been set.
     *
     * @param opt character name of the option.
     * @return true if set, false if not.
     */
    public boolean hasOption0(final char opt) {
        return hasOption2(String.valueOf(opt));
    }

    /**
     * Tests to see if an option has been set.
     *
     * @param opt the option to check.
     * @return true if set, false if not.
     * @since 1.5.0
     */
    public boolean hasOption1(final Option opt) {
        return options.contains(opt);
    }

    /**
     * Tests to see if an option has been set.
     *
     * @param opt Short name of the option.
     * @return true if set, false if not.
     */
    public boolean hasOption2(final String opt) {
        return hasOption1(resolveOption(opt));
    }

    /**
     * Returns an iterator over the Option members of CommandLine.
     *
     * @return an {@code Iterator} over the processed {@link Option} members of this {@link
     *     CommandLine}.
     */
    public Iterator<Option> iterator() {
        return options.iterator();
    }

    /**
     * Retrieves the option object given the long or short option as a String
     *
     * @param opt short or long name of the option.
     * @return Canonicalized option.
     */
    private Option resolveOption(String opt) {
        opt = Util.stripLeadingHyphens(opt);
        for (final Option option : options) {
            if (opt.equals(option.getOpt()) || opt.equals(option.getLongOpt())) {
                return option;
            }
        }
        return null;
    }
}
