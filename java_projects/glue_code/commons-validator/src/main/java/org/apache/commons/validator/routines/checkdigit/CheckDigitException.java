package org.apache.commons.validator.routines.checkdigit;

import org.apache.commons.validator.ContextInitializer;
import org.graalvm.polyglot.Value;

public class CheckDigitException extends Exception {
  private static final long serialVersionUID = -3519894732624685477L;
  private static Value clz =
      ContextInitializer.getPythonClass(
          "/routines/checkdigit/CheckDigitException.py", "CheckDigitException");
  private Value obj;

  public CheckDigitException(Value obj) {
    this.obj = obj;
  }

  public Value getPythonObject() {
    return obj;
  }

  public static CheckDigitException CheckDigitException2() {
    //
    // return new CheckDigitException(null, null);
    //

    // TODO: Check the type mapping below!
    return clz.invokeMember("CheckDigitException2").as(CheckDigitException.class);
  }

  public static CheckDigitException CheckDigitException1(String msg) {
    //
    // return new CheckDigitException(msg, null);
    //

    // TODO: Check the type mapping below!
    return clz.invokeMember("CheckDigitException1", msg).as(CheckDigitException.class);
  }

  public CheckDigitException(String msg, Throwable cause) {
    //
    // super(msg, cause);
    //

    this.obj = clz.invokeMember("__init__", msg, cause);
  }
}
