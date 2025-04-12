
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


package org.apache.commons.codec.binary;

import static org.junit.Assert.assertArrayEquals;
import static org.junit.Assert.assertEquals;
import static org.junit.Assert.assertFalse;
import static org.junit.Assert.assertNull;
import static org.junit.Assert.assertTrue;
import static org.junit.Assert.fail;

import org.apache.commons.codec.CodecPolicy;
import org.apache.commons.codec.DecoderException;
import org.apache.commons.codec.EncoderException;
import org.junit.Test;

import java.nio.charset.Charset;
import java.nio.charset.StandardCharsets;
import java.util.Random;

/**
 * Test cases for Base16 class.
 *
 * @since 1.15
 */
public class Base16Test {

    private static final Charset CHARSET_UTF8 = StandardCharsets.UTF_8;

    private final Random random = new Random();

    /**
     * @return Returns the random.
     */
    public Random getRandom() {
        return this.random;
    }

    /** Test the Base16 implementation */
    @Test
    public void testBase16() {
        final String content = "Hello World";
        final byte[] encodedBytes = Base16.Base162().encode0(StringUtils.getBytesUtf8(content));
        final String encodedContent = StringUtils.newStringUtf8(encodedBytes);
        assertEquals("encoding hello world", "48656C6C6F20576F726C64", encodedContent);

        final byte[] decodedBytes = Base16.Base162().decode0(encodedBytes);
        final String decodedContent = StringUtils.newStringUtf8(decodedBytes);
        assertEquals("decoding hello world", content, decodedContent);
    }

    /** isBase16 throws RuntimeException on some non-Base16 bytes */
    @Test(expected = RuntimeException.class)
    public void testCodec68() {
        final byte[] x = {'n', 'H', '=', '=', (byte) 0x9c};
        final Base16 b16 = Base16.Base162();
        b16.decode0(x);
    }

    @Test
    public void testConstructors() {
        Base16.Base162();
        Base16.Base161(false);
        Base16.Base161(true);
        new Base16(false, CodecPolicy.LENIENT);
        new Base16(false, CodecPolicy.STRICT);
    }

    @Test
    public void testConstructor_LowerCase() {
        final Base16 base16 = Base16.Base161(true);
        final byte[] encoded = base16.encode0(BaseNTestData.DECODED);
        final String expectedResult = Base16TestData.ENCODED_UTF8_LOWERCASE;
        final String result = StringUtils.newStringUtf8(encoded);
        assertEquals("new Base16(true)", expectedResult, result);
    }

    @Test
    public void testConstructor_LowerCase_DecodingPolicy() {
        final Base16 base16 = new Base16(false, CodecPolicy.STRICT);
        final byte[] encoded = base16.encode0(BaseNTestData.DECODED);
        final String expectedResult = Base16TestData.ENCODED_UTF8_UPPERCASE;
        final String result = StringUtils.newStringUtf8(encoded);
        assertEquals("new base16(false, CodecPolicy.STRICT)", result, expectedResult);
    }

    /** Test encode and decode of empty byte array. */
    @Test
    public void testEmptyBase16() {
        byte[] empty = {};
        byte[] result = Base16.Base162().encode0(empty);
        assertEquals("empty Base16 encode", 0, result.length);
        assertNull("empty Base16 encode", Base16.Base162().encode0(null));
        result = Base16.Base162().encode1(empty, 0, 1);
        assertEquals("empty Base16 encode with offset", 0, result.length);
        assertNull("empty Base16 encode with offset", Base16.Base162().encode0(null));

        empty = new byte[0];
        result = Base16.Base162().decode0(empty);
        assertEquals("empty Base16 decode", 0, result.length);
        assertNull("empty Base16 encode", Base16.Base162().decode0((byte[]) null));
    }

    @Test
    public void testEncodeDecodeRandom() {
        for (int i = 1; i < 5; i++) {
            final int len = this.getRandom().nextInt(10000) + 1;
            final byte[] data = new byte[len];
            this.getRandom().nextBytes(data);
            final byte[] enc = Base16.Base162().encode0(data);
            final byte[] data2 = Base16.Base162().decode0(enc);
            assertArrayEquals(data, data2);
        }
    }

    @Test
    public void testEncodeDecodeSmall() {
        for (int i = 0; i < 12; i++) {
            final byte[] data = new byte[i];
            this.getRandom().nextBytes(data);
            final byte[] enc = Base16.Base162().encode0(data);
            final byte[] data2 = Base16.Base162().decode0(enc);
            assertArrayEquals(toString(data) + " equals " + toString(data2), data, data2);
        }
    }

    @Test
    public void testKnownDecodings() {
        assertEquals(
                "The quick brown fox jumped over the lazy dogs.",
                new String(
                        Base16.Base161(true)
                                .decode0(
                                        "54686520717569636b2062726f776e20666f78206a756d706564206f76657220746865206c617a7920646f67732e"
                                                .getBytes(CHARSET_UTF8))));
        assertEquals(
                "It was the best of times, it was the worst of times.",
                new String(
                        Base16.Base161(true)
                                .decode0(
                                        "497420776173207468652062657374206f662074696d65732c206974207761732074686520776f727374206f662074696d65732e"
                                                .getBytes(CHARSET_UTF8))));
        assertEquals(
                "http://jakarta.apache.org/commmons",
                new String(
                        Base16.Base161(true)
                                .decode0(
                                        "687474703a2f2f6a616b617274612e6170616368652e6f72672f636f6d6d6d6f6e73"
                                                .getBytes(CHARSET_UTF8))));
        assertEquals(
                "AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz",
                new String(
                        Base16.Base161(true)
                                .decode0(
                                        "4161426243634464456546664767486849694a6a4b6b4c6c4d6d4e6e4f6f50705171527253735474557556765777587859795a7a"
                                                .getBytes(CHARSET_UTF8))));
        assertEquals(
                "{ 0, 1, 2, 3, 4, 5, 6, 7, 8, 9 }",
                new String(
                        Base16.Base161(true)
                                .decode0(
                                        "7b20302c20312c20322c20332c20342c20352c20362c20372c20382c2039207d"
                                                .getBytes(CHARSET_UTF8))));
        assertEquals(
                "xyzzy!",
                new String(Base16.Base161(true).decode0("78797a7a7921".getBytes(CHARSET_UTF8))));
    }

    @Test
    public void testKnownEncodings() {
        assertEquals(
                "54686520717569636b2062726f776e20666f78206a756d706564206f76657220746865206c617a7920646f67732e",
                new String(
                        Base16.Base161(true)
                                .encode0(
                                        "The quick brown fox jumped over the lazy dogs."
                                                .getBytes(CHARSET_UTF8))));
        assertEquals(
                "497420776173207468652062657374206f662074696d65732c206974207761732074686520776f727374206f662074696d65732e",
                new String(
                        Base16.Base161(true)
                                .encode0(
                                        "It was the best of times, it was the worst of times."
                                                .getBytes(CHARSET_UTF8))));
        assertEquals(
                "687474703a2f2f6a616b617274612e6170616368652e6f72672f636f6d6d6d6f6e73",
                new String(
                        Base16.Base161(true)
                                .encode0(
                                        "http://jakarta.apache.org/commmons"
                                                .getBytes(CHARSET_UTF8))));
        assertEquals(
                "4161426243634464456546664767486849694a6a4b6b4c6c4d6d4e6e4f6f50705171527253735474557556765777587859795a7a",
                new String(
                        Base16.Base161(true)
                                .encode0(
                                        "AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz"
                                                .getBytes(CHARSET_UTF8))));
        assertEquals(
                "7b20302c20312c20322c20332c20342c20352c20362c20372c20382c2039207d",
                new String(
                        Base16.Base161(true)
                                .encode0(
                                        "{ 0, 1, 2, 3, 4, 5, 6, 7, 8, 9 }"
                                                .getBytes(CHARSET_UTF8))));
        assertEquals(
                "78797a7a7921",
                new String(Base16.Base161(true).encode0("xyzzy!".getBytes(CHARSET_UTF8))));
    }

    @Test
    public void testNonBase16Test() {
        final byte[] invalidEncodedChars = {'/', ':', '@', 'G', '%', '`', 'g'};

        final byte[] encoded = new byte[1];
        for (final byte invalidEncodedChar : invalidEncodedChars) {
            try {
                encoded[0] = invalidEncodedChar;
                Base16.Base162().decode0(encoded);
                fail(
                        "IllegalArgumentException should have been thrown when trying to decode"
                                + " invalid Base16 char: "
                                + (char) invalidEncodedChar);
            } catch (final Exception e) {
                assertTrue(e instanceof IllegalArgumentException);
            }
        }
    }

    @Test
    public void testObjectDecodeWithInvalidParameter() {
        final Base16 b16 = Base16.Base162();

        try {
            b16.decode2(Integer.valueOf(5));
            fail("decode(Object) didn't throw an exception when passed an Integer object");
        } catch (final DecoderException e) {
        }
    }

    @Test
    public void testObjectDecodeWithValidParameter() throws Exception {
        final String original = "Hello World!";
        final Object o = Base16.Base162().encode0(original.getBytes(CHARSET_UTF8));

        final Base16 b16 = Base16.Base162();
        final Object oDecoded = b16.decode2(o);
        final byte[] baDecoded = (byte[]) oDecoded;
        final String dest = new String(baDecoded);

        assertEquals("dest string does not equal original", original, dest);
    }

    @Test
    public void testObjectEncodeWithInvalidParameter() {
        final Base16 b16 = Base16.Base162();
        try {
            b16.encode3("Yadayadayada");
            fail("encode(Object) didn't throw an exception when passed a String object");
        } catch (final EncoderException e) {
        }
    }

    @Test
    public void testObjectEncodeWithValidParameter() throws Exception {
        final String original = "Hello World!";
        final Object origObj = original.getBytes(CHARSET_UTF8);

        final Object oEncoded = Base16.Base162().encode3(origObj);
        final byte[] bArray = Base16.Base162().decode0((byte[]) oEncoded);
        final String dest = new String(bArray);

        assertEquals("dest string does not equal original", original, dest);
    }

    @Test
    public void testObjectEncode() {
        final Base16 b16 = Base16.Base162();
        assertEquals(
                "48656C6C6F20576F726C64",
                new String(b16.encode0("Hello World".getBytes(CHARSET_UTF8))));
    }

    @Test
    public void testPairs() {
        assertEquals("0000", new String(Base16.Base162().encode0(new byte[] {(byte) 0, (byte) 0})));
        assertEquals("0001", new String(Base16.Base162().encode0(new byte[] {(byte) 0, (byte) 1})));
        assertEquals("0002", new String(Base16.Base162().encode0(new byte[] {(byte) 0, (byte) 2})));
        assertEquals("0003", new String(Base16.Base162().encode0(new byte[] {(byte) 0, (byte) 3})));
        assertEquals("0004", new String(Base16.Base162().encode0(new byte[] {(byte) 0, (byte) 4})));
        assertEquals("0005", new String(Base16.Base162().encode0(new byte[] {(byte) 0, (byte) 5})));
        assertEquals("0006", new String(Base16.Base162().encode0(new byte[] {(byte) 0, (byte) 6})));
        assertEquals("0007", new String(Base16.Base162().encode0(new byte[] {(byte) 0, (byte) 7})));
        assertEquals("0008", new String(Base16.Base162().encode0(new byte[] {(byte) 0, (byte) 8})));
        assertEquals("0009", new String(Base16.Base162().encode0(new byte[] {(byte) 0, (byte) 9})));
        assertEquals(
                "000A", new String(Base16.Base162().encode0(new byte[] {(byte) 0, (byte) 10})));
        assertEquals(
                "000B", new String(Base16.Base162().encode0(new byte[] {(byte) 0, (byte) 11})));
        assertEquals(
                "000C", new String(Base16.Base162().encode0(new byte[] {(byte) 0, (byte) 12})));
        assertEquals(
                "000D", new String(Base16.Base162().encode0(new byte[] {(byte) 0, (byte) 13})));
        assertEquals(
                "000E", new String(Base16.Base162().encode0(new byte[] {(byte) 0, (byte) 14})));
        assertEquals(
                "000F", new String(Base16.Base162().encode0(new byte[] {(byte) 0, (byte) 15})));
        assertEquals(
                "0010", new String(Base16.Base162().encode0(new byte[] {(byte) 0, (byte) 16})));
        assertEquals(
                "0011", new String(Base16.Base162().encode0(new byte[] {(byte) 0, (byte) 17})));
        for (int i = -128; i <= 127; i++) {
            final byte test[] = {(byte) i, (byte) i};
            assertArrayEquals(test, Base16.Base162().decode0(Base16.Base162().encode0(test)));
        }
    }

    @Test
    public void testSingletons() {
        assertEquals("00", new String(Base16.Base162().encode0(new byte[] {(byte) 0})));
        assertEquals("01", new String(Base16.Base162().encode0(new byte[] {(byte) 1})));
        assertEquals("02", new String(Base16.Base162().encode0(new byte[] {(byte) 2})));
        assertEquals("03", new String(Base16.Base162().encode0(new byte[] {(byte) 3})));
        assertEquals("04", new String(Base16.Base162().encode0(new byte[] {(byte) 4})));
        assertEquals("05", new String(Base16.Base162().encode0(new byte[] {(byte) 5})));
        assertEquals("06", new String(Base16.Base162().encode0(new byte[] {(byte) 6})));
        assertEquals("07", new String(Base16.Base162().encode0(new byte[] {(byte) 7})));
        assertEquals("08", new String(Base16.Base162().encode0(new byte[] {(byte) 8})));
        assertEquals("09", new String(Base16.Base162().encode0(new byte[] {(byte) 9})));
        assertEquals("0A", new String(Base16.Base162().encode0(new byte[] {(byte) 10})));
        assertEquals("0B", new String(Base16.Base162().encode0(new byte[] {(byte) 11})));
        assertEquals("0C", new String(Base16.Base162().encode0(new byte[] {(byte) 12})));
        assertEquals("0D", new String(Base16.Base162().encode0(new byte[] {(byte) 13})));
        assertEquals("0E", new String(Base16.Base162().encode0(new byte[] {(byte) 14})));
        assertEquals("0F", new String(Base16.Base162().encode0(new byte[] {(byte) 15})));
        assertEquals("10", new String(Base16.Base162().encode0(new byte[] {(byte) 16})));
        assertEquals("11", new String(Base16.Base162().encode0(new byte[] {(byte) 17})));
        assertEquals("12", new String(Base16.Base162().encode0(new byte[] {(byte) 18})));
        assertEquals("13", new String(Base16.Base162().encode0(new byte[] {(byte) 19})));
        assertEquals("14", new String(Base16.Base162().encode0(new byte[] {(byte) 20})));
        assertEquals("15", new String(Base16.Base162().encode0(new byte[] {(byte) 21})));
        assertEquals("16", new String(Base16.Base162().encode0(new byte[] {(byte) 22})));
        assertEquals("17", new String(Base16.Base162().encode0(new byte[] {(byte) 23})));
        assertEquals("18", new String(Base16.Base162().encode0(new byte[] {(byte) 24})));
        assertEquals("19", new String(Base16.Base162().encode0(new byte[] {(byte) 25})));
        assertEquals("1A", new String(Base16.Base162().encode0(new byte[] {(byte) 26})));
        assertEquals("1B", new String(Base16.Base162().encode0(new byte[] {(byte) 27})));
        assertEquals("1C", new String(Base16.Base162().encode0(new byte[] {(byte) 28})));
        assertEquals("1D", new String(Base16.Base162().encode0(new byte[] {(byte) 29})));
        assertEquals("1E", new String(Base16.Base162().encode0(new byte[] {(byte) 30})));
        assertEquals("1F", new String(Base16.Base162().encode0(new byte[] {(byte) 31})));
        assertEquals("20", new String(Base16.Base162().encode0(new byte[] {(byte) 32})));
        assertEquals("21", new String(Base16.Base162().encode0(new byte[] {(byte) 33})));
        assertEquals("22", new String(Base16.Base162().encode0(new byte[] {(byte) 34})));
        assertEquals("23", new String(Base16.Base162().encode0(new byte[] {(byte) 35})));
        assertEquals("24", new String(Base16.Base162().encode0(new byte[] {(byte) 36})));
        assertEquals("25", new String(Base16.Base162().encode0(new byte[] {(byte) 37})));
        assertEquals("26", new String(Base16.Base162().encode0(new byte[] {(byte) 38})));
        assertEquals("27", new String(Base16.Base162().encode0(new byte[] {(byte) 39})));
        assertEquals("28", new String(Base16.Base162().encode0(new byte[] {(byte) 40})));
        assertEquals("29", new String(Base16.Base162().encode0(new byte[] {(byte) 41})));
        assertEquals("2A", new String(Base16.Base162().encode0(new byte[] {(byte) 42})));
        assertEquals("2B", new String(Base16.Base162().encode0(new byte[] {(byte) 43})));
        assertEquals("2C", new String(Base16.Base162().encode0(new byte[] {(byte) 44})));
        assertEquals("2D", new String(Base16.Base162().encode0(new byte[] {(byte) 45})));
        assertEquals("2E", new String(Base16.Base162().encode0(new byte[] {(byte) 46})));
        assertEquals("2F", new String(Base16.Base162().encode0(new byte[] {(byte) 47})));
        assertEquals("30", new String(Base16.Base162().encode0(new byte[] {(byte) 48})));
        assertEquals("31", new String(Base16.Base162().encode0(new byte[] {(byte) 49})));
        assertEquals("32", new String(Base16.Base162().encode0(new byte[] {(byte) 50})));
        assertEquals("33", new String(Base16.Base162().encode0(new byte[] {(byte) 51})));
        assertEquals("34", new String(Base16.Base162().encode0(new byte[] {(byte) 52})));
        assertEquals("35", new String(Base16.Base162().encode0(new byte[] {(byte) 53})));
        assertEquals("36", new String(Base16.Base162().encode0(new byte[] {(byte) 54})));
        assertEquals("37", new String(Base16.Base162().encode0(new byte[] {(byte) 55})));
        assertEquals("38", new String(Base16.Base162().encode0(new byte[] {(byte) 56})));
        assertEquals("39", new String(Base16.Base162().encode0(new byte[] {(byte) 57})));
        assertEquals("3A", new String(Base16.Base162().encode0(new byte[] {(byte) 58})));
        assertEquals("3B", new String(Base16.Base162().encode0(new byte[] {(byte) 59})));
        assertEquals("3C", new String(Base16.Base162().encode0(new byte[] {(byte) 60})));
        assertEquals("3D", new String(Base16.Base162().encode0(new byte[] {(byte) 61})));
        assertEquals("3E", new String(Base16.Base162().encode0(new byte[] {(byte) 62})));
        assertEquals("3F", new String(Base16.Base162().encode0(new byte[] {(byte) 63})));
        assertEquals("40", new String(Base16.Base162().encode0(new byte[] {(byte) 64})));
        assertEquals("41", new String(Base16.Base162().encode0(new byte[] {(byte) 65})));
        assertEquals("42", new String(Base16.Base162().encode0(new byte[] {(byte) 66})));
        assertEquals("43", new String(Base16.Base162().encode0(new byte[] {(byte) 67})));
        assertEquals("44", new String(Base16.Base162().encode0(new byte[] {(byte) 68})));
        assertEquals("45", new String(Base16.Base162().encode0(new byte[] {(byte) 69})));
        assertEquals("46", new String(Base16.Base162().encode0(new byte[] {(byte) 70})));
        assertEquals("47", new String(Base16.Base162().encode0(new byte[] {(byte) 71})));
        assertEquals("48", new String(Base16.Base162().encode0(new byte[] {(byte) 72})));
        assertEquals("49", new String(Base16.Base162().encode0(new byte[] {(byte) 73})));
        assertEquals("4A", new String(Base16.Base162().encode0(new byte[] {(byte) 74})));
        assertEquals("4B", new String(Base16.Base162().encode0(new byte[] {(byte) 75})));
        assertEquals("4C", new String(Base16.Base162().encode0(new byte[] {(byte) 76})));
        assertEquals("4D", new String(Base16.Base162().encode0(new byte[] {(byte) 77})));
        assertEquals("4E", new String(Base16.Base162().encode0(new byte[] {(byte) 78})));
        assertEquals("4F", new String(Base16.Base162().encode0(new byte[] {(byte) 79})));
        assertEquals("50", new String(Base16.Base162().encode0(new byte[] {(byte) 80})));
        assertEquals("51", new String(Base16.Base162().encode0(new byte[] {(byte) 81})));
        assertEquals("52", new String(Base16.Base162().encode0(new byte[] {(byte) 82})));
        assertEquals("53", new String(Base16.Base162().encode0(new byte[] {(byte) 83})));
        assertEquals("54", new String(Base16.Base162().encode0(new byte[] {(byte) 84})));
        assertEquals("55", new String(Base16.Base162().encode0(new byte[] {(byte) 85})));
        assertEquals("56", new String(Base16.Base162().encode0(new byte[] {(byte) 86})));
        assertEquals("57", new String(Base16.Base162().encode0(new byte[] {(byte) 87})));
        assertEquals("58", new String(Base16.Base162().encode0(new byte[] {(byte) 88})));
        assertEquals("59", new String(Base16.Base162().encode0(new byte[] {(byte) 89})));
        assertEquals("5A", new String(Base16.Base162().encode0(new byte[] {(byte) 90})));
        assertEquals("5B", new String(Base16.Base162().encode0(new byte[] {(byte) 91})));
        assertEquals("5C", new String(Base16.Base162().encode0(new byte[] {(byte) 92})));
        assertEquals("5D", new String(Base16.Base162().encode0(new byte[] {(byte) 93})));
        assertEquals("5E", new String(Base16.Base162().encode0(new byte[] {(byte) 94})));
        assertEquals("5F", new String(Base16.Base162().encode0(new byte[] {(byte) 95})));
        assertEquals("60", new String(Base16.Base162().encode0(new byte[] {(byte) 96})));
        assertEquals("61", new String(Base16.Base162().encode0(new byte[] {(byte) 97})));
        assertEquals("62", new String(Base16.Base162().encode0(new byte[] {(byte) 98})));
        assertEquals("63", new String(Base16.Base162().encode0(new byte[] {(byte) 99})));
        assertEquals("64", new String(Base16.Base162().encode0(new byte[] {(byte) 100})));
        assertEquals("65", new String(Base16.Base162().encode0(new byte[] {(byte) 101})));
        assertEquals("66", new String(Base16.Base162().encode0(new byte[] {(byte) 102})));
        assertEquals("67", new String(Base16.Base162().encode0(new byte[] {(byte) 103})));
        assertEquals("68", new String(Base16.Base162().encode0(new byte[] {(byte) 104})));
        for (int i = -128; i <= 127; i++) {
            final byte test[] = {(byte) i};
            assertArrayEquals(test, Base16.Base162().decode0(Base16.Base162().encode0(test)));
        }
    }

    @Test
    public void testTriplets() {
        assertEquals(
                "000000",
                new String(Base16.Base162().encode0(new byte[] {(byte) 0, (byte) 0, (byte) 0})));
        assertEquals(
                "000001",
                new String(Base16.Base162().encode0(new byte[] {(byte) 0, (byte) 0, (byte) 1})));
        assertEquals(
                "000002",
                new String(Base16.Base162().encode0(new byte[] {(byte) 0, (byte) 0, (byte) 2})));
        assertEquals(
                "000003",
                new String(Base16.Base162().encode0(new byte[] {(byte) 0, (byte) 0, (byte) 3})));
        assertEquals(
                "000004",
                new String(Base16.Base162().encode0(new byte[] {(byte) 0, (byte) 0, (byte) 4})));
        assertEquals(
                "000005",
                new String(Base16.Base162().encode0(new byte[] {(byte) 0, (byte) 0, (byte) 5})));
        assertEquals(
                "000006",
                new String(Base16.Base162().encode0(new byte[] {(byte) 0, (byte) 0, (byte) 6})));
        assertEquals(
                "000007",
                new String(Base16.Base162().encode0(new byte[] {(byte) 0, (byte) 0, (byte) 7})));
        assertEquals(
                "000008",
                new String(Base16.Base162().encode0(new byte[] {(byte) 0, (byte) 0, (byte) 8})));
        assertEquals(
                "000009",
                new String(Base16.Base162().encode0(new byte[] {(byte) 0, (byte) 0, (byte) 9})));
        assertEquals(
                "00000A",
                new String(Base16.Base162().encode0(new byte[] {(byte) 0, (byte) 0, (byte) 10})));
        assertEquals(
                "00000B",
                new String(Base16.Base162().encode0(new byte[] {(byte) 0, (byte) 0, (byte) 11})));
        assertEquals(
                "00000C",
                new String(Base16.Base162().encode0(new byte[] {(byte) 0, (byte) 0, (byte) 12})));
        assertEquals(
                "00000D",
                new String(Base16.Base162().encode0(new byte[] {(byte) 0, (byte) 0, (byte) 13})));
        assertEquals(
                "00000E",
                new String(Base16.Base162().encode0(new byte[] {(byte) 0, (byte) 0, (byte) 14})));
        assertEquals(
                "00000F",
                new String(Base16.Base162().encode0(new byte[] {(byte) 0, (byte) 0, (byte) 15})));
    }

    @Test
    public void testByteToStringVariations() throws DecoderException {
        final Base16 base16 = Base16.Base162();
        final byte[] b1 = StringUtils.getBytesUtf8("Hello World");
        final byte[] b2 = {};
        final byte[] b3 = null;

        assertEquals(
                "byteToString Hello World", "48656C6C6F20576F726C64", base16.encodeToString(b1));
        assertEquals(
                "byteToString static Hello World",
                "48656C6C6F20576F726C64",
                StringUtils.newStringUtf8(Base16.Base162().encode0(b1)));
        assertEquals("byteToString \"\"", "", base16.encodeToString(b2));
        assertEquals(
                "byteToString static \"\"",
                "",
                StringUtils.newStringUtf8(Base16.Base162().encode0(b2)));
        assertNull("byteToString null", base16.encodeToString(b3));
        assertNull(
                "byteToString static null",
                StringUtils.newStringUtf8(Base16.Base162().encode0(b3)));
    }

    @Test
    public void testStringToByteVariations() throws DecoderException {
        final Base16 base16 = Base16.Base162();
        final String s1 = "48656C6C6F20576F726C64";
        final String s2 = "";
        final String s3 = null;

        assertEquals(
                "StringToByte Hello World",
                "Hello World",
                StringUtils.newStringUtf8(base16.decode3(s1)));
        assertEquals(
                "StringToByte Hello World",
                "Hello World",
                StringUtils.newStringUtf8((byte[]) Base16.Base162().decode2((Object) s1)));
        assertEquals(
                "StringToByte static Hello World",
                "Hello World",
                StringUtils.newStringUtf8(Base16.Base162().decode3(s1)));
        assertEquals(
                "StringToByte \"\"", "", StringUtils.newStringUtf8(Base16.Base162().decode3(s2)));
        assertEquals(
                "StringToByte static \"\"",
                "",
                StringUtils.newStringUtf8(Base16.Base162().decode3(s2)));
        assertNull("StringToByte null", StringUtils.newStringUtf8(Base16.Base162().decode3(s3)));
        assertNull(
                "StringToByte static null",
                StringUtils.newStringUtf8(Base16.Base162().decode3(s3)));
    }

    private String toString(final byte[] data) {
        final StringBuilder buf = new StringBuilder();
        for (int i = 0; i < data.length; i++) {
            buf.append(data[i]);
            if (i != data.length - 1) {
                buf.append(",");
            }
        }
        return buf.toString();
    }

    @Test(expected = IllegalArgumentException.class)
    public void checkEncodeLengthBounds() {
        final Base16 base16 = Base16.Base162();
        base16.encode1(new byte[10], 0, 1 << 30);
    }

    @Test
    public void testIsInAlphabet() {
        Base16 b16 = Base16.Base161(true);
        assertFalse(b16.isInAlphabet0((byte) 0));
        assertFalse(b16.isInAlphabet0((byte) 1));
        assertFalse(b16.isInAlphabet0((byte) -1));
        assertFalse(b16.isInAlphabet0((byte) -15));
        assertFalse(b16.isInAlphabet0((byte) -16));
        assertFalse(b16.isInAlphabet0((byte) 128));
        assertFalse(b16.isInAlphabet0((byte) 255));

        b16 = Base16.Base161(true);
        for (char c = '0'; c <= '9'; c++) {
            assertTrue(b16.isInAlphabet0((byte) c));
        }
        for (char c = 'a'; c <= 'f'; c++) {
            assertTrue(b16.isInAlphabet0((byte) c));
        }
        for (char c = 'A'; c <= 'F'; c++) {
            assertFalse(b16.isInAlphabet0((byte) c));
        }
        assertFalse(b16.isInAlphabet0((byte) ('0' - 1)));
        assertFalse(b16.isInAlphabet0((byte) ('9' + 1)));
        assertFalse(b16.isInAlphabet0((byte) ('a' - 1)));
        assertFalse(b16.isInAlphabet0((byte) ('f' + 1)));
        assertFalse(b16.isInAlphabet0((byte) ('z' + 1)));

        b16 = Base16.Base161(false);
        for (char c = '0'; c <= '9'; c++) {
            assertTrue(b16.isInAlphabet0((byte) c));
        }
        for (char c = 'a'; c <= 'f'; c++) {
            assertFalse(b16.isInAlphabet0((byte) c));
        }
        for (char c = 'A'; c <= 'F'; c++) {
            assertTrue(b16.isInAlphabet0((byte) c));
        }
        assertFalse(b16.isInAlphabet0((byte) ('0' - 1)));
        assertFalse(b16.isInAlphabet0((byte) ('9' + 1)));
        assertFalse(b16.isInAlphabet0((byte) ('A' - 1)));
        assertFalse(b16.isInAlphabet0((byte) ('F' + 1)));
        assertFalse(b16.isInAlphabet0((byte) ('Z' + 1)));
    }

    @Test
    public void testDecodeSingleBytes() {
        final String encoded = "556E74696C206E6578742074696D6521";

        final BaseNCodec.Context context = new BaseNCodec.Context();
        final Base16 b16 = Base16.Base162();

        final byte[] encocdedBytes = StringUtils.getBytesUtf8(encoded);

        b16.decode1(encocdedBytes, 0, 1, context);
        b16.decode1(encocdedBytes, 1, 1, context); // yields "U"
        b16.decode1(encocdedBytes, 2, 1, context);
        b16.decode1(encocdedBytes, 3, 1, context); // yields "n"

        b16.decode1(encocdedBytes, 4, 3, context); // yields "t"
        b16.decode1(encocdedBytes, 7, 3, context); // yields "il"
        b16.decode1(encocdedBytes, 10, 3, context); // yields " "

        b16.decode1(encocdedBytes, 13, 19, context); // yields "next time!"

        final byte[] decodedBytes = new byte[context.pos];
        System.arraycopy(context.buffer, context.readPos, decodedBytes, 0, decodedBytes.length);
        final String decoded = StringUtils.newStringUtf8(decodedBytes);

        assertEquals("Until next time!", decoded);
    }

    @Test
    public void testDecodeSingleBytesOptimisation() {
        final BaseNCodec.Context context = new BaseNCodec.Context();
        assertEquals(0, context.ibitWorkArea);
        assertNull(context.buffer);

        final byte[] data = new byte[1];

        final Base16 b16 = Base16.Base162();

        data[0] = (byte) 'E';
        b16.decode1(data, 0, 1, context);
        assertEquals(15, context.ibitWorkArea);
        assertNull(context.buffer);

        data[0] = (byte) 'F';
        b16.decode1(data, 0, 1, context);
        assertEquals(0, context.ibitWorkArea);

        assertEquals((byte) 0xEF, context.buffer[0]);
    }

    @Test(expected = IllegalArgumentException.class)
    public void testStrictDecoding() {
        final String encoded =
                "aabbccdde"; // Note the trailing `e` which does not make up a hex-pair and so is

        final Base16 b16 = new Base16(true, CodecPolicy.STRICT);
        assertEquals(CodecPolicy.STRICT, b16.getCodecPolicy());
        b16.decode0(StringUtils.getBytesUtf8(encoded));
    }

    @Test
    public void testLenientDecoding() {
        final String encoded =
                "aabbccdde"; // Note the trailing `e` which does not make up a hex-pair and so is

        final Base16 b16 = new Base16(true, CodecPolicy.LENIENT);
        assertEquals(CodecPolicy.LENIENT, b16.getCodecPolicy());

        final byte[] decoded = b16.decode0(StringUtils.getBytesUtf8(encoded));
        assertArrayEquals(new byte[] {(byte) 0xaa, (byte) 0xbb, (byte) 0xcc, (byte) 0xdd}, decoded);
    }
}
