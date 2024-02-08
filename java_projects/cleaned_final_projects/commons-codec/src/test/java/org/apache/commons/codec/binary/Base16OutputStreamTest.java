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
import static org.junit.Assert.fail;

import org.junit.Test;

import java.io.ByteArrayOutputStream;
import java.io.IOException;
import java.io.OutputStream;

/**
 * @since 1.15
 */
public class Base16OutputStreamTest {

    private static final String STRING_FIXTURE = "Hello World";

    /**
     * Test the Base16OutputStream implementation against empty input.
     *
     * @throws IOException for some failure scenarios..
     */
    @Test
    public void testBase16EmptyOutputStream() throws IOException {
        final byte[] emptyEncoded = {};
        final byte[] emptyDecoded = {};
        testByteByByte0(emptyEncoded, emptyDecoded);
        testByChunk0(emptyEncoded, emptyDecoded);
    }

    /**
     * Test the Base16OutputStream implementation
     *
     * @throws IOException for some failure scenarios.
     */
    @Test
    public void testBase16OutputStreamByChunk() throws Exception {
        byte[] encoded = StringUtils.getBytesUtf8("48656C6C6F20576F726C64");
        byte[] decoded = StringUtils.getBytesUtf8(STRING_FIXTURE);
        testByChunk0(encoded, decoded);

        encoded = StringUtils.getBytesUtf8("41");
        decoded = new byte[] {(byte) 0x41};
        testByChunk0(encoded, decoded);

        final BaseNCodec codec = Base16.Base161(true);
        for (int i = 0; i <= 150; i++) {
            final byte[][] randomData = BaseNTestData.randomData(codec, i);
            encoded = randomData[1];
            decoded = randomData[0];
            testByChunk1(encoded, decoded, true);
        }
    }

    /**
     * Test the Base16OutputStream implementation
     *
     * @throws IOException for some failure scenarios.
     */
    @Test
    public void testBase16OutputStreamByteByByte() throws IOException {
        byte[] encoded = StringUtils.getBytesUtf8("48656C6C6F20576F726C64");
        byte[] decoded = StringUtils.getBytesUtf8(STRING_FIXTURE);
        testByteByByte0(encoded, decoded);

        encoded = StringUtils.getBytesUtf8("41");
        decoded = new byte[] {(byte) 0x41};
        testByteByByte0(encoded, decoded);

        final BaseNCodec codec = Base16.Base161(true);
        for (int i = 0; i <= 150; i++) {
            final byte[][] randomData = BaseNTestData.randomData(codec, i);
            encoded = randomData[1];
            decoded = randomData[0];
            testByteByByte1(encoded, decoded, true);
        }
    }

    /**
     * Test method does three tests on the supplied data: 1. encoded ---[DECODE]--> decoded 2.
     * decoded ---[ENCODE]--> encoded 3. decoded ---[WRAP-WRAP-WRAP-etc...] --> decoded
     *
     * <p>By "[WRAP-WRAP-WRAP-etc...]" we mean situation where the Base16OutputStream wraps itself
     * in encode and decode mode over and over again.
     *
     * @param encoded base16 encoded data
     * @param decoded the data from above, but decoded
     * @throws IOException Usually signifies a bug in the Base16 commons-codec implementation.
     */
    private void testByChunk0(final byte[] encoded, final byte[] decoded) throws IOException {
        testByChunk1(encoded, decoded, false);
    }

    /**
     * Test method does three tests on the supplied data: 1. encoded ---[DECODE]--> decoded 2.
     * decoded ---[ENCODE]--> encoded 3. decoded ---[WRAP-WRAP-WRAP-etc...] --> decoded
     *
     * <p>By "[WRAP-WRAP-WRAP-etc...]" we mean situation where the Base16OutputStream wraps itself
     * in encode and decode mode over and over again.
     *
     * @param encoded base16 encoded data
     * @param decoded the data from above, but decoded
     * @param lowerCase if {@code true} then use a lower-case Base16 alphabet
     * @throws IOException Usually signifies a bug in the Base16 commons-codec implementation.
     */
    private void testByChunk1(final byte[] encoded, final byte[] decoded, final boolean lowerCase)
            throws IOException {

        try (final ByteArrayOutputStream byteOut = new ByteArrayOutputStream();
                final OutputStream out =
                        Base16OutputStream.Base16OutputStream1(byteOut, true, lowerCase)) {
            out.write(decoded);
            final byte[] output = byteOut.toByteArray();
            assertArrayEquals("Streaming chunked base16 encode", encoded, output);
        }

        try (final ByteArrayOutputStream byteOut = new ByteArrayOutputStream();
                final OutputStream out =
                        Base16OutputStream.Base16OutputStream1(byteOut, false, lowerCase)) {
            out.write(encoded);
            final byte[] output = byteOut.toByteArray();
            assertArrayEquals("Streaming chunked base16 decode", decoded, output);
        }

        try (final ByteArrayOutputStream byteOut = new ByteArrayOutputStream()) {
            final OutputStream decoderOut =
                    Base16OutputStream.Base16OutputStream1(byteOut, false, lowerCase);
            final OutputStream encoderOut =
                    Base16OutputStream.Base16OutputStream1(decoderOut, true, lowerCase);

            encoderOut.write(decoded);
            final byte[] output = byteOut.toByteArray();

            assertArrayEquals("Streaming chunked base16 wrap-wrap!", decoded, output);
        }
    }

    /**
     * Test method does three tests on the supplied data: 1. encoded ---[DECODE]--> decoded 2.
     * decoded ---[ENCODE]--> encoded 3. decoded ---[WRAP-WRAP-WRAP-etc...] --> decoded
     *
     * <p>By "[WRAP-WRAP-WRAP-etc...]" we mean situation where the Base16OutputStream wraps itself
     * in encode and decode mode over and over again.
     *
     * @param encoded base16 encoded data
     * @param decoded the data from above, but decoded
     * @throws IOException Usually signifies a bug in the Base16 commons-codec implementation.
     */
    private void testByteByByte0(final byte[] encoded, final byte[] decoded) throws IOException {
        testByteByByte1(encoded, decoded, false);
    }

    /**
     * Test method does three tests on the supplied data: 1. encoded ---[DECODE]--> decoded 2.
     * decoded ---[ENCODE]--> encoded 3. decoded ---[WRAP-WRAP-WRAP-etc...] --> decoded
     *
     * <p>By "[WRAP-WRAP-WRAP-etc...]" we mean situation where the Base16OutputStream wraps itself
     * in encode and decode mode over and over again.
     *
     * @param encoded base16 encoded data
     * @param decoded the data from above, but decoded
     * @throws IOException Usually signifies a bug in the Base16 commons-codec implementation.
     */
    private void testByteByByte1(
            final byte[] encoded, final byte[] decoded, final boolean lowerCase)
            throws IOException {

        try (final ByteArrayOutputStream byteOut = new ByteArrayOutputStream();
                final OutputStream out =
                        Base16OutputStream.Base16OutputStream1(byteOut, true, lowerCase)) {
            for (final byte element : decoded) {
                out.write(element);
            }
            final byte[] output = byteOut.toByteArray();
            assertArrayEquals("Streaming byte-by-byte base16 encode", encoded, output);
        }

        try (final ByteArrayOutputStream byteOut = new ByteArrayOutputStream();
                final OutputStream out =
                        Base16OutputStream.Base16OutputStream1(byteOut, false, lowerCase)) {
            for (final byte element : encoded) {
                out.write(element);
            }
            final byte[] output = byteOut.toByteArray();
            assertArrayEquals("Streaming byte-by-byte base16 decode", decoded, output);
        }

        try (final ByteArrayOutputStream byteOut = new ByteArrayOutputStream();
                final OutputStream out =
                        Base16OutputStream.Base16OutputStream1(byteOut, false, lowerCase)) {
            for (final byte element : encoded) {
                out.write(element);
                out.flush();
            }
            final byte[] output = byteOut.toByteArray();
            assertArrayEquals("Streaming byte-by-byte flush() base16 decode", decoded, output);
        }

        try (final ByteArrayOutputStream byteOut = new ByteArrayOutputStream();
                final OutputStream decoderOut =
                        Base16OutputStream.Base16OutputStream1(byteOut, false, lowerCase);
                final OutputStream encoderOut =
                        Base16OutputStream.Base16OutputStream1(decoderOut, true, lowerCase)) {
            for (final byte element : decoded) {
                encoderOut.write(element);
            }
            final byte[] output = byteOut.toByteArray();
            assertArrayEquals("Streaming byte-by-byte base16 wrap-wrap!", decoded, output);
        }
    }

    /**
     * Tests Base16OutputStream.write for expected IndexOutOfBoundsException conditions.
     *
     * @throws IOException for some failure scenarios.
     */
    @Test
    public void testWriteOutOfBounds() throws IOException {
        final byte[] buf = new byte[1024];
        final ByteArrayOutputStream bout = new ByteArrayOutputStream();
        try (final Base16OutputStream out = Base16OutputStream.Base16OutputStream3(bout)) {

            try {
                out.write0(buf, -1, 1);
                fail(
                        "Expected Base16OutputStream.write(buf, -1, 1) to throw a"
                                + " IndexOutOfBoundsException");
            } catch (final IndexOutOfBoundsException ioobe) {
            }

            try {
                out.write0(buf, 1, -1);
                fail(
                        "Expected Base16OutputStream.write(buf, 1, -1) to throw a"
                                + " IndexOutOfBoundsException");
            } catch (final IndexOutOfBoundsException ioobe) {
            }

            try {
                out.write0(buf, buf.length + 1, 0);
                fail(
                        "Expected Base16OutputStream.write(buf, buf.length + 1, 0) to throw a"
                                + " IndexOutOfBoundsException");
            } catch (final IndexOutOfBoundsException ioobe) {
            }

            try {
                out.write0(buf, buf.length - 1, 2);
                fail(
                        "Expected Base16OutputStream.write(buf, buf.length - 1, 2) to throw a"
                                + " IndexOutOfBoundsException");
            } catch (final IndexOutOfBoundsException ioobe) {
            }
        }
    }

    /**
     * Tests Base16OutputStream.write(null).
     *
     * @throws IOException for some failure scenarios.
     */
    @Test
    public void testWriteToNullCoverage() throws IOException {
        final ByteArrayOutputStream bout = new ByteArrayOutputStream();
        try (final Base16OutputStream out = Base16OutputStream.Base16OutputStream3(bout)) {
            out.write0(null, 0, 0);
            fail("Expcted Base16OutputStream.write(null) to throw a NullPointerException");
        } catch (final NullPointerException e) {
        }
    }
}
