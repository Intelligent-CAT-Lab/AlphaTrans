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
import static org.junit.Assert.assertFalse;
import static org.junit.Assert.fail;

import org.junit.Test;

import java.io.ByteArrayInputStream;
import java.io.IOException;
import java.io.InputStream;

public class Base32InputStreamTest {

    private static final String ENCODED_FOO = "MZXW6===";

    private static final byte[] CRLF = {(byte) '\r', (byte) '\n'};

    private static final byte[] LF = {(byte) '\n'};

    private static final String STRING_FIXTURE = "Hello World";

    /** Tests the problem reported in CODEC-130. Missing / wrong implementation of skip. */

    /**
     * Tests the bug reported in CODEC-105. Bad interactions with InputStream when reading one byte
     * at a time.
     */
    

    /**
     * Another test for the CODEC-101 bug: In commons-codec-1.4 this test shows InputStreamReader
     * explicitly hating an InputStream.read(byte[]) return of 0:
     *
     * <p>java.io.IOException: Underlying input stream returned zero bytes at
     * sun.nio.cs.StreamDecoder.readBytes(StreamDecoder.java:268) at
     * sun.nio.cs.StreamDecoder.implRead(StreamDecoder.java:306) at
     * sun.nio.cs.StreamDecoder.read(StreamDecoder.java:158) at
     * java.io.InputStreamReader.read(InputStreamReader.java:167) at
     * java.io.BufferedReader.fill(BufferedReader.java:136) at
     * java.io.BufferedReader.readLine(BufferedReader.java:299) at
     * java.io.BufferedReader.readLine(BufferedReader.java:362) at
     * org.apache.commons.codec.binary.Base32InputStreamTest.testInputStreamReader(Base32InputStreamTest.java:75)
     *
     * <p>But in commons-codec-1.5 it's fixed. :-)
     *
     * @throws Exception for some failure scenarios.
     */

    /**
     * Test the Base32InputStream implementation against the special NPE inducing input identified
     * in the CODEC-98 bug.
     *
     * @throws Exception for some failure scenarios.
     */

    /**
     * Tests skipping past the end of a stream.
     *
     * @throws Throwable for some failure scenarios.
     */
    

    /**
     * Tests the Base32InputStream implementation against empty input.
     *
     * @throws Exception for some failure scenarios.
     */
    

    /**
     * Tests the Base32InputStream implementation against empty input.
     *
     * @throws Exception for some failure scenarios.
     */
    

    private void testBase32EmptyInputStream(final int chuckSize) throws Exception {
        final byte[] emptyEncoded = {};
        final byte[] emptyDecoded = {};
        testByteByByte(emptyEncoded, emptyDecoded, chuckSize, CRLF);
        testByChunk(emptyEncoded, emptyDecoded, chuckSize, CRLF);
    }

    /**
     * Tests the Base32InputStream implementation.
     *
     * @throws Exception for some failure scenarios.
     */

    /**
     * Tests the Base32InputStream implementation.
     *
     * @throws Exception for some failure scenarios.
     */

    /**
     * Tests method does three tests on the supplied data: 1. encoded ---[DECODE]--> decoded 2.
     * decoded ---[ENCODE]--> encoded 3. decoded ---[WRAP-WRAP-WRAP-etc...] --> decoded
     *
     * <p>By "[WRAP-WRAP-WRAP-etc...]" we mean situation where the Base32InputStream wraps itself in
     * encode and decode mode over and over again.
     *
     * @param encoded base32 encoded data
     * @param decoded the data from above, but decoded
     * @param chunkSize chunk size (line-length) of the base32 encoded data.
     * @param separator Line separator in the base32 encoded data.
     * @throws Exception Usually signifies a bug in the Base32 commons-codec implementation.
     */
    private void testByChunk(
            final byte[] encoded, final byte[] decoded, final int chunkSize, final byte[] separator)
            throws Exception {

        InputStream in;

        in =
                Base32InputStream.Base32InputStream2(
                        new ByteArrayInputStream(decoded), true, chunkSize, separator);
        byte[] output = BaseNTestData.streamToBytes0(in);

        assertEquals("EOF", -1, in.read());
        assertEquals("Still EOF", -1, in.read());
        assertArrayEquals("Streaming base32 encode", encoded, output);

        in = Base32InputStream.Base32InputStream0(new ByteArrayInputStream(encoded));
        output = BaseNTestData.streamToBytes0(in);

        assertEquals("EOF", -1, in.read());
        assertEquals("Still EOF", -1, in.read());
        assertArrayEquals("Streaming base32 decode", decoded, output);

        in = new ByteArrayInputStream(decoded);
        for (int i = 0; i < 10; i++) {
            in = Base32InputStream.Base32InputStream2(in, true, chunkSize, separator);
            in = Base32InputStream.Base32InputStream1(in, false);
        }
        output = BaseNTestData.streamToBytes0(in);

        assertEquals("EOF", -1, in.read());
        assertEquals("Still EOF", -1, in.read());
        assertArrayEquals("Streaming base32 wrap-wrap-wrap!", decoded, output);
        in.close();
    }

    /**
     * Tests method does three tests on the supplied data: 1. encoded ---[DECODE]--> decoded 2.
     * decoded ---[ENCODE]--> encoded 3. decoded ---[WRAP-WRAP-WRAP-etc...] --> decoded
     *
     * <p>By "[WRAP-WRAP-WRAP-etc...]" we mean situation where the Base32InputStream wraps itself in
     * encode and decode mode over and over again.
     *
     * @param encoded base32 encoded data
     * @param decoded the data from above, but decoded
     * @param chunkSize chunk size (line-length) of the base32 encoded data.
     * @param separator Line separator in the base32 encoded data.
     * @throws Exception Usually signifies a bug in the Base32 commons-codec implementation.
     */
    private void testByteByByte(
            final byte[] encoded, final byte[] decoded, final int chunkSize, final byte[] separator)
            throws Exception {

        InputStream in;
        in =
                Base32InputStream.Base32InputStream2(
                        new ByteArrayInputStream(decoded), true, chunkSize, separator);
        byte[] output = new byte[encoded.length];
        for (int i = 0; i < output.length; i++) {
            output[i] = (byte) in.read();
        }

        assertEquals("EOF", -1, in.read());
        assertEquals("Still EOF", -1, in.read());
        assertArrayEquals("Streaming base32 encode", encoded, output);

        in.close();

        in = Base32InputStream.Base32InputStream0(new ByteArrayInputStream(encoded));
        output = new byte[decoded.length];
        for (int i = 0; i < output.length; i++) {
            output[i] = (byte) in.read();
        }

        assertEquals("EOF", -1, in.read());
        assertEquals("Still EOF", -1, in.read());
        assertArrayEquals("Streaming base32 decode", decoded, output);

        in.close();

        in = new ByteArrayInputStream(decoded);
        for (int i = 0; i < 10; i++) {
            in = Base32InputStream.Base32InputStream2(in, true, chunkSize, separator);
            in = Base32InputStream.Base32InputStream1(in, false);
        }
        output = new byte[decoded.length];
        for (int i = 0; i < output.length; i++) {
            output[i] = (byte) in.read();
        }

        assertEquals("EOF", -1, in.read());
        assertEquals("Still EOF", -1, in.read());
        assertArrayEquals("Streaming base32 wrap-wrap-wrap!", decoded, output);
    }

    /**
     * Tests markSupported.
     *
     * @throws Exception for some failure scenarios.
     */
    

    /**
     * Tests read returning 0
     *
     * @throws Exception for some failure scenarios.
     */
    

    /**
     * Tests read with null.
     *
     * @throws Exception for some failure scenarios.
     */
    

    /**
     * Tests read throwing IndexOutOfBoundsException
     *
     * @throws Exception for some failure scenarios.
     */
    

    /**
     * Tests skipping as a noop
     *
     * @throws Throwable for some failure scenarios.
     */
    

    /**
     * Tests skipping number of characters larger than the internal buffer.
     *
     * @throws Throwable for some failure scenarios.
     */
    

    /**
     * Tests skipping past the end of a stream.
     *
     * @throws Throwable for some failure scenarios.
     */
    

    /**
     * Tests skipping to the end of a stream.
     *
     * @throws Throwable for some failure scenarios.
     */
    

    /**
     * Tests if negative arguments to skip are handled correctly.
     *
     * @throws Throwable for some failure scenarios.
     */
    

    /**
     * Test strict decoding.
     *
     * @throws Exception for some failure scenarios.
     */

    @Test
    public void testCodec105_test0_decomposed() throws IOException {
        try (final BaseNCodecInputStream in =
                Base32InputStream.Base32InputStream2(
                        new Codec105ErrorInputStream(), true, 0, null)) {
            for (int i = 0; i < 5; i++) {
                in.read0();
            }
        }
    }

    @Test
    public void testAvailable_test0_decomposed() throws Throwable {
        final InputStream ins =
                new ByteArrayInputStream(StringUtils.getBytesIso8859_1(ENCODED_FOO));
    }

    @Test
    public void testAvailable_test1_decomposed() throws Throwable {
        final InputStream ins =
                new ByteArrayInputStream(StringUtils.getBytesIso8859_1(ENCODED_FOO));
        try (final BaseNCodecInputStream b32stream =
                (BaseNCodecInputStream) Base32InputStream.Base32InputStream0(ins)) {
            assertEquals(1, b32stream.available());
            assertEquals(3, b32stream.skip(10));
            assertEquals(0, b32stream.available());
            assertEquals(-1, b32stream.read0());
            assertEquals(-1, b32stream.read0());
            assertEquals(0, b32stream.available());
        }
    }

    @Test
    public void testBase32EmptyInputStreamMimeChuckSize_test0_decomposed() throws Exception {
        testBase32EmptyInputStream(BaseNCodec.MIME_CHUNK_SIZE);
    }

    @Test
    public void testBase32EmptyInputStreamPemChuckSize_test0_decomposed() throws Exception {
        testBase32EmptyInputStream(BaseNCodec.PEM_CHUNK_SIZE);
    }

    @Test
    public void testMarkSupported_test0_decomposed() throws Exception {
        final byte[] decoded = StringUtils.getBytesUtf8(Base32TestData.STRING_FIXTURE);
    }

    @Test
    public void testMarkSupported_test1_decomposed() throws Exception {
        final byte[] decoded = StringUtils.getBytesUtf8(Base32TestData.STRING_FIXTURE);
        final ByteArrayInputStream bin = new ByteArrayInputStream(decoded);
        try (final BaseNCodecInputStream in =
                Base32InputStream.Base32InputStream2(bin, true, 4, new byte[] {0, 0, 0})) {
            assertFalse("Base32InputStream.markSupported() is false", in.markSupported());
        }
    }

    @Test
    public void testRead0_test0_decomposed() throws Exception {
        final byte[] decoded = StringUtils.getBytesUtf8(Base32TestData.STRING_FIXTURE);
    }

    @Test
    public void testRead0_test1_decomposed() throws Exception {
        final byte[] decoded = StringUtils.getBytesUtf8(Base32TestData.STRING_FIXTURE);
        final byte[] buf = new byte[1024];
        int bytesRead = 0;
        final ByteArrayInputStream bin = new ByteArrayInputStream(decoded);
        try (final BaseNCodecInputStream in =
                Base32InputStream.Base32InputStream2(bin, true, 4, new byte[] {0, 0, 0})) {
            bytesRead = in.read1(buf, 0, 0);
            assertEquals("Base32InputStream.read(buf, 0, 0) returns 0", 0, bytesRead);
        }
    }

    @Test
    public void testReadNull_test0_decomposed() throws Exception {
        final byte[] decoded = StringUtils.getBytesUtf8(Base32TestData.STRING_FIXTURE);
    }

    @Test
    public void testReadNull_test1_decomposed() throws Exception {
        final byte[] decoded = StringUtils.getBytesUtf8(Base32TestData.STRING_FIXTURE);
        final ByteArrayInputStream bin = new ByteArrayInputStream(decoded);
        try (final BaseNCodecInputStream in =
                Base32InputStream.Base32InputStream2(bin, true, 4, new byte[] {0, 0, 0})) {
            in.read1(null, 0, 0);
            fail("Base32InputStream.read(null, 0, 0) to throw a NullPointerException");
        } catch (final NullPointerException e) {
        }
    }

    @Test
    public void testReadOutOfBounds_test0_decomposed() throws Exception {
        final byte[] decoded = StringUtils.getBytesUtf8(Base32TestData.STRING_FIXTURE);
    }

    @Test
    public void testReadOutOfBounds_test1_decomposed() throws Exception {
        final byte[] decoded = StringUtils.getBytesUtf8(Base32TestData.STRING_FIXTURE);
        final byte[] buf = new byte[1024];
        final ByteArrayInputStream bin = new ByteArrayInputStream(decoded);
        try (final BaseNCodecInputStream in =
                Base32InputStream.Base32InputStream2(bin, true, 4, new byte[] {0, 0, 0})) {

            try {
                in.read1(buf, -1, 0);
                fail(
                        "Expected Base32InputStream.read(buf, -1, 0) to throw"
                                + " IndexOutOfBoundsException");
            } catch (final IndexOutOfBoundsException e) {
            }

            try {
                in.read1(buf, 0, -1);
                fail(
                        "Expected Base32InputStream.read(buf, 0, -1) to throw"
                                + " IndexOutOfBoundsException");
            } catch (final IndexOutOfBoundsException e) {
            }

            try {
                in.read1(buf, buf.length + 1, 0);
                fail(
                        "Base32InputStream.read(buf, buf.length + 1, 0) throws"
                                + " IndexOutOfBoundsException");
            } catch (final IndexOutOfBoundsException e) {
            }

            try {
                in.read1(buf, buf.length - 1, 2);
                fail(
                        "Base32InputStream.read(buf, buf.length - 1, 2) throws"
                                + " IndexOutOfBoundsException");
            } catch (final IndexOutOfBoundsException e) {
            }
        }
    }

    @Test
    public void testSkipNone_test0_decomposed() throws Throwable {
        final InputStream ins =
                new ByteArrayInputStream(StringUtils.getBytesIso8859_1(ENCODED_FOO));
    }

    @Test
    public void testSkipNone_test1_decomposed() throws Throwable {
        final InputStream ins =
                new ByteArrayInputStream(StringUtils.getBytesIso8859_1(ENCODED_FOO));
        try (final BaseNCodecInputStream b32stream = Base32InputStream.Base32InputStream0(ins)) {
            final byte[] actualBytes = new byte[6];
            assertEquals(0, b32stream.skip(0));
            b32stream.read1(actualBytes, 0, actualBytes.length);
            assertArrayEquals(actualBytes, new byte[] {102, 111, 111, 0, 0, 0});
            assertEquals(-1, b32stream.read0());
        }
    }

    @Test
    public void testSkipBig_test0_decomposed() throws Throwable {
        final InputStream ins =
                new ByteArrayInputStream(StringUtils.getBytesIso8859_1(ENCODED_FOO));
    }

    @Test
    public void testSkipBig_test1_decomposed() throws Throwable {
        final InputStream ins =
                new ByteArrayInputStream(StringUtils.getBytesIso8859_1(ENCODED_FOO));
        try (final BaseNCodecInputStream b32stream = Base32InputStream.Base32InputStream0(ins)) {
            assertEquals(3, b32stream.skip(1024));
            assertEquals(-1, b32stream.read0());
            assertEquals(-1, b32stream.read0());
        }
    }

    @Test
    public void testSkipPastEnd_test0_decomposed() throws Throwable {
        final InputStream ins =
                new ByteArrayInputStream(StringUtils.getBytesIso8859_1(ENCODED_FOO));
    }

    @Test
    public void testSkipPastEnd_test1_decomposed() throws Throwable {
        final InputStream ins =
                new ByteArrayInputStream(StringUtils.getBytesIso8859_1(ENCODED_FOO));
        try (final BaseNCodecInputStream b32stream = Base32InputStream.Base32InputStream0(ins)) {
            assertEquals(3, b32stream.skip(10));
            assertEquals(-1, b32stream.read0());
            assertEquals(-1, b32stream.read0());
        }
    }

    @Test
    public void testSkipToEnd_test0_decomposed() throws Throwable {
        final InputStream ins =
                new ByteArrayInputStream(StringUtils.getBytesIso8859_1(ENCODED_FOO));
    }

    @Test
    public void testSkipToEnd_test1_decomposed() throws Throwable {
        final InputStream ins =
                new ByteArrayInputStream(StringUtils.getBytesIso8859_1(ENCODED_FOO));
        try (final BaseNCodecInputStream b32stream = Base32InputStream.Base32InputStream0(ins)) {
            assertEquals(3, b32stream.skip(3));
            assertEquals(-1, b32stream.read0());
            assertEquals(-1, b32stream.read0());
        }
    }

    @Test
    public void testSkipWrongArgument_test0_decomposed() throws Throwable {
        final InputStream ins =
                new ByteArrayInputStream(StringUtils.getBytesIso8859_1(ENCODED_FOO));
    }

    @Test(expected = IllegalArgumentException.class)
    public void testSkipWrongArgument_test1_decomposed() throws Throwable {
        final InputStream ins =
                new ByteArrayInputStream(StringUtils.getBytesIso8859_1(ENCODED_FOO));
        try (final BaseNCodecInputStream b32stream = Base32InputStream.Base32InputStream0(ins)) {
            b32stream.skip(-10);
        }
    }
}