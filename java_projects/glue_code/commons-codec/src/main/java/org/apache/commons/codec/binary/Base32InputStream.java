package org.apache.commons.codec.binary;

import java.io.InputStream;
import org.apache.commons.codec.CodecPolicy;
import org.apache.commons.codec.ContextInitializer;
import org.graalvm.polyglot.Value;

public class Base32InputStream extends BaseNCodecInputStream {
  private static Value clz =
      ContextInitializer.getPythonClass("/binary/Base32InputStream.py", "Base32InputStream");
  private Value obj;

  public Base32InputStream(Value obj) {
    this.obj = obj;
  }

  public Value getPythonObject() {
    return obj;
  }

  public Base32InputStream(
      final InputStream input,
      final boolean doEncode,
      final int lineLength,
      final byte[] lineSeparator,
      final CodecPolicy decodingPolicy) {
    //
    // super(
    // input,
    // new Base32(
    // lineLength, lineSeparator, false, BaseNCodec.PAD_DEFAULT, decodingPolicy),
    // doEncode);
    //

    this.obj =
        clz.invokeMember("__init__", input, doEncode, lineLength, lineSeparator, decodingPolicy);
  }

  public static BaseNCodecInputStream Base32InputStream2(
      final InputStream input,
      final boolean doEncode,
      final int lineLength,
      final byte[] lineSeparator) {
    //
    // return new BaseNCodecInputStream(
    // input, Base32.Base325(lineLength, lineSeparator), doEncode);
    //

    // TODO: Check the type mapping below!
    return clz.invokeMember("Base32InputStream2", input, doEncode, lineLength, lineSeparator)
        .as(BaseNCodecInputStream.class);
  }

  public static BaseNCodecInputStream Base32InputStream1(
      final InputStream in, final boolean doEncode) {
    //
    // return new BaseNCodecInputStream(in, Base32.Base321(false), doEncode);
    //

    // TODO: Check the type mapping below!
    return clz.invokeMember("Base32InputStream1", in, doEncode).as(BaseNCodecInputStream.class);
  }

  public static BaseNCodecInputStream Base32InputStream0(final InputStream in) {
    //
    // return Base32InputStream1(in, false);
    //

    // TODO: Check the type mapping below!
    return clz.invokeMember("Base32InputStream0", in).as(BaseNCodecInputStream.class);
  }
}
