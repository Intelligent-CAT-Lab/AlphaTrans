
/*
  Licensed to the Apache Software Foundation (ASF) under one or more
  contributor license agreements.  See the NOTICE file distributed with
  this work for additional information regarding copyright ownership.
  The ASF licenses this file to You under the Apache License, Version 2.0
  (the "License"); you may not use this file except in compliance with
  the License.  You may obtain a copy of the License at

      http://www.apache.org/licenses/LICENSE-2.0

  Unless required by applicable law or agreed to in writing, software
  distributed under the License is distributed on an "AS IS" BASIS,
  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
  See the License for the specific language governing permissions and
  limitations under the License.
 */


package org.apache.commons.codec.binary;

import org.apache.commons.codec.CodecPolicy;

/**
 * Provides Base32 encoding and decoding as defined by <a
 * href="http://www.ietf.org/rfc/rfc4648.txt">RFC 4648</a>.
 *
 * <p>The class can be parameterized in the following manner with various constructors:
 *
 * <ul>
 *   <li>Whether to use the "base32hex" variant instead of the default "base32"
 *   <li>Line length: Default 76. Line length that aren't multiples of 8 will still essentially end
 *       up being multiples of 8 in the encoded data.
 *   <li>Line separator: Default is CRLF ("\r\n")
 * </ul>
 *
 * <p>This class operates directly on byte streams, and not character streams.
 *
 * <p>This class is thread-safe.
 *
 * @see <a href="http://www.ietf.org/rfc/rfc4648.txt">RFC 4648</a>
 * @since 1.5
 */
public class Base32 extends BaseNCodec {

    /**
     * BASE32 characters are 5 bits in length. They are formed by taking a block of five octets to
     * form a 40-bit string, which is converted into eight BASE32 characters.
     */
    private static final int BITS_PER_ENCODED_BYTE = 5;

    private static final int BYTES_PER_ENCODED_BLOCK = 8;
    private static final int BYTES_PER_UNENCODED_BLOCK = 5;

    /**
     * This array is a lookup table that translates Unicode characters drawn from the "Base32
     * Alphabet" (as specified in Table 3 of RFC 4648) into their 5-bit positive integer
     * equivalents. Characters that are not in the Base32 alphabet but fall within the bounds of the
     * array are translated to -1.
     */
    private static final byte[] DECODE_TABLE = {
        -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, // 00-0f
        -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, // 10-1f
        -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, // 20-2f
        -1, -1, 26, 27, 28, 29, 30, 31, -1, -1, -1, -1, -1, -1, -1, -1, // 30-3f 2-7
        -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, // 40-4f A-O
        15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, // 50-5a P-Z
                -1, -1, -1, -1, -1, // 5b-5f
        -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, // 60-6f a-o
        15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, // 70-7a p-z
    };

    /**
     * This array is a lookup table that translates 5-bit positive integer index values into their
     * "Base32 Alphabet" equivalents as specified in Table 3 of RFC 4648.
     */
    private static final byte[] ENCODE_TABLE = {
        'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
        'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',
        '2', '3', '4', '5', '6', '7',
    };

    /**
     * This array is a lookup table that translates Unicode characters drawn from the "Base32 Hex
     * Alphabet" (as specified in Table 4 of RFC 4648) into their 5-bit positive integer
     * equivalents. Characters that are not in the Base32 Hex alphabet but fall within the bounds of
     * the array are translated to -1.
     */
    private static final byte[] HEX_DECODE_TABLE = {
        -1,
        -1,
        -1,
        -1,
        -1,
        -1,
        -1,
        -1,
        -1,
        -1,
        -1,
        -1,
        -1,
        -1,
        -1,
        -1, // 00-0f
        -1,
        -1,
        -1,
        -1,
        -1,
        -1,
        -1,
        -1,
        -1,
        -1,
        -1,
        -1,
        -1,
        -1,
        -1,
        -1, // 10-1f
        -1,
        -1,
        -1,
        -1,
        -1,
        -1,
        -1,
        -1,
        -1,
        -1,
        -1,
        -1,
        -1,
        -1,
        -1,
        -1, // 20-2f
        0,
        1,
        2,
        3,
        4,
        5,
        6,
        7,
        8,
        9,
        -1,
        -1,
        -1,
        -1,
        -1,
        -1, // 30-3f 0-9
        -1,
        10,
        11,
        12,
        13,
        14,
        15,
        16,
        17,
        18,
        19,
        20,
        21,
        22,
        23,
        24, // 40-4f A-O
        25,
        26,
        27,
        28,
        29,
        30,
        31, // 50-56 P-V
        -1,
        -1,
        -1,
        -1,
        -1,
        -1,
        -1,
        -1,
        -1, // 57-5f
        -1,
        10,
        11,
        12,
        13,
        14,
        15,
        16,
        17,
        18,
        19,
        20,
        21,
        22,
        23,
        24, // 60-6f a-o
        25,
        26,
        27,
        28,
        29,
        30,
        31 // 70-76 p-v
    };

    /**
     * This array is a lookup table that translates 5-bit positive integer index values into their
     * "Base32 Hex Alphabet" equivalents as specified in Table 4 of RFC 4648.
     */
    private static final byte[] HEX_ENCODE_TABLE = {
        '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H',
        'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V',
    };

    /** Mask used to extract 5 bits, used when encoding Base32 bytes */
    private static final int MASK_5BITS = 0x1f;

    /** Mask used to extract 4 bits, used when decoding final trailing character. */
    private static final long MASK_4BITS = 0x0fL;

    /** Mask used to extract 3 bits, used when decoding final trailing character. */
    private static final long MASK_3BITS = 0x07L;

    /** Mask used to extract 2 bits, used when decoding final trailing character. */
    private static final long MASK_2BITS = 0x03L;

    /** Mask used to extract 1 bits, used when decoding final trailing character. */
    private static final long MASK_1BITS = 0x01L;

    /**
     * Place holder for the bytes we're dealing with for our based logic. Bitwise operations store
     * and extract the encoding or decoding from this variable.
     */

    /**
     * Convenience variable to help us determine when our buffer is going to run out of room and
     * needs resizing. {@code decodeSize = {@link #BYTES_PER_ENCODED_BLOCK} - 1 +
     * lineSeparator.length;}
     */
    private final int decodeSize;

    /** Decode table to use. */
    private final byte[] decodeTable;

    /**
     * Convenience variable to help us determine when our buffer is going to run out of room and
     * needs resizing. {@code encodeSize = {@link #BYTES_PER_ENCODED_BLOCK} + lineSeparator.length;}
     */
    private final int encodeSize;

    /** Encode table to use. */
    private final byte[] encodeTable;

    /** Line separator for encoding. Not used when decoding. Only used if lineLength &gt; 0. */
    private final byte[] lineSeparator;

    /**
     * Creates a Base32 codec used for decoding and encoding.
     *
     * <p>When encoding the line length is 0 (no chunking).
     */
    public static Base32 Base320() {
        return Base321(false);
    }

    /**
     * Creates a Base32 codec used for decoding and encoding.
     *
     * <p>When encoding the line length is 0 (no chunking).
     *
     * @param useHex if {@code true} then use Base32 Hex alphabet
     */
    public static Base32 Base321(final boolean useHex) {
        return Base327(0, null, useHex, PAD_DEFAULT);
    }

    /**
     * Creates a Base32 codec used for decoding and encoding.
     *
     * <p>When encoding the line length is 0 (no chunking).
     *
     * @param useHex if {@code true} then use Base32 Hex alphabet
     * @param padding byte used as padding byte.
     */
    public static Base32 Base322(final boolean useHex, final byte padding) {
        return Base327(0, null, useHex, padding);
    }

    /**
     * Creates a Base32 codec used for decoding and encoding.
     *
     * <p>When encoding the line length is 0 (no chunking).
     *
     * @param pad byte used as padding byte.
     */
    public static Base32 Base323(final byte pad) {
        return Base322(false, pad);
    }

    /**
     * Creates a Base32 codec used for decoding and encoding.
     *
     * <p>When encoding the line length is given in the constructor, the line separator is CRLF.
     *
     * @param lineLength Each line of encoded data will be at most of the given length (rounded down
     *     to nearest multiple of 8). If lineLength &lt;= 0, then the output will not be divided
     *     into lines (chunks). Ignored when decoding.
     */
    public static Base32 Base324(final int lineLength) {
        return Base325(lineLength, CHUNK_SEPARATOR);
    }

    /**
     * Creates a Base32 codec used for decoding and encoding.
     *
     * <p>When encoding the line length and line separator are given in the constructor.
     *
     * <p>Line lengths that aren't multiples of 8 will still essentially end up being multiples of 8
     * in the encoded data.
     *
     * @param lineLength Each line of encoded data will be at most of the given length (rounded down
     *     to nearest multiple of 8). If lineLength &lt;= 0, then the output will not be divided
     *     into lines (chunks). Ignored when decoding.
     * @param lineSeparator Each line of encoded data will end with this sequence of bytes.
     * @throws IllegalArgumentException Thrown when the {@code lineSeparator} contains Base32
     *     characters.
     */
    public static Base32 Base325(final int lineLength, final byte[] lineSeparator) {
        return Base327(lineLength, lineSeparator, false, PAD_DEFAULT);
    }

    /**
     * Creates a Base32 / Base32 Hex codec used for decoding and encoding.
     *
     * <p>When encoding the line length and line separator are given in the constructor.
     *
     * <p>Line lengths that aren't multiples of 8 will still essentially end up being multiples of 8
     * in the encoded data.
     *
     * @param lineLength Each line of encoded data will be at most of the given length (rounded down
     *     to nearest multiple of 8). If lineLength &lt;= 0, then the output will not be divided
     *     into lines (chunks). Ignored when decoding.
     * @param lineSeparator Each line of encoded data will end with this sequence of bytes.
     * @param useHex if {@code true}, then use Base32 Hex alphabet, otherwise use Base32 alphabet
     * @throws IllegalArgumentException Thrown when the {@code lineSeparator} contains Base32
     *     characters. Or the lineLength &gt; 0 and lineSeparator is null.
     */
    public static Base32 Base326(
            final int lineLength, final byte[] lineSeparator, final boolean useHex) {
        return Base327(lineLength, lineSeparator, useHex, PAD_DEFAULT);
    }

    /**
     * Creates a Base32 / Base32 Hex codec used for decoding and encoding.
     *
     * <p>When encoding the line length and line separator are given in the constructor.
     *
     * <p>Line lengths that aren't multiples of 8 will still essentially end up being multiples of 8
     * in the encoded data.
     *
     * @param lineLength Each line of encoded data will be at most of the given length (rounded down
     *     to nearest multiple of 8). If lineLength &lt;= 0, then the output will not be divided
     *     into lines (chunks). Ignored when decoding.
     * @param lineSeparator Each line of encoded data will end with this sequence of bytes.
     * @param useHex if {@code true}, then use Base32 Hex alphabet, otherwise use Base32 alphabet
     * @param padding byte used as padding byte.
     * @throws IllegalArgumentException Thrown when the {@code lineSeparator} contains Base32
     *     characters. Or the lineLength &gt; 0 and lineSeparator is null.
     */
    public static Base32 Base327(
            final int lineLength,
            final byte[] lineSeparator,
            final boolean useHex,
            final byte padding) {
        return new Base32(lineLength, lineSeparator, useHex, padding, DECODING_POLICY_DEFAULT);
    }

    /**
     * Creates a Base32 / Base32 Hex codec used for decoding and encoding.
     *
     * <p>When encoding the line length and line separator are given in the constructor.
     *
     * <p>Line lengths that aren't multiples of 8 will still essentially end up being multiples of 8
     * in the encoded data.
     *
     * @param lineLength Each line of encoded data will be at most of the given length (rounded down
     *     to nearest multiple of 8). If lineLength &lt;= 0, then the output will not be divided
     *     into lines (chunks). Ignored when decoding.
     * @param lineSeparator Each line of encoded data will end with this sequence of bytes.
     * @param useHex if {@code true}, then use Base32 Hex alphabet, otherwise use Base32 alphabet
     * @param padding byte used as padding byte.
     * @param decodingPolicy The decoding policy.
     * @throws IllegalArgumentException Thrown when the {@code lineSeparator} contains Base32
     *     characters. Or the lineLength &gt; 0 and lineSeparator is null.
     * @since 1.15
     */
    public Base32(
            final int lineLength,
            final byte[] lineSeparator,
            final boolean useHex,
            final byte padding,
            final CodecPolicy decodingPolicy) {
        super(  2,
                BYTES_PER_UNENCODED_BLOCK,
                BYTES_PER_ENCODED_BLOCK,
                lineLength,
                lineSeparator == null ? 0 : lineSeparator.length,
                padding,
                decodingPolicy);
        if (useHex) {
            this.encodeTable = HEX_ENCODE_TABLE;
            this.decodeTable = HEX_DECODE_TABLE;
        } else {
            this.encodeTable = ENCODE_TABLE;
            this.decodeTable = DECODE_TABLE;
        }
        if (lineLength > 0) {
            if (lineSeparator == null) {
                throw new IllegalArgumentException(
                        "lineLength " + lineLength + " > 0, but lineSeparator is null");
            }
            if (containsAlphabetOrPad(lineSeparator)) {
                final String sep = StringUtils.newStringUtf8(lineSeparator);
                throw new IllegalArgumentException(
                        "lineSeparator must not contain Base32 characters: [" + sep + "]");
            }
            this.encodeSize = BYTES_PER_ENCODED_BLOCK + lineSeparator.length;
            this.lineSeparator = lineSeparator.clone();
        } else {
            this.encodeSize = BYTES_PER_ENCODED_BLOCK;
            this.lineSeparator = null;
        }
        this.decodeSize = this.encodeSize - 1;

        if (isInAlphabet0(padding) || isWhiteSpace(padding)) {
            throw new IllegalArgumentException("pad must not be in alphabet or whitespace");
        }
    }

    /**
     * Decodes all of the provided data, starting at inPos, for inAvail bytes. Should be called at
     * least twice: once with the data to decode, and once with inAvail set to "-1" to alert decoder
     * that EOF has been reached. The "-1" call is not necessary when decoding, but it doesn't hurt,
     * either.
     *
     * <p>Ignores all non-Base32 characters. This is how chunked (e.g. 76 character) data is
     * handled, since CR and LF are silently ignored, but has implications for other bytes, too.
     * This method subscribes to the garbage-in, garbage-out philosophy: it will not check the
     * provided data for validity.
     *
     * <p>Output is written to {@link org.apache.commons.codec.binary.BaseNCodec.Context#buffer
     * Context#buffer} as 8-bit octets, using {@link
     * org.apache.commons.codec.binary.BaseNCodec.Context#pos Context#pos} as the buffer position
     *
     * @param input byte[] array of ascii data to Base32 decode.
     * @param inPos Position to start reading data from.
     * @param inAvail Amount of bytes available from input for decoding.
     * @param context the context to be used
     */
    @Override
    void decode1(final byte[] input, int inPos, final int inAvail, final Context context) {

        if (context.eof) {
            return;
        }
        if (inAvail < 0) {
            context.eof = true;
        }
        for (int i = 0; i < inAvail; i++) {
            final byte b = input[inPos++];
            if (b == pad) {
                context.eof = true;
                break;
            }
            final byte[] buffer = ensureBufferSize(decodeSize, context);
            if (b >= 0 && b < this.decodeTable.length) {
                final int result = this.decodeTable[b];
                if (result >= 0) {
                    context.modulus = (context.modulus + 1) % BYTES_PER_ENCODED_BLOCK;
                    context.lbitWorkArea = (context.lbitWorkArea << BITS_PER_ENCODED_BYTE) + result;
                    if (context.modulus == 0) { // we can output the 5 bytes
                        buffer[context.pos++] = (byte) ((context.lbitWorkArea >> 32) & MASK_8BITS);
                        buffer[context.pos++] = (byte) ((context.lbitWorkArea >> 24) & MASK_8BITS);
                        buffer[context.pos++] = (byte) ((context.lbitWorkArea >> 16) & MASK_8BITS);
                        buffer[context.pos++] = (byte) ((context.lbitWorkArea >> 8) & MASK_8BITS);
                        buffer[context.pos++] = (byte) (context.lbitWorkArea & MASK_8BITS);
                    }
                }
            }
        }

        if (context.eof && context.modulus > 0) { // if modulus == 0, nothing to do
            final byte[] buffer = ensureBufferSize(decodeSize, context);

            switch (context.modulus) {
                case 1: // 5 bits - either ignore entirely, or raise an exception
                    validateTrailingCharacters();
                case 2: // 10 bits, drop 2 and output one byte
                    validateCharacter(MASK_2BITS, context);
                    buffer[context.pos++] = (byte) ((context.lbitWorkArea >> 2) & MASK_8BITS);
                    break;
                case 3: // 15 bits, drop 7 and output 1 byte, or raise an exception
                    validateTrailingCharacters();
                    buffer[context.pos++] = (byte) ((context.lbitWorkArea >> 7) & MASK_8BITS);
                    break;
                case 4: // 20 bits = 2*8 + 4
                    validateCharacter(MASK_4BITS, context);
                    context.lbitWorkArea = context.lbitWorkArea >> 4; // drop 4 bits
                    buffer[context.pos++] = (byte) ((context.lbitWorkArea >> 8) & MASK_8BITS);
                    buffer[context.pos++] = (byte) ((context.lbitWorkArea) & MASK_8BITS);
                    break;
                case 5: // 25 bits = 3*8 + 1
                    validateCharacter(MASK_1BITS, context);
                    context.lbitWorkArea = context.lbitWorkArea >> 1;
                    buffer[context.pos++] = (byte) ((context.lbitWorkArea >> 16) & MASK_8BITS);
                    buffer[context.pos++] = (byte) ((context.lbitWorkArea >> 8) & MASK_8BITS);
                    buffer[context.pos++] = (byte) ((context.lbitWorkArea) & MASK_8BITS);
                    break;
                case 6: // 30 bits = 3*8 + 6, or raise an exception
                    validateTrailingCharacters();
                    context.lbitWorkArea = context.lbitWorkArea >> 6;
                    buffer[context.pos++] = (byte) ((context.lbitWorkArea >> 16) & MASK_8BITS);
                    buffer[context.pos++] = (byte) ((context.lbitWorkArea >> 8) & MASK_8BITS);
                    buffer[context.pos++] = (byte) ((context.lbitWorkArea) & MASK_8BITS);
                    break;
                case 7: // 35 bits = 4*8 +3
                    validateCharacter(MASK_3BITS, context);
                    context.lbitWorkArea = context.lbitWorkArea >> 3;
                    buffer[context.pos++] = (byte) ((context.lbitWorkArea >> 24) & MASK_8BITS);
                    buffer[context.pos++] = (byte) ((context.lbitWorkArea >> 16) & MASK_8BITS);
                    buffer[context.pos++] = (byte) ((context.lbitWorkArea >> 8) & MASK_8BITS);
                    buffer[context.pos++] = (byte) ((context.lbitWorkArea) & MASK_8BITS);
                    break;
                default:
                    throw new IllegalStateException("Impossible modulus " + context.modulus);
            }
        }
    }

    /**
     * Encodes all of the provided data, starting at inPos, for inAvail bytes. Must be called at
     * least twice: once with the data to encode, and once with inAvail set to "-1" to alert encoder
     * that EOF has been reached, so flush last remaining bytes (if not multiple of 5).
     *
     * @param input byte[] array of binary data to Base32 encode.
     * @param inPos Position to start reading data from.
     * @param inAvail Amount of bytes available from input for encoding.
     * @param context the context to be used
     */
    @Override
    void encode2(final byte[] input, int inPos, final int inAvail, final Context context) {

        if (context.eof) {
            return;
        }
        if (inAvail < 0) {
            context.eof = true;
            if (0 == context.modulus && lineLength == 0) {
                return; // no leftovers to process and not using chunking
            }
            final byte[] buffer = ensureBufferSize(encodeSize, context);
            final int savedPos = context.pos;
            switch (context.modulus) { // % 5
                case 0:
                    break;
                case 1: // Only 1 octet; take top 5 bits then remainder
                    buffer[context.pos++] =
                            encodeTable[
                                    (int) (context.lbitWorkArea >> 3) & MASK_5BITS]; // 8-1*5 = 3
                    buffer[context.pos++] =
                            encodeTable[(int) (context.lbitWorkArea << 2) & MASK_5BITS]; // 5-3=2
                    buffer[context.pos++] = pad;
                    buffer[context.pos++] = pad;
                    buffer[context.pos++] = pad;
                    buffer[context.pos++] = pad;
                    buffer[context.pos++] = pad;
                    buffer[context.pos++] = pad;
                    break;
                case 2: // 2 octets = 16 bits to use
                    buffer[context.pos++] =
                            encodeTable[
                                    (int) (context.lbitWorkArea >> 11) & MASK_5BITS]; // 16-1*5 = 11
                    buffer[context.pos++] =
                            encodeTable[
                                    (int) (context.lbitWorkArea >> 6) & MASK_5BITS]; // 16-2*5 = 6
                    buffer[context.pos++] =
                            encodeTable[
                                    (int) (context.lbitWorkArea >> 1) & MASK_5BITS]; // 16-3*5 = 1
                    buffer[context.pos++] =
                            encodeTable[(int) (context.lbitWorkArea << 4) & MASK_5BITS]; // 5-1 = 4
                    buffer[context.pos++] = pad;
                    buffer[context.pos++] = pad;
                    buffer[context.pos++] = pad;
                    buffer[context.pos++] = pad;
                    break;
                case 3: // 3 octets = 24 bits to use
                    buffer[context.pos++] =
                            encodeTable[
                                    (int) (context.lbitWorkArea >> 19) & MASK_5BITS]; // 24-1*5 = 19
                    buffer[context.pos++] =
                            encodeTable[
                                    (int) (context.lbitWorkArea >> 14) & MASK_5BITS]; // 24-2*5 = 14
                    buffer[context.pos++] =
                            encodeTable[
                                    (int) (context.lbitWorkArea >> 9) & MASK_5BITS]; // 24-3*5 = 9
                    buffer[context.pos++] =
                            encodeTable[
                                    (int) (context.lbitWorkArea >> 4) & MASK_5BITS]; // 24-4*5 = 4
                    buffer[context.pos++] =
                            encodeTable[(int) (context.lbitWorkArea << 1) & MASK_5BITS]; // 5-4 = 1
                    buffer[context.pos++] = pad;
                    buffer[context.pos++] = pad;
                    buffer[context.pos++] = pad;
                    break;
                case 4: // 4 octets = 32 bits to use
                    buffer[context.pos++] =
                            encodeTable[
                                    (int) (context.lbitWorkArea >> 27) & MASK_5BITS]; // 32-1*5 = 27
                    buffer[context.pos++] =
                            encodeTable[
                                    (int) (context.lbitWorkArea >> 22) & MASK_5BITS]; // 32-2*5 = 22
                    buffer[context.pos++] =
                            encodeTable[
                                    (int) (context.lbitWorkArea >> 17) & MASK_5BITS]; // 32-3*5 = 17
                    buffer[context.pos++] =
                            encodeTable[
                                    (int) (context.lbitWorkArea >> 12) & MASK_5BITS]; // 32-4*5 = 12
                    buffer[context.pos++] =
                            encodeTable[
                                    (int) (context.lbitWorkArea >> 7) & MASK_5BITS]; // 32-5*5 =  7
                    buffer[context.pos++] =
                            encodeTable[
                                    (int) (context.lbitWorkArea >> 2) & MASK_5BITS]; // 32-6*5 =  2
                    buffer[context.pos++] =
                            encodeTable[(int) (context.lbitWorkArea << 3) & MASK_5BITS]; // 5-2 = 3
                    buffer[context.pos++] = pad;
                    break;
                default:
                    throw new IllegalStateException("Impossible modulus " + context.modulus);
            }
            context.currentLinePos += context.pos - savedPos; // keep track of current line position
            if (lineLength > 0 && context.currentLinePos > 0) { // add chunk separator if required
                System.arraycopy(lineSeparator, 0, buffer, context.pos, lineSeparator.length);
                context.pos += lineSeparator.length;
            }
        } else {
            for (int i = 0; i < inAvail; i++) {
                final byte[] buffer = ensureBufferSize(encodeSize, context);
                context.modulus = (context.modulus + 1) % BYTES_PER_UNENCODED_BLOCK;
                int b = input[inPos++];
                if (b < 0) {
                    b += 256;
                }
                context.lbitWorkArea = (context.lbitWorkArea << 8) + b; // BITS_PER_BYTE
                if (0 == context.modulus) { // we have enough bytes to create our output
                    buffer[context.pos++] =
                            encodeTable[(int) (context.lbitWorkArea >> 35) & MASK_5BITS];
                    buffer[context.pos++] =
                            encodeTable[(int) (context.lbitWorkArea >> 30) & MASK_5BITS];
                    buffer[context.pos++] =
                            encodeTable[(int) (context.lbitWorkArea >> 25) & MASK_5BITS];
                    buffer[context.pos++] =
                            encodeTable[(int) (context.lbitWorkArea >> 20) & MASK_5BITS];
                    buffer[context.pos++] =
                            encodeTable[(int) (context.lbitWorkArea >> 15) & MASK_5BITS];
                    buffer[context.pos++] =
                            encodeTable[(int) (context.lbitWorkArea >> 10) & MASK_5BITS];
                    buffer[context.pos++] =
                            encodeTable[(int) (context.lbitWorkArea >> 5) & MASK_5BITS];
                    buffer[context.pos++] = encodeTable[(int) context.lbitWorkArea & MASK_5BITS];
                    context.currentLinePos += BYTES_PER_ENCODED_BLOCK;
                    if (lineLength > 0 && lineLength <= context.currentLinePos) {
                        System.arraycopy(
                                lineSeparator, 0, buffer, context.pos, lineSeparator.length);
                        context.pos += lineSeparator.length;
                        context.currentLinePos = 0;
                    }
                }
            }
        }
    }

    /**
     * Returns whether or not the {@code octet} is in the Base32 alphabet.
     *
     * @param octet The value to test
     * @return {@code true} if the value is defined in the the Base32 alphabet {@code false}
     *     otherwise.
     */
    @Override
    public boolean isInAlphabet0(final byte octet) {
        return octet >= 0 && octet < decodeTable.length && decodeTable[octet] != -1;
    }

    /**
     * Validates whether decoding the final trailing character is possible in the context of the set
     * of possible base 32 values.
     *
     * <p>The character is valid if the lower bits within the provided mask are zero. This is used
     * to test the final trailing base-32 digit is zero in the bits that will be discarded.
     *
     * @param emptyBitsMask The mask of the lower bits that should be empty
     * @param context the context to be used
     * @throws IllegalArgumentException if the bits being checked contain any non-zero value
     */
    private void validateCharacter(final long emptyBitsMask, final Context context) {
        if (isStrictDecoding() && (context.lbitWorkArea & emptyBitsMask) != 0) {
            throw new IllegalArgumentException(
                    "Strict decoding: Last encoded character (before the paddings if any) is a"
                            + " valid base 32 alphabet but not a possible encoding. Expected the"
                            + " discarded bits from the character to be zero.");
        }
    }

    /**
     * Validates whether decoding allows final trailing characters that cannot be created during
     * encoding.
     *
     * @throws IllegalArgumentException if strict decoding is enabled
     */
    private void validateTrailingCharacters() {
        if (isStrictDecoding()) {
            throw new IllegalArgumentException(
                    "Strict decoding: Last encoded character(s) (before the paddings if any) are"
                        + " valid base 32 alphabet but not a possible encoding. Decoding requires"
                        + " either 2, 4, 5, or 7 trailing 5-bit characters to create bytes.");
        }
    }
}
