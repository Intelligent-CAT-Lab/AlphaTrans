package org.apache.commons.codec.net;

import java.nio.charset.Charset;
import java.util.BitSet;
import org.apache.commons.codec.ContextInitializer;
import org.apache.commons.codec.DecoderException;
import org.apache.commons.codec.EncoderException;
import org.apache.commons.codec.ExceptionHandler;
import org.apache.commons.codec.StringDecoder;
import org.apache.commons.codec.StringEncoder;
import org.graalvm.polyglot.PolyglotException;
import org.graalvm.polyglot.Value;

public class QCodec extends RFC1522Codec implements StringEncoder, StringDecoder {
  private boolean encodeBlanks = false;
  private static final byte UNDERSCORE = 95;
  private static final byte SPACE = 32;
  private static final BitSet PRINTABLE_CHARS = new BitSet(256);
  private static Value clz = ContextInitializer.getPythonClass("/net/QCodec.py", "QCodec");
  private Value obj;

  public QCodec(Value obj) {
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
      throw (DecoderException) ExceptionHandler.handle(e, "QCodec.decode");
    }
  }

  public Object encode(final Object obj) throws EncoderException {
    try {
      //
      // return encode3(obj);
      //

      // TODO: Check the type mapping below!
      return this.obj.invokeMember("encode", obj).as(Object.class);
    } catch (PolyglotException e) {
      // TODO: Handle EncoderException
      throw (EncoderException) ExceptionHandler.handle(e, "QCodec.encode");
    }
  }

  public String decode(final String str) throws DecoderException {
    try {
      //
      // return decode0(str);
      //

      // TODO: Check the type mapping below!
      return this.obj.invokeMember("decode", str).as(String.class);
    } catch (PolyglotException e) {
      // TODO: Handle DecoderException
      throw (DecoderException) ExceptionHandler.handle(e, "QCodec.decode");
    }
  }

  public String encode(final String sourceStr) throws EncoderException {
    try {
      //
      // return encode2(sourceStr);
      //

      // TODO: Check the type mapping below!
      return this.obj.invokeMember("encode", sourceStr).as(String.class);
    } catch (PolyglotException e) {
      // TODO: Handle EncoderException
      throw (EncoderException) ExceptionHandler.handle(e, "QCodec.encode");
    }
  }

  protected byte[] doDecoding(final byte[] bytes) throws DecoderException {
    try {
      //
      // if (bytes == null) {
      // return null;
      // }
      // boolean hasUnderscores = false;
      // for (final byte b : bytes) {
      // if (b == UNDERSCORE) {
      // hasUnderscores = true;
      // break;
      // }
      // }
      // if (hasUnderscores) {
      // final byte[] tmp = new byte[bytes.length];
      // for (int i = 0; i < bytes.length; i++) {
      // final byte b = bytes[i];
      // if (b != UNDERSCORE) {
      // tmp[i] = b;
      // } else {
      // tmp[i] = SPACE;
      // }
      // }
      // return QuotedPrintableCodec.decodeQuotedPrintable(tmp);
      // }
      // return QuotedPrintableCodec.decodeQuotedPrintable(bytes);
      //

      // TODO: Check the type mapping below!
      return this.obj.invokeMember("doDecoding", bytes).as(byte[].class);
    } catch (PolyglotException e) {
      // TODO: Handle DecoderException
      throw (DecoderException) ExceptionHandler.handle(e, "QCodec.doDecoding");
    }
  }

  protected byte[] doEncoding(final byte[] bytes) {
    //
    // if (bytes == null) {
    // return null;
    // }
    // final byte[] data = QuotedPrintableCodec.encodeQuotedPrintable1(PRINTABLE_CHARS, bytes);
    // if (this.encodeBlanks) {
    // for (int i = 0; i < data.length; i++) {
    // if (data[i] == SPACE) {
    // data[i] = UNDERSCORE;
    // }
    // }
    // }
    // return data;
    //

    // TODO: Check the type mapping below!
    return this.obj.invokeMember("doEncoding", bytes).as(byte[].class);
  }

  protected String getEncoding() {
    //
    // return "Q";
    //

    // TODO: Check the type mapping below!
    return this.obj.invokeMember("getEncoding").as(String.class);
  }

  public void setEncodeBlanks(final boolean b) {
    //
    // this.encodeBlanks = b;
    //

    obj.invokeMember("setEncodeBlanks", b);
  }

  public boolean isEncodeBlanks() {
    //
    // return this.encodeBlanks;
    //

    // TODO: Check the type mapping below!
    return this.obj.invokeMember("isEncodeBlanks").as(boolean.class);
  }

  public String getDefaultCharset() {
    //
    // return this.charset.name();
    //

    // TODO: Check the type mapping below!
    return this.obj.invokeMember("getDefaultCharset").as(String.class);
  }

  public Charset getCharset() {
    //
    // return this.charset;
    //

    // TODO: Check the type mapping below!
    return this.obj.invokeMember("getCharset").as(Charset.class);
  }

  public Object decode1(final Object obj) throws DecoderException {
    try {
      //
      // if (obj == null) {
      // return null;
      // }
      // if (obj instanceof String) {
      // return decode0((String) obj);
      // }
      // throw new DecoderException(
      // "Objects of type " + obj.getClass().getName() + " cannot be decoded using Q codec",
      // null);
      //

      // TODO: Check the type mapping below!
      return this.obj.invokeMember("decode1", obj).as(Object.class);
    } catch (PolyglotException e) {
      // TODO: Handle DecoderException
      throw (DecoderException) ExceptionHandler.handle(e, "QCodec.decode1");
    }
  }

  public Object encode3(final Object obj) throws EncoderException {
    try {
      //
      // if (obj == null) {
      // return null;
      // }
      // if (obj instanceof String) {
      // return encode2((String) obj);
      // }
      // throw new EncoderException(
      // "Objects of type " + obj.getClass().getName() + " cannot be encoded using Q codec",
      // null);
      //

      // TODO: Check the type mapping below!
      return this.obj.invokeMember("encode3", obj).as(Object.class);
    } catch (PolyglotException e) {
      // TODO: Handle EncoderException
      throw (EncoderException) ExceptionHandler.handle(e, "QCodec.encode3");
    }
  }

  public String decode0(final String str) throws DecoderException {
    try {
      //
      // if (str == null) {
      // return null;
      // }
      // try {
      // return decodeText(str);
      // } catch (final UnsupportedEncodingException e) {
      // throw new DecoderException(e.getMessage(), e);
      // }
      //

      // TODO: Check the type mapping below!
      return this.obj.invokeMember("decode0", str).as(String.class);
    } catch (PolyglotException e) {
      // TODO: Handle DecoderException
      throw (DecoderException) ExceptionHandler.handle(e, "QCodec.decode0");
    }
  }

  public String encode2(final String sourceStr) throws EncoderException {
    try {
      //
      // if (sourceStr == null) {
      // return null;
      // }
      // return encode0(sourceStr, getCharset());
      //

      // TODO: Check the type mapping below!
      return this.obj.invokeMember("encode2", sourceStr).as(String.class);
    } catch (PolyglotException e) {
      // TODO: Handle EncoderException
      throw (EncoderException) ExceptionHandler.handle(e, "QCodec.encode2");
    }
  }

  public String encode1(final String sourceStr, final String sourceCharset)
      throws EncoderException {
    try {
      //
      // if (sourceStr == null) {
      // return null;
      // }
      // try {
      // return encodeText1(sourceStr, sourceCharset);
      // } catch (final UnsupportedEncodingException e) {
      // throw new EncoderException(e.getMessage(), e);
      // }
      //

      // TODO: Check the type mapping below!
      return this.obj.invokeMember("encode1", sourceStr, sourceCharset).as(String.class);
    } catch (PolyglotException e) {
      // TODO: Handle EncoderException
      throw (EncoderException) ExceptionHandler.handle(e, "QCodec.encode1");
    }
  }

  public String encode0(final String sourceStr, final Charset sourceCharset)
      throws EncoderException {
    try {
      //
      // if (sourceStr == null) {
      // return null;
      // }
      // return encodeText0(sourceStr, sourceCharset);
      //

      // TODO: Check the type mapping below!
      return this.obj.invokeMember("encode0", sourceStr, sourceCharset).as(String.class);
    } catch (PolyglotException e) {
      // TODO: Handle EncoderException
      throw (EncoderException) ExceptionHandler.handle(e, "QCodec.encode0");
    }
  }

  public static QCodec QCodec2() {
    //
    // return new QCodec(1, null, StandardCharsets.UTF_8);
    //

    // TODO: Check the type mapping below!
    return clz.invokeMember("QCodec2").as(QCodec.class);
  }

  public static QCodec QCodec0(final String charsetName) {
    //
    // return new QCodec(1, null, Charset.forName(charsetName));
    //

    // TODO: Check the type mapping below!
    return clz.invokeMember("QCodec0", charsetName).as(QCodec.class);
  }

  public QCodec(int constructorId, final String charsetName, final Charset charset) {
    //
    // if (constructorId == 1) {
    //
    // this.charset = charset;
    // } else {
    //
    // this.charset = charset;
    // }
    //

    this.obj = clz.invokeMember("__init__", constructorId, charsetName, charset);
  }
}
