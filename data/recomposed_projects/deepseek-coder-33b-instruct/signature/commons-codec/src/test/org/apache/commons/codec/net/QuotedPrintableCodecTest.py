from __future__ import annotations
import re
import os
from io import StringIO
import unittest
import pytest
import io
import typing
from typing import *
import unittest
from src.main.org.apache.commons.codec.CharEncoding import *
from src.main.org.apache.commons.codec.DecoderException import *
from src.main.org.apache.commons.codec.EncoderException import *
from src.main.org.apache.commons.codec.net.QuotedPrintableCodec import *


class QuotedPrintableCodecTest(unittest.TestCase):

    RUSSIAN_STUFF_UNICODE: List[int] = [
        0x412,
        0x441,
        0x435,
        0x43C,
        0x5F,
        0x43F,
        0x440,
        0x438,
        0x432,
        0x435,
        0x442,
    ]
    SWISS_GERMAN_STUFF_UNICODE: List[int] = [
        0x47,
        0x72,
        0xFC,
        0x65,
        0x7A,
        0x69,
        0x5F,
        0x7A,
        0xE4,
        0x6D,
        0xE4,
    ]

    def testFinalBytes(self) -> None:

        plain = "This is a example of a quoted=printable text file. There is no tt"
        expected = "This is a example of a quoted=3Dprintable text file. There is no tt"

        self.assertEqual(
            expected, QuotedPrintableCodec.QuotedPrintableCodec3(True).encode1(plain)
        )

    def testUltimateSoftBreak(self) -> None:

        qpcodec = QuotedPrintableCodec.QuotedPrintableCodec3(True)

        plain = (
            "This is a example of a quoted-printable text file. There is no end to it\t"
        )
        expected = "This is a example of a quoted-printable text file. There is no end to i=\r\nt=09"
        self.assertEqual(expected, qpcodec.encode1(plain))

        plain = (
            "This is a example of a quoted-printable text file. There is no end to it "
        )
        expected = "This is a example of a quoted-printable text file. There is no end to i=\r\nt=20"
        self.assertEqual(expected, qpcodec.encode1(plain))

        plain = (
            "This is a example of a quoted-printable text file. There is no end to   "
        )
        expected = "This is a example of a quoted-printable text file. There is no end to=20=\r\n =20"
        self.assertEqual(expected, qpcodec.encode1(plain))

        plain = (
            "This is a example of a quoted-printable text file. There is no end to=  "
        )
        expected = "This is a example of a quoted-printable text file. There is no end to=3D=\r\n =20"
        self.assertEqual(expected, qpcodec.encode1(plain))

    def testTrailingSpecial(self) -> None:

        qpcodec = QuotedPrintableCodec.QuotedPrintableCodec3(True)

        plain = "This is a example of a quoted-printable text file. This might contain sp=cial chars."
        expected = (
            "This is a example of a quoted-printable text file. This might contain sp=3D=\r\n"
            + "cial chars."
        )
        self.assertEqual(expected, qpcodec.encode1(plain))

        plain = "This is a example of a quoted-printable text file. This might contain ta\tbs as well."
        expected = (
            "This is a example of a quoted-printable text file. This might contain ta=09=\r\n"
            + "bs as well."
        )
        self.assertEqual(expected, qpcodec.encode1(plain))

    def testSkipNotEncodedCRLF(self) -> None:

        qpdata = (
            "CRLF in an\n encoded text should be=20=\r\n\rskipped in the\r decoding."
        )
        expected = "CRLF in an encoded text should be skipped in the decoding."

        qpcodec = QuotedPrintableCodec.QuotedPrintableCodec3(True)
        self.assertEqual(expected, qpcodec.decode3(qpdata))

        encoded = qpcodec.encode1(expected)
        self.assertEqual(expected, qpcodec.decode3(encoded))

    def testSoftLineBreakEncode(self) -> None:

        qpdata = (
            "If you believe that truth=3Dbeauty, then surely mathematics is the most b=\r\n"
            + "eautiful branch of philosophy."
        )
        expected = (
            "If you believe that truth=beauty, then surely mathematics is the most beautiful"
            + " branch of philosophy."
        )

        qpcodec = QuotedPrintableCodec.QuotedPrintableCodec3(True)
        self.assertEqual(qpdata, qpcodec.encode1(expected))

        decoded = qpcodec.decode3(qpdata)
        self.assertEqual(qpdata, qpcodec.encode1(decoded))

    def testSoftLineBreakDecode(self) -> None:

        qpdata = (
            "If you believe that truth=3Dbeauty, then surely=20=\r\n"
            + "mathematics is the most beautiful branch of philosophy."
        )
        expected = (
            "If you believe that truth=beauty, then surely mathematics is the most beautiful"
            + " branch of philosophy."
        )

        qpcodec = QuotedPrintableCodec.QuotedPrintableCodec4()
        self.assertEqual(expected, qpcodec.decode3(qpdata))

        encoded = qpcodec.encode1(expected)
        self.assertEqual(expected, qpcodec.decode3(encoded))

    def testDefaultEncoding(self) -> None:

        plain = "Hello there!"
        qpcodec = QuotedPrintableCodec.QuotedPrintableCodec0("UnicodeBig")
        qpcodec.encode1(plain)
        encoded1 = qpcodec.encode4(plain, "UnicodeBig")
        encoded2 = qpcodec.encode1(plain)
        self.assertEqual(encoded1, encoded2)

    def testDecodeObjects(self) -> None:

        qpcodec = QuotedPrintableCodec.QuotedPrintableCodec4()
        plain = "1+1 =3D 2"
        decoded = qpcodec.decode4(plain)
        self.assertEqual("Basic quoted-printable decoding test", "1+1 = 2", decoded)

        plainBA = plain.encode("utf-8")
        decodedBA = qpcodec.decode4(plainBA)
        decoded = decodedBA.decode("utf-8")
        self.assertEqual("Basic quoted-printable decoding test", "1+1 = 2", decoded)

        result = qpcodec.decode4(None)
        self.assertIsNone(result, "Decoding a null Object should return null")

        with self.assertRaises(DecoderException):
            dObj = float(3.0)
            qpcodec.decode4(dObj)

    def testInvalidEncoding(self) -> None:
        with pytest.raises(UnsupportedCharsetException):
            QuotedPrintableCodec.QuotedPrintableCodec0("NONSENSE")

    def testEncodeObjects(self) -> None:

        qpcodec = QuotedPrintableCodec.QuotedPrintableCodec4()
        plain = "1+1 = 2"
        encoded = qpcodec.encode2(plain)
        self.assertEqual("Basic quoted-printable encoding test", "1+1 =3D 2", encoded)

        plainBA = plain.encode("utf-8")
        encodedBA = qpcodec.encode2(plainBA)
        encoded = encodedBA.decode("utf-8")
        self.assertEqual("Basic quoted-printable encoding test", "1+1 =3D 2", encoded)

        result = qpcodec.encode2(None)
        self.assertIsNone(result, "Encoding a null Object should return None")

        with self.assertRaises(EncoderException):
            dObj = float(3.0)
            qpcodec.encode2(dObj)

    def testDecodeStringWithNull(self) -> None:

        qpcodec = QuotedPrintableCodec.QuotedPrintableCodec4()
        test = None
        result = qpcodec.decode2(test, "charset")
        self.assertIsNone(result, "Result should be None")

    def testEncodeStringWithNull(self) -> None:

        qpcodec = QuotedPrintableCodec.QuotedPrintableCodec4()
        test = None
        result = qpcodec.encode4(test, "charset")
        self.assertIsNone(result, "Result should be None")

    def testDecodeWithNullArray(self) -> None:

        plain = None
        result = QuotedPrintableCodec.decodeQuotedPrintable(plain)
        self.assertIsNone(result, "Result should be None")

    def testEncodeUrlWithNullBitSet(self) -> None:

        qpcodec = QuotedPrintableCodec.QuotedPrintableCodec4()
        plain = "1+1 = 2"
        encoded = QuotedPrintableCodec.encodeQuotedPrintable1(
            None, plain.encode("utf-8")
        )
        self.assertEqual(
            "Basic quoted-printable encoding test", "1+1 =3D 2", encoded.decode("utf-8")
        )
        self.assertEqual(
            "Basic quoted-printable decoding test",
            plain,
            qpcodec.decode3(encoded.decode("utf-8")),
        )

    def testEncodeNull(self) -> None:

        qpcodec = QuotedPrintableCodec.QuotedPrintableCodec4()
        plain = None
        encoded = qpcodec.encode0(plain)
        self.assertIsNone(encoded, "Encoding a null string should return None")

    def testDecodeInvalid(self) -> None:

        qpcodec = QuotedPrintableCodec.QuotedPrintableCodec4()

        with pytest.raises(DecoderException):
            qpcodec.decode3("=")

        with pytest.raises(DecoderException):
            qpcodec.decode3("=A")

        with pytest.raises(DecoderException):
            qpcodec.decode3("=WW")

    def testEncodeDecodeNull(self) -> None:

        qpcodec = QuotedPrintableCodec.QuotedPrintableCodec4()
        self.assertIsNone(
            qpcodec.encode1(None), "Null string quoted-printable encoding test"
        )
        self.assertIsNone(
            qpcodec.decode3(None), "Null string quoted-printable decoding test"
        )

    def testUnsafeEncodeDecode(self) -> None:

        qpcodec = QuotedPrintableCodec.QuotedPrintableCodec4()
        plain = "=\r\n"
        encoded = qpcodec.encode1(plain)
        self.assertEqual(
            "Unsafe chars quoted-printable encoding test", "=3D=0D=0A", encoded
        )
        self.assertEqual(
            "Unsafe chars quoted-printable decoding test",
            plain,
            qpcodec.decode3(encoded),
        )

    def testSafeCharEncodeDecode(self) -> None:

        qpcodec = QuotedPrintableCodec.QuotedPrintableCodec4()
        plain = "abc123_-.*~!\"#$%&'()*+,-./:;<=>?@[]^_`{|}~"
        encoded = qpcodec.encode1(plain)
        self.assertEqual("Safe chars quoted-printable encoding test", plain, encoded)
        self.assertEqual(
            "Safe chars quoted-printable decoding test", plain, qpcodec.decode3(encoded)
        )

    def testBasicEncodeDecode(self) -> None:

        qpcodec = QuotedPrintableCodec.QuotedPrintableCodec4()
        plain = "= Hello there =\r\n"
        encoded = qpcodec.encode1(plain)
        self.assertEqual(
            "Basic quoted-printable encoding test", "=3D Hello there =3D=0D=0A", encoded
        )
        self.assertEqual(
            "Basic quoted-printable decoding test", plain, qpcodec.decode3(encoded)
        )

    def testUTF8RoundTrip(self) -> None:

        ru_msg = self.__constructString(self.RUSSIAN_STUFF_UNICODE)
        ch_msg = self.__constructString(self.SWISS_GERMAN_STUFF_UNICODE)

        qpcodec = QuotedPrintableCodec.QuotedPrintableCodec4()

        self.assertEqual(
            "=D0=92=D1=81=D0=B5=D0=BC_=D0=BF=D1=80=D0=B8=D0=B2=D0=B5=D1=82",
            qpcodec.encode4(ru_msg, CharEncoding.UTF_8),
        )
        self.assertEqual(
            "Gr=C3=BCezi_z=C3=A4m=C3=A4", qpcodec.encode4(ch_msg, CharEncoding.UTF_8)
        )

        self.assertEqual(
            ru_msg,
            qpcodec.decode2(
                qpcodec.encode4(ru_msg, CharEncoding.UTF_8), CharEncoding.UTF_8
            ),
        )
        self.assertEqual(
            ch_msg,
            qpcodec.decode2(
                qpcodec.encode4(ch_msg, CharEncoding.UTF_8), CharEncoding.UTF_8
            ),
        )

    def __constructString(self, unicodeChars: typing.List[int]) -> str:

        buffer = io.StringIO()
        if unicodeChars is not None:
            for unicodeChar in unicodeChars:
                buffer.write(chr(unicodeChar))
        return buffer.getvalue()
