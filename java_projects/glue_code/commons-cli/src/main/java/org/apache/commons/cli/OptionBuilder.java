package org.apache.commons.cli;

import org.graalvm.polyglot.PolyglotException;
import org.graalvm.polyglot.Value;

public final class OptionBuilder {
  private static final OptionBuilder INSTANCE = new OptionBuilder();
  private static int argCount = Option.UNINITIALIZED;
  private static Value clz =
      ContextInitializer.getPythonClass("/OptionBuilder.py", "OptionBuilder");
  private Value obj;

  public OptionBuilder(Value obj) {
    this.obj = obj;
  }

  public Value getPythonObject() {
    return obj;
  }

  public static OptionBuilder withType1(final Object newType) {
    //
    // return withType0((Class<?>) newType);
    //

    // TODO: Check the type mapping below!
    return clz.invokeMember("withType1", newType).as(OptionBuilder.class);
  }

  public static OptionBuilder withValueSeparator1(final char sep) {
    //
    // OptionBuilder.valueSeparator = sep;
    //
    // return INSTANCE;
    //

    // TODO: Check the type mapping below!
    return clz.invokeMember("withValueSeparator1", sep).as(OptionBuilder.class);
  }

  public static OptionBuilder withValueSeparator0() {
    //
    // OptionBuilder.valueSeparator = '=';
    //
    // return INSTANCE;
    //

    // TODO: Check the type mapping below!
    return clz.invokeMember("withValueSeparator0").as(OptionBuilder.class);
  }

  public static OptionBuilder withType0(final Class<?> newType) {
    //
    // OptionBuilder.type = newType;
    //
    // return INSTANCE;
    //

    // TODO: Check the type mapping below!
    return clz.invokeMember("withType0", newType).as(OptionBuilder.class);
  }

  public static OptionBuilder withLongOpt(final String newLongopt) {
    //
    // OptionBuilder.longOption = newLongopt;
    //
    // return INSTANCE;
    //

    // TODO: Check the type mapping below!
    return clz.invokeMember("withLongOpt", newLongopt).as(OptionBuilder.class);
  }

  public static OptionBuilder withDescription(final String newDescription) {
    //
    // OptionBuilder.description = newDescription;
    //
    // return INSTANCE;
    //

    // TODO: Check the type mapping below!
    return clz.invokeMember("withDescription", newDescription).as(OptionBuilder.class);
  }

  public static OptionBuilder withArgName(final String name) {
    //
    // OptionBuilder.argName = name;
    //
    // return INSTANCE;
    //

    // TODO: Check the type mapping below!
    return clz.invokeMember("withArgName", name).as(OptionBuilder.class);
  }

  public static OptionBuilder isRequired1(final boolean newRequired) {
    //
    // OptionBuilder.required = newRequired;
    //
    // return INSTANCE;
    //

    // TODO: Check the type mapping below!
    return clz.invokeMember("isRequired1", newRequired).as(OptionBuilder.class);
  }

  public static OptionBuilder isRequired0() {
    //
    // OptionBuilder.required = true;
    //
    // return INSTANCE;
    //

    // TODO: Check the type mapping below!
    return clz.invokeMember("isRequired0").as(OptionBuilder.class);
  }

  public static OptionBuilder hasOptionalArgs1(final int numArgs) {
    //
    // OptionBuilder.argCount = numArgs;
    // OptionBuilder.optionalArg = true;
    //
    // return INSTANCE;
    //

    // TODO: Check the type mapping below!
    return clz.invokeMember("hasOptionalArgs1", numArgs).as(OptionBuilder.class);
  }

  public static OptionBuilder hasOptionalArgs0() {
    //
    // OptionBuilder.argCount = Option.UNLIMITED_VALUES;
    // OptionBuilder.optionalArg = true;
    //
    // return INSTANCE;
    //

    // TODO: Check the type mapping below!
    return clz.invokeMember("hasOptionalArgs0").as(OptionBuilder.class);
  }

  public static OptionBuilder hasOptionalArg() {
    //
    // OptionBuilder.argCount = 1;
    // OptionBuilder.optionalArg = true;
    //
    // return INSTANCE;
    //

    // TODO: Check the type mapping below!
    return clz.invokeMember("hasOptionalArg").as(OptionBuilder.class);
  }

  public static OptionBuilder hasArgs1(final int num) {
    //
    // OptionBuilder.argCount = num;
    //
    // return INSTANCE;
    //

    // TODO: Check the type mapping below!
    return clz.invokeMember("hasArgs1", num).as(OptionBuilder.class);
  }

  public static OptionBuilder hasArgs0() {
    //
    // OptionBuilder.argCount = Option.UNLIMITED_VALUES;
    //
    // return INSTANCE;
    //

    // TODO: Check the type mapping below!
    return clz.invokeMember("hasArgs0").as(OptionBuilder.class);
  }

  public static OptionBuilder hasArg1(final boolean hasArg) {
    //
    // OptionBuilder.argCount = hasArg ? 1 : Option.UNINITIALIZED;
    //
    // return INSTANCE;
    //

    // TODO: Check the type mapping below!
    return clz.invokeMember("hasArg1", hasArg).as(OptionBuilder.class);
  }

  public static OptionBuilder hasArg0() {
    //
    // OptionBuilder.argCount = 1;
    //
    // return INSTANCE;
    //

    // TODO: Check the type mapping below!
    return clz.invokeMember("hasArg0").as(OptionBuilder.class);
  }

  public static Option create2(final String opt) throws IllegalArgumentException {
    try {
      //
      // Option option = null;
      // try {
      // option = Option.Option1(opt, description);
      //
      // option.setLongOpt(longOption);
      // option.setRequired(required);
      // option.setOptionalArg(optionalArg);
      // option.setArgs(argCount);
      // option.setType0(type);
      // option.setValueSeparator(valueSeparator);
      // option.setArgName(argName);
      // } finally {
      // OptionBuilder.reset();
      // }
      //
      // return option;
      //

      // TODO: Check the type mapping below!
      return clz.invokeMember("create2", opt).as(Option.class);
    } catch (PolyglotException e) {
      // TODO: Handle IllegalArgumentException
      throw (IllegalArgumentException) ExceptionHandler.handle(e, "OptionBuilder.create2");
    }
  }

  public static Option create1(final char opt) throws IllegalArgumentException {
    try {
      //
      // return create2(String.valueOf(opt));
      //

      // TODO: Check the type mapping below!
      return clz.invokeMember("create1", opt).as(Option.class);
    } catch (PolyglotException e) {
      // TODO: Handle IllegalArgumentException
      throw (IllegalArgumentException) ExceptionHandler.handle(e, "OptionBuilder.create1");
    }
  }

  public static Option create0() throws IllegalArgumentException {
    try {
      //
      // if (longOption == null) {
      // OptionBuilder.reset();
      // throw new IllegalArgumentException("must specify longopt");
      // }
      //
      // return create2(null);
      //

      // TODO: Check the type mapping below!
      return clz.invokeMember("create0").as(Option.class);
    } catch (PolyglotException e) {
      // TODO: Handle IllegalArgumentException
      throw (IllegalArgumentException) ExceptionHandler.handle(e, "OptionBuilder.create0");
    }
  }

  private OptionBuilder() {
    //

    this.obj = clz.invokeMember("__init__");
  }

  private static void reset() {
    //
    // description = null;
    // argName = null;
    // longOption = null;
    // type = String.class;
    // required = false;
    // argCount = Option.UNINITIALIZED;
    // optionalArg = false;
    // valueSeparator = (char) 0;
    //

    clz.invokeMember("reset");
  }
}
