package org.apache.commons.validator;

import org.graalvm.polyglot.Value;

public class ValidatorException extends Exception {
  private static final long serialVersionUID = 1025759372615616964L;
  private static Value clz =
      ContextInitializer.getPythonClass("/ValidatorException.py", "ValidatorException");
  private Value obj;

  public ValidatorException(Value obj) {
    this.obj = obj;
  }

  public Value getPythonObject() {
    return obj;
  }

  public static ValidatorException ValidatorException1() {
    //
    // return new ValidatorException(null);
    //

    // TODO: Check the type mapping below!
    return clz.invokeMember("ValidatorException1").as(ValidatorException.class);
  }

  public ValidatorException(String message) {
    //
    // super(message);
    //

    this.obj = clz.invokeMember("__init__", message);
  }
}
