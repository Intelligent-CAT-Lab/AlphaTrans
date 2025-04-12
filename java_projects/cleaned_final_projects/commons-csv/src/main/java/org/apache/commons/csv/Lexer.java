/*
 * Licensed to the Apache Software Foundation (ASF) under one or more
 * contributor license agreements.  See the NOTICE file distributed with
 * this work for additional information regarding copyright ownership.
 * The ASF licenses this file to You under the Apache License, Version 2.0
 * (the "License"); you may not use this file except in compliance with
 * the License.  You may obtain a copy of the License at
 *
 *      http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */

package org.apache.commons.csv;

import static org.apache.commons.csv.Constants.BACKSPACE;
import static org.apache.commons.csv.Constants.CR;
import static org.apache.commons.csv.Constants.END_OF_STREAM;
import static org.apache.commons.csv.Constants.FF;
import static org.apache.commons.csv.Constants.LF;
import static org.apache.commons.csv.Constants.TAB;
import static org.apache.commons.csv.Constants.UNDEFINED;
import static org.apache.commons.csv.Token.Type.COMMENT;
import static org.apache.commons.csv.Token.Type.EOF;
import static org.apache.commons.csv.Token.Type.EORECORD;
import static org.apache.commons.csv.Token.Type.INVALID;
import static org.apache.commons.csv.Token.Type.TOKEN;

import java.io.Closeable;
import java.io.IOException;

/** Lexical analyzer. */
final class Lexer implements Closeable {

    private static final String CR_STRING = Character.toString(CR);
    private static final String LF_STRING = Character.toString(LF);

    /**
     * Constant char to use for disabling comments, escapes and encapsulation. The value -2 is used
     * because it won't be confused with an EOF signal (-1), and because the Unicode value {@code
     * FFFE} would be encoded as two chars (using surrogates) and thus there should never be a
     * collision with a real text char.
     */
    private static final char DISABLED = '\ufffe';

    private final char[] delimiter;
    private final char[] delimiterBuf;
    private final char[] escapeDelimiterBuf;
    private final char escape;
    private final char quoteChar;
    private final char commentStart;

    private final boolean ignoreSurroundingSpaces;
    private final boolean ignoreEmptyLines;

    /** The input stream */
    private final ExtendedBufferedReader reader;

    private String firstEol;

    private boolean isLastTokenDelimiter;

    Lexer(final CSVFormat format, final ExtendedBufferedReader reader) {
        this.reader = reader;
        this.delimiter = format.getDelimiterString().toCharArray();
        this.escape = mapNullToDisabled(format.getEscapeCharacter());
        this.quoteChar = mapNullToDisabled(format.getQuoteCharacter());
        this.commentStart = mapNullToDisabled(format.getCommentMarker());
        this.ignoreSurroundingSpaces = format.getIgnoreSurroundingSpaces();
        this.ignoreEmptyLines = format.getIgnoreEmptyLines();
        this.delimiterBuf = new char[delimiter.length - 1];
        this.escapeDelimiterBuf = new char[2 * delimiter.length - 1];
    }

    /**
     * Closes resources.
     *
     * @throws IOException If an I/O error occurs
     */
    @Override
    public void close() throws IOException {
        reader.close();
    }

    /**
     * Returns the current character position
     *
     * @return the current character position
     */
    long getCharacterPosition() {
        return reader.getPosition();
    }

    /**
     * Returns the current line number
     *
     * @return the current line number
     */
    long getCurrentLineNumber() {
        return reader.getCurrentLineNumber();
    }

    String getFirstEol() {
        return firstEol;
    }

    boolean isClosed() {
        return reader.isClosed();
    }

    boolean isCommentStart(final int ch) {
        return ch == commentStart;
    }

    /**
     * Determine whether the next characters constitute a delimiter through {@link
     * ExtendedBufferedReader#lookAhead(char[])}.
     *
     * @param ch the current character.
     * @return true if the next characters constitute a delimiter.
     * @throws IOException If an I/O error occurs.
     */
    boolean isDelimiter(final int ch) throws IOException {
        isLastTokenDelimiter = false;
        if (ch != delimiter[0]) {
            return false;
        }
        if (delimiter.length == 1) {
            isLastTokenDelimiter = true;
            return true;
        }
        reader.lookAhead1(delimiterBuf);
        for (int i = 0; i < delimiterBuf.length; i++) {
            if (delimiterBuf[i] != delimiter[i + 1]) {
                return false;
            }
        }
        final int count = reader.read1(delimiterBuf, 0, delimiterBuf.length);
        isLastTokenDelimiter = count != END_OF_STREAM;
        return isLastTokenDelimiter;
    }

    /**
     * Tests if the given character indicates end of file.
     *
     * @return true if the given character indicates end of file.
     */
    boolean isEndOfFile(final int ch) {
        return ch == END_OF_STREAM;
    }

    /**
     * Tests if the given character is the escape character.
     *
     * @return true if the given character is the escape character.
     */
    boolean isEscape(final int ch) {
        return ch == escape;
    }

    /**
     * Tests if the next characters constitute a escape delimiter through {@link
     * ExtendedBufferedReader#lookAhead(char[])}.
     *
     * <p>For example, for delimiter "[|]" and escape '!', return true if the next characters
     * constitute "![!|!]".
     *
     * @return true if the next characters constitute a escape delimiter.
     * @throws IOException If an I/O error occurs.
     */
    boolean isEscapeDelimiter() throws IOException {
        reader.lookAhead1(escapeDelimiterBuf);
        if (escapeDelimiterBuf[0] != delimiter[0]) {
            return false;
        }
        for (int i = 1; i < delimiter.length; i++) {
            if (escapeDelimiterBuf[2 * i] != delimiter[i]
                    || escapeDelimiterBuf[2 * i - 1] != escape) {
                return false;
            }
        }
        final int count = reader.read1(escapeDelimiterBuf, 0, escapeDelimiterBuf.length);
        return count != END_OF_STREAM;
    }

    private boolean isMetaChar(final int ch) {
        return ch == escape || ch == quoteChar || ch == commentStart;
    }

    boolean isQuoteChar(final int ch) {
        return ch == quoteChar;
    }

    /**
     * Tests if the current character represents the start of a line: a CR, LF or is at the start of
     * the file.
     *
     * @param ch the character to check
     * @return true if the character is at the start of a line.
     */
    boolean isStartOfLine(final int ch) {
        return ch == LF || ch == CR || ch == UNDEFINED;
    }

    private char mapNullToDisabled(final Character c) {
        return c == null ? DISABLED : c.charValue();
    }

    /**
     * Returns the next token.
     *
     * <p>A token corresponds to a term, a record change or an end-of-file indicator.
     *
     * @param token an existing Token object to reuse. The caller is responsible to initialize the
     *     Token.
     * @return the next token found.
     * @throws IOException on stream access error.
     */
    Token nextToken(final Token token) throws IOException {

        int lastChar = reader.getLastChar();

        int c = reader.read0();
        /*
         * Note: The following call will swallow LF if c == CR. But we don't need to know if the last char was CR or LF
         * - they are equivalent here.
         */
        boolean eol = readEndOfLine(c);

        if (ignoreEmptyLines) {
            while (eol && isStartOfLine(lastChar)) {
                lastChar = c;
                c = reader.read0();
                eol = readEndOfLine(c);
                if (isEndOfFile(c)) {
                    token.type = EOF;
                    return token;
                }
            }
        }

        if (isEndOfFile(lastChar) || !isLastTokenDelimiter && isEndOfFile(c)) {
            token.type = EOF;
            return token;
        }

        if (isStartOfLine(lastChar) && isCommentStart(c)) {
            final String line = reader.readLine();
            if (line == null) {
                token.type = EOF;
                return token;
            }
            final String comment = line.trim();
            token.content.append(comment);
            token.type = COMMENT;
            return token;
        }

        while (token.type == INVALID) {
            if (ignoreSurroundingSpaces) {
                while (Character.isWhitespace((char) c) && !isDelimiter(c) && !eol) {
                    c = reader.read0();
                    eol = readEndOfLine(c);
                }
            }

            if (isDelimiter(c)) {
                token.type = TOKEN;
            } else if (eol) {
                token.type = EORECORD;
            } else if (isQuoteChar(c)) {
                parseEncapsulatedToken(token);
            } else if (isEndOfFile(c)) {
                token.type = EOF;
                token.isReady = true; // there is data at EOF
            } else {
                parseSimpleToken(token, c);
            }
        }
        return token;
    }

    /**
     * Parses an encapsulated token.
     *
     * <p>Encapsulated tokens are surrounded by the given encapsulating-string. The encapsulator
     * itself might be included in the token using a doubling syntax (as "", '') or using escaping
     * (as in \", \'). Whitespaces before and after an encapsulated token are ignored. The token is
     * finished when one of the following conditions become true:
     *
     * <ul>
     *   <li>an unescaped encapsulator has been reached, and is followed by optional whitespace
     *       then:
     *       <ul>
     *         <li>delimiter (TOKEN)
     *         <li>end of line (EORECORD)
     *       </ul>
     *   <li>end of stream has been reached (EOF)
     * </ul>
     *
     * @param token the current token
     * @return a valid token object
     * @throws IOException on invalid state: EOF before closing encapsulator or invalid character
     *     before delimiter or EOL
     */
    private Token parseEncapsulatedToken(final Token token) throws IOException {
        token.isQuoted = true;
        final long startLineNumber = getCurrentLineNumber();
        int c;
        while (true) {
            c = reader.read0();

            if (isEscape(c)) {
                if (isEscapeDelimiter()) {
                    token.content.append(delimiter);
                } else {
                    final int unescaped = readEscape();
                    if (unescaped == END_OF_STREAM) { // unexpected char after escape
                        token.content.append((char) c).append((char) reader.getLastChar());
                    } else {
                        token.content.append((char) unescaped);
                    }
                }
            } else if (isQuoteChar(c)) {
                if (isQuoteChar(reader.lookAhead0())) {
                    c = reader.read0();
                    token.content.append((char) c);
                } else {
                    while (true) {
                        c = reader.read0();
                        if (isDelimiter(c)) {
                            token.type = TOKEN;
                            return token;
                        }
                        if (isEndOfFile(c)) {
                            token.type = EOF;
                            token.isReady = true; // There is data at EOF
                            return token;
                        }
                        if (readEndOfLine(c)) {
                            token.type = EORECORD;
                            return token;
                        }
                        if (!Character.isWhitespace((char) c)) {
                            throw new IOException(
                                    "(line "
                                            + getCurrentLineNumber()
                                            + ") invalid char between encapsulated token and"
                                            + " delimiter");
                        }
                    }
                }
            } else if (isEndOfFile(c)) {
                throw new IOException(
                        "(startline "
                                + startLineNumber
                                + ") EOF reached before encapsulated token finished");
            } else {
                token.content.append((char) c);
            }
        }
    }

    /**
     * Parses a simple token.
     *
     * <p>Simple token are tokens which are not surrounded by encapsulators. A simple token might
     * contain escaped delimiters (as \, or \;). The token is finished when one of the following
     * conditions become true:
     *
     * <ul>
     *   <li>end of line has been reached (EORECORD)
     *   <li>end of stream has been reached (EOF)
     *   <li>an unescaped delimiter has been reached (TOKEN)
     * </ul>
     *
     * @param token the current token
     * @param ch the current character
     * @return the filled token
     * @throws IOException on stream access error
     */
    private Token parseSimpleToken(final Token token, int ch) throws IOException {
        while (true) {
            if (readEndOfLine(ch)) {
                token.type = EORECORD;
                break;
            }
            if (isEndOfFile(ch)) {
                token.type = EOF;
                token.isReady = true; // There is data at EOF
                break;
            }
            if (isDelimiter(ch)) {
                token.type = TOKEN;
                break;
            }
            if (isEscape(ch)) {
                if (isEscapeDelimiter()) {
                    token.content.append(delimiter);
                } else {
                    final int unescaped = readEscape();
                    if (unescaped == END_OF_STREAM) { // unexpected char after escape
                        token.content.append((char) ch).append((char) reader.getLastChar());
                    } else {
                        token.content.append((char) unescaped);
                    }
                }
            } else {
                token.content.append((char) ch);
            }
            ch = reader.read0(); // continue
        }

        if (ignoreSurroundingSpaces) {
            trimTrailingSpaces(token.content);
        }

        return token;
    }

    /**
     * Greedily accepts \n, \r and \r\n This checker consumes silently the second
     * control-character...
     *
     * @return true if the given or next character is a line-terminator
     */
    boolean readEndOfLine(int ch) throws IOException {
        if (ch == CR && reader.lookAhead0() == LF) {
            ch = reader.read0();
            if (firstEol == null) {
                this.firstEol = Constants.CRLF;
            }
        }
        if (firstEol == null) {
            if (ch == LF) {
                this.firstEol = LF_STRING;
            } else if (ch == CR) {
                this.firstEol = CR_STRING;
            }
        }

        return ch == LF || ch == CR;
    }

    /**
     * Handle an escape sequence. The current character must be the escape character. On return, the
     * next character is available by calling {@link ExtendedBufferedReader#getLastChar()} on the
     * input stream.
     *
     * @return the unescaped character (as an int) or {@link Constants#END_OF_STREAM} if char
     *     following the escape is invalid.
     * @throws IOException if there is a problem reading the stream or the end of stream is
     *     detected: the escape character is not allowed at end of stream
     */
    int readEscape() throws IOException {
        final int ch = reader.read0();
        switch (ch) {
            case 'r':
                return CR;
            case 'n':
                return LF;
            case 't':
                return TAB;
            case 'b':
                return BACKSPACE;
            case 'f':
                return FF;
            case CR:
            case LF:
            case FF: // TODO is this correct?
            case TAB: // TODO is this correct? Do tabs need to be escaped?
            case BACKSPACE: // TODO is this correct?
                return ch;
            case END_OF_STREAM:
                throw new IOException("EOF whilst processing escape sequence");
            default:
                if (isMetaChar(ch)) {
                    return ch;
                }
                return END_OF_STREAM;
        }
    }

    void trimTrailingSpaces(final StringBuilder buffer) {
        int length = buffer.length();
        while (length > 0 && Character.isWhitespace(buffer.charAt(length - 1))) {
            length = length - 1;
        }
        if (length != buffer.length()) {
            buffer.setLength(length);
        }
    }
}
