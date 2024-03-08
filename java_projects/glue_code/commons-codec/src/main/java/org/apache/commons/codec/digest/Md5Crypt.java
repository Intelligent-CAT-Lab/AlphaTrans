package org.apache.commons.codec.digest;

import org.apache.commons.codec.ContextInitializer;
import org.graalvm.polyglot.Value;

public class Md5Crypt {
  static final String MD5_PREFIX = "$1$";
  static final String APR1_PREFIX = "$apr1$";
  private static final int ROUNDS = 1000;
  private static final int BLOCKSIZE = 16;
  private static Value clz = ContextInitializer.getPythonClass("/digest/Md5Crypt.py", "Md5Crypt");
  private Value obj;

  public Md5Crypt(Value obj) {
    this.obj = obj;
  }

  public Value getPythonObject() {
    return obj;
  }
}
