package org.apache.commons.cli;

import java.util.List;
import java.util.ListIterator;
import java.util.Properties;
import org.graalvm.polyglot.PolyglotException;
import org.graalvm.polyglot.Value;

public abstract class Parser implements CommandLineParser {
  private static Value clz = ContextInitializer.getPythonClass("/Parser.py", "Parser");
  private Value obj;

  public Parser(Value obj) {
    this.obj = obj;
  }

  public Parser(){
    this.obj = clz.newInstance();
  }

  public Value getPythonObject() {
    return obj;
  }

  protected void setOptions(final Options options) {
    //
    // this.options = options;
    // this.requiredOptions = new ArrayList<>(options.getRequiredOptions());
    //

    obj.invokeMember("setOptions", options);
  }

  protected void processProperties(final Properties properties) throws ParseException {
    try {
      //
      // if (properties == null) {
      // return;
      // }
      //
      // for (final Enumeration<?> e = properties.propertyNames(); e.hasMoreElements(); ) {
      // final String option = e.nextElement().toString();
      //
      // final Option opt = options.getOption(option);
      // if (opt == null) {
      // throw new UnrecognizedOptionException("Default option wasn't defined", option);
      // }
      //
      // final OptionGroup group = options.getOptionGroup(opt);
      // final boolean selected = group != null && group.getSelected() != null;
      //
      // if (!cmd.hasOption2(option) && !selected) {
      // final String value = properties.getProperty(option);
      //
      // if (opt.hasArg()) {
      // if (opt.getValues() == null || opt.getValues().length == 0) {
      // try {
      // opt.addValueForProcessing(value);
      // } catch (final RuntimeException exp) { // NOPMD
      // }
      // }
      // } else if (!("yes".equalsIgnoreCase(value)
      // || "true".equalsIgnoreCase(value)
      // || "1".equalsIgnoreCase(value))) {
      // continue;
      // }
      //
      // cmd.addOption(opt);
      // updateRequiredOptions(opt);
      // }
      // }
      //

      obj.invokeMember("processProperties", properties);
    } catch (PolyglotException e) {
      // TODO: Handle ParseException
      throw (ParseException) ExceptionHandler.handle(e, "Parser.processProperties");
    }
  }

  protected void processOption(final String arg, final ListIterator<String> iter)
      throws ParseException {
    try {
      //
      // final boolean hasOption = getOptions().hasOption(arg);
      //
      // if (!hasOption) {
      // throw new UnrecognizedOptionException("Unrecognized option: " + arg, arg);
      // }
      //
      // final Option opt = (Option) getOptions().getOption(arg).clone();
      //
      // updateRequiredOptions(opt);
      //
      // if (opt.hasArg()) {
      // processArgs(opt, iter);
      // }
      //
      // cmd.addOption(opt);
      //

      obj.invokeMember("processOption", arg, iter);
    } catch (PolyglotException e) {
      // TODO: Handle ParseException
      throw (ParseException) ExceptionHandler.handle(e, "Parser.processOption");
    }
  }

  public void processArgs(final Option opt, final ListIterator<String> iter) throws ParseException {
    try {
      //
      // while (iter.hasNext()) {
      // final String str = iter.next();
      //
      // if (getOptions().hasOption(str) && str.startsWith("-")) {
      // iter.previous();
      // break;
      // }
      //
      // try {
      // opt.addValueForProcessing(Util.stripLeadingAndTrailingQuotes(str));
      // } catch (final RuntimeException exp) {
      // iter.previous();
      // break;
      // }
      // }
      //
      // if (opt.getValues() == null && !opt.hasOptionalArg()) {
      // throw MissingArgumentException.MissingArgumentException1(1, null, opt);
      // }
      //

      obj.invokeMember("processArgs", opt, iter);
    } catch (PolyglotException e) {
      // TODO: Handle ParseException
      throw (ParseException) ExceptionHandler.handle(e, "Parser.processArgs");
    }
  }

  public CommandLine parse3(
      final Options options,
      String[] arguments,
      final Properties properties,
      final boolean stopAtNonOption)
      throws ParseException {
    try {
      //
      // for (final Option opt : options.helpOptions()) {
      // opt.clearValues();
      // }
      //
      // for (final OptionGroup group : options.getOptionGroups()) {
      // group.setSelected(null);
      // }
      //
      // setOptions(options);
      //
      // cmd = new CommandLine();
      //
      // boolean eatTheRest = false;
      //
      // if (arguments == null) {
      // arguments = new String[0];
      // }
      //
      // final List<String> tokenList =
      // Arrays.asList(flatten(getOptions(), arguments, stopAtNonOption));
      //
      // final ListIterator<String> iterator = tokenList.listIterator();
      //
      // while (iterator.hasNext()) {
      // final String t = iterator.next();
      //
      // if ("--".equals(t)) {
      // eatTheRest = true;
      // } else if ("-".equals(t)) {
      // if (stopAtNonOption) {
      // eatTheRest = true;
      // } else {
      // cmd.addArg(t);
      // }
      // } else if (t.startsWith("-")) {
      // if (stopAtNonOption && !getOptions().hasOption(t)) {
      // eatTheRest = true;
      // cmd.addArg(t);
      // } else {
      // processOption(t, iterator);
      // }
      // } else {
      // cmd.addArg(t);
      //
      // if (stopAtNonOption) {
      // eatTheRest = true;
      // }
      // }
      //
      // if (eatTheRest) {
      // while (iterator.hasNext()) {
      // final String str = iterator.next();
      //
      // if (!"--".equals(str)) {
      // cmd.addArg(str);
      // }
      // }
      // }
      // }
      //
      // processProperties(properties);
      // checkRequiredOptions();
      //
      // return cmd;
      //

      // TODO: Check the type mapping below!
      return obj.invokeMember("parse3", options, arguments, properties, stopAtNonOption)
          .as(CommandLine.class);
    } catch (PolyglotException e) {
      // TODO: Handle ParseException
      throw (ParseException) ExceptionHandler.handle(e, "Parser.parse3");
    }
  }

  public CommandLine parse2(
      final Options options, final String[] arguments, final Properties properties)
      throws ParseException {
    try {
      //
      // return parse3(options, arguments, properties, false);
      //

      // TODO: Check the type mapping below!
      return obj.invokeMember("parse2", options, arguments, properties).as(CommandLine.class);
    } catch (PolyglotException e) {
      // TODO: Handle ParseException
      throw (ParseException) ExceptionHandler.handle(e, "Parser.parse2");
    }
  }

  public CommandLine parse1(
      final Options options, final String[] arguments, final boolean stopAtNonOption)
      throws ParseException {
    try {
      //
      // return parse3(options, arguments, null, stopAtNonOption);
      //

      // TODO: Check the type mapping below!
      return obj.invokeMember("parse1", options, arguments, stopAtNonOption).as(CommandLine.class);
    } catch (PolyglotException e) {
      // TODO: Handle ParseException
      throw (ParseException) ExceptionHandler.handle(e, "Parser.parse1");
    }
  }

  public CommandLine parse0(final Options options, final String[] arguments) throws ParseException {
    try {
      //
      // return parse3(options, arguments, null, false);
      //

      // TODO: Check the type mapping below!
      return obj.invokeMember("parse0", options, arguments).as(CommandLine.class);
    } catch (PolyglotException e) {
      // TODO: Handle ParseException
      throw (ParseException) ExceptionHandler.handle(e, "Parser.parse0");
    }
  }

  protected List getRequiredOptions() {
    //
    // return requiredOptions;
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("getRequiredOptions").as(List.class);
  }

  protected Options getOptions() {
    //
    // return options;
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("getOptions").as(Options.class);
  }

  protected void checkRequiredOptions() throws MissingOptionException {
    try {
      //
      // if (!getRequiredOptions().isEmpty()) {
      // throw MissingOptionException.MissingOptionException1(1, getRequiredOptions(), null);
      // }
      //

      obj.invokeMember("checkRequiredOptions");
    } catch (PolyglotException e) {
      // TODO: Handle MissingOptionException
      throw (MissingOptionException) ExceptionHandler.handle(e, "Parser.checkRequiredOptions");
    }
  }

  private void updateRequiredOptions(final Option opt) throws ParseException {
    try {
      //
      // if (opt.isRequired()) {
      // getRequiredOptions().remove(opt.getKey());
      // }
      //
      // if (getOptions().getOptionGroup(opt) != null) {
      // final OptionGroup group = getOptions().getOptionGroup(opt);
      //
      // if (group.isRequired()) {
      // getRequiredOptions().remove(group);
      // }
      //
      // group.setSelected(opt);
      // }
      //

      obj.invokeMember("updateRequiredOptions", opt);
    } catch (PolyglotException e) {
      // TODO: Handle ParseException
      throw (ParseException) ExceptionHandler.handle(e, "Parser.updateRequiredOptions");
    }
  }

  protected abstract String[] flatten(Options opts, String[] arguments, boolean stopAtNonOption) throws ParseException;
}
