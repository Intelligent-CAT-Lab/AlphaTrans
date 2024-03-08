package org.apache.commons.codec.binary;

import java.io.OutputStream;
import org.apache.commons.codec.CodecPolicy;
import org.apache.commons.codec.ContextInitializer;
import org.graalvm.polyglot.Value;

public class Base16OutputStream extends BaseNCodecOutputStream {
  private static Value clz =
      ContextInitializer.getPythonClass("/binary/Base16OutputStream.py", "Base16OutputStream");
  private Value obj;

  public Base16OutputStream(Value obj) {
    this.obj = obj;
  }

  public Value getPythonObject() {
    return obj;
  }

  public static Base16OutputStream Base16OutputStream3(final OutputStream out) {
    //
    // return Base16OutputStream2(out, true);
    //

    // TODO: Check the type mapping below!
    return clz.invokeMember("Base16OutputStream3", out).as(Base16OutputStream.class);
  }

  public static Base16OutputStream Base16OutputStream2(
      final OutputStream out, final boolean doEncode) {
    //
    // return Base16OutputStream1(out, doEncode, false);
    //

    // TODO: Check the type mapping below!
    return clz.invokeMember("Base16OutputStream2", out, doEncode).as(Base16OutputStream.class);
  }

  public static Base16OutputStream Base16OutputStream1(
      final OutputStream out, final boolean doEncode, final boolean lowerCase) {
    //
    // return new Base16OutputStream(out, doEncode, lowerCase, CodecPolicy.LENIENT);
    //

    // TODO: Check the type mapping below!
    return clz.invokeMember("Base16OutputStream1", out, doEncode, lowerCase)
        .as(Base16OutputStream.class);
  }

  public Base16OutputStream(
      final OutputStream out,
      final boolean doEncode,
      final boolean lowerCase,
      final CodecPolicy decodingPolicy) {
    //
    // super(out, new Base16(lowerCase, decodingPolicy), doEncode);
    //

    this.obj = clz.invokeMember("__init__", out, doEncode, lowerCase, decodingPolicy);
  }
}
