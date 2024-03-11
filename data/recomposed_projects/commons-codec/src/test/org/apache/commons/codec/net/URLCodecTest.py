# Imports Begin
from src.main.org.apache.commons.codec.net.URLCodec import *
from src.main.org.apache.commons.codec.EncoderException import *
from src.main.org.apache.commons.codec.DecoderException import *
from src.main.org.apache.commons.codec.CharEncoding import *
import unittest
import typing
from typing import *

# Imports End


class URLCodecTest(unittest.TestCase):

    # Class Fields Begin
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
        self.assertEqual("Basic URL decoding test", "Hello there!", decoded)
        plainBA = plain.encode("utf-8")
        decodedBA = urlCodec.decode3(plainBA)
        decoded = decodedBA.decode("utf-8")
        self.assertEqual("Basic URL decoding test", "Hello there!", decoded)
        result = urlCodec.decode3(None)
        assertNull("Decoding a null Object should return null", result)
        try:
            dObj = Double(3.0)
            urlCodec.decode3(dObj)
            fail("Trying to url encode a Double object should cause an exception.")
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
        except EncoderException:
            pass
        try:
            urlCodec.decode2(plain)
            self.fail(
                "We set the encoding to a bogus NONSENSE vlaue, this shouldn't have worked."
            )
        except DecoderException:
            pass
        self.__validateState(urlCodec)

    def testEncodeObjects(self) -> None:

        url_codec = URLCodec.URLCodec1()
        plain = "Hello there!"
        encoded = url_codec.encode3(plain)
        assert encoded == "Hello+there%21"
        plain_ba = plain.encode("utf-8")
        encoded_ba = url_codec.encode3(plain_ba)
        encoded = encoded_ba.decode("utf-8")
        assert encoded == "Hello+there%21"
        result = url_codec.encode3(None)
        assert result is None
        try:
            d_obj = 3.0
            url_codec.encode3(d_obj)
            fail("Trying to url encode a Double object should cause an exception.")
        except EncoderException:
            pass
        self.validateState(url_codec)

    def testDecodeStringWithNull(self) -> None:

        urlCodec = URLCodec.URLCodec1()
        test = None
        result = urlCodec.decode1(test, "charset")
        self.assertIsNone(result)

    def testEncodeStringWithNull(self) -> None:

        url_codec = URLCodec.URLCodec1()
        test = None
        result = url_codec.encode1(test, "charset")
        self.assertIsNone(result)

    def testDecodeWithNullArray(self) -> None:

        plain = None
        result = URLCodec.decodeUrl(plain)
        self.assertIsNone(result)

    def testEncodeUrlWithNullBitSet(self) -> None:

        urlCodec = URLCodec.URLCodec1()
        plain = "Hello there!"
        encoded = URLCodec.encodeUrl(None, plain.encode("utf-8"))
        self.assertEqual("Basic URL encoding test", "Hello+there%21", encoded)
        self.assertEqual("Basic URL decoding test", plain, urlCodec.decode2(encoded))
        self.__validateState(urlCodec)

    def testEncodeNull(self) -> None:

        urlCodec = URLCodec.URLCodec1()
        plain = None
        encoded = urlCodec.encode0(plain)
        assertNull("Encoding a null string should return null", encoded)
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

        urlCodec = URLCodec.URLCodec1()
        try:
            urlCodec.decode2("%")
            self.fail("DecoderException should have been thrown")
        except DecoderException:
            pass
        try:
            urlCodec.decode2("%A")
            self.fail("DecoderException should have been thrown")
        except DecoderException:
            pass
        try:
            urlCodec.decode2("%WW")
            self.fail("DecoderException should have been thrown")
        except DecoderException:
            pass
        try:
            urlCodec.decode2("%0W")
            self.fail("DecoderException should have been thrown")
        except DecoderException:
            pass
        self.__validateState(urlCodec)

    def testEncodeDecodeNull(self) -> None:

        urlCodec = URLCodec.URLCodec1()
        assertNull("Null string URL encoding test", urlCodec.encode2(None))
        assertNull("Null string URL decoding test", urlCodec.decode2(None))
        self.__validateState(urlCodec)

    def testUnsafeEncodeDecode(self) -> None:

        urlCodec = URLCodec.URLCodec1()
        plain = '~!@#$%^&()+{}"\\;:`,/[]'
        encoded = urlCodec.encode2(plain)
        assert (
            encoded
            == "%7E%21%40%23%24%25%5E%26%28%29%2B%7B%7D%22%5C%3B%3A%60%2C%2F%5B%5D"
        )
        assert urlCodec.decode2(encoded) == plain
        self.__validateState(urlCodec)

    def testSafeCharEncodeDecode(self) -> None:

        urlCodec = URLCodec.URLCodec1()
        plain = "abc123_-.*"
        encoded = urlCodec.encode2(plain)
        self.assertEqual("Safe chars URL encoding test", plain, encoded)
        self.assertEqual(
            "Safe chars URL decoding test", plain, urlCodec.decode2(encoded)
        )
        self.__validateState(urlCodec)

    def testBasicEncodeDecode(self) -> None:

        urlCodec = URLCodec.URLCodec1()
        plain = "Hello there!"
        encoded = urlCodec.encode2(plain)
        self.assertEqual("Basic URL encoding test", "Hello+there%21", encoded)
        self.assertEqual("Basic URL decoding test", plain, urlCodec.decode2(encoded))
        self.__validateState(urlCodec)

    def testUTF8RoundTrip(self) -> None:

        ru_msg = self.__constructString(self.RUSSIAN_STUFF_UNICODE)
        ch_msg = self.__constructString(self.SWISS_GERMAN_STUFF_UNICODE)
        urlCodec = self.URLCodec1()
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

        buffer = ""
        if unicodeChars is not None:
            for unicodeChar in unicodeChars:
                buffer += chr(unicodeChar)
        return buffer

    def __validateState(self, urlCodec: URLCodec) -> None:

        pass

    # Class Methods End
