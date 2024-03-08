package org.apache.commons.codec.binary;

import java.io.InputStream;
import org.apache.commons.codec.CodecPolicy;
import org.apache.commons.codec.ContextInitializer;
import org.graalvm.polyglot.Value;

public class Base16InputStream extends BaseNCodecInputStream {
  private static Value clz =
      ContextInitializer.getPythonClass("/binary/Base16InputStream.py", "Base16InputStream");
  private Value obj;

  public Base16InputStream(Value obj) {
    this.obj = obj;
  }

  public Value getPythonObject() {
    return obj;
  }

  public static Base16InputStream Base16InputStream3(final InputStream in) {
    //
    // return Base16InputStream2(in, false);
    //

    // TODO: Check the type mapping below!
    return clz.invokeMember("Base16InputStream3", in).as(Base16InputStream.class);
  }

  public static Base16InputStream Base16InputStream2(final InputStream in, final boolean doEncode) {
    //
    // return Base16InputStream1(in, doEncode, false);
    //

    // TODO: Check the type mapping below!
    return clz.invokeMember("Base16InputStream2", in, doEncode).as(Base16InputStream.class);
  }

  public static Base16InputStream Base16InputStream1(
      final InputStream in, final boolean doEncode, final boolean lowerCase) {
    //
    // return new Base16InputStream(in, doEncode, lowerCase, CodecPolicy.LENIENT);
    //

    // TODO: Check the type mapping below!
    return clz.invokeMember("Base16InputStream1", in, doEncode, lowerCase)
        .as(Base16InputStream.class);
  }

  public Base16InputStream(
      final InputStream in,
      final boolean doEncode,
      final boolean lowerCase,
      final CodecPolicy decodingPolicy) {
    //
    // super(in, new Base16(lowerCase, decodingPolicy), doEncode);
    //

    this.obj = clz.invokeMember("__init__", in, doEncode, lowerCase, decodingPolicy);
  }
}
