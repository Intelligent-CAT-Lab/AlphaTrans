package org.apache.commons.codec.language;

import org.apache.commons.codec.ContextInitializer;
import org.apache.commons.codec.EncoderException;
import org.apache.commons.codec.ExceptionHandler;
import org.apache.commons.codec.StringEncoder;
import org.graalvm.polyglot.PolyglotException;
import org.graalvm.polyglot.Value;

final class SoundexUtils {
  private static Value clz =
      ContextInitializer.getPythonClass("/language/SoundexUtils.py", "SoundexUtils");
  private Value obj;

  public SoundexUtils(Value obj) {
    this.obj = obj;
  }

  public Value getPythonObject() {
    return obj;
  }

  static int differenceEncoded(final String es1, final String es2) {
    //
    //
    // if (es1 == null || es2 == null) {
    // return 0;
    // }
    // final int lengthToMatch = Math.min(es1.length(), es2.length());
    // int diff = 0;
    // for (int i = 0; i < lengthToMatch; i++) {
    // if (es1.charAt(i) == es2.charAt(i)) {
    // diff++;
    // }
    // }
    // return diff;
    //

    // TODO: Check the type mapping below!
    return clz.invokeMember("differenceEncoded", es1, es2).as(int.class);
  }

  static int difference(final StringEncoder encoder, final String s1, final String s2)
      throws EncoderException {
    try {
      //
      // return differenceEncoded(encoder.encode(s1), encoder.encode(s2));
      //

      // TODO: Check the type mapping below!
      return clz.invokeMember("difference", encoder, s1, s2).as(int.class);
    } catch (PolyglotException e) {
      // TODO: Handle EncoderException
      throw (EncoderException) ExceptionHandler.handle(e, "SoundexUtils.difference");
    }
  }

  static String clean(final String str) {
    //
    // if (str == null || str.isEmpty()) {
    // return str;
    // }
    // final int len = str.length();
    // final char[] chars = new char[len];
    // int count = 0;
    // for (int i = 0; i < len; i++) {
    // if (Character.isLetter(str.charAt(i))) {
    // chars[count++] = str.charAt(i);
    // }
    // }
    // if (count == len) {
    // return str.toUpperCase(java.util.Locale.ENGLISH);
    // }
    // return new String(chars, 0, count).toUpperCase(java.util.Locale.ENGLISH);
    //

    // TODO: Check the type mapping below!
    return clz.invokeMember("clean", str).as(String.class);
  }
}
