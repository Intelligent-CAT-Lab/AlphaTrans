package org.apache.commons.codec.net;

import org.graalvm.polyglot.Value;
import org.graalvm.polyglot.PolyglotException;
import org.apache.commons.codec.ContextInitializer;
import org.apache.commons.codec.ExceptionHandler;
import org.apache.commons.codec.IntegrationUtils;
import java.io.ByteArrayOutputStream;
import java.io.UnsupportedEncodingException;
import java.util.BitSet;
import org.apache.commons.codec.BinaryDecoder;
import org.apache.commons.codec.DecoderException;
import org.apache.commons.codec.BinaryEncoder;
import org.apache.commons.codec.EncoderException;
import org.apache.commons.codec.CharEncoding;
import org.apache.commons.codec.StringDecoder;
import org.apache.commons.codec.StringEncoder;
import org.apache.commons.codec.binary.StringUtils;
public class URLCodec implements BinaryEncoder, BinaryDecoder, StringEncoder, StringDecoder {
    protected static final byte ESCAPE_CHAR = '%';
    private static final BitSet WWW_FORM_URL_SAFE = new BitSet(256);
    private static Value clz = ContextInitializer.getPythonClass("/net/URLCodec.py", "URLCodec");
    private Value obj;
    public URLCodec(Value obj) {
        this.obj = obj;
    }
    public Value getPythonObject() {
        return obj;
    }
    public String getEncoding() {
// 
// return this.charset;
// 


// TODO: Check the type mapping below!
return obj.invokeMember("getEncoding").as(String.class);
}
    public Object decode(final Object obj) throws DecoderException {
try {
// 
// return decode3(obj);
// 


// TODO: Check the type mapping below!
return obj.invokeMember("decode", obj).as(Object.class);
} catch (PolyglotException e) {
    // TODO: Handle DecoderException
    throw (DecoderException) ExceptionHandler.handle(e, "URLCodec.decode");
}
}
    public Object encode(final Object obj) throws EncoderException {
try {
// 
// return encode3(obj);
// 


// TODO: Check the type mapping below!
return obj.invokeMember("encode", obj).as(Object.class);
} catch (PolyglotException e) {
    // TODO: Handle EncoderException
    throw (EncoderException) ExceptionHandler.handle(e, "URLCodec.encode");
}
}
    public String decode(final String str) throws DecoderException {
try {
// 
// return decode2(str);
// 


// TODO: Check the type mapping below!
return obj.invokeMember("decode", str).as(String.class);
} catch (PolyglotException e) {
    // TODO: Handle DecoderException
    throw (DecoderException) ExceptionHandler.handle(e, "URLCodec.decode");
}
}
    public String encode(final String str) throws EncoderException {
try {
// 
// return encode2(str);
// 


// TODO: Check the type mapping below!
return obj.invokeMember("encode", str).as(String.class);
} catch (PolyglotException e) {
    // TODO: Handle EncoderException
    throw (EncoderException) ExceptionHandler.handle(e, "URLCodec.encode");
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
    throw (DecoderException) ExceptionHandler.handle(e, "URLCodec.decode");
}
}
    public byte[] encode(final byte[] bytes) {
// 
// return encode0(bytes);
// 


// TODO: Check the type mapping below!
return obj.invokeMember("encode", bytes).as(byte[].class);
}
    public String getDefaultCharset() {
// 
// return this.charset;
// 


// TODO: Check the type mapping below!
return obj.invokeMember("getDefaultCharset").as(String.class);
}
    public Object decode3(final Object obj) throws DecoderException {
try {
// 
// if (obj == null) {
// return null;
// }
// if (obj instanceof byte[]) {
// return decode0((byte[]) obj);
// }
// if (obj instanceof String) {
// return decode2((String) obj);
// }
// throw new DecoderException(
// "Objects of type " + obj.getClass().getName() + " cannot be URL decoded", null);
// 


// TODO: Check the type mapping below!
return obj.invokeMember("decode3", obj).as(Object.class);
} catch (PolyglotException e) {
    // TODO: Handle DecoderException
    throw (DecoderException) ExceptionHandler.handle(e, "URLCodec.decode3");
}
}
    public Object encode3(final Object obj) throws EncoderException {
try {
// 
// if (obj == null) {
// return null;
// }
// if (obj instanceof byte[]) {
// return encode0((byte[]) obj);
// }
// if (obj instanceof String) {
// return encode2((String) obj);
// }
// throw new EncoderException(
// "Objects of type " + obj.getClass().getName() + " cannot be URL encoded", null);
// 


// TODO: Check the type mapping below!
return obj.invokeMember("encode3", obj).as(Object.class);
} catch (PolyglotException e) {
    // TODO: Handle EncoderException
    throw (EncoderException) ExceptionHandler.handle(e, "URLCodec.encode3");
}
}
    public String decode2(final String str) throws DecoderException {
try {
// 
// if (str == null) {
// return null;
// }
// try {
// return decode1(str, getDefaultCharset());
// } catch (final UnsupportedEncodingException e) {
// throw new DecoderException(e.getMessage(), e);
// }
// 


// TODO: Check the type mapping below!
return obj.invokeMember("decode2", str).as(String.class);
} catch (PolyglotException e) {
    // TODO: Handle DecoderException
    throw (DecoderException) ExceptionHandler.handle(e, "URLCodec.decode2");
}
}
    public String decode1(final String str, final String charsetName)
            throws DecoderException, UnsupportedEncodingException {
try {
// 
// if (str == null) {
// return null;
// }
// return new String(decode0(StringUtils.getBytesUsAscii(str)), charsetName);
// 


// TODO: Check the type mapping below!
return obj.invokeMember("decode1", str, charsetName).as(String.class);
} catch (PolyglotException e) {
    // TODO: Handle DecoderException, UnsupportedEncodingException
    throw (DecoderException, UnsupportedEncodingException) ExceptionHandler.handle(e, "URLCodec.decode1");
}
}
    public String decode(final String str, final String charsetName)
            throws DecoderException, UnsupportedEncodingException {
try {
// 
// return decode1(str, charsetName);
// 


// TODO: Check the type mapping below!
return obj.invokeMember("decode", str, charsetName).as(String.class);
} catch (PolyglotException e) {
    // TODO: Handle DecoderException, UnsupportedEncodingException
    throw (DecoderException, UnsupportedEncodingException) ExceptionHandler.handle(e, "URLCodec.decode");
}
}
    public String encode2(final String str) throws EncoderException {
try {
// 
// if (str == null) {
// return null;
// }
// try {
// return encode1(str, getDefaultCharset());
// } catch (final UnsupportedEncodingException e) {
// throw new EncoderException(e.getMessage(), e);
// }
// 


// TODO: Check the type mapping below!
return obj.invokeMember("encode2", str).as(String.class);
} catch (PolyglotException e) {
    // TODO: Handle EncoderException
    throw (EncoderException) ExceptionHandler.handle(e, "URLCodec.encode2");
}
}
    public String encode1(final String str, final String charsetName)
            throws UnsupportedEncodingException {
try {
// 
// if (str == null) {
// return null;
// }
// return StringUtils.newStringUsAscii(encode0(str.getBytes(charsetName)));
// 


// TODO: Check the type mapping below!
return obj.invokeMember("encode1", str, charsetName).as(String.class);
} catch (PolyglotException e) {
    // TODO: Handle UnsupportedEncodingException
    throw (UnsupportedEncodingException) ExceptionHandler.handle(e, "URLCodec.encode1");
}
}
    public String encode(final String str, final String charsetName)
            throws UnsupportedEncodingException {
try {
// 
// return encode1(str, charsetName);
// 


// TODO: Check the type mapping below!
return obj.invokeMember("encode", str, charsetName).as(String.class);
} catch (PolyglotException e) {
    // TODO: Handle UnsupportedEncodingException
    throw (UnsupportedEncodingException) ExceptionHandler.handle(e, "URLCodec.encode");
}
}
    public byte[] decode0(final byte[] bytes) throws DecoderException {
try {
// 
// return decodeUrl(bytes);
// 


// TODO: Check the type mapping below!
return obj.invokeMember("decode0", bytes).as(byte[].class);
} catch (PolyglotException e) {
    // TODO: Handle DecoderException
    throw (DecoderException) ExceptionHandler.handle(e, "URLCodec.decode0");
}
}
    public byte[] encode0(final byte[] bytes) {
// 
// return encodeUrl(WWW_FORM_URL_SAFE, bytes);
// 


// TODO: Check the type mapping below!
return obj.invokeMember("encode0", bytes).as(byte[].class);
}
    public static final byte[] decodeUrl(final byte[] bytes) throws DecoderException {
try {
// 
// if (bytes == null) {
// return null;
// }
// final ByteArrayOutputStream buffer = new ByteArrayOutputStream();
// for (int i = 0; i < bytes.length; i++) {
// final int b = bytes[i];
// if (b == '+') {
// buffer.write(' ');
// } else if (b == ESCAPE_CHAR) {
// try {
// final int u = Utils.digit16(bytes[++i]);
// final int l = Utils.digit16(bytes[++i]);
// buffer.write((char) ((u << 4) + l));
// } catch (final ArrayIndexOutOfBoundsException e) {
// throw new DecoderException("Invalid URL encoding: ", e);
// }
// } else {
// buffer.write(b);
// }
// }
// return buffer.toByteArray();
// 


// TODO: Check the type mapping below!
return clz.invokeMember("decodeUrl", bytes).as(byte[].class);
} catch (PolyglotException e) {
    // TODO: Handle DecoderException
    throw (DecoderException) ExceptionHandler.handle(e, "URLCodec.decodeUrl");
}
}
    public static final byte[] encodeUrl(BitSet urlsafe, final byte[] bytes) {
// 
// if (bytes == null) {
// return null;
// }
// if (urlsafe == null) {
// urlsafe = WWW_FORM_URL_SAFE;
// }
// 
// final ByteArrayOutputStream buffer = new ByteArrayOutputStream();
// for (final byte c : bytes) {
// int b = c;
// if (b < 0) {
// b = 256 + b;
// }
// if (urlsafe.get(b)) {
// if (b == ' ') {
// b = '+';
// }
// buffer.write(b);
// } else {
// buffer.write(ESCAPE_CHAR);
// final char hex1 = Utils.hexDigit(b >> 4);
// final char hex2 = Utils.hexDigit(b);
// buffer.write(hex1);
// buffer.write(hex2);
// }
// }
// return buffer.toByteArray();
// 


// TODO: Check the type mapping below!
return clz.invokeMember("encodeUrl", urlsafe, bytes).as(byte[].class);
}
    public static URLCodec URLCodec1() {
// 
// return new URLCodec(CharEncoding.UTF_8);
// 


// TODO: Check the type mapping below!
return clz.invokeMember("URLCodec1").as(URLCodec.class);
}
    public URLCodec(final String charset) {
// 
// this.charset = charset;
// 

this.obj = clz.invokeMember("__init__", charset);
}
}
