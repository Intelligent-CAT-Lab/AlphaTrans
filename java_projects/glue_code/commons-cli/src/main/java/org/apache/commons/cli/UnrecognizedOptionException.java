package org.apache.commons.cli;

import org.graalvm.polyglot.Value;

public class UnrecognizedOptionException extends ParseException {
  private static final long serialVersionUID = -252504690284625623L;
  private static Value clz =
      ContextInitializer.getPythonClass(
          "/UnrecognizedOptionException.py", "UnrecognizedOptionException");
  private Value obj;

  public UnrecognizedOptionException(Value obj) {
    super(obj);
    this.obj = obj;
  }

  public Value getPythonObject() {
    return obj;
  }

  public String getOption() {
    //
    // return option;
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("getOption").as(String.class);
  }

  public static UnrecognizedOptionException UnrecognizedOptionException1(final String message) {
    //
    // return new UnrecognizedOptionException(message, null);
    //

    // TODO: Check the type mapping below!
    return clz.invokeMember("UnrecognizedOptionException1", message)
        .as(UnrecognizedOptionException.class);
  }

  public UnrecognizedOptionException(final String message, final String option) {
    super(message);
    // this.option = option;
    //

    this.obj = clz.invokeMember("__init__", message, option);
  }
}
