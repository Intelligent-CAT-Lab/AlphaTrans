package org.apache.commons.codec.binary;

import org.apache.commons.codec.BinaryDecoder;
import org.apache.commons.codec.BinaryEncoder;
import org.apache.commons.codec.ContextInitializer;
import org.apache.commons.codec.DecoderException;
import org.apache.commons.codec.EncoderException;
import org.apache.commons.codec.ExceptionHandler;
import org.graalvm.polyglot.PolyglotException;
import org.graalvm.polyglot.Value;

public class BinaryCodec implements BinaryDecoder, BinaryEncoder {
  private static final int BIT_7 = 0x80;
  private static final int BIT_6 = 0x40;
  private static final int BIT_5 = 0x20;
  private static final int BIT_4 = 0x10;
  private static final int BIT_3 = 0x08;
  private static final int BIT_2 = 0x04;
  private static final int BIT_1 = 0x02;
  private static final int BIT_0 = 1;
  private static final int[] BITS = {BIT_0, BIT_1, BIT_2, BIT_3, BIT_4, BIT_5, BIT_6, BIT_7};
  private static final byte[] EMPTY_BYTE_ARRAY = {};
  private static final char[] EMPTY_CHAR_ARRAY = {};
  private static Value clz =
      ContextInitializer.getPythonClass("/binary/BinaryCodec.py", "BinaryCodec");
  private Value obj;

  public BinaryCodec(Value obj) {
    this.obj = obj;
  }

  public Value getPythonObject() {
    return obj;
  }

  public Object encode(final Object raw) throws EncoderException {
    try {
      //
      // return encode1(raw);
      //

      // TODO: Check the type mapping below!
      return obj.invokeMember("encode", raw).as(Object.class);
    } catch (PolyglotException e) {
      // TODO: Handle EncoderException
      throw (EncoderException) ExceptionHandler.handle(e, "BinaryCodec.encode");
    }
  }

  public byte[] encode(final byte[] raw) {
    //
    // return encode0(raw);
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("encode", raw).as(byte[].class);
  }

  public Object decode(final Object ascii) throws DecoderException {
    try {
      //
      // return decode1(ascii);
      //

      // TODO: Check the type mapping below!
      return obj.invokeMember("decode", ascii).as(Object.class);
    } catch (PolyglotException e) {
      // TODO: Handle DecoderException
      throw (DecoderException) ExceptionHandler.handle(e, "BinaryCodec.decode");
    }
  }

  public byte[] decode(final byte[] ascii) {
    //
    // return decode0(ascii);
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("decode", ascii).as(byte[].class);
  }

  public byte[] toByteArray(final String ascii) {
    //
    // if (ascii == null) {
    // return EMPTY_BYTE_ARRAY;
    // }
    // return fromAscii1(ascii.toCharArray());
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("toByteArray", ascii).as(byte[].class);
  }

  public Object encode1(final Object raw) throws EncoderException {
    try {
      //
      // if (!(raw instanceof byte[])) {
      // throw new EncoderException("argument not a byte array", null);
      // }
      // return toAsciiChars((byte[]) raw);
      //

      // TODO: Check the type mapping below!
      return obj.invokeMember("encode1", raw).as(Object.class);
    } catch (PolyglotException e) {
      // TODO: Handle EncoderException
      throw (EncoderException) ExceptionHandler.handle(e, "BinaryCodec.encode1");
    }
  }

  public byte[] encode0(final byte[] raw) {
    //
    // return toAsciiBytes(raw);
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("encode0", raw).as(byte[].class);
  }

  public Object decode1(final Object ascii) throws DecoderException {
    try {
      //
      // if (ascii == null) {
      // return EMPTY_BYTE_ARRAY;
      // }
      // if (ascii instanceof byte[]) {
      // return fromAscii0((byte[]) ascii);
      // }
      // if (ascii instanceof char[]) {
      // return fromAscii1((char[]) ascii);
      // }
      // if (ascii instanceof String) {
      // return fromAscii1(((String) ascii).toCharArray());
      // }
      // throw new DecoderException("argument not a byte array", null);
      //

      // TODO: Check the type mapping below!
      return obj.invokeMember("decode1", ascii).as(Object.class);
    } catch (PolyglotException e) {
      // TODO: Handle DecoderException
      throw (DecoderException) ExceptionHandler.handle(e, "BinaryCodec.decode1");
    }
  }

  public byte[] decode0(final byte[] ascii) {
    //
    // return fromAscii0(ascii);
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("decode0", ascii).as(byte[].class);
  }

  public static String toAsciiString(final byte[] raw) {
    //
    // return new String(toAsciiChars(raw));
    //

    // TODO: Check the type mapping below!
    return clz.invokeMember("toAsciiString", raw).as(String.class);
  }

  public static char[] toAsciiChars(final byte[] raw) {
    //
    // if (isEmpty(raw)) {
    // return EMPTY_CHAR_ARRAY;
    // }
    // final int rawLength = raw.length;
    // final char[] l_ascii = new char[rawLength << 3];
    // /*
    // * We decr index jj by 8 as we go along to not recompute indices using multiplication every
    // time inside the
    // * loop.
    // */
    // for (int ii = 0, jj = l_ascii.length - 1; ii < rawLength; ii++, jj -= 8) {
    // for (int bits = 0; bits < BITS.length; ++bits) {
    // if ((raw[ii] & BITS[bits]) == 0) {
    // l_ascii[jj - bits] = '0';
    // } else {
    // l_ascii[jj - bits] = '1';
    // }
    // }
    // }
    // return l_ascii;
    //

    // TODO: Check the type mapping below!
    return clz.invokeMember("toAsciiChars", raw).as(char[].class);
  }

  public static byte[] toAsciiBytes(final byte[] raw) {
    //
    // if (isEmpty(raw)) {
    // return EMPTY_BYTE_ARRAY;
    // }
    // final int rawLength = raw.length;
    // final byte[] l_ascii = new byte[rawLength << 3];
    // /*
    // * We decr index jj by 8 as we go along to not recompute indices using multiplication every
    // time inside the
    // * loop.
    // */
    // for (int ii = 0, jj = l_ascii.length - 1; ii < rawLength; ii++, jj -= 8) {
    // for (int bits = 0; bits < BITS.length; ++bits) {
    // if ((raw[ii] & BITS[bits]) == 0) {
    // l_ascii[jj - bits] = '0';
    // } else {
    // l_ascii[jj - bits] = '1';
    // }
    // }
    // }
    // return l_ascii;
    //

    // TODO: Check the type mapping below!
    return clz.invokeMember("toAsciiBytes", raw).as(byte[].class);
  }

  public static byte[] fromAscii1(final char[] ascii) {
    //
    // if (ascii == null || ascii.length == 0) {
    // return EMPTY_BYTE_ARRAY;
    // }
    // final int asciiLength = ascii.length;
    // final byte[] l_raw = new byte[asciiLength >> 3];
    // /*
    // * We decr index jj by 8 as we go along to not recompute indices using multiplication every
    // time inside the
    // * loop.
    // */
    // for (int ii = 0, jj = asciiLength - 1; ii < l_raw.length; ii++, jj -= 8) {
    // for (int bits = 0; bits < BITS.length; ++bits) {
    // if (ascii[jj - bits] == '1') {
    // l_raw[ii] |= BITS[bits];
    // }
    // }
    // }
    // return l_raw;
    //

    // TODO: Check the type mapping below!
    return clz.invokeMember("fromAscii1", ascii).as(byte[].class);
  }

  public static byte[] fromAscii0(final byte[] ascii) {
    //
    // if (isEmpty(ascii)) {
    // return EMPTY_BYTE_ARRAY;
    // }
    // final int asciiLength = ascii.length;
    // final byte[] l_raw = new byte[asciiLength >> 3];
    // /*
    // * We decr index jj by 8 as we go along to not recompute indices using multiplication every
    // time inside the
    // * loop.
    // */
    // for (int ii = 0, jj = asciiLength - 1; ii < l_raw.length; ii++, jj -= 8) {
    // for (int bits = 0; bits < BITS.length; ++bits) {
    // if (ascii[jj - bits] == '1') {
    // l_raw[ii] |= BITS[bits];
    // }
    // }
    // }
    // return l_raw;
    //

    // TODO: Check the type mapping below!
    return clz.invokeMember("fromAscii0", ascii).as(byte[].class);
  }

  private static boolean isEmpty(final byte[] array) {
    //
    // return array == null || array.length == 0;
    //

    // TODO: Check the type mapping below!
    return clz.invokeMember("isEmpty", array).as(boolean.class);
  }
}
