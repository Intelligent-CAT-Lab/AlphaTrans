from __future__ import annotations
import re
import unittest
import pytest
import io
import typing
from typing import *
import os
import unittest
from src.main.org.apache.commons.codec.CharEncoding import *
from src.main.org.apache.commons.codec.CodecPolicy import *
from src.main.org.apache.commons.codec.DecoderException import *
from src.main.org.apache.commons.codec.EncoderException import *
from src.main.org.apache.commons.codec.net.BCodec import *


class BCodecTest(unittest.TestCase):

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
    __BASE64_IMPOSSIBLE_CASES: typing.List[str] = [
        "=?ASCII?B?ZE==?=",
        "=?ASCII?B?ZmC=?=",
        "=?ASCII?B?Zm9vYE==?=",
        "=?ASCII?B?Zm9vYmC=?=",
        "=?ASCII?B?AB==?=",
    ]

    def testBase64ImpossibleSamplesStrict(self) -> None:
        codec = BCodec(StandardCharsets.UTF_8, CodecPolicy.STRICT)
        self.assertTrue(codec.isStrictDecoding())
        for s in self.__BASE64_IMPOSSIBLE_CASES:
            try:
                codec.decode0(s)
                self.fail("Expected an exception for impossible case")
            except DecoderException as ex:
                pass

    def testBase64ImpossibleSamplesLenient(self) -> None:
        codec = BCodec(StandardCharsets.UTF_8, CodecPolicy.LENIENT)
        self.assertFalse(codec.isStrictDecoding())
        for s in self.__BASE64_IMPOSSIBLE_CASES:
            codec.decode0(s)

    def testBase64ImpossibleSamplesDefault(self) -> None:
        codec: BCodec = BCodec.BCodec0()
        self.assertFalse(codec.isStrictDecoding())
        for s in self.__BASE64_IMPOSSIBLE_CASES:
            codec.decode0(s)

    def testDecodeObjects(self) -> None:
        bcodec: BCodec = BCodec.BCodec0()
        decoded: str = "=?UTF-8?B?d2hhdCBub3Q=?="
        plain: str = typing.cast(str, bcodec.decode1(decoded))
        self.assertEqual("Basic B decoding test", "what not", plain)

        result: typing.Any = bcodec.decode1(None)
        self.assertIsNone("Decoding a null Object should return null", result)

        try:
            dObj: typing.Any = Double.valueOf(3.0)
            bcodec.decode1(dObj)
            self.fail("Trying to url encode a Double object should cause an exception.")
        except DecoderException as ee:
            pass

    def testInvalidEncoding(self) -> None:
        with self.assertRaises(UnsupportedCharsetException):
            BCodec.BCodec2("NONSENSE")

    def testEncodeObjects(self) -> None:

        pass  # LLM could not translate this method

    def testDecodeStringWithNull(self) -> None:
        bcodec: BCodec = BCodec.BCodec0()
        test: str = None
        result: str = bcodec.decode0(test)
        self.assertIsNone(result, "Result should be null")

    def testEncodeStringWithNull(self) -> None:
        bcodec = BCodec.BCodec0()
        test = None
        result = bcodec.encode1(test, "charset")
        self.assertIsNone(result, "Result should be null")

    def testEncodeDecodeNull(self) -> None:
        bcodec = BCodec.BCodec0()
        self.assertIsNone("Null string B encoding test", bcodec.encode2(None))
        self.assertIsNone("Null string B decoding test", bcodec.decode0(None))

    def testBasicEncodeDecode(self) -> None:
        bcodec = BCodec.BCodec0()
        plain = "Hello there"
        encoded = bcodec.encode2(plain)
        self.assertEqual(
            "Basic B encoding test", "=?UTF-8?B?SGVsbG8gdGhlcmU=?=", encoded
        )
        self.assertEqual("Basic B decoding test", plain, bcodec.decode0(encoded))

    def testUTF8RoundTrip(self) -> None:
        ru_msg: str = self.__constructString(self.RUSSIAN_STUFF_UNICODE)
        ch_msg: str = self.__constructString(self.SWISS_GERMAN_STUFF_UNICODE)

        bcodec: BCodec = BCodec.BCodec2(CharEncoding.UTF_8)

        self.assertEqual(
            "=?UTF-8?B?0JLRgdC10Lxf0L/RgNC40LLQtdGC?=", bcodec.encode2(ru_msg)
        )
        self.assertEqual("=?UTF-8?B?R3LDvGV6aV96w6Rtw6Q=?=", bcodec.encode2(ch_msg))

        self.assertEqual(ru_msg, bcodec.decode0(bcodec.encode2(ru_msg)))
        self.assertEqual(ch_msg, bcodec.decode0(bcodec.encode2(ch_msg)))

    def testNullInput(self) -> None:
        bcodec = BCodec.BCodec0()
        self.assertIsNone(bcodec.doDecoding(None))
        self.assertIsNone(bcodec.doEncoding(None))

    def __constructString(self, unicodeChars: typing.List[int]) -> str:
        buffer = StringBuilder()
        if unicodeChars is not None:
            for unicodeChar in unicodeChars:
                buffer.append(chr(unicodeChar))
        return buffer.toString()
