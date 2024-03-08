package org.apache.commons.codec.language;

import org.apache.commons.codec.ContextInitializer;
import org.apache.commons.codec.EncoderException;
import org.apache.commons.codec.ExceptionHandler;
import org.apache.commons.codec.StringEncoder;
import org.graalvm.polyglot.PolyglotException;
import org.graalvm.polyglot.Value;

public class Soundex implements StringEncoder {
  public static final Soundex US_ENGLISH_GENEALOGY =
      new Soundex(1, false, "-123-12--22455-12623-1-2-2", null);
  public static final Soundex US_ENGLISH_SIMPLIFIED =
      new Soundex(0, false, US_ENGLISH_MAPPING_STRING, null);
  public static final Soundex US_ENGLISH = new Soundex(3, false, null, null);
  public static final String US_ENGLISH_MAPPING_STRING = "01230120022455012623010202";
  public static final char SILENT_MARKER = '-';
  @Deprecated private int maxLength = 4;
  private static final char[] US_ENGLISH_MAPPING = US_ENGLISH_MAPPING_STRING.toCharArray();
  private static Value clz = ContextInitializer.getPythonClass("/language/Soundex.py", "Soundex");
  private Value obj;

  public Soundex(Value obj) {
    this.obj = obj;
  }

  public Value getPythonObject() {
    return obj;
  }

  public void setMaxLength(final int maxLength) {
    //
    // this.maxLength = maxLength;
    //

    obj.invokeMember("setMaxLength", maxLength);
  }

  public int getMaxLength() {
    //
    // return this.maxLength;
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("getMaxLength").as(int.class);
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
      throw (EncoderException) ExceptionHandler.handle(e, "Soundex.encode");
    }
  }

  public String soundex(String str) {
    //
    // if (str == null) {
    // return null;
    // }
    // str = SoundexUtils.clean(str);
    // if (str.isEmpty()) {
    // return str;
    // }
    // final char out[] = {'0', '0', '0', '0'};
    // int count = 0;
    // final char first = str.charAt(0);
    // out[count++] = first;
    // char lastDigit = map(first); // previous digit
    // for (int i = 1; i < str.length() && count < out.length; i++) {
    // final char ch = str.charAt(i);
    // if ((this.specialCaseHW) && (ch == 'H' || ch == 'W')) { // these are ignored completely
    // continue;
    // }
    // final char digit = map(ch);
    // if (digit == SILENT_MARKER) {
    // continue;
    // }
    // if (digit != '0' && digit != lastDigit) { // don't store vowels or repeats
    // out[count++] = digit;
    // }
    // lastDigit = digit;
    // }
    // return new String(out);
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("soundex", str).as(String.class);
  }

  public String encode1(final String str) {
    //
    // return soundex(str);
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("encode1", str).as(String.class);
  }

  public Object encode0(final Object obj) throws EncoderException {
    try {
      //
      // if (!(obj instanceof String)) {
      // throw new EncoderException(
      // "Parameter supplied to Soundex encode is not of type java.lang.String", null);
      // }
      // return soundex((String) obj);
      //

      // TODO: Check the type mapping below!
      return obj.invokeMember("encode0", obj).as(Object.class);
    } catch (PolyglotException e) {
      // TODO: Handle EncoderException
      throw (EncoderException) ExceptionHandler.handle(e, "Soundex.encode0");
    }
  }

  public int difference(final String s1, final String s2) throws EncoderException {
    try {
      //
      // return SoundexUtils.difference(this, s1, s2);
      //

      // TODO: Check the type mapping below!
      return obj.invokeMember("difference", s1, s2).as(int.class);
    } catch (PolyglotException e) {
      // TODO: Handle EncoderException
      throw (EncoderException) ExceptionHandler.handle(e, "Soundex.difference");
    }
  }

  public Soundex(
      int constructorId, final boolean specialCaseHW, final String mapping, final char[] mapping1) {
    //
    // if (constructorId == 0) {
    // this.soundexMapping = mapping.toCharArray();
    // this.specialCaseHW = specialCaseHW;
    // } else if (constructorId == 1) {
    // this.soundexMapping = mapping.toCharArray();
    // this.specialCaseHW = !hasMarker(this.soundexMapping);
    // } else if (constructorId == 2) {
    // this.soundexMapping = mapping1.clone();
    // this.specialCaseHW = !hasMarker(this.soundexMapping);
    // } else {
    // this.soundexMapping = US_ENGLISH_MAPPING;
    // this.specialCaseHW = true;
    // }
    //

    this.obj = clz.invokeMember("__init__", constructorId, specialCaseHW, mapping, mapping1);
  }

  private char map(final char ch) {
    //
    // final int index = ch - 'A';
    // if (index < 0 || index >= this.soundexMapping.length) {
    // throw new IllegalArgumentException(
    // "The character is not mapped: " + ch + " (index=" + index + ")");
    // }
    // return this.soundexMapping[index];
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("map", ch).as(char.class);
  }

  private boolean hasMarker(final char[] mapping) {
    //
    // for (final char ch : mapping) {
    // if (ch == SILENT_MARKER) {
    // return true;
    // }
    // }
    // return false;
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("hasMarker", mapping).as(boolean.class);
  }
}
