package org.apache.commons.cli;

import org.graalvm.polyglot.Value;

public class MissingArgumentException extends ParseException {
  private static final long serialVersionUID = -7098538588704965017L;
  private static Value clz =
      ContextInitializer.getPythonClass("/MissingArgumentException.py", "MissingArgumentException");
  private Value obj;

  public MissingArgumentException(Value obj) {
    this.obj = obj;
  }

  public Value getPythonObject() {
    return obj;
  }

  public Option getOption() {
    //
    // return option;
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("getOption").as(Option.class);
  }

  public static MissingArgumentException MissingArgumentException1(
      int constructorId, final String message, final Option option) {
    //
    // if (constructorId == 1) {
    // return new MissingArgumentException(
    // constructorId, "Missing argument for option: " + option.getKey(), option);
    // }
    // return new MissingArgumentException(constructorId, message, option);
    //

    // TODO: Check the type mapping below!
    return clz.invokeMember("MissingArgumentException1", constructorId, message, option)
        .as(MissingArgumentException.class);
  }

  public MissingArgumentException(int constructorId, final String message, final Option option) {
    //
    //
    // super(message);
    // if (constructorId == 1) {
    // this.option = option;
    // }
    //

    this.obj = clz.invokeMember("__init__", constructorId, message, option);
  }
}
