from __future__ import annotations
import re
import unittest
import pytest
import io
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

        assert (
            encoded_s == "%CE%B1%CE%B2%CE%B3%CE%B4%CE%B5%CE%B6%25 "
        ), "Basic PercentCodec unsafe char encoding test"
        assert decoded_s == input_str, "Basic PercentCodec unsafe char decoding test"

    def testSafeCharEncodeDecodeObject(self) -> None:

        percent_codec = PercentCodec(0, True, None)
        input_str = "abc123_-.*"
        encoded = percent_codec.encode1(input_str.encode("utf-8"))
        encoded_s = encoded.decode("utf-8")
        decoded = percent_codec.decode1(encoded)
        decoded_s = decoded.decode("utf-8")

        assert "Basic PercentCodec safe char encoding test" == input_str == encoded_s
        assert "Basic PercentCodec safe char decoding test" == input_str == decoded_s

    def testPercentEncoderDecoderWithPlusForSpace(self) -> None:

        input_str = "a b c d"
        percent_codec = PercentCodec(0, True, None)
        encoded = percent_codec.encode0(input_str.encode("utf-8"))
        encoded_s = encoded.decode("utf-8")
        assert encoded_s == "a+b+c+d", "PercentCodec plus for space encoding test"
        decoded = percent_codec.decode0(encoded)
        assert (
            decoded.decode("utf-8") == input_str
        ), "PercentCodec plus for space decoding test"

    def testPercentEncoderDecoderWithNullOrEmptyInput(self) -> None:

        percent_codec = PercentCodec(0, True, None)
        assert percent_codec.encode0(None) is None, "Null input value encoding test"
        assert percent_codec.decode0(None) is None, "Null input value decoding test"
        empty_input = "".encode("utf-8")
        assert (
            percent_codec.encode0(empty_input) == empty_input
        ), "Empty input value encoding test"
        assert (
            percent_codec.decode0(empty_input) == empty_input
        ), "Empty input value decoding test"

    def testEncodeUnsupportedObject(self) -> None:

        percentCodec = PercentCodec(1, False, None)
        percentCodec.encode1("test")

    def testEncodeNullObject(self) -> None:

        percent_codec = PercentCodec(1, False, None)
        assert percent_codec.encode1(None) is None

    def testDecodeUnsupportedObject(self) -> None:

        percentCodec = PercentCodec(1, False, None)
        percentCodec.decode1("test")

    def testDecodeNullObject(self) -> None:

        percentCodec = PercentCodec(1, False, None)
        assert percentCodec.decode1(None) is None

    def testDecodeInvalidEncodedResultDecoding(self) -> None:

        inputS = "\u03B1\u03B2"
        percentCodec = PercentCodec(1, False, None)
        encoded = percentCodec.encode0(inputS.encode("utf-8"))
        try:
            percentCodec.decode0(encoded[:-1])  # exclude one byte
        except Exception as e:
            assert isinstance(e, DecoderException) and isinstance(
                e.__cause__, IndexError
            )

    def testConfigurablePercentEncoder(self) -> None:

        input_str = "abc123_-.*\u03B1\u03B2"
        percent_codec = PercentCodec(0, False, "abcdef".encode("utf-8"))
        encoded = percent_codec.encode0(input_str.encode("utf-8"))
        encoded_s = encoded.decode("utf-8")
        assert (
            encoded_s == "%61%62%63123_-.*%CE%B1%CE%B2"
        ), "Configurable PercentCodec encoding test"
        decoded = percent_codec.decode0(encoded)
        assert (
            decoded.decode("utf-8") == input_str
        ), "Configurable PercentCodec decoding test"

    @pytest.mark.skip(reason="Ignore")
    def testBasicSpace(self) -> None:

        percentCodec = PercentCodec(1, False, None)
        input = " "
        encoded = percentCodec.encode0(input.encode("utf-8"))
        assert encoded == "%20".encode("utf-8")

    def testBasicEncodeDecode(self) -> None:

        percent_codec = PercentCodec(1, False, None)
        input_str = "abcdABCD"
        encoded = percent_codec.encode0(input_str.encode("utf-8"))
        encoded_s = encoded.decode("utf-8")
        decoded = percent_codec.decode0(encoded)
        decoded_s = decoded.decode("utf-8")

        assert "Basic PercentCodec encoding test" == input_str == encoded_s
        assert "Basic PercentCodec decoding test" == input_str == decoded_s
