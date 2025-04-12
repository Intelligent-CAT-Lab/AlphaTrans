
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

import static org.junit.Assert.*;

import org.apache.commons.codec.CharEncoding;
import org.apache.commons.codec.DecoderException;
import org.apache.commons.codec.EncoderException;
import org.junit.Test;

import java.nio.charset.StandardCharsets;
import java.nio.charset.UnsupportedCharsetException;

/** Quoted-printable codec test cases */
public class QuotedPrintableCodecTest {

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
    public void testUTF8RoundTrip() throws Exception {

        final String ru_msg = constructString(RUSSIAN_STUFF_UNICODE);
        final String ch_msg = constructString(SWISS_GERMAN_STUFF_UNICODE);

        final QuotedPrintableCodec qpcodec = QuotedPrintableCodec.QuotedPrintableCodec4();

        assertEquals(
                "=D0=92=D1=81=D0=B5=D0=BC_=D0=BF=D1=80=D0=B8=D0=B2=D0=B5=D1=82",
                qpcodec.encode4(ru_msg, CharEncoding.UTF_8));
        assertEquals("Gr=C3=BCezi_z=C3=A4m=C3=A4", qpcodec.encode4(ch_msg, CharEncoding.UTF_8));

        assertEquals(
                ru_msg,
                qpcodec.decode2(qpcodec.encode4(ru_msg, CharEncoding.UTF_8), CharEncoding.UTF_8));
        assertEquals(
                ch_msg,
                qpcodec.decode2(qpcodec.encode4(ch_msg, CharEncoding.UTF_8), CharEncoding.UTF_8));
    }

    @Test
    public void testBasicEncodeDecode() throws Exception {
        final QuotedPrintableCodec qpcodec = QuotedPrintableCodec.QuotedPrintableCodec4();
        final String plain = "= Hello there =\r\n";
        final String encoded = qpcodec.encode1(plain);
        assertEquals("Basic quoted-printable encoding test", "=3D Hello there =3D=0D=0A", encoded);
        assertEquals("Basic quoted-printable decoding test", plain, qpcodec.decode3(encoded));
    }

    @Test
    public void testSafeCharEncodeDecode() throws Exception {
        final QuotedPrintableCodec qpcodec = QuotedPrintableCodec.QuotedPrintableCodec4();
        final String plain = "abc123_-.*~!@#$%^&()+{}\"\\;:`,/[]";
        final String encoded = qpcodec.encode1(plain);
        assertEquals("Safe chars quoted-printable encoding test", plain, encoded);
        assertEquals("Safe chars quoted-printable decoding test", plain, qpcodec.decode3(encoded));
    }

    @Test
    public void testUnsafeEncodeDecode() throws Exception {
        final QuotedPrintableCodec qpcodec = QuotedPrintableCodec.QuotedPrintableCodec4();
        final String plain = "=\r\n";
        final String encoded = qpcodec.encode1(plain);
        assertEquals("Unsafe chars quoted-printable encoding test", "=3D=0D=0A", encoded);
        assertEquals(
                "Unsafe chars quoted-printable decoding test", plain, qpcodec.decode3(encoded));
    }

    @Test
    public void testEncodeDecodeNull() throws Exception {
        final QuotedPrintableCodec qpcodec = QuotedPrintableCodec.QuotedPrintableCodec4();
        assertNull("Null string quoted-printable encoding test", qpcodec.encode1((String) null));
        assertNull("Null string quoted-printable decoding test", qpcodec.decode3((String) null));
    }

    @Test
    public void testDecodeInvalid() throws Exception {
        final QuotedPrintableCodec qpcodec = QuotedPrintableCodec.QuotedPrintableCodec4();
        try {
            qpcodec.decode3("=");
            fail("DecoderException should have been thrown");
        } catch (final DecoderException e) {
        }
        try {
            qpcodec.decode3("=A");
            fail("DecoderException should have been thrown");
        } catch (final DecoderException e) {
        }
        try {
            qpcodec.decode3("=WW");
            fail("DecoderException should have been thrown");
        } catch (final DecoderException e) {
        }
    }

    @Test
    public void testEncodeNull() throws Exception {
        final QuotedPrintableCodec qpcodec = QuotedPrintableCodec.QuotedPrintableCodec4();
        final byte[] plain = null;
        final byte[] encoded = qpcodec.encode0(plain);
        assertNull("Encoding a null string should return null", encoded);
    }

    @Test
    public void testEncodeUrlWithNullBitSet() throws Exception {
        final QuotedPrintableCodec qpcodec = QuotedPrintableCodec.QuotedPrintableCodec4();
        final String plain = "1+1 = 2";
        final String encoded =
                new String(
                        QuotedPrintableCodec.encodeQuotedPrintable1(
                                null, plain.getBytes(StandardCharsets.UTF_8)));
        assertEquals("Basic quoted-printable encoding test", "1+1 =3D 2", encoded);
        assertEquals("Basic quoted-printable decoding test", plain, qpcodec.decode3(encoded));
    }

    @Test
    public void testDecodeWithNullArray() throws Exception {
        final byte[] plain = null;
        final byte[] result = QuotedPrintableCodec.decodeQuotedPrintable(plain);
        assertNull("Result should be null", result);
    }

    @Test
    public void testEncodeStringWithNull() throws Exception {
        final QuotedPrintableCodec qpcodec = QuotedPrintableCodec.QuotedPrintableCodec4();
        final String test = null;
        final String result = qpcodec.encode4(test, "charset");
        assertNull("Result should be null", result);
    }

    @Test
    public void testDecodeStringWithNull() throws Exception {
        final QuotedPrintableCodec qpcodec = QuotedPrintableCodec.QuotedPrintableCodec4();
        final String test = null;
        final String result = qpcodec.decode2(test, "charset");
        assertNull("Result should be null", result);
    }

    @Test
    public void testEncodeObjects() throws Exception {
        final QuotedPrintableCodec qpcodec = QuotedPrintableCodec.QuotedPrintableCodec4();
        final String plain = "1+1 = 2";
        String encoded = (String) qpcodec.encode2((Object) plain);
        assertEquals("Basic quoted-printable encoding test", "1+1 =3D 2", encoded);

        final byte[] plainBA = plain.getBytes(StandardCharsets.UTF_8);
        final byte[] encodedBA = (byte[]) qpcodec.encode2((Object) plainBA);
        encoded = new String(encodedBA);
        assertEquals("Basic quoted-printable encoding test", "1+1 =3D 2", encoded);

        final Object result = qpcodec.encode2((Object) null);
        assertNull("Encoding a null Object should return null", result);

        try {
            final Object dObj = Double.valueOf(3.0d);
            qpcodec.encode2(dObj);
            fail("Trying to url encode a Double object should cause an exception.");
        } catch (final EncoderException ee) {
        }
    }

    @Test(expected = UnsupportedCharsetException.class)
    public void testInvalidEncoding() {
        QuotedPrintableCodec.QuotedPrintableCodec0("NONSENSE");
    }

    @Test
    public void testDecodeObjects() throws Exception {
        final QuotedPrintableCodec qpcodec = QuotedPrintableCodec.QuotedPrintableCodec4();
        final String plain = "1+1 =3D 2";
        String decoded = (String) qpcodec.decode4((Object) plain);
        assertEquals("Basic quoted-printable decoding test", "1+1 = 2", decoded);

        final byte[] plainBA = plain.getBytes(StandardCharsets.UTF_8);
        final byte[] decodedBA = (byte[]) qpcodec.decode4((Object) plainBA);
        decoded = new String(decodedBA);
        assertEquals("Basic quoted-printable decoding test", "1+1 = 2", decoded);

        final Object result = qpcodec.decode4((Object) null);
        assertNull("Decoding a null Object should return null", result);

        try {
            final Object dObj = Double.valueOf(3.0d);
            qpcodec.decode4(dObj);
            fail("Trying to url encode a Double object should cause an exception.");
        } catch (final DecoderException ee) {
        }
    }

    @Test
    public void testDefaultEncoding() throws Exception {
        final String plain = "Hello there!";
        final QuotedPrintableCodec qpcodec =
                QuotedPrintableCodec.QuotedPrintableCodec0("UnicodeBig");
        qpcodec.encode1(plain); // To work around a weird quirk in Java 1.2.2
        final String encoded1 = qpcodec.encode4(plain, "UnicodeBig");
        final String encoded2 = qpcodec.encode1(plain);
        assertEquals(encoded1, encoded2);
    }

    @Test
    public void testSoftLineBreakDecode() throws Exception {
        final String qpdata =
                "If you believe that truth=3Dbeauty, then surely=20=\r\n"
                        + "mathematics is the most beautiful branch of philosophy.";
        final String expected =
                "If you believe that truth=beauty, then surely mathematics is the most beautiful"
                        + " branch of philosophy.";

        final QuotedPrintableCodec qpcodec = QuotedPrintableCodec.QuotedPrintableCodec4();
        assertEquals(expected, qpcodec.decode3(qpdata));

        final String encoded = qpcodec.encode1(expected);
        assertEquals(expected, qpcodec.decode3(encoded));
    }

    @Test
    public void testSoftLineBreakEncode() throws Exception {
        final String qpdata =
                "If you believe that truth=3Dbeauty, then surely mathematics is the most b=\r\n"
                        + "eautiful branch of philosophy.";
        final String expected =
                "If you believe that truth=beauty, then surely mathematics is the most beautiful"
                        + " branch of philosophy.";

        final QuotedPrintableCodec qpcodec = QuotedPrintableCodec.QuotedPrintableCodec3(true);
        assertEquals(qpdata, qpcodec.encode1(expected));

        final String decoded = qpcodec.decode3(qpdata);
        assertEquals(qpdata, qpcodec.encode1(decoded));
    }

    @Test
    public void testSkipNotEncodedCRLF() throws Exception {
        final String qpdata =
                "CRLF in an\n encoded text should be=20=\r\n\rskipped in the\r decoding.";
        final String expected = "CRLF in an encoded text should be skipped in the decoding.";

        final QuotedPrintableCodec qpcodec = QuotedPrintableCodec.QuotedPrintableCodec3(true);
        assertEquals(expected, qpcodec.decode3(qpdata));

        final String encoded = qpcodec.encode1(expected);
        assertEquals(expected, qpcodec.decode3(encoded));
    }

    @Test
    public void testTrailingSpecial() throws Exception {
        final QuotedPrintableCodec qpcodec = QuotedPrintableCodec.QuotedPrintableCodec3(true);

        String plain =
                "This is a example of a quoted-printable text file. This might contain sp=cial"
                        + " chars.";
        String expected =
                "This is a example of a quoted-printable text file. This might contain sp=3D=\r\n"
                        + "cial chars.";
        assertEquals(expected, qpcodec.encode1(plain));

        plain =
                "This is a example of a quoted-printable text file. This might contain ta\tbs as"
                        + " well.";
        expected =
                "This is a example of a quoted-printable text file. This might contain ta=09=\r\n"
                        + "bs as well.";
        assertEquals(expected, qpcodec.encode1(plain));
    }

    @Test
    public void testUltimateSoftBreak() throws Exception {
        final QuotedPrintableCodec qpcodec = QuotedPrintableCodec.QuotedPrintableCodec3(true);

        String plain = "This is a example of a quoted-printable text file. There is no end to it\t";
        String expected =
                "This is a example of a quoted-printable text file. There is no end to i=\r\nt=09";

        assertEquals(expected, qpcodec.encode1(plain));

        plain = "This is a example of a quoted-printable text file. There is no end to it ";
        expected =
                "This is a example of a quoted-printable text file. There is no end to i=\r\nt=20";

        assertEquals(expected, qpcodec.encode1(plain));

        plain = "This is a example of a quoted-printable text file. There is no end to   ";
        expected =
                "This is a example of a quoted-printable text file. There is no end to=20=\r\n =20";

        assertEquals(expected, qpcodec.encode1(plain));

        plain = "This is a example of a quoted-printable text file. There is no end to=  ";
        expected =
                "This is a example of a quoted-printable text file. There is no end to=3D=\r\n =20";

        assertEquals(expected, qpcodec.encode1(plain));
    }

    @Test
    public void testFinalBytes() throws Exception {
        final String plain = "This is a example of a quoted=printable text file. There is no tt";
        final String expected =
                "This is a example of a quoted=3Dprintable text file. There is no tt";

        assertEquals(expected, QuotedPrintableCodec.QuotedPrintableCodec3(true).encode1(plain));
    }
}
