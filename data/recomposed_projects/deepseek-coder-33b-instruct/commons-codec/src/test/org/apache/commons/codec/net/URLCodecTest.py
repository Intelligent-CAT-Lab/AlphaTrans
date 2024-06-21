from __future__ import annotations
import re
import unittest
import pytest
import io
import typing
from typing import *
from src.main.org.apache.commons.codec.CharEncoding import *
from src.main.org.apache.commons.codec.DecoderException import *
from src.main.org.apache.commons.codec.EncoderException import *
from src.main.org.apache.commons.codec.net.URLCodec import *


class URLCodecTest(unittest.TestCase):

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

    def testDefaultEncoding(self) -> None:

        plain = "Hello there!"
        urlCodec = URLCodec("UnicodeBig")
        urlCodec.encode2(plain)  # To work around a weird quirk in Java 1.2.2
        encoded1 = urlCodec.encode1(plain, "UnicodeBig")
        encoded2 = urlCodec.encode2(plain)
        assert encoded1 == encoded2
        self.__validateState(urlCodec)

    def testDecodeObjects(self) -> None:

        urlCodec = URLCodec.URLCodec1()
        plain = "Hello+there%21"
        decoded = urlCodec.decode3(plain)
        assert decoded == "Hello there!"

        plainBA = plain.encode(UTF_8)
        decodedBA = urlCodec.decode3(plainBA)
        decoded = decodedBA.decode(UTF_8)
        assert decoded == "Hello there!"

        result = urlCodec.decode3(None)
        assert result is None

        try:
            dObj = float(3.0)
            urlCodec.decode3(dObj)
            assert (
                False
            ), "Trying to url encode a Double object should cause an exception."
        except DecoderException:
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

        urlCodec = URLCodec.URLCodec1()
        plain = "Hello there!"
        encoded = urlCodec.encode3(plain)
        assert encoded == "Hello+there%21", "Basic URL encoding test"

        plainBA = plain.encode(UTF_8)
        encodedBA = urlCodec.encode3(plainBA)
        encoded = encodedBA.decode(UTF_8)
        assert encoded == "Hello+there%21", "Basic URL encoding test"

        result = urlCodec.encode3(None)
        assert result is None, "Encoding a null Object should return null"

        try:
            dObj = float(3.0)
            urlCodec.encode3(dObj)
            assert (
                False
            ), "Trying to url encode a Double object should cause an exception."
        except EncoderException:
            pass
        self.__validateState(urlCodec)

    def testDecodeStringWithNull(self) -> None:

        urlCodec = URLCodec.URLCodec1()
        test = None
        result = urlCodec.decode1(test, "charset")
        assert result is None, "Result should be None"

    def testEncodeStringWithNull(self) -> None:

        urlCodec = URLCodec.URLCodec1()
        test = None
        result = urlCodec.encode1(test, "charset")
        assert result is None, "Result should be None"

    def testDecodeWithNullArray(self) -> None:

        plain = None
        result = URLCodec.decodeUrl(plain)
        assert result is None, "Result should be None"

    def testEncodeUrlWithNullBitSet(self) -> None:

        urlCodec = URLCodec.URLCodec1()
        plain = "Hello there!"
        encoded = URLCodec.encodeUrl(None, plain.encode(UTF_8))
        assert encoded.decode(UTF_8) == "Hello+there%21", "Basic URL encoding test"
        assert (
            urlCodec.decode2(encoded.decode(UTF_8)) == plain
        ), "Basic URL decoding test"
        self.__validateState(urlCodec)

    def testEncodeNull(self) -> None:

        urlCodec = URLCodec.URLCodec1()
        plain = None
        encoded = urlCodec.encode0(plain)
        assert encoded is None, "Encoding a null string should return None"
        self.__validateState(urlCodec)

    def testDecodeInvalidContent(self) -> None:

        ch_msg = self.__constructString(self.SWISS_GERMAN_STUFF_UNICODE)
        urlCodec = URLCodec.URLCodec1()
        input = ch_msg.encode("ISO-8859-1")
        output = urlCodec.decode0(input)
        assert len(input) == len(output)
        for i in range(len(input)):
            assert input[i] == output[i]
        self.__validateState(urlCodec)

    def testDecodeInvalid(self) -> None:

        urlCodec = URLCodec.URLCodec1()
        try:
            urlCodec.decode2("%")
            assert False, "DecoderException should have been thrown"
        except DecoderException:
            pass
        try:
            urlCodec.decode2("%A")
            assert False, "DecoderException should have been thrown"
        except DecoderException:
            pass
        try:
            urlCodec.decode2("%WW")
            assert False, "DecoderException should have been thrown"
        except DecoderException:
            pass
        try:
            urlCodec.decode2("%0W")
            assert False, "DecoderException should have been thrown"
        except DecoderException:
            pass
        self.__validateState(urlCodec)

    def testEncodeDecodeNull(self) -> None:

        urlCodec = URLCodec.URLCodec1()
        assert urlCodec.encode2(None) is None, "Null string URL encoding test"
        assert urlCodec.decode2(None) is None, "Null string URL decoding test"
        self.__validateState(urlCodec)

    def testUnsafeEncodeDecode(self) -> None:

        pass  # LLM could not translate this method

    def testSafeCharEncodeDecode(self) -> None:

        urlCodec = URLCodec.URLCodec1()
        plain = "abc123_-.*"
        encoded = urlCodec.encode2(plain)
        assert encoded == plain, "Safe chars URL encoding test"
        assert urlCodec.decode2(encoded) == plain, "Safe chars URL decoding test"
        self.__validateState(urlCodec)

    def testBasicEncodeDecode(self) -> None:

        urlCodec = URLCodec.URLCodec1()
        plain = "Hello there!"
        encoded = urlCodec.encode2(plain)
        assert encoded == "Hello+there%21", "Basic URL encoding test"
        assert plain == urlCodec.decode2(encoded), "Basic URL decoding test"
        self.__validateState(urlCodec)

    def testUTF8RoundTrip(self) -> None:

        ru_msg = self.__constructString(self.RUSSIAN_STUFF_UNICODE)
        ch_msg = self.__constructString(self.SWISS_GERMAN_STUFF_UNICODE)

        urlCodec = URLCodec.URLCodec1()
        self.__validateState(urlCodec)

        assert (
            "%D0%92%D1%81%D0%B5%D0%BC_%D0%BF%D1%80%D0%B8%D0%B2%D0%B5%D1%82"
            == urlCodec.encode1(ru_msg, CharEncoding.UTF_8)
        )
        assert "Gr%C3%BCezi_z%C3%A4m%C3%A4" == urlCodec.encode1(
            ch_msg, CharEncoding.UTF_8
        )

        assert ru_msg == urlCodec.decode1(
            urlCodec.encode1(ru_msg, CharEncoding.UTF_8), CharEncoding.UTF_8
        )
        assert ch_msg == urlCodec.decode1(
            urlCodec.encode1(ch_msg, CharEncoding.UTF_8), CharEncoding.UTF_8
        )
        self.__validateState(urlCodec)

    def __constructString(self, unicodeChars: typing.List[int]) -> str:

        buffer = io.StringIO()
        if unicodeChars is not None:
            for unicodeChar in unicodeChars:
                buffer.write(chr(unicodeChar))
        return buffer.getvalue()

    def __validateState(self, urlCodec: URLCodec) -> None:

        pass
