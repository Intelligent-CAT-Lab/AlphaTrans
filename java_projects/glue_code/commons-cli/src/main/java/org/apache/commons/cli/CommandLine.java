package org.apache.commons.cli;

import java.io.Serializable;
import java.util.ArrayList;
import java.util.Iterator;
import java.util.LinkedList;
import java.util.List;
import java.util.Properties;
import org.graalvm.polyglot.PolyglotException;
import org.graalvm.polyglot.Value;

public class CommandLine implements Serializable {
  private final List<Option> options = new ArrayList<>();
  private final List<String> args = new LinkedList<>();
  private static final long serialVersionUID = 1L;
  private static Value clz = ContextInitializer.getPythonClass("/CommandLine.py", "CommandLine");
  private Value obj;

  public CommandLine(Value obj) {
    this.obj = obj;
  }

  public Value getPythonObject() {
    return obj;
  }

  public Object getOptionObject1(final String opt) {
    //
    // try {
    // return getParsedOptionValue2(opt);
    // } catch (final ParseException pe) {
    // System.err.println(
    // "Exception found converting " + opt + " to desired type: " + pe.getMessage());
    // return null;
    // }
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("getOptionObject1", opt).as(Object.class);
  }

  public Object getOptionObject0(final char opt) {
    //
    // return getOptionObject1(String.valueOf(opt));
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("getOptionObject0", opt).as(Object.class);
  }

  public Iterator<Option> iterator() {
    //
    // return options.iterator();
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("iterator").as(Iterator.class);
  }

  public boolean hasOption2(final String opt) {
    //
    // return hasOption1(resolveOption(opt));
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("hasOption2", opt).as(boolean.class);
  }

  public boolean hasOption1(final Option opt) {
    //
    // return options.contains(opt);
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("hasOption1", opt).as(boolean.class);
  }

  public boolean hasOption0(final char opt) {
    //
    // return hasOption2(String.valueOf(opt));
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("hasOption0", opt).as(boolean.class);
  }

  public Object getParsedOptionValue2(final String opt) throws ParseException {
    try {
      //
      // return getParsedOptionValue1(resolveOption(opt));
      //

      // TODO: Check the type mapping below!
      return obj.invokeMember("getParsedOptionValue2", opt).as(Object.class);
    } catch (PolyglotException e) {
      // TODO: Handle ParseException
      throw (ParseException) ExceptionHandler.handle(e, "CommandLine.getParsedOptionValue2");
    }
  }

  public Object getParsedOptionValue1(final Option option) throws ParseException {
    try {
      //
      // if (option == null) {
      // return null;
      // }
      // final String res = getOptionValue2(option);
      // if (res == null) {
      // return null;
      // }
      // return TypeHandler.createValue1(res, option.getType());
      //

      // TODO: Check the type mapping below!
      return obj.invokeMember("getParsedOptionValue1", option).as(Object.class);
    } catch (PolyglotException e) {
      // TODO: Handle ParseException
      throw (ParseException) ExceptionHandler.handle(e, "CommandLine.getParsedOptionValue1");
    }
  }

  public Object getParsedOptionValue0(final char opt) throws ParseException {
    try {
      //
      // return getParsedOptionValue2(String.valueOf(opt));
      //

      // TODO: Check the type mapping below!
      return obj.invokeMember("getParsedOptionValue0", opt).as(Object.class);
    } catch (PolyglotException e) {
      // TODO: Handle ParseException
      throw (ParseException) ExceptionHandler.handle(e, "CommandLine.getParsedOptionValue0");
    }
  }

  public String[] getOptionValues2(final String opt) {
    //
    // return getOptionValues1(resolveOption(opt));
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("getOptionValues2", opt).as(String[].class);
  }

  public String[] getOptionValues1(final Option option) {
    //
    // final List<String> values = new ArrayList<>();
    //
    // for (final Option processedOption : options) {
    // if (processedOption.equals(option)) {
    // values.addAll(processedOption.getValuesList());
    // }
    // }
    //
    // return values.isEmpty() ? null : values.toArray(new String[values.size()]);
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("getOptionValues1", option).as(String[].class);
  }

  public String[] getOptionValues0(final char opt) {
    //
    // return getOptionValues2(String.valueOf(opt));
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("getOptionValues0", opt).as(String[].class);
  }

  public String getOptionValue5(final String opt, final String defaultValue) {
    //
    // return getOptionValue3(resolveOption(opt), defaultValue);
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("getOptionValue5", opt, defaultValue).as(String.class);
  }

  public String getOptionValue4(final String opt) {
    //
    // return getOptionValue2(resolveOption(opt));
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("getOptionValue4", opt).as(String.class);
  }

  public String getOptionValue3(final Option option, final String defaultValue) {
    //
    // final String answer = getOptionValue2(option);
    // return answer != null ? answer : defaultValue;
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("getOptionValue3", option, defaultValue).as(String.class);
  }

  public String getOptionValue2(final Option option) {
    //
    // if (option == null) {
    // return null;
    // }
    // final String[] values = getOptionValues1(option);
    // return values == null ? null : values[0];
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("getOptionValue2", option).as(String.class);
  }

  public String getOptionValue1(final char opt, final String defaultValue) {
    //
    // return getOptionValue5(String.valueOf(opt), defaultValue);
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("getOptionValue1", opt, defaultValue).as(String.class);
  }

  public String getOptionValue0(final char opt) {
    //
    // return getOptionValue4(String.valueOf(opt));
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("getOptionValue0", opt).as(String.class);
  }

  public Option[] getOptions() {
    //
    // final Collection<Option> processed = options;
    //
    // final Option[] optionsArray = new Option[processed.size()];
    //
    // return processed.toArray(optionsArray);
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("getOptions").as(Option[].class);
  }

  public Properties getOptionProperties1(final String opt) {
    //
    // final Properties props = new Properties();
    //
    // for (final Option option : options) {
    // if (opt.equals(option.getOpt()) || opt.equals(option.getLongOpt())) {
    // final List<String> values = option.getValuesList();
    // if (values.size() >= 2) {
    // props.put(values.get(0), values.get(1));
    // } else if (values.size() == 1) {
    // props.put(values.get(0), "true");
    // }
    // }
    // }
    //
    // return props;
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("getOptionProperties1", opt).as(Properties.class);
  }

  public Properties getOptionProperties0(final Option option) {
    //
    // final Properties props = new Properties();
    //
    // for (final Option processedOption : options) {
    // if (processedOption.equals(option)) {
    // final List<String> values = processedOption.getValuesList();
    // if (values.size() >= 2) {
    // props.put(values.get(0), values.get(1));
    // } else if (values.size() == 1) {
    // props.put(values.get(0), "true");
    // }
    // }
    // }
    //
    // return props;
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("getOptionProperties0", option).as(Properties.class);
  }

  public String[] getArgs() {
    //
    // final String[] answer = new String[args.size()];
    //
    // args.toArray(answer);
    //
    // return answer;
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("getArgs").as(String[].class);
  }

  public List<String> getArgList() {
    //
    // return args;
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("getArgList").as(List.class);
  }

  protected void addOption(final Option opt) {
    //
    // options.add(opt);
    //

    obj.invokeMember("addOption", opt);
  }

  protected void addArg(final String arg) {
    //
    // args.add(arg);
    //

    obj.invokeMember("addArg", arg);
  }

  protected CommandLine() {
    //

    this.obj = clz.invokeMember("__init__");
  }

  private Option resolveOption(String opt) {
    //
    // opt = Util.stripLeadingHyphens(opt);
    // for (final Option option : options) {
    // if (opt.equals(option.getOpt()) || opt.equals(option.getLongOpt())) {
    // return option;
    // }
    // }
    // return null;
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("resolveOption", opt).as(Option.class);
  }

  public static final class Builder {
    private final CommandLine commandLine = new CommandLine();
    private static Value clz = ContextInitializer.getPythonClass("/CommandLine.py", "Builder");
    private Value obj;

    public Builder(Value obj) {
      this.obj = obj;
    }

    public Value getPythonObject() {
      return obj;
    }

    public CommandLine build() {
      //
      // return commandLine;
      //

      // TODO: Check the type mapping below!
      return obj.invokeMember("build").as(CommandLine.class);
    }

    public Builder addOption(final Option opt) {
      //
      // commandLine.addOption(opt);
      // return this;
      //

      // TODO: Check the type mapping below!
      return obj.invokeMember("addOption", opt).as(Builder.class);
    }

    public Builder addArg(final String arg) {
      //
      // commandLine.addArg(arg);
      // return this;
      //

      // TODO: Check the type mapping below!
      return obj.invokeMember("addArg", arg).as(Builder.class);
    }
  }
}
