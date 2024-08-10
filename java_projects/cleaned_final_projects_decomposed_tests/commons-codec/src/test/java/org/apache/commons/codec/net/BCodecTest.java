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

package org.apache.commons.codec.net;

import static org.junit.Assert.assertEquals;
import static org.junit.Assert.assertNull;
import static org.junit.Assert.fail;

import org.apache.commons.codec.CharEncoding;
import org.apache.commons.codec.CodecPolicy;
import org.apache.commons.codec.DecoderException;
import org.apache.commons.codec.EncoderException;
import org.junit.Assert;
import org.junit.Test;

import java.nio.charset.StandardCharsets;
import java.nio.charset.UnsupportedCharsetException;

/** Quoted-printable codec test cases */
public class BCodecTest {
    private static final String[] BASE64_IMPOSSIBLE_CASES = {
        "=?ASCII?B?ZE==?=",
        "=?ASCII?B?ZmC=?=",
        "=?ASCII?B?Zm9vYE==?=",
        "=?ASCII?B?Zm9vYmC=?=",
        "=?ASCII?B?AB==?="
    };

    static final int SWISS_GERMAN_STUFF_UNICODE[] = {
        0x47, 0x72, 0xFC, 0x65, 0x7A, 0x69, 0x5F, 0x7A, 0xE4, 0x6D, 0xE4
    };

    static final int RUSSIAN_STUFF_UNICODE[] = {
        0x412, 0x441, 0x435, 0x43C, 0x5F, 0x43F, 0x440, 0x438, 0x432, 0x435, 0x442
    };

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
    public void testNullInput_test0_decomposed() throws Exception {
        final BCodec bcodec = BCodec.BCodec0();
    }

    @Test
    public void testNullInput_test1_decomposed() throws Exception {
        final BCodec bcodec = BCodec.BCodec0();
        assertNull(bcodec.doDecoding(null));
    }

    @Test
    public void testNullInput_test2_decomposed() throws Exception {
        final BCodec bcodec = BCodec.BCodec0();
        assertNull(bcodec.doDecoding(null));
        assertNull(bcodec.doEncoding(null));
    }

    @Test
    public void testUTF8RoundTrip_test0_decomposed() throws Exception {
        final String ru_msg = constructString(RUSSIAN_STUFF_UNICODE);
        final String ch_msg = constructString(SWISS_GERMAN_STUFF_UNICODE);
    }

    @Test
    public void testUTF8RoundTrip_test1_decomposed() throws Exception {
        final String ru_msg = constructString(RUSSIAN_STUFF_UNICODE);
        final String ch_msg = constructString(SWISS_GERMAN_STUFF_UNICODE);
        final BCodec bcodec = BCodec.BCodec2(CharEncoding.UTF_8);
    }

    @Test
    public void testUTF8RoundTrip_test2_decomposed() throws Exception {
        final String ru_msg = constructString(RUSSIAN_STUFF_UNICODE);
        final String ch_msg = constructString(SWISS_GERMAN_STUFF_UNICODE);
        final BCodec bcodec = BCodec.BCodec2(CharEncoding.UTF_8);
        assertEquals("=?UTF-8?B?0JLRgdC10Lxf0L/RgNC40LLQtdGC?=", bcodec.encode2(ru_msg));
        assertEquals("=?UTF-8?B?R3LDvGV6aV96w6Rtw6Q=?=", bcodec.encode2(ch_msg));
        bcodec.encode2(ru_msg);
    }

    @Test
    public void testUTF8RoundTrip_test3_decomposed() throws Exception {
        final String ru_msg = constructString(RUSSIAN_STUFF_UNICODE);
        final String ch_msg = constructString(SWISS_GERMAN_STUFF_UNICODE);
        final BCodec bcodec = BCodec.BCodec2(CharEncoding.UTF_8);
        assertEquals("=?UTF-8?B?0JLRgdC10Lxf0L/RgNC40LLQtdGC?=", bcodec.encode2(ru_msg));
        assertEquals("=?UTF-8?B?R3LDvGV6aV96w6Rtw6Q=?=", bcodec.encode2(ch_msg));
        bcodec.encode2(ru_msg);
        assertEquals(ru_msg, bcodec.decode0(bcodec.encode2(ru_msg)));
    }

    @Test
    public void testUTF8RoundTrip_test4_decomposed() throws Exception {
        final String ru_msg = constructString(RUSSIAN_STUFF_UNICODE);
        final String ch_msg = constructString(SWISS_GERMAN_STUFF_UNICODE);
        final BCodec bcodec = BCodec.BCodec2(CharEncoding.UTF_8);
        assertEquals("=?UTF-8?B?0JLRgdC10Lxf0L/RgNC40LLQtdGC?=", bcodec.encode2(ru_msg));
        assertEquals("=?UTF-8?B?R3LDvGV6aV96w6Rtw6Q=?=", bcodec.encode2(ch_msg));
        bcodec.encode2(ru_msg);
        assertEquals(ru_msg, bcodec.decode0(bcodec.encode2(ru_msg)));
        bcodec.encode2(ch_msg);
    }

    @Test
    public void testUTF8RoundTrip_test5_decomposed() throws Exception {
        final String ru_msg = constructString(RUSSIAN_STUFF_UNICODE);
        final String ch_msg = constructString(SWISS_GERMAN_STUFF_UNICODE);
        final BCodec bcodec = BCodec.BCodec2(CharEncoding.UTF_8);
        assertEquals("=?UTF-8?B?0JLRgdC10Lxf0L/RgNC40LLQtdGC?=", bcodec.encode2(ru_msg));
        assertEquals("=?UTF-8?B?R3LDvGV6aV96w6Rtw6Q=?=", bcodec.encode2(ch_msg));
        bcodec.encode2(ru_msg);
        assertEquals(ru_msg, bcodec.decode0(bcodec.encode2(ru_msg)));
        bcodec.encode2(ch_msg);
        assertEquals(ch_msg, bcodec.decode0(bcodec.encode2(ch_msg)));
    }

    @Test
    public void testBasicEncodeDecode_test0_decomposed() throws Exception {
        final BCodec bcodec = BCodec.BCodec0();
    }

    @Test
    public void testBasicEncodeDecode_test1_decomposed() throws Exception {
        final BCodec bcodec = BCodec.BCodec0();
        final String plain = "Hello there";
        final String encoded = bcodec.encode2(plain);
    }

    @Test
    public void testBasicEncodeDecode_test2_decomposed() throws Exception {
        final BCodec bcodec = BCodec.BCodec0();
        final String plain = "Hello there";
        final String encoded = bcodec.encode2(plain);
        assertEquals("Basic B encoding test", "=?UTF-8?B?SGVsbG8gdGhlcmU=?=", encoded);
        assertEquals("Basic B decoding test", plain, bcodec.decode0(encoded));
    }

    @Test
    public void testEncodeDecodeNull_test0_decomposed() throws Exception {
        final BCodec bcodec = BCodec.BCodec0();
    }

    @Test
    public void testEncodeDecodeNull_test1_decomposed() throws Exception {
        final BCodec bcodec = BCodec.BCodec0();
        assertNull("Null string B encoding test", bcodec.encode2((String) null));
    }

    @Test
    public void testEncodeDecodeNull_test2_decomposed() throws Exception {
        final BCodec bcodec = BCodec.BCodec0();
        assertNull("Null string B encoding test", bcodec.encode2((String) null));
        assertNull("Null string B decoding test", bcodec.decode0((String) null));
    }

    @Test
    public void testEncodeStringWithNull_test0_decomposed() throws Exception {
        final BCodec bcodec = BCodec.BCodec0();
    }

    @Test
    public void testEncodeStringWithNull_test1_decomposed() throws Exception {
        final BCodec bcodec = BCodec.BCodec0();
        final String test = null;
        final String result = bcodec.encode1(test, "charset");
    }

    @Test
    public void testEncodeStringWithNull_test2_decomposed() throws Exception {
        final BCodec bcodec = BCodec.BCodec0();
        final String test = null;
        final String result = bcodec.encode1(test, "charset");
        assertNull("Result should be null", result);
    }

    @Test
    public void testDecodeStringWithNull_test0_decomposed() throws Exception {
        final BCodec bcodec = BCodec.BCodec0();
    }

    @Test
    public void testDecodeStringWithNull_test1_decomposed() throws Exception {
        final BCodec bcodec = BCodec.BCodec0();
        final String test = null;
        final String result = bcodec.decode0(test);
    }

    @Test
    public void testDecodeStringWithNull_test2_decomposed() throws Exception {
        final BCodec bcodec = BCodec.BCodec0();
        final String test = null;
        final String result = bcodec.decode0(test);
        assertNull("Result should be null", result);
    }

    @Test
    public void testEncodeObjects_test0_decomposed() throws Exception {
        final BCodec bcodec = BCodec.BCodec0();
    }

    @Test
    public void testEncodeObjects_test1_decomposed() throws Exception {
        final BCodec bcodec = BCodec.BCodec0();
        final String plain = "what not";
        final String encoded = (String) bcodec.encode3((Object) plain);
    }

    @Test
    public void testEncodeObjects_test2_decomposed() throws Exception {
        final BCodec bcodec = BCodec.BCodec0();
        final String plain = "what not";
        final String encoded = (String) bcodec.encode3((Object) plain);
        assertEquals("Basic B encoding test", "=?UTF-8?B?d2hhdCBub3Q=?=", encoded);
        final Object result = bcodec.encode3((Object) null);
    }

    @Test
    public void testEncodeObjects_test3_decomposed() throws Exception {
        final BCodec bcodec = BCodec.BCodec0();
        final String plain = "what not";
        final String encoded = (String) bcodec.encode3((Object) plain);
        assertEquals("Basic B encoding test", "=?UTF-8?B?d2hhdCBub3Q=?=", encoded);
        final Object result = bcodec.encode3((Object) null);
        assertNull("Encoding a null Object should return null", result);
        try {
            final Object dObj = Double.valueOf(3.0d);
            bcodec.encode3(dObj);
            fail("Trying to url encode a Double object should cause an exception.");
        } catch (final EncoderException ee) {
        }
    }

    @Test(expected = UnsupportedCharsetException.class)
    public void testInvalidEncoding_test0_decomposed()  {
        BCodec.BCodec2("NONSENSE");
    }

    @Test
    public void testDecodeObjects_test0_decomposed() throws Exception {
        final BCodec bcodec = BCodec.BCodec0();
    }

    @Test
    public void testDecodeObjects_test1_decomposed() throws Exception {
        final BCodec bcodec = BCodec.BCodec0();
        final String decoded = "=?UTF-8?B?d2hhdCBub3Q=?=";
        final String plain = (String) bcodec.decode1((Object) decoded);
    }

    @Test
    public void testDecodeObjects_test2_decomposed() throws Exception {
        final BCodec bcodec = BCodec.BCodec0();
        final String decoded = "=?UTF-8?B?d2hhdCBub3Q=?=";
        final String plain = (String) bcodec.decode1((Object) decoded);
        assertEquals("Basic B decoding test", "what not", plain);
        final Object result = bcodec.decode1((Object) null);
    }

    @Test
    public void testDecodeObjects_test3_decomposed() throws Exception {
        final BCodec bcodec = BCodec.BCodec0();
        final String decoded = "=?UTF-8?B?d2hhdCBub3Q=?=";
        final String plain = (String) bcodec.decode1((Object) decoded);
        assertEquals("Basic B decoding test", "what not", plain);
        final Object result = bcodec.decode1((Object) null);
        assertNull("Decoding a null Object should return null", result);
        try {
            final Object dObj = Double.valueOf(3.0d);
            bcodec.decode1(dObj);
            fail("Trying to url encode a Double object should cause an exception.");
        } catch (final DecoderException ee) {
        }
    }

    @Test
    public void testBase64ImpossibleSamplesDefault_test0_decomposed() throws DecoderException {
        final BCodec codec = BCodec.BCodec0();
    }

    @Test
    public void testBase64ImpossibleSamplesDefault_test1_decomposed() throws DecoderException {
        final BCodec codec = BCodec.BCodec0();
        Assert.assertFalse(codec.isStrictDecoding());
    }

    @Test
    public void testBase64ImpossibleSamplesDefault_test2_decomposed() throws DecoderException {
        final BCodec codec = BCodec.BCodec0();
        Assert.assertFalse(codec.isStrictDecoding());
        for (final String s : BASE64_IMPOSSIBLE_CASES) {
            codec.decode0(s);
        }
    }

    @Test
    public void testBase64ImpossibleSamplesLenient_test0_decomposed() throws DecoderException {
        final BCodec codec = new BCodec(StandardCharsets.UTF_8, CodecPolicy.LENIENT);
    }

    @Test
    public void testBase64ImpossibleSamplesLenient_test1_decomposed() throws DecoderException {
        final BCodec codec = new BCodec(StandardCharsets.UTF_8, CodecPolicy.LENIENT);
        Assert.assertFalse(codec.isStrictDecoding());
    }

    @Test
    public void testBase64ImpossibleSamplesLenient_test2_decomposed() throws DecoderException {
        final BCodec codec = new BCodec(StandardCharsets.UTF_8, CodecPolicy.LENIENT);
        Assert.assertFalse(codec.isStrictDecoding());
        for (final String s : BASE64_IMPOSSIBLE_CASES) {
            codec.decode0(s);
        }
    }

    @Test
    public void testBase64ImpossibleSamplesStrict_test0_decomposed() throws DecoderException {
        final BCodec codec = new BCodec(StandardCharsets.UTF_8, CodecPolicy.STRICT);
    }

    @Test
    public void testBase64ImpossibleSamplesStrict_test1_decomposed() throws DecoderException {
        final BCodec codec = new BCodec(StandardCharsets.UTF_8, CodecPolicy.STRICT);
        Assert.assertTrue(codec.isStrictDecoding());
    }

    @Test
    public void testBase64ImpossibleSamplesStrict_test2_decomposed() throws DecoderException {
        final BCodec codec = new BCodec(StandardCharsets.UTF_8, CodecPolicy.STRICT);
        Assert.assertTrue(codec.isStrictDecoding());
        for (final String s : BASE64_IMPOSSIBLE_CASES) {
            try {
                codec.decode0(s);
                fail("Expected an exception for impossible case");
            } catch (final DecoderException ex) {
            }
        }
    }
}