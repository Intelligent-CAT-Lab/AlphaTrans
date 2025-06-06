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
package org.apache.commons.fileupload.util.mime;

import static org.junit.Assert.assertArrayEquals;
import static org.junit.Assert.assertTrue;
import static org.junit.Assert.fail;

import org.junit.Test;

import java.io.ByteArrayOutputStream;
import java.io.IOException;
import java.io.UnsupportedEncodingException;

/**
 * @since 1.3
 */
public final class Base64DecoderTestCase {

    private static final String US_ASCII_CHARSET = "US-ASCII";

    /**
     * Tests RFC 4648 section 10 test vectors.
     *
     * <ul>
     *   <li>BASE64("") = ""
     *   <li>BASE64("f") = "Zg=="
     *   <li>BASE64("fo") = "Zm8="
     *   <li>BASE64("foo") = "Zm9v"
     *   <li>BASE64("foob") = "Zm9vYg=="
     *   <li>BASE64("fooba") = "Zm9vYmE="
     *   <li>BASE64("foobar") = "Zm9vYmFy"
     * </ul>
     *
     * @see <a href="http://tools.ietf.org/html/rfc4648">http://tools.ietf.org/html/rfc4648</a>
     */
    

    /**
     * Test our decode with pad character in the middle. Continues provided that the padding is in
     * the correct place, i.e. concatenated valid strings decode OK.
     */
    

    /** Ignores non-BASE64 bytes. */
    

    

    

    

    

    

    

    

    

    

    

    private static void assertEncoded(String clearText, String encoded) throws Exception {
        byte[] expected = clearText.getBytes(US_ASCII_CHARSET);

        ByteArrayOutputStream out = new ByteArrayOutputStream(encoded.length());
        byte[] encodedData = encoded.getBytes(US_ASCII_CHARSET);
        Base64Decoder.decode(encodedData, out);
        byte[] actual = out.toByteArray();

        assertArrayEquals(expected, actual);
    }

    private static void assertIOException(String messageText, String encoded)
            throws UnsupportedEncodingException {
        ByteArrayOutputStream out = new ByteArrayOutputStream(encoded.length());
        byte[] encodedData = encoded.getBytes(US_ASCII_CHARSET);
        try {
            Base64Decoder.decode(encodedData, out);
            fail("Expected IOException");
        } catch (IOException e) {
            String em = e.getMessage();
            assertTrue(
                    "Expected to find " + messageText + " in '" + em + "'",
                    em.contains(messageText));
        }
    }

    @Test
    public void rfc4648Section10Decode_test0_decomposed() throws Exception {
        assertEncoded("", "");
        assertEncoded("f", "Zg==");
        assertEncoded("fo", "Zm8=");
        assertEncoded("foo", "Zm9v");
        assertEncoded("foob", "Zm9vYg==");
        assertEncoded("fooba", "Zm9vYmE=");
        assertEncoded("foobar", "Zm9vYmFy");
    }

    @Test
    public void decodeWithInnerPad_test0_decomposed() throws Exception {
        assertEncoded("Hello WorldHello World", "SGVsbG8gV29ybGQ=SGVsbG8gV29ybGQ=");
    }

    @Test
    public void nonBase64Bytes_test0_decomposed() throws Exception {
        assertEncoded("Hello World", "S?G!V%sbG 8g\rV\t\n29ybGQ*=");
    }

    @Test(expected = IOException.class)
    public void truncatedString_test0_decomposed() throws Exception {
        final byte[] x = new byte[] {'n'};
        Base64Decoder.decode(x, new ByteArrayOutputStream());
    }

    @Test
    public void decodeTrailingJunk_test0_decomposed() throws Exception {
        assertEncoded("foobar", "Zm9vYmFy!!!");
    }

    @Test
    public void decodeTrailing1_test0_decomposed() throws Exception {
        assertIOException("truncated", "Zm9vYmFy1");
    }

    @Test
    public void decodeTrailing2_test0_decomposed() throws Exception {
        assertIOException("truncated", "Zm9vYmFy12");
    }

    @Test
    public void decodeTrailing3_test0_decomposed() throws Exception {
        assertIOException("truncated", "Zm9vYmFy123");
    }

    @Test
    public void badPadding_test0_decomposed() throws Exception {
        assertIOException("incorrect padding, 4th byte", "Zg=a");
    }

    @Test
    public void badPaddingLeading1_test0_decomposed() throws Exception {
        assertIOException("incorrect padding, first two bytes cannot be padding", "=A==");
    }

    @Test
    public void badPaddingLeading2_test0_decomposed() throws Exception {
        assertIOException("incorrect padding, first two bytes cannot be padding", "====");
    }

    @Test
    public void badLength_test0_decomposed() throws Exception {
        assertIOException("truncated", "Zm8==");
    }

    @Test
    public void nonASCIIcharacter_test0_decomposed() throws Exception {
        assertEncoded("f", "Zg=À=");
        assertEncoded("f", "Zg=\u0100=");
    }
}