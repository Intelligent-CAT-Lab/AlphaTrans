package org.apache.commons.codec.binary;

import java.io.OutputStream;
import org.apache.commons.codec.CodecPolicy;
import org.apache.commons.codec.ContextInitializer;
import org.graalvm.polyglot.Value;

public class Base64OutputStream extends BaseNCodecOutputStream {
  private static Value clz =
      ContextInitializer.getPythonClass("/binary/Base64OutputStream.py", "Base64OutputStream");
  private Value obj;

  public Base64OutputStream(Value obj) {
    this.obj = obj;
  }

  public Value getPythonObject() {
    return obj;
  }

  public Base64OutputStream(
      final OutputStream out,
      final boolean doEncode,
      final int lineLength,
      final byte[] lineSeparator,
      final CodecPolicy decodingPolicy) {
    //
    // super(out, new Base64(lineLength, lineSeparator, false, decodingPolicy), doEncode);
    //

    this.obj =
        clz.invokeMember("__init__", out, doEncode, lineLength, lineSeparator, decodingPolicy);
  }

  public static BaseNCodecOutputStream Base64OutputStream2(
      final OutputStream out,
      final boolean doEncode,
      final int lineLength,
      final byte[] lineSeparator) {
    //
    // return new BaseNCodecOutputStream(out, Base64.Base642(lineLength, lineSeparator), doEncode);
    //

    // TODO: Check the type mapping below!
    return clz.invokeMember("Base64OutputStream2", out, doEncode, lineLength, lineSeparator)
        .as(BaseNCodecOutputStream.class);
  }

  public static BaseNCodecOutputStream Base64OutputStream1(
      final OutputStream out, final boolean doEncode) {
    //
    // return new BaseNCodecOutputStream(out, Base64.Base644(false), doEncode);
    //

    // TODO: Check the type mapping below!
    return clz.invokeMember("Base64OutputStream1", out, doEncode).as(BaseNCodecOutputStream.class);
  }

  public static BaseNCodecOutputStream Base64OutputStream0(final OutputStream out) {
    //
    // return Base64OutputStream1(out, true);
    //

    // TODO: Check the type mapping below!
    return clz.invokeMember("Base64OutputStream0", out).as(BaseNCodecOutputStream.class);
  }
}
