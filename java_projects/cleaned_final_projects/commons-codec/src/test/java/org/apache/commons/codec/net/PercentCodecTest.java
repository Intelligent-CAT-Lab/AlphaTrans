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

import static org.junit.Assert.assertArrayEquals;
import static org.junit.Assert.assertEquals;
import static org.junit.Assert.assertNull;
import static org.junit.Assert.assertTrue;

import org.apache.commons.codec.DecoderException;
import org.apache.commons.codec.EncoderException;
import org.junit.Assert;
import org.junit.Ignore;
import org.junit.Test;

import java.nio.charset.StandardCharsets;
import java.util.Arrays;

/** Percent codec test cases. */
public class PercentCodecTest {

    @Test
    public void testBasicEncodeDecode() throws Exception {
        final PercentCodec percentCodec = new PercentCodec(1, false, null);
        final String input = "abcdABCD";
        final byte[] encoded = percentCodec.encode0(input.getBytes(StandardCharsets.UTF_8));
        final String encodedS = new String(encoded, StandardCharsets.UTF_8);
        final byte[] decoded = percentCodec.decode0(encoded);
        final String decodedS = new String(decoded, StandardCharsets.UTF_8);
        assertEquals("Basic PercentCodec encoding test", input, encodedS);
        assertEquals("Basic PercentCodec decoding test", input, decodedS);
    }

    @Test
    @Ignore
    public void testBasicSpace() throws Exception {
        final PercentCodec percentCodec = new PercentCodec(1, false, null);
        final String input = " ";
        final byte[] encoded = percentCodec.encode0(input.getBytes(StandardCharsets.UTF_8));
        Assert.assertArrayEquals("%20".getBytes(StandardCharsets.UTF_8), encoded);
    }

    @Test
    public void testConfigurablePercentEncoder() throws Exception {
        final String input = "abc123_-.*\u03B1\u03B2";
        final PercentCodec percentCodec =
                new PercentCodec(0, false, "abcdef".getBytes(StandardCharsets.UTF_8));
        final byte[] encoded = percentCodec.encode0(input.getBytes(StandardCharsets.UTF_8));
        final String encodedS = new String(encoded, StandardCharsets.UTF_8);
        assertEquals(
                "Configurable PercentCodec encoding test",
                "%61%62%63123_-.*%CE%B1%CE%B2",
                encodedS);
        final byte[] decoded = percentCodec.decode0(encoded);
        assertEquals(
                "Configurable PercentCodec decoding test",
                new String(decoded, StandardCharsets.UTF_8),
                input);
    }

    @Test
    public void testDecodeInvalidEncodedResultDecoding() throws Exception {
        final String inputS = "\u03B1\u03B2";
        final PercentCodec percentCodec = new PercentCodec(1, false, null);
        final byte[] encoded = percentCodec.encode0(inputS.getBytes(StandardCharsets.UTF_8));
        try {
            percentCodec.decode0(Arrays.copyOf(encoded, encoded.length - 1)); // exclude one byte
        } catch (final Exception e) {
            assertTrue(
                    DecoderException.class.isInstance(e)
                            && ArrayIndexOutOfBoundsException.class.isInstance(e.getCause()));
        }
    }

    @Test
    public void testDecodeNullObject() throws Exception {
        final PercentCodec percentCodec = new PercentCodec(1, false, null);
        assertNull(percentCodec.decode1((Object) null));
    }

    @Test(expected = DecoderException.class)
    public void testDecodeUnsupportedObject() throws Exception {
        final PercentCodec percentCodec = new PercentCodec(1, false, null);
        percentCodec.decode1("test");
    }

    @Test
    public void testEncodeNullObject() throws Exception {
        final PercentCodec percentCodec = new PercentCodec(1, false, null);
        assertNull(percentCodec.encode1((Object) null));
    }

    @Test(expected = EncoderException.class)
    public void testEncodeUnsupportedObject() throws Exception {
        final PercentCodec percentCodec = new PercentCodec(1, false, null);
        percentCodec.encode1("test");
    }

    @Test
    public void testPercentEncoderDecoderWithNullOrEmptyInput() throws Exception {
        final PercentCodec percentCodec = new PercentCodec(0, true, null);
        assertNull("Null input value encoding test", percentCodec.encode0(null));
        assertNull("Null input value decoding test", percentCodec.decode0(null));
        final byte[] emptyInput = "".getBytes(StandardCharsets.UTF_8);
        assertEquals(
                "Empty input value encoding test", percentCodec.encode0(emptyInput), emptyInput);
        assertArrayEquals(
                "Empty input value decoding test", percentCodec.decode0(emptyInput), emptyInput);
    }

    @Test
    public void testPercentEncoderDecoderWithPlusForSpace() throws Exception {
        final String input = "a b c d";
        final PercentCodec percentCodec = new PercentCodec(0, true, null);
        final byte[] encoded = percentCodec.encode0(input.getBytes(StandardCharsets.UTF_8));
        final String encodedS = new String(encoded, StandardCharsets.UTF_8);
        assertEquals("PercentCodec plus for space encoding test", "a+b+c+d", encodedS);
        final byte[] decode = percentCodec.decode0(encoded);
        assertEquals(
                "PercentCodec plus for space decoding test",
                new String(decode, StandardCharsets.UTF_8),
                input);
    }

    @Test
    public void testSafeCharEncodeDecodeObject() throws Exception {
        final PercentCodec percentCodec = new PercentCodec(0, true, null);
        final String input = "abc123_-.*";
        final Object encoded =
                percentCodec.encode1((Object) input.getBytes(StandardCharsets.UTF_8));
        final String encodedS = new String((byte[]) encoded, StandardCharsets.UTF_8);
        final Object decoded = percentCodec.decode1(encoded);
        final String decodedS = new String((byte[]) decoded, StandardCharsets.UTF_8);
        assertEquals("Basic PercentCodec safe char encoding test", input, encodedS);
        assertEquals("Basic PercentCodec safe char decoding test", input, decodedS);
    }

    @Test
    public void testUnsafeCharEncodeDecode() throws Exception {
        final PercentCodec percentCodec = new PercentCodec(1, false, null);
        final String input = "\u03B1\u03B2\u03B3\u03B4\u03B5\u03B6% ";
        final byte[] encoded = percentCodec.encode0(input.getBytes(StandardCharsets.UTF_8));
        final String encodedS = new String(encoded, StandardCharsets.UTF_8);
        final byte[] decoded = percentCodec.decode0(encoded);
        final String decodedS = new String(decoded, StandardCharsets.UTF_8);
        assertEquals(
                "Basic PercentCodec unsafe char encoding test",
                "%CE%B1%CE%B2%CE%B3%CE%B4%CE%B5%CE%B6%25 ",
                encodedS);
        assertEquals("Basic PercentCodec unsafe char decoding test", input, decodedS);
    }
}
