# Imports Begin
from src.main.org.apache.commons.codec.net.PercentCodec import *
from src.main.org.apache.commons.codec.DecoderException import *
import unittest
from abc import ABC

# Imports End


class PercentCodecTest(unittest.TestCase):

    # Class Fields Begin
    # Class Fields End

    # Class Methods Begin
    def testUnsafeCharEncodeDecode(self) -> None:

        percentCodec = PercentCodec(1, False, None)
        input = "\u03B1\u03B2\u03B3\u03B4\u03B5\u03B6% "
        encoded = percentCodec.encode0(input.encode("utf-8"))
        encodedS = encoded.decode("utf-8")
        decoded = percentCodec.decode0(encoded)
        decodedS = decoded.decode("utf-8")
        self.assertEqual(
            "Basic PercentCodec unsafe char encoding test",
            "%CE%B1%CE%B2%CE%B3%CE%B4%CE%B5%CE%B6%25 ",
            encodedS,
        )
        self.assertEqual(
            "Basic PercentCodec unsafe char decoding test", input, decodedS
        )

    def testSafeCharEncodeDecodeObject(self) -> None:

        percentCodec = PercentCodec(0, True, None)
        input = "abc123_-.*"
        encoded = percentCodec.encode1(input.encode("utf-8"))
        encoded_s = encoded.decode("utf-8")
        decoded = percentCodec.decode1(encoded)
        decoded_s = decoded.decode("utf-8")
        assert encoded_s == input
        assert decoded_s == input

    def testPercentEncoderDecoderWithPlusForSpace(self) -> None:

        input = "a b c d"
        percentCodec = PercentCodec(0, True, None)
        encoded = percentCodec.encode0(input.encode("utf-8"))
        encoded_s = encoded.decode("utf-8")
        assert encoded_s == "a+b+c+d"
        decoded = percentCodec.decode0(encoded)
        assert decoded.decode("utf-8") == input

    def testPercentEncoderDecoderWithNullOrEmptyInput(self) -> None:

        percentCodec = PercentCodec(0, True, None)
        assert percentCodec.encode0(None) is None
        assert percentCodec.decode0(None) is None
        emptyInput = b""
        assert percentCodec.encode0(emptyInput) == emptyInput
        assert percentCodec.decode0(emptyInput) == emptyInput

    def testEncodeUnsupportedObject(self) -> None:

        percentCodec = PercentCodec(1, False, None)
        percentCodec.encode1("test")

    def testEncodeNullObject(self) -> None:

        percentCodec = PercentCodec(1, False, None)
        self.assertIsNone(percentCodec.encode1(None))

    def testDecodeUnsupportedObject(self) -> None:

        percentCodec = PercentCodec(1, False, None)
        percentCodec.decode1("test")

    def testDecodeNullObject(self) -> None:

        percentCodec = PercentCodec(1, False, None)
        assertNull(percentCodec.decode1(None))

    def testDecodeInvalidEncodedResultDecoding(self) -> None:

        input_s = "\u03B1\u03B2"
        percent_codec = PercentCodec(1, False, None)
        encoded = percent_codec.encode0(input_s.encode("utf-8"))
        try:
            percent_codec.decode0(encoded[:-1])
        except Exception as e:
            assert isinstance(e, DecoderException) and isinstance(
                e.__cause__, ArrayIndexOutOfBoundsException
            )

    def testConfigurablePercentEncoder(self) -> None:

        input = "abc123_-.*\u03B1\u03B2"
        percentCodec = PercentCodec(0, False, b"abcdef")
        encoded = percentCodec.encode0(input.encode("utf-8"))
        encoded_s = encoded.decode("utf-8")
        assert encoded_s == "%61%62%63123_-.*%CE%B1%CE%B2"
        decoded = percentCodec.decode0(encoded)
        assert decoded.decode("utf-8") == input

    def testBasicSpace(self) -> None:

        percentCodec = PercentCodec(1, False, None)
        input = " "
        encoded = percentCodec.encode0(input.encode("utf-8"))
        self.assertEqual(b"%20", encoded)

    def testBasicEncodeDecode(self) -> None:

        percentCodec = PercentCodec(1, False, None)
        input = "abcdABCD"
        encoded = percentCodec.encode0(input.encode("utf-8"))
        encodedS = encoded.decode("utf-8")
        decoded = percentCodec.decode0(encoded)
        decodedS = decoded.decode("utf-8")
        self.assertEqual("Basic PercentCodec encoding test", input, encodedS)
        self.assertEqual("Basic PercentCodec decoding test", input, decodedS)

    # Class Methods End
