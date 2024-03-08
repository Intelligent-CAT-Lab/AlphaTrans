package org.apache.commons.codec;

import org.graalvm.polyglot.Value;

public class CharEncoding {
  public static final String UTF_8 = "UTF-8";
  public static final String UTF_16LE = "UTF-16LE";
  public static final String UTF_16BE = "UTF-16BE";
  public static final String UTF_16 = "UTF-16";
  public static final String US_ASCII = "US-ASCII";
  public static final String ISO_8859_1 = "ISO-8859-1";
  private static Value clz = ContextInitializer.getPythonClass("/CharEncoding.py", "CharEncoding");
  private Value obj;

  public CharEncoding(Value obj) {
    this.obj = obj;
  }

  public Value getPythonObject() {
    return obj;
  }
}
