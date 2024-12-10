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
import static org.junit.Assert.assertTrue;
import static org.junit.Assert.fail;

import org.apache.commons.codec.CodecPolicy;
import org.junit.Test;

import java.io.ByteArrayOutputStream;
import java.io.OutputStream;

/**
 * @since 1.4
 */
public class Base64OutputStreamTest {

    private static final byte[] CR_LF = {(byte) '\r', (byte) '\n'};

    private static final byte[] LF = {(byte) '\n'};

    private static final String STRING_FIXTURE = "Hello World";

    /**
     * Test the Base64OutputStream implementation against the special NPE inducing input identified
     * in the CODEC-98 bug.
     *
     * @throws Exception for some failure scenarios.
     */
    

    /**
     * Test the Base64OutputStream implementation against empty input.
     *
     * @throws Exception for some failure scenarios.
     */
    

    /**
     * Test the Base64OutputStream implementation against empty input.
     *
     * @throws Exception for some failure scenarios.
     */
    

    private void testBase64EmptyOutputStream(final int chunkSize) throws Exception {
        final byte[] emptyEncoded = {};
        final byte[] emptyDecoded = {};
        testByteByByte(emptyEncoded, emptyDecoded, chunkSize, CR_LF);
        testByChunk(emptyEncoded, emptyDecoded, chunkSize, CR_LF);
    }

    /**
     * Test the Base64OutputStream implementation
     *
     * @throws Exception for some failure scenarios.
     */
    

    /**
     * Test the Base64OutputStream implementation
     *
     * @throws Exception for some failure scenarios.
     */
    

    /**
     * Test method does three tests on the supplied data: 1. encoded ---[DECODE]--> decoded 2.
     * decoded ---[ENCODE]--> encoded 3. decoded ---[WRAP-WRAP-WRAP-etc...] --> decoded
     *
     * <p>By "[WRAP-WRAP-WRAP-etc...]" we mean situation where the Base64OutputStream wraps itself
     * in encode and decode mode over and over again.
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

        ByteArrayOutputStream byteOut = new ByteArrayOutputStream();
        OutputStream out =
                Base64OutputStream.Base64OutputStream2(byteOut, true, chunkSize, separator);
        out.write(decoded);
        out.close();
        byte[] output = byteOut.toByteArray();
        assertArrayEquals("Streaming chunked base64 encode", encoded, output);

        byteOut = new ByteArrayOutputStream();
        out = Base64OutputStream.Base64OutputStream1(byteOut, false);
        out.write(encoded);
        out.close();
        output = byteOut.toByteArray();
        assertArrayEquals("Streaming chunked base64 decode", decoded, output);

        byteOut = new ByteArrayOutputStream();
        out = byteOut;
        for (int i = 0; i < 10; i++) {
            out = Base64OutputStream.Base64OutputStream1(out, false);
            out = Base64OutputStream.Base64OutputStream2(out, true, chunkSize, separator);
        }
        out.write(decoded);
        out.close();
        output = byteOut.toByteArray();

        assertArrayEquals("Streaming chunked base64 wrap-wrap-wrap!", decoded, output);
    }

    /**
     * Test method does three tests on the supplied data: 1. encoded ---[DECODE]--> decoded 2.
     * decoded ---[ENCODE]--> encoded 3. decoded ---[WRAP-WRAP-WRAP-etc...] --> decoded
     *
     * <p>By "[WRAP-WRAP-WRAP-etc...]" we mean situation where the Base64OutputStream wraps itself
     * in encode and decode mode over and over again.
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

        ByteArrayOutputStream byteOut = new ByteArrayOutputStream();
        OutputStream out =
                Base64OutputStream.Base64OutputStream2(byteOut, true, chunkSize, separator);
        for (final byte element : decoded) {
            out.write(element);
        }
        out.close();
        byte[] output = byteOut.toByteArray();
        assertArrayEquals("Streaming byte-by-byte base64 encode", encoded, output);

        byteOut = new ByteArrayOutputStream();
        out = Base64OutputStream.Base64OutputStream1(byteOut, false);
        for (final byte element : encoded) {
            out.write(element);
        }
        out.close();
        output = byteOut.toByteArray();
        assertArrayEquals("Streaming byte-by-byte base64 decode", decoded, output);

        byteOut = new ByteArrayOutputStream();
        out = Base64OutputStream.Base64OutputStream1(byteOut, false);
        for (final byte element : encoded) {
            out.write(element);
            out.flush();
        }
        out.close();
        output = byteOut.toByteArray();
        assertArrayEquals("Streaming byte-by-byte flush() base64 decode", decoded, output);

        byteOut = new ByteArrayOutputStream();
        out = byteOut;
        for (int i = 0; i < 10; i++) {
            out = Base64OutputStream.Base64OutputStream1(out, false);
            out = Base64OutputStream.Base64OutputStream2(out, true, chunkSize, separator);
        }
        for (final byte element : decoded) {
            out.write(element);
        }
        out.close();
        output = byteOut.toByteArray();

        assertArrayEquals("Streaming byte-by-byte base64 wrap-wrap-wrap!", decoded, output);
    }

    /**
     * Tests Base64OutputStream.write for expected IndexOutOfBoundsException conditions.
     *
     * @throws Exception for some failure scenarios.
     */
    

    /**
     * Tests Base64OutputStream.write(null).
     *
     * @throws Exception for some failure scenarios.
     */
    

    /**
     * Test strict decoding.
     *
     * @throws Exception for some failure scenarios.
     */

    @Test
    public void testCodec98NPE_test0_decomposed() throws Exception {
        final byte[] codec98 = StringUtils.getBytesUtf8(Base64TestData.CODEC_98_NPE);
    }

    @Test
    public void testCodec98NPE_test1_decomposed() throws Exception {
        final byte[] codec98 = StringUtils.getBytesUtf8(Base64TestData.CODEC_98_NPE);
        final byte[] codec98_1024 = new byte[1024];
        System.arraycopy(codec98, 0, codec98_1024, 0, codec98.length);
        final ByteArrayOutputStream data = new ByteArrayOutputStream(1024);
        try (final BaseNCodecOutputStream stream =
                Base64OutputStream.Base64OutputStream1(data, false)) {
            stream.write0(codec98_1024, 0, 1024);
        }
    }

    @Test
    public void testCodec98NPE_test2_decomposed() throws Exception {
        final byte[] codec98 = StringUtils.getBytesUtf8(Base64TestData.CODEC_98_NPE);
        final byte[] codec98_1024 = new byte[1024];
        System.arraycopy(codec98, 0, codec98_1024, 0, codec98.length);
        final ByteArrayOutputStream data = new ByteArrayOutputStream(1024);
        try (final BaseNCodecOutputStream stream =
                Base64OutputStream.Base64OutputStream1(data, false)) {
            stream.write0(codec98_1024, 0, 1024);
        }
        final byte[] decodedBytes = data.toByteArray();
    }

    @Test
    public void testCodec98NPE_test3_decomposed() throws Exception {
        final byte[] codec98 = StringUtils.getBytesUtf8(Base64TestData.CODEC_98_NPE);
        final byte[] codec98_1024 = new byte[1024];
        System.arraycopy(codec98, 0, codec98_1024, 0, codec98.length);
        final ByteArrayOutputStream data = new ByteArrayOutputStream(1024);
        try (final BaseNCodecOutputStream stream =
                Base64OutputStream.Base64OutputStream1(data, false)) {
            stream.write0(codec98_1024, 0, 1024);
        }
        final byte[] decodedBytes = data.toByteArray();
        final String decoded = StringUtils.newStringUtf8(decodedBytes);
    }

    @Test
    public void testCodec98NPE_test4_decomposed() throws Exception {
        final byte[] codec98 = StringUtils.getBytesUtf8(Base64TestData.CODEC_98_NPE);
        final byte[] codec98_1024 = new byte[1024];
        System.arraycopy(codec98, 0, codec98_1024, 0, codec98.length);
        final ByteArrayOutputStream data = new ByteArrayOutputStream(1024);
        try (final BaseNCodecOutputStream stream =
                Base64OutputStream.Base64OutputStream1(data, false)) {
            stream.write0(codec98_1024, 0, 1024);
        }
        final byte[] decodedBytes = data.toByteArray();
        final String decoded = StringUtils.newStringUtf8(decodedBytes);
        assertEquals(
                "codec-98 NPE Base64OutputStream", Base64TestData.CODEC_98_NPE_DECODED, decoded);
    }

    @Test
    public void testBase64EmptyOutputStreamMimeChunkSize_test0_decomposed() throws Exception {
        testBase64EmptyOutputStream(BaseNCodec.MIME_CHUNK_SIZE);
    }

    @Test
    public void testBase64EmptyOutputStreamPemChunkSize_test0_decomposed() throws Exception {
        testBase64EmptyOutputStream(BaseNCodec.PEM_CHUNK_SIZE);
    }

    @Test
    public void testBase64OutputStreamByChunk_test0_decomposed() throws Exception {
        byte[] encoded = StringUtils.getBytesUtf8("SGVsbG8gV29ybGQ=\r\n");
        byte[] decoded = StringUtils.getBytesUtf8(STRING_FIXTURE);
    }

    @Test
    public void testBase64OutputStreamByChunk_test1_decomposed() throws Exception {
        byte[] encoded = StringUtils.getBytesUtf8("SGVsbG8gV29ybGQ=\r\n");
        byte[] decoded = StringUtils.getBytesUtf8(STRING_FIXTURE);
        testByChunk(encoded, decoded, BaseNCodec.MIME_CHUNK_SIZE, CR_LF);
    }

    @Test
    public void testBase64OutputStreamByChunk_test2_decomposed() throws Exception {
        byte[] encoded = StringUtils.getBytesUtf8("SGVsbG8gV29ybGQ=\r\n");
        byte[] decoded = StringUtils.getBytesUtf8(STRING_FIXTURE);
        testByChunk(encoded, decoded, BaseNCodec.MIME_CHUNK_SIZE, CR_LF);
        encoded = StringUtils.getBytesUtf8("AA==\r\n");
    }

    @Test
    public void testBase64OutputStreamByChunk_test3_decomposed() throws Exception {
        byte[] encoded = StringUtils.getBytesUtf8("SGVsbG8gV29ybGQ=\r\n");
        byte[] decoded = StringUtils.getBytesUtf8(STRING_FIXTURE);
        testByChunk(encoded, decoded, BaseNCodec.MIME_CHUNK_SIZE, CR_LF);
        encoded = StringUtils.getBytesUtf8("AA==\r\n");
        decoded = new byte[] {(byte) 0};
        testByChunk(encoded, decoded, BaseNCodec.MIME_CHUNK_SIZE, CR_LF);
    }

    @Test
    public void testBase64OutputStreamByChunk_test4_decomposed() throws Exception {
        byte[] encoded = StringUtils.getBytesUtf8("SGVsbG8gV29ybGQ=\r\n");
        byte[] decoded = StringUtils.getBytesUtf8(STRING_FIXTURE);
        testByChunk(encoded, decoded, BaseNCodec.MIME_CHUNK_SIZE, CR_LF);
        encoded = StringUtils.getBytesUtf8("AA==\r\n");
        decoded = new byte[] {(byte) 0};
        testByChunk(encoded, decoded, BaseNCodec.MIME_CHUNK_SIZE, CR_LF);
        encoded = StringUtils.getBytesUtf8(Base64TestData.ENCODED_64_CHARS_PER_LINE);
    }

    @Test
    public void testBase64OutputStreamByChunk_test5_decomposed() throws Exception {
        byte[] encoded = StringUtils.getBytesUtf8("SGVsbG8gV29ybGQ=\r\n");
        byte[] decoded = StringUtils.getBytesUtf8(STRING_FIXTURE);
        testByChunk(encoded, decoded, BaseNCodec.MIME_CHUNK_SIZE, CR_LF);
        encoded = StringUtils.getBytesUtf8("AA==\r\n");
        decoded = new byte[] {(byte) 0};
        testByChunk(encoded, decoded, BaseNCodec.MIME_CHUNK_SIZE, CR_LF);
        encoded = StringUtils.getBytesUtf8(Base64TestData.ENCODED_64_CHARS_PER_LINE);
        decoded = BaseNTestData.DECODED;
        testByChunk(encoded, decoded, BaseNCodec.PEM_CHUNK_SIZE, LF);
    }

    @Test
    public void testBase64OutputStreamByChunk_test6_decomposed() throws Exception {
        byte[] encoded = StringUtils.getBytesUtf8("SGVsbG8gV29ybGQ=\r\n");
        byte[] decoded = StringUtils.getBytesUtf8(STRING_FIXTURE);
        testByChunk(encoded, decoded, BaseNCodec.MIME_CHUNK_SIZE, CR_LF);
        encoded = StringUtils.getBytesUtf8("AA==\r\n");
        decoded = new byte[] {(byte) 0};
        testByChunk(encoded, decoded, BaseNCodec.MIME_CHUNK_SIZE, CR_LF);
        encoded = StringUtils.getBytesUtf8(Base64TestData.ENCODED_64_CHARS_PER_LINE);
        decoded = BaseNTestData.DECODED;
        testByChunk(encoded, decoded, BaseNCodec.PEM_CHUNK_SIZE, LF);
        final String singleLine = Base64TestData.ENCODED_64_CHARS_PER_LINE.replace("\n", "");
        encoded = StringUtils.getBytesUtf8(singleLine);
    }

    @Test
    public void testBase64OutputStreamByChunk_test7_decomposed() throws Exception {
        byte[] encoded = StringUtils.getBytesUtf8("SGVsbG8gV29ybGQ=\r\n");
        byte[] decoded = StringUtils.getBytesUtf8(STRING_FIXTURE);
        testByChunk(encoded, decoded, BaseNCodec.MIME_CHUNK_SIZE, CR_LF);
        encoded = StringUtils.getBytesUtf8("AA==\r\n");
        decoded = new byte[] {(byte) 0};
        testByChunk(encoded, decoded, BaseNCodec.MIME_CHUNK_SIZE, CR_LF);
        encoded = StringUtils.getBytesUtf8(Base64TestData.ENCODED_64_CHARS_PER_LINE);
        decoded = BaseNTestData.DECODED;
        testByChunk(encoded, decoded, BaseNCodec.PEM_CHUNK_SIZE, LF);
        final String singleLine = Base64TestData.ENCODED_64_CHARS_PER_LINE.replace("\n", "");
        encoded = StringUtils.getBytesUtf8(singleLine);
        decoded = BaseNTestData.DECODED;
        testByChunk(encoded, decoded, 0, LF);
    }

    @Test
    public void testBase64OutputStreamByChunk_test8_decomposed() throws Exception {
        byte[] encoded = StringUtils.getBytesUtf8("SGVsbG8gV29ybGQ=\r\n");
        byte[] decoded = StringUtils.getBytesUtf8(STRING_FIXTURE);
        testByChunk(encoded, decoded, BaseNCodec.MIME_CHUNK_SIZE, CR_LF);
        encoded = StringUtils.getBytesUtf8("AA==\r\n");
        decoded = new byte[] {(byte) 0};
        testByChunk(encoded, decoded, BaseNCodec.MIME_CHUNK_SIZE, CR_LF);
        encoded = StringUtils.getBytesUtf8(Base64TestData.ENCODED_64_CHARS_PER_LINE);
        decoded = BaseNTestData.DECODED;
        testByChunk(encoded, decoded, BaseNCodec.PEM_CHUNK_SIZE, LF);
        final String singleLine = Base64TestData.ENCODED_64_CHARS_PER_LINE.replace("\n", "");
        encoded = StringUtils.getBytesUtf8(singleLine);
        decoded = BaseNTestData.DECODED;
        testByChunk(encoded, decoded, 0, LF);
        final BaseNCodec codec = Base64.Base641(0, null, false);
    }

    @Test
    public void testBase64OutputStreamByChunk_test9_decomposed() throws Exception {
        byte[] encoded = StringUtils.getBytesUtf8("SGVsbG8gV29ybGQ=\r\n");
        byte[] decoded = StringUtils.getBytesUtf8(STRING_FIXTURE);
        testByChunk(encoded, decoded, BaseNCodec.MIME_CHUNK_SIZE, CR_LF);
        encoded = StringUtils.getBytesUtf8("AA==\r\n");
        decoded = new byte[] {(byte) 0};
        testByChunk(encoded, decoded, BaseNCodec.MIME_CHUNK_SIZE, CR_LF);
        encoded = StringUtils.getBytesUtf8(Base64TestData.ENCODED_64_CHARS_PER_LINE);
        decoded = BaseNTestData.DECODED;
        testByChunk(encoded, decoded, BaseNCodec.PEM_CHUNK_SIZE, LF);
        final String singleLine = Base64TestData.ENCODED_64_CHARS_PER_LINE.replace("\n", "");
        encoded = StringUtils.getBytesUtf8(singleLine);
        decoded = BaseNTestData.DECODED;
        testByChunk(encoded, decoded, 0, LF);
        final BaseNCodec codec = Base64.Base641(0, null, false);
        for (int i = 0; i <= 150; i++) {
            final byte[][] randomData = BaseNTestData.randomData(codec, i);
            encoded = randomData[1];
            decoded = randomData[0];
            testByChunk(encoded, decoded, 0, LF);
        }
    }

    @Test
    public void testBase64OutputStreamByteByByte_test0_decomposed() throws Exception {
        byte[] encoded = StringUtils.getBytesUtf8("SGVsbG8gV29ybGQ=\r\n");
        byte[] decoded = StringUtils.getBytesUtf8(STRING_FIXTURE);
    }

    @Test
    public void testBase64OutputStreamByteByByte_test1_decomposed() throws Exception {
        byte[] encoded = StringUtils.getBytesUtf8("SGVsbG8gV29ybGQ=\r\n");
        byte[] decoded = StringUtils.getBytesUtf8(STRING_FIXTURE);
        testByteByByte(encoded, decoded, 76, CR_LF);
    }

    @Test
    public void testBase64OutputStreamByteByByte_test2_decomposed() throws Exception {
        byte[] encoded = StringUtils.getBytesUtf8("SGVsbG8gV29ybGQ=\r\n");
        byte[] decoded = StringUtils.getBytesUtf8(STRING_FIXTURE);
        testByteByByte(encoded, decoded, 76, CR_LF);
        encoded = StringUtils.getBytesUtf8("AA==\r\n");
    }

    @Test
    public void testBase64OutputStreamByteByByte_test3_decomposed() throws Exception {
        byte[] encoded = StringUtils.getBytesUtf8("SGVsbG8gV29ybGQ=\r\n");
        byte[] decoded = StringUtils.getBytesUtf8(STRING_FIXTURE);
        testByteByByte(encoded, decoded, 76, CR_LF);
        encoded = StringUtils.getBytesUtf8("AA==\r\n");
        decoded = new byte[] {(byte) 0};
        testByteByByte(encoded, decoded, 76, CR_LF);
    }

    @Test
    public void testBase64OutputStreamByteByByte_test4_decomposed() throws Exception {
        byte[] encoded = StringUtils.getBytesUtf8("SGVsbG8gV29ybGQ=\r\n");
        byte[] decoded = StringUtils.getBytesUtf8(STRING_FIXTURE);
        testByteByByte(encoded, decoded, 76, CR_LF);
        encoded = StringUtils.getBytesUtf8("AA==\r\n");
        decoded = new byte[] {(byte) 0};
        testByteByByte(encoded, decoded, 76, CR_LF);
        encoded = StringUtils.getBytesUtf8(Base64TestData.ENCODED_64_CHARS_PER_LINE);
    }

    @Test
    public void testBase64OutputStreamByteByByte_test5_decomposed() throws Exception {
        byte[] encoded = StringUtils.getBytesUtf8("SGVsbG8gV29ybGQ=\r\n");
        byte[] decoded = StringUtils.getBytesUtf8(STRING_FIXTURE);
        testByteByByte(encoded, decoded, 76, CR_LF);
        encoded = StringUtils.getBytesUtf8("AA==\r\n");
        decoded = new byte[] {(byte) 0};
        testByteByByte(encoded, decoded, 76, CR_LF);
        encoded = StringUtils.getBytesUtf8(Base64TestData.ENCODED_64_CHARS_PER_LINE);
        decoded = BaseNTestData.DECODED;
        testByteByByte(encoded, decoded, 64, LF);
    }

    @Test
    public void testBase64OutputStreamByteByByte_test6_decomposed() throws Exception {
        byte[] encoded = StringUtils.getBytesUtf8("SGVsbG8gV29ybGQ=\r\n");
        byte[] decoded = StringUtils.getBytesUtf8(STRING_FIXTURE);
        testByteByByte(encoded, decoded, 76, CR_LF);
        encoded = StringUtils.getBytesUtf8("AA==\r\n");
        decoded = new byte[] {(byte) 0};
        testByteByByte(encoded, decoded, 76, CR_LF);
        encoded = StringUtils.getBytesUtf8(Base64TestData.ENCODED_64_CHARS_PER_LINE);
        decoded = BaseNTestData.DECODED;
        testByteByByte(encoded, decoded, 64, LF);
        final String singleLine = Base64TestData.ENCODED_64_CHARS_PER_LINE.replace("\n", "");
        encoded = StringUtils.getBytesUtf8(singleLine);
    }

    @Test
    public void testBase64OutputStreamByteByByte_test7_decomposed() throws Exception {
        byte[] encoded = StringUtils.getBytesUtf8("SGVsbG8gV29ybGQ=\r\n");
        byte[] decoded = StringUtils.getBytesUtf8(STRING_FIXTURE);
        testByteByByte(encoded, decoded, 76, CR_LF);
        encoded = StringUtils.getBytesUtf8("AA==\r\n");
        decoded = new byte[] {(byte) 0};
        testByteByByte(encoded, decoded, 76, CR_LF);
        encoded = StringUtils.getBytesUtf8(Base64TestData.ENCODED_64_CHARS_PER_LINE);
        decoded = BaseNTestData.DECODED;
        testByteByByte(encoded, decoded, 64, LF);
        final String singleLine = Base64TestData.ENCODED_64_CHARS_PER_LINE.replace("\n", "");
        encoded = StringUtils.getBytesUtf8(singleLine);
        decoded = BaseNTestData.DECODED;
        testByteByByte(encoded, decoded, 0, LF);
    }

    @Test
    public void testBase64OutputStreamByteByByte_test8_decomposed() throws Exception {
        byte[] encoded = StringUtils.getBytesUtf8("SGVsbG8gV29ybGQ=\r\n");
        byte[] decoded = StringUtils.getBytesUtf8(STRING_FIXTURE);
        testByteByByte(encoded, decoded, 76, CR_LF);
        encoded = StringUtils.getBytesUtf8("AA==\r\n");
        decoded = new byte[] {(byte) 0};
        testByteByByte(encoded, decoded, 76, CR_LF);
        encoded = StringUtils.getBytesUtf8(Base64TestData.ENCODED_64_CHARS_PER_LINE);
        decoded = BaseNTestData.DECODED;
        testByteByByte(encoded, decoded, 64, LF);
        final String singleLine = Base64TestData.ENCODED_64_CHARS_PER_LINE.replace("\n", "");
        encoded = StringUtils.getBytesUtf8(singleLine);
        decoded = BaseNTestData.DECODED;
        testByteByByte(encoded, decoded, 0, LF);
        final BaseNCodec codec = Base64.Base641(0, null, false);
    }

    @Test
    public void testBase64OutputStreamByteByByte_test9_decomposed() throws Exception {
        byte[] encoded = StringUtils.getBytesUtf8("SGVsbG8gV29ybGQ=\r\n");
        byte[] decoded = StringUtils.getBytesUtf8(STRING_FIXTURE);
        testByteByByte(encoded, decoded, 76, CR_LF);
        encoded = StringUtils.getBytesUtf8("AA==\r\n");
        decoded = new byte[] {(byte) 0};
        testByteByByte(encoded, decoded, 76, CR_LF);
        encoded = StringUtils.getBytesUtf8(Base64TestData.ENCODED_64_CHARS_PER_LINE);
        decoded = BaseNTestData.DECODED;
        testByteByByte(encoded, decoded, 64, LF);
        final String singleLine = Base64TestData.ENCODED_64_CHARS_PER_LINE.replace("\n", "");
        encoded = StringUtils.getBytesUtf8(singleLine);
        decoded = BaseNTestData.DECODED;
        testByteByByte(encoded, decoded, 0, LF);
        final BaseNCodec codec = Base64.Base641(0, null, false);
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
        try (final BaseNCodecOutputStream out = Base64OutputStream.Base64OutputStream0(bout)) {

            try {
                out.write0(buf, -1, 1);
                fail(
                        "Expected Base64OutputStream.write(buf, -1, 1) to throw a"
                                + " IndexOutOfBoundsException");
            } catch (final IndexOutOfBoundsException ioobe) {
            }

            try {
                out.write0(buf, 1, -1);
                fail(
                        "Expected Base64OutputStream.write(buf, 1, -1) to throw a"
                                + " IndexOutOfBoundsException");
            } catch (final IndexOutOfBoundsException ioobe) {
            }

            try {
                out.write0(buf, buf.length + 1, 0);
                fail(
                        "Expected Base64OutputStream.write(buf, buf.length + 1, 0) to throw a"
                                + " IndexOutOfBoundsException");
            } catch (final IndexOutOfBoundsException ioobe) {
            }

            try {
                out.write0(buf, buf.length - 1, 2);
                fail(
                        "Expected Base64OutputStream.write(buf, buf.length - 1, 2) to throw a"
                                + " IndexOutOfBoundsException");
            } catch (final IndexOutOfBoundsException ioobe) {
            }
        }
    }

    @Test
    public void testWriteToNullCoverage_test0_decomposed() throws Exception {
        final ByteArrayOutputStream bout = new ByteArrayOutputStream();
        try (final BaseNCodecOutputStream out = Base64OutputStream.Base64OutputStream0(bout)) {
            out.write0(null, 0, 0);
            fail("Expcted Base64OutputStream.write(null) to throw a NullPointerException");
        } catch (final NullPointerException e) {
        }
    }

    @Test
    public void testStrictDecoding_test0_decomposed() throws Exception {
        for (final String s : Base64Test.BASE64_IMPOSSIBLE_CASES) {
            final byte[] encoded = StringUtils.getBytesUtf8(s);
            ByteArrayOutputStream bout = new ByteArrayOutputStream();
            BaseNCodecOutputStream out = Base64OutputStream.Base64OutputStream1(bout, false);
            assertFalse(out.isStrictDecoding());
            out.write(encoded);
            out.close();
            assertTrue(bout.size() > 0);

            bout = new ByteArrayOutputStream();
            out = new Base64OutputStream(bout, false, 0, null, CodecPolicy.STRICT);
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