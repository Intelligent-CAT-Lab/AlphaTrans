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

package org.apache.commons.codec.binary;

import org.apache.commons.codec.BinaryDecoder;
import org.apache.commons.codec.BinaryEncoder;
import org.apache.commons.codec.CharEncoding;
import org.apache.commons.codec.DecoderException;
import org.apache.commons.codec.EncoderException;

import java.nio.ByteBuffer;
import java.nio.charset.Charset;
import java.nio.charset.StandardCharsets;

/**
 * Converts hexadecimal Strings. The Charset used for certain operation can be set, the default is
 * set in {@link #DEFAULT_CHARSET_NAME}
 *
 * <p>This class is thread-safe.
 *
 * @since 1.1
 */
public class Hex implements BinaryEncoder, BinaryDecoder {

    /**
     * Default charset is {@link StandardCharsets#UTF_8}.
     *
     * @since 1.7
     */
    public static final Charset DEFAULT_CHARSET = StandardCharsets.UTF_8;

    /**
     * Default charset name is {@link CharEncoding#UTF_8}.
     *
     * @since 1.4
     */
    public static final String DEFAULT_CHARSET_NAME = CharEncoding.UTF_8;

    /** Used to build output as hex. */
    private static final char[] DIGITS_LOWER = {
        '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f'
    };

    /** Used to build output as hex. */
    private static final char[] DIGITS_UPPER = {
        '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F'
    };

    /**
     * Converts an array of characters representing hexadecimal values into an array of bytes of
     * those same values. The returned array will be half the length of the passed array, as it
     * takes two characters to represent any given byte. An exception is thrown if the passed char
     * array has an odd number of elements.
     *
     * @param data An array of characters containing hexadecimal digits
     * @return A byte array containing binary data decoded from the supplied char array.
     * @throws DecoderException Thrown if an odd number of characters or illegal characters are
     *     supplied
     */
    public static byte[] decodeHex0(final char[] data) throws DecoderException {
        final byte[] out = new byte[data.length >> 1];
        decodeHex1(data, out, 0);
        return out;
    }

    /**
     * Converts an array of characters representing hexadecimal values into an array of bytes of
     * those same values. The returned array will be half the length of the passed array, as it
     * takes two characters to represent any given byte. An exception is thrown if the passed char
     * array has an odd number of elements.
     *
     * @param data An array of characters containing hexadecimal digits
     * @param out A byte array to contain the binary data decoded from the supplied char array.
     * @param outOffset The position within {@code out} to start writing the decoded bytes.
     * @return the number of bytes written to {@code out}.
     * @throws DecoderException Thrown if an odd number of characters or illegal characters are
     *     supplied
     * @since 1.15
     */
    public static int decodeHex1(final char[] data, final byte[] out, final int outOffset)
            throws DecoderException {
        final int len = data.length;

        if ((len & 0x01) != 0) {
            throw new DecoderException("Odd number of characters.", null);
        }

        final int outLen = len >> 1;
        if (out.length - outOffset < outLen) {
            throw new DecoderException(
                    "Output array is not large enough to accommodate decoded data.", null);
        }

        for (int i = outOffset, j = 0; j < len; i++) {
            int f = toDigit(data[j], j) << 4;
            j++;
            f = f | toDigit(data[j], j);
            j++;
            out[i] = (byte) (f & 0xFF);
        }

        return outLen;
    }

    /**
     * Converts a String representing hexadecimal values into an array of bytes of those same
     * values. The returned array will be half the length of the passed String, as it takes two
     * characters to represent any given byte. An exception is thrown if the passed String has an
     * odd number of elements.
     *
     * @param data A String containing hexadecimal digits
     * @return A byte array containing binary data decoded from the supplied char array.
     * @throws DecoderException Thrown if an odd number of characters or illegal characters are
     *     supplied
     * @since 1.11
     */
    public static byte[] decodeHex2(final String data) throws DecoderException {
        return decodeHex0(data.toCharArray());
    }

    /**
     * Converts an array of bytes into an array of characters representing the hexadecimal values of
     * each byte in order. The returned array will be double the length of the passed array, as it
     * takes two characters to represent any given byte.
     *
     * @param data a byte[] to convert to hex characters
     * @return A char[] containing lower-case hexadecimal characters
     */
    public static char[] encodeHex0(final byte[] data) {
        return encodeHex1(data, true);
    }

    /**
     * Converts an array of bytes into an array of characters representing the hexadecimal values of
     * each byte in order. The returned array will be double the length of the passed array, as it
     * takes two characters to represent any given byte.
     *
     * @param data a byte[] to convert to Hex characters
     * @param toLowerCase {@code true} converts to lowercase, {@code false} to uppercase
     * @return A char[] containing hexadecimal characters in the selected case
     * @since 1.4
     */
    public static char[] encodeHex1(final byte[] data, final boolean toLowerCase) {
        return encodeHex2(data, toLowerCase ? DIGITS_LOWER : DIGITS_UPPER);
    }

    /**
     * Converts an array of bytes into an array of characters representing the hexadecimal values of
     * each byte in order. The returned array will be double the length of the passed array, as it
     * takes two characters to represent any given byte.
     *
     * @param data a byte[] to convert to hex characters
     * @param toDigits the output alphabet (must contain at least 16 chars)
     * @return A char[] containing the appropriate characters from the alphabet For best results,
     *     this should be either upper- or lower-case hex.
     * @since 1.4
     */
    protected static char[] encodeHex2(final byte[] data, final char[] toDigits) {
        final int dataLength = data.length;
        final char[] out = new char[dataLength << 1];
        encodeHex5(data, 0, dataLength, toDigits, out, 0);
        return out;
    }

    /**
     * Converts an array of bytes into an array of characters representing the hexadecimal values of
     * each byte in order.
     *
     * @param data a byte[] to convert to hex characters
     * @param dataOffset the position in {@code data} to start encoding from
     * @param dataLen the number of bytes from {@code dataOffset} to encode
     * @param toLowerCase {@code true} converts to lowercase, {@code false} to uppercase
     * @return A char[] containing the appropriate characters from the alphabet For best results,
     *     this should be either upper- or lower-case hex.
     * @since 1.15
     */
    public static char[] encodeHex3(
            final byte[] data, final int dataOffset, final int dataLen, final boolean toLowerCase) {
        final char[] out = new char[dataLen << 1];
        encodeHex5(data, dataOffset, dataLen, toLowerCase ? DIGITS_LOWER : DIGITS_UPPER, out, 0);
        return out;
    }

    /**
     * Converts an array of bytes into an array of characters representing the hexadecimal values of
     * each byte in order.
     *
     * @param data a byte[] to convert to hex characters
     * @param dataOffset the position in {@code data} to start encoding from
     * @param dataLen the number of bytes from {@code dataOffset} to encode
     * @param toLowerCase {@code true} converts to lowercase, {@code false} to uppercase
     * @param out a char[] which will hold the resultant appropriate characters from the alphabet.
     * @param outOffset the position within {@code out} at which to start writing the encoded
     *     characters.
     * @since 1.15
     */
    public static void encodeHex4(
            final byte[] data,
            final int dataOffset,
            final int dataLen,
            final boolean toLowerCase,
            final char[] out,
            final int outOffset) {
        encodeHex5(
                data,
                dataOffset,
                dataLen,
                toLowerCase ? DIGITS_LOWER : DIGITS_UPPER,
                out,
                outOffset);
    }

    /**
     * Converts an array of bytes into an array of characters representing the hexadecimal values of
     * each byte in order.
     *
     * @param data a byte[] to convert to hex characters
     * @param dataOffset the position in {@code data} to start encoding from
     * @param dataLen the number of bytes from {@code dataOffset} to encode
     * @param toDigits the output alphabet (must contain at least 16 chars)
     * @param out a char[] which will hold the resultant appropriate characters from the alphabet.
     * @param outOffset the position within {@code out} at which to start writing the encoded
     *     characters.
     */
    private static void encodeHex5(
            final byte[] data,
            final int dataOffset,
            final int dataLen,
            final char[] toDigits,
            final char[] out,
            final int outOffset) {
        for (int i = dataOffset, j = outOffset; i < dataOffset + dataLen; i++) {
            out[j++] = toDigits[(0xF0 & data[i]) >>> 4];
            out[j++] = toDigits[0x0F & data[i]];
        }
    }

    /**
     * Converts a byte buffer into an array of characters representing the hexadecimal values of
     * each byte in order. The returned array will be double the length of the passed array, as it
     * takes two characters to represent any given byte.
     *
     * <p>All bytes identified by {@link ByteBuffer#remaining()} will be used; after this method the
     * value {@link ByteBuffer#remaining() remaining()} will be zero.
     *
     * @param data a byte buffer to convert to hex characters
     * @return A char[] containing lower-case hexadecimal characters
     * @since 1.11
     */
    public static char[] encodeHex6(final ByteBuffer data) {
        return encodeHex7(data, true);
    }

    /**
     * Converts a byte buffer into an array of characters representing the hexadecimal values of
     * each byte in order. The returned array will be double the length of the passed array, as it
     * takes two characters to represent any given byte.
     *
     * <p>All bytes identified by {@link ByteBuffer#remaining()} will be used; after this method the
     * value {@link ByteBuffer#remaining() remaining()} will be zero.
     *
     * @param data a byte buffer to convert to hex characters
     * @param toLowerCase {@code true} converts to lowercase, {@code false} to uppercase
     * @return A char[] containing hexadecimal characters in the selected case
     * @since 1.11
     */
    public static char[] encodeHex7(final ByteBuffer data, final boolean toLowerCase) {
        return encodeHex8(data, toLowerCase ? DIGITS_LOWER : DIGITS_UPPER);
    }

    /**
     * Converts a byte buffer into an array of characters representing the hexadecimal values of
     * each byte in order. The returned array will be double the length of the passed array, as it
     * takes two characters to represent any given byte.
     *
     * <p>All bytes identified by {@link ByteBuffer#remaining()} will be used; after this method the
     * value {@link ByteBuffer#remaining() remaining()} will be zero.
     *
     * @param byteBuffer a byte buffer to convert to hex characters
     * @param toDigits the output alphabet (must be at least 16 characters)
     * @return A char[] containing the appropriate characters from the alphabet For best results,
     *     this should be either upper- or lower-case hex.
     * @since 1.11
     */
    protected static char[] encodeHex8(final ByteBuffer byteBuffer, final char[] toDigits) {
        return encodeHex2(toByteArray(byteBuffer), toDigits);
    }

    /**
     * Converts an array of bytes into a String representing the hexadecimal values of each byte in
     * order. The returned String will be double the length of the passed array, as it takes two
     * characters to represent any given byte.
     *
     * @param data a byte[] to convert to hex characters
     * @return A String containing lower-case hexadecimal characters
     * @since 1.4
     */
    public static String encodeHexString0(final byte[] data) {
        return new String(encodeHex0(data));
    }

    /**
     * Converts an array of bytes into a String representing the hexadecimal values of each byte in
     * order. The returned String will be double the length of the passed array, as it takes two
     * characters to represent any given byte.
     *
     * @param data a byte[] to convert to hex characters
     * @param toLowerCase {@code true} converts to lowercase, {@code false} to uppercase
     * @return A String containing lower-case hexadecimal characters
     * @since 1.11
     */
    public static String encodeHexString1(final byte[] data, final boolean toLowerCase) {
        return new String(encodeHex1(data, toLowerCase));
    }

    /**
     * Converts a byte buffer into a String representing the hexadecimal values of each byte in
     * order. The returned String will be double the length of the passed array, as it takes two
     * characters to represent any given byte.
     *
     * <p>All bytes identified by {@link ByteBuffer#remaining()} will be used; after this method the
     * value {@link ByteBuffer#remaining() remaining()} will be zero.
     *
     * @param data a byte buffer to convert to hex characters
     * @return A String containing lower-case hexadecimal characters
     * @since 1.11
     */
    public static String encodeHexString2(final ByteBuffer data) {
        return new String(encodeHex6(data));
    }

    /**
     * Converts a byte buffer into a String representing the hexadecimal values of each byte in
     * order. The returned String will be double the length of the passed array, as it takes two
     * characters to represent any given byte.
     *
     * <p>All bytes identified by {@link ByteBuffer#remaining()} will be used; after this method the
     * value {@link ByteBuffer#remaining() remaining()} will be zero.
     *
     * @param data a byte buffer to convert to hex characters
     * @param toLowerCase {@code true} converts to lowercase, {@code false} to uppercase
     * @return A String containing lower-case hexadecimal characters
     * @since 1.11
     */
    public static String encodeHexString3(final ByteBuffer data, final boolean toLowerCase) {
        return new String(encodeHex7(data, toLowerCase));
    }

    /**
     * Convert the byte buffer to a byte array. All bytes identified by {@link
     * ByteBuffer#remaining()} will be used.
     *
     * @param byteBuffer the byte buffer
     * @return the byte[]
     */
    private static byte[] toByteArray(final ByteBuffer byteBuffer) {
        final int remaining = byteBuffer.remaining();
        if (byteBuffer.hasArray()) {
            final byte[] byteArray = byteBuffer.array();
            if (remaining == byteArray.length) {
                byteBuffer.position(remaining);
                return byteArray;
            }
        }
        final byte[] byteArray = new byte[remaining];
        byteBuffer.get(byteArray);
        return byteArray;
    }

    /**
     * Converts a hexadecimal character to an integer.
     *
     * @param ch A character to convert to an integer digit
     * @param index The index of the character in the source
     * @return An integer
     * @throws DecoderException Thrown if ch is an illegal hex character
     */
    protected static int toDigit(final char ch, final int index) throws DecoderException {
        final int digit = Character.digit(ch, 16);
        if (digit == -1) {
            throw new DecoderException(
                    "Illegal hexadecimal character " + ch + " at index " + index, null);
        }
        return digit;
    }

    private final Charset charset;

    /** Creates a new codec with the default charset name {@link #DEFAULT_CHARSET} */
    public Hex(int constructorId, final String charsetName, final Charset charset) {
        if (constructorId == 1) {

            this.charset = charset;
        } else {

            this.charset = DEFAULT_CHARSET;
        }
    }

    public static Hex Hex0(final String charsetName) {
        return new Hex(1, null, Charset.forName(charsetName));
    }

    /**
     * Creates a new codec with the given Charset.
     *
     * @param charset the charset.
     * @since 1.7
     */

    /**
     * Creates a new codec with the given charset name.
     *
     * @param charsetName the charset name.
     * @throws java.nio.charset.UnsupportedCharsetException If the named charset is unavailable
     * @since 1.4
     * @since 1.7 throws UnsupportedCharsetException if the named charset is unavailable
     */

    /**
     * Converts an array of character bytes representing hexadecimal values into an array of bytes
     * of those same values. The returned array will be half the length of the passed array, as it
     * takes two characters to represent any given byte. An exception is thrown if the passed char
     * array has an odd number of elements.
     *
     * @param array An array of character bytes containing hexadecimal digits
     * @return A byte array containing binary data decoded from the supplied byte array
     *     (representing characters).
     * @throws DecoderException Thrown if an odd number of characters is supplied to this function
     * @see #decodeHex(char[])
     */
    @Override
    public byte[] decode(final byte[] array) throws DecoderException {
        return decode0(array);
    }

    public byte[] decode0(final byte[] array) throws DecoderException {
        return decodeHex0(new String(array, getCharset()).toCharArray());
    }

    /**
     * Converts a buffer of character bytes representing hexadecimal values into an array of bytes
     * of those same values. The returned array will be half the length of the passed array, as it
     * takes two characters to represent any given byte. An exception is thrown if the passed char
     * array has an odd number of elements.
     *
     * <p>All bytes identified by {@link ByteBuffer#remaining()} will be used; after this method the
     * value {@link ByteBuffer#remaining() remaining()} will be zero.
     *
     * @param buffer An array of character bytes containing hexadecimal digits
     * @return A byte array containing binary data decoded from the supplied byte array
     *     (representing characters).
     * @throws DecoderException Thrown if an odd number of characters is supplied to this function
     * @see #decodeHex(char[])
     * @since 1.11
     */
    public byte[] decode(final ByteBuffer buffer) throws DecoderException {
        return decode1(buffer);
    }

    public byte[] decode1(final ByteBuffer buffer) throws DecoderException {
        return decodeHex0(new String(toByteArray(buffer), getCharset()).toCharArray());
    }

    /**
     * Converts a String or an array of character bytes representing hexadecimal values into an
     * array of bytes of those same values. The returned array will be half the length of the passed
     * String or array, as it takes two characters to represent any given byte. An exception is
     * thrown if the passed char array has an odd number of elements.
     *
     * @param object A String, ByteBuffer, byte[], or an array of character bytes containing
     *     hexadecimal digits
     * @return A byte array containing binary data decoded from the supplied byte array
     *     (representing characters).
     * @throws DecoderException Thrown if an odd number of characters is supplied to this function
     *     or the object is not a String or char[]
     * @see #decodeHex(char[])
     */
    @Override
    public Object decode(final Object object) throws DecoderException {
        return decode2(object);
    }

    public Object decode2(final Object object) throws DecoderException {
        if (object instanceof String) {
            return decode2(((String) object).toCharArray());
        }
        if (object instanceof byte[]) {
            return decode0((byte[]) object);
        }
        if (object instanceof ByteBuffer) {
            return decode1((ByteBuffer) object);
        }
        try {
            return decodeHex0((char[]) object);
        } catch (final ClassCastException e) {
            throw new DecoderException(e.getMessage(), e);
        }
    }

    /**
     * Converts an array of bytes into an array of bytes for the characters representing the
     * hexadecimal values of each byte in order. The returned array will be double the length of the
     * passed array, as it takes two characters to represent any given byte.
     *
     * <p>The conversion from hexadecimal characters to the returned bytes is performed with the
     * charset named by {@link #getCharset()}.
     *
     * @param array a byte[] to convert to hex characters
     * @return A byte[] containing the bytes of the lower-case hexadecimal characters
     * @since 1.7 No longer throws IllegalStateException if the charsetName is invalid.
     * @see #encodeHex(byte[])
     */
    @Override
    public byte[] encode(final byte[] array) {
        return encode0(array);
    }

    public byte[] encode0(final byte[] array) {
        return encodeHexString0(array).getBytes(this.getCharset());
    }

    /**
     * Converts byte buffer into an array of bytes for the characters representing the hexadecimal
     * values of each byte in order. The returned array will be double the length of the passed
     * array, as it takes two characters to represent any given byte.
     *
     * <p>The conversion from hexadecimal characters to the returned bytes is performed with the
     * charset named by {@link #getCharset()}.
     *
     * <p>All bytes identified by {@link ByteBuffer#remaining()} will be used; after this method the
     * value {@link ByteBuffer#remaining() remaining()} will be zero.
     *
     * @param array a byte buffer to convert to hex characters
     * @return A byte[] containing the bytes of the lower-case hexadecimal characters
     * @see #encodeHex(byte[])
     * @since 1.11
     */
    public byte[] encode(final ByteBuffer array) {
        return encode1(array);
    }

    public byte[] encode1(final ByteBuffer array) {
        return encodeHexString2(array).getBytes(this.getCharset());
    }

    /**
     * Converts a String or an array of bytes into an array of characters representing the
     * hexadecimal values of each byte in order. The returned array will be double the length of the
     * passed String or array, as it takes two characters to represent any given byte.
     *
     * <p>The conversion from hexadecimal characters to bytes to be encoded to performed with the
     * charset named by {@link #getCharset()}.
     *
     * @param object a String, ByteBuffer, or byte[] to convert to hex characters
     * @return A char[] containing lower-case hexadecimal characters
     * @throws EncoderException Thrown if the given object is not a String or byte[]
     * @see #encodeHex(byte[])
     */
    @Override
    public Object encode(final Object object) throws EncoderException {
        return encode2(object);
    }

    public Object encode2(final Object object) throws EncoderException {
        final byte[] byteArray;
        if (object instanceof String) {
            byteArray = ((String) object).getBytes(this.getCharset());
        } else if (object instanceof ByteBuffer) {
            byteArray = toByteArray((ByteBuffer) object);
        } else {
            try {
                byteArray = (byte[]) object;
            } catch (final ClassCastException e) {
                throw new EncoderException(e.getMessage(), e);
            }
        }
        return encodeHex0(byteArray);
    }

    /**
     * Gets the charset.
     *
     * @return the charset.
     * @since 1.7
     */
    public Charset getCharset() {
        return this.charset;
    }

    /**
     * Gets the charset name.
     *
     * @return the charset name.
     * @since 1.4
     */
    public String getCharsetName() {
        return this.charset.name();
    }

    /**
     * Returns a string representation of the object, which includes the charset name.
     *
     * @return a string representation of the object.
     */
    @Override
    public String toString() {
        return super.toString() + "[charsetName=" + this.charset + "]";
    }
}
