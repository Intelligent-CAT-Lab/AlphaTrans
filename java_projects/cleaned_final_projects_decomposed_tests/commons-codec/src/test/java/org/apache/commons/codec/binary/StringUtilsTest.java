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

import org.junit.Assert;
import org.junit.Test;

import java.io.UnsupportedEncodingException;
import java.nio.ByteBuffer;
import java.nio.charset.StandardCharsets;

/** Tests {@link StringUtils} */
public class StringUtilsTest {

    private static final byte[] BYTES_FIXTURE = {'a', 'b', 'c'};

    private static final byte[] BYTES_FIXTURE_16BE = {0, 'a', 0, 'b', 0, 'c'};

    private static final byte[] BYTES_FIXTURE_16LE = {'a', 0, 'b', 0, 'c', 0};

    private static final String STRING_FIXTURE = "ABC";

    /**
     * We could make the constructor private but there does not seem to be a point to jumping
     * through extra code hoops to restrict instantiation right now.
     */
    

    

    private void testGetBytesUnchecked(final String charsetName)
            throws UnsupportedEncodingException {
        final byte[] expected = STRING_FIXTURE.getBytes(charsetName);
        final byte[] actual = StringUtils.getBytesUnchecked(STRING_FIXTURE, charsetName);
        Assert.assertArrayEquals(expected, actual);
    }

    

    

    

    

    

    

    

    private void testNewString(final String charsetName) throws UnsupportedEncodingException {
        final String expected = new String(BYTES_FIXTURE, charsetName);
        final String actual = StringUtils.newString1(BYTES_FIXTURE, charsetName);
        Assert.assertEquals(expected, actual);
    }

    @Test
    public void testConstructor_test0_decomposed()  {
        new StringUtils();
    }

    @Test
    public void testGetBytesIso8859_1_test0_decomposed() throws UnsupportedEncodingException {
        final String charsetName = "ISO-8859-1";
        testGetBytesUnchecked(charsetName);
    }

    @Test
    public void testGetBytesIso8859_1_test1_decomposed() throws UnsupportedEncodingException {
        final String charsetName = "ISO-8859-1";
        testGetBytesUnchecked(charsetName);
        final byte[] expected = STRING_FIXTURE.getBytes(charsetName);
    }

    @Test
    public void testGetBytesIso8859_1_test2_decomposed() throws UnsupportedEncodingException {
        final String charsetName = "ISO-8859-1";
        testGetBytesUnchecked(charsetName);
        final byte[] expected = STRING_FIXTURE.getBytes(charsetName);
        final byte[] actual = StringUtils.getBytesIso8859_1(STRING_FIXTURE);
    }

    @Test
    public void testGetBytesIso8859_1_test3_decomposed() throws UnsupportedEncodingException {
        final String charsetName = "ISO-8859-1";
        testGetBytesUnchecked(charsetName);
        final byte[] expected = STRING_FIXTURE.getBytes(charsetName);
        final byte[] actual = StringUtils.getBytesIso8859_1(STRING_FIXTURE);
        Assert.assertArrayEquals(expected, actual);
    }

    @Test
    public void testGetBytesUsAscii_test0_decomposed() throws UnsupportedEncodingException {
        final String charsetName = "US-ASCII";
        testGetBytesUnchecked(charsetName);
    }

    @Test
    public void testGetBytesUsAscii_test1_decomposed() throws UnsupportedEncodingException {
        final String charsetName = "US-ASCII";
        testGetBytesUnchecked(charsetName);
        final byte[] expected = STRING_FIXTURE.getBytes(charsetName);
    }

    @Test
    public void testGetBytesUsAscii_test2_decomposed() throws UnsupportedEncodingException {
        final String charsetName = "US-ASCII";
        testGetBytesUnchecked(charsetName);
        final byte[] expected = STRING_FIXTURE.getBytes(charsetName);
        final byte[] actual = StringUtils.getBytesUsAscii(STRING_FIXTURE);
    }

    @Test
    public void testGetBytesUsAscii_test3_decomposed() throws UnsupportedEncodingException {
        final String charsetName = "US-ASCII";
        testGetBytesUnchecked(charsetName);
        final byte[] expected = STRING_FIXTURE.getBytes(charsetName);
        final byte[] actual = StringUtils.getBytesUsAscii(STRING_FIXTURE);
        Assert.assertArrayEquals(expected, actual);
    }

    @Test
    public void testGetBytesUtf16_test0_decomposed() throws UnsupportedEncodingException {
        final String charsetName = "UTF-16";
        testGetBytesUnchecked(charsetName);
    }

    @Test
    public void testGetBytesUtf16_test1_decomposed() throws UnsupportedEncodingException {
        final String charsetName = "UTF-16";
        testGetBytesUnchecked(charsetName);
        final byte[] expected = STRING_FIXTURE.getBytes(charsetName);
    }

    @Test
    public void testGetBytesUtf16_test2_decomposed() throws UnsupportedEncodingException {
        final String charsetName = "UTF-16";
        testGetBytesUnchecked(charsetName);
        final byte[] expected = STRING_FIXTURE.getBytes(charsetName);
        final byte[] actual = StringUtils.getBytesUtf16(STRING_FIXTURE);
    }

    @Test
    public void testGetBytesUtf16_test3_decomposed() throws UnsupportedEncodingException {
        final String charsetName = "UTF-16";
        testGetBytesUnchecked(charsetName);
        final byte[] expected = STRING_FIXTURE.getBytes(charsetName);
        final byte[] actual = StringUtils.getBytesUtf16(STRING_FIXTURE);
        Assert.assertArrayEquals(expected, actual);
    }

    @Test
    public void testGetBytesUtf16Be_test0_decomposed() throws UnsupportedEncodingException {
        final String charsetName = "UTF-16BE";
        testGetBytesUnchecked(charsetName);
    }

    @Test
    public void testGetBytesUtf16Be_test1_decomposed() throws UnsupportedEncodingException {
        final String charsetName = "UTF-16BE";
        testGetBytesUnchecked(charsetName);
        final byte[] expected = STRING_FIXTURE.getBytes(charsetName);
    }

    @Test
    public void testGetBytesUtf16Be_test2_decomposed() throws UnsupportedEncodingException {
        final String charsetName = "UTF-16BE";
        testGetBytesUnchecked(charsetName);
        final byte[] expected = STRING_FIXTURE.getBytes(charsetName);
        final byte[] actual = StringUtils.getBytesUtf16Be(STRING_FIXTURE);
    }

    @Test
    public void testGetBytesUtf16Be_test3_decomposed() throws UnsupportedEncodingException {
        final String charsetName = "UTF-16BE";
        testGetBytesUnchecked(charsetName);
        final byte[] expected = STRING_FIXTURE.getBytes(charsetName);
        final byte[] actual = StringUtils.getBytesUtf16Be(STRING_FIXTURE);
        Assert.assertArrayEquals(expected, actual);
    }

    @Test
    public void testGetBytesUtf16Le_test0_decomposed() throws UnsupportedEncodingException {
        final String charsetName = "UTF-16LE";
        testGetBytesUnchecked(charsetName);
    }

    @Test
    public void testGetBytesUtf16Le_test1_decomposed() throws UnsupportedEncodingException {
        final String charsetName = "UTF-16LE";
        testGetBytesUnchecked(charsetName);
        final byte[] expected = STRING_FIXTURE.getBytes(charsetName);
    }

    @Test
    public void testGetBytesUtf16Le_test2_decomposed() throws UnsupportedEncodingException {
        final String charsetName = "UTF-16LE";
        testGetBytesUnchecked(charsetName);
        final byte[] expected = STRING_FIXTURE.getBytes(charsetName);
        final byte[] actual = StringUtils.getBytesUtf16Le(STRING_FIXTURE);
    }

    @Test
    public void testGetBytesUtf16Le_test3_decomposed() throws UnsupportedEncodingException {
        final String charsetName = "UTF-16LE";
        testGetBytesUnchecked(charsetName);
        final byte[] expected = STRING_FIXTURE.getBytes(charsetName);
        final byte[] actual = StringUtils.getBytesUtf16Le(STRING_FIXTURE);
        Assert.assertArrayEquals(expected, actual);
    }

    @Test
    public void testGetBytesUtf8_test0_decomposed() throws UnsupportedEncodingException {
        final String charsetName = "UTF-8";
        testGetBytesUnchecked(charsetName);
    }

    @Test
    public void testGetBytesUtf8_test1_decomposed() throws UnsupportedEncodingException {
        final String charsetName = "UTF-8";
        testGetBytesUnchecked(charsetName);
        final byte[] expected = STRING_FIXTURE.getBytes(charsetName);
    }

    @Test
    public void testGetBytesUtf8_test2_decomposed() throws UnsupportedEncodingException {
        final String charsetName = "UTF-8";
        testGetBytesUnchecked(charsetName);
        final byte[] expected = STRING_FIXTURE.getBytes(charsetName);
        final byte[] actual = StringUtils.getBytesUtf8(STRING_FIXTURE);
    }

    @Test
    public void testGetBytesUtf8_test3_decomposed() throws UnsupportedEncodingException {
        final String charsetName = "UTF-8";
        testGetBytesUnchecked(charsetName);
        final byte[] expected = STRING_FIXTURE.getBytes(charsetName);
        final byte[] actual = StringUtils.getBytesUtf8(STRING_FIXTURE);
        Assert.assertArrayEquals(expected, actual);
    }

    @Test
    public void testGetBytesUncheckedBadName_test0_decomposed()  {
        try {
            StringUtils.getBytesUnchecked(STRING_FIXTURE, "UNKNOWN");
            Assert.fail("Expected " + IllegalStateException.class.getName());
        } catch (final IllegalStateException e) {
        }
    }

    @Test
    public void testGetBytesUncheckedNullInput_test0_decomposed()  {
        Assert.assertNull(StringUtils.getBytesUnchecked(null, "UNKNOWN"));
    }

    @Test
    public void testNewStringBadEnc_test0_decomposed()  {
        try {
            StringUtils.newString1(BYTES_FIXTURE, "UNKNOWN");
            Assert.fail("Expected " + IllegalStateException.class.getName());
        } catch (final IllegalStateException e) {
        }
    }

    @Test
    public void testNewStringNullInput_test0_decomposed()  {
        Assert.assertNull(StringUtils.newString1(null, "UNKNOWN"));
    }

    @Test
    public void testNewStringNullInput_CODEC229_test0_decomposed()  {
        Assert.assertNull(StringUtils.newStringUtf8(null));
    }

    @Test
    public void testNewStringNullInput_CODEC229_test1_decomposed()  {
        Assert.assertNull(StringUtils.newStringUtf8(null));
        Assert.assertNull(StringUtils.newStringIso8859_1(null));
    }

    @Test
    public void testNewStringNullInput_CODEC229_test2_decomposed()  {
        Assert.assertNull(StringUtils.newStringUtf8(null));
        Assert.assertNull(StringUtils.newStringIso8859_1(null));
        Assert.assertNull(StringUtils.newStringUsAscii(null));
    }

    @Test
    public void testNewStringNullInput_CODEC229_test3_decomposed()  {
        Assert.assertNull(StringUtils.newStringUtf8(null));
        Assert.assertNull(StringUtils.newStringIso8859_1(null));
        Assert.assertNull(StringUtils.newStringUsAscii(null));
        Assert.assertNull(StringUtils.newStringUtf16(null));
    }

    @Test
    public void testNewStringNullInput_CODEC229_test4_decomposed()  {
        Assert.assertNull(StringUtils.newStringUtf8(null));
        Assert.assertNull(StringUtils.newStringIso8859_1(null));
        Assert.assertNull(StringUtils.newStringUsAscii(null));
        Assert.assertNull(StringUtils.newStringUtf16(null));
        Assert.assertNull(StringUtils.newStringUtf16Be(null));
    }

    @Test
    public void testNewStringNullInput_CODEC229_test5_decomposed()  {
        Assert.assertNull(StringUtils.newStringUtf8(null));
        Assert.assertNull(StringUtils.newStringIso8859_1(null));
        Assert.assertNull(StringUtils.newStringUsAscii(null));
        Assert.assertNull(StringUtils.newStringUtf16(null));
        Assert.assertNull(StringUtils.newStringUtf16Be(null));
        Assert.assertNull(StringUtils.newStringUtf16Le(null));
    }

    @Test
    public void testNewStringIso8859_1_test0_decomposed() throws UnsupportedEncodingException {
        final String charsetName = "ISO-8859-1";
        testNewString(charsetName);
    }

    @Test
    public void testNewStringIso8859_1_test1_decomposed() throws UnsupportedEncodingException {
        final String charsetName = "ISO-8859-1";
        testNewString(charsetName);
        final String expected = new String(BYTES_FIXTURE, charsetName);
        final String actual = StringUtils.newStringIso8859_1(BYTES_FIXTURE);
    }

    @Test
    public void testNewStringIso8859_1_test2_decomposed() throws UnsupportedEncodingException {
        final String charsetName = "ISO-8859-1";
        testNewString(charsetName);
        final String expected = new String(BYTES_FIXTURE, charsetName);
        final String actual = StringUtils.newStringIso8859_1(BYTES_FIXTURE);
        Assert.assertEquals(expected, actual);
    }

    @Test
    public void testNewStringUsAscii_test0_decomposed() throws UnsupportedEncodingException {
        final String charsetName = "US-ASCII";
        testNewString(charsetName);
    }

    @Test
    public void testNewStringUsAscii_test1_decomposed() throws UnsupportedEncodingException {
        final String charsetName = "US-ASCII";
        testNewString(charsetName);
        final String expected = new String(BYTES_FIXTURE, charsetName);
        final String actual = StringUtils.newStringUsAscii(BYTES_FIXTURE);
    }

    @Test
    public void testNewStringUsAscii_test2_decomposed() throws UnsupportedEncodingException {
        final String charsetName = "US-ASCII";
        testNewString(charsetName);
        final String expected = new String(BYTES_FIXTURE, charsetName);
        final String actual = StringUtils.newStringUsAscii(BYTES_FIXTURE);
        Assert.assertEquals(expected, actual);
    }

    @Test
    public void testNewStringUtf16_test0_decomposed() throws UnsupportedEncodingException {
        final String charsetName = "UTF-16";
        testNewString(charsetName);
    }

    @Test
    public void testNewStringUtf16_test1_decomposed() throws UnsupportedEncodingException {
        final String charsetName = "UTF-16";
        testNewString(charsetName);
        final String expected = new String(BYTES_FIXTURE, charsetName);
        final String actual = StringUtils.newStringUtf16(BYTES_FIXTURE);
    }

    @Test
    public void testNewStringUtf16_test2_decomposed() throws UnsupportedEncodingException {
        final String charsetName = "UTF-16";
        testNewString(charsetName);
        final String expected = new String(BYTES_FIXTURE, charsetName);
        final String actual = StringUtils.newStringUtf16(BYTES_FIXTURE);
        Assert.assertEquals(expected, actual);
    }

    @Test
    public void testNewStringUtf16Be_test0_decomposed() throws UnsupportedEncodingException {
        final String charsetName = "UTF-16BE";
        testNewString(charsetName);
    }

    @Test
    public void testNewStringUtf16Be_test1_decomposed() throws UnsupportedEncodingException {
        final String charsetName = "UTF-16BE";
        testNewString(charsetName);
        final String expected = new String(BYTES_FIXTURE_16BE, charsetName);
        final String actual = StringUtils.newStringUtf16Be(BYTES_FIXTURE_16BE);
    }

    @Test
    public void testNewStringUtf16Be_test2_decomposed() throws UnsupportedEncodingException {
        final String charsetName = "UTF-16BE";
        testNewString(charsetName);
        final String expected = new String(BYTES_FIXTURE_16BE, charsetName);
        final String actual = StringUtils.newStringUtf16Be(BYTES_FIXTURE_16BE);
        Assert.assertEquals(expected, actual);
    }

    @Test
    public void testNewStringUtf16Le_test0_decomposed() throws UnsupportedEncodingException {
        final String charsetName = "UTF-16LE";
        testNewString(charsetName);
    }

    @Test
    public void testNewStringUtf16Le_test1_decomposed() throws UnsupportedEncodingException {
        final String charsetName = "UTF-16LE";
        testNewString(charsetName);
        final String expected = new String(BYTES_FIXTURE_16LE, charsetName);
        final String actual = StringUtils.newStringUtf16Le(BYTES_FIXTURE_16LE);
    }

    @Test
    public void testNewStringUtf16Le_test2_decomposed() throws UnsupportedEncodingException {
        final String charsetName = "UTF-16LE";
        testNewString(charsetName);
        final String expected = new String(BYTES_FIXTURE_16LE, charsetName);
        final String actual = StringUtils.newStringUtf16Le(BYTES_FIXTURE_16LE);
        Assert.assertEquals(expected, actual);
    }

    @Test
    public void testNewStringUtf8_test0_decomposed() throws UnsupportedEncodingException {
        final String charsetName = "UTF-8";
        testNewString(charsetName);
    }

    @Test
    public void testNewStringUtf8_test1_decomposed() throws UnsupportedEncodingException {
        final String charsetName = "UTF-8";
        testNewString(charsetName);
        final String expected = new String(BYTES_FIXTURE, charsetName);
        final String actual = StringUtils.newStringUtf8(BYTES_FIXTURE);
    }

    @Test
    public void testNewStringUtf8_test2_decomposed() throws UnsupportedEncodingException {
        final String charsetName = "UTF-8";
        testNewString(charsetName);
        final String expected = new String(BYTES_FIXTURE, charsetName);
        final String actual = StringUtils.newStringUtf8(BYTES_FIXTURE);
        Assert.assertEquals(expected, actual);
    }

    @Test
    public void testEqualsString_test0_decomposed()  {
        Assert.assertTrue(StringUtils.equals(null, null));
        Assert.assertFalse(StringUtils.equals("abc", null));
        Assert.assertFalse(StringUtils.equals(null, "abc"));
        Assert.assertTrue(StringUtils.equals("abc", "abc"));
        Assert.assertFalse(StringUtils.equals("abc", "abcd"));
        Assert.assertFalse(StringUtils.equals("abcd", "abc"));
        Assert.assertFalse(StringUtils.equals("abc", "ABC"));
    }

    @Test
    public void testEqualsCS1_test0_decomposed()  {
        Assert.assertFalse(StringUtils.equals(new StringBuilder("abc"), null));
        Assert.assertFalse(StringUtils.equals(null, new StringBuilder("abc")));
        Assert.assertTrue(StringUtils.equals(new StringBuilder("abc"), new StringBuilder("abc")));
        Assert.assertFalse(StringUtils.equals(new StringBuilder("abc"), new StringBuilder("abcd")));
        Assert.assertFalse(StringUtils.equals(new StringBuilder("abcd"), new StringBuilder("abc")));
        Assert.assertFalse(StringUtils.equals(new StringBuilder("abc"), new StringBuilder("ABC")));
    }

    @Test
    public void testEqualsCS2_test0_decomposed()  {
        Assert.assertTrue(StringUtils.equals("abc", new StringBuilder("abc")));
        Assert.assertFalse(StringUtils.equals(new StringBuilder("abc"), "abcd"));
        Assert.assertFalse(StringUtils.equals("abcd", new StringBuilder("abc")));
        Assert.assertFalse(StringUtils.equals(new StringBuilder("abc"), "ABC"));
    }

    @Test
    public void testByteBufferUtf8_test0_decomposed()  {
        Assert.assertNull("Should be null safe", StringUtils.getByteBufferUtf8(null));
    }

    @Test
    public void testByteBufferUtf8_test1_decomposed()  {
        Assert.assertNull("Should be null safe", StringUtils.getByteBufferUtf8(null));
        final String text = "asdhjfhsadiogasdjhagsdygfjasfgsdaksjdhfk";
        final ByteBuffer bb = StringUtils.getByteBufferUtf8(text);
    }

    @Test
    public void testByteBufferUtf8_test2_decomposed()  {
        Assert.assertNull("Should be null safe", StringUtils.getByteBufferUtf8(null));
        final String text = "asdhjfhsadiogasdjhagsdygfjasfgsdaksjdhfk";
        final ByteBuffer bb = StringUtils.getByteBufferUtf8(text);
        Assert.assertArrayEquals(text.getBytes(StandardCharsets.UTF_8), bb.array());
    }
}