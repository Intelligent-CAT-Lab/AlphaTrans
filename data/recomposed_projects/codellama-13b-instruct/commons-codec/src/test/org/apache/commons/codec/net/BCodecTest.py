# Imports Begin
from src.main.org.apache.commons.codec.net.BCodec import *
from src.main.org.apache.commons.codec.EncoderException import *
from src.main.org.apache.commons.codec.DecoderException import *
from src.main.org.apache.commons.codec.CodecPolicy import *
from src.main.org.apache.commons.codec.CharEncoding import *
import unittest
import os
import typing
from typing import *

# Imports End


class BCodecTest(unittest.TestCase):

    # Class Fields Begin
    __BASE64_IMPOSSIBLE_CASES: List[str] = [
        "=?ASCII?B?ZE==?=",
        "=?ASCII?B?ZmC=?=",
        "=?ASCII?B?Zm9vYE==?=",
        "=?ASCII?B?Zm9vYmC=?=",
        "=?ASCII?B?AB==?=",
    ]
    SWISS_GERMAN_STUFF_UNICODE: List = [
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
    RUSSIAN_STUFF_UNICODE: List = [
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
    # Class Fields End

    # Class Methods Begin
    def testBase64ImpossibleSamplesStrict(self) -> None:

        codec = BCodec(
            charset=StandardCharsets.UTF_8, decodingPolicy=CodecPolicy.STRICT
        )
        self.assertTrue(codec.isStrictDecoding())
        for s in BASE64_IMPOSSIBLE_CASES:
            try:
                codec.decode0(s)
                self.fail("Expected an exception for impossible case")
            except DecoderException:
                pass

    def testBase64ImpossibleSamplesLenient(self) -> None:

        codec = BCodec(
            charset=StandardCharsets.UTF_8, decodingPolicy=CodecPolicy.LENIENT
        )
        self.assertFalse(codec.isStrictDecoding())
        for s in BASE64_IMPOSSIBLE_CASES:
            codec.decode0(s)

    def testBase64ImpossibleSamplesDefault(self) -> None:

        pass  # LLM could not translate method body

    def testDecodeObjects(self) -> None:

        pass  # LLM could not translate method body

    def testInvalidEncoding(self) -> None:

        BCodec.BCodec2("NONSENSE")

    def testEncodeObjects(self) -> None:

        bcodec = BCodec.BCodec0()
        plain = "what not"
        encoded = bcodec.encode3(plain)
        assert encoded == "=?UTF-8?B?d2hhdCBub3Q=?="
        result = bcodec.encode3(None)
        assert result is None
        try:
            d_obj = 3.0
            bcodec.encode3(d_obj)
            fail("Trying to url encode a Double object should cause an exception.")
        except EncoderException:
            pass

    def testDecodeStringWithNull(self) -> None:

        bcodec = BCodec.BCodec0()
        test = None
        result = bcodec.decode0(test)
        assertNull("Result should be null", result)

    def testEncodeStringWithNull(self) -> None:

        bcodec = BCodec.BCodec0()
        test = None
        result = bcodec.encode1(test, "charset")
        self.assertIsNone(result)

    def testEncodeDecodeNull(self) -> None:

        bcodec = BCodec.BCodec0()
        assertNull("Null string B encoding test", bcodec.encode2(None))
        assertNull("Null string B decoding test", bcodec.decode0(None))

    def testBasicEncodeDecode(self) -> None:

        bcodec = BCodec.BCodec0()
        plain = "Hello there"
        encoded = bcodec.encode2(plain)
        self.assertEqual(
            "Basic B encoding test", "=?UTF-8?B?SGVsbG8gdGhlcmU=?=", encoded
        )
        self.assertEqual("Basic B decoding test", plain, bcodec.decode0(encoded))

    def testUTF8RoundTrip(self) -> None:

        ru_msg = self.__constructString(self.RUSSIAN_STUFF_UNICODE)
        ch_msg = self.__constructString(self.SWISS_GERMAN_STUFF_UNICODE)
        bcodec = BCodec.BCodec2(CharEncoding.UTF_8)
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

        buffer = ""
        if unicodeChars is not None:
            for unicodeChar in unicodeChars:
                buffer += chr(unicodeChar)
        return buffer

    # Class Methods End
