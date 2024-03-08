package org.apache.commons.codec.binary;

import java.io.InputStream;
import org.apache.commons.codec.CodecPolicy;
import org.apache.commons.codec.ContextInitializer;
import org.graalvm.polyglot.Value;

public class Base64InputStream extends BaseNCodecInputStream {
  private static Value clz =
      ContextInitializer.getPythonClass("/binary/Base64InputStream.py", "Base64InputStream");
  private Value obj;

  public Base64InputStream(Value obj) {
    this.obj = obj;
  }

  public Value getPythonObject() {
    return obj;
  }

  public Base64InputStream(
      final InputStream in,
      final boolean doEncode,
      final int lineLength,
      final byte[] lineSeparator,
      final CodecPolicy decodingPolicy) {
    //
    // super(in, new Base64(lineLength, lineSeparator, false, decodingPolicy), doEncode);
    //

    this.obj =
        clz.invokeMember("__init__", in, doEncode, lineLength, lineSeparator, decodingPolicy);
  }

  public static BaseNCodecInputStream Base64InputStream2(
      final InputStream in,
      final boolean doEncode,
      final int lineLength,
      final byte[] lineSeparator) {
    //
    // return new BaseNCodecInputStream(in, Base64.Base642(lineLength, lineSeparator), doEncode);
    //

    // TODO: Check the type mapping below!
    return clz.invokeMember("Base64InputStream2", in, doEncode, lineLength, lineSeparator)
        .as(BaseNCodecInputStream.class);
  }

  public static BaseNCodecInputStream Base64InputStream1(
      final InputStream in, final boolean doEncode) {
    //
    // return new BaseNCodecInputStream(in, Base64.Base644(false), doEncode);
    //

    // TODO: Check the type mapping below!
    return clz.invokeMember("Base64InputStream1", in, doEncode).as(BaseNCodecInputStream.class);
  }

  public static BaseNCodecInputStream Base64InputStream0(final InputStream in) {
    //
    // return Base64InputStream1(in, false);
    //

    // TODO: Check the type mapping below!
    return clz.invokeMember("Base64InputStream0", in).as(BaseNCodecInputStream.class);
  }
}
