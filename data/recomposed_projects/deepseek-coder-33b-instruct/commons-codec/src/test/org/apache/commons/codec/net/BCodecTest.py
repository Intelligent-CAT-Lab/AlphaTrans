from __future__ import annotations
import re
import unittest
import pytest
import io
import typing
from typing import *
import os
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
        assert codec.isStrictDecoding()
        for s in self.__BASE64_IMPOSSIBLE_CASES:
            try:
                codec.decode0(s)
                assert False, "Expected an exception for impossible case"
            except DecoderException:
                pass

    def testBase64ImpossibleSamplesLenient(self) -> None:

        codec = BCodec(StandardCharsets.UTF_8, CodecPolicy.LENIENT)
        assert not codec.isStrictDecoding()
        for s in self.__BASE64_IMPOSSIBLE_CASES:
            codec.decode0(s)

    def testBase64ImpossibleSamplesDefault(self) -> None:

        codec = BCodec.BCodec0()
        assert not codec.isStrictDecoding()
        for s in self.__BASE64_IMPOSSIBLE_CASES:
            try:
                codec.decode0(s)
            except DecoderException:
                pass

    def testDecodeObjects(self) -> None:

        bcodec = BCodec.BCodec0()
        decoded = "=?UTF-8?B?d2hhdCBub3Q=?="
        plain = bcodec.decode1(decoded)
        assert plain == "what not", "Basic B decoding test"

        result = bcodec.decode1(None)
        assert result is None, "Decoding a null Object should return null"

        try:
            dObj = 3.0
            bcodec.decode1(dObj)
            assert (
                False
            ), "Trying to url encode a Double object should cause an exception."
        except DecoderException:
            pass

    def testInvalidEncoding(self) -> None:

        try:
            BCodec.BCodec2("NONSENSE")
        except Exception as e:
            print(f"An error occurred: {e}")

    def testEncodeObjects(self) -> None:

        bcodec = BCodec.BCodec0()
        plain = "what not"
        encoded = bcodec.encode3(plain)

        assert encoded == "=?UTF-8?B?d2hhdCBub3Q=?=", "Basic B encoding test"

        result = bcodec.encode3(None)
        assert result is None, "Encoding a null Object should return null"

        try:
            dObj = float(3.0)
            bcodec.encode3(dObj)
            assert (
                False
            ), "Trying to url encode a Double object should cause an exception."
        except EncoderException:
            pass

    def testDecodeStringWithNull(self) -> None:

        bcodec = BCodec.BCodec0()
        test = None
        result = bcodec.decode0(test)
        assert result is None, "Result should be None"

    def testEncodeStringWithNull(self) -> None:

        bcodec = BCodec.BCodec0()
        test = None
        result = bcodec.encode1(test, "charset")
        assert result is None, "Result should be None"

    def testEncodeDecodeNull(self) -> None:

        bcodec = BCodec.BCodec0()
        assert bcodec.encode2(None) is None, "Null string B encoding test"
        assert bcodec.decode0(None) is None, "Null string B decoding test"

    def testBasicEncodeDecode(self) -> None:

        bcodec = BCodec.BCodec0()
        plain = "Hello there"
        encoded = bcodec.encode2(plain)
        assert encoded == "=?UTF-8?B?SGVsbG8gdGhlcmU=?=", "Basic B encoding test"
        assert bcodec.decode0(encoded) == plain, "Basic B decoding test"

    def testUTF8RoundTrip(self) -> None:

        ru_msg = self.__constructString(self.RUSSIAN_STUFF_UNICODE)
        ch_msg = self.__constructString(self.SWISS_GERMAN_STUFF_UNICODE)

        bcodec = BCodec.BCodec2(CharEncoding.UTF_8)

        assert "=?UTF-8?B?0JLRgdC10Lxf0L/RgNC40LLQtdGC?=" == bcodec.encode2(ru_msg)
        assert "=?UTF-8?B?R3LDvGV6aV96w6Rtw6Q=?=" == bcodec.encode2(ch_msg)

        assert ru_msg == bcodec.decode0(bcodec.encode2(ru_msg))
        assert ch_msg == bcodec.decode0(bcodec.encode2(ch_msg))

    def testNullInput(self) -> None:

        bcodec = BCodec.BCodec0()
        assert bcodec.doDecoding(None) is None
        assert bcodec.doEncoding(None) is None

    def __constructString(self, unicodeChars: typing.List[int]) -> str:

        buffer = io.StringIO()
        if unicodeChars is not None:
            for unicodeChar in unicodeChars:
                buffer.write(chr(unicodeChar))
        return buffer.getvalue()
