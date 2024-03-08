package org.apache.commons.codec;

import org.graalvm.polyglot.Value;

public class DecoderException extends Exception {
  private static final long serialVersionUID = 1L;
  private static Value clz =
      ContextInitializer.getPythonClass("/DecoderException.py", "DecoderException");
  private Value obj;

  public DecoderException(Value obj) {
    this.obj = obj;
  }

  public Value getPythonObject() {
    return obj;
  }

  public DecoderException(final String message, final Throwable cause) {
    //
    // super(message, cause);
    //

    this.obj = clz.invokeMember("__init__", message, cause);
  }
}
