
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


package org.apache.commons.codec.net;

import static org.junit.Assert.assertEquals;
import static org.junit.Assert.assertNull;
import static org.junit.Assert.fail;

import org.apache.commons.codec.CharEncoding;
import org.apache.commons.codec.DecoderException;
import org.apache.commons.codec.EncoderException;
import org.junit.Test;

import java.io.UnsupportedEncodingException;
import java.nio.charset.StandardCharsets;

/** URL codec test cases */
public class URLCodecTest {

    static final int SWISS_GERMAN_STUFF_UNICODE[] = {
        0x47, 0x72, 0xFC, 0x65, 0x7A, 0x69, 0x5F, 0x7A, 0xE4, 0x6D, 0xE4
    };

    static final int RUSSIAN_STUFF_UNICODE[] = {
        0x412, 0x441, 0x435, 0x43C, 0x5F, 0x43F, 0x440, 0x438, 0x432, 0x435, 0x442
    };

    private void validateState(final URLCodec urlCodec) {}

    private String constructString(final int[] unicodeChars) {
        final StringBuilder buffer = new StringBuilder();
        if (unicodeChars != null) {
            for (final int unicodeChar : unicodeChars) {
                buffer.append((char) unicodeChar);
            }
        }
        return buffer.toString();
    }

    @Test
    public void testUTF8RoundTrip() throws Exception {

        final String ru_msg = constructString(RUSSIAN_STUFF_UNICODE);
        final String ch_msg = constructString(SWISS_GERMAN_STUFF_UNICODE);

        final URLCodec urlCodec = URLCodec.URLCodec1();
        this.validateState(urlCodec);

        assertEquals(
                "%D0%92%D1%81%D0%B5%D0%BC_%D0%BF%D1%80%D0%B8%D0%B2%D0%B5%D1%82",
                urlCodec.encode1(ru_msg, CharEncoding.UTF_8));
        assertEquals("Gr%C3%BCezi_z%C3%A4m%C3%A4", urlCodec.encode1(ch_msg, CharEncoding.UTF_8));

        assertEquals(
                ru_msg,
                urlCodec.decode1(urlCodec.encode1(ru_msg, CharEncoding.UTF_8), CharEncoding.UTF_8));
        assertEquals(
                ch_msg,
                urlCodec.decode1(urlCodec.encode1(ch_msg, CharEncoding.UTF_8), CharEncoding.UTF_8));
        this.validateState(urlCodec);
    }

    @Test
    public void testBasicEncodeDecode() throws Exception {
        final URLCodec urlCodec = URLCodec.URLCodec1();
        final String plain = "Hello there!";
        final String encoded = urlCodec.encode2(plain);
        assertEquals("Basic URL encoding test", "Hello+there%21", encoded);
        assertEquals("Basic URL decoding test", plain, urlCodec.decode2(encoded));
        this.validateState(urlCodec);
    }

    @Test
    public void testSafeCharEncodeDecode() throws Exception {
        final URLCodec urlCodec = URLCodec.URLCodec1();
        final String plain = "abc123_-.*";
        final String encoded = urlCodec.encode2(plain);
        assertEquals("Safe chars URL encoding test", plain, encoded);
        assertEquals("Safe chars URL decoding test", plain, urlCodec.decode2(encoded));
        this.validateState(urlCodec);
    }

    @Test
    public void testUnsafeEncodeDecode() throws Exception {
        final URLCodec urlCodec = URLCodec.URLCodec1();
        final String plain = "~!@#$%^&()+{}\"\\;:`,/[]";
        final String encoded = urlCodec.encode2(plain);
        assertEquals(
                "Unsafe chars URL encoding test",
                "%7E%21%40%23%24%25%5E%26%28%29%2B%7B%7D%22%5C%3B%3A%60%2C%2F%5B%5D",
                encoded);
        assertEquals("Unsafe chars URL decoding test", plain, urlCodec.decode2(encoded));
        this.validateState(urlCodec);
    }

    @Test
    public void testEncodeDecodeNull() throws Exception {
        final URLCodec urlCodec = URLCodec.URLCodec1();
        assertNull("Null string URL encoding test", urlCodec.encode2((String) null));
        assertNull("Null string URL decoding test", urlCodec.decode2((String) null));
        this.validateState(urlCodec);
    }

    @Test
    public void testDecodeInvalid() throws Exception {
        final URLCodec urlCodec = URLCodec.URLCodec1();
        try {
            urlCodec.decode2("%");
            fail("DecoderException should have been thrown");
        } catch (final DecoderException e) {
        }
        try {
            urlCodec.decode2("%A");
            fail("DecoderException should have been thrown");
        } catch (final DecoderException e) {
        }
        try {
            urlCodec.decode2("%WW");
            fail("DecoderException should have been thrown");
        } catch (final DecoderException e) {
        }
        try {
            urlCodec.decode2("%0W");
            fail("DecoderException should have been thrown");
        } catch (final DecoderException e) {
        }
        this.validateState(urlCodec);
    }

    @Test
    public void testDecodeInvalidContent() throws UnsupportedEncodingException, DecoderException {
        final String ch_msg = constructString(SWISS_GERMAN_STUFF_UNICODE);
        final URLCodec urlCodec = URLCodec.URLCodec1();
        final byte[] input = ch_msg.getBytes(StandardCharsets.ISO_8859_1);
        final byte[] output = urlCodec.decode0(input);
        assertEquals(input.length, output.length);
        for (int i = 0; i < input.length; i++) {
            assertEquals(input[i], output[i]);
        }
        this.validateState(urlCodec);
    }

    @Test
    public void testEncodeNull() throws Exception {
        final URLCodec urlCodec = URLCodec.URLCodec1();
        final byte[] plain = null;
        final byte[] encoded = urlCodec.encode0(plain);
        assertNull("Encoding a null string should return null", encoded);
        this.validateState(urlCodec);
    }

    @Test
    public void testEncodeUrlWithNullBitSet() throws Exception {
        final URLCodec urlCodec = URLCodec.URLCodec1();
        final String plain = "Hello there!";
        final String encoded =
                new String(URLCodec.encodeUrl(null, plain.getBytes(StandardCharsets.UTF_8)));
        assertEquals("Basic URL encoding test", "Hello+there%21", encoded);
        assertEquals("Basic URL decoding test", plain, urlCodec.decode2(encoded));
        this.validateState(urlCodec);
    }

    @Test
    public void testDecodeWithNullArray() throws Exception {
        final byte[] plain = null;
        final byte[] result = URLCodec.decodeUrl(plain);
        assertNull("Result should be null", result);
    }

    @Test
    public void testEncodeStringWithNull() throws Exception {
        final URLCodec urlCodec = URLCodec.URLCodec1();
        final String test = null;
        final String result = urlCodec.encode1(test, "charset");
        assertNull("Result should be null", result);
    }

    @Test
    public void testDecodeStringWithNull() throws Exception {
        final URLCodec urlCodec = URLCodec.URLCodec1();
        final String test = null;
        final String result = urlCodec.decode1(test, "charset");
        assertNull("Result should be null", result);
    }

    @Test
    public void testEncodeObjects() throws Exception {
        final URLCodec urlCodec = URLCodec.URLCodec1();
        final String plain = "Hello there!";
        String encoded = (String) urlCodec.encode3((Object) plain);
        assertEquals("Basic URL encoding test", "Hello+there%21", encoded);

        final byte[] plainBA = plain.getBytes(StandardCharsets.UTF_8);
        final byte[] encodedBA = (byte[]) urlCodec.encode3((Object) plainBA);
        encoded = new String(encodedBA);
        assertEquals("Basic URL encoding test", "Hello+there%21", encoded);

        final Object result = urlCodec.encode3((Object) null);
        assertNull("Encoding a null Object should return null", result);

        try {
            final Object dObj = Double.valueOf(3.0d);
            urlCodec.encode3(dObj);
            fail("Trying to url encode a Double object should cause an exception.");
        } catch (final EncoderException ee) {
        }
        this.validateState(urlCodec);
    }

    @Test
    public void testInvalidEncoding() {
        final URLCodec urlCodec = new URLCodec("NONSENSE");
        final String plain = "Hello there!";
        try {
            urlCodec.encode2(plain);
            fail("We set the encoding to a bogus NONSENSE vlaue, this shouldn't have worked.");
        } catch (final EncoderException ee) {
        }
        try {
            urlCodec.decode2(plain);
            fail("We set the encoding to a bogus NONSENSE vlaue, this shouldn't have worked.");
        } catch (final DecoderException ee) {
        }
        this.validateState(urlCodec);
    }

    @Test
    public void testDecodeObjects() throws Exception {
        final URLCodec urlCodec = URLCodec.URLCodec1();
        final String plain = "Hello+there%21";
        String decoded = (String) urlCodec.decode3((Object) plain);
        assertEquals("Basic URL decoding test", "Hello there!", decoded);

        final byte[] plainBA = plain.getBytes(StandardCharsets.UTF_8);
        final byte[] decodedBA = (byte[]) urlCodec.decode3((Object) plainBA);
        decoded = new String(decodedBA);
        assertEquals("Basic URL decoding test", "Hello there!", decoded);

        final Object result = urlCodec.decode3((Object) null);
        assertNull("Decoding a null Object should return null", result);

        try {
            final Object dObj = Double.valueOf(3.0d);
            urlCodec.decode3(dObj);
            fail("Trying to url encode a Double object should cause an exception.");
        } catch (final DecoderException ee) {
        }
        this.validateState(urlCodec);
    }

    @Test
    public void testDefaultEncoding() throws Exception {
        final String plain = "Hello there!";
        final URLCodec urlCodec = new URLCodec("UnicodeBig");
        urlCodec.encode2(plain); // To work around a weird quirk in Java 1.2.2
        final String encoded1 = urlCodec.encode1(plain, "UnicodeBig");
        final String encoded2 = urlCodec.encode2(plain);
        assertEquals(encoded1, encoded2);
        this.validateState(urlCodec);
    }
}
