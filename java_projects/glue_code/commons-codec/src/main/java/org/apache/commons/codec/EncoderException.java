package org.apache.commons.codec;

import org.graalvm.polyglot.Value;

public class EncoderException extends Exception {
  private static final long serialVersionUID = 1L;
  private static Value clz =
      ContextInitializer.getPythonClass("/EncoderException.py", "EncoderException");
  private Value obj;

  public EncoderException(Value obj) {
    this.obj = obj;
  }

  public Value getPythonObject() {
    return obj;
  }

  public EncoderException(final String message, final Throwable cause) {
    //
    // super(message, cause);
    //

    this.obj = clz.invokeMember("__init__", message, cause);
  }
}
