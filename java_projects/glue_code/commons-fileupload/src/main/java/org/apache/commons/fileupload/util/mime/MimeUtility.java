package org.apache.commons.fileupload.util.mime;

import org.graalvm.polyglot.Value;
import org.graalvm.polyglot.PolyglotException;

import org.apache.commons.fileupload.ContextInitializer;
import org.apache.commons.fileupload.ExceptionHandler;

import java.io.IOException;
import java.io.ByteArrayOutputStream;
import java.io.UnsupportedEncodingException;
import java.util.Map;
import java.util.Locale;
import java.util.HashMap;
public final class MimeUtility {
    private static final Map<String, String> MIME2JAVA = new HashMap<String, String>();
    private static final String LINEAR_WHITESPACE = " \t\r\n";
    private static final String ENCODED_TOKEN_FINISHER = "?=";
    private static final String ENCODED_TOKEN_MARKER = "=?";
    private static final String QUOTEDPRINTABLE_ENCODING_MARKER = "Q";
    private static final String BASE64_ENCODING_MARKER = "B";
    private static final String US_ASCII_CHARSET = "US-ASCII";
    private static Value clz = ContextInitializer.getPythonClass("<placeholder>", "MimeUtility");
    private Value obj;
    public MimeUtility(Value obj) {
        this.obj = obj;
    }
    public Value getPythonObject() {
        return obj;
    }
    public static String decodeText(String text) throws UnsupportedEncodingException {
try {
// 
// if (text.indexOf(ENCODED_TOKEN_MARKER) < 0) {
// return text;
// }
// 
// int offset = 0;
// int endOffset = text.length();
// 
// int startWhiteSpace = -1;
// int endWhiteSpace = -1;
// 
// StringBuilder decodedText = new StringBuilder(text.length());
// 
// boolean previousTokenEncoded = false;
// 
// while (offset < endOffset) {
// char ch = text.charAt(offset);
// 
// if (LINEAR_WHITESPACE.indexOf(ch) != -1) { // whitespace found
// startWhiteSpace = offset;
// while (offset < endOffset) {
// ch = text.charAt(offset);
// if (LINEAR_WHITESPACE.indexOf(ch) != -1) { // whitespace found
// offset++;
// } else {
// endWhiteSpace = offset;
// break;
// }
// }
// } else {
// int wordStart = offset;
// 
// while (offset < endOffset) {
// ch = text.charAt(offset);
// if (LINEAR_WHITESPACE.indexOf(ch) == -1) { // not white space
// offset++;
// } else {
// break;
// }
// }
// String word = text.substring(wordStart, offset);
// if (word.startsWith(ENCODED_TOKEN_MARKER)) {
// try {
// String decodedWord = decodeWord(word);
// 
// if (!previousTokenEncoded && startWhiteSpace != -1) {
// decodedText.append(text.substring(startWhiteSpace, endWhiteSpace));
// startWhiteSpace = -1;
// }
// previousTokenEncoded = true;
// decodedText.append(decodedWord);
// continue;
// 
// } catch (ParseException e) {
// }
// }
// if (startWhiteSpace != -1) {
// decodedText.append(text.substring(startWhiteSpace, endWhiteSpace));
// startWhiteSpace = -1;
// }
// previousTokenEncoded = false;
// decodedText.append(word);
// }
// }
// 
// return decodedText.toString();
// 


// TODO: Check the type mapping below!
return clz.invokeMember("decodeText", text).as(String.class);
} catch (PolyglotException e) {
    throw (UnsupportedEncodingException) ExceptionHandler.handle(e, "MimeUtility.decodeText");
}
}
    private static String javaCharset(String charset) {
// 
// if (charset == null) {
// return null;
// }
// 
// String mappedCharset = MIME2JAVA.get(charset.toLowerCase(Locale.ENGLISH));
// if (mappedCharset == null) {
// return charset;
// }
// return mappedCharset;
// 


// TODO: Check the type mapping below!
return clz.invokeMember("javaCharset", charset).as(String.class);
}
    private static String decodeWord(String word)
            throws ParseException, UnsupportedEncodingException {
try {
// 
// 
// if (!word.startsWith(ENCODED_TOKEN_MARKER)) {
// throw new ParseException("Invalid RFC 2047 encoded-word: " + word);
// }
// 
// int charsetPos = word.indexOf('?', 2);
// if (charsetPos == -1) {
// throw new ParseException("Missing charset in RFC 2047 encoded-word: " + word);
// }
// 
// String charset = word.substring(2, charsetPos).toLowerCase(Locale.ENGLISH);
// 
// int encodingPos = word.indexOf('?', charsetPos + 1);
// if (encodingPos == -1) {
// throw new ParseException("Missing encoding in RFC 2047 encoded-word: " + word);
// }
// 
// String encoding = word.substring(charsetPos + 1, encodingPos);
// 
// int encodedTextPos = word.indexOf(ENCODED_TOKEN_FINISHER, encodingPos + 1);
// if (encodedTextPos == -1) {
// throw new ParseException("Missing encoded text in RFC 2047 encoded-word: " + word);
// }
// 
// String encodedText = word.substring(encodingPos + 1, encodedTextPos);
// 
// if (encodedText.length() == 0) {
// return "";
// }
// 
// try {
// ByteArrayOutputStream out = new ByteArrayOutputStream(encodedText.length());
// 
// byte[] encodedData = encodedText.getBytes(US_ASCII_CHARSET);
// 
// if (encoding.equals(BASE64_ENCODING_MARKER)) {
// Base64Decoder.decode(encodedData, out);
// } else if (encoding.equals(
// QUOTEDPRINTABLE_ENCODING_MARKER)) { // maybe quoted printable.
// QuotedPrintableDecoder.decode(encodedData, out);
// } else {
// throw new UnsupportedEncodingException("Unknown RFC 2047 encoding: " + encoding);
// }
// byte[] decodedData = out.toByteArray();
// return new String(decodedData, javaCharset(charset));
// } catch (IOException e) {
// throw new UnsupportedEncodingException("Invalid RFC 2047 encoding");
// }
// 


// TODO: Check the type mapping below!
return clz.invokeMember("decodeWord", word).as(String.class);
} catch (PolyglotException e) {
    throw (ParseException, UnsupportedEncodingException) ExceptionHandler.handle(e, "MimeUtility.decodeWord");
}
}
    private MimeUtility() {
// 

this.obj = clz.invokeMember("__init__");
}
}
