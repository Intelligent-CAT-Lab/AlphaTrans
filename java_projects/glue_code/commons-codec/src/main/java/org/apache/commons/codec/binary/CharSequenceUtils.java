package org.apache.commons.codec.binary;

import org.apache.commons.codec.ContextInitializer;
import org.graalvm.polyglot.Value;

public class CharSequenceUtils {
  private static Value clz =
      ContextInitializer.getPythonClass("/binary/CharSequenceUtils.py", "CharSequenceUtils");
  private Value obj;

  public CharSequenceUtils(Value obj) {
    this.obj = obj;
  }

  public Value getPythonObject() {
    return obj;
  }

  static boolean regionMatches(
      final CharSequence cs,
      final boolean ignoreCase,
      final int thisStart,
      final CharSequence substring,
      final int start,
      final int length) {
    //
    // if (cs instanceof String && substring instanceof String) {
    // return ((String) cs)
    // .regionMatches(ignoreCase, thisStart, (String) substring, start, length);
    // }
    // int index1 = thisStart;
    // int index2 = start;
    // int tmpLen = length;
    //
    // while (tmpLen-- > 0) {
    // final char c1 = cs.charAt(index1++);
    // final char c2 = substring.charAt(index2++);
    //
    // if (c1 == c2) {
    // continue;
    // }
    //
    // if (!ignoreCase) {
    // return false;
    // }
    //
    // if (Character.toUpperCase(c1) != Character.toUpperCase(c2)
    // && Character.toLowerCase(c1) != Character.toLowerCase(c2)) {
    // return false;
    // }
    // }
    //
    // return true;
    //

    // TODO: Check the type mapping below!
    return clz.invokeMember("regionMatches", cs, ignoreCase, thisStart, substring, start, length)
        .as(boolean.class);
  }
}
