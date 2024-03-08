package org.apache.commons.codec.digest;

import java.util.Random;
import org.apache.commons.codec.ContextInitializer;
import org.graalvm.polyglot.Value;

class B64 {
  static final String B64T_STRING =
      "./0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz";
      static final char[] B64T_ARRAY = B64T_STRING.toCharArray();
  private static Value clz = ContextInitializer.getPythonClass("/digest/B64.py", "B64");
  private Value obj;

  public B64(Value obj) {
    this.obj = obj;
  }

  public Value getPythonObject() {
    return obj;
  }

  static String getRandomSalt(final int num, final Random random) {
    //
    // final StringBuilder saltString = new StringBuilder(num);
    // for (int i = 1; i <= num; i++) {
    // saltString.append(B64T_STRING.charAt(random.nextInt(B64T_STRING.length())));
    // }
    // return saltString.toString();
    //

    // TODO: Check the type mapping below!
    return clz.invokeMember("getRandomSalt", num, random).as(String.class);
  }

  static void b64from24bit(
      final byte b2, final byte b1, final byte b0, final int outLen, final StringBuilder buffer) {
    //
    // int w = ((b2 << 16) & 0x00ffffff) | ((b1 << 8) & 0x00ffff) | (b0 & 0xff);
    // int n = outLen;
    // while (n-- > 0) {
    // buffer.append(B64T_ARRAY[w & 0x3f]);
    // w >>= 6;
    // }
    //

    clz.invokeMember("b64from24bit", b2, b1, b0, outLen, buffer);
  }
}
