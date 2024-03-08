package org.apache.commons.codec.digest;

import java.util.regex.Pattern;
import org.apache.commons.codec.ContextInitializer;
import org.graalvm.polyglot.Value;

public class Sha2Crypt {
  static final String SHA512_PREFIX = "$6$";
  static final String SHA256_PREFIX = "$5$";
  private static final Pattern SALT_PATTERN =
      Pattern.compile("^\\$([56])\\$(rounds=(\\d+)\\$)?([\\.\\/a-zA-Z0-9]{1,16}).*");
  private static final int SHA512_BLOCKSIZE = 64;
  private static final int SHA256_BLOCKSIZE = 32;
  private static final String ROUNDS_PREFIX = "rounds=";
  private static final int ROUNDS_MIN = 1000;
  private static final int ROUNDS_MAX = 999999999;
  private static final int ROUNDS_DEFAULT = 5000;
  private static Value clz = ContextInitializer.getPythonClass("/digest/Sha2Crypt.py", "Sha2Crypt");
  private Value obj;

  public Sha2Crypt(Value obj) {
    this.obj = obj;
  }

  public Value getPythonObject() {
    return obj;
  }
}
