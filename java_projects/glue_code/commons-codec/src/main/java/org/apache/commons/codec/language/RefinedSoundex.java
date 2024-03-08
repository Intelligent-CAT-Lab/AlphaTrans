package org.apache.commons.codec.language;

import org.apache.commons.codec.ContextInitializer;
import org.apache.commons.codec.EncoderException;
import org.apache.commons.codec.ExceptionHandler;
import org.apache.commons.codec.StringEncoder;
import org.graalvm.polyglot.PolyglotException;
import org.graalvm.polyglot.Value;

public class RefinedSoundex implements StringEncoder {
  public static final RefinedSoundex US_ENGLISH = new RefinedSoundex(2, null, null);
  public static final String US_ENGLISH_MAPPING_STRING = "01360240043788015936020505";
  private static final char[] US_ENGLISH_MAPPING = US_ENGLISH_MAPPING_STRING.toCharArray();
  private static Value clz =
      ContextInitializer.getPythonClass("/language/RefinedSoundex.py", "RefinedSoundex");
  private Value obj;

  public RefinedSoundex(Value obj) {
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
      throw (EncoderException) ExceptionHandler.handle(e, "RefinedSoundex.encode");
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
    //
    // final StringBuilder sBuf = new StringBuilder();
    // sBuf.append(str.charAt(0));
    //
    // char last, current;
    // last = '*';
    //
    // for (int i = 0; i < str.length(); i++) {
    //
    // current = getMappingCode(str.charAt(i));
    // if (current == last) {
    // continue;
    // }
    // if (current != 0) {
    // sBuf.append(current);
    // }
    //
    // last = current;
    // }
    //
    // return sBuf.toString();
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
      // "Parameter supplied to RefinedSoundex encode is not of type java.lang.String",
      // null);
      // }
      // return soundex((String) obj);
      //

      // TODO: Check the type mapping below!
      return obj.invokeMember("encode0", obj).as(Object.class);
    } catch (PolyglotException e) {
      // TODO: Handle EncoderException
      throw (EncoderException) ExceptionHandler.handle(e, "RefinedSoundex.encode0");
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
      throw (EncoderException) ExceptionHandler.handle(e, "RefinedSoundex.difference");
    }
  }

  public RefinedSoundex(int constructorId, final String mapping, final char[] mapping1) {
    //
    // if (constructorId == 0) {
    // this.soundexMapping = mapping.toCharArray();
    // } else if (constructorId == 1) {
    // this.soundexMapping = mapping1.clone();
    // } else {
    // this.soundexMapping = US_ENGLISH_MAPPING;
    // }
    //

    this.obj = clz.invokeMember("__init__", constructorId, mapping, mapping1);
  }

  char getMappingCode(final char c) {
    //
    // if (!Character.isLetter(c)) {
    // return 0;
    // }
    // return this.soundexMapping[Character.toUpperCase(c) - 'A'];
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("getMappingCode", c).as(char.class);
  }
}
