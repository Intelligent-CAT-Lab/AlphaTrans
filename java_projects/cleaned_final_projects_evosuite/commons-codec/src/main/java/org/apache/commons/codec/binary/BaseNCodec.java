
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

import org.apache.commons.codec.BinaryDecoder;
import org.apache.commons.codec.BinaryEncoder;
import org.apache.commons.codec.CodecPolicy;
import org.apache.commons.codec.DecoderException;
import org.apache.commons.codec.EncoderException;

import java.util.Arrays;
import java.util.Objects;

/**
 * Abstract superclass for Base-N encoders and decoders.
 *
 * <p>This class is thread-safe. You can set the decoding behavior when the input bytes contain
 * leftover trailing bits that cannot be created by a valid encoding. These can be bits that are
 * unused from the final character or entire characters. The default mode is lenient decoding.
 *
 * <ul>
 *   <li>Lenient: Any trailing bits are composed into 8-bit bytes where possible. The remainder are
 *       discarded.
 *   <li>Strict: The decoding will raise an {@link IllegalArgumentException} if trailing bits are
 *       not part of a valid encoding. Any unused bits from the final character must be zero.
 *       Impossible counts of entire final characters are not allowed.
 * </ul>
 *
 * <p>When strict decoding is enabled it is expected that the decoded bytes will be re-encoded to a
 * byte array that matches the original, i.e. no changes occur on the final character. This requires
 * that the input bytes use the same padding and alphabet as the encoder.
 */
public abstract class BaseNCodec implements BinaryEncoder, BinaryDecoder {

    /**
     * Holds thread context so classes can be thread-safe.
     *
     * <p>This class is not itself thread-safe; each thread must allocate its own copy.
     *
     * @since 1.7
     */
    static class Context {

        /**
         * Place holder for the bytes we're dealing with for our based logic. Bitwise operations
         * store and extract the encoding or decoding from this variable.
         */
        int ibitWorkArea;

        /**
         * Place holder for the bytes we're dealing with for our based logic. Bitwise operations
         * store and extract the encoding or decoding from this variable.
         */
        long lbitWorkArea;

        /** Buffer for streaming. */
        byte[] buffer;

        /** Position where next character should be written in the buffer. */
        int pos;

        /** Position where next character should be read from the buffer. */
        int readPos;

        /**
         * Boolean flag to indicate the EOF has been reached. Once EOF has been reached, this object
         * becomes useless, and must be thrown away.
         */
        boolean eof;

        /**
         * Variable tracks how many characters have been written to the current line. Only used when
         * encoding. We use it to make sure each encoded line never goes beyond lineLength (if
         * lineLength &gt; 0).
         */
        int currentLinePos;

        /**
         * Writes to the buffer only occur after every 3/5 reads when encoding, and every 4/8 reads
         * when decoding. This variable helps track that.
         */
        int modulus;

        Context() {}

        /**
         * Returns a String useful for debugging (especially within a debugger.)
         *
         * @return a String useful for debugging.
         */
        @SuppressWarnings("boxing") // OK to ignore boxing here
        @Override
        public String toString() {
            return String.format(
                    "%s[buffer=%s, currentLinePos=%s, eof=%s, ibitWorkArea=%s, lbitWorkArea=%s, "
                            + "modulus=%s, pos=%s, readPos=%s]",
                    this.getClass().getSimpleName(),
                    Arrays.toString(buffer),
                    currentLinePos,
                    eof,
                    ibitWorkArea,
                    lbitWorkArea,
                    modulus,
                    pos,
                    readPos);
        }
    }

    /**
     * EOF
     *
     * @since 1.7
     */
    static final int EOF = -1;

    /**
     * MIME chunk size per RFC 2045 section 6.8.
     *
     * <p>The {@value} character limit does not count the trailing CRLF, but counts all other
     * characters, including any equal signs.
     *
     * @see <a href="http://www.ietf.org/rfc/rfc2045.txt">RFC 2045 section 6.8</a>
     */
    public static final int MIME_CHUNK_SIZE = 76;

    /**
     * PEM chunk size per RFC 1421 section 4.3.2.4.
     *
     * <p>The {@value} character limit does not count the trailing CRLF, but counts all other
     * characters, including any equal signs.
     *
     * @see <a href="http://tools.ietf.org/html/rfc1421">RFC 1421 section 4.3.2.4</a>
     */
    public static final int PEM_CHUNK_SIZE = 64;

    private static final int DEFAULT_BUFFER_RESIZE_FACTOR = 2;

    /**
     * Defines the default buffer size - currently {@value} - must be large enough for at least one
     * encoded block+separator
     */
    private static final int DEFAULT_BUFFER_SIZE = 8192;

    /**
     * The maximum size buffer to allocate.
     *
     * <p>This is set to the same size used in the JDK {@code java.util.ArrayList}:
     *
     * <blockquote>
     *
     * Some VMs reserve some header words in an array. Attempts to allocate larger arrays may result
     * in OutOfMemoryError: Requested array size exceeds VM limit.
     *
     * </blockquote>
     */
    private static final int MAX_BUFFER_SIZE = Integer.MAX_VALUE - 8;

    /** Mask used to extract 8 bits, used in decoding bytes */
    protected static final int MASK_8BITS = 0xff;

    /** Byte used to pad output. */
    protected static final byte PAD_DEFAULT = '='; // Allow static access to default

    /**
     * The default decoding policy.
     *
     * @since 1.15
     */
    protected static final CodecPolicy DECODING_POLICY_DEFAULT = CodecPolicy.LENIENT;

    /**
     * Chunk separator per RFC 2045 section 2.1.
     *
     * @see <a href="http://www.ietf.org/rfc/rfc2045.txt">RFC 2045 section 2.1</a>
     */
    static final byte[] CHUNK_SEPARATOR = {'\r', '\n'};

    /**
     * Compares two {@code int} values numerically treating the values as unsigned. Taken from JDK
     * 1.8.
     *
     * <p>TODO: Replace with JDK 1.8 Integer::compareUnsigned(int, int).
     *
     * @param x the first {@code int} to compare
     * @param y the second {@code int} to compare
     * @return the value {@code 0} if {@code x == y}; a value less than {@code 0} if {@code x < y}
     *     as unsigned values; and a value greater than {@code 0} if {@code x > y} as unsigned
     *     values
     */
    private static int compareUnsigned(final int x, final int y) {
        return Integer.compare(x + Integer.MIN_VALUE, y + Integer.MIN_VALUE);
    }

    /**
     * Create a positive capacity at least as large the minimum required capacity. If the minimum
     * capacity is negative then this throws an OutOfMemoryError as no array can be allocated.
     *
     * @param minCapacity the minimum capacity
     * @return the capacity
     * @throws OutOfMemoryError if the {@code minCapacity} is negative
     */
    private static int createPositiveCapacity(final int minCapacity) {
        if (minCapacity < 0) {
            throw new OutOfMemoryError(
                    "Unable to allocate array size: " + (minCapacity & 0xffffffffL));
        }
        return (minCapacity > MAX_BUFFER_SIZE) ? minCapacity : MAX_BUFFER_SIZE;
    }

    /**
     * Gets a copy of the chunk separator per RFC 2045 section 2.1.
     *
     * @return the chunk separator
     * @see <a href="http://www.ietf.org/rfc/rfc2045.txt">RFC 2045 section 2.1</a>
     * @since 1.15
     */
    public static byte[] getChunkSeparator() {
        return CHUNK_SEPARATOR.clone();
    }

    /**
     * Checks if a byte value is whitespace or not. Whitespace is taken to mean: space, tab, CR, LF
     *
     * @param byteToCheck the byte to check
     * @return true if byte is whitespace, false otherwise
     */
    protected static boolean isWhiteSpace(final byte byteToCheck) {
        switch (byteToCheck) {
            case ' ':
            case '\n':
            case '\r':
            case '\t':
                return true;
            default:
                return false;
        }
    }

    /**
     * Increases our buffer by the {@link #DEFAULT_BUFFER_RESIZE_FACTOR}.
     *
     * @param context the context to be used
     * @param minCapacity the minimum required capacity
     * @return the resized byte[] buffer
     * @throws OutOfMemoryError if the {@code minCapacity} is negative
     */
    private static byte[] resizeBuffer(final Context context, final int minCapacity) {
        final int oldCapacity = context.buffer.length;
        int newCapacity = oldCapacity * DEFAULT_BUFFER_RESIZE_FACTOR;
        if (compareUnsigned(newCapacity, minCapacity) < 0) {
            newCapacity = minCapacity;
        }
        if (compareUnsigned(newCapacity, MAX_BUFFER_SIZE) > 0) {
            newCapacity = createPositiveCapacity(minCapacity);
        }

        final byte[] b = new byte[newCapacity];
        System.arraycopy(context.buffer, 0, b, 0, context.buffer.length);
        context.buffer = b;
        return b;
    }

    /**
     * @deprecated Use {@link #pad}. Will be removed in 2.0.
     */
    @Deprecated
    protected final byte PAD = PAD_DEFAULT; // instance variable just in case it needs to vary later

    protected final byte pad; // instance variable just in case it needs to vary later

    /** Number of bytes in each full block of unencoded data, e.g. 4 for Base64 and 5 for Base32 */
    private final int unencodedBlockSize;

    /** Number of bytes in each full block of encoded data, e.g. 3 for Base64 and 8 for Base32 */
    private final int encodedBlockSize;

    /**
     * Chunksize for encoding. Not used when decoding. A value of zero or less implies no chunking
     * of the encoded data. Rounded down to nearest multiple of encodedBlockSize.
     */
    protected final int lineLength;

    /** Size of chunk separator. Not used unless {@link #lineLength} &gt; 0. */
    private final int chunkSeparatorLength;

    /**
     * Defines the decoding behavior when the input bytes contain leftover trailing bits that cannot
     * be created by a valid encoding. These can be bits that are unused from the final character or
     * entire characters. The default mode is lenient decoding. Set this to {@code true} to enable
     * strict decoding.
     *
     * <ul>
     *   <li>Lenient: Any trailing bits are composed into 8-bit bytes where possible. The remainder
     *       are discarded.
     *   <li>Strict: The decoding will raise an {@link IllegalArgumentException} if trailing bits
     *       are not part of a valid encoding. Any unused bits from the final character must be
     *       zero. Impossible counts of entire final characters are not allowed.
     * </ul>
     *
     * <p>When strict decoding is enabled it is expected that the decoded bytes will be re-encoded
     * to a byte array that matches the original, i.e. no changes occur on the final character. This
     * requires that the input bytes use the same padding and alphabet as the encoder.
     */
    private final CodecPolicy decodingPolicy;

    /**
     * Note {@code lineLength} is rounded down to the nearest multiple of the encoded block size. If
     * {@code chunkSeparatorLength} is zero, then chunking is disabled.
     *
     * @param unencodedBlockSize the size of an unencoded block (e.g. Base64 = 3)
     * @param encodedBlockSize the size of an encoded block (e.g. Base64 = 4)
     * @param lineLength if &gt; 0, use chunking with a length {@code lineLength}
     * @param chunkSeparatorLength the chunk separator length, if relevant
     * @param pad byte used as padding byte.
     * @param decodingPolicy Decoding policy.
     * @since 1.15
     */
    protected BaseNCodec(
            int constructorId,
            final int unencodedBlockSize,
            final int encodedBlockSize,
            final int lineLength,
            final int chunkSeparatorLength,
            final byte pad,
            final CodecPolicy decodingPolicy) {
        this.unencodedBlockSize = unencodedBlockSize;
        this.encodedBlockSize = encodedBlockSize;
        final boolean useChunking = lineLength > 0 && chunkSeparatorLength > 0;
        this.lineLength = useChunking ? (lineLength / encodedBlockSize) * encodedBlockSize : 0;
        this.chunkSeparatorLength = chunkSeparatorLength;
        if (constructorId == 0) {
            this.pad = PAD_DEFAULT;
        } else {
            this.pad = pad;
        }

        if (constructorId == 2) {
            this.decodingPolicy = Objects.requireNonNull(decodingPolicy, "codecPolicy");
        } else {
            this.decodingPolicy = DECODING_POLICY_DEFAULT;
        }
    }

    /**
     * Returns the amount of buffered data available for reading.
     *
     * @param context the context to be used
     * @return The amount of buffered data available for reading.
     */
    int available(final Context context) { // package protected for access from I/O streams
        return hasData(context) ? context.pos - context.readPos : 0;
    }

    /**
     * Tests a given byte array to see if it contains any characters within the alphabet or PAD.
     *
     * <p>Intended for use in checking line-ending arrays
     *
     * @param arrayOctet byte array to test
     * @return {@code true} if any byte is a valid character in the alphabet or PAD; {@code false}
     *     otherwise
     */
    protected boolean containsAlphabetOrPad(final byte[] arrayOctet) {
        if (arrayOctet == null) {
            return false;
        }
        for (final byte element : arrayOctet) {
            if (pad == element || isInAlphabet0(element)) {
                return true;
            }
        }
        return false;
    }

    /**
     * Decodes a byte[] containing characters in the Base-N alphabet.
     *
     * @param pArray A byte array containing Base-N character data
     * @return a byte array containing binary data
     */
    @Override
    public byte[] decode(final byte[] pArray) {
        return decode0(pArray);
    }

    public byte[] decode0(final byte[] pArray) {
        if (pArray == null || pArray.length == 0) {
            return pArray;
        }
        final Context context = new Context();
        decode1(pArray, 0, pArray.length, context);
        decode1(pArray, 0, EOF, context); // Notify decoder of EOF.
        final byte[] result = new byte[context.pos];
        readResults(result, 0, result.length, context);
        return result;
    }

    abstract void decode1(byte[] pArray, int i, int length, Context context);

    /**
     * Decodes an Object using the Base-N algorithm. This method is provided in order to satisfy the
     * requirements of the Decoder interface, and will throw a DecoderException if the supplied
     * object is not of type byte[] or String.
     *
     * @param obj Object to decode
     * @return An object (of type byte[]) containing the binary data which corresponds to the byte[]
     *     or String supplied.
     * @throws DecoderException if the parameter supplied is not of type byte[]
     */
    @Override
    public Object decode(final Object obj) throws DecoderException {
        return decode2(obj);
    }

    public Object decode2(final Object obj) throws DecoderException {
        if (obj instanceof byte[]) {
            return decode0((byte[]) obj);
        }
        if (obj instanceof String) {
            return decode3((String) obj);
        }
        throw new DecoderException(
                "Parameter supplied to Base-N decode is not a byte[] or a String", null);
    }

    /**
     * Decodes a String containing characters in the Base-N alphabet.
     *
     * @param pArray A String containing Base-N character data
     * @return a byte array containing binary data
     */
    public byte[] decode3(final String pArray) {
        return decode0(StringUtils.getBytesUtf8(pArray));
    }

    /**
     * Encodes a byte[] containing binary data, into a byte[] containing characters in the alphabet.
     *
     * @param pArray a byte array containing binary data
     * @return A byte array containing only the base N alphabetic character data
     */
    @Override
    public byte[] encode(final byte[] pArray) {
        return encode0(pArray);
    }

    public byte[] encode0(final byte[] pArray) {
        if (pArray == null || pArray.length == 0) {
            return pArray;
        }
        return encode1(pArray, 0, pArray.length);
    }

    /**
     * Encodes a byte[] containing binary data, into a byte[] containing characters in the alphabet.
     *
     * @param pArray a byte array containing binary data
     * @param offset initial offset of the subarray.
     * @param length length of the subarray.
     * @return A byte array containing only the base N alphabetic character data
     * @since 1.11
     */
    public byte[] encode1(final byte[] pArray, final int offset, final int length) {
        if (pArray == null || pArray.length == 0) {
            return pArray;
        }
        final Context context = new Context();
        encode2(pArray, offset, length, context);
        encode2(pArray, offset, EOF, context); // Notify encoder of EOF.
        final byte[] buf = new byte[context.pos - context.readPos];
        readResults(buf, 0, buf.length, context);
        return buf;
    }

    abstract void encode2(byte[] pArray, int i, int length, Context context);

    /**
     * Encodes an Object using the Base-N algorithm. This method is provided in order to satisfy the
     * requirements of the Encoder interface, and will throw an EncoderException if the supplied
     * object is not of type byte[].
     *
     * @param obj Object to encode
     * @return An object (of type byte[]) containing the Base-N encoded data which corresponds to
     *     the byte[] supplied.
     * @throws EncoderException if the parameter supplied is not of type byte[]
     */
    @Override
    public Object encode(final Object obj) throws EncoderException {
        return encode3(obj);
    }

    public Object encode3(final Object obj) throws EncoderException {
        if (!(obj instanceof byte[])) {
            throw new EncoderException("Parameter supplied to Base-N encode is not a byte[]", null);
        }
        return encode0((byte[]) obj);
    }

    /**
     * Encodes a byte[] containing binary data, into a String containing characters in the
     * appropriate alphabet. Uses UTF8 encoding.
     *
     * @param pArray a byte array containing binary data
     * @return String containing only character data in the appropriate alphabet.
     * @since 1.5 This is a duplicate of {@link #encodeToString(byte[])}; it was merged during
     *     refactoring.
     */
    public String encodeAsString(final byte[] pArray) {
        return StringUtils.newStringUtf8(encode0(pArray));
    }

    /**
     * Encodes a byte[] containing binary data, into a String containing characters in the Base-N
     * alphabet. Uses UTF8 encoding.
     *
     * @param pArray a byte array containing binary data
     * @return A String containing only Base-N character data
     */
    public String encodeToString(final byte[] pArray) {
        return StringUtils.newStringUtf8(encode0(pArray));
    }

    /**
     * Ensure that the buffer has room for {@code size} bytes
     *
     * @param size minimum spare space required
     * @param context the context to be used
     * @return the buffer
     */
    protected byte[] ensureBufferSize(final int size, final Context context) {
        if (context.buffer == null) {
            context.buffer = new byte[Math.max(size, getDefaultBufferSize())];
            context.pos = 0;
            context.readPos = 0;

        } else if (context.pos + size - context.buffer.length > 0) {
            return resizeBuffer(context, context.pos + size);
        }
        return context.buffer;
    }

    /**
     * Returns the decoding behavior policy.
     *
     * <p>The default is lenient. If the decoding policy is strict, then decoding will raise an
     * {@link IllegalArgumentException} if trailing bits are not part of a valid encoding. Decoding
     * will compose trailing bits into 8-bit bytes and discard the remainder.
     *
     * @return true if using strict decoding
     * @since 1.15
     */
    public CodecPolicy getCodecPolicy() {
        return decodingPolicy;
    }

    /**
     * Get the default buffer size. Can be overridden.
     *
     * @return the default buffer size.
     */
    protected int getDefaultBufferSize() {
        return DEFAULT_BUFFER_SIZE;
    }

    /**
     * Calculates the amount of space needed to encode the supplied array.
     *
     * @param pArray byte[] array which will later be encoded
     * @return amount of space needed to encoded the supplied array. Returns a long since a max-len
     *     array will require &gt; Integer.MAX_VALUE
     */
    public long getEncodedLength(final byte[] pArray) {
        long len =
                ((pArray.length + unencodedBlockSize - 1) / unencodedBlockSize)
                        * (long) encodedBlockSize;
        if (lineLength > 0) { // We're using chunking
            len += ((len + lineLength - 1) / lineLength) * chunkSeparatorLength;
        }
        return len;
    }

    /**
     * Returns true if this object has buffered data for reading.
     *
     * @param context the context to be used
     * @return true if there is data still available for reading.
     */
    boolean hasData(final Context context) { // package protected for access from I/O streams
        return context.pos > context.readPos;
    }

    /**
     * Returns whether or not the {@code octet} is in the current alphabet. Does not allow
     * whitespace or pad.
     *
     * @param value The value to test
     * @return {@code true} if the value is defined in the current alphabet, {@code false}
     *     otherwise.
     */
    protected abstract boolean isInAlphabet0(byte value);

    /**
     * Tests a given byte array to see if it contains only valid characters within the alphabet. The
     * method optionally treats whitespace and pad as valid.
     *
     * @param arrayOctet byte array to test
     * @param allowWSPad if {@code true}, then whitespace and PAD are also allowed
     * @return {@code true} if all bytes are valid characters in the alphabet or if the byte array
     *     is empty; {@code false}, otherwise
     */
    public boolean isInAlphabet1(final byte[] arrayOctet, final boolean allowWSPad) {
        for (final byte octet : arrayOctet) {
            if (!isInAlphabet0(octet) && (!allowWSPad || (octet != pad) && !isWhiteSpace(octet))) {
                return false;
            }
        }
        return true;
    }

    /**
     * Tests a given String to see if it contains only valid characters within the alphabet. The
     * method treats whitespace and PAD as valid.
     *
     * @param basen String to test
     * @return {@code true} if all characters in the String are valid characters in the alphabet or
     *     if the String is empty; {@code false}, otherwise
     * @see #isInAlphabet(byte[], boolean)
     */
    public boolean isInAlphabet2(final String basen) {
        return isInAlphabet1(StringUtils.getBytesUtf8(basen), true);
    }

    /**
     * Returns true if decoding behavior is strict. Decoding will raise an {@link
     * IllegalArgumentException} if trailing bits are not part of a valid encoding.
     *
     * <p>The default is false for lenient decoding. Decoding will compose trailing bits into 8-bit
     * bytes and discard the remainder.
     *
     * @return true if using strict decoding
     * @since 1.15
     */
    public boolean isStrictDecoding() {
        return decodingPolicy == CodecPolicy.STRICT;
    }

    /**
     * Extracts buffered data into the provided byte[] array, starting at position bPos, up to a
     * maximum of bAvail bytes. Returns how many bytes were actually extracted.
     *
     * <p>Package protected for access from I/O streams.
     *
     * @param b byte[] array to extract the buffered data into.
     * @param bPos position in byte[] array to start extraction at.
     * @param bAvail amount of bytes we're allowed to extract. We may extract fewer (if fewer are
     *     available).
     * @param context the context to be used
     * @return The number of bytes successfully extracted into the provided byte[] array.
     */
    int readResults(final byte[] b, final int bPos, final int bAvail, final Context context) {
        if (hasData(context)) {
            final int len = Math.min(available(context), bAvail);
            System.arraycopy(context.buffer, context.readPos, b, bPos, len);
            context.readPos += len;
            if (!hasData(context)) {
                context.pos = context.readPos = 0;
            }
            return len;
        }
        return context.eof ? EOF : 0;
    }
}
