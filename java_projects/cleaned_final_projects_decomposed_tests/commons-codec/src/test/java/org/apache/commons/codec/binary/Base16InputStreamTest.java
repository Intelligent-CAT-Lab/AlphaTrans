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

/**
 * @since 1.15
 */
public class Base16InputStreamTest {

    /** Decodes to {202, 254, 186, 190, 255, 255} */
    private static final String ENCODED_B16 = "CAFEBABEFFFF";

    private static final String STRING_FIXTURE = "Hello World";

    /**
     * Tests skipping past the end of a stream.
     *
     * @throws IOException for some failure scenarios.
     */
    

    /**
     * Tests the Base16InputStream implementation against empty input.
     *
     * @throws IOException for some failure scenarios.
     */
    

    /**
     * Tests the Base16InputStream implementation.
     *
     * @throws IOException for some failure scenarios.
     */

    /**
     * Tests the Base16InputStream implementation.
     *
     * @throws IOException for some failure scenarios.
     */

    /**
     * Tests method does three tests on the supplied data: 1. encoded ---[DECODE]--> decoded 2.
     * decoded ---[ENCODE]--> encoded 3. decoded ---[WRAP-WRAP-WRAP-etc...] --> decoded
     *
     * <p>By "[WRAP-WRAP-WRAP-etc...]" we mean situation where the Base16InputStream wraps itself in
     * encode and decode mode over and over again.
     *
     * @param encoded Base16 encoded data
     * @param decoded the data from above, but decoded
     * @throws IOException Usually signifies a bug in the Base16 commons-codec implementation.
     */
    private void testByChunk0(final byte[] encoded, final byte[] decoded) throws IOException {
        testByChunk1(encoded, decoded, false);
    }

    /**
     * Tests method does three tests on the supplied data: 1. encoded ---[DECODE]--> decoded 2.
     * decoded ---[ENCODE]--> encoded 3. decoded ---[WRAP-WRAP-WRAP-etc...] --> decoded
     *
     * <p>By "[WRAP-WRAP-WRAP-etc...]" we mean situation where the Base16InputStream wraps itself in
     * encode and decode mode over and over again.
     *
     * @param encoded Base16 encoded data
     * @param decoded the data from above, but decoded
     * @param lowerCase if {@code true} then use a lower-case Base16 alphabet
     * @throws IOException Usually signifies a bug in the Base16 commons-codec implementation.
     */
    private void testByChunk1(final byte[] encoded, final byte[] decoded, final boolean lowerCase)
            throws IOException {

        try (final InputStream in =
                Base16InputStream.Base16InputStream1(
                        new ByteArrayInputStream(decoded), true, lowerCase)) {
            final byte[] output = BaseNTestData.streamToBytes0(in);

            assertEquals("EOF", -1, in.read());
            assertEquals("Still EOF", -1, in.read());
            assertArrayEquals("Streaming Base16 encode", encoded, output);
        }

        try (final InputStream in =
                Base16InputStream.Base16InputStream1(
                        new ByteArrayInputStream(encoded), false, lowerCase)) {
            final byte[] output = BaseNTestData.streamToBytes0(in);

            assertEquals("EOF", -1, in.read());
            assertEquals("Still EOF", -1, in.read());
            assertArrayEquals("Streaming Base16 decode", decoded, output);
        }

        try (final InputStream in = new ByteArrayInputStream(decoded);
                final InputStream inEncode =
                        Base16InputStream.Base16InputStream1(in, true, lowerCase);
                final InputStream inDecode =
                        Base16InputStream.Base16InputStream1(inEncode, false, lowerCase)) {

            final byte[] output = BaseNTestData.streamToBytes0(inDecode);

            assertEquals("EOF", -1, inDecode.read());
            assertEquals("Still EOF", -1, inDecode.read());
            assertArrayEquals("Streaming Base16 wrap-wrap!", decoded, output);
        }
    }

    /**
     * Tests method does three tests on the supplied data: 1. encoded ---[DECODE]--> decoded 2.
     * decoded ---[ENCODE]--> encoded 3. decoded ---[WRAP-WRAP-WRAP-etc...] --> decoded
     *
     * <p>By "[WRAP-WRAP-WRAP-etc...]" we mean situation where the Base16InputStream wraps itself in
     * encode and decode mode over and over again.
     *
     * @param encoded Base16 encoded data
     * @param decoded the data from above, but decoded
     * @throws IOException Usually signifies a bug in the Base16 commons-codec implementation.
     */
    private void testByteByByte0(final byte[] encoded, final byte[] decoded) throws IOException {
        testByteByByte1(encoded, decoded, false);
    }

    /**
     * Tests method does three tests on the supplied data: 1. encoded ---[DECODE]--> decoded 2.
     * decoded ---[ENCODE]--> encoded 3. decoded ---[WRAP-WRAP-WRAP-etc...] --> decoded
     *
     * <p>By "[WRAP-WRAP-WRAP-etc...]" we mean situation where the Base16InputStream wraps itself in
     * encode and decode mode over and over again.
     *
     * @param encoded Base16 encoded data
     * @param decoded the data from above, but decoded
     * @param lowerCase if {@code true} then use a lower-case Base16 alphabet
     * @throws IOException Usually signifies a bug in the Base16 commons-codec implementation.
     */
    private void testByteByByte1(
            final byte[] encoded, final byte[] decoded, final boolean lowerCase)
            throws IOException {

        try (final InputStream in =
                Base16InputStream.Base16InputStream1(
                        new ByteArrayInputStream(decoded), true, lowerCase)) {
            final byte[] output = new byte[encoded.length];
            for (int i = 0; i < output.length; i++) {
                output[i] = (byte) in.read();
            }

            assertEquals("EOF", -1, in.read());
            assertEquals("Still EOF", -1, in.read());
            assertArrayEquals("Streaming Base16 encode", encoded, output);
        }

        try (final InputStream in =
                Base16InputStream.Base16InputStream1(
                        new ByteArrayInputStream(encoded), false, lowerCase)) {
            final byte[] output = new byte[decoded.length];
            for (int i = 0; i < output.length; i++) {
                output[i] = (byte) in.read();
            }

            assertEquals("EOF", -1, in.read());
            assertEquals("Still EOF", -1, in.read());
            assertArrayEquals("Streaming Base16 decode", decoded, output);
        }

        try (final InputStream in = new ByteArrayInputStream(decoded);
                final InputStream inEncode =
                        Base16InputStream.Base16InputStream1(in, true, lowerCase);
                final InputStream inDecode =
                        Base16InputStream.Base16InputStream1(inEncode, false, lowerCase)) {

            final byte[] output = new byte[decoded.length];
            for (int i = 0; i < output.length; i++) {
                output[i] = (byte) inDecode.read();
            }

            assertEquals("EOF", -1, inDecode.read());
            assertEquals("Still EOF", -1, inDecode.read());
            assertArrayEquals("Streaming Base16 wrap-wrap!", decoded, output);
        }
    }

    /**
     * Tests markSupported.
     *
     * @throws IOException for some failure scenarios.
     */
    

    /**
     * Tests read returning 0
     *
     * @throws IOException for some failure scenarios.
     */
    

    /**
     * Tests read with null.
     *
     * @throws IOException for some failure scenarios.
     */
    

    /**
     * Tests read throwing IndexOutOfBoundsException
     *
     * @throws IOException for some failure scenarios.
     */
    

    /**
     * Tests skipping number of characters larger than the internal buffer.
     *
     * @throws IOException for some failure scenarios.
     */
    

    /**
     * Tests skipping as a noop
     *
     * @throws IOException for some failure scenarios.
     */
    

    /**
     * Tests skipping past the end of a stream.
     *
     * @throws IOException for some failure scenarios.
     */
    

    /**
     * Tests skipping to the end of a stream.
     *
     * @throws IOException for some failure scenarios.
     */
    

    /**
     * Tests if negative arguments to skip are handled correctly.
     *
     * @throws IOException for some failure scenarios.
     */

    @Test
    public void testAvailable_test0_decomposed() throws IOException {
        final InputStream ins =
                new ByteArrayInputStream(StringUtils.getBytesIso8859_1(ENCODED_B16));
    }

    @Test
    public void testAvailable_test1_decomposed() throws IOException {
        final InputStream ins =
                new ByteArrayInputStream(StringUtils.getBytesIso8859_1(ENCODED_B16));
        try (final Base16InputStream b16Stream = Base16InputStream.Base16InputStream3(ins)) {
            assertEquals(1, b16Stream.available());
            assertEquals(6, b16Stream.skip(10));
            assertEquals(0, b16Stream.available());
            assertEquals(-1, b16Stream.read0());
            assertEquals(-1, b16Stream.read0());
            assertEquals(0, b16Stream.available());
        }
    }

    @Test
    public void testBase16EmptyInputStream_test0_decomposed() throws IOException {
        final byte[] emptyEncoded = {};
        final byte[] emptyDecoded = {};
        testByteByByte0(emptyEncoded, emptyDecoded);
    }

    @Test
    public void testBase16EmptyInputStream_test1_decomposed() throws IOException {
        final byte[] emptyEncoded = {};
        final byte[] emptyDecoded = {};
        testByteByByte0(emptyEncoded, emptyDecoded);
        testByChunk0(emptyEncoded, emptyDecoded);
    }

    @Test
    public void testMarkSupported_test0_decomposed() throws IOException {
        final byte[] decoded = StringUtils.getBytesUtf8(STRING_FIXTURE);
    }

    @Test
    public void testMarkSupported_test1_decomposed() throws IOException {
        final byte[] decoded = StringUtils.getBytesUtf8(STRING_FIXTURE);
        final ByteArrayInputStream bin = new ByteArrayInputStream(decoded);
        try (final Base16InputStream in = Base16InputStream.Base16InputStream2(bin, true)) {
            assertFalse("Base16InputStream.markSupported() is false", in.markSupported());
        }
    }

    @Test
    public void testRead0_test0_decomposed() throws IOException {
        final byte[] decoded = StringUtils.getBytesUtf8(STRING_FIXTURE);
    }

    @Test
    public void testRead0_test1_decomposed() throws IOException {
        final byte[] decoded = StringUtils.getBytesUtf8(STRING_FIXTURE);
        final byte[] buf = new byte[1024];
        int bytesRead = 0;
        final ByteArrayInputStream bin = new ByteArrayInputStream(decoded);
        try (final Base16InputStream in = Base16InputStream.Base16InputStream2(bin, true)) {
            bytesRead = in.read1(buf, 0, 0);
            assertEquals("Base16InputStream.read(buf, 0, 0) returns 0", 0, bytesRead);
        }
    }

    @Test
    public void testReadNull_test0_decomposed() throws IOException {
        final byte[] decoded = StringUtils.getBytesUtf8(STRING_FIXTURE);
    }

    @Test
    public void testReadNull_test1_decomposed() throws IOException {
        final byte[] decoded = StringUtils.getBytesUtf8(STRING_FIXTURE);
        final ByteArrayInputStream bin = new ByteArrayInputStream(decoded);
        try (final Base16InputStream in = Base16InputStream.Base16InputStream2(bin, true)) {
            in.read1(null, 0, 0);
            fail("Base16InputStream.read(null, 0, 0) to throw a NullPointerException");
        } catch (final NullPointerException e) {
        }
    }

    @Test
    public void testReadOutOfBounds_test0_decomposed() throws IOException {
        final byte[] decoded = StringUtils.getBytesUtf8(STRING_FIXTURE);
    }

    @Test
    public void testReadOutOfBounds_test1_decomposed() throws IOException {
        final byte[] decoded = StringUtils.getBytesUtf8(STRING_FIXTURE);
        final byte[] buf = new byte[1024];
        final ByteArrayInputStream bin = new ByteArrayInputStream(decoded);
        try (final Base16InputStream in = Base16InputStream.Base16InputStream2(bin, true)) {

            try {
                in.read1(buf, -1, 0);
                fail(
                        "Expected Base16InputStream.read(buf, -1, 0) to throw"
                                + " IndexOutOfBoundsException");
            } catch (final IndexOutOfBoundsException e) {
            }

            try {
                in.read1(buf, 0, -1);
                fail(
                        "Expected Base16InputStream.read(buf, 0, -1) to throw"
                                + " IndexOutOfBoundsException");
            } catch (final IndexOutOfBoundsException e) {
            }

            try {
                in.read1(buf, buf.length + 1, 0);
                fail(
                        "Base16InputStream.read(buf, buf.length + 1, 0) throws"
                                + " IndexOutOfBoundsException");
            } catch (final IndexOutOfBoundsException e) {
            }

            try {
                in.read1(buf, buf.length - 1, 2);
                fail(
                        "Base16InputStream.read(buf, buf.length - 1, 2) throws"
                                + " IndexOutOfBoundsException");
            } catch (final IndexOutOfBoundsException e) {
            }
        }
    }

    @Test
    public void testSkipBig_test0_decomposed() throws IOException {
        final InputStream ins =
                new ByteArrayInputStream(StringUtils.getBytesIso8859_1(ENCODED_B16));
    }

    @Test
    public void testSkipBig_test1_decomposed() throws IOException {
        final InputStream ins =
                new ByteArrayInputStream(StringUtils.getBytesIso8859_1(ENCODED_B16));
        try (final Base16InputStream b16Stream = Base16InputStream.Base16InputStream3(ins)) {
            assertEquals(6, b16Stream.skip(Integer.MAX_VALUE));
            assertEquals(-1, b16Stream.read0());
            assertEquals(-1, b16Stream.read0());
        }
    }

    @Test
    public void testSkipNone_test0_decomposed() throws IOException {
        final InputStream ins =
                new ByteArrayInputStream(StringUtils.getBytesIso8859_1(ENCODED_B16));
    }

    @Test
    public void testSkipNone_test1_decomposed() throws IOException {
        final InputStream ins =
                new ByteArrayInputStream(StringUtils.getBytesIso8859_1(ENCODED_B16));
        try (final Base16InputStream b16Stream = Base16InputStream.Base16InputStream3(ins)) {
            final byte[] actualBytes = new byte[6];
            assertEquals(0, b16Stream.skip(0));
            b16Stream.read1(actualBytes, 0, actualBytes.length);
            assertArrayEquals(
                    actualBytes,
                    new byte[] {
                        (byte) 202, (byte) 254, (byte) 186, (byte) 190, (byte) 255, (byte) 255
                    });
            assertEquals(-1, b16Stream.read0());
        }
    }

    @Test
    public void testSkipPastEnd_test0_decomposed() throws IOException {
        final InputStream ins =
                new ByteArrayInputStream(StringUtils.getBytesIso8859_1(ENCODED_B16));
    }

    @Test
    public void testSkipPastEnd_test1_decomposed() throws IOException {
        final InputStream ins =
                new ByteArrayInputStream(StringUtils.getBytesIso8859_1(ENCODED_B16));
        try (final Base16InputStream b16Stream = Base16InputStream.Base16InputStream3(ins)) {
            assertEquals(6, b16Stream.skip(10));
            assertEquals(-1, b16Stream.read0());
            assertEquals(-1, b16Stream.read0());
        }
    }

    @Test
    public void testSkipToEnd_test0_decomposed() throws IOException {
        final InputStream ins =
                new ByteArrayInputStream(StringUtils.getBytesIso8859_1(ENCODED_B16));
    }

    @Test
    public void testSkipToEnd_test1_decomposed() throws IOException {
        final InputStream ins =
                new ByteArrayInputStream(StringUtils.getBytesIso8859_1(ENCODED_B16));
        try (final Base16InputStream b16Stream = Base16InputStream.Base16InputStream3(ins)) {
            assertEquals(6, b16Stream.skip(6));
            assertEquals(-1, b16Stream.read0());
            assertEquals(-1, b16Stream.read0());
        }
    }

    @Test
    public void testSkipWrongArgument_test0_decomposed() throws IOException {
        final InputStream ins =
                new ByteArrayInputStream(StringUtils.getBytesIso8859_1(ENCODED_B16));
    }

    @Test(expected = IllegalArgumentException.class)
    public void testSkipWrongArgument_test1_decomposed() throws IOException {
        final InputStream ins =
                new ByteArrayInputStream(StringUtils.getBytesIso8859_1(ENCODED_B16));
        try (final Base16InputStream b16Stream = Base16InputStream.Base16InputStream3(ins)) {
            b16Stream.skip(-10);
        }
    }
}