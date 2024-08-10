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
import static org.junit.Assert.assertNotNull;
import static org.junit.Assert.assertTrue;
import static org.junit.Assert.fail;

import org.junit.Test;

import java.io.BufferedReader;
import java.io.ByteArrayInputStream;
import java.io.IOException;
import java.io.InputStream;
import java.io.InputStreamReader;

/**
 * @since 1.4
 */
public class Base64InputStreamTest {

    /** Decodes to {0, 0, 0, 255, 255, 255} */
    private static final String ENCODED_B64 = "AAAA////";

    private static final byte[] CRLF = {(byte) '\r', (byte) '\n'};

    private static final byte[] LF = {(byte) '\n'};

    private static final String STRING_FIXTURE = "Hello World";

    /** Tests the problem reported in CODEC-130. Missing / wrong implementation of skip. */

    /**
     * Tests the bug reported in CODEC-105. Bad interactions with InputStream when reading one byte
     * at a time.
     */
    

    /**
     * Test for the CODEC-101 bug: InputStream.read(byte[]) should never return 0 because Java's
     * builtin InputStreamReader hates that.
     *
     * @throws Exception for some failure scenarios.
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
     * org.apache.commons.codec.binary.Base64InputStreamTest.testInputStreamReader(Base64InputStreamTest.java:75)
     *
     * <p>But in commons-codec-1.5 it's fixed. :-)
     *
     * @throws Exception for some failure scenarios.
     */
    

    /**
     * Test the Base64InputStream implementation against the special NPE inducing input identified
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
     * Tests the Base64InputStream implementation against empty input.
     *
     * @throws Exception for some failure scenarios.
     */
    

    /**
     * Tests the Base64InputStream implementation against empty input.
     *
     * @throws Exception for some failure scenarios.
     */
    

    private void testBase64EmptyInputStream(final int chuckSize) throws Exception {
        final byte[] emptyEncoded = {};
        final byte[] emptyDecoded = {};
        testByteByByte(emptyEncoded, emptyDecoded, chuckSize, CRLF);
        testByChunk(emptyEncoded, emptyDecoded, chuckSize, CRLF);
    }

    /**
     * Tests the Base64InputStream implementation.
     *
     * @throws Exception for some failure scenarios.
     */

    /**
     * Tests the Base64InputStream implementation.
     *
     * @throws Exception for some failure scenarios.
     */

    /**
     * Tests method does three tests on the supplied data: 1. encoded ---[DECODE]--> decoded 2.
     * decoded ---[ENCODE]--> encoded 3. decoded ---[WRAP-WRAP-WRAP-etc...] --> decoded
     *
     * <p>By "[WRAP-WRAP-WRAP-etc...]" we mean situation where the Base64InputStream wraps itself in
     * encode and decode mode over and over again.
     *
     * @param encoded base64 encoded data
     * @param decoded the data from above, but decoded
     * @param chunkSize chunk size (line-length) of the base64 encoded data.
     * @param separator Line separator in the base64 encoded data.
     * @throws Exception Usually signifies a bug in the Base64 commons-codec implementation.
     */
    private void testByChunk(
            final byte[] encoded, final byte[] decoded, final int chunkSize, final byte[] separator)
            throws Exception {

        InputStream in;
        in =
                Base64InputStream.Base64InputStream2(
                        new ByteArrayInputStream(decoded), true, chunkSize, separator);
        byte[] output = BaseNTestData.streamToBytes0(in);

        assertEquals("EOF", -1, in.read());
        assertEquals("Still EOF", -1, in.read());
        assertArrayEquals("Streaming base64 encode", encoded, output);

        in.close();

        in = Base64InputStream.Base64InputStream0(new ByteArrayInputStream(encoded));
        output = BaseNTestData.streamToBytes0(in);

        assertEquals("EOF", -1, in.read());
        assertEquals("Still EOF", -1, in.read());
        assertArrayEquals("Streaming base64 decode", decoded, output);

        in = new ByteArrayInputStream(decoded);
        for (int i = 0; i < 10; i++) {
            in = Base64InputStream.Base64InputStream2(in, true, chunkSize, separator);
            in = Base64InputStream.Base64InputStream1(in, false);
        }
        output = BaseNTestData.streamToBytes0(in);

        assertEquals("EOF", -1, in.read());
        assertEquals("Still EOF", -1, in.read());
        assertArrayEquals("Streaming base64 wrap-wrap-wrap!", decoded, output);
        in.close();
    }

    /**
     * Tests method does three tests on the supplied data: 1. encoded ---[DECODE]--> decoded 2.
     * decoded ---[ENCODE]--> encoded 3. decoded ---[WRAP-WRAP-WRAP-etc...] --> decoded
     *
     * <p>By "[WRAP-WRAP-WRAP-etc...]" we mean situation where the Base64InputStream wraps itself in
     * encode and decode mode over and over again.
     *
     * @param encoded base64 encoded data
     * @param decoded the data from above, but decoded
     * @param chunkSize chunk size (line-length) of the base64 encoded data.
     * @param separator Line separator in the base64 encoded data.
     * @throws Exception Usually signifies a bug in the Base64 commons-codec implementation.
     */
    private void testByteByByte(
            final byte[] encoded, final byte[] decoded, final int chunkSize, final byte[] separator)
            throws Exception {

        InputStream in;
        in =
                Base64InputStream.Base64InputStream2(
                        new ByteArrayInputStream(decoded), true, chunkSize, separator);
        byte[] output = new byte[encoded.length];
        for (int i = 0; i < output.length; i++) {
            output[i] = (byte) in.read();
        }

        assertEquals("EOF", -1, in.read());
        assertEquals("Still EOF", -1, in.read());
        assertArrayEquals("Streaming base64 encode", encoded, output);

        in.close();
        in = Base64InputStream.Base64InputStream0(new ByteArrayInputStream(encoded));
        output = new byte[decoded.length];
        for (int i = 0; i < output.length; i++) {
            output[i] = (byte) in.read();
        }

        assertEquals("EOF", -1, in.read());
        assertEquals("Still EOF", -1, in.read());
        assertArrayEquals("Streaming base64 decode", decoded, output);

        in.close();

        in = new ByteArrayInputStream(decoded);
        for (int i = 0; i < 10; i++) {
            in = Base64InputStream.Base64InputStream2(in, true, chunkSize, separator);
            in = Base64InputStream.Base64InputStream1(in, false);
        }
        output = new byte[decoded.length];
        for (int i = 0; i < output.length; i++) {
            output[i] = (byte) in.read();
        }

        assertEquals("EOF", -1, in.read());
        assertEquals("Still EOF", -1, in.read());
        assertArrayEquals("Streaming base64 wrap-wrap-wrap!", decoded, output);
        in.close();
    }

    /**
     * Tests markSupported.
     *
     * @throws Exception for some failure scenarios.
     */
    

    /**
     * Tests read using different buffer sizes
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
     * Tests skipping number of characters larger than the internal buffer.
     *
     * @throws Throwable for some failure scenarios.
     */
    

    /**
     * Tests skipping as a noop
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
                Base64InputStream.Base64InputStream2(
                        new Codec105ErrorInputStream(), true, 0, null)) {
            for (int i = 0; i < 5; i++) {
                in.read0();
            }
        }
    }

    @Test
    public void testCodec101_test0_decomposed() throws Exception {
        final byte[] codec101 =
                StringUtils.getBytesUtf8(Base64TestData.CODEC_101_INPUT_LENGTH_IS_MULTIPLE_OF_3);
    }

    @Test
    public void testCodec101_test1_decomposed() throws Exception {
        final byte[] codec101 =
                StringUtils.getBytesUtf8(Base64TestData.CODEC_101_INPUT_LENGTH_IS_MULTIPLE_OF_3);
        final ByteArrayInputStream bais = new ByteArrayInputStream(codec101);
        try (final BaseNCodecInputStream in = Base64InputStream.Base64InputStream0(bais)) {
            final byte[] result = new byte[8192];
            int c = in.read(result);
            assertTrue("Codec101: First read successful [c=" + c + "]", c > 0);

            c = in.read(result);
            assertTrue("Codec101: Second read should report end-of-stream [c=" + c + "]", c < 0);
        }
    }

    @Test
    public void testInputStreamReader_test0_decomposed() throws Exception {
        final byte[] codec101 =
                StringUtils.getBytesUtf8(Base64TestData.CODEC_101_INPUT_LENGTH_IS_MULTIPLE_OF_3);
    }

    @Test
    public void testInputStreamReader_test1_decomposed() throws Exception {
        final byte[] codec101 =
                StringUtils.getBytesUtf8(Base64TestData.CODEC_101_INPUT_LENGTH_IS_MULTIPLE_OF_3);
        final ByteArrayInputStream bais = new ByteArrayInputStream(codec101);
        final BaseNCodecInputStream in = Base64InputStream.Base64InputStream0(bais);
    }

    @Test
    public void testInputStreamReader_test2_decomposed() throws Exception {
        final byte[] codec101 =
                StringUtils.getBytesUtf8(Base64TestData.CODEC_101_INPUT_LENGTH_IS_MULTIPLE_OF_3);
        final ByteArrayInputStream bais = new ByteArrayInputStream(codec101);
        final BaseNCodecInputStream in = Base64InputStream.Base64InputStream0(bais);
        final InputStreamReader isr = new InputStreamReader(in);
        try (final BufferedReader br = new BufferedReader(isr)) {
            final String line = br.readLine();
            assertNotNull("Codec101:  InputStreamReader works!", line);
        }
    }

    @Test
    public void testAvailable_test0_decomposed() throws Throwable {
        final InputStream ins =
                new ByteArrayInputStream(StringUtils.getBytesIso8859_1(ENCODED_B64));
    }

    @Test
    public void testAvailable_test1_decomposed() throws Throwable {
        final InputStream ins =
                new ByteArrayInputStream(StringUtils.getBytesIso8859_1(ENCODED_B64));
        try (final BaseNCodecInputStream b64stream = Base64InputStream.Base64InputStream0(ins)) {
            assertEquals(1, b64stream.available());
            assertEquals(6, b64stream.skip(10));
            assertEquals(0, b64stream.available());
            assertEquals(-1, b64stream.read0());
            assertEquals(-1, b64stream.read0());
            assertEquals(0, b64stream.available());
        }
    }

    @Test
    public void testBase64EmptyInputStreamMimeChuckSize_test0_decomposed() throws Exception {
        testBase64EmptyInputStream(BaseNCodec.MIME_CHUNK_SIZE);
    }

    @Test
    public void testBase64EmptyInputStreamPemChuckSize_test0_decomposed() throws Exception {
        testBase64EmptyInputStream(BaseNCodec.PEM_CHUNK_SIZE);
    }

    @Test
    public void testMarkSupported_test0_decomposed() throws Exception {
        final byte[] decoded = StringUtils.getBytesUtf8(STRING_FIXTURE);
    }

    @Test
    public void testMarkSupported_test1_decomposed() throws Exception {
        final byte[] decoded = StringUtils.getBytesUtf8(STRING_FIXTURE);
        final ByteArrayInputStream bin = new ByteArrayInputStream(decoded);
        try (final BaseNCodecInputStream in =
                Base64InputStream.Base64InputStream2(bin, true, 4, new byte[] {0, 0, 0})) {
            assertFalse("Base64InputStream.markSupported() is false", in.markSupported());
        }
    }

    @Test
    public void testRead0_test0_decomposed() throws Exception {
        final byte[] decoded = StringUtils.getBytesUtf8(STRING_FIXTURE);
    }

    @Test
    public void testRead0_test1_decomposed() throws Exception {
        final byte[] decoded = StringUtils.getBytesUtf8(STRING_FIXTURE);
        final byte[] buf = new byte[1024];
        int bytesRead = 0;
        final ByteArrayInputStream bin = new ByteArrayInputStream(decoded);
        try (final BaseNCodecInputStream in =
                Base64InputStream.Base64InputStream2(bin, true, 4, new byte[] {0, 0, 0})) {
            bytesRead = in.read1(buf, 0, 0);
            assertEquals("Base64InputStream.read(buf, 0, 0) returns 0", 0, bytesRead);
        }
    }

    @Test
    public void testReadNull_test0_decomposed() throws Exception {
        final byte[] decoded = StringUtils.getBytesUtf8(STRING_FIXTURE);
    }

    @Test
    public void testReadNull_test1_decomposed() throws Exception {
        final byte[] decoded = StringUtils.getBytesUtf8(STRING_FIXTURE);
        final ByteArrayInputStream bin = new ByteArrayInputStream(decoded);
        try (final BaseNCodecInputStream in =
                Base64InputStream.Base64InputStream2(bin, true, 4, new byte[] {0, 0, 0})) {
            in.read1(null, 0, 0);
            fail("Base64InputStream.read(null, 0, 0) to throw a NullPointerException");
        } catch (final NullPointerException e) {
        }
    }

    @Test
    public void testReadOutOfBounds_test0_decomposed() throws Exception {
        final byte[] decoded = StringUtils.getBytesUtf8(STRING_FIXTURE);
    }

    @Test
    public void testReadOutOfBounds_test1_decomposed() throws Exception {
        final byte[] decoded = StringUtils.getBytesUtf8(STRING_FIXTURE);
        final byte[] buf = new byte[1024];
        final ByteArrayInputStream bin = new ByteArrayInputStream(decoded);
        try (final BaseNCodecInputStream in =
                Base64InputStream.Base64InputStream2(bin, true, 4, new byte[] {0, 0, 0})) {

            try {
                in.read1(buf, -1, 0);
                fail(
                        "Expected Base64InputStream.read(buf, -1, 0) to throw"
                                + " IndexOutOfBoundsException");
            } catch (final IndexOutOfBoundsException e) {
            }

            try {
                in.read1(buf, 0, -1);
                fail(
                        "Expected Base64InputStream.read(buf, 0, -1) to throw"
                                + " IndexOutOfBoundsException");
            } catch (final IndexOutOfBoundsException e) {
            }

            try {
                in.read1(buf, buf.length + 1, 0);
                fail(
                        "Base64InputStream.read(buf, buf.length + 1, 0) throws"
                                + " IndexOutOfBoundsException");
            } catch (final IndexOutOfBoundsException e) {
            }

            try {
                in.read1(buf, buf.length - 1, 2);
                fail(
                        "Base64InputStream.read(buf, buf.length - 1, 2) throws"
                                + " IndexOutOfBoundsException");
            } catch (final IndexOutOfBoundsException e) {
            }
        }
    }

    @Test
    public void testSkipBig_test0_decomposed() throws Throwable {
        final InputStream ins =
                new ByteArrayInputStream(StringUtils.getBytesIso8859_1(ENCODED_B64));
    }

    @Test
    public void testSkipBig_test1_decomposed() throws Throwable {
        final InputStream ins =
                new ByteArrayInputStream(StringUtils.getBytesIso8859_1(ENCODED_B64));
        try (final BaseNCodecInputStream b64stream = Base64InputStream.Base64InputStream0(ins)) {
            assertEquals(6, b64stream.skip(Integer.MAX_VALUE));
            assertEquals(-1, b64stream.read0());
            assertEquals(-1, b64stream.read0());
        }
    }

    @Test
    public void testSkipNone_test0_decomposed() throws Throwable {
        final InputStream ins =
                new ByteArrayInputStream(StringUtils.getBytesIso8859_1(ENCODED_B64));
    }

    @Test
    public void testSkipNone_test1_decomposed() throws Throwable {
        final InputStream ins =
                new ByteArrayInputStream(StringUtils.getBytesIso8859_1(ENCODED_B64));
        try (final BaseNCodecInputStream b64stream = Base64InputStream.Base64InputStream0(ins)) {
            final byte[] actualBytes = new byte[6];
            assertEquals(0, b64stream.skip(0));
            b64stream.read1(actualBytes, 0, actualBytes.length);
            assertArrayEquals(
                    actualBytes, new byte[] {0, 0, 0, (byte) 255, (byte) 255, (byte) 255});
            assertEquals(-1, b64stream.read0());
        }
    }

    @Test
    public void testSkipPastEnd_test0_decomposed() throws Throwable {
        final InputStream ins =
                new ByteArrayInputStream(StringUtils.getBytesIso8859_1(ENCODED_B64));
    }

    @Test
    public void testSkipPastEnd_test1_decomposed() throws Throwable {
        final InputStream ins =
                new ByteArrayInputStream(StringUtils.getBytesIso8859_1(ENCODED_B64));
        try (final BaseNCodecInputStream b64stream = Base64InputStream.Base64InputStream0(ins)) {
            assertEquals(6, b64stream.skip(10));
            assertEquals(-1, b64stream.read0());
            assertEquals(-1, b64stream.read0());
        }
    }

    @Test
    public void testSkipToEnd_test0_decomposed() throws Throwable {
        final InputStream ins =
                new ByteArrayInputStream(StringUtils.getBytesIso8859_1(ENCODED_B64));
    }

    @Test
    public void testSkipToEnd_test1_decomposed() throws Throwable {
        final InputStream ins =
                new ByteArrayInputStream(StringUtils.getBytesIso8859_1(ENCODED_B64));
        try (final BaseNCodecInputStream b64stream = Base64InputStream.Base64InputStream0(ins)) {
            assertEquals(6, b64stream.skip(6));
            assertEquals(-1, b64stream.read0());
            assertEquals(-1, b64stream.read0());
        }
    }

    @Test
    public void testSkipWrongArgument_test0_decomposed() throws Throwable {
        final InputStream ins =
                new ByteArrayInputStream(StringUtils.getBytesIso8859_1(ENCODED_B64));
    }

    @Test(expected = IllegalArgumentException.class)
    public void testSkipWrongArgument_test1_decomposed() throws Throwable {
        final InputStream ins =
                new ByteArrayInputStream(StringUtils.getBytesIso8859_1(ENCODED_B64));
        try (final BaseNCodecInputStream b64stream = Base64InputStream.Base64InputStream0(ins)) {
            b64stream.skip(-10);
        }
    }
}