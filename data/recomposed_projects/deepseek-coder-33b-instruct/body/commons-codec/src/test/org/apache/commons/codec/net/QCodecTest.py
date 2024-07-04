from __future__ import annotations
import re
import os
import unittest
import pytest
import io
import typing
from typing import *
import unittest
from src.main.org.apache.commons.codec.CharEncoding import *
from src.main.org.apache.commons.codec.DecoderException import *
from src.main.org.apache.commons.codec.EncoderException import *
from src.main.org.apache.commons.codec.net.QCodec import *


class QCodecTest(unittest.TestCase):

    RUSSIAN_STUFF_UNICODE: typing.List[int] = [
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
    SWISS_GERMAN_STUFF_UNICODE: typing.List[int] = [
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

    def testLetUsMakeCloverHappy(self) -> None:
        qcodec = QCodec.QCodec2()
        qcodec.setEncodeBlanks(True)
        self.assertTrue(qcodec.isEncodeBlanks())
        qcodec.setEncodeBlanks(False)
        self.assertFalse(qcodec.isEncodeBlanks())

    def testEncodeDecodeBlanks(self) -> None:

        plain = "Mind those pesky blanks"
        encoded1 = "=?UTF-8?Q?Mind those pesky blanks?="
        encoded2 = "=?UTF-8?Q?Mind_those_pesky_blanks?="
        qcodec = QCodec.QCodec2()
        qcodec.setEncodeBlanks(False)
        s = qcodec.encode2(plain)
        self.assertEqual("Blanks encoding with the Q codec test", encoded1, s)
        qcodec.setEncodeBlanks(True)
        s = qcodec.encode2(plain)
        self.assertEqual("Blanks encoding with the Q codec test", encoded2, s)
        s = qcodec.decode0(encoded1)
        self.assertEqual("Blanks decoding with the Q codec test", plain, s)
        s = qcodec.decode0(encoded2)
        self.assertEqual("Blanks decoding with the Q codec test", plain, s)

    def testDecodeObjects(self) -> None:

        qcodec = QCodec.QCodec2()
        decoded = "=?UTF-8?Q?1+1 =3D 2?="
        plain = qcodec.decode1(decoded)
        self.assertEqual("Basic Q decoding test", "1+1 = 2", plain)

        result = qcodec.decode1(None)
        self.assertIsNone(result, "Decoding a null Object should return null")

        try:
            dObj = float(3.0)
            qcodec.decode1(dObj)
            self.fail("Trying to url encode a Double object should cause an exception.")
        except DecoderException:
            pass

    def testInvalidEncoding(self) -> None:
        with pytest.raises(UnsupportedCharsetException):
            QCodec.QCodec0("NONSENSE")

    def testEncodeObjects(self) -> None:

        qcodec = QCodec.QCodec2()
        plain = "1+1 = 2"
        encoded = qcodec.encode3(plain)
        self.assertEqual("Basic Q encoding test", "=?UTF-8?Q?1+1 =3D 2?=", encoded)

        result = qcodec.encode3(None)
        self.assertIsNone(result, "Encoding a null Object should return None")

        try:
            dObj = float(3.0)
            qcodec.encode3(dObj)
            self.fail("Trying to url encode a Double object should cause an exception.")
        except EncoderException:
            pass

    def testDecodeStringWithNull(self) -> None:

        qcodec = QCodec.QCodec2()
        test = None
        result = qcodec.decode0(test)
        self.assertIsNone(result, "Result should be None")

    def testEncodeStringWithNull(self) -> None:
        qcodec = QCodec.QCodec2()
        test = None
        result = qcodec.encode1(test, "charset")
        self.assertIsNone(result, "Result should be None")

    def testEncodeDecodeNull(self) -> None:

        qcodec = QCodec.QCodec2()

        self.assertIsNone(qcodec.encode2(None), "Null string Q encoding test")
        self.assertIsNone(qcodec.decode0(None), "Null string Q decoding test")

    def testUnsafeEncodeDecode(self) -> None:

        qcodec = QCodec.QCodec2()
        plain = "?_=\r\n"
        encoded = qcodec.encode2(plain)
        self.assertEqual(
            "Unsafe chars Q encoding test", "=?UTF-8?Q?=3F=5F=3D=0D=0A?=", encoded
        )
        self.assertEqual("Unsafe chars Q decoding test", plain, qcodec.decode0(encoded))

    def testBasicEncodeDecode(self) -> None:

        qcodec = QCodec.QCodec2()
        plain = "= Hello there =\r\n"
        encoded = qcodec.encode2(plain)
        self.assertEqual(
            "Basic Q encoding test", "=?UTF-8?Q?=3D Hello there =3D=0D=0A?=", encoded
        )
        self.assertEqual("Basic Q decoding test", plain, qcodec.decode0(encoded))

    def testUTF8RoundTrip(self) -> None:

        ru_msg = self.__constructString(self.RUSSIAN_STUFF_UNICODE)
        ch_msg = self.__constructString(self.SWISS_GERMAN_STUFF_UNICODE)

        qcodec = QCodec.QCodec0(CharEncoding.UTF_8)

        self.assertEqual(
            "=?UTF-8?Q?=D0=92=D1=81=D0=B5=D0=BC=5F=D0=BF=D1=80=D0=B8=D0=B2=D0=B5=D1=82?=",
            qcodec.encode2(ru_msg),
        )
        self.assertEqual(
            "=?UTF-8?Q?Gr=C3=BCezi=5Fz=C3=A4m=C3=A4?=", qcodec.encode2(ch_msg)
        )

        self.assertEqual(ru_msg, qcodec.decode0(qcodec.encode2(ru_msg)))
        self.assertEqual(ch_msg, qcodec.decode0(qcodec.encode2(ch_msg)))

    def testNullInput(self) -> None:

        qcodec = QCodec.QCodec2()
        self.assertIsNone(qcodec.doDecoding(None))
        self.assertIsNone(qcodec.doEncoding(None))

    def __constructString(self, unicodeChars: typing.List[int]) -> str:

        buffer = []
        if unicodeChars is not None:
            for unicodeChar in unicodeChars:
                buffer.append(chr(unicodeChar))
        return "".join(buffer)
