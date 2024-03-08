package org.apache.commons.cli;

import org.graalvm.polyglot.Value;

public class ParseException extends Exception {
  private static final long serialVersionUID = 9112808380089253192L;
  private static Value clz =
      ContextInitializer.getPythonClass("/ParseException.py", "ParseException");
  private Value obj;

  public ParseException(Value obj) {
    this.obj = obj;
  }

  public Value getPythonObject() {
    return obj;
  }

  public ParseException(final String message) {
    //
    // super(message);
    //

    this.obj = clz.invokeMember("__init__", message);
  }
}
