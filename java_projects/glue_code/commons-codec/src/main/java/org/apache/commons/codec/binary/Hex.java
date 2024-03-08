package org.apache.commons.codec.binary;

import java.nio.ByteBuffer;
import java.nio.charset.Charset;
import java.nio.charset.StandardCharsets;
import org.apache.commons.codec.BinaryDecoder;
import org.apache.commons.codec.BinaryEncoder;
import org.apache.commons.codec.CharEncoding;
import org.apache.commons.codec.ContextInitializer;
import org.apache.commons.codec.DecoderException;
import org.apache.commons.codec.EncoderException;
import org.apache.commons.codec.ExceptionHandler;
import org.graalvm.polyglot.PolyglotException;
import org.graalvm.polyglot.Value;

public class Hex implements BinaryEncoder, BinaryDecoder {
  public static final String DEFAULT_CHARSET_NAME = CharEncoding.UTF_8;
  public static final Charset DEFAULT_CHARSET = StandardCharsets.UTF_8;
  private static final char[] DIGITS_UPPER = {
    '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F'
  };
  private static final char[] DIGITS_LOWER = {
    '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f'
  };
  private static Value clz = ContextInitializer.getPythonClass("/binary/Hex.py", "Hex");
  private Value obj;

  public Hex(Value obj) {
    this.obj = obj;
  }

  public Value getPythonObject() {
    return obj;
  }

  public String toString() {
    //
    // return super.toString() + "[charsetName=" + this.charset + "]";
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("toString").as(String.class);
  }

  public Object encode(final Object object) throws EncoderException {
    try {
      //
      // return encode2(object);
      //

      // TODO: Check the type mapping below!
      return obj.invokeMember("encode", object).as(Object.class);
    } catch (PolyglotException e) {
      // TODO: Handle EncoderException
      throw (EncoderException) ExceptionHandler.handle(e, "Hex.encode");
    }
  }

  public byte[] encode(final byte[] array) {
    //
    // return encode0(array);
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("encode", array).as(byte[].class);
  }

  public Object decode(final Object object) throws DecoderException {
    try {
      //
      // return decode2(object);
      //

      // TODO: Check the type mapping below!
      return obj.invokeMember("decode", object).as(Object.class);
    } catch (PolyglotException e) {
      // TODO: Handle DecoderException
      throw (DecoderException) ExceptionHandler.handle(e, "Hex.decode");
    }
  }

  public byte[] decode(final byte[] array) throws DecoderException {
    try {
      //
      // return decode0(array);
      //

      // TODO: Check the type mapping below!
      return obj.invokeMember("decode", array).as(byte[].class);
    } catch (PolyglotException e) {
      // TODO: Handle DecoderException
      throw (DecoderException) ExceptionHandler.handle(e, "Hex.decode");
    }
  }

  public String getCharsetName() {
    //
    // return this.charset.name();
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("getCharsetName").as(String.class);
  }

  public Charset getCharset() {
    //
    // return this.charset;
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("getCharset").as(Charset.class);
  }

  public Object encode2(final Object object) throws EncoderException {
    try {
      //
      // final byte[] byteArray;
      // if (object instanceof String) {
      // byteArray = ((String) object).getBytes(this.getCharset());
      // } else if (object instanceof ByteBuffer) {
      // byteArray = toByteArray((ByteBuffer) object);
      // } else {
      // try {
      // byteArray = (byte[]) object;
      // } catch (final ClassCastException e) {
      // throw new EncoderException(e.getMessage(), e);
      // }
      // }
      // return encodeHex0(byteArray);
      //

      // TODO: Check the type mapping below!
      return obj.invokeMember("encode2", object).as(Object.class);
    } catch (PolyglotException e) {
      // TODO: Handle EncoderException
      throw (EncoderException) ExceptionHandler.handle(e, "Hex.encode2");
    }
  }

  public byte[] encode1(final ByteBuffer array) {
    //
    // return encodeHexString2(array).getBytes(this.getCharset());
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("encode1", array).as(byte[].class);
  }

  public byte[] encode(final ByteBuffer array) {
    //
    // return encode1(array);
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("encode", array).as(byte[].class);
  }

  public byte[] encode0(final byte[] array) {
    //
    // return encodeHexString0(array).getBytes(this.getCharset());
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("encode0", array).as(byte[].class);
  }

  public Object decode2(final Object object) throws DecoderException {
    try {
      //
      // if (object instanceof String) {
      // return decode2(((String) object).toCharArray());
      // }
      // if (object instanceof byte[]) {
      // return decode0((byte[]) object);
      // }
      // if (object instanceof ByteBuffer) {
      // return decode1((ByteBuffer) object);
      // }
      // try {
      // return decodeHex0((char[]) object);
      // } catch (final ClassCastException e) {
      // throw new DecoderException(e.getMessage(), e);
      // }
      //

      // TODO: Check the type mapping below!
      return obj.invokeMember("decode2", object).as(Object.class);
    } catch (PolyglotException e) {
      // TODO: Handle DecoderException
      throw (DecoderException) ExceptionHandler.handle(e, "Hex.decode2");
    }
  }

  public byte[] decode1(final ByteBuffer buffer) throws DecoderException {
    try {
      //
      // return decodeHex0(new String(toByteArray(buffer), getCharset()).toCharArray());
      //

      // TODO: Check the type mapping below!
      return obj.invokeMember("decode1", buffer).as(byte[].class);
    } catch (PolyglotException e) {
      // TODO: Handle DecoderException
      throw (DecoderException) ExceptionHandler.handle(e, "Hex.decode1");
    }
  }

  public byte[] decode(final ByteBuffer buffer) throws DecoderException {
    try {
      //
      // return decode1(buffer);
      //

      // TODO: Check the type mapping below!
      return obj.invokeMember("decode", buffer).as(byte[].class);
    } catch (PolyglotException e) {
      // TODO: Handle DecoderException
      throw (DecoderException) ExceptionHandler.handle(e, "Hex.decode");
    }
  }

  public byte[] decode0(final byte[] array) throws DecoderException {
    try {
      //
      // return decodeHex0(new String(array, getCharset()).toCharArray());
      //

      // TODO: Check the type mapping below!
      return obj.invokeMember("decode0", array).as(byte[].class);
    } catch (PolyglotException e) {
      // TODO: Handle DecoderException
      throw (DecoderException) ExceptionHandler.handle(e, "Hex.decode0");
    }
  }

  public static Hex Hex0(final String charsetName) {
    //
    // return new Hex(1, null, Charset.forName(charsetName));
    //

    // TODO: Check the type mapping below!
    return clz.invokeMember("Hex0", charsetName).as(Hex.class);
  }

  public Hex(int constructorId, final String charsetName, final Charset charset) {
    //
    // if (constructorId == 1) {
    //
    // this.charset = charset;
    // } else {
    //
    // this.charset = DEFAULT_CHARSET;
    // }
    //

    this.obj = clz.invokeMember("__init__", constructorId, charsetName, charset);
  }

  protected static int toDigit(final char ch, final int index) throws DecoderException {
    try {
      //
      // final int digit = Character.digit(ch, 16);
      // if (digit == -1) {
      // throw new DecoderException(
      // "Illegal hexadecimal character " + ch + " at index " + index, null);
      // }
      // return digit;
      //

      // TODO: Check the type mapping below!
      return clz.invokeMember("toDigit", ch, index).as(int.class);
    } catch (PolyglotException e) {
      // TODO: Handle DecoderException
      throw (DecoderException) ExceptionHandler.handle(e, "Hex.toDigit");
    }
  }

  public static String encodeHexString3(final ByteBuffer data, final boolean toLowerCase) {
    //
    // return new String(encodeHex7(data, toLowerCase));
    //

    // TODO: Check the type mapping below!
    return clz.invokeMember("encodeHexString3", data, toLowerCase).as(String.class);
  }

  public static String encodeHexString2(final ByteBuffer data) {
    //
    // return new String(encodeHex6(data));
    //

    // TODO: Check the type mapping below!
    return clz.invokeMember("encodeHexString2", data).as(String.class);
  }

  public static String encodeHexString1(final byte[] data, final boolean toLowerCase) {
    //
    // return new String(encodeHex1(data, toLowerCase));
    //

    // TODO: Check the type mapping below!
    return clz.invokeMember("encodeHexString1", data, toLowerCase).as(String.class);
  }

  public static String encodeHexString0(final byte[] data) {
    //
    // return new String(encodeHex0(data));
    //

    // TODO: Check the type mapping below!
    return clz.invokeMember("encodeHexString0", data).as(String.class);
  }

  protected static char[] encodeHex8(final ByteBuffer byteBuffer, final char[] toDigits) {
    //
    // return encodeHex2(toByteArray(byteBuffer), toDigits);
    //

    // TODO: Check the type mapping below!
    return clz.invokeMember("encodeHex8", byteBuffer, toDigits).as(char[].class);
  }

  public static char[] encodeHex7(final ByteBuffer data, final boolean toLowerCase) {
    //
    // return encodeHex8(data, toLowerCase ? DIGITS_LOWER : DIGITS_UPPER);
    //

    // TODO: Check the type mapping below!
    return clz.invokeMember("encodeHex7", data, toLowerCase).as(char[].class);
  }

  public static char[] encodeHex6(final ByteBuffer data) {
    //
    // return encodeHex7(data, true);
    //

    // TODO: Check the type mapping below!
    return clz.invokeMember("encodeHex6", data).as(char[].class);
  }

  public static void encodeHex4(
      final byte[] data,
      final int dataOffset,
      final int dataLen,
      final boolean toLowerCase,
      final char[] out,
      final int outOffset) {
    //
    // encodeHex5(
    // data,
    // dataOffset,
    // dataLen,
    // toLowerCase ? DIGITS_LOWER : DIGITS_UPPER,
    // out,
    // outOffset);
    //

    clz.invokeMember("encodeHex4", data, dataOffset, dataLen, toLowerCase, out, outOffset);
  }

  public static char[] encodeHex3(
      final byte[] data, final int dataOffset, final int dataLen, final boolean toLowerCase) {
    //
    // final char[] out = new char[dataLen << 1];
    // encodeHex5(data, dataOffset, dataLen, toLowerCase ? DIGITS_LOWER : DIGITS_UPPER, out, 0);
    // return out;
    //

    // TODO: Check the type mapping below!
    return clz.invokeMember("encodeHex3", data, dataOffset, dataLen, toLowerCase).as(char[].class);
  }

  protected static char[] encodeHex2(final byte[] data, final char[] toDigits) {
    //
    // final int dataLength = data.length;
    // final char[] out = new char[dataLength << 1];
    // encodeHex5(data, 0, dataLength, toDigits, out, 0);
    // return out;
    //

    // TODO: Check the type mapping below!
    return clz.invokeMember("encodeHex2", data, toDigits).as(char[].class);
  }

  public static char[] encodeHex1(final byte[] data, final boolean toLowerCase) {
    //
    // return encodeHex2(data, toLowerCase ? DIGITS_LOWER : DIGITS_UPPER);
    //

    // TODO: Check the type mapping below!
    return clz.invokeMember("encodeHex1", data, toLowerCase).as(char[].class);
  }

  public static char[] encodeHex0(final byte[] data) {
    //
    // return encodeHex1(data, true);
    //

    // TODO: Check the type mapping below!
    return clz.invokeMember("encodeHex0", data).as(char[].class);
  }

  public static byte[] decodeHex2(final String data) throws DecoderException {
    try {
      //
      // return decodeHex0(data.toCharArray());
      //

      // TODO: Check the type mapping below!
      return clz.invokeMember("decodeHex2", data).as(byte[].class);
    } catch (PolyglotException e) {
      // TODO: Handle DecoderException
      throw (DecoderException) ExceptionHandler.handle(e, "Hex.decodeHex2");
    }
  }

  public static int decodeHex1(final char[] data, final byte[] out, final int outOffset)
      throws DecoderException {
    try {
      //
      // final int len = data.length;
      //
      // if ((len & 0x01) != 0) {
      // throw new DecoderException("Odd number of characters.", null);
      // }
      //
      // final int outLen = len >> 1;
      // if (out.length - outOffset < outLen) {
      // throw new DecoderException(
      // "Output array is not large enough to accommodate decoded data.", null);
      // }
      //
      // for (int i = outOffset, j = 0; j < len; i++) {
      // int f = toDigit(data[j], j) << 4;
      // j++;
      // f = f | toDigit(data[j], j);
      // j++;
      // out[i] = (byte) (f & 0xFF);
      // }
      //
      // return outLen;
      //

      // TODO: Check the type mapping below!
      return clz.invokeMember("decodeHex1", data, out, outOffset).as(int.class);
    } catch (PolyglotException e) {
      // TODO: Handle DecoderException
      throw (DecoderException) ExceptionHandler.handle(e, "Hex.decodeHex1");
    }
  }

  public static byte[] decodeHex0(final char[] data) throws DecoderException {
    try {
      //
      // final byte[] out = new byte[data.length >> 1];
      // decodeHex1(data, out, 0);
      // return out;
      //

      // TODO: Check the type mapping below!
      return clz.invokeMember("decodeHex0", data).as(byte[].class);
    } catch (PolyglotException e) {
      // TODO: Handle DecoderException
      throw (DecoderException) ExceptionHandler.handle(e, "Hex.decodeHex0");
    }
  }

  private static byte[] toByteArray(final ByteBuffer byteBuffer) {
    //
    // final int remaining = byteBuffer.remaining();
    // if (byteBuffer.hasArray()) {
    // final byte[] byteArray = byteBuffer.array();
    // if (remaining == byteArray.length) {
    // byteBuffer.position(remaining);
    // return byteArray;
    // }
    // }
    // final byte[] byteArray = new byte[remaining];
    // byteBuffer.get(byteArray);
    // return byteArray;
    //

    // TODO: Check the type mapping below!
    return clz.invokeMember("toByteArray", byteBuffer).as(byte[].class);
  }

  private static void encodeHex5(
      final byte[] data,
      final int dataOffset,
      final int dataLen,
      final char[] toDigits,
      final char[] out,
      final int outOffset) {
    //
    // for (int i = dataOffset, j = outOffset; i < dataOffset + dataLen; i++) {
    // out[j++] = toDigits[(0xF0 & data[i]) >>> 4];
    // out[j++] = toDigits[0x0F & data[i]];
    // }
    //

    clz.invokeMember("encodeHex5", data, dataOffset, dataLen, toDigits, out, outOffset);
  }
}
