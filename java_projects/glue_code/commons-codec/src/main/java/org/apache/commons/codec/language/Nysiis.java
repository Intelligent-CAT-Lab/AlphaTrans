package org.apache.commons.codec.language;

import java.util.regex.Pattern;
import org.apache.commons.codec.ContextInitializer;
import org.apache.commons.codec.EncoderException;
import org.apache.commons.codec.ExceptionHandler;
import org.apache.commons.codec.StringEncoder;
import org.graalvm.polyglot.PolyglotException;
import org.graalvm.polyglot.Value;

public class Nysiis implements StringEncoder {
  private static final int TRUE_LENGTH = 6;
  private static final char SPACE = ' ';
  private static final Pattern PAT_DT_ETC = Pattern.compile("(DT|RT|RD|NT|ND)$");
  private static final Pattern PAT_EE_IE = Pattern.compile("(EE|IE)$");
  private static final Pattern PAT_SCH = Pattern.compile("^SCH");
  private static final Pattern PAT_PH_PF = Pattern.compile("^(PH|PF)");
  private static final Pattern PAT_K = Pattern.compile("^K");
  private static final Pattern PAT_KN = Pattern.compile("^KN");
  private static final Pattern PAT_MAC = Pattern.compile("^MAC");
  private static final char[] CHARS_SSS = {'S', 'S', 'S'};
  private static final char[] CHARS_S = {'S'};
  private static final char[] CHARS_NN = {'N', 'N'};
  private static final char[] CHARS_N = {'N'};
  private static final char[] CHARS_G = {'G'};
  private static final char[] CHARS_FF = {'F', 'F'};
  private static final char[] CHARS_C = {'C'};
  private static final char[] CHARS_AF = {'A', 'F'};
  private static final char[] CHARS_A = {'A'};
  private static Value clz = ContextInitializer.getPythonClass("/language/Nysiis.py", "Nysiis");
  private Value obj;

  public Nysiis(Value obj) {
    this.obj = obj;
  }

  public Value getPythonObject() {
    return obj;
  }

  public String encode(final String str) {
    //
    // return encode1(str);
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("encode", str).as(String.class);
  }

  public Object encode(final Object obj) throws EncoderException {
    try {
      //
      // return encode0(obj);
      //

      // TODO: Check the type mapping below!
      return obj.invokeMember("encode", obj).as(Object.class);
    } catch (PolyglotException e) {
      // TODO: Handle EncoderException
      throw (EncoderException) ExceptionHandler.handle(e, "Nysiis.encode");
    }
  }

  public String nysiis(String str) {
    //
    // if (str == null) {
    // return null;
    // }
    //
    // str = SoundexUtils.clean(str);
    //
    // if (str.isEmpty()) {
    // return str;
    // }
    //
    // str = PAT_MAC.matcher(str).replaceFirst("MCC");
    // str = PAT_KN.matcher(str).replaceFirst("NN");
    // str = PAT_K.matcher(str).replaceFirst("C");
    // str = PAT_PH_PF.matcher(str).replaceFirst("FF");
    // str = PAT_SCH.matcher(str).replaceFirst("SSS");
    //
    // str = PAT_EE_IE.matcher(str).replaceFirst("Y");
    // str = PAT_DT_ETC.matcher(str).replaceFirst("D");
    //
    // final StringBuilder key = new StringBuilder(str.length());
    // key.append(str.charAt(0));
    //
    // final char[] chars = str.toCharArray();
    // final int len = chars.length;
    //
    // for (int i = 1; i < len; i++) {
    // final char next = i < len - 1 ? chars[i + 1] : SPACE;
    // final char aNext = i < len - 2 ? chars[i + 2] : SPACE;
    // final char[] transcoded = transcodeRemaining(chars[i - 1], chars[i], next, aNext);
    // System.arraycopy(transcoded, 0, chars, i, transcoded.length);
    //
    // if (chars[i] != chars[i - 1]) {
    // key.append(chars[i]);
    // }
    // }
    //
    // if (key.length() > 1) {
    // char lastChar = key.charAt(key.length() - 1);
    //
    // if (lastChar == 'S') {
    // key.deleteCharAt(key.length() - 1);
    // lastChar = key.charAt(key.length() - 1);
    // }
    //
    // if (key.length() > 2) {
    // final char last2Char = key.charAt(key.length() - 2);
    // if (last2Char == 'A' && lastChar == 'Y') {
    // key.deleteCharAt(key.length() - 2);
    // }
    // }
    //
    // if (lastChar == 'A') {
    // key.deleteCharAt(key.length() - 1);
    // }
    // }
    //
    // final String string = key.toString();
    // return this.isStrict()
    // ? string.substring(0, Math.min(TRUE_LENGTH, string.length()))
    // : string;
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("nysiis", str).as(String.class);
  }

  public boolean isStrict() {
    //
    // return this.strict;
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("isStrict").as(boolean.class);
  }

  public String encode1(final String str) {
    //
    // return this.nysiis(str);
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("encode1", str).as(String.class);
  }

  public Object encode0(final Object obj) throws EncoderException {
    try {
      //
      // if (!(obj instanceof String)) {
      // throw new EncoderException(
      // "Parameter supplied to Nysiis encode is not of type java.lang.String", null);
      // }
      // return this.nysiis((String) obj);
      //

      // TODO: Check the type mapping below!
      return obj.invokeMember("encode0", obj).as(Object.class);
    } catch (PolyglotException e) {
      // TODO: Handle EncoderException
      throw (EncoderException) ExceptionHandler.handle(e, "Nysiis.encode0");
    }
  }

  public static Nysiis Nysiis1() {
    //
    // return new Nysiis(true);
    //

    // TODO: Check the type mapping below!
    return clz.invokeMember("Nysiis1").as(Nysiis.class);
  }

  public Nysiis(final boolean strict) {
    //
    // this.strict = strict;
    //

    this.obj = clz.invokeMember("__init__", strict);
  }

  private static char[] transcodeRemaining(
      final char prev, final char curr, final char next, final char aNext) {
    //
    // if (curr == 'E' && next == 'V') {
    // return CHARS_AF;
    // }
    //
    // if (isVowel(curr)) {
    // return CHARS_A;
    // }
    //
    // switch (curr) {
    // case 'Q':
    // return CHARS_G;
    // case 'Z':
    // return CHARS_S;
    // case 'M':
    // return CHARS_N;
    // case 'K':
    // if (next == 'N') {
    // return CHARS_NN;
    // }
    // return CHARS_C;
    // default:
    // break;
    // }
    //
    // if (curr == 'S' && next == 'C' && aNext == 'H') {
    // return CHARS_SSS;
    // }
    //
    // if (curr == 'P' && next == 'H') {
    // return CHARS_FF;
    // }
    //
    // if (curr == 'H' && (!isVowel(prev) || !isVowel(next))) {
    // return new char[] {prev};
    // }
    //
    // if (curr == 'W' && isVowel(prev)) {
    // return new char[] {prev};
    // }
    //
    // return new char[] {curr};
    //

    // TODO: Check the type mapping below!
    return clz.invokeMember("transcodeRemaining", prev, curr, next, aNext).as(char[].class);
  }

  private static boolean isVowel(final char c) {
    //
    // return c == 'A' || c == 'E' || c == 'I' || c == 'O' || c == 'U';
    //

    // TODO: Check the type mapping below!
    return clz.invokeMember("isVowel", c).as(boolean.class);
  }
}
