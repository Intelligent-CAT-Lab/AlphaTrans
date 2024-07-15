from __future__ import annotations
import re
import unittest
import pytest
import io
import typing
from typing import *
import unittest
from src.main.org.apache.commons.codec.CharEncoding import *
from src.main.org.apache.commons.codec.DecoderException import *
from src.main.org.apache.commons.codec.EncoderException import *
from src.main.org.apache.commons.codec.net.URLCodec import *


class URLCodecTest(unittest.TestCase):

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

    def testDefaultEncoding(self) -> None:
        plain: str = "Hello there!"
        urlCodec: URLCodec = URLCodec("UnicodeBig")
        urlCodec.encode2(plain)  # To work around a weird quirk in Java 1.2.2
        encoded1: str = urlCodec.encode1(plain, "UnicodeBig")
        encoded2: str = urlCodec.encode2(plain)
        self.assertEqual(encoded1, encoded2)
        self.__validateState(urlCodec)

    def testDecodeObjects(self) -> None:
        urlCodec: URLCodec = URLCodec.URLCodec1()
        plain: str = "Hello+there%21"
        decoded: str = typing.cast(
            str, urlCodec.decode3(typing.cast(typing.Any, plain))
        )
        self.assertEqual("Basic URL decoding test", "Hello there!", decoded)

        plainBA: typing.List[int] = plain.encode(StandardCharsets.UTF_8)
        decodedBA: typing.List[int] = typing.cast(
            typing.List[int], urlCodec.decode3(typing.cast(typing.Any, plainBA))
        )
        decoded: str = str(decodedBA)
        self.assertEqual("Basic URL decoding test", "Hello there!", decoded)

        result: typing.Any = urlCodec.decode3(typing.cast(typing.Any, None))
        self.assertIsNone("Decoding a null Object should return null", result)

        try:
            dObj: typing.Any = Double.valueOf(3.0)
            urlCodec.decode3(dObj)
            self.fail("Trying to url encode a Double object should cause an exception.")
        except DecoderException as ee:
            pass
        self.__validateState(urlCodec)

    def testInvalidEncoding(self) -> None:
        urlCodec = URLCodec("NONSENSE")
        plain = "Hello there!"
        try:
            urlCodec.encode2(plain)
            self.fail(
                "We set the encoding to a bogus NONSENSE vlaue, this shouldn't have worked."
            )
        except EncoderException as ee:
            pass
        try:
            urlCodec.decode2(plain)
            self.fail(
                "We set the encoding to a bogus NONSENSE vlaue, this shouldn't have worked."
            )
        except DecoderException as ee:
            pass
        self.__validateState(urlCodec)

    def testEncodeObjects(self) -> None:
        urlCodec: URLCodec = URLCodec.URLCodec1()
        plain: str = "Hello there!"
        encoded: str = typing.cast(
            str, urlCodec.encode3(typing.cast(typing.Any, plain))
        )
        self.assertEqual("Basic URL encoding test", "Hello+there%21", encoded)

        plainBA: typing.List[int] = plain.encode(StandardCharsets.UTF_8)
        encodedBA: typing.List[int] = typing.cast(
            typing.List[int], urlCodec.encode3(typing.cast(typing.Any, plainBA))
        )
        encoded: str = str(encodedBA)
        self.assertEqual("Basic URL encoding test", "Hello+there%21", encoded)

        result: typing.Any = urlCodec.encode3(typing.cast(typing.Any, None))
        self.assertIsNone("Encoding a null Object should return null", result)

        try:
            dObj: typing.Any = Double.valueOf(3.0)
            urlCodec.encode3(dObj)
            self.fail("Trying to url encode a Double object should cause an exception.")
        except EncoderException as ee:
            pass
        self.__validateState(urlCodec)

    def testDecodeStringWithNull(self) -> None:
        urlCodec = URLCodec.URLCodec1()
        test = None
        result = urlCodec.decode1(test, "charset")
        self.assertIsNone(result, "Result should be null")

    def testEncodeStringWithNull(self) -> None:
        urlCodec = URLCodec.URLCodec1()
        test = None
        result = urlCodec.encode1(test, "charset")
        self.assertIsNone(result, "Result should be null")

    def testDecodeWithNullArray(self) -> None:
        plain: typing.List[int] = None
        result: typing.List[int] = URLCodec.decodeUrl(plain)
        self.assertIsNone(result, "Result should be null")

    def testEncodeUrlWithNullBitSet(self) -> None:
        urlCodec: URLCodec = URLCodec.URLCodec1()
        plain: str = "Hello there!"
        encoded: str = str(
            URLCodec.encodeUrl(None, plain.encode(StandardCharsets.UTF_8))
        )
        self.assertEqual("Basic URL encoding test", "Hello+there%21", encoded)
        self.assertEqual("Basic URL decoding test", plain, urlCodec.decode2(encoded))
        self.__validateState(urlCodec)

    def testEncodeNull(self) -> None:
        urlCodec: URLCodec = URLCodec.URLCodec1()
        plain: typing.List[int] = None
        encoded: typing.List[int] = urlCodec.encode0(plain)
        self.assertIsNone(encoded, "Encoding a null string should return null")
        self.__validateState(urlCodec)

    def testDecodeInvalidContent(self) -> None:
        ch_msg = self.__constructString(self.SWISS_GERMAN_STUFF_UNICODE)
        urlCodec = URLCodec.URLCodec1()
        input = ch_msg.encode(StandardCharsets.ISO_8859_1)
        output = urlCodec.decode0(input)
        self.assertEqual(len(input), len(output))
        for i in range(len(input)):
            self.assertEqual(input[i], output[i])
        self.__validateState(urlCodec)

    def testDecodeInvalid(self) -> None:
        urlCodec: URLCodec = URLCodec.URLCodec1()
        try:
            urlCodec.decode2("%")
            self.fail("DecoderException should have been thrown")
        except DecoderException as e:
            pass
        try:
            urlCodec.decode2("%A")
            self.fail("DecoderException should have been thrown")
        except DecoderException as e:
            pass
        try:
            urlCodec.decode2("%WW")
            self.fail("DecoderException should have been thrown")
        except DecoderException as e:
            pass
        try:
            urlCodec.decode2("%0W")
            self.fail("DecoderException should have been thrown")
        except DecoderException as e:
            pass
        self.__validateState(urlCodec)

    def testEncodeDecodeNull(self) -> None:

        pass  # LLM could not translate this method

    def testUnsafeEncodeDecode(self) -> None:
        urlCodec: URLCodec = URLCodec.URLCodec1()
        plain: str = '~!@#$%^&()+{}"\\;:`,/[]'
        encoded: str = urlCodec.encode2(plain)
        self.assertEqual(
            "Unsafe chars URL encoding test",
            "%7E%21%40%23%24%25%5E%26%28%29%2B%7B%7D%22%5C%3B%3A%60%2C%2F%5B%5D",
            encoded,
        )
        self.assertEqual(
            "Unsafe chars URL decoding test", plain, urlCodec.decode2(encoded)
        )
        self.__validateState(urlCodec)

    def testSafeCharEncodeDecode(self) -> None:
        urlCodec: URLCodec = URLCodec.URLCodec1()
        plain: str = "abc123_-.*"
        encoded: str = urlCodec.encode2(plain)
        self.assertEqual("Safe chars URL encoding test", plain, encoded)
        self.assertEqual(
            "Safe chars URL decoding test", plain, urlCodec.decode2(encoded)
        )
        self.__validateState(urlCodec)

    def testBasicEncodeDecode(self) -> None:
        urlCodec: URLCodec = URLCodec.URLCodec1()
        plain: str = "Hello there!"
        encoded: str = urlCodec.encode2(plain)
        self.assertEqual("Basic URL encoding test", "Hello+there%21", encoded)
        self.assertEqual("Basic URL decoding test", plain, urlCodec.decode2(encoded))
        self.__validateState(urlCodec)

    def testUTF8RoundTrip(self) -> None:
        ru_msg: str = self.__constructString(URLCodecTest.RUSSIAN_STUFF_UNICODE)
        ch_msg: str = self.__constructString(URLCodecTest.SWISS_GERMAN_STUFF_UNICODE)

        urlCodec: URLCodec = URLCodec.URLCodec1()
        self.__validateState(urlCodec)

        self.assertEqual(
            "%D0%92%D1%81%D0%B5%D0%BC_%D0%BF%D1%80%D0%B8%D0%B2%D0%B5%D1%82",
            urlCodec.encode1(ru_msg, CharEncoding.UTF_8),
        )
        self.assertEqual(
            "Gr%C3%BCezi_z%C3%A4m%C3%A4", urlCodec.encode1(ch_msg, CharEncoding.UTF_8)
        )

        self.assertEqual(
            ru_msg,
            urlCodec.decode1(
                urlCodec.encode1(ru_msg, CharEncoding.UTF_8), CharEncoding.UTF_8
            ),
        )
        self.assertEqual(
            ch_msg,
            urlCodec.decode1(
                urlCodec.encode1(ch_msg, CharEncoding.UTF_8), CharEncoding.UTF_8
            ),
        )
        self.__validateState(urlCodec)

    def __constructString(self, unicodeChars: typing.List[int]) -> str:
        buffer = StringBuilder()
        if unicodeChars is not None:
            for unicodeChar in unicodeChars:
                buffer.append(chr(unicodeChar))
        return buffer.toString()

    def __validateState(self, urlCodec: URLCodec) -> None:
        self.assertEqual(urlCodec.getEncoding(), CharEncoding.ISO_8859_1)
        self.assertEqual(urlCodec.getDefaultCharset(), CharEncoding.ISO_8859_1)
        self.assertEqual(urlCodec.getSafeChars(), URLCodec.URL_SAFE_CHARS)
        self.assertEqual(urlCodec.isEncodeBlanks(), False)
        self.assertEqual(urlCodec.isEncodeEquals(), False)
        self.assertEqual(urlCodec.isEncodePlus(), False)
        self.assertEqual(urlCodec.isEncodeSlash(), False)
        self.assertEqual(urlCodec.isEncodeSpaceAsPlus(), False)
        self.assertEqual(urlCodec.isEncodeUnsafe(), False)
        self.assertEqual(urlCodec.isUseStandardCharacterEncoding(), False)
