package org.joda.money;

import org.graalvm.polyglot.Value;

public class IllegalCurrencyException extends IllegalArgumentException {
  private static final long serialVersionUID = 1L;
  private static Value clz =
      ContextInitializer.getPythonClass("/IllegalCurrencyException.py", "IllegalCurrencyException");
  private Value obj;

  public IllegalCurrencyException(Value obj) {
    this.obj = obj;
  }

  public Value getPythonObject() {
    return obj;
  }

  public IllegalCurrencyException(String message) {
    //
    // super(message);
    //

    this.obj = clz.invokeMember("__init__", message);
  }
}
