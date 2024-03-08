package org.apache.commons.codec.net;

import java.util.BitSet;
import org.apache.commons.codec.BinaryDecoder;
import org.apache.commons.codec.BinaryEncoder;
import org.apache.commons.codec.ContextInitializer;
import org.apache.commons.codec.DecoderException;
import org.apache.commons.codec.EncoderException;
import org.apache.commons.codec.ExceptionHandler;
import org.graalvm.polyglot.PolyglotException;
import org.graalvm.polyglot.Value;

public class PercentCodec implements BinaryEncoder, BinaryDecoder {
  private int alwaysEncodeCharsMin = Integer.MAX_VALUE, alwaysEncodeCharsMax = Integer.MIN_VALUE;
  private final BitSet alwaysEncodeChars = new BitSet();
  private static final byte ESCAPE_CHAR = '%';
  private static Value clz =
      ContextInitializer.getPythonClass("/net/PercentCodec.py", "PercentCodec");
  private Value obj;

  public PercentCodec(Value obj) {
    this.obj = obj;
  }

  public Value getPythonObject() {
    return obj;
  }

  public Object decode(final Object obj) throws DecoderException {
    try {
      //
      // return decode1(obj);
      //

      // TODO: Check the type mapping below!
      return this.obj.invokeMember("decode", obj).as(Object.class);
    } catch (PolyglotException e) {
      // TODO: Handle DecoderException
      throw (DecoderException) ExceptionHandler.handle(e, "PercentCodec.decode");
    }
  }

  public Object encode(final Object obj) throws EncoderException {
    try {
      //
      // return encode1(obj);
      //

      // TODO: Check the type mapping below!
      return this.obj.invokeMember("encode", obj).as(Object.class);
    } catch (PolyglotException e) {
      // TODO: Handle EncoderException
      throw (EncoderException) ExceptionHandler.handle(e, "PercentCodec.encode");
    }
  }

  public byte[] decode(final byte[] bytes) throws DecoderException {
    try {
      //
      // return decode0(bytes);
      //

      // TODO: Check the type mapping below!
      return obj.invokeMember("decode", bytes).as(byte[].class);
    } catch (PolyglotException e) {
      // TODO: Handle DecoderException
      throw (DecoderException) ExceptionHandler.handle(e, "PercentCodec.decode");
    }
  }

  public byte[] encode(final byte[] bytes) throws EncoderException {
    try {
      //
      // return encode0(bytes);
      //

      // TODO: Check the type mapping below!
      return obj.invokeMember("encode", bytes).as(byte[].class);
    } catch (PolyglotException e) {
      // TODO: Handle EncoderException
      throw (EncoderException) ExceptionHandler.handle(e, "PercentCodec.encode");
    }
  }

  public Object decode1(final Object obj) throws DecoderException {
    try {
      //
      // if (obj == null) {
      // return null;
      // }
      // if (obj instanceof byte[]) {
      // return decode0((byte[]) obj);
      // }
      // throw new DecoderException(
      // "Objects of type " + obj.getClass().getName() + " cannot be Percent decoded", null);
      //

      // TODO: Check the type mapping below!
      return this.obj.invokeMember("decode1", obj).as(Object.class);
    } catch (PolyglotException e) {
      // TODO: Handle DecoderException
      throw (DecoderException) ExceptionHandler.handle(e, "PercentCodec.decode1");
    }
  }

  public Object encode1(final Object obj) throws EncoderException {
    try {
      //
      // if (obj == null) {
      // return null;
      // }
      // if (obj instanceof byte[]) {
      // return encode0((byte[]) obj);
      // }
      // throw new EncoderException(
      // "Objects of type " + obj.getClass().getName() + " cannot be Percent encoded", null);
      //

      // TODO: Check the type mapping below!
      return this.obj.invokeMember("encode1", obj).as(Object.class);
    } catch (PolyglotException e) {
      // TODO: Handle EncoderException
      throw (EncoderException) ExceptionHandler.handle(e, "PercentCodec.encode1");
    }
  }

  public byte[] decode0(final byte[] bytes) throws DecoderException {
    try {
      //
      // if (bytes == null) {
      // return null;
      // }
      //
      // final ByteBuffer buffer = ByteBuffer.allocate(expectedDecodingBytes(bytes));
      // for (int i = 0; i < bytes.length; i++) {
      // final byte b = bytes[i];
      // if (b == ESCAPE_CHAR) {
      // try {
      // final int u = Utils.digit16(bytes[++i]);
      // final int l = Utils.digit16(bytes[++i]);
      // buffer.put((byte) ((u << 4) + l));
      // } catch (final ArrayIndexOutOfBoundsException e) {
      // throw new DecoderException("Invalid percent decoding: ", e);
      // }
      // } else if (plusForSpace && b == '+') {
      // buffer.put((byte) ' ');
      // } else {
      // buffer.put(b);
      // }
      // }
      // return buffer.array();
      //

      // TODO: Check the type mapping below!
      return obj.invokeMember("decode0", bytes).as(byte[].class);
    } catch (PolyglotException e) {
      // TODO: Handle DecoderException
      throw (DecoderException) ExceptionHandler.handle(e, "PercentCodec.decode0");
    }
  }

  public byte[] encode0(final byte[] bytes) throws EncoderException {
    try {
      //
      // if (bytes == null) {
      // return null;
      // }
      //
      // final int expectedEncodingBytes = expectedEncodingBytes(bytes);
      // final boolean willEncode = expectedEncodingBytes != bytes.length;
      // if (willEncode || (plusForSpace && containsSpace(bytes))) {
      // return doEncode(bytes, expectedEncodingBytes, willEncode);
      // }
      // return bytes;
      //

      // TODO: Check the type mapping below!
      return obj.invokeMember("encode0", bytes).as(byte[].class);
    } catch (PolyglotException e) {
      // TODO: Handle EncoderException
      throw (EncoderException) ExceptionHandler.handle(e, "PercentCodec.encode0");
    }
  }

  public PercentCodec(
      int constructorId, final boolean plusForSpace, final byte[] alwaysEncodeChars) {
    //
    // if (constructorId == 0) {
    //
    // this.plusForSpace = plusForSpace;
    // insertAlwaysEncodeChars(alwaysEncodeChars);
    // } else {
    //
    // this.plusForSpace = false;
    // insertAlwaysEncodeChar(ESCAPE_CHAR);
    // }
    //

    this.obj = clz.invokeMember("__init__", constructorId, plusForSpace, alwaysEncodeChars);
  }

  private int expectedDecodingBytes(final byte[] bytes) {
    //
    // int byteCount = 0;
    // for (int i = 0; i < bytes.length; ) {
    // final byte b = bytes[i];
    // i += b == ESCAPE_CHAR ? 3 : 1;
    // byteCount++;
    // }
    // return byteCount;
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("expectedDecodingBytes", bytes).as(int.class);
  }

  private boolean isAsciiChar(final byte c) {
    //
    // return c >= 0;
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("isAsciiChar", c).as(boolean.class);
  }

  private boolean inAlwaysEncodeCharsRange(final byte c) {
    //
    // return c >= alwaysEncodeCharsMin && c <= alwaysEncodeCharsMax;
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("inAlwaysEncodeCharsRange", c).as(boolean.class);
  }

  private boolean canEncode(final byte c) {
    //
    // return !isAsciiChar(c) || (inAlwaysEncodeCharsRange(c) && alwaysEncodeChars.get(c));
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("canEncode", c).as(boolean.class);
  }

  private boolean containsSpace(final byte[] bytes) {
    //
    // for (final byte b : bytes) {
    // if (b == ' ') {
    // return true;
    // }
    // }
    // return false;
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("containsSpace", bytes).as(boolean.class);
  }

  private int expectedEncodingBytes(final byte[] bytes) {
    //
    // int byteCount = 0;
    // for (final byte b : bytes) {
    // byteCount += canEncode(b) ? 3 : 1;
    // }
    // return byteCount;
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("expectedEncodingBytes", bytes).as(int.class);
  }

  private byte[] doEncode(final byte[] bytes, final int expectedLength, final boolean willEncode) {
    //
    // final ByteBuffer buffer = ByteBuffer.allocate(expectedLength);
    // for (final byte b : bytes) {
    // if (willEncode && canEncode(b)) {
    // byte bb = b;
    // if (bb < 0) {
    // bb = (byte) (256 + bb);
    // }
    // final char hex1 = Utils.hexDigit(bb >> 4);
    // final char hex2 = Utils.hexDigit(bb);
    // buffer.put(ESCAPE_CHAR);
    // buffer.put((byte) hex1);
    // buffer.put((byte) hex2);
    // } else if (plusForSpace && b == ' ') {
    // buffer.put((byte) '+');
    // } else {
    // buffer.put(b);
    // }
    // }
    // return buffer.array();
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("doEncode", bytes, expectedLength, willEncode).as(byte[].class);
  }

  private void insertAlwaysEncodeChar(final byte b) {
    //
    // this.alwaysEncodeChars.set(b);
    // if (b < alwaysEncodeCharsMin) {
    // alwaysEncodeCharsMin = b;
    // }
    // if (b > alwaysEncodeCharsMax) {
    // alwaysEncodeCharsMax = b;
    // }
    //

    obj.invokeMember("insertAlwaysEncodeChar", b);
  }

  private void insertAlwaysEncodeChars(final byte[] alwaysEncodeCharsArray) {
    //
    // if (alwaysEncodeCharsArray != null) {
    // for (final byte b : alwaysEncodeCharsArray) {
    // insertAlwaysEncodeChar(b);
    // }
    // }
    // insertAlwaysEncodeChar(ESCAPE_CHAR);
    //

    obj.invokeMember("insertAlwaysEncodeChars", alwaysEncodeCharsArray);
  }
}
