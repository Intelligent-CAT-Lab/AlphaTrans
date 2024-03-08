package org.apache.commons.codec.language;

import org.apache.commons.codec.ContextInitializer;
import org.apache.commons.codec.EncoderException;
import org.apache.commons.codec.ExceptionHandler;
import org.apache.commons.codec.StringEncoder;
import org.graalvm.polyglot.PolyglotException;
import org.graalvm.polyglot.Value;

public class Caverphone implements StringEncoder {
  private final Caverphone2 encoder = new Caverphone2();
  private static Value clz =
      ContextInitializer.getPythonClass("/language/Caverphone.py", "Caverphone");
  private Value obj;

  public Caverphone(Value obj) {
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

  public Object encode(final Object obj2) throws EncoderException {
    try {
      //
      // return encode0(obj);
      //

      // TODO: Check the type mapping below!
      return obj.invokeMember("encode", obj2).as(Object.class);
    } catch (PolyglotException e) {
      // TODO: Handle EncoderException
      throw (EncoderException) ExceptionHandler.handle(e, "Caverphone.encode");
    }
  }

  public boolean isCaverphoneEqual(final String str1, final String str2) {
    //
    // return this.caverphone(str1).equals(this.caverphone(str2));
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("isCaverphoneEqual", str1, str2).as(boolean.class);
  }

  public String encode1(final String str) {
    //
    // return this.caverphone(str);
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("encode1", str).as(String.class);
  }

  public Object encode0(final Object obj2) throws EncoderException {
    try {
      //
      // if (!(obj instanceof String)) {
      // throw new EncoderException(
      // "Parameter supplied to Caverphone encode is not of type java.lang.String",
      // null);
      // }
      // return this.caverphone((String) obj);
      //

      // TODO: Check the type mapping below!
      return obj.invokeMember("encode0", obj2).as(Object.class);
    } catch (PolyglotException e) {
      // TODO: Handle EncoderException
      throw (EncoderException) ExceptionHandler.handle(e, "Caverphone.encode0");
    }
  }

  public String caverphone(final String source) {
    //
    // return this.encoder.encode(source);
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("caverphone", source).as(String.class);
  }

  public Caverphone() {
    //

    this.obj = clz.invokeMember("__init__");
  }
}
