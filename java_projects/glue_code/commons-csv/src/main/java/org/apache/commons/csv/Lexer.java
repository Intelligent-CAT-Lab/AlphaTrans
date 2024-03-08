package org.apache.commons.csv;

import static org.apache.commons.csv.Constants.CR;
import static org.apache.commons.csv.Constants.LF;

import java.io.Closeable;
import java.io.IOException;
import org.graalvm.polyglot.PolyglotException;
import org.graalvm.polyglot.Value;

final class Lexer implements Closeable {
  private static final char DISABLED = '\ufffe';
  private static final String LF_STRING = Character.toString(LF);
  private static final String CR_STRING = Character.toString(CR);
  private static Value clz = ContextInitializer.getPythonClass("/Lexer.py", "Lexer");
  private Value obj;

  public Lexer(Value obj) {
    this.obj = obj;
  }

  public Value getPythonObject() {
    return obj;
  }

  public void close() throws IOException {
    try {
      //
      // reader.close();
      //

      obj.invokeMember("close");
    } catch (PolyglotException e) {
      // TODO: Handle IOException
      throw (IOException) ExceptionHandler.handle(e, "Lexer.close");
    }
  }

  private Token parseSimpleToken(final Token token, int ch) throws IOException {
    try {
      //
      // while (true) {
      // if (readEndOfLine(ch)) {
      // token.type = EORECORD;
      // break;
      // }
      // if (isEndOfFile(ch)) {
      // token.type = EOF;
      // token.isReady = true; // There is data at EOF
      // break;
      // }
      // if (isDelimiter(ch)) {
      // token.type = TOKEN;
      // break;
      // }
      // if (isEscape(ch)) {
      // if (isEscapeDelimiter()) {
      // token.content.append(delimiter);
      // } else {
      // final int unescaped = readEscape();
      // if (unescaped == END_OF_STREAM) { // unexpected char after escape
      // token.content.append((char) ch).append((char) reader.getLastChar());
      // } else {
      // token.content.append((char) unescaped);
      // }
      // }
      // } else {
      // token.content.append((char) ch);
      // }
      // ch = reader.read0(); // continue
      // }
      //
      // if (ignoreSurroundingSpaces) {
      // trimTrailingSpaces(token.content);
      // }
      //
      // return token;
      //

      // TODO: Check the type mapping below!
      return obj.invokeMember("parseSimpleToken", token, ch).as(Token.class);
    } catch (PolyglotException e) {
      // TODO: Handle IOException
      throw (IOException) ExceptionHandler.handle(e, "Lexer.parseSimpleToken");
    }
  }

  private Token parseEncapsulatedToken(final Token token) throws IOException {
    try {
      //
      // token.isQuoted = true;
      // final long startLineNumber = getCurrentLineNumber();
      // int c;
      // while (true) {
      // c = reader.read0();
      //
      // if (isEscape(c)) {
      // if (isEscapeDelimiter()) {
      // token.content.append(delimiter);
      // } else {
      // final int unescaped = readEscape();
      // if (unescaped == END_OF_STREAM) { // unexpected char after escape
      // token.content.append((char) c).append((char) reader.getLastChar());
      // } else {
      // token.content.append((char) unescaped);
      // }
      // }
      // } else if (isQuoteChar(c)) {
      // if (isQuoteChar(reader.lookAhead0())) {
      // c = reader.read0();
      // token.content.append((char) c);
      // } else {
      // while (true) {
      // c = reader.read0();
      // if (isDelimiter(c)) {
      // token.type = TOKEN;
      // return token;
      // }
      // if (isEndOfFile(c)) {
      // token.type = EOF;
      // token.isReady = true; // There is data at EOF
      // return token;
      // }
      // if (readEndOfLine(c)) {
      // token.type = EORECORD;
      // return token;
      // }
      // if (!Character.isWhitespace((char) c)) {
      // throw new IOException(
      // "(line "
      // + getCurrentLineNumber()
      // + ") invalid char between encapsulated token and"
      // + " delimiter");
      // }
      // }
      // }
      // } else if (isEndOfFile(c)) {
      // throw new IOException(
      // "(startline "
      // + startLineNumber
      // + ") EOF reached before encapsulated token finished");
      // } else {
      // token.content.append((char) c);
      // }
      // }
      //

      // TODO: Check the type mapping below!
      return obj.invokeMember("parseEncapsulatedToken", token).as(Token.class);
    } catch (PolyglotException e) {
      // TODO: Handle IOException
      throw (IOException) ExceptionHandler.handle(e, "Lexer.parseEncapsulatedToken");
    }
  }

  private char mapNullToDisabled(final Character c) {
    //
    // return c == null ? DISABLED : c.charValue();
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("mapNullToDisabled", c).as(char.class);
  }

  private boolean isMetaChar(final int ch) {
    //
    // return ch == escape || ch == quoteChar || ch == commentStart;
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("isMetaChar", ch).as(boolean.class);
  }

  void trimTrailingSpaces(final StringBuilder buffer) {
    //
    // int length = buffer.length();
    // while (length > 0 && Character.isWhitespace(buffer.charAt(length - 1))) {
    // length = length - 1;
    // }
    // if (length != buffer.length()) {
    // buffer.setLength(length);
    // }
    //

    obj.invokeMember("trimTrailingSpaces", buffer);
  }

  int readEscape() throws IOException {
    try {
      //
      // final int ch = reader.read0();
      // switch (ch) {
      // case 'r':
      // return CR;
      // case 'n':
      // return LF;
      // case 't':
      // return TAB;
      // case 'b':
      // return BACKSPACE;
      // case 'f':
      // return FF;
      // case CR:
      // case LF:
      // case FF: // TODO is this correct?
      // case TAB: // TODO is this correct? Do tabs need to be escaped?
      // case BACKSPACE: // TODO is this correct?
      // return ch;
      // case END_OF_STREAM:
      // throw new IOException("EOF whilst processing escape sequence");
      // default:
      // if (isMetaChar(ch)) {
      // return ch;
      // }
      // return END_OF_STREAM;
      // }
      //

      // TODO: Check the type mapping below!
      return obj.invokeMember("readEscape").as(int.class);
    } catch (PolyglotException e) {
      // TODO: Handle IOException
      throw (IOException) ExceptionHandler.handle(e, "Lexer.readEscape");
    }
  }

  boolean readEndOfLine(int ch) throws IOException {
    try {
      //
      // if (ch == CR && reader.lookAhead0() == LF) {
      // ch = reader.read0();
      // if (firstEol == null) {
      // this.firstEol = Constants.CRLF;
      // }
      // }
      // if (firstEol == null) {
      // if (ch == LF) {
      // this.firstEol = LF_STRING;
      // } else if (ch == CR) {
      // this.firstEol = CR_STRING;
      // }
      // }
      //
      // return ch == LF || ch == CR;
      //

      // TODO: Check the type mapping below!
      return obj.invokeMember("readEndOfLine", ch).as(boolean.class);
    } catch (PolyglotException e) {
      // TODO: Handle IOException
      throw (IOException) ExceptionHandler.handle(e, "Lexer.readEndOfLine");
    }
  }

  Token nextToken(final Token token) throws IOException {
    try {
      //
      //
      // int lastChar = reader.getLastChar();
      //
      // int c = reader.read0();
      // /*
      // * Note: The following call will swallow LF if c == CR. But we don't need to know if the
      // last char was CR or LF
      // * - they are equivalent here.
      // */
      // boolean eol = readEndOfLine(c);
      //
      // if (ignoreEmptyLines) {
      // while (eol && isStartOfLine(lastChar)) {
      // lastChar = c;
      // c = reader.read0();
      // eol = readEndOfLine(c);
      // if (isEndOfFile(c)) {
      // token.type = EOF;
      // return token;
      // }
      // }
      // }
      //
      // if (isEndOfFile(lastChar) || !isLastTokenDelimiter && isEndOfFile(c)) {
      // token.type = EOF;
      // return token;
      // }
      //
      // if (isStartOfLine(lastChar) && isCommentStart(c)) {
      // final String line = reader.readLine();
      // if (line == null) {
      // token.type = EOF;
      // return token;
      // }
      // final String comment = line.trim();
      // token.content.append(comment);
      // token.type = COMMENT;
      // return token;
      // }
      //
      // while (token.type == INVALID) {
      // if (ignoreSurroundingSpaces) {
      // while (Character.isWhitespace((char) c) && !isDelimiter(c) && !eol) {
      // c = reader.read0();
      // eol = readEndOfLine(c);
      // }
      // }
      //
      // if (isDelimiter(c)) {
      // token.type = TOKEN;
      // } else if (eol) {
      // token.type = EORECORD;
      // } else if (isQuoteChar(c)) {
      // parseEncapsulatedToken(token);
      // } else if (isEndOfFile(c)) {
      // token.type = EOF;
      // token.isReady = true; // there is data at EOF
      // } else {
      // parseSimpleToken(token, c);
      // }
      // }
      // return token;
      //

      // TODO: Check the type mapping below!
      return obj.invokeMember("nextToken", token).as(Token.class);
    } catch (PolyglotException e) {
      // TODO: Handle IOException
      throw (IOException) ExceptionHandler.handle(e, "Lexer.nextToken");
    }
  }

  boolean isStartOfLine(final int ch) {
    //
    // return ch == LF || ch == CR || ch == UNDEFINED;
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("isStartOfLine", ch).as(boolean.class);
  }

  boolean isQuoteChar(final int ch) {
    //
    // return ch == quoteChar;
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("isQuoteChar", ch).as(boolean.class);
  }

  boolean isEscapeDelimiter() throws IOException {
    try {
      //
      // reader.lookAhead1(escapeDelimiterBuf);
      // if (escapeDelimiterBuf[0] != delimiter[0]) {
      // return false;
      // }
      // for (int i = 1; i < delimiter.length; i++) {
      // if (escapeDelimiterBuf[2 * i] != delimiter[i]
      // || escapeDelimiterBuf[2 * i - 1] != escape) {
      // return false;
      // }
      // }
      // final int count = reader.read1(escapeDelimiterBuf, 0, escapeDelimiterBuf.length);
      // return count != END_OF_STREAM;
      //

      // TODO: Check the type mapping below!
      return obj.invokeMember("isEscapeDelimiter").as(boolean.class);
    } catch (PolyglotException e) {
      // TODO: Handle IOException
      throw (IOException) ExceptionHandler.handle(e, "Lexer.isEscapeDelimiter");
    }
  }

  boolean isEscape(final int ch) {
    //
    // return ch == escape;
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("isEscape", ch).as(boolean.class);
  }

  boolean isEndOfFile(final int ch) {
    //
    // return ch == END_OF_STREAM;
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("isEndOfFile", ch).as(boolean.class);
  }

  boolean isDelimiter(final int ch) throws IOException {
    try {
      //
      // isLastTokenDelimiter = false;
      // if (ch != delimiter[0]) {
      // return false;
      // }
      // if (delimiter.length == 1) {
      // isLastTokenDelimiter = true;
      // return true;
      // }
      // reader.lookAhead1(delimiterBuf);
      // for (int i = 0; i < delimiterBuf.length; i++) {
      // if (delimiterBuf[i] != delimiter[i + 1]) {
      // return false;
      // }
      // }
      // final int count = reader.read1(delimiterBuf, 0, delimiterBuf.length);
      // isLastTokenDelimiter = count != END_OF_STREAM;
      // return isLastTokenDelimiter;
      //

      // TODO: Check the type mapping below!
      return obj.invokeMember("isDelimiter", ch).as(boolean.class);
    } catch (PolyglotException e) {
      // TODO: Handle IOException
      throw (IOException) ExceptionHandler.handle(e, "Lexer.isDelimiter");
    }
  }

  boolean isCommentStart(final int ch) {
    //
    // return ch == commentStart;
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("isCommentStart", ch).as(boolean.class);
  }

  boolean isClosed() {
    //
    // return reader.isClosed();
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("isClosed").as(boolean.class);
  }

  String getFirstEol() {
    //
    // return firstEol;
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("getFirstEol").as(String.class);
  }

  long getCurrentLineNumber() {
    //
    // return reader.getCurrentLineNumber();
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("getCurrentLineNumber").as(long.class);
  }

  long getCharacterPosition() {
    //
    // return reader.getPosition();
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("getCharacterPosition").as(long.class);
  }

  Lexer(final CSVFormat format, final ExtendedBufferedReader reader) {
    //
    // this.reader = reader;
    // this.delimiter = format.getDelimiterString().toCharArray();
    // this.escape = mapNullToDisabled(format.getEscapeCharacter());
    // this.quoteChar = mapNullToDisabled(format.getQuoteCharacter());
    // this.commentStart = mapNullToDisabled(format.getCommentMarker());
    // this.ignoreSurroundingSpaces = format.getIgnoreSurroundingSpaces();
    // this.ignoreEmptyLines = format.getIgnoreEmptyLines();
    // this.delimiterBuf = new char[delimiter.length - 1];
    // this.escapeDelimiterBuf = new char[2 * delimiter.length - 1];
    //

    this.obj = clz.invokeMember("__init__", format, reader);
  }
}
