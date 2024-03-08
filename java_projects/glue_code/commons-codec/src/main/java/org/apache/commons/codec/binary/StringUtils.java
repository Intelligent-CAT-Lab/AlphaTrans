package org.apache.commons.codec.binary;

import java.io.UnsupportedEncodingException;
import java.nio.ByteBuffer;
import java.nio.charset.Charset;
import org.apache.commons.codec.ContextInitializer;
import org.graalvm.polyglot.Value;

public class StringUtils {
  private static Value clz =
      ContextInitializer.getPythonClass("/binary/StringUtils.py", "StringUtils");
  private Value obj;

  public StringUtils(Value obj) {
    this.obj = obj;
  }

  public Value getPythonObject() {
    return obj;
  }

  public static String newStringUtf8(final byte[] bytes) {
    //
    // return newString0(bytes, StandardCharsets.UTF_8);
    //

    // TODO: Check the type mapping below!
    return clz.invokeMember("newStringUtf8", bytes).as(String.class);
  }

  public static String newStringUtf16Le(final byte[] bytes) {
    //
    // return newString0(bytes, StandardCharsets.UTF_16LE);
    //

    // TODO: Check the type mapping below!
    return clz.invokeMember("newStringUtf16Le", bytes).as(String.class);
  }

  public static String newStringUtf16Be(final byte[] bytes) {
    //
    // return newString0(bytes, StandardCharsets.UTF_16BE);
    //

    // TODO: Check the type mapping below!
    return clz.invokeMember("newStringUtf16Be", bytes).as(String.class);
  }

  public static String newStringUtf16(final byte[] bytes) {
    //
    // return newString0(bytes, StandardCharsets.UTF_16);
    //

    // TODO: Check the type mapping below!
    return clz.invokeMember("newStringUtf16", bytes).as(String.class);
  }

  public static String newStringUsAscii(final byte[] bytes) {
    //
    // return newString0(bytes, StandardCharsets.US_ASCII);
    //

    // TODO: Check the type mapping below!
    return clz.invokeMember("newStringUsAscii", bytes).as(String.class);
  }

  public static String newStringIso8859_1(final byte[] bytes) {
    //
    // return newString0(bytes, StandardCharsets.ISO_8859_1);
    //

    // TODO: Check the type mapping below!
    return clz.invokeMember("newStringIso8859_1", bytes).as(String.class);
  }

  public static String newString1(final byte[] bytes, final String charsetName) {
    //
    // if (bytes == null) {
    // return null;
    // }
    // try {
    // return new String(bytes, charsetName);
    // } catch (final UnsupportedEncodingException e) {
    // throw StringUtils.newIllegalStateException(charsetName, e);
    // }
    //

    // TODO: Check the type mapping below!
    return clz.invokeMember("newString1", bytes, charsetName).as(String.class);
  }

  public static byte[] getBytesUtf8(final String string) {
    //
    // return getBytes(string, StandardCharsets.UTF_8);
    //

    // TODO: Check the type mapping below!
    return clz.invokeMember("getBytesUtf8", string).as(byte[].class);
  }

  public static byte[] getBytesUtf16Le(final String string) {
    //
    // return getBytes(string, StandardCharsets.UTF_16LE);
    //

    // TODO: Check the type mapping below!
    return clz.invokeMember("getBytesUtf16Le", string).as(byte[].class);
  }

  public static byte[] getBytesUtf16Be(final String string) {
    //
    // return getBytes(string, StandardCharsets.UTF_16BE);
    //

    // TODO: Check the type mapping below!
    return clz.invokeMember("getBytesUtf16Be", string).as(byte[].class);
  }

  public static byte[] getBytesUtf16(final String string) {
    //
    // return getBytes(string, StandardCharsets.UTF_16);
    //

    // TODO: Check the type mapping below!
    return clz.invokeMember("getBytesUtf16", string).as(byte[].class);
  }

  public static byte[] getBytesUsAscii(final String string) {
    //
    // return getBytes(string, StandardCharsets.US_ASCII);
    //

    // TODO: Check the type mapping below!
    return clz.invokeMember("getBytesUsAscii", string).as(byte[].class);
  }

  public static byte[] getBytesUnchecked(final String string, final String charsetName) {
    //
    // if (string == null) {
    // return null;
    // }
    // try {
    // return string.getBytes(charsetName);
    // } catch (final UnsupportedEncodingException e) {
    // throw StringUtils.newIllegalStateException(charsetName, e);
    // }
    //

    // TODO: Check the type mapping below!
    return clz.invokeMember("getBytesUnchecked", string, charsetName).as(byte[].class);
  }

  public static byte[] getBytesIso8859_1(final String string) {
    //
    // return getBytes(string, StandardCharsets.ISO_8859_1);
    //

    // TODO: Check the type mapping below!
    return clz.invokeMember("getBytesIso8859_1", string).as(byte[].class);
  }

  public static ByteBuffer getByteBufferUtf8(final String string) {
    //
    // return getByteBuffer(string, StandardCharsets.UTF_8);
    //

    // TODO: Check the type mapping below!
    return clz.invokeMember("getByteBufferUtf8", string).as(ByteBuffer.class);
  }

  public static boolean equals(final CharSequence cs1, final CharSequence cs2) {
    //
    // if (cs1 == cs2) {
    // return true;
    // }
    // if (cs1 == null || cs2 == null) {
    // return false;
    // }
    // if (cs1 instanceof String && cs2 instanceof String) {
    // return cs1.equals(cs2);
    // }
    // return cs1.length() == cs2.length()
    // && CharSequenceUtils.regionMatches(cs1, false, 0, cs2, 0, cs1.length());
    //

    // TODO: Check the type mapping below!
    return clz.invokeMember("equals", cs1, cs2).as(boolean.class);
  }

  private static String newString0(final byte[] bytes, final Charset charset) {
    //
    // return bytes == null ? null : new String(bytes, charset);
    //

    // TODO: Check the type mapping below!
    return clz.invokeMember("newString0", bytes, charset).as(String.class);
  }

  private static IllegalStateException newIllegalStateException(
      final String charsetName, final UnsupportedEncodingException e) {
    //
    // return new IllegalStateException(charsetName + ": " + e);
    //

    // TODO: Check the type mapping below!
    return clz.invokeMember("newIllegalStateException", charsetName, e)
        .as(IllegalStateException.class);
  }

  private static byte[] getBytes(final String string, final Charset charset) {
    //
    // if (string == null) {
    // return null;
    // }
    // return string.getBytes(charset);
    //

    // TODO: Check the type mapping below!
    return clz.invokeMember("getBytes", string, charset).as(byte[].class);
  }

  private static ByteBuffer getByteBuffer(final String string, final Charset charset) {
    //
    // if (string == null) {
    // return null;
    // }
    // return ByteBuffer.wrap(string.getBytes(charset));
    //

    // TODO: Check the type mapping below!
    return clz.invokeMember("getByteBuffer", string, charset).as(ByteBuffer.class);
  }
}
