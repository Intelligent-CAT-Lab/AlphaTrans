package org.apache.commons.codec.digest;

import org.apache.commons.codec.ContextInitializer;
import org.graalvm.polyglot.Value;

public final class HmacUtils {
  private static final int STREAM_BUFFER_LENGTH = 1024;
  private static Value clz = ContextInitializer.getPythonClass("/digest/HmacUtils.py", "HmacUtils");
  private Value obj;

  public HmacUtils(Value obj) {
    this.obj = obj;
  }

  public Value getPythonObject() {
    return obj;
  }
}
