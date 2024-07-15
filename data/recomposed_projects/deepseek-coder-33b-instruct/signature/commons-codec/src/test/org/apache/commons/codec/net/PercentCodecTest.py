from __future__ import annotations
import re
from abc import ABC
import unittest
import pytest
import io
import unittest
from src.main.org.apache.commons.codec.DecoderException import *
from src.main.org.apache.commons.codec.net.PercentCodec import *


class PercentCodecTest(unittest.TestCase):

    def testUnsafeCharEncodeDecode(self) -> None:

        percent_codec = PercentCodec(1, False, None)
        input_str = "\u03B1\u03B2\u03B3\u03B4\u03B5\u03B6% "
        encoded = percent_codec.encode0(input_str.encode("utf-8"))
        encoded_s = encoded.decode("utf-8")
        decoded = percent_codec.decode0(encoded)
        decoded_s = decoded.decode("utf-8")
        self.assertEqual(
            "Basic PercentCodec unsafe char encoding test",
            "%CE%B1%CE%B2%CE%B3%CE%B4%CE%B5%CE%B6%25 ",
            encoded_s,
        )
        self.assertEqual(
            "Basic PercentCodec unsafe char decoding test", input_str, decoded_s
        )

    def testSafeCharEncodeDecodeObject(self) -> None:

        percent_codec = PercentCodec(0, True, None)
        input_str = "abc123_-.*"
        encoded = percent_codec.encode1(input_str.encode("utf-8"))
        encoded_s = encoded.decode("utf-8")
        decoded = percent_codec.decode1(encoded)
        decoded_s = decoded.decode("utf-8")
        self.assertEqual(
            "Basic PercentCodec safe char encoding test", input_str, encoded_s
        )
        self.assertEqual(
            "Basic PercentCodec safe char decoding test", input_str, decoded_s
        )

    def testPercentEncoderDecoderWithPlusForSpace(self) -> None:

        input_str = "a b c d"
        percent_codec = PercentCodec(0, True, None)
        encoded = percent_codec.encode0(input_str.encode("utf-8"))
        encoded_s = encoded.decode("utf-8")
        self.assertEqual(
            "PercentCodec plus for space encoding test", "a+b+c+d", encoded_s
        )
        decode = percent_codec.decode0(encoded)
        self.assertEqual(
            "PercentCodec plus for space decoding test",
            decode.decode("utf-8"),
            input_str,
        )

    def testPercentEncoderDecoderWithNullOrEmptyInput(self) -> None:

        percent_codec = PercentCodec(0, True, None)
        self.assertIsNone(percent_codec.encode0(None), "Null input value encoding test")
        self.assertIsNone(percent_codec.decode0(None), "Null input value decoding test")
        empty_input = "".encode("utf-8")
        self.assertEqual(
            percent_codec.encode0(empty_input),
            empty_input,
            "Empty input value encoding test",
        )
        self.assertEqual(
            percent_codec.decode0(empty_input),
            empty_input,
            "Empty input value decoding test",
        )

    def testEncodeUnsupportedObject(self) -> None:

        percent_codec = PercentCodec(1, False, None)

        with pytest.raises(DecoderException):
            percent_codec.encode1("test")

    def testEncodeNullObject(self) -> None:

        percent_codec = PercentCodec(1, False, None)
        self.assertIsNone(percent_codec.encode1(None))

    def testDecodeUnsupportedObject(self) -> None:

        percent_codec = PercentCodec(1, False, None)

        with pytest.raises(DecoderException):
            percent_codec.decode1("test")

    def testDecodeNullObject(self) -> None:

        percent_codec = PercentCodec(1, False, None)
        self.assertIsNone(percent_codec.decode1(None))

    def testDecodeInvalidEncodedResultDecoding(self) -> None:

        inputS = "\u03B1\u03B2"
        percentCodec = PercentCodec(1, False, None)
        encoded = percentCodec.encode0(inputS.encode("utf-8"))

        try:
            percentCodec.decode0(encoded[:-1])  # exclude one byte
        except Exception as e:
            self.assertTrue(
                isinstance(e, DecoderException) and isinstance(e.__cause__, IndexError)
            )

    def testConfigurablePercentEncoder(self) -> None:

        input = "abc123_-.*\u03B1\u03B2"
        percentCodec = PercentCodec(
            0, False, [97, 98, 99, 100, 101, 102]
        )  # 'abcdef' in ASCII
        encoded = percentCodec.encode0(input.encode("utf-8"))
        encodedS = encoded.decode("utf-8")
        self.assertEqual(
            "Configurable PercentCodec encoding test",
            "%61%62%63123_-.*%CE%B1%CE%B2",
            encodedS,
        )
        decoded = percentCodec.decode0(encoded)
        self.assertEqual(
            "Configurable PercentCodec decoding test", decoded.decode("utf-8"), input
        )

    @pytest.mark.skip(reason="Ignore")
    def testBasicSpace(self) -> None:

        percent_codec = PercentCodec(1, False, None)
        input_str = " "
        encoded = percent_codec.encode0(input_str.encode("utf-8"))
        self.assertEqual(b"%20", bytes(encoded))

    def testBasicEncodeDecode(self) -> None:

        percent_codec = PercentCodec(1, False, None)
        input_str = "abcdABCD"
        encoded = percent_codec.encode0(input_str.encode("utf-8"))
        encoded_s = encoded.decode("utf-8")
        decoded = percent_codec.decode0(encoded)
        decoded_s = decoded.decode("utf-8")
        self.assertEqual("Basic PercentCodec encoding test", input_str, encoded_s)
        self.assertEqual("Basic PercentCodec decoding test", input_str, decoded_s)
