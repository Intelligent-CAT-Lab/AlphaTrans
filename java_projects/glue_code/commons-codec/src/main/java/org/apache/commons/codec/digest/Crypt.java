package org.apache.commons.codec.digest;

import org.apache.commons.codec.ContextInitializer;
import org.graalvm.polyglot.Value;

public class Crypt {
  private static Value clz = ContextInitializer.getPythonClass("/digest/Crypt.py", "Crypt");
  private Value obj;

  public Crypt(Value obj) {
    this.obj = obj;
  }

  public Value getPythonObject() {
    return obj;
  }
}
