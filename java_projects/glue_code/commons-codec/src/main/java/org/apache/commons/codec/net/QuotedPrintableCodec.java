package org.apache.commons.codec.net;

import org.graalvm.polyglot.Value;
import org.graalvm.polyglot.PolyglotException;
import org.apache.commons.codec.ContextInitializer;
import org.apache.commons.codec.ExceptionHandler;
import org.apache.commons.codec.IntegrationUtils;
import java.io.ByteArrayOutputStream;
import java.nio.charset.Charset;
import java.io.UnsupportedEncodingException;
import java.nio.charset.IllegalCharsetNameException;
import java.nio.charset.StandardCharsets;
import java.nio.charset.UnsupportedCharsetException;
import java.util.BitSet;
import org.apache.commons.codec.BinaryDecoder;
import org.apache.commons.codec.DecoderException;
import org.apache.commons.codec.BinaryEncoder;
import org.apache.commons.codec.EncoderException;
import org.apache.commons.codec.StringDecoder;
import org.apache.commons.codec.StringEncoder;
import org.apache.commons.codec.binary.StringUtils;
public class QuotedPrintableCodec implements BinaryEncoder, BinaryDecoder, StringEncoder, StringDecoder {
    private static final int SAFE_LENGTH = 73;
    private static final byte LF = 10;
    private static final byte CR = 13;
    private static final byte SPACE = 32;
    private static final byte TAB = 9;
    private static final byte ESCAPE_CHAR = '=';
    private static final BitSet PRINTABLE_CHARS = new BitSet(256);
    private static Value clz = ContextInitializer.getPythonClass("/net/QuotedPrintableCodec.py", "QuotedPrintableCodec");
    private Value obj;
    public QuotedPrintableCodec(Value obj) {
        this.obj = obj;
    }
    public Value getPythonObject() {
        return obj;
    }
    public Object decode(final Object obj) throws DecoderException {
try {
// 
// return decode4(obj);
// 


// TODO: Check the type mapping below!
return this.obj.invokeMember("decode", obj).as(Object.class);
} catch (PolyglotException e) {
    // TODO: Handle DecoderException
    throw (DecoderException) ExceptionHandler.handle(e, "QuotedPrintableCodec.decode");
}
}
    public Object encode(final Object obj) throws EncoderException {
try {
// 
// return encode2(obj);
// 


// TODO: Check the type mapping below!
return this.obj.invokeMember("encode", obj).as(Object.class);
} catch (PolyglotException e) {
    // TODO: Handle EncoderException
    throw (EncoderException) ExceptionHandler.handle(e, "QuotedPrintableCodec.encode");
}
}
    public String decode(final String sourceStr) throws DecoderException {
try {
// 
// return decode3(sourceStr);
// 


// TODO: Check the type mapping below!
return this.obj.invokeMember("decode", sourceStr).as(String.class);
} catch (PolyglotException e) {
    // TODO: Handle DecoderException
    throw (DecoderException) ExceptionHandler.handle(e, "QuotedPrintableCodec.decode");
}
}
    public String encode(final String sourceStr) throws EncoderException {
try {
// 
// return encode1(sourceStr);
// 


// TODO: Check the type mapping below!
return this.obj.invokeMember("encode", sourceStr).as(String.class);
} catch (PolyglotException e) {
    // TODO: Handle EncoderException
    throw (EncoderException) ExceptionHandler.handle(e, "QuotedPrintableCodec.encode");
}
}
    public byte[] decode(final byte[] bytes) throws DecoderException {
try {
// 
// return decode0(bytes);
// 


// TODO: Check the type mapping below!
return this.obj.invokeMember("decode", bytes).as(byte[].class);
} catch (PolyglotException e) {
    // TODO: Handle DecoderException
    throw (DecoderException) ExceptionHandler.handle(e, "QuotedPrintableCodec.decode");
}
}
    public byte[] encode(final byte[] bytes) {
// 
// return encode0(bytes);
// 


// TODO: Check the type mapping below!
return this.obj.invokeMember("encode", bytes).as(byte[].class);
}
    public String encode4(final String sourceStr, final String sourceCharset)
            throws UnsupportedEncodingException {
try {
// 
// if (sourceStr == null) {
// return null;
// }
// return StringUtils.newStringUsAscii(encode0(sourceStr.getBytes(sourceCharset)));
// 


// TODO: Check the type mapping below!
return this.obj.invokeMember("encode4", sourceStr, sourceCharset).as(String.class);
} catch (PolyglotException e) {
    // TODO: Handle UnsupportedEncodingException
    throw (UnsupportedEncodingException) ExceptionHandler.handle(e, "QuotedPrintableCodec.encode4");
}
}
    public String encode3(final String sourceStr, final Charset sourceCharset) {
// 
// if (sourceStr == null) {
// return null;
// }
// return StringUtils.newStringUsAscii(this.encode0(sourceStr.getBytes(sourceCharset)));
// 


// TODO: Check the type mapping below!
return this.obj.invokeMember("encode3", sourceStr, sourceCharset).as(String.class);
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
    public Object decode4(final Object obj) throws DecoderException {
try {
// 
// if (obj == null) {
// return null;
// }
// if (obj instanceof byte[]) {
// return decode0((byte[]) obj);
// }
// if (obj instanceof String) {
// return decode3((String) obj);
// }
// throw new DecoderException(
// "Objects of type "
// + obj.getClass().getName()
// + " cannot be quoted-printable decoded",
// null);
// 


// TODO: Check the type mapping below!
return this.obj.invokeMember("decode4", obj).as(Object.class);
} catch (PolyglotException e) {
    // TODO: Handle DecoderException
    throw (DecoderException) ExceptionHandler.handle(e, "QuotedPrintableCodec.decode4");
}
}
    public Object encode2(final Object obj) throws EncoderException {
try {
// 
// if (obj == null) {
// return null;
// }
// if (obj instanceof byte[]) {
// return encode0((byte[]) obj);
// }
// if (obj instanceof String) {
// return encode1((String) obj);
// }
// throw new EncoderException(
// "Objects of type "
// + obj.getClass().getName()
// + " cannot be quoted-printable encoded",
// null);
// 


// TODO: Check the type mapping below!
return this.obj.invokeMember("encode2", obj).as(Object.class);
} catch (PolyglotException e) {
    // TODO: Handle EncoderException
    throw (EncoderException) ExceptionHandler.handle(e, "QuotedPrintableCodec.encode2");
}
}
    public String decode3(final String sourceStr) throws DecoderException {
try {
// 
// return this.decode1(sourceStr, this.getCharset());
// 


// TODO: Check the type mapping below!
return this.obj.invokeMember("decode3", sourceStr).as(String.class);
} catch (PolyglotException e) {
    // TODO: Handle DecoderException
    throw (DecoderException) ExceptionHandler.handle(e, "QuotedPrintableCodec.decode3");
}
}
    public String decode2(final String sourceStr, final String sourceCharset)
            throws DecoderException, UnsupportedEncodingException {
try {
// 
// if (sourceStr == null) {
// return null;
// }
// return new String(decode0(StringUtils.getBytesUsAscii(sourceStr)), sourceCharset);
// 


// TODO: Check the type mapping below!
return this.obj.invokeMember("decode2", sourceStr, sourceCharset).as(String.class);
} catch (PolyglotException e) {
    // TODO: Handle DecoderException, UnsupportedEncodingException
    // throw (DecoderException, UnsupportedEncodingException) ExceptionHandler.handle(e, "QuotedPrintableCodec.decode2");
    throw (DecoderException) ExceptionHandler.handle(e, "QuotedPrintableCodec.decode2");
}
}
    public String decode1(final String sourceStr, final Charset sourceCharset)
            throws DecoderException {
try {
// 
// if (sourceStr == null) {
// return null;
// }
// return new String(this.decode0(StringUtils.getBytesUsAscii(sourceStr)), sourceCharset);
// 


// TODO: Check the type mapping below!
return this.obj.invokeMember("decode1", sourceStr, sourceCharset).as(String.class);
} catch (PolyglotException e) {
    // TODO: Handle DecoderException
    throw (DecoderException) ExceptionHandler.handle(e, "QuotedPrintableCodec.decode1");
}
}
    public String encode1(final String sourceStr) throws EncoderException {
try {
// 
// return this.encode3(sourceStr, getCharset());
// 


// TODO: Check the type mapping below!
return this.obj.invokeMember("encode1", sourceStr).as(String.class);
} catch (PolyglotException e) {
    // TODO: Handle EncoderException
    throw (EncoderException) ExceptionHandler.handle(e, "QuotedPrintableCodec.encode1");
}
}
    public byte[] decode0(final byte[] bytes) throws DecoderException {
try {
// 
// return decodeQuotedPrintable(bytes);
// 


// TODO: Check the type mapping below!
return this.obj.invokeMember("decode0", bytes).as(byte[].class);
} catch (PolyglotException e) {
    // TODO: Handle DecoderException
    throw (DecoderException) ExceptionHandler.handle(e, "QuotedPrintableCodec.decode0");
}
}
    public byte[] encode0(final byte[] bytes) {
// 
// return encodeQuotedPrintable2(PRINTABLE_CHARS, bytes, strict);
// 


// TODO: Check the type mapping below!
return this.obj.invokeMember("encode0", bytes).as(byte[].class);
}
    public static final byte[] decodeQuotedPrintable(final byte[] bytes) throws DecoderException {
try {
// 
// if (bytes == null) {
// return null;
// }
// final ByteArrayOutputStream buffer = new ByteArrayOutputStream();
// for (int i = 0; i < bytes.length; i++) {
// final int b = bytes[i];
// if (b == ESCAPE_CHAR) {
// try {
// if (bytes[++i] == CR) {
// continue;
// }
// final int u = Utils.digit16(bytes[i]);
// final int l = Utils.digit16(bytes[++i]);
// buffer.write((char) ((u << 4) + l));
// } catch (final ArrayIndexOutOfBoundsException e) {
// throw new DecoderException("Invalid quoted-printable encoding", e);
// }
// } else if (b != CR && b != LF) {
// buffer.write(b);
// }
// }
// return buffer.toByteArray();
// 


// TODO: Check the type mapping below!
return clz.invokeMember("decodeQuotedPrintable", bytes).as(byte[].class);
} catch (PolyglotException e) {
    // TODO: Handle DecoderException
    throw (DecoderException) ExceptionHandler.handle(e, "QuotedPrintableCodec.decodeQuotedPrintable");
}
}
    public static final byte[] encodeQuotedPrintable2(
            BitSet printable, final byte[] bytes, final boolean strict) {
// 
// if (bytes == null) {
// return null;
// }
// if (printable == null) {
// printable = PRINTABLE_CHARS;
// }
// final ByteArrayOutputStream buffer = new ByteArrayOutputStream();
// final int bytesLength = bytes.length;
// 
// if (strict) {
// int pos = 1;
// for (int i = 0; i < bytesLength - 3; i++) {
// final int b = getUnsignedOctet(i, bytes);
// if (pos < SAFE_LENGTH) {
// pos += encodeByte(b, !printable.get(b), buffer);
// } else {
// encodeByte(b, !printable.get(b) || isWhitespace(b), buffer);
// 
// buffer.write(ESCAPE_CHAR);
// buffer.write(CR);
// buffer.write(LF);
// pos = 1;
// }
// }
// 
// int b = getUnsignedOctet(bytesLength - 3, bytes);
// boolean encode = !printable.get(b) || (isWhitespace(b) && pos > SAFE_LENGTH - 5);
// pos += encodeByte(b, encode, buffer);
// 
// if (pos > SAFE_LENGTH - 2) {
// buffer.write(ESCAPE_CHAR);
// buffer.write(CR);
// buffer.write(LF);
// }
// for (int i = bytesLength - 2; i < bytesLength; i++) {
// b = getUnsignedOctet(i, bytes);
// encode = !printable.get(b) || (i > bytesLength - 2 && isWhitespace(b));
// encodeByte(b, encode, buffer);
// }
// } else {
// for (final byte c : bytes) {
// int b = c;
// if (b < 0) {
// b = 256 + b;
// }
// if (printable.get(b)) {
// buffer.write(b);
// } else {
// encodeQuotedPrintable0(b, buffer);
// }
// }
// }
// return buffer.toByteArray();
// 


// TODO: Check the type mapping below!
return clz.invokeMember("encodeQuotedPrintable2", printable, bytes, strict).as(byte[].class);
}
    public static final byte[] encodeQuotedPrintable1(final BitSet printable, final byte[] bytes) {
// 
// return encodeQuotedPrintable2(printable, bytes, false);
// 


// TODO: Check the type mapping below!
return clz.invokeMember("encodeQuotedPrintable1", printable, bytes).as(byte[].class);
}
    public static QuotedPrintableCodec QuotedPrintableCodec4() {
// 
// return new QuotedPrintableCodec(1, null, StandardCharsets.UTF_8, false);
// 


// TODO: Check the type mapping below!
return clz.invokeMember("QuotedPrintableCodec4").as(QuotedPrintableCodec.class);
}
    public static QuotedPrintableCodec QuotedPrintableCodec3(final boolean strict) {
// 
// return new QuotedPrintableCodec(1, null, StandardCharsets.UTF_8, strict);
// 


// TODO: Check the type mapping below!
return clz.invokeMember("QuotedPrintableCodec3", strict).as(QuotedPrintableCodec.class);
}
    public static QuotedPrintableCodec QuotedPrintableCodec2(final Charset charset) {
// 
// return new QuotedPrintableCodec(1, null, charset, false);
// 


// TODO: Check the type mapping below!
return clz.invokeMember("QuotedPrintableCodec2", charset).as(QuotedPrintableCodec.class);
}
    public static QuotedPrintableCodec QuotedPrintableCodec0(final String charsetName)
            throws IllegalCharsetNameException,
                    IllegalArgumentException,
                    UnsupportedCharsetException {
try {
// 
// return new QuotedPrintableCodec(1, null, Charset.forName(charsetName), false);
// 


// TODO: Check the type mapping below!
return clz.invokeMember("QuotedPrintableCodec0", charsetName).as(QuotedPrintableCodec.class);
} catch (PolyglotException e) {
    // TODO: Handle IllegalCharsetNameException,
                    // IllegalArgumentException,
                    // UnsupportedCharsetException
    // throw (IllegalCharsetNameException,
    // IllegalArgumentException,
    // UnsupportedCharsetException) ExceptionHandler.handle(e, "QuotedPrintableCodec.QuotedPrintableCodec0");
    throw (IllegalCharsetNameException) ExceptionHandler.handle(e, "QuotedPrintableCodec.QuotedPrintableCodec0");
}
}
    public QuotedPrintableCodec(
            int constructorId,
            final String charsetName,
            final Charset charset,
            final boolean strict) {
// 
// if (constructorId == 1) {
// 
// this.charset = charset;
// this.strict = strict;
// } else {
// 
// this.charset = charset;
// this.strict = strict;
// }
// 

this.obj = clz.invokeMember("__init__", constructorId, charsetName, charset, strict);
}
    private static boolean isWhitespace(final int b) {
// 
// return b == SPACE || b == TAB;
// 


// TODO: Check the type mapping below!
return clz.invokeMember("isWhitespace", b).as(boolean.class);
}
    private static int encodeByte(
            final int b, final boolean encode, final ByteArrayOutputStream buffer) {
// 
// if (encode) {
// return encodeQuotedPrintable0(b, buffer);
// }
// buffer.write(b);
// return 1;
// 


// TODO: Check the type mapping below!
return clz.invokeMember("encodeByte", b, encode, buffer).as(int.class);
}
    private static int getUnsignedOctet(final int index, final byte[] bytes) {
// 
// int b = bytes[index];
// if (b < 0) {
// b = 256 + b;
// }
// return b;
// 


// TODO: Check the type mapping below!
return clz.invokeMember("getUnsignedOctet", index, bytes).as(int.class);
}
    private static final int encodeQuotedPrintable0(
            final int b, final ByteArrayOutputStream buffer) {
// 
// buffer.write(ESCAPE_CHAR);
// final char hex1 = Utils.hexDigit(b >> 4);
// final char hex2 = Utils.hexDigit(b);
// buffer.write(hex1);
// buffer.write(hex2);
// return 3;
// 


// TODO: Check the type mapping below!
return clz.invokeMember("encodeQuotedPrintable0", b, buffer).as(int.class);
}
}
