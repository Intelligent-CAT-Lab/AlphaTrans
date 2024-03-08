package org.apache.commons.codec.net;

import org.graalvm.polyglot.Value;
import org.graalvm.polyglot.PolyglotException;
import org.apache.commons.codec.ContextInitializer;
import org.apache.commons.codec.ExceptionHandler;
import org.apache.commons.codec.IntegrationUtils;
import java.nio.charset.Charset;
import java.io.UnsupportedEncodingException;
import org.apache.commons.codec.DecoderException;
import org.apache.commons.codec.EncoderException;
import org.apache.commons.codec.binary.StringUtils;
abstract class RFC1522Codec {
    protected static final String PREFIX = "=?";
    protected static final String POSTFIX = "?=";
    protected static final char SEP = '?';
    private static Value clz = ContextInitializer.getPythonClass("/net/RFC1522Codec.py", "RFC1522Codec");
    private Value obj;
    public RFC1522Codec(Value obj) {
        this.obj = obj;
    }
    public Value getPythonObject() {
        return obj;
    }
    protected String decodeText(final String text)
            throws DecoderException, UnsupportedEncodingException {
try {
// 
// if (text == null) {
// return null;
// }
// if (!text.startsWith(PREFIX) || !text.endsWith(POSTFIX)) {
// throw new DecoderException("RFC 1522 violation: malformed encoded content", null);
// }
// final int terminator = text.length() - 2;
// int from = 2;
// int to = text.indexOf(SEP, from);
// if (to == terminator) {
// throw new DecoderException("RFC 1522 violation: charset token not found", null);
// }
// final String charset = text.substring(from, to);
// if (charset.equals("")) {
// throw new DecoderException("RFC 1522 violation: charset not specified", null);
// }
// from = to + 1;
// to = text.indexOf(SEP, from);
// if (to == terminator) {
// throw new DecoderException("RFC 1522 violation: encoding token not found", null);
// }
// final String encoding = text.substring(from, to);
// if (!getEncoding().equalsIgnoreCase(encoding)) {
// throw new DecoderException(
// "This codec cannot decode " + encoding + " encoded content", null);
// }
// from = to + 1;
// to = text.indexOf(SEP, from);
// byte[] data = StringUtils.getBytesUsAscii(text.substring(from, to));
// data = doDecoding(data);
// return new String(data, charset);
// 


// TODO: Check the type mapping below!
return obj.invokeMember("decodeText", text).as(String.class);
} catch (PolyglotException e) {
    // TODO: Handle DecoderException, UnsupportedEncodingException
    throw (DecoderException, UnsupportedEncodingException) ExceptionHandler.handle(e, "RFC1522Codec.decodeText");
}
}
    protected String encodeText1(final String text, final String charsetName)
            throws EncoderException, UnsupportedEncodingException {
try {
// 
// if (text == null) {
// return null;
// }
// return this.encodeText0(text, Charset.forName(charsetName));
// 


// TODO: Check the type mapping below!
return obj.invokeMember("encodeText1", text, charsetName).as(String.class);
} catch (PolyglotException e) {
    // TODO: Handle EncoderException, UnsupportedEncodingException
    throw (EncoderException, UnsupportedEncodingException) ExceptionHandler.handle(e, "RFC1522Codec.encodeText1");
}
}
    protected String encodeText0(final String text, final Charset charset) throws EncoderException {
try {
// 
// if (text == null) {
// return null;
// }
// final StringBuilder buffer = new StringBuilder();
// buffer.append(PREFIX);
// buffer.append(charset);
// buffer.append(SEP);
// buffer.append(this.getEncoding());
// buffer.append(SEP);
// buffer.append(StringUtils.newStringUsAscii(this.doEncoding(text.getBytes(charset))));
// buffer.append(POSTFIX);
// return buffer.toString();
// 


// TODO: Check the type mapping below!
return obj.invokeMember("encodeText0", text, charset).as(String.class);
} catch (PolyglotException e) {
    // TODO: Handle EncoderException
    throw (EncoderException) ExceptionHandler.handle(e, "RFC1522Codec.encodeText0");
}
}
    protected abstract byte[] doDecoding(byte[] bytes) throws DecoderException;
    protected abstract byte[] doEncoding(byte[] bytes) throws EncoderException;
    protected abstract String getEncoding();
}
