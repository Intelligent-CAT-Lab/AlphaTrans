package org.apache.commons.codec.net;

import java.nio.charset.Charset;
import org.apache.commons.codec.CodecPolicy;
import org.apache.commons.codec.ContextInitializer;
import org.apache.commons.codec.DecoderException;
import org.apache.commons.codec.EncoderException;
import org.apache.commons.codec.ExceptionHandler;
import org.apache.commons.codec.StringDecoder;
import org.apache.commons.codec.StringEncoder;
import org.graalvm.polyglot.PolyglotException;
import org.graalvm.polyglot.Value;

public class BCodec extends RFC1522Codec implements StringEncoder, StringDecoder {
  private static final CodecPolicy DECODING_POLICY_DEFAULT = CodecPolicy.LENIENT;
  private static Value clz = ContextInitializer.getPythonClass("/net/BCodec.py", "BCodec");
  private Value obj;

  public BCodec(Value obj) {
    this.obj = obj;
  }

  public Value getPythonObject() {
    return obj;
  }

  public Object decode(final Object value) throws DecoderException {
    try {
      //
      // return decode1(value);
      //

      // TODO: Check the type mapping below!
      return obj.invokeMember("decode", value).as(Object.class);
    } catch (PolyglotException e) {
      // TODO: Handle DecoderException
      throw (DecoderException) ExceptionHandler.handle(e, "BCodec.decode");
    }
  }

  public Object encode(final Object value) throws EncoderException {
    try {
      //
      // return encode3(value);
      //

      // TODO: Check the type mapping below!
      return obj.invokeMember("encode", value).as(Object.class);
    } catch (PolyglotException e) {
      // TODO: Handle EncoderException
      throw (EncoderException) ExceptionHandler.handle(e, "BCodec.encode");
    }
  }

  public String decode(final String value) throws DecoderException {
    try {
      //
      // return decode0(value);
      //

      // TODO: Check the type mapping below!
      return obj.invokeMember("decode", value).as(String.class);
    } catch (PolyglotException e) {
      // TODO: Handle DecoderException
      throw (DecoderException) ExceptionHandler.handle(e, "BCodec.decode");
    }
  }

  public String encode(final String strSource) throws EncoderException {
    try {
      //
      // return encode2(strSource);
      //

      // TODO: Check the type mapping below!
      return obj.invokeMember("encode", strSource).as(String.class);
    } catch (PolyglotException e) {
      // TODO: Handle EncoderException
      throw (EncoderException) ExceptionHandler.handle(e, "BCodec.encode");
    }
  }

  protected byte[] doDecoding(final byte[] bytes) {
    //
    // if (bytes == null) {
    // return null;
    // }
    // return new Base64(0, BaseNCodec.getChunkSeparator(), false, decodingPolicy).decode0(bytes);
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("doDecoding", bytes).as(byte[].class);
  }

  protected byte[] doEncoding(final byte[] bytes) {
    //
    // if (bytes == null) {
    // return null;
    // }
    // return Base64.encodeBase640(bytes);
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("doEncoding", bytes).as(byte[].class);
  }

  protected String getEncoding() {
    //
    // return "B";
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("getEncoding").as(String.class);
  }

  public String getDefaultCharset() {
    //
    // return this.charset.name();
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("getDefaultCharset").as(String.class);
  }

  public Charset getCharset() {
    //
    // return this.charset;
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("getCharset").as(Charset.class);
  }

  public Object decode1(final Object value) throws DecoderException {
    try {
      //
      // if (value == null) {
      // return null;
      // }
      // if (value instanceof String) {
      // return decode0((String) value);
      // }
      // throw new DecoderException(
      // "Objects of type " + value.getClass().getName() + " cannot be decoded using BCodec",
      // null);
      //

      // TODO: Check the type mapping below!
      return obj.invokeMember("decode1", value).as(Object.class);
    } catch (PolyglotException e) {
      // TODO: Handle DecoderException
      throw (DecoderException) ExceptionHandler.handle(e, "BCodec.decode1");
    }
  }

  public Object encode3(final Object value) throws EncoderException {
    try {
      //
      // if (value == null) {
      // return null;
      // }
      // if (value instanceof String) {
      // return encode2((String) value);
      // }
      // throw new EncoderException(
      // "Objects of type " + value.getClass().getName() + " cannot be encoded using BCodec",
      // null);
      //

      // TODO: Check the type mapping below!
      return obj.invokeMember("encode3", value).as(Object.class);
    } catch (PolyglotException e) {
      // TODO: Handle EncoderException
      throw (EncoderException) ExceptionHandler.handle(e, "BCodec.encode3");
    }
  }

  public String decode0(final String value) throws DecoderException {
    try {
      //
      // if (value == null) {
      // return null;
      // }
      // try {
      // return this.decodeText(value);
      // } catch (final UnsupportedEncodingException | IllegalArgumentException e) {
      // throw new DecoderException(e.getMessage(), e);
      // }
      //

      // TODO: Check the type mapping below!
      return obj.invokeMember("decode0", value).as(String.class);
    } catch (PolyglotException e) {
      // TODO: Handle DecoderException
      throw (DecoderException) ExceptionHandler.handle(e, "BCodec.decode0");
    }
  }

  public String encode2(final String strSource) throws EncoderException {
    try {
      //
      // if (strSource == null) {
      // return null;
      // }
      // return encode0(strSource, this.getCharset());
      //

      // TODO: Check the type mapping below!
      return obj.invokeMember("encode2", strSource).as(String.class);
    } catch (PolyglotException e) {
      // TODO: Handle EncoderException
      throw (EncoderException) ExceptionHandler.handle(e, "BCodec.encode2");
    }
  }

  public String encode1(final String strSource, final String sourceCharset)
      throws EncoderException {
    try {
      //
      // if (strSource == null) {
      // return null;
      // }
      // try {
      // return this.encodeText1(strSource, sourceCharset);
      // } catch (final UnsupportedEncodingException e) {
      // throw new EncoderException(e.getMessage(), e);
      // }
      //

      // TODO: Check the type mapping below!
      return obj.invokeMember("encode1", strSource, sourceCharset).as(String.class);
    } catch (PolyglotException e) {
      // TODO: Handle EncoderException
      throw (EncoderException) ExceptionHandler.handle(e, "BCodec.encode1");
    }
  }

  public String encode0(final String strSource, final Charset sourceCharset)
      throws EncoderException {
    try {
      //
      // if (strSource == null) {
      // return null;
      // }
      // return encodeText0(strSource, sourceCharset);
      //

      // TODO: Check the type mapping below!
      return obj.invokeMember("encode0", strSource, sourceCharset).as(String.class);
    } catch (PolyglotException e) {
      // TODO: Handle EncoderException
      throw (EncoderException) ExceptionHandler.handle(e, "BCodec.encode0");
    }
  }

  public String encode(final String strSource, final Charset sourceCharset)
      throws EncoderException {
    try {
      //
      // return encode0(strSource, sourceCharset);
      //

      // TODO: Check the type mapping below!
      return obj.invokeMember("encode", strSource, sourceCharset).as(String.class);
    } catch (PolyglotException e) {
      // TODO: Handle EncoderException
      throw (EncoderException) ExceptionHandler.handle(e, "BCodec.encode");
    }
  }

  public boolean isStrictDecoding() {
    //
    // return decodingPolicy == CodecPolicy.STRICT;
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("isStrictDecoding").as(boolean.class);
  }

  public static BCodec BCodec2(final String charsetName) {
    //
    // return BCodec1(Charset.forName(charsetName));
    //

    // TODO: Check the type mapping below!
    return clz.invokeMember("BCodec2", charsetName).as(BCodec.class);
  }

  public BCodec(final Charset charset, final CodecPolicy decodingPolicy) {
    //
    // this.charset = charset;
    // this.decodingPolicy = decodingPolicy;
    //

    this.obj = clz.invokeMember("__init__", charset, decodingPolicy);
  }

  public static BCodec BCodec1(final Charset charset) {
    //
    // return new BCodec(charset, DECODING_POLICY_DEFAULT);
    //

    // TODO: Check the type mapping below!
    return clz.invokeMember("BCodec1", charset).as(BCodec.class);
  }

  public static BCodec BCodec0() {
    //
    // return BCodec1(StandardCharsets.UTF_8);
    //

    // TODO: Check the type mapping below!
    return clz.invokeMember("BCodec0").as(BCodec.class);
  }
}
