
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
import static org.junit.Assert.assertNotNull;
import static org.junit.Assert.assertNull;
import static org.junit.Assert.assertTrue;
import static org.junit.Assert.fail;

import org.apache.commons.codec.CodecPolicy;
import org.apache.commons.codec.DecoderException;
import org.apache.commons.codec.EncoderException;
import org.junit.Assume;
import org.junit.Test;

import java.math.BigInteger;
import java.nio.charset.Charset;
import java.nio.charset.StandardCharsets;
import java.util.Arrays;
import java.util.Random;

/**
 * Test cases for Base64 class.
 *
 * @see <a href="http://www.ietf.org/rfc/rfc2045.txt">RFC 2045</a>
 */
public class Base64Test {

    private static final Charset CHARSET_UTF8 = StandardCharsets.UTF_8;

    /**
     * Example test cases with valid characters but impossible combinations of trailing characters
     * (i.e. cannot be created during encoding).
     */
    static final String[] BASE64_IMPOSSIBLE_CASES = {
        "ZE==", "ZmC=", "Zm9vYE==", "Zm9vYmC=", "AB",
    };

    /**
     * Copy of the standard base-64 encoding table. Used to test decoding the final character of
     * encoded bytes.
     */
    private static final byte[] STANDARD_ENCODE_TABLE = {
        'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
        'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',
        'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
        'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
        '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '+', '/'
    };

    private final Random random = new Random();

    /**
     * @return Returns the random.
     */
    public Random getRandom() {
        return this.random;
    }

    /** Test the isStringBase64 method. */
    @Test
    public void testIsStringBase64() {
        final String nullString = null;
        final String emptyString = "";
        final String validString =
                "abc===defg\n\r123456\r789\r\rABC\n\nDEF==GHI\r\nJKL==============";
        final String invalidString = validString + (char) 0; // append null

        try {
            Base64.isBase642(nullString);
            fail("Base64.isStringBase64() should not be null-safe.");
        } catch (final NullPointerException npe) {
            assertNotNull("Base64.isStringBase64() should not be null-safe.", npe);
        }

        assertTrue("Base64.isStringBase64(empty-string) is true", Base64.isBase642(emptyString));
        assertTrue("Base64.isStringBase64(valid-string) is true", Base64.isBase642(validString));
        assertFalse(
                "Base64.isStringBase64(invalid-string) is false", Base64.isBase642(invalidString));
    }

    /** Test the Base64 implementation */
    @Test
    public void testBase64() {
        final String content = "Hello World";
        String encodedContent;
        byte[] encodedBytes = Base64.encodeBase640(StringUtils.getBytesUtf8(content));
        encodedContent = StringUtils.newStringUtf8(encodedBytes);
        assertEquals("encoding hello world", "SGVsbG8gV29ybGQ=", encodedContent);

        Base64 b64 = Base64.Base642(BaseNCodec.MIME_CHUNK_SIZE, null); // null
        encodedBytes = b64.encode0(StringUtils.getBytesUtf8(content));
        encodedContent = StringUtils.newStringUtf8(encodedBytes);
        assertEquals("encoding hello world", "SGVsbG8gV29ybGQ=", encodedContent);

        b64 = Base64.Base642(0, null); // null lineSeparator same as saying
        encodedBytes = b64.encode0(StringUtils.getBytesUtf8(content));
        encodedContent = StringUtils.newStringUtf8(encodedBytes);
        assertEquals("encoding hello world", "SGVsbG8gV29ybGQ=", encodedContent);

        final byte[] decode = b64.decode3("SGVsbG{\u00e9\u00e9\u00e9\u00e9\u00e9\u00e9}8gV29ybGQ=");
        final String decodeString = StringUtils.newStringUtf8(decode);
        assertEquals("decode hello world", "Hello World", decodeString);
    }

    /**
     * Test our decode with pad character in the middle. (Our current implementation: halt decode
     * and return what we've got so far).
     *
     * <p>The point of this test is not to say "this is the correct way to decode base64." The point
     * is simply to keep us aware of the current logic since 1.4 so we don't accidentally break it
     * without realizing.
     *
     * <p>Note for historians. The 1.3 logic would decode to: "Hello World\u0000Hello World" -- null
     * in the middle --- and 1.4 unwittingly changed it to current logic.
     */
    @Test
    public void testDecodeWithInnerPad() {
        final String content = "SGVsbG8gV29ybGQ=SGVsbG8gV29ybGQ=";
        final byte[] result = Base64.decodeBase641(content);
        final byte[] shouldBe = StringUtils.getBytesUtf8("Hello World");
        assertArrayEquals("decode should halt at pad (=)", result, shouldBe);
    }

    /** Tests Base64.encodeBase64(). */
    @Test
    public void testChunkedEncodeMultipleOf76() {
        final byte[] expectedEncode = Base64.encodeBase641(BaseNTestData.DECODED, true);
        final String actualResult = Base64TestData.ENCODED_76_CHARS_PER_LINE.replace("\n", "\r\n");
        final byte[] actualEncode = StringUtils.getBytesUtf8(actualResult);
        assertArrayEquals("chunkedEncodeMultipleOf76", expectedEncode, actualEncode);
    }

    /** CODEC-68: isBase64 throws ArrayIndexOutOfBoundsException on some non-BASE64 bytes */
    @Test
    public void testCodec68() {
        final byte[] x = {'n', 'A', '=', '=', (byte) 0x9c};
        Base64.decodeBase640(x);
    }

    @Test
    public void testCodeInteger1() {
        final String encodedInt1 = "li7dzDacuo67Jg7mtqEm2TRuOMU=";
        final BigInteger bigInt1 =
                new BigInteger("85739377120809420210425962799" + "0318636601332086981");

        assertEquals(encodedInt1, new String(Base64.encodeInteger(bigInt1)));
        assertEquals(bigInt1, Base64.decodeInteger(encodedInt1.getBytes(CHARSET_UTF8)));
    }

    @Test
    public void testCodeInteger2() {
        final String encodedInt2 = "9B5ypLY9pMOmtxCeTDHgwdNFeGs=";
        final BigInteger bigInt2 =
                new BigInteger("13936727572861167254666467268" + "91466679477132949611");

        assertEquals(encodedInt2, new String(Base64.encodeInteger(bigInt2)));
        assertEquals(bigInt2, Base64.decodeInteger(encodedInt2.getBytes(CHARSET_UTF8)));
    }

    @Test
    public void testCodeInteger3() {
        final String encodedInt3 =
                "FKIhdgaG5LGKiEtF1vHy4f3y700zaD6QwDS3IrNVGzNp2"
                        + "rY+1LFWTK6D44AyiC1n8uWz1itkYMZF0/aKDK0Yjg==";
        final BigInteger bigInt3 =
                new BigInteger(
                        "10806548154093873461951748545"
                            + "1196989136416448805819079363524309897749044958112417136240557"
                            + "4495062430572478766856090958495998158114332651671116876320938126");

        assertEquals(encodedInt3, new String(Base64.encodeInteger(bigInt3)));
        assertEquals(bigInt3, Base64.decodeInteger(encodedInt3.getBytes(CHARSET_UTF8)));
    }

    @Test
    public void testCodeInteger4() {
        final String encodedInt4 =
                "ctA8YGxrtngg/zKVvqEOefnwmViFztcnPBYPlJsvh6yKI"
                        + "4iDm68fnp4Mi3RrJ6bZAygFrUIQLxLjV+OJtgJAEto0xAs+Mehuq1DkSFEpP3o"
                        + "DzCTOsrOiS1DwQe4oIb7zVk/9l7aPtJMHW0LVlMdwZNFNNJoqMcT2ZfCPrfvYv"
                        + "Q0=";
        final BigInteger bigInt4 =
                new BigInteger(
                        "80624726256040348115552042320"
                                + "6968135001872753709424419772586693950232350200555646471175944"
                                + "519297087885987040810778908507262272892702303774422853675597"
                                + "748008534040890923814202286633163248086055216976551456088015"
                                + "338880713818192088877057717530169381044092839402438015097654"
                                + "53542091716518238707344493641683483917");

        assertEquals(encodedInt4, new String(Base64.encodeInteger(bigInt4)));
        assertEquals(bigInt4, Base64.decodeInteger(encodedInt4.getBytes(CHARSET_UTF8)));
    }

    @Test
    public void testCodeIntegerEdgeCases() {}

    @Test
    public void testCodeIntegerNull() {
        try {
            Base64.encodeInteger(null);
            fail("Exception not thrown when passing in null to encodeInteger(BigInteger)");
        } catch (final NullPointerException npe) {
        } catch (final Exception e) {
            fail("Incorrect Exception caught when passing in null to encodeInteger(BigInteger)");
        }
    }

    @Test
    public void testConstructors() {
        Base64 base64;
        base64 = Base64.Base645();
        base64 = Base64.Base643(-1);
        base64 = Base64.Base642(-1, new byte[] {});
        base64 = Base64.Base642(64, new byte[] {});
        try {
            base64 = Base64.Base642(-1, new byte[] {'A'}); // TODO do we need to
            fail("Should have rejected attempt to use 'A' as a line separator");
        } catch (final IllegalArgumentException ignored) {
        }
        try {
            base64 = Base64.Base642(64, new byte[] {'A'});
            fail("Should have rejected attempt to use 'A' as a line separator");
        } catch (final IllegalArgumentException ignored) {
        }
        try {
            base64 = Base64.Base642(64, new byte[] {'='});
            fail("Should have rejected attempt to use '=' as a line separator");
        } catch (final IllegalArgumentException ignored) {
        }
        base64 = Base64.Base642(64, new byte[] {'$'}); // OK
        try {
            base64 = Base64.Base642(64, new byte[] {'A', '$'});
            fail("Should have rejected attempt to use 'A$' as a line separator");
        } catch (final IllegalArgumentException ignored) {
        }
        base64 = Base64.Base642(64, new byte[] {' ', '$', '\n', '\r', '\t'}); // OK
        assertNotNull(base64);
    }

    @Test
    public void testConstructor_Int_ByteArray_Boolean() {
        final Base64 base64 = Base64.Base641(65, new byte[] {'\t'}, false);
        final byte[] encoded = base64.encode0(BaseNTestData.DECODED);
        String expectedResult = Base64TestData.ENCODED_64_CHARS_PER_LINE;
        expectedResult = expectedResult.replace('\n', '\t');
        final String result = StringUtils.newStringUtf8(encoded);
        assertEquals("new Base64(65, \\t, false)", expectedResult, result);
    }

    @Test
    public void testConstructor_Int_ByteArray_Boolean_UrlSafe() {
        final Base64 base64 = Base64.Base641(64, new byte[] {'\t'}, true);
        final byte[] encoded = base64.encode0(BaseNTestData.DECODED);
        String expectedResult = Base64TestData.ENCODED_64_CHARS_PER_LINE;
        expectedResult = expectedResult.replace("=", ""); // url-safe has no
        expectedResult = expectedResult.replace('\n', '\t');
        expectedResult = expectedResult.replace('+', '-');
        expectedResult = expectedResult.replace('/', '_');
        final String result = StringUtils.newStringUtf8(encoded);
        assertEquals("new Base64(64, \\t, true)", result, expectedResult);
    }

    /** Tests conditional true branch for "marker0" test. */
    @Test
    public void testDecodePadMarkerIndex2() {
        assertEquals("A", new String(Base64.decodeBase640("QQ==".getBytes(CHARSET_UTF8))));
    }

    /** Tests conditional branches for "marker1" test. */
    @Test
    public void testDecodePadMarkerIndex3() {
        assertEquals("AA", new String(Base64.decodeBase640("QUE=".getBytes(CHARSET_UTF8))));
        assertEquals("AAA", new String(Base64.decodeBase640("QUFB".getBytes(CHARSET_UTF8))));
    }

    @Test
    public void testDecodePadOnly() {
        assertEquals(0, Base64.decodeBase640("====".getBytes(CHARSET_UTF8)).length);
        assertEquals("", new String(Base64.decodeBase640("====".getBytes(CHARSET_UTF8))));
        assertEquals(0, Base64.decodeBase640("===".getBytes(CHARSET_UTF8)).length);
        assertEquals(0, Base64.decodeBase640("==".getBytes(CHARSET_UTF8)).length);
        assertEquals(0, Base64.decodeBase640("=".getBytes(CHARSET_UTF8)).length);
        assertEquals(0, Base64.decodeBase640("".getBytes(CHARSET_UTF8)).length);
    }

    @Test
    public void testDecodePadOnlyChunked() {
        assertEquals(0, Base64.decodeBase640("====\n".getBytes(CHARSET_UTF8)).length);
        assertEquals("", new String(Base64.decodeBase640("====\n".getBytes(CHARSET_UTF8))));
        assertEquals(0, Base64.decodeBase640("===\n".getBytes(CHARSET_UTF8)).length);
        assertEquals(0, Base64.decodeBase640("==\n".getBytes(CHARSET_UTF8)).length);
        assertEquals(0, Base64.decodeBase640("=\n".getBytes(CHARSET_UTF8)).length);
        assertEquals(0, Base64.decodeBase640("\n".getBytes(CHARSET_UTF8)).length);
    }

    @Test
    public void testDecodeWithWhitespace() throws Exception {

        final String orig = "I am a late night coder.";

        final byte[] encodedArray = Base64.encodeBase640(orig.getBytes(CHARSET_UTF8));
        final StringBuilder intermediate = new StringBuilder(new String(encodedArray));

        intermediate.insert(2, ' ');
        intermediate.insert(5, '\t');
        intermediate.insert(10, '\r');
        intermediate.insert(15, '\n');

        final byte[] encodedWithWS = intermediate.toString().getBytes(CHARSET_UTF8);
        final byte[] decodedWithWS = Base64.decodeBase640(encodedWithWS);

        final String dest = new String(decodedWithWS);

        assertEquals("Dest string doesn't equal the original", orig, dest);
    }

    /** Test encode and decode of empty byte array. */
    @Test
    public void testEmptyBase64() {
        byte[] empty = {};
        byte[] result = Base64.encodeBase640(empty);
        assertEquals("empty base64 encode", 0, result.length);
        assertNull("empty base64 encode", Base64.encodeBase640(null));
        result = Base64.Base645().encode1(empty, 0, 1);
        assertEquals("empty base64 encode", 0, result.length);
        assertNull("empty base64 encode", Base64.Base645().encode1(null, 0, 1));

        empty = new byte[0];
        result = Base64.decodeBase640(empty);
        assertEquals("empty base64 decode", 0, result.length);
        assertNull("empty base64 encode", Base64.decodeBase640((byte[]) null));
    }

    @Test
    public void testEncodeDecodeRandom() {
        for (int i = 1; i < 5; i++) {
            final byte[] data = new byte[this.getRandom().nextInt(10000) + 1];
            this.getRandom().nextBytes(data);
            final byte[] enc = Base64.encodeBase640(data);
            assertTrue(Base64.isBase641(enc));
            final byte[] data2 = Base64.decodeBase640(enc);
            assertArrayEquals(data, data2);
        }
    }

    @Test
    public void testEncodeDecodeSmall() {
        for (int i = 0; i < 12; i++) {
            final byte[] data = new byte[i];
            this.getRandom().nextBytes(data);
            final byte[] enc = Base64.encodeBase640(data);
            assertTrue("\"" + new String(enc) + "\" is Base64 data.", Base64.isBase641(enc));
            final byte[] data2 = Base64.decodeBase640(enc);
            assertArrayEquals(toString(data) + " equals " + toString(data2), data, data2);
        }
    }

    @Test
    public void testEncodeOverMaxSize0() throws Exception {
        testEncodeOverMaxSize1(-1);
        testEncodeOverMaxSize1(0);
        testEncodeOverMaxSize1(1);
        testEncodeOverMaxSize1(2);
    }

    @Test
    public void testCodec112() { // size calculation assumes always chunked
        final byte[] in = {0};
        final byte[] out = Base64.encodeBase640(in);
        Base64.encodeBase643(in, false, false, out.length);
    }

    private void testEncodeOverMaxSize1(final int maxSize) throws Exception {
        try {
            Base64.encodeBase643(BaseNTestData.DECODED, true, false, maxSize);
            fail("Expected " + IllegalArgumentException.class.getName());
        } catch (final IllegalArgumentException e) {
        }
    }

    @Test
    public void testIgnoringNonBase64InDecode() throws Exception {
        assertEquals(
                "The quick brown fox jumped over the lazy dogs.",
                new String(
                        Base64.decodeBase640(
                                "VGhlIH@$#$@%F1aWN@#@#@@rIGJyb3duIGZve\n\r\t%#%#%#%CBqd##$#$W1wZWQgb3ZlciB0aGUgbGF6eSBkb2dzLg=="
                                        .getBytes(CHARSET_UTF8))));
    }

    @Test
    public void testIsArrayByteBase64() {
        assertFalse(Base64.isBase641(new byte[] {Byte.MIN_VALUE}));
        assertFalse(Base64.isBase641(new byte[] {-125}));
        assertFalse(Base64.isBase641(new byte[] {-10}));
        assertFalse(Base64.isBase641(new byte[] {0}));
        assertFalse(Base64.isBase641(new byte[] {64, Byte.MAX_VALUE}));
        assertFalse(Base64.isBase641(new byte[] {Byte.MAX_VALUE}));
        assertTrue(Base64.isBase641(new byte[] {'A'}));
        assertFalse(Base64.isBase641(new byte[] {'A', Byte.MIN_VALUE}));
        assertTrue(Base64.isBase641(new byte[] {'A', 'Z', 'a'}));
        assertTrue(Base64.isBase641(new byte[] {'/', '=', '+'}));
        assertFalse(Base64.isBase641(new byte[] {'$'}));
    }

    /** Tests isUrlSafe. */
    @Test
    public void testIsUrlSafe() {
        final Base64 base64Standard = Base64.Base644(false);
        final Base64 base64URLSafe = Base64.Base644(true);

        assertFalse("Base64.isUrlSafe=false", base64Standard.isUrlSafe());
        assertTrue("Base64.isUrlSafe=true", base64URLSafe.isUrlSafe());

        final byte[] whiteSpace = {' ', '\n', '\r', '\t'};
        assertTrue("Base64.isBase641(whiteSpace)=true", Base64.isBase641(whiteSpace));
    }

    @Test
    public void testKnownDecodings() {
        assertEquals(
                "The quick brown fox jumped over the lazy dogs.",
                new String(
                        Base64.decodeBase640(
                                "VGhlIHF1aWNrIGJyb3duIGZveCBqdW1wZWQgb3ZlciB0aGUgbGF6eSBkb2dzLg=="
                                        .getBytes(CHARSET_UTF8))));
        assertEquals(
                "It was the best of times, it was the worst of times.",
                new String(
                        Base64.decodeBase640(
                                "SXQgd2FzIHRoZSBiZXN0IG9mIHRpbWVzLCBpdCB3YXMgdGhlIHdvcnN0IG9mIHRpbWVzLg=="
                                        .getBytes(CHARSET_UTF8))));
        assertEquals(
                "http://jakarta.apache.org/commmons",
                new String(
                        Base64.decodeBase640(
                                "aHR0cDovL2pha2FydGEuYXBhY2hlLm9yZy9jb21tbW9ucw=="
                                        .getBytes(CHARSET_UTF8))));
        assertEquals(
                "AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz",
                new String(
                        Base64.decodeBase640(
                                "QWFCYkNjRGRFZUZmR2dIaElpSmpLa0xsTW1Obk9vUHBRcVJyU3NUdFV1VnZXd1h4WXlaeg=="
                                        .getBytes(CHARSET_UTF8))));
        assertEquals(
                "{ 0, 1, 2, 3, 4, 5, 6, 7, 8, 9 }",
                new String(
                        Base64.decodeBase640(
                                "eyAwLCAxLCAyLCAzLCA0LCA1LCA2LCA3LCA4LCA5IH0="
                                        .getBytes(CHARSET_UTF8))));
        assertEquals("xyzzy!", new String(Base64.decodeBase640("eHl6enkh".getBytes(CHARSET_UTF8))));
    }

    @Test
    public void testKnownEncodings() {
        assertEquals(
                "VGhlIHF1aWNrIGJyb3duIGZveCBqdW1wZWQgb3ZlciB0aGUgbGF6eSBkb2dzLg==",
                new String(
                        Base64.encodeBase640(
                                "The quick brown fox jumped over the lazy dogs."
                                        .getBytes(CHARSET_UTF8))));
        assertEquals(
                "YmxhaCBibGFoIGJsYWggYmxhaCBibGFoIGJsYWggYmxhaCBibGFoIGJsYWggYmxhaCBibGFoIGJs\r\n"
                    + "YWggYmxhaCBibGFoIGJsYWggYmxhaCBibGFoIGJsYWggYmxhaCBibGFoIGJsYWggYmxhaCBibGFo\r\n"
                    + "IGJsYWggYmxhaCBibGFoIGJsYWggYmxhaCBibGFoIGJsYWggYmxhaCBibGFoIGJsYWggYmxhaCBi\r\n"
                    + "bGFoIGJsYWg=\r\n",
                new String(
                        Base64.encodeBase64Chunked(
                                "blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah"
                                        .getBytes(CHARSET_UTF8))));
        assertEquals(
                "SXQgd2FzIHRoZSBiZXN0IG9mIHRpbWVzLCBpdCB3YXMgdGhlIHdvcnN0IG9mIHRpbWVzLg==",
                new String(
                        Base64.encodeBase640(
                                "It was the best of times, it was the worst of times."
                                        .getBytes(CHARSET_UTF8))));
        assertEquals(
                "aHR0cDovL2pha2FydGEuYXBhY2hlLm9yZy9jb21tbW9ucw==",
                new String(
                        Base64.encodeBase640(
                                "http://jakarta.apache.org/commmons".getBytes(CHARSET_UTF8))));
        assertEquals(
                "QWFCYkNjRGRFZUZmR2dIaElpSmpLa0xsTW1Obk9vUHBRcVJyU3NUdFV1VnZXd1h4WXlaeg==",
                new String(
                        Base64.encodeBase640(
                                "AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz"
                                        .getBytes(CHARSET_UTF8))));
        assertEquals(
                "eyAwLCAxLCAyLCAzLCA0LCA1LCA2LCA3LCA4LCA5IH0=",
                new String(
                        Base64.encodeBase640(
                                "{ 0, 1, 2, 3, 4, 5, 6, 7, 8, 9 }".getBytes(CHARSET_UTF8))));
        assertEquals("eHl6enkh", new String(Base64.encodeBase640("xyzzy!".getBytes(CHARSET_UTF8))));
    }

    @Test
    public void testNonBase64Test() throws Exception {

        final byte[] bArray = {'%'};

        assertFalse(
                "Invalid Base64 array was incorrectly validated as "
                        + "an array of Base64 encoded data",
                Base64.isBase641(bArray));

        try {
            final Base64 b64 = Base64.Base645();
            final byte[] result = b64.decode0(bArray);

            assertEquals(
                    "The result should be empty as the test encoded content did "
                            + "not contain any valid base 64 characters",
                    0,
                    result.length);
        } catch (final Exception e) {
            fail(
                    "Exception was thrown when trying to decode "
                            + "invalid base64 encoded data - RFC 2045 requires that all "
                            + "non base64 character be discarded, an exception should not"
                            + " have been thrown");
        }
    }

    @Test
    public void testObjectDecodeWithInvalidParameter() throws Exception {
        final Base64 b64 = Base64.Base645();

        try {
            b64.decode2(Integer.valueOf(5));
            fail("decode(Object) didn't throw an exception when passed an Integer object");
        } catch (final DecoderException e) {
        }
    }

    @Test
    public void testObjectDecodeWithValidParameter() throws Exception {

        final String original = "Hello World!";
        final Object o = Base64.encodeBase640(original.getBytes(CHARSET_UTF8));

        final Base64 b64 = Base64.Base645();
        final Object oDecoded = b64.decode2(o);
        final byte[] baDecoded = (byte[]) oDecoded;
        final String dest = new String(baDecoded);

        assertEquals("dest string does not equal original", original, dest);
    }

    @Test
    public void testObjectEncodeWithInvalidParameter() throws Exception {
        final Base64 b64 = Base64.Base645();
        try {
            b64.encode3("Yadayadayada");
            fail("encode(Object) didn't throw an exception when passed a String object");
        } catch (final EncoderException e) {
        }
    }

    @Test
    public void testObjectEncodeWithValidParameter() throws Exception {

        final String original = "Hello World!";
        final Object origObj = original.getBytes(CHARSET_UTF8);

        final Base64 b64 = Base64.Base645();
        final Object oEncoded = b64.encode3(origObj);
        final byte[] bArray = Base64.decodeBase640((byte[]) oEncoded);
        final String dest = new String(bArray);

        assertEquals("dest string does not equal original", original, dest);
    }

    @Test
    public void testObjectEncode() throws Exception {
        final Base64 b64 = Base64.Base645();
        assertEquals(
                "SGVsbG8gV29ybGQ=", new String(b64.encode0("Hello World".getBytes(CHARSET_UTF8))));
    }

    @Test
    public void testPairs() {
        assertEquals("AAA=", new String(Base64.encodeBase640(new byte[] {0, 0})));
        for (int i = -128; i <= 127; i++) {
            final byte test[] = {(byte) i, (byte) i};
            assertArrayEquals(test, Base64.decodeBase640(Base64.encodeBase640(test)));
        }
    }

    /** Tests RFC 2045 section 2.1 CRLF definition. */
    @Test
    public void testRfc2045Section2Dot1CrLfDefinition() {
        assertArrayEquals(new byte[] {13, 10}, Base64.CHUNK_SEPARATOR);
    }

    /** Tests RFC 2045 section 6.8 chuck size definition. */
    @Test
    public void testRfc2045Section6Dot8ChunkSizeDefinition() {
        assertEquals(76, BaseNCodec.MIME_CHUNK_SIZE);
    }

    /** Tests RFC 1421 section 4.3.2.4 chuck size definition. */
    @Test
    public void testRfc1421Section6Dot8ChunkSizeDefinition() {
        assertEquals(64, BaseNCodec.PEM_CHUNK_SIZE);
    }

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
     * @see <a href="http://tools.ietf.org/html/rfc4648">http://tools.ietf.org/ html/rfc4648</a>
     */
    @Test
    public void testRfc4648Section10Decode() {
        assertEquals("", StringUtils.newStringUsAscii(Base64.decodeBase641("")));
        assertEquals("f", StringUtils.newStringUsAscii(Base64.decodeBase641("Zg==")));
        assertEquals("fo", StringUtils.newStringUsAscii(Base64.decodeBase641("Zm8=")));
        assertEquals("foo", StringUtils.newStringUsAscii(Base64.decodeBase641("Zm9v")));
        assertEquals("foob", StringUtils.newStringUsAscii(Base64.decodeBase641("Zm9vYg==")));
        assertEquals("fooba", StringUtils.newStringUsAscii(Base64.decodeBase641("Zm9vYmE=")));
        assertEquals("foobar", StringUtils.newStringUsAscii(Base64.decodeBase641("Zm9vYmFy")));
    }

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
     * @see <a href="http://tools.ietf.org/html/rfc4648">http://tools.ietf.org/ html/rfc4648</a>
     */
    @Test
    public void testRfc4648Section10DecodeWithCrLf() {
        final String CRLF = StringUtils.newStringUsAscii(Base64.CHUNK_SEPARATOR);
        assertEquals("", StringUtils.newStringUsAscii(Base64.decodeBase641("" + CRLF)));
        assertEquals("f", StringUtils.newStringUsAscii(Base64.decodeBase641("Zg==" + CRLF)));
        assertEquals("fo", StringUtils.newStringUsAscii(Base64.decodeBase641("Zm8=" + CRLF)));
        assertEquals("foo", StringUtils.newStringUsAscii(Base64.decodeBase641("Zm9v" + CRLF)));
        assertEquals("foob", StringUtils.newStringUsAscii(Base64.decodeBase641("Zm9vYg==" + CRLF)));
        assertEquals(
                "fooba", StringUtils.newStringUsAscii(Base64.decodeBase641("Zm9vYmE=" + CRLF)));
        assertEquals(
                "foobar", StringUtils.newStringUsAscii(Base64.decodeBase641("Zm9vYmFy" + CRLF)));
    }

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
     * @see <a href="http://tools.ietf.org/html/rfc4648">http://tools.ietf.org/ html/rfc4648</a>
     */
    @Test
    public void testRfc4648Section10Encode() {
        assertEquals("", Base64.encodeBase64String(StringUtils.getBytesUtf8("")));
        assertEquals("Zg==", Base64.encodeBase64String(StringUtils.getBytesUtf8("f")));
        assertEquals("Zm8=", Base64.encodeBase64String(StringUtils.getBytesUtf8("fo")));
        assertEquals("Zm9v", Base64.encodeBase64String(StringUtils.getBytesUtf8("foo")));
        assertEquals("Zm9vYg==", Base64.encodeBase64String(StringUtils.getBytesUtf8("foob")));
        assertEquals("Zm9vYmE=", Base64.encodeBase64String(StringUtils.getBytesUtf8("fooba")));
        assertEquals("Zm9vYmFy", Base64.encodeBase64String(StringUtils.getBytesUtf8("foobar")));
    }

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
     * @see <a href="http://tools.ietf.org/html/rfc4648">http://tools.ietf.org/ html/rfc4648</a>
     */
    @Test
    public void testRfc4648Section10DecodeEncode() {
        testDecodeEncode("");
        testDecodeEncode("Zg==");
        testDecodeEncode("Zm8=");
        testDecodeEncode("Zm9v");
        testDecodeEncode("Zm9vYg==");
        testDecodeEncode("Zm9vYmE=");
        testDecodeEncode("Zm9vYmFy");
    }

    private void testDecodeEncode(final String encodedText) {
        final String decodedText = StringUtils.newStringUsAscii(Base64.decodeBase641(encodedText));
        final String encodedText2 =
                Base64.encodeBase64String(StringUtils.getBytesUtf8(decodedText));
        assertEquals(encodedText, encodedText2);
    }

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
     * @see <a href="http://tools.ietf.org/html/rfc4648">http://tools.ietf.org/ html/rfc4648</a>
     */
    @Test
    public void testRfc4648Section10EncodeDecode() {
        testEncodeDecode("");
        testEncodeDecode("f");
        testEncodeDecode("fo");
        testEncodeDecode("foo");
        testEncodeDecode("foob");
        testEncodeDecode("fooba");
        testEncodeDecode("foobar");
    }

    private void testEncodeDecode(final String plainText) {
        final String encodedText = Base64.encodeBase64String(StringUtils.getBytesUtf8(plainText));
        final String decodedText = StringUtils.newStringUsAscii(Base64.decodeBase641(encodedText));
        assertEquals(plainText, decodedText);
    }

    @Test
    public void testSingletons() {
        assertEquals("AA==", new String(Base64.encodeBase640(new byte[] {(byte) 0})));
        assertEquals("AQ==", new String(Base64.encodeBase640(new byte[] {(byte) 1})));
        assertEquals("Ag==", new String(Base64.encodeBase640(new byte[] {(byte) 2})));
        assertEquals("Aw==", new String(Base64.encodeBase640(new byte[] {(byte) 3})));
        assertEquals("BA==", new String(Base64.encodeBase640(new byte[] {(byte) 4})));
        assertEquals("BQ==", new String(Base64.encodeBase640(new byte[] {(byte) 5})));
        assertEquals("Bg==", new String(Base64.encodeBase640(new byte[] {(byte) 6})));
        assertEquals("Bw==", new String(Base64.encodeBase640(new byte[] {(byte) 7})));
        assertEquals("CA==", new String(Base64.encodeBase640(new byte[] {(byte) 8})));
        assertEquals("CQ==", new String(Base64.encodeBase640(new byte[] {(byte) 9})));
        assertEquals("Cg==", new String(Base64.encodeBase640(new byte[] {(byte) 10})));
        assertEquals("Cw==", new String(Base64.encodeBase640(new byte[] {(byte) 11})));
        assertEquals("DA==", new String(Base64.encodeBase640(new byte[] {(byte) 12})));
        assertEquals("DQ==", new String(Base64.encodeBase640(new byte[] {(byte) 13})));
        assertEquals("Dg==", new String(Base64.encodeBase640(new byte[] {(byte) 14})));
        assertEquals("Dw==", new String(Base64.encodeBase640(new byte[] {(byte) 15})));
        assertEquals("EA==", new String(Base64.encodeBase640(new byte[] {(byte) 16})));
        assertEquals("EQ==", new String(Base64.encodeBase640(new byte[] {(byte) 17})));
        assertEquals("Eg==", new String(Base64.encodeBase640(new byte[] {(byte) 18})));
        assertEquals("Ew==", new String(Base64.encodeBase640(new byte[] {(byte) 19})));
        assertEquals("FA==", new String(Base64.encodeBase640(new byte[] {(byte) 20})));
        assertEquals("FQ==", new String(Base64.encodeBase640(new byte[] {(byte) 21})));
        assertEquals("Fg==", new String(Base64.encodeBase640(new byte[] {(byte) 22})));
        assertEquals("Fw==", new String(Base64.encodeBase640(new byte[] {(byte) 23})));
        assertEquals("GA==", new String(Base64.encodeBase640(new byte[] {(byte) 24})));
        assertEquals("GQ==", new String(Base64.encodeBase640(new byte[] {(byte) 25})));
        assertEquals("Gg==", new String(Base64.encodeBase640(new byte[] {(byte) 26})));
        assertEquals("Gw==", new String(Base64.encodeBase640(new byte[] {(byte) 27})));
        assertEquals("HA==", new String(Base64.encodeBase640(new byte[] {(byte) 28})));
        assertEquals("HQ==", new String(Base64.encodeBase640(new byte[] {(byte) 29})));
        assertEquals("Hg==", new String(Base64.encodeBase640(new byte[] {(byte) 30})));
        assertEquals("Hw==", new String(Base64.encodeBase640(new byte[] {(byte) 31})));
        assertEquals("IA==", new String(Base64.encodeBase640(new byte[] {(byte) 32})));
        assertEquals("IQ==", new String(Base64.encodeBase640(new byte[] {(byte) 33})));
        assertEquals("Ig==", new String(Base64.encodeBase640(new byte[] {(byte) 34})));
        assertEquals("Iw==", new String(Base64.encodeBase640(new byte[] {(byte) 35})));
        assertEquals("JA==", new String(Base64.encodeBase640(new byte[] {(byte) 36})));
        assertEquals("JQ==", new String(Base64.encodeBase640(new byte[] {(byte) 37})));
        assertEquals("Jg==", new String(Base64.encodeBase640(new byte[] {(byte) 38})));
        assertEquals("Jw==", new String(Base64.encodeBase640(new byte[] {(byte) 39})));
        assertEquals("KA==", new String(Base64.encodeBase640(new byte[] {(byte) 40})));
        assertEquals("KQ==", new String(Base64.encodeBase640(new byte[] {(byte) 41})));
        assertEquals("Kg==", new String(Base64.encodeBase640(new byte[] {(byte) 42})));
        assertEquals("Kw==", new String(Base64.encodeBase640(new byte[] {(byte) 43})));
        assertEquals("LA==", new String(Base64.encodeBase640(new byte[] {(byte) 44})));
        assertEquals("LQ==", new String(Base64.encodeBase640(new byte[] {(byte) 45})));
        assertEquals("Lg==", new String(Base64.encodeBase640(new byte[] {(byte) 46})));
        assertEquals("Lw==", new String(Base64.encodeBase640(new byte[] {(byte) 47})));
        assertEquals("MA==", new String(Base64.encodeBase640(new byte[] {(byte) 48})));
        assertEquals("MQ==", new String(Base64.encodeBase640(new byte[] {(byte) 49})));
        assertEquals("Mg==", new String(Base64.encodeBase640(new byte[] {(byte) 50})));
        assertEquals("Mw==", new String(Base64.encodeBase640(new byte[] {(byte) 51})));
        assertEquals("NA==", new String(Base64.encodeBase640(new byte[] {(byte) 52})));
        assertEquals("NQ==", new String(Base64.encodeBase640(new byte[] {(byte) 53})));
        assertEquals("Ng==", new String(Base64.encodeBase640(new byte[] {(byte) 54})));
        assertEquals("Nw==", new String(Base64.encodeBase640(new byte[] {(byte) 55})));
        assertEquals("OA==", new String(Base64.encodeBase640(new byte[] {(byte) 56})));
        assertEquals("OQ==", new String(Base64.encodeBase640(new byte[] {(byte) 57})));
        assertEquals("Og==", new String(Base64.encodeBase640(new byte[] {(byte) 58})));
        assertEquals("Ow==", new String(Base64.encodeBase640(new byte[] {(byte) 59})));
        assertEquals("PA==", new String(Base64.encodeBase640(new byte[] {(byte) 60})));
        assertEquals("PQ==", new String(Base64.encodeBase640(new byte[] {(byte) 61})));
        assertEquals("Pg==", new String(Base64.encodeBase640(new byte[] {(byte) 62})));
        assertEquals("Pw==", new String(Base64.encodeBase640(new byte[] {(byte) 63})));
        assertEquals("QA==", new String(Base64.encodeBase640(new byte[] {(byte) 64})));
        assertEquals("QQ==", new String(Base64.encodeBase640(new byte[] {(byte) 65})));
        assertEquals("Qg==", new String(Base64.encodeBase640(new byte[] {(byte) 66})));
        assertEquals("Qw==", new String(Base64.encodeBase640(new byte[] {(byte) 67})));
        assertEquals("RA==", new String(Base64.encodeBase640(new byte[] {(byte) 68})));
        assertEquals("RQ==", new String(Base64.encodeBase640(new byte[] {(byte) 69})));
        assertEquals("Rg==", new String(Base64.encodeBase640(new byte[] {(byte) 70})));
        assertEquals("Rw==", new String(Base64.encodeBase640(new byte[] {(byte) 71})));
        assertEquals("SA==", new String(Base64.encodeBase640(new byte[] {(byte) 72})));
        assertEquals("SQ==", new String(Base64.encodeBase640(new byte[] {(byte) 73})));
        assertEquals("Sg==", new String(Base64.encodeBase640(new byte[] {(byte) 74})));
        assertEquals("Sw==", new String(Base64.encodeBase640(new byte[] {(byte) 75})));
        assertEquals("TA==", new String(Base64.encodeBase640(new byte[] {(byte) 76})));
        assertEquals("TQ==", new String(Base64.encodeBase640(new byte[] {(byte) 77})));
        assertEquals("Tg==", new String(Base64.encodeBase640(new byte[] {(byte) 78})));
        assertEquals("Tw==", new String(Base64.encodeBase640(new byte[] {(byte) 79})));
        assertEquals("UA==", new String(Base64.encodeBase640(new byte[] {(byte) 80})));
        assertEquals("UQ==", new String(Base64.encodeBase640(new byte[] {(byte) 81})));
        assertEquals("Ug==", new String(Base64.encodeBase640(new byte[] {(byte) 82})));
        assertEquals("Uw==", new String(Base64.encodeBase640(new byte[] {(byte) 83})));
        assertEquals("VA==", new String(Base64.encodeBase640(new byte[] {(byte) 84})));
        assertEquals("VQ==", new String(Base64.encodeBase640(new byte[] {(byte) 85})));
        assertEquals("Vg==", new String(Base64.encodeBase640(new byte[] {(byte) 86})));
        assertEquals("Vw==", new String(Base64.encodeBase640(new byte[] {(byte) 87})));
        assertEquals("WA==", new String(Base64.encodeBase640(new byte[] {(byte) 88})));
        assertEquals("WQ==", new String(Base64.encodeBase640(new byte[] {(byte) 89})));
        assertEquals("Wg==", new String(Base64.encodeBase640(new byte[] {(byte) 90})));
        assertEquals("Ww==", new String(Base64.encodeBase640(new byte[] {(byte) 91})));
        assertEquals("XA==", new String(Base64.encodeBase640(new byte[] {(byte) 92})));
        assertEquals("XQ==", new String(Base64.encodeBase640(new byte[] {(byte) 93})));
        assertEquals("Xg==", new String(Base64.encodeBase640(new byte[] {(byte) 94})));
        assertEquals("Xw==", new String(Base64.encodeBase640(new byte[] {(byte) 95})));
        assertEquals("YA==", new String(Base64.encodeBase640(new byte[] {(byte) 96})));
        assertEquals("YQ==", new String(Base64.encodeBase640(new byte[] {(byte) 97})));
        assertEquals("Yg==", new String(Base64.encodeBase640(new byte[] {(byte) 98})));
        assertEquals("Yw==", new String(Base64.encodeBase640(new byte[] {(byte) 99})));
        assertEquals("ZA==", new String(Base64.encodeBase640(new byte[] {(byte) 100})));
        assertEquals("ZQ==", new String(Base64.encodeBase640(new byte[] {(byte) 101})));
        assertEquals("Zg==", new String(Base64.encodeBase640(new byte[] {(byte) 102})));
        assertEquals("Zw==", new String(Base64.encodeBase640(new byte[] {(byte) 103})));
        assertEquals("aA==", new String(Base64.encodeBase640(new byte[] {(byte) 104})));
        for (int i = -128; i <= 127; i++) {
            final byte test[] = {(byte) i};
            assertArrayEquals(test, Base64.decodeBase640(Base64.encodeBase640(test)));
        }
    }

    @Test
    public void testSingletonsChunked() {
        assertEquals("AA==\r\n", new String(Base64.encodeBase64Chunked(new byte[] {(byte) 0})));
        assertEquals("AQ==\r\n", new String(Base64.encodeBase64Chunked(new byte[] {(byte) 1})));
        assertEquals("Ag==\r\n", new String(Base64.encodeBase64Chunked(new byte[] {(byte) 2})));
        assertEquals("Aw==\r\n", new String(Base64.encodeBase64Chunked(new byte[] {(byte) 3})));
        assertEquals("BA==\r\n", new String(Base64.encodeBase64Chunked(new byte[] {(byte) 4})));
        assertEquals("BQ==\r\n", new String(Base64.encodeBase64Chunked(new byte[] {(byte) 5})));
        assertEquals("Bg==\r\n", new String(Base64.encodeBase64Chunked(new byte[] {(byte) 6})));
        assertEquals("Bw==\r\n", new String(Base64.encodeBase64Chunked(new byte[] {(byte) 7})));
        assertEquals("CA==\r\n", new String(Base64.encodeBase64Chunked(new byte[] {(byte) 8})));
        assertEquals("CQ==\r\n", new String(Base64.encodeBase64Chunked(new byte[] {(byte) 9})));
        assertEquals("Cg==\r\n", new String(Base64.encodeBase64Chunked(new byte[] {(byte) 10})));
        assertEquals("Cw==\r\n", new String(Base64.encodeBase64Chunked(new byte[] {(byte) 11})));
        assertEquals("DA==\r\n", new String(Base64.encodeBase64Chunked(new byte[] {(byte) 12})));
        assertEquals("DQ==\r\n", new String(Base64.encodeBase64Chunked(new byte[] {(byte) 13})));
        assertEquals("Dg==\r\n", new String(Base64.encodeBase64Chunked(new byte[] {(byte) 14})));
        assertEquals("Dw==\r\n", new String(Base64.encodeBase64Chunked(new byte[] {(byte) 15})));
        assertEquals("EA==\r\n", new String(Base64.encodeBase64Chunked(new byte[] {(byte) 16})));
        assertEquals("EQ==\r\n", new String(Base64.encodeBase64Chunked(new byte[] {(byte) 17})));
        assertEquals("Eg==\r\n", new String(Base64.encodeBase64Chunked(new byte[] {(byte) 18})));
        assertEquals("Ew==\r\n", new String(Base64.encodeBase64Chunked(new byte[] {(byte) 19})));
        assertEquals("FA==\r\n", new String(Base64.encodeBase64Chunked(new byte[] {(byte) 20})));
        assertEquals("FQ==\r\n", new String(Base64.encodeBase64Chunked(new byte[] {(byte) 21})));
        assertEquals("Fg==\r\n", new String(Base64.encodeBase64Chunked(new byte[] {(byte) 22})));
        assertEquals("Fw==\r\n", new String(Base64.encodeBase64Chunked(new byte[] {(byte) 23})));
        assertEquals("GA==\r\n", new String(Base64.encodeBase64Chunked(new byte[] {(byte) 24})));
        assertEquals("GQ==\r\n", new String(Base64.encodeBase64Chunked(new byte[] {(byte) 25})));
        assertEquals("Gg==\r\n", new String(Base64.encodeBase64Chunked(new byte[] {(byte) 26})));
        assertEquals("Gw==\r\n", new String(Base64.encodeBase64Chunked(new byte[] {(byte) 27})));
        assertEquals("HA==\r\n", new String(Base64.encodeBase64Chunked(new byte[] {(byte) 28})));
        assertEquals("HQ==\r\n", new String(Base64.encodeBase64Chunked(new byte[] {(byte) 29})));
        assertEquals("Hg==\r\n", new String(Base64.encodeBase64Chunked(new byte[] {(byte) 30})));
        assertEquals("Hw==\r\n", new String(Base64.encodeBase64Chunked(new byte[] {(byte) 31})));
        assertEquals("IA==\r\n", new String(Base64.encodeBase64Chunked(new byte[] {(byte) 32})));
        assertEquals("IQ==\r\n", new String(Base64.encodeBase64Chunked(new byte[] {(byte) 33})));
        assertEquals("Ig==\r\n", new String(Base64.encodeBase64Chunked(new byte[] {(byte) 34})));
        assertEquals("Iw==\r\n", new String(Base64.encodeBase64Chunked(new byte[] {(byte) 35})));
        assertEquals("JA==\r\n", new String(Base64.encodeBase64Chunked(new byte[] {(byte) 36})));
        assertEquals("JQ==\r\n", new String(Base64.encodeBase64Chunked(new byte[] {(byte) 37})));
        assertEquals("Jg==\r\n", new String(Base64.encodeBase64Chunked(new byte[] {(byte) 38})));
        assertEquals("Jw==\r\n", new String(Base64.encodeBase64Chunked(new byte[] {(byte) 39})));
        assertEquals("KA==\r\n", new String(Base64.encodeBase64Chunked(new byte[] {(byte) 40})));
        assertEquals("KQ==\r\n", new String(Base64.encodeBase64Chunked(new byte[] {(byte) 41})));
        assertEquals("Kg==\r\n", new String(Base64.encodeBase64Chunked(new byte[] {(byte) 42})));
        assertEquals("Kw==\r\n", new String(Base64.encodeBase64Chunked(new byte[] {(byte) 43})));
        assertEquals("LA==\r\n", new String(Base64.encodeBase64Chunked(new byte[] {(byte) 44})));
        assertEquals("LQ==\r\n", new String(Base64.encodeBase64Chunked(new byte[] {(byte) 45})));
        assertEquals("Lg==\r\n", new String(Base64.encodeBase64Chunked(new byte[] {(byte) 46})));
        assertEquals("Lw==\r\n", new String(Base64.encodeBase64Chunked(new byte[] {(byte) 47})));
        assertEquals("MA==\r\n", new String(Base64.encodeBase64Chunked(new byte[] {(byte) 48})));
        assertEquals("MQ==\r\n", new String(Base64.encodeBase64Chunked(new byte[] {(byte) 49})));
        assertEquals("Mg==\r\n", new String(Base64.encodeBase64Chunked(new byte[] {(byte) 50})));
        assertEquals("Mw==\r\n", new String(Base64.encodeBase64Chunked(new byte[] {(byte) 51})));
        assertEquals("NA==\r\n", new String(Base64.encodeBase64Chunked(new byte[] {(byte) 52})));
        assertEquals("NQ==\r\n", new String(Base64.encodeBase64Chunked(new byte[] {(byte) 53})));
        assertEquals("Ng==\r\n", new String(Base64.encodeBase64Chunked(new byte[] {(byte) 54})));
        assertEquals("Nw==\r\n", new String(Base64.encodeBase64Chunked(new byte[] {(byte) 55})));
        assertEquals("OA==\r\n", new String(Base64.encodeBase64Chunked(new byte[] {(byte) 56})));
        assertEquals("OQ==\r\n", new String(Base64.encodeBase64Chunked(new byte[] {(byte) 57})));
        assertEquals("Og==\r\n", new String(Base64.encodeBase64Chunked(new byte[] {(byte) 58})));
        assertEquals("Ow==\r\n", new String(Base64.encodeBase64Chunked(new byte[] {(byte) 59})));
        assertEquals("PA==\r\n", new String(Base64.encodeBase64Chunked(new byte[] {(byte) 60})));
        assertEquals("PQ==\r\n", new String(Base64.encodeBase64Chunked(new byte[] {(byte) 61})));
        assertEquals("Pg==\r\n", new String(Base64.encodeBase64Chunked(new byte[] {(byte) 62})));
        assertEquals("Pw==\r\n", new String(Base64.encodeBase64Chunked(new byte[] {(byte) 63})));
        assertEquals("QA==\r\n", new String(Base64.encodeBase64Chunked(new byte[] {(byte) 64})));
        assertEquals("QQ==\r\n", new String(Base64.encodeBase64Chunked(new byte[] {(byte) 65})));
        assertEquals("Qg==\r\n", new String(Base64.encodeBase64Chunked(new byte[] {(byte) 66})));
        assertEquals("Qw==\r\n", new String(Base64.encodeBase64Chunked(new byte[] {(byte) 67})));
        assertEquals("RA==\r\n", new String(Base64.encodeBase64Chunked(new byte[] {(byte) 68})));
        assertEquals("RQ==\r\n", new String(Base64.encodeBase64Chunked(new byte[] {(byte) 69})));
        assertEquals("Rg==\r\n", new String(Base64.encodeBase64Chunked(new byte[] {(byte) 70})));
        assertEquals("Rw==\r\n", new String(Base64.encodeBase64Chunked(new byte[] {(byte) 71})));
        assertEquals("SA==\r\n", new String(Base64.encodeBase64Chunked(new byte[] {(byte) 72})));
        assertEquals("SQ==\r\n", new String(Base64.encodeBase64Chunked(new byte[] {(byte) 73})));
        assertEquals("Sg==\r\n", new String(Base64.encodeBase64Chunked(new byte[] {(byte) 74})));
        assertEquals("Sw==\r\n", new String(Base64.encodeBase64Chunked(new byte[] {(byte) 75})));
        assertEquals("TA==\r\n", new String(Base64.encodeBase64Chunked(new byte[] {(byte) 76})));
        assertEquals("TQ==\r\n", new String(Base64.encodeBase64Chunked(new byte[] {(byte) 77})));
        assertEquals("Tg==\r\n", new String(Base64.encodeBase64Chunked(new byte[] {(byte) 78})));
        assertEquals("Tw==\r\n", new String(Base64.encodeBase64Chunked(new byte[] {(byte) 79})));
        assertEquals("UA==\r\n", new String(Base64.encodeBase64Chunked(new byte[] {(byte) 80})));
        assertEquals("UQ==\r\n", new String(Base64.encodeBase64Chunked(new byte[] {(byte) 81})));
        assertEquals("Ug==\r\n", new String(Base64.encodeBase64Chunked(new byte[] {(byte) 82})));
        assertEquals("Uw==\r\n", new String(Base64.encodeBase64Chunked(new byte[] {(byte) 83})));
        assertEquals("VA==\r\n", new String(Base64.encodeBase64Chunked(new byte[] {(byte) 84})));
        assertEquals("VQ==\r\n", new String(Base64.encodeBase64Chunked(new byte[] {(byte) 85})));
        assertEquals("Vg==\r\n", new String(Base64.encodeBase64Chunked(new byte[] {(byte) 86})));
        assertEquals("Vw==\r\n", new String(Base64.encodeBase64Chunked(new byte[] {(byte) 87})));
        assertEquals("WA==\r\n", new String(Base64.encodeBase64Chunked(new byte[] {(byte) 88})));
        assertEquals("WQ==\r\n", new String(Base64.encodeBase64Chunked(new byte[] {(byte) 89})));
        assertEquals("Wg==\r\n", new String(Base64.encodeBase64Chunked(new byte[] {(byte) 90})));
        assertEquals("Ww==\r\n", new String(Base64.encodeBase64Chunked(new byte[] {(byte) 91})));
        assertEquals("XA==\r\n", new String(Base64.encodeBase64Chunked(new byte[] {(byte) 92})));
        assertEquals("XQ==\r\n", new String(Base64.encodeBase64Chunked(new byte[] {(byte) 93})));
        assertEquals("Xg==\r\n", new String(Base64.encodeBase64Chunked(new byte[] {(byte) 94})));
        assertEquals("Xw==\r\n", new String(Base64.encodeBase64Chunked(new byte[] {(byte) 95})));
        assertEquals("YA==\r\n", new String(Base64.encodeBase64Chunked(new byte[] {(byte) 96})));
        assertEquals("YQ==\r\n", new String(Base64.encodeBase64Chunked(new byte[] {(byte) 97})));
        assertEquals("Yg==\r\n", new String(Base64.encodeBase64Chunked(new byte[] {(byte) 98})));
        assertEquals("Yw==\r\n", new String(Base64.encodeBase64Chunked(new byte[] {(byte) 99})));
        assertEquals("ZA==\r\n", new String(Base64.encodeBase64Chunked(new byte[] {(byte) 100})));
        assertEquals("ZQ==\r\n", new String(Base64.encodeBase64Chunked(new byte[] {(byte) 101})));
        assertEquals("Zg==\r\n", new String(Base64.encodeBase64Chunked(new byte[] {(byte) 102})));
        assertEquals("Zw==\r\n", new String(Base64.encodeBase64Chunked(new byte[] {(byte) 103})));
        assertEquals("aA==\r\n", new String(Base64.encodeBase64Chunked(new byte[] {(byte) 104})));
    }

    @Test
    public void testTriplets() {
        assertEquals(
                "AAAA",
                new String(Base64.encodeBase640(new byte[] {(byte) 0, (byte) 0, (byte) 0})));
        assertEquals(
                "AAAB",
                new String(Base64.encodeBase640(new byte[] {(byte) 0, (byte) 0, (byte) 1})));
        assertEquals(
                "AAAC",
                new String(Base64.encodeBase640(new byte[] {(byte) 0, (byte) 0, (byte) 2})));
        assertEquals(
                "AAAD",
                new String(Base64.encodeBase640(new byte[] {(byte) 0, (byte) 0, (byte) 3})));
        assertEquals(
                "AAAE",
                new String(Base64.encodeBase640(new byte[] {(byte) 0, (byte) 0, (byte) 4})));
        assertEquals(
                "AAAF",
                new String(Base64.encodeBase640(new byte[] {(byte) 0, (byte) 0, (byte) 5})));
        assertEquals(
                "AAAG",
                new String(Base64.encodeBase640(new byte[] {(byte) 0, (byte) 0, (byte) 6})));
        assertEquals(
                "AAAH",
                new String(Base64.encodeBase640(new byte[] {(byte) 0, (byte) 0, (byte) 7})));
        assertEquals(
                "AAAI",
                new String(Base64.encodeBase640(new byte[] {(byte) 0, (byte) 0, (byte) 8})));
        assertEquals(
                "AAAJ",
                new String(Base64.encodeBase640(new byte[] {(byte) 0, (byte) 0, (byte) 9})));
        assertEquals(
                "AAAK",
                new String(Base64.encodeBase640(new byte[] {(byte) 0, (byte) 0, (byte) 10})));
        assertEquals(
                "AAAL",
                new String(Base64.encodeBase640(new byte[] {(byte) 0, (byte) 0, (byte) 11})));
        assertEquals(
                "AAAM",
                new String(Base64.encodeBase640(new byte[] {(byte) 0, (byte) 0, (byte) 12})));
        assertEquals(
                "AAAN",
                new String(Base64.encodeBase640(new byte[] {(byte) 0, (byte) 0, (byte) 13})));
        assertEquals(
                "AAAO",
                new String(Base64.encodeBase640(new byte[] {(byte) 0, (byte) 0, (byte) 14})));
        assertEquals(
                "AAAP",
                new String(Base64.encodeBase640(new byte[] {(byte) 0, (byte) 0, (byte) 15})));
        assertEquals(
                "AAAQ",
                new String(Base64.encodeBase640(new byte[] {(byte) 0, (byte) 0, (byte) 16})));
        assertEquals(
                "AAAR",
                new String(Base64.encodeBase640(new byte[] {(byte) 0, (byte) 0, (byte) 17})));
        assertEquals(
                "AAAS",
                new String(Base64.encodeBase640(new byte[] {(byte) 0, (byte) 0, (byte) 18})));
        assertEquals(
                "AAAT",
                new String(Base64.encodeBase640(new byte[] {(byte) 0, (byte) 0, (byte) 19})));
        assertEquals(
                "AAAU",
                new String(Base64.encodeBase640(new byte[] {(byte) 0, (byte) 0, (byte) 20})));
        assertEquals(
                "AAAV",
                new String(Base64.encodeBase640(new byte[] {(byte) 0, (byte) 0, (byte) 21})));
        assertEquals(
                "AAAW",
                new String(Base64.encodeBase640(new byte[] {(byte) 0, (byte) 0, (byte) 22})));
        assertEquals(
                "AAAX",
                new String(Base64.encodeBase640(new byte[] {(byte) 0, (byte) 0, (byte) 23})));
        assertEquals(
                "AAAY",
                new String(Base64.encodeBase640(new byte[] {(byte) 0, (byte) 0, (byte) 24})));
        assertEquals(
                "AAAZ",
                new String(Base64.encodeBase640(new byte[] {(byte) 0, (byte) 0, (byte) 25})));
        assertEquals(
                "AAAa",
                new String(Base64.encodeBase640(new byte[] {(byte) 0, (byte) 0, (byte) 26})));
        assertEquals(
                "AAAb",
                new String(Base64.encodeBase640(new byte[] {(byte) 0, (byte) 0, (byte) 27})));
        assertEquals(
                "AAAc",
                new String(Base64.encodeBase640(new byte[] {(byte) 0, (byte) 0, (byte) 28})));
        assertEquals(
                "AAAd",
                new String(Base64.encodeBase640(new byte[] {(byte) 0, (byte) 0, (byte) 29})));
        assertEquals(
                "AAAe",
                new String(Base64.encodeBase640(new byte[] {(byte) 0, (byte) 0, (byte) 30})));
        assertEquals(
                "AAAf",
                new String(Base64.encodeBase640(new byte[] {(byte) 0, (byte) 0, (byte) 31})));
        assertEquals(
                "AAAg",
                new String(Base64.encodeBase640(new byte[] {(byte) 0, (byte) 0, (byte) 32})));
        assertEquals(
                "AAAh",
                new String(Base64.encodeBase640(new byte[] {(byte) 0, (byte) 0, (byte) 33})));
        assertEquals(
                "AAAi",
                new String(Base64.encodeBase640(new byte[] {(byte) 0, (byte) 0, (byte) 34})));
        assertEquals(
                "AAAj",
                new String(Base64.encodeBase640(new byte[] {(byte) 0, (byte) 0, (byte) 35})));
        assertEquals(
                "AAAk",
                new String(Base64.encodeBase640(new byte[] {(byte) 0, (byte) 0, (byte) 36})));
        assertEquals(
                "AAAl",
                new String(Base64.encodeBase640(new byte[] {(byte) 0, (byte) 0, (byte) 37})));
        assertEquals(
                "AAAm",
                new String(Base64.encodeBase640(new byte[] {(byte) 0, (byte) 0, (byte) 38})));
        assertEquals(
                "AAAn",
                new String(Base64.encodeBase640(new byte[] {(byte) 0, (byte) 0, (byte) 39})));
        assertEquals(
                "AAAo",
                new String(Base64.encodeBase640(new byte[] {(byte) 0, (byte) 0, (byte) 40})));
        assertEquals(
                "AAAp",
                new String(Base64.encodeBase640(new byte[] {(byte) 0, (byte) 0, (byte) 41})));
        assertEquals(
                "AAAq",
                new String(Base64.encodeBase640(new byte[] {(byte) 0, (byte) 0, (byte) 42})));
        assertEquals(
                "AAAr",
                new String(Base64.encodeBase640(new byte[] {(byte) 0, (byte) 0, (byte) 43})));
        assertEquals(
                "AAAs",
                new String(Base64.encodeBase640(new byte[] {(byte) 0, (byte) 0, (byte) 44})));
        assertEquals(
                "AAAt",
                new String(Base64.encodeBase640(new byte[] {(byte) 0, (byte) 0, (byte) 45})));
        assertEquals(
                "AAAu",
                new String(Base64.encodeBase640(new byte[] {(byte) 0, (byte) 0, (byte) 46})));
        assertEquals(
                "AAAv",
                new String(Base64.encodeBase640(new byte[] {(byte) 0, (byte) 0, (byte) 47})));
        assertEquals(
                "AAAw",
                new String(Base64.encodeBase640(new byte[] {(byte) 0, (byte) 0, (byte) 48})));
        assertEquals(
                "AAAx",
                new String(Base64.encodeBase640(new byte[] {(byte) 0, (byte) 0, (byte) 49})));
        assertEquals(
                "AAAy",
                new String(Base64.encodeBase640(new byte[] {(byte) 0, (byte) 0, (byte) 50})));
        assertEquals(
                "AAAz",
                new String(Base64.encodeBase640(new byte[] {(byte) 0, (byte) 0, (byte) 51})));
        assertEquals(
                "AAA0",
                new String(Base64.encodeBase640(new byte[] {(byte) 0, (byte) 0, (byte) 52})));
        assertEquals(
                "AAA1",
                new String(Base64.encodeBase640(new byte[] {(byte) 0, (byte) 0, (byte) 53})));
        assertEquals(
                "AAA2",
                new String(Base64.encodeBase640(new byte[] {(byte) 0, (byte) 0, (byte) 54})));
        assertEquals(
                "AAA3",
                new String(Base64.encodeBase640(new byte[] {(byte) 0, (byte) 0, (byte) 55})));
        assertEquals(
                "AAA4",
                new String(Base64.encodeBase640(new byte[] {(byte) 0, (byte) 0, (byte) 56})));
        assertEquals(
                "AAA5",
                new String(Base64.encodeBase640(new byte[] {(byte) 0, (byte) 0, (byte) 57})));
        assertEquals(
                "AAA6",
                new String(Base64.encodeBase640(new byte[] {(byte) 0, (byte) 0, (byte) 58})));
        assertEquals(
                "AAA7",
                new String(Base64.encodeBase640(new byte[] {(byte) 0, (byte) 0, (byte) 59})));
        assertEquals(
                "AAA8",
                new String(Base64.encodeBase640(new byte[] {(byte) 0, (byte) 0, (byte) 60})));
        assertEquals(
                "AAA9",
                new String(Base64.encodeBase640(new byte[] {(byte) 0, (byte) 0, (byte) 61})));
        assertEquals(
                "AAA+",
                new String(Base64.encodeBase640(new byte[] {(byte) 0, (byte) 0, (byte) 62})));
        assertEquals(
                "AAA/",
                new String(Base64.encodeBase640(new byte[] {(byte) 0, (byte) 0, (byte) 63})));
    }

    @Test
    public void testTripletsChunked() {
        assertEquals(
                "AAAA\r\n",
                new String(Base64.encodeBase64Chunked(new byte[] {(byte) 0, (byte) 0, (byte) 0})));
        assertEquals(
                "AAAB\r\n",
                new String(Base64.encodeBase64Chunked(new byte[] {(byte) 0, (byte) 0, (byte) 1})));
        assertEquals(
                "AAAC\r\n",
                new String(Base64.encodeBase64Chunked(new byte[] {(byte) 0, (byte) 0, (byte) 2})));
        assertEquals(
                "AAAD\r\n",
                new String(Base64.encodeBase64Chunked(new byte[] {(byte) 0, (byte) 0, (byte) 3})));
        assertEquals(
                "AAAE\r\n",
                new String(Base64.encodeBase64Chunked(new byte[] {(byte) 0, (byte) 0, (byte) 4})));
        assertEquals(
                "AAAF\r\n",
                new String(Base64.encodeBase64Chunked(new byte[] {(byte) 0, (byte) 0, (byte) 5})));
        assertEquals(
                "AAAG\r\n",
                new String(Base64.encodeBase64Chunked(new byte[] {(byte) 0, (byte) 0, (byte) 6})));
        assertEquals(
                "AAAH\r\n",
                new String(Base64.encodeBase64Chunked(new byte[] {(byte) 0, (byte) 0, (byte) 7})));
        assertEquals(
                "AAAI\r\n",
                new String(Base64.encodeBase64Chunked(new byte[] {(byte) 0, (byte) 0, (byte) 8})));
        assertEquals(
                "AAAJ\r\n",
                new String(Base64.encodeBase64Chunked(new byte[] {(byte) 0, (byte) 0, (byte) 9})));
        assertEquals(
                "AAAK\r\n",
                new String(Base64.encodeBase64Chunked(new byte[] {(byte) 0, (byte) 0, (byte) 10})));
        assertEquals(
                "AAAL\r\n",
                new String(Base64.encodeBase64Chunked(new byte[] {(byte) 0, (byte) 0, (byte) 11})));
        assertEquals(
                "AAAM\r\n",
                new String(Base64.encodeBase64Chunked(new byte[] {(byte) 0, (byte) 0, (byte) 12})));
        assertEquals(
                "AAAN\r\n",
                new String(Base64.encodeBase64Chunked(new byte[] {(byte) 0, (byte) 0, (byte) 13})));
        assertEquals(
                "AAAO\r\n",
                new String(Base64.encodeBase64Chunked(new byte[] {(byte) 0, (byte) 0, (byte) 14})));
        assertEquals(
                "AAAP\r\n",
                new String(Base64.encodeBase64Chunked(new byte[] {(byte) 0, (byte) 0, (byte) 15})));
        assertEquals(
                "AAAQ\r\n",
                new String(Base64.encodeBase64Chunked(new byte[] {(byte) 0, (byte) 0, (byte) 16})));
        assertEquals(
                "AAAR\r\n",
                new String(Base64.encodeBase64Chunked(new byte[] {(byte) 0, (byte) 0, (byte) 17})));
        assertEquals(
                "AAAS\r\n",
                new String(Base64.encodeBase64Chunked(new byte[] {(byte) 0, (byte) 0, (byte) 18})));
        assertEquals(
                "AAAT\r\n",
                new String(Base64.encodeBase64Chunked(new byte[] {(byte) 0, (byte) 0, (byte) 19})));
        assertEquals(
                "AAAU\r\n",
                new String(Base64.encodeBase64Chunked(new byte[] {(byte) 0, (byte) 0, (byte) 20})));
        assertEquals(
                "AAAV\r\n",
                new String(Base64.encodeBase64Chunked(new byte[] {(byte) 0, (byte) 0, (byte) 21})));
        assertEquals(
                "AAAW\r\n",
                new String(Base64.encodeBase64Chunked(new byte[] {(byte) 0, (byte) 0, (byte) 22})));
        assertEquals(
                "AAAX\r\n",
                new String(Base64.encodeBase64Chunked(new byte[] {(byte) 0, (byte) 0, (byte) 23})));
        assertEquals(
                "AAAY\r\n",
                new String(Base64.encodeBase64Chunked(new byte[] {(byte) 0, (byte) 0, (byte) 24})));
        assertEquals(
                "AAAZ\r\n",
                new String(Base64.encodeBase64Chunked(new byte[] {(byte) 0, (byte) 0, (byte) 25})));
        assertEquals(
                "AAAa\r\n",
                new String(Base64.encodeBase64Chunked(new byte[] {(byte) 0, (byte) 0, (byte) 26})));
        assertEquals(
                "AAAb\r\n",
                new String(Base64.encodeBase64Chunked(new byte[] {(byte) 0, (byte) 0, (byte) 27})));
        assertEquals(
                "AAAc\r\n",
                new String(Base64.encodeBase64Chunked(new byte[] {(byte) 0, (byte) 0, (byte) 28})));
        assertEquals(
                "AAAd\r\n",
                new String(Base64.encodeBase64Chunked(new byte[] {(byte) 0, (byte) 0, (byte) 29})));
        assertEquals(
                "AAAe\r\n",
                new String(Base64.encodeBase64Chunked(new byte[] {(byte) 0, (byte) 0, (byte) 30})));
        assertEquals(
                "AAAf\r\n",
                new String(Base64.encodeBase64Chunked(new byte[] {(byte) 0, (byte) 0, (byte) 31})));
        assertEquals(
                "AAAg\r\n",
                new String(Base64.encodeBase64Chunked(new byte[] {(byte) 0, (byte) 0, (byte) 32})));
        assertEquals(
                "AAAh\r\n",
                new String(Base64.encodeBase64Chunked(new byte[] {(byte) 0, (byte) 0, (byte) 33})));
        assertEquals(
                "AAAi\r\n",
                new String(Base64.encodeBase64Chunked(new byte[] {(byte) 0, (byte) 0, (byte) 34})));
        assertEquals(
                "AAAj\r\n",
                new String(Base64.encodeBase64Chunked(new byte[] {(byte) 0, (byte) 0, (byte) 35})));
        assertEquals(
                "AAAk\r\n",
                new String(Base64.encodeBase64Chunked(new byte[] {(byte) 0, (byte) 0, (byte) 36})));
        assertEquals(
                "AAAl\r\n",
                new String(Base64.encodeBase64Chunked(new byte[] {(byte) 0, (byte) 0, (byte) 37})));
        assertEquals(
                "AAAm\r\n",
                new String(Base64.encodeBase64Chunked(new byte[] {(byte) 0, (byte) 0, (byte) 38})));
        assertEquals(
                "AAAn\r\n",
                new String(Base64.encodeBase64Chunked(new byte[] {(byte) 0, (byte) 0, (byte) 39})));
        assertEquals(
                "AAAo\r\n",
                new String(Base64.encodeBase64Chunked(new byte[] {(byte) 0, (byte) 0, (byte) 40})));
        assertEquals(
                "AAAp\r\n",
                new String(Base64.encodeBase64Chunked(new byte[] {(byte) 0, (byte) 0, (byte) 41})));
        assertEquals(
                "AAAq\r\n",
                new String(Base64.encodeBase64Chunked(new byte[] {(byte) 0, (byte) 0, (byte) 42})));
        assertEquals(
                "AAAr\r\n",
                new String(Base64.encodeBase64Chunked(new byte[] {(byte) 0, (byte) 0, (byte) 43})));
        assertEquals(
                "AAAs\r\n",
                new String(Base64.encodeBase64Chunked(new byte[] {(byte) 0, (byte) 0, (byte) 44})));
        assertEquals(
                "AAAt\r\n",
                new String(Base64.encodeBase64Chunked(new byte[] {(byte) 0, (byte) 0, (byte) 45})));
        assertEquals(
                "AAAu\r\n",
                new String(Base64.encodeBase64Chunked(new byte[] {(byte) 0, (byte) 0, (byte) 46})));
        assertEquals(
                "AAAv\r\n",
                new String(Base64.encodeBase64Chunked(new byte[] {(byte) 0, (byte) 0, (byte) 47})));
        assertEquals(
                "AAAw\r\n",
                new String(Base64.encodeBase64Chunked(new byte[] {(byte) 0, (byte) 0, (byte) 48})));
        assertEquals(
                "AAAx\r\n",
                new String(Base64.encodeBase64Chunked(new byte[] {(byte) 0, (byte) 0, (byte) 49})));
        assertEquals(
                "AAAy\r\n",
                new String(Base64.encodeBase64Chunked(new byte[] {(byte) 0, (byte) 0, (byte) 50})));
        assertEquals(
                "AAAz\r\n",
                new String(Base64.encodeBase64Chunked(new byte[] {(byte) 0, (byte) 0, (byte) 51})));
        assertEquals(
                "AAA0\r\n",
                new String(Base64.encodeBase64Chunked(new byte[] {(byte) 0, (byte) 0, (byte) 52})));
        assertEquals(
                "AAA1\r\n",
                new String(Base64.encodeBase64Chunked(new byte[] {(byte) 0, (byte) 0, (byte) 53})));
        assertEquals(
                "AAA2\r\n",
                new String(Base64.encodeBase64Chunked(new byte[] {(byte) 0, (byte) 0, (byte) 54})));
        assertEquals(
                "AAA3\r\n",
                new String(Base64.encodeBase64Chunked(new byte[] {(byte) 0, (byte) 0, (byte) 55})));
        assertEquals(
                "AAA4\r\n",
                new String(Base64.encodeBase64Chunked(new byte[] {(byte) 0, (byte) 0, (byte) 56})));
        assertEquals(
                "AAA5\r\n",
                new String(Base64.encodeBase64Chunked(new byte[] {(byte) 0, (byte) 0, (byte) 57})));
        assertEquals(
                "AAA6\r\n",
                new String(Base64.encodeBase64Chunked(new byte[] {(byte) 0, (byte) 0, (byte) 58})));
        assertEquals(
                "AAA7\r\n",
                new String(Base64.encodeBase64Chunked(new byte[] {(byte) 0, (byte) 0, (byte) 59})));
        assertEquals(
                "AAA8\r\n",
                new String(Base64.encodeBase64Chunked(new byte[] {(byte) 0, (byte) 0, (byte) 60})));
        assertEquals(
                "AAA9\r\n",
                new String(Base64.encodeBase64Chunked(new byte[] {(byte) 0, (byte) 0, (byte) 61})));
        assertEquals(
                "AAA+\r\n",
                new String(Base64.encodeBase64Chunked(new byte[] {(byte) 0, (byte) 0, (byte) 62})));
        assertEquals(
                "AAA/\r\n",
                new String(Base64.encodeBase64Chunked(new byte[] {(byte) 0, (byte) 0, (byte) 63})));
    }

    /** Tests url-safe Base64 against random data, sizes 0 to 150. */
    @Test
    public void testUrlSafe() {
        final BaseNCodec codec = Base64.Base644(true);
        for (int i = 0; i <= 150; i++) {
            final byte[][] randomData = BaseNTestData.randomData(codec, i);
            final byte[] encoded = randomData[1];
            final byte[] decoded = randomData[0];
            final byte[] result = Base64.decodeBase640(encoded);
            assertArrayEquals("url-safe i=" + i, decoded, result);
            assertFalse(
                    "url-safe i=" + i + " no '='", BaseNTestData.bytesContain(encoded, (byte) '='));
            assertFalse(
                    "url-safe i=" + i + " no '\\'",
                    BaseNTestData.bytesContain(encoded, (byte) '\\'));
            assertFalse(
                    "url-safe i=" + i + " no '+'", BaseNTestData.bytesContain(encoded, (byte) '+'));
        }
    }

    /**
     * Base64 encoding of UUID's is a common use-case, especially in URL-SAFE mode. This test case
     * ends up being the "URL-SAFE" JUnit's.
     *
     * @throws DecoderException if Hex.decode() fails - a serious problem since Hex comes from our
     *     own commons-codec!
     */
    @Test
    public void testUUID() throws DecoderException {
        final byte[][] ids = new byte[4][];

        ids[0] = Hex.decodeHex2("94ed8d0319e4493399560fb67404d370");

        ids[1] = Hex.decodeHex2("2bf7cc2701fe4397b49ebeed5acc7090");

        ids[2] = Hex.decodeHex2("64be154b6ffa40258d1a01288e7c31ca");

        ids[3] = Hex.decodeHex2("ff7f8fc01cdb471a8c8b5a9306183fe8");

        final byte[][] standard = new byte[4][];
        standard[0] = StringUtils.getBytesUtf8("lO2NAxnkSTOZVg+2dATTcA==");
        standard[1] = StringUtils.getBytesUtf8("K/fMJwH+Q5e0nr7tWsxwkA==");
        standard[2] = StringUtils.getBytesUtf8("ZL4VS2/6QCWNGgEojnwxyg==");
        standard[3] = StringUtils.getBytesUtf8("/3+PwBzbRxqMi1qTBhg/6A==");

        final byte[][] urlSafe1 = new byte[4][];
        urlSafe1[0] = StringUtils.getBytesUtf8("lO2NAxnkSTOZVg-2dATTcA==");
        urlSafe1[1] = StringUtils.getBytesUtf8("K_fMJwH-Q5e0nr7tWsxwkA==");
        urlSafe1[2] = StringUtils.getBytesUtf8("ZL4VS2_6QCWNGgEojnwxyg==");
        urlSafe1[3] = StringUtils.getBytesUtf8("_3-PwBzbRxqMi1qTBhg_6A==");

        final byte[][] urlSafe2 = new byte[4][];
        urlSafe2[0] = StringUtils.getBytesUtf8("lO2NAxnkSTOZVg-2dATTcA=");
        urlSafe2[1] = StringUtils.getBytesUtf8("K_fMJwH-Q5e0nr7tWsxwkA=");
        urlSafe2[2] = StringUtils.getBytesUtf8("ZL4VS2_6QCWNGgEojnwxyg=");
        urlSafe2[3] = StringUtils.getBytesUtf8("_3-PwBzbRxqMi1qTBhg_6A=");

        final byte[][] urlSafe3 = new byte[4][];
        urlSafe3[0] = StringUtils.getBytesUtf8("lO2NAxnkSTOZVg-2dATTcA");
        urlSafe3[1] = StringUtils.getBytesUtf8("K_fMJwH-Q5e0nr7tWsxwkA");
        urlSafe3[2] = StringUtils.getBytesUtf8("ZL4VS2_6QCWNGgEojnwxyg");
        urlSafe3[3] = StringUtils.getBytesUtf8("_3-PwBzbRxqMi1qTBhg_6A");

        for (int i = 0; i < 4; i++) {
            final byte[] encodedStandard = Base64.encodeBase640(ids[i]);
            final byte[] encodedUrlSafe = Base64.encodeBase64URLSafe(ids[i]);
            final byte[] decodedStandard = Base64.decodeBase640(standard[i]);
            final byte[] decodedUrlSafe1 = Base64.decodeBase640(urlSafe1[i]);
            final byte[] decodedUrlSafe2 = Base64.decodeBase640(urlSafe2[i]);
            final byte[] decodedUrlSafe3 = Base64.decodeBase640(urlSafe3[i]);

            assertArrayEquals("standard encode uuid", encodedStandard, standard[i]);
            assertArrayEquals("url-safe encode uuid", encodedUrlSafe, urlSafe3[i]);
            assertArrayEquals("standard decode uuid", decodedStandard, ids[i]);
            assertArrayEquals("url-safe1 decode uuid", decodedUrlSafe1, ids[i]);
            assertArrayEquals("url-safe2 decode uuid", decodedUrlSafe2, ids[i]);
            assertArrayEquals("url-safe3 decode uuid", decodedUrlSafe3, ids[i]);
        }
    }

    @Test
    public void testByteToStringVariations() throws DecoderException {
        final Base64 base64 = Base64.Base643(0);
        final byte[] b1 = StringUtils.getBytesUtf8("Hello World");
        final byte[] b2 = {};
        final byte[] b3 = null;
        final byte[] b4 = Hex.decodeHex2("2bf7cc2701fe4397b49ebeed5acc7090"); // for

        assertEquals("byteToString Hello World", "SGVsbG8gV29ybGQ=", base64.encodeToString(b1));
        assertEquals(
                "byteToString static Hello World",
                "SGVsbG8gV29ybGQ=",
                Base64.encodeBase64String(b1));
        assertEquals("byteToString \"\"", "", base64.encodeToString(b2));
        assertEquals("byteToString static \"\"", "", Base64.encodeBase64String(b2));
        assertNull("byteToString null", base64.encodeToString(b3));
        assertNull("byteToString static null", Base64.encodeBase64String(b3));
        assertEquals("byteToString UUID", "K/fMJwH+Q5e0nr7tWsxwkA==", base64.encodeToString(b4));
        assertEquals(
                "byteToString static UUID",
                "K/fMJwH+Q5e0nr7tWsxwkA==",
                Base64.encodeBase64String(b4));
        assertEquals(
                "byteToString static-url-safe UUID",
                "K_fMJwH-Q5e0nr7tWsxwkA",
                Base64.encodeBase64URLSafeString(b4));
    }

    @Test
    public void testStringToByteVariations() throws DecoderException {
        final Base64 base64 = Base64.Base645();
        final String s1 = "SGVsbG8gV29ybGQ=\r\n";
        final String s2 = "";
        final String s3 = null;
        final String s4a = "K/fMJwH+Q5e0nr7tWsxwkA==\r\n";
        final String s4b = "K_fMJwH-Q5e0nr7tWsxwkA";
        final byte[] b4 = Hex.decodeHex2("2bf7cc2701fe4397b49ebeed5acc7090"); // for

        assertEquals(
                "StringToByte Hello World",
                "Hello World",
                StringUtils.newStringUtf8(base64.decode3(s1)));
        assertEquals(
                "StringToByte Hello World",
                "Hello World",
                StringUtils.newStringUtf8((byte[]) base64.decode2((Object) s1)));
        assertEquals(
                "StringToByte static Hello World",
                "Hello World",
                StringUtils.newStringUtf8(Base64.decodeBase641(s1)));
        assertEquals("StringToByte \"\"", "", StringUtils.newStringUtf8(base64.decode3(s2)));
        assertEquals(
                "StringToByte static \"\"",
                "",
                StringUtils.newStringUtf8(Base64.decodeBase641(s2)));
        assertNull("StringToByte null", StringUtils.newStringUtf8(base64.decode3(s3)));
        assertNull("StringToByte static null", StringUtils.newStringUtf8(Base64.decodeBase641(s3)));
        assertArrayEquals("StringToByte UUID", b4, base64.decode3(s4b));
        assertArrayEquals("StringToByte static UUID", b4, Base64.decodeBase641(s4a));
        assertArrayEquals("StringToByte static-url-safe UUID", b4, Base64.decodeBase641(s4b));
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

    /**
     * Tests a lineSeparator much bigger than DEFAULT_BUFFER_SIZE.
     *
     * @see "<a
     *     href='https://mail-archives.apache.org/mod_mbox/commons-dev/201202.mbox/%3C4F3C85D7.5060706@snafu.de%3E'>dev@commons.apache.org</a>"
     */
    @Test
    public void testHugeLineSeparator() {
        final int BaseNCodec_DEFAULT_BUFFER_SIZE = 8192;
        final int Base64_BYTES_PER_ENCODED_BLOCK = 4;
        final byte[] baLineSeparator = new byte[BaseNCodec_DEFAULT_BUFFER_SIZE * 4 - 3];
        final Base64 b64 = Base64.Base642(Base64_BYTES_PER_ENCODED_BLOCK, baLineSeparator);
        final String strOriginal = "Hello World";
        final String strDecoded =
                new String(b64.decode0(b64.encode0(StringUtils.getBytesUtf8(strOriginal))));
        assertEquals("testDEFAULT_BUFFER_SIZE", strOriginal, strDecoded);
    }

    @Test
    public void testBase64ImpossibleSamples() {
        final Base64 codec = new Base64(0, null, false, CodecPolicy.STRICT);
        for (final String s : BASE64_IMPOSSIBLE_CASES) {
            try {
                codec.decode3(s);
                fail();
            } catch (final IllegalArgumentException ex) {
            }
        }
    }

    @Test
    public void testBase64DecodingOfTrailing6Bits() {
        assertBase64DecodingOfTrailingBits(6);
    }

    @Test
    public void testBase64DecodingOfTrailing12Bits() {
        assertBase64DecodingOfTrailingBits(12);
    }

    @Test
    public void testBase64DecodingOfTrailing18Bits() {
        assertBase64DecodingOfTrailingBits(18);
    }

    /**
     * Test base 64 decoding of the final trailing bits. Trailing encoded bytes cannot fit exactly
     * into 6-bit characters so the last character has a limited alphabet where the final bits are
     * zero. This asserts that illegal final characters throw an exception when decoding.
     *
     * @param nbits the number of trailing bits (must be a factor of 6 and {@code <24})
     */
    private static void assertBase64DecodingOfTrailingBits(final int nbits) {
        final Base64 codec = new Base64(0, null, false, CodecPolicy.STRICT);
        assertTrue(codec.isStrictDecoding());
        assertEquals(CodecPolicy.STRICT, codec.getCodecPolicy());
        final Base64 defaultCodec = Base64.Base645();
        assertFalse(defaultCodec.isStrictDecoding());
        assertEquals(CodecPolicy.LENIENT, defaultCodec.getCodecPolicy());

        final int length = nbits / 6;
        final byte[] encoded = new byte[4];
        Arrays.fill(encoded, 0, length, STANDARD_ENCODE_TABLE[0]);
        Arrays.fill(encoded, length, encoded.length, (byte) '=');
        final int discard = nbits % 8;
        final int emptyBitsMask = (1 << discard) - 1;
        final boolean invalid = length == 1;
        final int last = length - 1;
        for (int i = 0; i < 64; i++) {
            encoded[last] = STANDARD_ENCODE_TABLE[i];
            if (invalid || (i & emptyBitsMask) != 0) {
                try {
                    codec.decode0(encoded);
                    fail("Final base-64 digit should not be allowed");
                } catch (final IllegalArgumentException ex) {
                }
                final byte[] decoded = defaultCodec.decode0(encoded);
                assertFalse(Arrays.equals(encoded, defaultCodec.encode0(decoded)));
            } else {
                final byte[] decoded = codec.decode0(encoded);
                final int bitsEncoded = i >> discard;
                assertEquals(
                        "Invalid decoding of last character",
                        bitsEncoded,
                        decoded[decoded.length - 1]);
                assertArrayEquals(encoded, codec.encode0(decoded));
            }
        }
    }

    /**
     * Test for CODEC-265: Encode a 1GiB file.
     *
     * @see <a href="https://issues.apache.org/jira/projects/CODEC/issues/CODEC-265">CODEC-265</a>
     */
    @Test
    public void testCodec265() {
        final int size1GiB = 1 << 30;

        final int blocks = (int) Math.ceil(size1GiB / 3.0);
        final int expectedLength = 4 * blocks;

        final long presumableFreeMemory = BaseNCodecTest.getPresumableFreeMemory();

        final long estimatedMemory = (long) size1GiB * 4 + expectedLength + 32 * 1024;
        Assume.assumeTrue(
                "Not enough free memory for the test", presumableFreeMemory > estimatedMemory);

        final byte[] bytes = new byte[size1GiB];
        final byte[] encoded = Base64.encodeBase640(bytes);
        assertEquals(expectedLength, encoded.length);
    }
}
