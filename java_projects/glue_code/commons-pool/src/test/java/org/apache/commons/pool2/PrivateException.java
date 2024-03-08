package org.apache.commons.pool;

import org.graalvm.polyglot.Value;

public class PrivateException extends RuntimeException {
  private static final long serialVersionUID = 1L;
  private static Value clz =
      ContextInitializer.getPythonClass("/PrivateException.py", "PrivateException");
  private Value obj;

  public PrivateException(Value obj) {
    this.obj = obj;
  }

  public Value getPythonObject() {
    return obj;
  }

  public PrivateException(final String message) {
    //
    // super(message);
    //

    this.obj = clz.invokeMember("__init__", message);
  }
}
