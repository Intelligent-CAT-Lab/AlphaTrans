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

import static org.junit.Assert.assertArrayEquals;
import static org.junit.Assert.assertEquals;
import static org.junit.Assert.assertNotEquals;
import static org.junit.Assert.assertTrue;
import static org.junit.Assert.fail;

import org.apache.commons.codec.DecoderException;
import org.apache.commons.codec.EncoderException;
import org.junit.Assert;
import org.junit.Test;

import java.io.UnsupportedEncodingException;
import java.nio.ByteBuffer;
import java.nio.charset.Charset;
import java.nio.charset.StandardCharsets;
import java.nio.charset.UnsupportedCharsetException;
import java.util.Arrays;
import java.util.concurrent.ThreadLocalRandom;

/** Tests {@link org.apache.commons.codec.binary.Hex}. */
public class HexTest {

    private static final String BAD_ENCODING_NAME = "UNKNOWN";

    private static final boolean LOG = false;

    /**
     * Allocate a ByteBuffer.
     *
     * <p>The default implementation uses {@link ByteBuffer#allocate(int)}. The method is overridden
     * in AllocateDirectHexTest to use {@link ByteBuffer#allocateDirect(int)}
     *
     * @param capacity the capacity
     * @return the byte buffer
     */
    protected ByteBuffer allocate(final int capacity) {
        return ByteBuffer.allocate(capacity);
    }

    /**
     * Encodes the given string into a byte buffer using the UTF-8 charset.
     *
     * <p>The buffer is allocated using {@link #allocate(int)}.
     *
     * @param string the String to encode
     * @return the byte buffer
     */
    private ByteBuffer getByteBufferUtf8(final String string) {
        final byte[] bytes = string.getBytes(StandardCharsets.UTF_8);
        final ByteBuffer bb = allocate(bytes.length);
        bb.put(bytes);
        bb.flip();
        return bb;
    }

    private boolean charsetSanityCheck(final String name) {
        final String source = "the quick brown dog jumped over the lazy fox";
        try {
            final byte[] bytes = source.getBytes(name);
            final String str = new String(bytes, name);
            final boolean equals = source.equals(str);
            if (!equals) {
                log0(
                        "FAILED charsetSanityCheck=Interesting Java charset oddity: Roundtrip"
                                + " failed for "
                                + name);
            }
            return equals;
        } catch (final UnsupportedEncodingException | UnsupportedOperationException e) {
            if (LOG) {
                log0("FAILED charsetSanityCheck=" + name + ", e=" + e);
                log1(e);
            }
            return false;
        }
    }

    private void checkDecodeHexCharArrayOddCharacters0(final char[] data) {
        try {
            Hex.decodeHex0(data);
            fail("An exception wasn't thrown when trying to decode an odd number of characters");
        } catch (final DecoderException e) {
        }
    }

    private void checkDecodeHexByteBufferOddCharacters(final ByteBuffer data) {
        try {
            new Hex(2, null, null).decode1(data);
            fail("An exception wasn't thrown when trying to decode an odd number of characters");
        } catch (final DecoderException e) {
        }
    }

    private void checkDecodeHexCharArrayOddCharacters1(final String data) {
        try {
            Hex.decodeHex2(data);
            fail("An exception wasn't thrown when trying to decode an odd number of characters");
        } catch (final DecoderException e) {
        }
    }

    private void log0(final String s) {
        if (LOG) {
            System.out.println(s);
            System.out.flush();
        }
    }

    private void log1(final Throwable t) {
        if (LOG) {
            t.printStackTrace(System.out);
            System.out.flush();
        }
    }

    

    /**
     * @param name
     * @param parent
     * @throws UnsupportedEncodingException
     * @throws DecoderException
     */
    private void testCustomCharset1(final String name, final String parent)
            throws UnsupportedEncodingException, DecoderException {
        if (!charsetSanityCheck(name)) {
            return;
        }
        log0(parent + "=" + name);
        final Hex customCodec = Hex.Hex0(name);
        final String sourceString = "Hello World";
        final byte[] sourceBytes = sourceString.getBytes(name);
        final byte[] actualEncodedBytes = customCodec.encode0(sourceBytes);
        String expectedHexString = Hex.encodeHexString0(sourceBytes);
        final byte[] expectedHexStringBytes = expectedHexString.getBytes(name);
        assertArrayEquals(expectedHexStringBytes, actualEncodedBytes);
        String actualStringFromBytes = new String(actualEncodedBytes, name);
        assertEquals(
                name
                        + ", expectedHexString="
                        + expectedHexString
                        + ", actualStringFromBytes="
                        + actualStringFromBytes,
                expectedHexString,
                actualStringFromBytes);
        final Hex utf8Codec = new Hex(2, null, null);
        expectedHexString = "48656c6c6f20576f726c64";
        final byte[] decodedUtf8Bytes = (byte[]) utf8Codec.decode2(expectedHexString);
        actualStringFromBytes = new String(decodedUtf8Bytes, utf8Codec.getCharset());
        assertEquals(name, sourceString, actualStringFromBytes);
        final byte[] decodedCustomBytes = customCodec.decode0(actualEncodedBytes);
        actualStringFromBytes = new String(decodedCustomBytes, name);
        assertEquals(name, sourceString, actualStringFromBytes);
    }

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    /** Test encoding of a read only byte buffer. See CODEC-261. */

    @Test
    public void testCustomCharset0_test0_decomposed() throws UnsupportedEncodingException , DecoderException {
        for (final String name : Charset.availableCharsets().keySet()) {
            testCustomCharset1(name, "testCustomCharset");
        }
    }

    @Test(expected = UnsupportedCharsetException.class)
    public void testCustomCharsetBadName_test0_decomposed()  {
        Hex.Hex0(BAD_ENCODING_NAME);
    }

    @Test
    public void testCustomCharsetToString_test0_decomposed()  {
        assertTrue(new Hex(2, null, null).toString().indexOf(Hex.DEFAULT_CHARSET_NAME) >= 0);
    }

    @Test
    public void testDecodeBadCharacterPos0_test0_decomposed()  {
        try {
            new Hex(2, null, null).decode2("q0");
            fail("An exception wasn't thrown when trying to decode an illegal character");
        } catch (final DecoderException e) {
        }
    }

    @Test
    public void testDecodeBadCharacterPos1_test0_decomposed()  {
        try {
            new Hex(2, null, null).decode2("0q");
            fail("An exception wasn't thrown when trying to decode an illegal character");
        } catch (final DecoderException e) {
        }
    }

    @Test
    public void testDecodeByteArrayEmpty_test0_decomposed() throws DecoderException {
        assertArrayEquals(new byte[0], new Hex(2, null, null).decode0(new byte[0]));
    }

    @Test
    public void testDecodeByteArrayObjectEmpty_test0_decomposed() throws DecoderException {
        assertArrayEquals(
                new byte[0], (byte[]) new Hex(2, null, null).decode2((Object) new byte[0]));
    }

    @Test
    public void testDecodeByteArrayOddCharacters_test0_decomposed()  {
        try {
            new Hex(2, null, null).decode0(new byte[] {65});
            fail("An exception wasn't thrown when trying to decode an odd number of characters");
        } catch (final DecoderException e) {
        }
    }

    @Test
    public void testDecodeByteBufferEmpty_test0_decomposed() throws DecoderException {
        allocate(0);
    }

    @Test
    public void testDecodeByteBufferEmpty_test1_decomposed() throws DecoderException {
        allocate(0);
        assertArrayEquals(new byte[0], new Hex(2, null, null).decode1(allocate(0)));
    }

    @Test
    public void testDecodeByteBufferAllocatedButEmpty_test0_decomposed() throws DecoderException {
        final ByteBuffer bb = allocate(10);
    }

    @Test
    public void testDecodeByteBufferAllocatedButEmpty_test1_decomposed() throws DecoderException {
        final ByteBuffer bb = allocate(10);
        bb.flip();
        assertArrayEquals(new byte[0], new Hex(2, null, null).decode1(bb));
    }

    @Test
    public void testDecodeByteBufferAllocatedButEmpty_test2_decomposed() throws DecoderException {
        final ByteBuffer bb = allocate(10);
        bb.flip();
        assertArrayEquals(new byte[0], new Hex(2, null, null).decode1(bb));
        assertEquals(0, bb.remaining());
    }

    @Test
    public void testDecodeByteBufferObjectEmpty_test0_decomposed() throws DecoderException {
        allocate(0);
    }

    @Test
    public void testDecodeByteBufferObjectEmpty_test1_decomposed() throws DecoderException {
        allocate(0);
        assertArrayEquals(
                new byte[0], (byte[]) new Hex(2, null, null).decode2((Object) allocate(0)));
    }

    @Test
    public void testDecodeByteBufferOddCharacters_test0_decomposed()  {
        final ByteBuffer bb = allocate(1);
    }

    @Test
    public void testDecodeByteBufferOddCharacters_test1_decomposed()  {
        final ByteBuffer bb = allocate(1);
        bb.put((byte) 65);
    }

    @Test
    public void testDecodeByteBufferOddCharacters_test2_decomposed()  {
        final ByteBuffer bb = allocate(1);
        bb.put((byte) 65);
        bb.flip();
        checkDecodeHexByteBufferOddCharacters(bb);
    }

    @Test
    public void testDecodeByteBufferWithLimitOddCharacters_test0_decomposed()  {
        final ByteBuffer bb = allocate(10);
    }

    @Test
    public void testDecodeByteBufferWithLimitOddCharacters_test1_decomposed()  {
        final ByteBuffer bb = allocate(10);
        bb.put(1, (byte) 65);
    }

    @Test
    public void testDecodeByteBufferWithLimitOddCharacters_test2_decomposed()  {
        final ByteBuffer bb = allocate(10);
        bb.put(1, (byte) 65);
        bb.position(1);
        bb.limit(2);
        checkDecodeHexByteBufferOddCharacters(bb);
    }

    @Test
    public void testDecodeHexCharArrayEmpty_test0_decomposed() throws DecoderException {
        assertArrayEquals(new byte[0], Hex.decodeHex0(new char[0]));
    }

    @Test
    public void testDecodeHexStringEmpty_test0_decomposed() throws DecoderException {
        assertArrayEquals(new byte[0], Hex.decodeHex2(""));
    }

    @Test
    public void testDecodeClassCastException_test0_decomposed()  {
        try {
            new Hex(2, null, null).decode2(new int[] {65});
            fail("An exception wasn't thrown when trying to decode.");
        } catch (final DecoderException e) {
        }
    }

    @Test
    public void testDecodeHexCharArrayOddCharacters1_test0_decomposed()  {
        checkDecodeHexCharArrayOddCharacters0(new char[] {'A'});
    }

    @Test
    public void testDecodeHexStringOddCharacters1_test0_decomposed()  {
        checkDecodeHexCharArrayOddCharacters1("A");
    }

    @Test
    public void testDecodeHexCharArrayOddCharacters3_test0_decomposed()  {
        checkDecodeHexCharArrayOddCharacters0(new char[] {'A', 'B', 'C'});
    }

    @Test
    public void testDecodeHexCharArrayOddCharacters5_test0_decomposed()  {
        checkDecodeHexCharArrayOddCharacters0(new char[] {'A', 'B', 'C', 'D', 'E'});
    }

    @Test(expected = DecoderException.class)
    public void testDecodeHexCharArrayOutBufferUnderSized_test0_decomposed() throws DecoderException {
        final byte[] out = new byte[4];
        Hex.decodeHex1("aabbccddeeff".toCharArray(), out, 0);
    }

    @Test(expected = DecoderException.class)
    public void testDecodeHexCharArrayOutBufferUnderSizedByOffset_test0_decomposed() throws DecoderException {
        final byte[] out = new byte[6];
        Hex.decodeHex1("aabbccddeeff".toCharArray(), out, 1);
    }

    @Test
    public void testDecodeHexStringOddCharacters_test0_decomposed()  {
        try {
            new Hex(2, null, null).decode2("6");
            fail("An exception wasn't thrown when trying to decode an odd number of characters");
        } catch (final DecoderException e) {
        }
    }

    @Test
    public void testDecodeStringEmpty_test0_decomposed() throws DecoderException {
        assertArrayEquals(new byte[0], (byte[]) new Hex(2, null, null).decode2(""));
    }

    @Test
    public void testDecodeByteBufferWithLimit_test0_decomposed() throws DecoderException {
        final ByteBuffer bb = getByteBufferUtf8("000102030405060708090a0b0c0d0e0f");
    }

    @Test
    public void testDecodeByteBufferWithLimit_test1_decomposed() throws DecoderException {
        final ByteBuffer bb = getByteBufferUtf8("000102030405060708090a0b0c0d0e0f");
        final byte[] expected = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15};
        for (int i = 0; i < 15; i++) {
            bb.position(i * 2);
            bb.limit(i * 2 + 4);
            assertEquals(
                    new String(Arrays.copyOfRange(expected, i, i + 2)),
                    new String(new Hex(2, null, null).decode1(bb)));
            assertEquals(0, bb.remaining());
        }
    }

    @Test
    public void testEncodeByteArrayEmpty_test0_decomposed()  {
        assertArrayEquals(new byte[0], new Hex(2, null, null).encode0(new byte[0]));
    }

    @Test
    public void testEncodeByteArrayObjectEmpty_test0_decomposed() throws EncoderException {
        assertArrayEquals(
                new char[0], (char[]) new Hex(2, null, null).encode2((Object) new byte[0]));
    }

    @Test
    public void testEncodeByteBufferEmpty_test0_decomposed()  {
        allocate(0);
    }

    @Test
    public void testEncodeByteBufferEmpty_test1_decomposed()  {
        allocate(0);
        assertArrayEquals(new byte[0], new Hex(2, null, null).encode1(allocate(0)));
    }

    @Test
    public void testEncodeByteBufferAllocatedButEmpty_test0_decomposed()  {
        final ByteBuffer bb = allocate(10);
    }

    @Test
    public void testEncodeByteBufferAllocatedButEmpty_test1_decomposed()  {
        final ByteBuffer bb = allocate(10);
        bb.flip();
        assertArrayEquals(new byte[0], new Hex(2, null, null).encode1(bb));
    }

    @Test
    public void testEncodeByteBufferAllocatedButEmpty_test2_decomposed()  {
        final ByteBuffer bb = allocate(10);
        bb.flip();
        assertArrayEquals(new byte[0], new Hex(2, null, null).encode1(bb));
        assertEquals(0, bb.remaining());
    }

    @Test
    public void testEncodeByteBufferObjectEmpty_test0_decomposed() throws EncoderException {
        allocate(0);
    }

    @Test
    public void testEncodeByteBufferObjectEmpty_test1_decomposed() throws EncoderException {
        allocate(0);
        assertArrayEquals(
                new char[0], (char[]) new Hex(2, null, null).encode2((Object) allocate(0)));
    }

    @Test
    public void testEncodeClassCastException_test0_decomposed()  {
        try {
            new Hex(2, null, null).encode2(new int[] {65});
            fail("An exception wasn't thrown when trying to encode.");
        } catch (final EncoderException e) {
        }
    }

    @Test
    public void testEncodeDecodeHexCharArrayRandom_test0_decomposed() throws DecoderException , EncoderException {
        final Hex hex = new Hex(2, null, null);
    }

    @Test
    public void testEncodeDecodeHexCharArrayRandom_test1_decomposed() throws DecoderException , EncoderException {
        final Hex hex = new Hex(2, null, null);
        for (int i = 5; i > 0; i--) {
            final byte[] data = new byte[ThreadLocalRandom.current().nextInt(10000) + 1];
            ThreadLocalRandom.current().nextBytes(data);

            final char[] encodedChars = Hex.encodeHex0(data);
            byte[] decodedBytes = Hex.decodeHex0(encodedChars);
            assertArrayEquals(data, decodedBytes);

            final byte[] encodedStringBytes = hex.encode0(data);
            decodedBytes = hex.decode0(encodedStringBytes);
            assertArrayEquals(data, decodedBytes);

            String dataString = new String(encodedChars);
            char[] encodedStringChars = (char[]) hex.encode2(dataString);
            decodedBytes = (byte[]) hex.decode2(encodedStringChars);
            assertArrayEquals(StringUtils.getBytesUtf8(dataString), decodedBytes);

            dataString = new String(encodedChars);
            encodedStringChars = (char[]) hex.encode2(dataString);
            decodedBytes = (byte[]) hex.decode2(new String(encodedStringChars));
            assertArrayEquals(StringUtils.getBytesUtf8(dataString), decodedBytes);
        }
    }

    @Test
    public void testEncodeDecodeHexCharArrayRandomToOutput_test0_decomposed() throws DecoderException , EncoderException {
        for (int i = 5; i > 0; i--) {
            final byte[] data = new byte[ThreadLocalRandom.current().nextInt(10000) + 1];
            ThreadLocalRandom.current().nextBytes(data);

            final char[] lowerEncodedChars = new char[data.length * 2];
            Hex.encodeHex4(data, 0, data.length, true, lowerEncodedChars, 0);
            final byte[] decodedLowerCaseBytes = Hex.decodeHex0(lowerEncodedChars);
            assertArrayEquals(data, decodedLowerCaseBytes);

            final char[] upperEncodedChars = new char[data.length * 2];
            Hex.encodeHex4(data, 0, data.length, false, upperEncodedChars, 0);
            final byte[] decodedUpperCaseBytes = Hex.decodeHex0(upperEncodedChars);
            assertArrayEquals(data, decodedUpperCaseBytes);
        }
    }

    @Test
    public void testEncodeHexByteArrayEmpty_test0_decomposed()  {
        assertArrayEquals(new char[0], Hex.encodeHex0(new byte[0]));
    }

    @Test
    public void testEncodeHexByteArrayEmpty_test1_decomposed()  {
        assertArrayEquals(new char[0], Hex.encodeHex0(new byte[0]));
        assertArrayEquals(new byte[0], new Hex(2, null, null).encode0(new byte[0]));
    }

    @Test
    public void testEncodeHexByteArrayHelloWorldLowerCaseHex_test0_decomposed()  {
        final byte[] b = StringUtils.getBytesUtf8("Hello World");
    }

    @Test
    public void testEncodeHexByteArrayHelloWorldLowerCaseHex_test1_decomposed()  {
        final byte[] b = StringUtils.getBytesUtf8("Hello World");
        final String expected = "48656c6c6f20576f726c64";
        char[] actual;
        actual = Hex.encodeHex0(b);
    }

    @Test
    public void testEncodeHexByteArrayHelloWorldLowerCaseHex_test2_decomposed()  {
        final byte[] b = StringUtils.getBytesUtf8("Hello World");
        final String expected = "48656c6c6f20576f726c64";
        char[] actual;
        actual = Hex.encodeHex0(b);
        assertEquals(expected, new String(actual));
        actual = Hex.encodeHex1(b, true);
    }

    @Test
    public void testEncodeHexByteArrayHelloWorldLowerCaseHex_test3_decomposed()  {
        final byte[] b = StringUtils.getBytesUtf8("Hello World");
        final String expected = "48656c6c6f20576f726c64";
        char[] actual;
        actual = Hex.encodeHex0(b);
        assertEquals(expected, new String(actual));
        actual = Hex.encodeHex1(b, true);
        assertEquals(expected, new String(actual));
        actual = Hex.encodeHex1(b, false);
    }

    @Test
    public void testEncodeHexByteArrayHelloWorldLowerCaseHex_test4_decomposed()  {
        final byte[] b = StringUtils.getBytesUtf8("Hello World");
        final String expected = "48656c6c6f20576f726c64";
        char[] actual;
        actual = Hex.encodeHex0(b);
        assertEquals(expected, new String(actual));
        actual = Hex.encodeHex1(b, true);
        assertEquals(expected, new String(actual));
        actual = Hex.encodeHex1(b, false);
        assertNotEquals(expected, new String(actual));
    }

    @Test
    public void testEncodeHexByteArrayHelloWorldUpperCaseHex_test0_decomposed()  {
        final byte[] b = StringUtils.getBytesUtf8("Hello World");
    }

    @Test
    public void testEncodeHexByteArrayHelloWorldUpperCaseHex_test1_decomposed()  {
        final byte[] b = StringUtils.getBytesUtf8("Hello World");
        final String expected = "48656C6C6F20576F726C64";
        char[] actual;
        actual = Hex.encodeHex0(b);
    }

    @Test
    public void testEncodeHexByteArrayHelloWorldUpperCaseHex_test2_decomposed()  {
        final byte[] b = StringUtils.getBytesUtf8("Hello World");
        final String expected = "48656C6C6F20576F726C64";
        char[] actual;
        actual = Hex.encodeHex0(b);
        assertNotEquals(expected, new String(actual));
        actual = Hex.encodeHex1(b, true);
    }

    @Test
    public void testEncodeHexByteArrayHelloWorldUpperCaseHex_test3_decomposed()  {
        final byte[] b = StringUtils.getBytesUtf8("Hello World");
        final String expected = "48656C6C6F20576F726C64";
        char[] actual;
        actual = Hex.encodeHex0(b);
        assertNotEquals(expected, new String(actual));
        actual = Hex.encodeHex1(b, true);
        assertNotEquals(expected, new String(actual));
        actual = Hex.encodeHex1(b, false);
    }

    @Test
    public void testEncodeHexByteArrayHelloWorldUpperCaseHex_test4_decomposed()  {
        final byte[] b = StringUtils.getBytesUtf8("Hello World");
        final String expected = "48656C6C6F20576F726C64";
        char[] actual;
        actual = Hex.encodeHex0(b);
        assertNotEquals(expected, new String(actual));
        actual = Hex.encodeHex1(b, true);
        assertNotEquals(expected, new String(actual));
        actual = Hex.encodeHex1(b, false);
        assertEquals(expected, new String(actual));
    }

    @Test
    public void testEncodeHexByteArrayZeroes_test0_decomposed()  {
        final char[] c = Hex.encodeHex0(new byte[36]);
    }

    @Test
    public void testEncodeHexByteArrayZeroes_test1_decomposed()  {
        final char[] c = Hex.encodeHex0(new byte[36]);
        assertEquals(
                "000000000000000000000000000000000000000000000000000000000000000000000000",
                new String(c));
    }

    @Test
    public void testEncodeHexByteBufferEmpty_test0_decomposed()  {
        allocate(0);
    }

    @Test
    public void testEncodeHexByteBufferEmpty_test1_decomposed()  {
        allocate(0);
        assertArrayEquals(new char[0], Hex.encodeHex6(allocate(0)));
    }

    @Test
    public void testEncodeHexByteBufferEmpty_test2_decomposed()  {
        allocate(0);
        assertArrayEquals(new char[0], Hex.encodeHex6(allocate(0)));
        allocate(0);
    }

    @Test
    public void testEncodeHexByteBufferEmpty_test3_decomposed()  {
        allocate(0);
        assertArrayEquals(new char[0], Hex.encodeHex6(allocate(0)));
        allocate(0);
        assertArrayEquals(new byte[0], new Hex(2, null, null).encode1(allocate(0)));
    }

    @Test
    public void testEncodeHexByteBufferHelloWorldLowerCaseHex_test0_decomposed()  {
        final ByteBuffer b = getByteBufferUtf8("Hello World");
    }

    @Test
    public void testEncodeHexByteBufferHelloWorldLowerCaseHex_test1_decomposed()  {
        final ByteBuffer b = getByteBufferUtf8("Hello World");
        final String expected = "48656c6c6f20576f726c64";
        char[] actual;
        actual = Hex.encodeHex6(b);
    }

    @Test
    public void testEncodeHexByteBufferHelloWorldLowerCaseHex_test2_decomposed()  {
        final ByteBuffer b = getByteBufferUtf8("Hello World");
        final String expected = "48656c6c6f20576f726c64";
        char[] actual;
        actual = Hex.encodeHex6(b);
        assertEquals(expected, new String(actual));
        assertEquals(0, b.remaining());
    }

    @Test
    public void testEncodeHexByteBufferHelloWorldLowerCaseHex_test3_decomposed()  {
        final ByteBuffer b = getByteBufferUtf8("Hello World");
        final String expected = "48656c6c6f20576f726c64";
        char[] actual;
        actual = Hex.encodeHex6(b);
        assertEquals(expected, new String(actual));
        assertEquals(0, b.remaining());
        b.flip();
        actual = Hex.encodeHex7(b, true);
    }

    @Test
    public void testEncodeHexByteBufferHelloWorldLowerCaseHex_test4_decomposed()  {
        final ByteBuffer b = getByteBufferUtf8("Hello World");
        final String expected = "48656c6c6f20576f726c64";
        char[] actual;
        actual = Hex.encodeHex6(b);
        assertEquals(expected, new String(actual));
        assertEquals(0, b.remaining());
        b.flip();
        actual = Hex.encodeHex7(b, true);
        assertEquals(expected, new String(actual));
        assertEquals(0, b.remaining());
    }

    @Test
    public void testEncodeHexByteBufferHelloWorldLowerCaseHex_test5_decomposed()  {
        final ByteBuffer b = getByteBufferUtf8("Hello World");
        final String expected = "48656c6c6f20576f726c64";
        char[] actual;
        actual = Hex.encodeHex6(b);
        assertEquals(expected, new String(actual));
        assertEquals(0, b.remaining());
        b.flip();
        actual = Hex.encodeHex7(b, true);
        assertEquals(expected, new String(actual));
        assertEquals(0, b.remaining());
        b.flip();
        actual = Hex.encodeHex7(b, false);
    }

    @Test
    public void testEncodeHexByteBufferHelloWorldLowerCaseHex_test6_decomposed()  {
        final ByteBuffer b = getByteBufferUtf8("Hello World");
        final String expected = "48656c6c6f20576f726c64";
        char[] actual;
        actual = Hex.encodeHex6(b);
        assertEquals(expected, new String(actual));
        assertEquals(0, b.remaining());
        b.flip();
        actual = Hex.encodeHex7(b, true);
        assertEquals(expected, new String(actual));
        assertEquals(0, b.remaining());
        b.flip();
        actual = Hex.encodeHex7(b, false);
        assertEquals(expected.toUpperCase(), new String(actual));
        assertEquals(0, b.remaining());
    }

    @Test
    public void testEncodeHexByteBufferHelloWorldUpperCaseHex_test0_decomposed()  {
        final ByteBuffer b = getByteBufferUtf8("Hello World");
    }

    @Test
    public void testEncodeHexByteBufferHelloWorldUpperCaseHex_test1_decomposed()  {
        final ByteBuffer b = getByteBufferUtf8("Hello World");
        final String expected = "48656C6C6F20576F726C64";
        char[] actual;
        actual = Hex.encodeHex6(b);
    }

    @Test
    public void testEncodeHexByteBufferHelloWorldUpperCaseHex_test2_decomposed()  {
        final ByteBuffer b = getByteBufferUtf8("Hello World");
        final String expected = "48656C6C6F20576F726C64";
        char[] actual;
        actual = Hex.encodeHex6(b);
        assertEquals(expected.toLowerCase(), new String(actual));
        assertEquals(0, b.remaining());
    }

    @Test
    public void testEncodeHexByteBufferHelloWorldUpperCaseHex_test3_decomposed()  {
        final ByteBuffer b = getByteBufferUtf8("Hello World");
        final String expected = "48656C6C6F20576F726C64";
        char[] actual;
        actual = Hex.encodeHex6(b);
        assertEquals(expected.toLowerCase(), new String(actual));
        assertEquals(0, b.remaining());
        b.flip();
        actual = Hex.encodeHex7(b, true);
    }

    @Test
    public void testEncodeHexByteBufferHelloWorldUpperCaseHex_test4_decomposed()  {
        final ByteBuffer b = getByteBufferUtf8("Hello World");
        final String expected = "48656C6C6F20576F726C64";
        char[] actual;
        actual = Hex.encodeHex6(b);
        assertEquals(expected.toLowerCase(), new String(actual));
        assertEquals(0, b.remaining());
        b.flip();
        actual = Hex.encodeHex7(b, true);
        assertEquals(expected.toLowerCase(), new String(actual));
        assertEquals(0, b.remaining());
    }

    @Test
    public void testEncodeHexByteBufferHelloWorldUpperCaseHex_test5_decomposed()  {
        final ByteBuffer b = getByteBufferUtf8("Hello World");
        final String expected = "48656C6C6F20576F726C64";
        char[] actual;
        actual = Hex.encodeHex6(b);
        assertEquals(expected.toLowerCase(), new String(actual));
        assertEquals(0, b.remaining());
        b.flip();
        actual = Hex.encodeHex7(b, true);
        assertEquals(expected.toLowerCase(), new String(actual));
        assertEquals(0, b.remaining());
        b.flip();
        actual = Hex.encodeHex7(b, false);
    }

    @Test
    public void testEncodeHexByteBufferHelloWorldUpperCaseHex_test6_decomposed()  {
        final ByteBuffer b = getByteBufferUtf8("Hello World");
        final String expected = "48656C6C6F20576F726C64";
        char[] actual;
        actual = Hex.encodeHex6(b);
        assertEquals(expected.toLowerCase(), new String(actual));
        assertEquals(0, b.remaining());
        b.flip();
        actual = Hex.encodeHex7(b, true);
        assertEquals(expected.toLowerCase(), new String(actual));
        assertEquals(0, b.remaining());
        b.flip();
        actual = Hex.encodeHex7(b, false);
        assertEquals(expected, new String(actual));
        assertEquals(0, b.remaining());
    }

    @Test
    public void testEncodeHex_ByteBufferOfZeroes_test0_decomposed()  {
        allocate(36);
    }

    @Test
    public void testEncodeHex_ByteBufferOfZeroes_test1_decomposed()  {
        allocate(36);
        final char[] c = Hex.encodeHex6(allocate(36));
    }

    @Test
    public void testEncodeHex_ByteBufferOfZeroes_test2_decomposed()  {
        allocate(36);
        final char[] c = Hex.encodeHex6(allocate(36));
        assertEquals(
                "000000000000000000000000000000000000000000000000000000000000000000000000",
                new String(c));
    }

    @Test
    public void testEncodeHex_ByteBufferWithLimit_test0_decomposed()  {
        final ByteBuffer bb = allocate(16);
    }

    @Test
    public void testEncodeHex_ByteBufferWithLimit_test1_decomposed()  {
        final ByteBuffer bb = allocate(16);
        for (int i = 0; i < 16; i++) {
            bb.put((byte) i);
        }
    }

    @Test
    public void testEncodeHex_ByteBufferWithLimit_test2_decomposed()  {
        final ByteBuffer bb = allocate(16);
        for (int i = 0; i < 16; i++) {
            bb.put((byte) i);
        }
        bb.flip();
        final String expected = "000102030405060708090a0b0c0d0e0f";
        for (int i = 0; i < 15; i++) {
            bb.position(i);
            bb.limit(i + 2);
            assertEquals(expected.substring(i * 2, i * 2 + 4), new String(Hex.encodeHex6(bb)));
            assertEquals(0, bb.remaining());
        }
    }

    @Test
    public void testEncodeHexPartialInput_test0_decomposed()  {
        final byte data[] = "hello world".getBytes(StandardCharsets.UTF_8);
    }

    @Test
    public void testEncodeHexPartialInput_test1_decomposed()  {
        final byte data[] = "hello world".getBytes(StandardCharsets.UTF_8);
        char[] hex = Hex.encodeHex3(data, 0, 0, true);
    }

    @Test
    public void testEncodeHexPartialInput_test2_decomposed()  {
        final byte data[] = "hello world".getBytes(StandardCharsets.UTF_8);
        char[] hex = Hex.encodeHex3(data, 0, 0, true);
        assertArrayEquals(new char[0], hex);
        hex = Hex.encodeHex3(data, 0, 1, true);
    }

    @Test
    public void testEncodeHexPartialInput_test3_decomposed()  {
        final byte data[] = "hello world".getBytes(StandardCharsets.UTF_8);
        char[] hex = Hex.encodeHex3(data, 0, 0, true);
        assertArrayEquals(new char[0], hex);
        hex = Hex.encodeHex3(data, 0, 1, true);
        assertArrayEquals("68".toCharArray(), hex);
        hex = Hex.encodeHex3(data, 0, 1, false);
    }

    @Test
    public void testEncodeHexPartialInput_test4_decomposed()  {
        final byte data[] = "hello world".getBytes(StandardCharsets.UTF_8);
        char[] hex = Hex.encodeHex3(data, 0, 0, true);
        assertArrayEquals(new char[0], hex);
        hex = Hex.encodeHex3(data, 0, 1, true);
        assertArrayEquals("68".toCharArray(), hex);
        hex = Hex.encodeHex3(data, 0, 1, false);
        assertArrayEquals("68".toCharArray(), hex);
        hex = Hex.encodeHex3(data, 2, 4, true);
    }

    @Test
    public void testEncodeHexPartialInput_test5_decomposed()  {
        final byte data[] = "hello world".getBytes(StandardCharsets.UTF_8);
        char[] hex = Hex.encodeHex3(data, 0, 0, true);
        assertArrayEquals(new char[0], hex);
        hex = Hex.encodeHex3(data, 0, 1, true);
        assertArrayEquals("68".toCharArray(), hex);
        hex = Hex.encodeHex3(data, 0, 1, false);
        assertArrayEquals("68".toCharArray(), hex);
        hex = Hex.encodeHex3(data, 2, 4, true);
        assertArrayEquals("6c6c6f20".toCharArray(), hex);
        hex = Hex.encodeHex3(data, 2, 4, false);
    }

    @Test
    public void testEncodeHexPartialInput_test6_decomposed()  {
        final byte data[] = "hello world".getBytes(StandardCharsets.UTF_8);
        char[] hex = Hex.encodeHex3(data, 0, 0, true);
        assertArrayEquals(new char[0], hex);
        hex = Hex.encodeHex3(data, 0, 1, true);
        assertArrayEquals("68".toCharArray(), hex);
        hex = Hex.encodeHex3(data, 0, 1, false);
        assertArrayEquals("68".toCharArray(), hex);
        hex = Hex.encodeHex3(data, 2, 4, true);
        assertArrayEquals("6c6c6f20".toCharArray(), hex);
        hex = Hex.encodeHex3(data, 2, 4, false);
        assertArrayEquals("6C6C6F20".toCharArray(), hex);
        hex = Hex.encodeHex3(data, 10, 1, true);
    }

    @Test
    public void testEncodeHexPartialInput_test7_decomposed()  {
        final byte data[] = "hello world".getBytes(StandardCharsets.UTF_8);
        char[] hex = Hex.encodeHex3(data, 0, 0, true);
        assertArrayEquals(new char[0], hex);
        hex = Hex.encodeHex3(data, 0, 1, true);
        assertArrayEquals("68".toCharArray(), hex);
        hex = Hex.encodeHex3(data, 0, 1, false);
        assertArrayEquals("68".toCharArray(), hex);
        hex = Hex.encodeHex3(data, 2, 4, true);
        assertArrayEquals("6c6c6f20".toCharArray(), hex);
        hex = Hex.encodeHex3(data, 2, 4, false);
        assertArrayEquals("6C6C6F20".toCharArray(), hex);
        hex = Hex.encodeHex3(data, 10, 1, true);
        assertArrayEquals("64".toCharArray(), hex);
        hex = Hex.encodeHex3(data, 10, 1, false);
    }

    @Test
    public void testEncodeHexPartialInput_test8_decomposed()  {
        final byte data[] = "hello world".getBytes(StandardCharsets.UTF_8);
        char[] hex = Hex.encodeHex3(data, 0, 0, true);
        assertArrayEquals(new char[0], hex);
        hex = Hex.encodeHex3(data, 0, 1, true);
        assertArrayEquals("68".toCharArray(), hex);
        hex = Hex.encodeHex3(data, 0, 1, false);
        assertArrayEquals("68".toCharArray(), hex);
        hex = Hex.encodeHex3(data, 2, 4, true);
        assertArrayEquals("6c6c6f20".toCharArray(), hex);
        hex = Hex.encodeHex3(data, 2, 4, false);
        assertArrayEquals("6C6C6F20".toCharArray(), hex);
        hex = Hex.encodeHex3(data, 10, 1, true);
        assertArrayEquals("64".toCharArray(), hex);
        hex = Hex.encodeHex3(data, 10, 1, false);
        assertArrayEquals("64".toCharArray(), hex);
    }

    @Test
    public void testEncodeHexPartialInputUnderbounds_test0_decomposed()  {
        final byte data[] = "hello world".getBytes(StandardCharsets.UTF_8);
    }

    @Test(expected = ArrayIndexOutOfBoundsException.class)
    public void testEncodeHexPartialInputUnderbounds_test1_decomposed()  {
        final byte data[] = "hello world".getBytes(StandardCharsets.UTF_8);
        final char[] hex = Hex.encodeHex3(data, -2, 10, true);
    }

    @Test(expected = ArrayIndexOutOfBoundsException.class)
    public void testEncodeHexPartialInputUnderbounds_test2_decomposed()  {
        final byte data[] = "hello world".getBytes(StandardCharsets.UTF_8);
        final char[] hex = Hex.encodeHex3(data, -2, 10, true);
        assertArrayEquals("64".toCharArray(), hex);
    }

    @Test
    public void testEncodeHexPartialInputOverbounds_test0_decomposed()  {
        final byte data[] = "hello world".getBytes(StandardCharsets.UTF_8);
    }

    @Test(expected = ArrayIndexOutOfBoundsException.class)
    public void testEncodeHexPartialInputOverbounds_test1_decomposed()  {
        final byte data[] = "hello world".getBytes(StandardCharsets.UTF_8);
        final char[] hex = Hex.encodeHex3(data, 9, 10, true);
    }

    @Test(expected = ArrayIndexOutOfBoundsException.class)
    public void testEncodeHexPartialInputOverbounds_test2_decomposed()  {
        final byte data[] = "hello world".getBytes(StandardCharsets.UTF_8);
        final char[] hex = Hex.encodeHex3(data, 9, 10, true);
        assertArrayEquals("64".toCharArray(), hex);
    }

    @Test
    public void testEncodeHexByteString_ByteBufferOfZeroes_test0_decomposed()  {
        allocate(36);
    }

    @Test
    public void testEncodeHexByteString_ByteBufferOfZeroes_test1_decomposed()  {
        allocate(36);
        final String c = Hex.encodeHexString2(allocate(36));
    }

    @Test
    public void testEncodeHexByteString_ByteBufferOfZeroes_test2_decomposed()  {
        allocate(36);
        final String c = Hex.encodeHexString2(allocate(36));
        assertEquals("000000000000000000000000000000000000000000000000000000000000000000000000", c);
    }

    @Test
    public void testEncodeHexByteString_ByteBufferOfZeroesWithLimit_test0_decomposed()  {
        final ByteBuffer bb = allocate(36);
    }

    @Test
    public void testEncodeHexByteString_ByteBufferOfZeroesWithLimit_test1_decomposed()  {
        final ByteBuffer bb = allocate(36);
        bb.limit(3);
        assertEquals("000000", Hex.encodeHexString2(bb));
    }

    @Test
    public void testEncodeHexByteString_ByteBufferOfZeroesWithLimit_test2_decomposed()  {
        final ByteBuffer bb = allocate(36);
        bb.limit(3);
        assertEquals("000000", Hex.encodeHexString2(bb));
        assertEquals(0, bb.remaining());
        bb.position(1);
        bb.limit(3);
        assertEquals("0000", Hex.encodeHexString2(bb));
    }

    @Test
    public void testEncodeHexByteString_ByteBufferOfZeroesWithLimit_test3_decomposed()  {
        final ByteBuffer bb = allocate(36);
        bb.limit(3);
        assertEquals("000000", Hex.encodeHexString2(bb));
        assertEquals(0, bb.remaining());
        bb.position(1);
        bb.limit(3);
        assertEquals("0000", Hex.encodeHexString2(bb));
        assertEquals(0, bb.remaining());
    }

    @Test
    public void testEncodeHexByteString_ByteArrayOfZeroes_test0_decomposed()  {
        final String c = Hex.encodeHexString0(new byte[36]);
    }

    @Test
    public void testEncodeHexByteString_ByteArrayOfZeroes_test1_decomposed()  {
        final String c = Hex.encodeHexString0(new byte[36]);
        assertEquals("000000000000000000000000000000000000000000000000000000000000000000000000", c);
    }

    @Test
    public void testEncodeHexByteString_ByteArrayBoolean_ToLowerCase_test0_decomposed()  {
        assertEquals("0a", Hex.encodeHexString1(new byte[] {10}, true));
    }

    @Test
    public void testEncodeHexByteString_ByteArrayBoolean_ToUpperCase_test0_decomposed()  {
        assertEquals("0A", Hex.encodeHexString1(new byte[] {10}, false));
    }

    @Test
    public void testEncodeHexByteString_ByteBufferBoolean_ToLowerCase_test0_decomposed()  {
        final ByteBuffer bb = allocate(1);
    }

    @Test
    public void testEncodeHexByteString_ByteBufferBoolean_ToLowerCase_test1_decomposed()  {
        final ByteBuffer bb = allocate(1);
        bb.put((byte) 10);
    }

    @Test
    public void testEncodeHexByteString_ByteBufferBoolean_ToLowerCase_test2_decomposed()  {
        final ByteBuffer bb = allocate(1);
        bb.put((byte) 10);
        bb.flip();
        assertEquals("0a", Hex.encodeHexString3(bb, true));
    }

    @Test
    public void testEncodeHexByteString_ByteBufferBoolean_ToUpperCase_test0_decomposed()  {
        final ByteBuffer bb = allocate(1);
    }

    @Test
    public void testEncodeHexByteString_ByteBufferBoolean_ToUpperCase_test1_decomposed()  {
        final ByteBuffer bb = allocate(1);
        bb.put((byte) 10);
    }

    @Test
    public void testEncodeHexByteString_ByteBufferBoolean_ToUpperCase_test2_decomposed()  {
        final ByteBuffer bb = allocate(1);
        bb.put((byte) 10);
        bb.flip();
        assertEquals("0A", Hex.encodeHexString3(bb, false));
    }

    @Test
    public void testEncodeHexByteString_ByteBufferWithLimitBoolean_ToLowerCase_test0_decomposed()  {
        final ByteBuffer bb = allocate(4);
    }

    @Test
    public void testEncodeHexByteString_ByteBufferWithLimitBoolean_ToLowerCase_test1_decomposed()  {
        final ByteBuffer bb = allocate(4);
        bb.put(1, (byte) 10);
    }

    @Test
    public void testEncodeHexByteString_ByteBufferWithLimitBoolean_ToLowerCase_test2_decomposed()  {
        final ByteBuffer bb = allocate(4);
        bb.put(1, (byte) 10);
        bb.position(1);
        bb.limit(2);
        assertEquals("0a", Hex.encodeHexString3(bb, true));
    }

    @Test
    public void testEncodeHexByteString_ByteBufferWithLimitBoolean_ToLowerCase_test3_decomposed()  {
        final ByteBuffer bb = allocate(4);
        bb.put(1, (byte) 10);
        bb.position(1);
        bb.limit(2);
        assertEquals("0a", Hex.encodeHexString3(bb, true));
        assertEquals(0, bb.remaining());
    }

    @Test
    public void testEncodeHexByteString_ByteBufferWithLimitBoolean_ToUpperCase_test0_decomposed()  {
        final ByteBuffer bb = allocate(4);
    }

    @Test
    public void testEncodeHexByteString_ByteBufferWithLimitBoolean_ToUpperCase_test1_decomposed()  {
        final ByteBuffer bb = allocate(4);
        bb.put(1, (byte) 10);
    }

    @Test
    public void testEncodeHexByteString_ByteBufferWithLimitBoolean_ToUpperCase_test2_decomposed()  {
        final ByteBuffer bb = allocate(4);
        bb.put(1, (byte) 10);
        bb.position(1);
        bb.limit(2);
        assertEquals("0A", Hex.encodeHexString3(bb, false));
    }

    @Test
    public void testEncodeHexByteString_ByteBufferWithLimitBoolean_ToUpperCase_test3_decomposed()  {
        final ByteBuffer bb = allocate(4);
        bb.put(1, (byte) 10);
        bb.position(1);
        bb.limit(2);
        assertEquals("0A", Hex.encodeHexString3(bb, false));
        assertEquals(0, bb.remaining());
    }

    @Test
    public void testEncodeHexReadOnlyByteBuffer_test0_decomposed()  {
        final char[] chars = Hex.encodeHex6(ByteBuffer.wrap(new byte[] {10}).asReadOnlyBuffer());
    }

    @Test
    public void testEncodeHexReadOnlyByteBuffer_test1_decomposed()  {
        final char[] chars = Hex.encodeHex6(ByteBuffer.wrap(new byte[] {10}).asReadOnlyBuffer());
        assertEquals("0a", String.valueOf(chars));
    }

    @Test
    public void testEncodeStringEmpty_test0_decomposed() throws EncoderException {
        assertArrayEquals(new char[0], (char[]) new Hex(2, null, null).encode2(""));
    }

    @Test
    public void testGetCharset_test0_decomposed()  {
        Assert.assertEquals(
                StandardCharsets.UTF_8, new Hex(1, null, StandardCharsets.UTF_8).getCharset());
    }

    @Test
    public void testGetCharsetName_test0_decomposed()  {
        Assert.assertEquals(
                StandardCharsets.UTF_8.name(),
                new Hex(1, null, StandardCharsets.UTF_8).getCharsetName());
    }

    @Test
    public void testRequiredCharset_test0_decomposed() throws UnsupportedEncodingException , DecoderException {
        testCustomCharset1("UTF-8", "testRequiredCharset");
        testCustomCharset1("UTF-16", "testRequiredCharset");
        testCustomCharset1("UTF-16BE", "testRequiredCharset");
        testCustomCharset1("UTF-16LE", "testRequiredCharset");
        testCustomCharset1("US-ASCII", "testRequiredCharset");
        testCustomCharset1("ISO8859_1", "testRequiredCharset");
    }
}