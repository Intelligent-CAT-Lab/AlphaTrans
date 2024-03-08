package org.apache.commons.codec.binary;

import java.io.OutputStream;
import org.apache.commons.codec.CodecPolicy;
import org.apache.commons.codec.ContextInitializer;
import org.graalvm.polyglot.Value;

public class Base32OutputStream extends BaseNCodecOutputStream {
  private static Value clz =
      ContextInitializer.getPythonClass("/binary/Base32OutputStream.py", "Base32OutputStream");
  private Value obj;

  public Base32OutputStream(Value obj) {
    this.obj = obj;
  }

  public Value getPythonObject() {
    return obj;
  }

  public Base32OutputStream(
      final OutputStream ouput,
      final boolean doEncode,
      final int lineLength,
      final byte[] lineSeparator,
      final CodecPolicy decodingPolicy) {
    //
    // super(
    // ouput,
    // new Base32(
    // lineLength, lineSeparator, false, BaseNCodec.PAD_DEFAULT, decodingPolicy),
    // doEncode);
    //

    this.obj =
        clz.invokeMember("__init__", ouput, doEncode, lineLength, lineSeparator, decodingPolicy);
  }

  public static BaseNCodecOutputStream Base32OutputStream2(
      final OutputStream ouput,
      final boolean doEncode,
      final int lineLength,
      final byte[] lineSeparator) {
    //
    // return new BaseNCodecOutputStream(
    // ouput, Base32.Base325(lineLength, lineSeparator), doEncode);
    //

    // TODO: Check the type mapping below!
    return clz.invokeMember("Base32OutputStream2", ouput, doEncode, lineLength, lineSeparator)
        .as(BaseNCodecOutputStream.class);
  }

  public static BaseNCodecOutputStream Base32OutputStream1(
      final OutputStream out, final boolean doEncode) {
    //
    // return new BaseNCodecOutputStream(out, Base32.Base321(false), doEncode);
    //

    // TODO: Check the type mapping below!
    return clz.invokeMember("Base32OutputStream1", out, doEncode).as(BaseNCodecOutputStream.class);
  }

  public static BaseNCodecOutputStream Base32OutputStream0(final OutputStream out) {
    //
    // return Base32OutputStream1(out, true);
    //

    // TODO: Check the type mapping below!
    return clz.invokeMember("Base32OutputStream0", out).as(BaseNCodecOutputStream.class);
  }
}
