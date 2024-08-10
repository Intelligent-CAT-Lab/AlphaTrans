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
import static org.junit.Assert.assertFalse;
import static org.junit.Assert.assertTrue;
import static org.junit.Assert.fail;

import org.apache.commons.codec.CodecPolicy;
import org.junit.Test;

import java.io.ByteArrayOutputStream;
import java.io.OutputStream;

public class Base32OutputStreamTest {

    private static final byte[] CR_LF = {(byte) '\r', (byte) '\n'};

    private static final byte[] LF = {(byte) '\n'};

    /**
     * Test the Base32OutputStream implementation against empty input.
     *
     * @throws Exception for some failure scenarios.
     */
    

    /**
     * Test the Base32OutputStream implementation against empty input.
     *
     * @throws Exception for some failure scenarios.
     */
    

    private void testBase32EmptyOutputStream(final int chunkSize) throws Exception {
        final byte[] emptyEncoded = {};
        final byte[] emptyDecoded = {};
        testByteByByte(emptyEncoded, emptyDecoded, chunkSize, CR_LF);
        testByChunk(emptyEncoded, emptyDecoded, chunkSize, CR_LF);
    }

    /**
     * Test the Base32OutputStream implementation
     *
     * @throws Exception for some failure scenarios.
     */
    

    /**
     * Test the Base32OutputStream implementation
     *
     * @throws Exception for some failure scenarios.
     */
    

    /**
     * Test method does three tests on the supplied data: 1. encoded ---[DECODE]--> decoded 2.
     * decoded ---[ENCODE]--> encoded 3. decoded ---[WRAP-WRAP-WRAP-etc...] --> decoded
     *
     * <p>By "[WRAP-WRAP-WRAP-etc...]" we mean situation where the Base32OutputStream wraps itself
     * in encode and decode mode over and over again.
     *
     * @param encoded Base32 encoded data
     * @param decoded the data from above, but decoded
     * @param chunkSize chunk size (line-length) of the Base32 encoded data.
     * @param separator Line separator in the Base32 encoded data.
     * @throws Exception Usually signifies a bug in the Base32 commons-codec implementation.
     */
    private void testByChunk(
            final byte[] encoded, final byte[] decoded, final int chunkSize, final byte[] separator)
            throws Exception {

        ByteArrayOutputStream byteOut = new ByteArrayOutputStream();
        OutputStream out =
                Base32OutputStream.Base32OutputStream2(byteOut, true, chunkSize, separator);
        out.write(decoded);
        out.close();
        byte[] output = byteOut.toByteArray();
        assertArrayEquals("Streaming chunked Base32 encode", encoded, output);

        byteOut = new ByteArrayOutputStream();
        out = Base32OutputStream.Base32OutputStream1(byteOut, false);
        out.write(encoded);
        out.close();
        output = byteOut.toByteArray();
        assertArrayEquals("Streaming chunked Base32 decode", decoded, output);

        byteOut = new ByteArrayOutputStream();
        out = byteOut;
        for (int i = 0; i < 10; i++) {
            out = Base32OutputStream.Base32OutputStream1(out, false);
            out = Base32OutputStream.Base32OutputStream2(out, true, chunkSize, separator);
        }
        out.write(decoded);
        out.close();
        output = byteOut.toByteArray();

        assertArrayEquals("Streaming chunked Base32 wrap-wrap-wrap!", decoded, output);
    }

    /**
     * Test method does three tests on the supplied data: 1. encoded ---[DECODE]--> decoded 2.
     * decoded ---[ENCODE]--> encoded 3. decoded ---[WRAP-WRAP-WRAP-etc...] --> decoded
     *
     * <p>By "[WRAP-WRAP-WRAP-etc...]" we mean situation where the Base32OutputStream wraps itself
     * in encode and decode mode over and over again.
     *
     * @param encoded Base32 encoded data
     * @param decoded the data from above, but decoded
     * @param chunkSize chunk size (line-length) of the Base32 encoded data.
     * @param separator Line separator in the Base32 encoded data.
     * @throws Exception Usually signifies a bug in the Base32 commons-codec implementation.
     */
    private void testByteByByte(
            final byte[] encoded, final byte[] decoded, final int chunkSize, final byte[] separator)
            throws Exception {

        ByteArrayOutputStream byteOut = new ByteArrayOutputStream();
        OutputStream out =
                Base32OutputStream.Base32OutputStream2(byteOut, true, chunkSize, separator);
        for (final byte element : decoded) {
            out.write(element);
        }
        out.close();
        byte[] output = byteOut.toByteArray();
        assertArrayEquals("Streaming byte-by-byte Base32 encode", encoded, output);

        byteOut = new ByteArrayOutputStream();
        out = Base32OutputStream.Base32OutputStream1(byteOut, false);
        for (final byte element : encoded) {
            out.write(element);
        }
        out.close();
        output = byteOut.toByteArray();
        assertArrayEquals("Streaming byte-by-byte Base32 decode", decoded, output);

        byteOut = new ByteArrayOutputStream();
        out = Base32OutputStream.Base32OutputStream1(byteOut, false);
        for (final byte element : encoded) {
            out.write(element);
            out.flush();
        }
        out.close();
        output = byteOut.toByteArray();
        assertArrayEquals("Streaming byte-by-byte flush() Base32 decode", decoded, output);

        byteOut = new ByteArrayOutputStream();
        out = byteOut;
        for (int i = 0; i < 10; i++) {
            out = Base32OutputStream.Base32OutputStream1(out, false);
            out = Base32OutputStream.Base32OutputStream2(out, true, chunkSize, separator);
        }
        for (final byte element : decoded) {
            out.write(element);
        }
        out.close();
        output = byteOut.toByteArray();

        assertArrayEquals("Streaming byte-by-byte Base32 wrap-wrap-wrap!", decoded, output);
    }

    /**
     * Tests Base32OutputStream.write for expected IndexOutOfBoundsException conditions.
     *
     * @throws Exception for some failure scenarios.
     */
    

    /**
     * Tests Base32OutputStream.write(null).
     *
     * @throws Exception for some failure scenarios.
     */
    

    /**
     * Test strict decoding.
     *
     * @throws Exception for some failure scenarios.
     */

    @Test
    public void testBase32EmptyOutputStreamMimeChunkSize_test0_decomposed() throws Exception {
        testBase32EmptyOutputStream(BaseNCodec.MIME_CHUNK_SIZE);
    }

    @Test
    public void testBase32EmptyOutputStreamPemChunkSize_test0_decomposed() throws Exception {
        testBase32EmptyOutputStream(BaseNCodec.PEM_CHUNK_SIZE);
    }

    @Test
    public void testBase32OutputStreamByChunk_test0_decomposed() throws Exception {
        byte[] encoded = StringUtils.getBytesUtf8(Base32TestData.BASE32_FIXTURE);
        byte[] decoded = StringUtils.getBytesUtf8(Base32TestData.STRING_FIXTURE);
    }

    @Test
    public void testBase32OutputStreamByChunk_test1_decomposed() throws Exception {
        byte[] encoded = StringUtils.getBytesUtf8(Base32TestData.BASE32_FIXTURE);
        byte[] decoded = StringUtils.getBytesUtf8(Base32TestData.STRING_FIXTURE);
        testByChunk(encoded, decoded, BaseNCodec.MIME_CHUNK_SIZE, CR_LF);
    }

    @Test
    public void testBase32OutputStreamByChunk_test2_decomposed() throws Exception {
        byte[] encoded = StringUtils.getBytesUtf8(Base32TestData.BASE32_FIXTURE);
        byte[] decoded = StringUtils.getBytesUtf8(Base32TestData.STRING_FIXTURE);
        testByChunk(encoded, decoded, BaseNCodec.MIME_CHUNK_SIZE, CR_LF);
        final BaseNCodec codec = Base32.Base320();
    }

    @Test
    public void testBase32OutputStreamByChunk_test3_decomposed() throws Exception {
        byte[] encoded = StringUtils.getBytesUtf8(Base32TestData.BASE32_FIXTURE);
        byte[] decoded = StringUtils.getBytesUtf8(Base32TestData.STRING_FIXTURE);
        testByChunk(encoded, decoded, BaseNCodec.MIME_CHUNK_SIZE, CR_LF);
        final BaseNCodec codec = Base32.Base320();
        for (int i = 0; i <= 150; i++) {
            final byte[][] randomData = BaseNTestData.randomData(codec, i);
            encoded = randomData[1];
            decoded = randomData[0];
            testByChunk(encoded, decoded, 0, LF);
        }
    }

    @Test
    public void testBase32OutputStreamByteByByte_test0_decomposed() throws Exception {
        byte[] encoded = StringUtils.getBytesUtf8(Base32TestData.BASE32_FIXTURE);
        byte[] decoded = StringUtils.getBytesUtf8(Base32TestData.STRING_FIXTURE);
    }

    @Test
    public void testBase32OutputStreamByteByByte_test1_decomposed() throws Exception {
        byte[] encoded = StringUtils.getBytesUtf8(Base32TestData.BASE32_FIXTURE);
        byte[] decoded = StringUtils.getBytesUtf8(Base32TestData.STRING_FIXTURE);
        testByteByByte(encoded, decoded, 76, CR_LF);
    }

    @Test
    public void testBase32OutputStreamByteByByte_test2_decomposed() throws Exception {
        byte[] encoded = StringUtils.getBytesUtf8(Base32TestData.BASE32_FIXTURE);
        byte[] decoded = StringUtils.getBytesUtf8(Base32TestData.STRING_FIXTURE);
        testByteByByte(encoded, decoded, 76, CR_LF);
        final BaseNCodec codec = Base32.Base320();
    }

    @Test
    public void testBase32OutputStreamByteByByte_test3_decomposed() throws Exception {
        byte[] encoded = StringUtils.getBytesUtf8(Base32TestData.BASE32_FIXTURE);
        byte[] decoded = StringUtils.getBytesUtf8(Base32TestData.STRING_FIXTURE);
        testByteByByte(encoded, decoded, 76, CR_LF);
        final BaseNCodec codec = Base32.Base320();
        for (int i = 0; i <= 150; i++) {
            final byte[][] randomData = BaseNTestData.randomData(codec, i);
            encoded = randomData[1];
            decoded = randomData[0];
            testByteByByte(encoded, decoded, 0, LF);
        }
    }

    @Test
    public void testWriteOutOfBounds_test0_decomposed() throws Exception {
        final byte[] buf = new byte[1024];
        final ByteArrayOutputStream bout = new ByteArrayOutputStream();
        try (final BaseNCodecOutputStream out = Base32OutputStream.Base32OutputStream0(bout)) {

            try {
                out.write0(buf, -1, 1);
                fail(
                        "Expected Base32OutputStream.write(buf, -1, 1) to throw a"
                                + " IndexOutOfBoundsException");
            } catch (final IndexOutOfBoundsException ioobe) {
            }

            try {
                out.write0(buf, 1, -1);
                fail(
                        "Expected Base32OutputStream.write(buf, 1, -1) to throw a"
                                + " IndexOutOfBoundsException");
            } catch (final IndexOutOfBoundsException ioobe) {
            }

            try {
                out.write0(buf, buf.length + 1, 0);
                fail(
                        "Expected Base32OutputStream.write(buf, buf.length + 1, 0) to throw a"
                                + " IndexOutOfBoundsException");
            } catch (final IndexOutOfBoundsException ioobe) {
            }

            try {
                out.write0(buf, buf.length - 1, 2);
                fail(
                        "Expected Base32OutputStream.write(buf, buf.length - 1, 2) to throw a"
                                + " IndexOutOfBoundsException");
            } catch (final IndexOutOfBoundsException ioobe) {
            }
        }
    }

    @Test
    public void testWriteToNullCoverage_test0_decomposed() throws Exception {
        final ByteArrayOutputStream bout = new ByteArrayOutputStream();
        try (final BaseNCodecOutputStream out = Base32OutputStream.Base32OutputStream0(bout)) {
            out.write0(null, 0, 0);
            fail("Expcted Base32OutputStream.write(null) to throw a NullPointerException");
        } catch (final NullPointerException e) {
        }
    }

    @Test
    public void testStrictDecoding_test0_decomposed() throws Exception {
        for (final String s : Base32Test.BASE32_IMPOSSIBLE_CASES) {
            final byte[] encoded = StringUtils.getBytesUtf8(s);
            ByteArrayOutputStream bout = new ByteArrayOutputStream();
            BaseNCodecOutputStream out = Base32OutputStream.Base32OutputStream1(bout, false);
            assertFalse(out.isStrictDecoding());
            out.write(encoded);
            out.close();
            assertTrue(bout.size() > 0);

            bout = new ByteArrayOutputStream();
            out = new Base32OutputStream(bout, false, 0, null, CodecPolicy.STRICT);
            assertTrue(out.isStrictDecoding());
            try {
                out.write(encoded);
                out.close();
                fail();
            } catch (final IllegalArgumentException ex) {
            }
        }
    }
}