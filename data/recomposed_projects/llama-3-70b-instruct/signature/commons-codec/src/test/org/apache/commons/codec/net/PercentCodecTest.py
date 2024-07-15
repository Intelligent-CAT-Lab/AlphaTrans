from __future__ import annotations
import re
import typing
from typing import *
from abc import ABC
import unittest
import pytest
import io
import unittest
from src.main.org.apache.commons.codec.DecoderException import *
from src.main.org.apache.commons.codec.net.PercentCodec import *


class PercentCodecTest(unittest.TestCase):

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
        encodedS = encoded.decode("utf-8")
        decoded = percentCodec.decode1(encoded)
        decodedS = decoded.decode("utf-8")
        self.assertEqual("Basic PercentCodec safe char encoding test", input, encodedS)
        self.assertEqual("Basic PercentCodec safe char decoding test", input, decodedS)

    def testPercentEncoderDecoderWithPlusForSpace(self) -> None:
        input: str = "a b c d"
        percentCodec: PercentCodec = PercentCodec(0, True, None)
        encoded: typing.List[int] = percentCodec.encode0(
            input.encode(StandardCharsets.UTF_8)
        )
        encodedS: str = encoded.decode(StandardCharsets.UTF_8)
        self.assertEqual(
            "PercentCodec plus for space encoding test", "a+b+c+d", encodedS
        )
        decode: typing.List[int] = percentCodec.decode0(encoded)
        self.assertEqual(
            "PercentCodec plus for space decoding test",
            decode.decode(StandardCharsets.UTF_8),
            input,
        )

    def testPercentEncoderDecoderWithNullOrEmptyInput(self) -> None:
        percentCodec = PercentCodec(0, True, None)
        self.assertIsNone("Null input value encoding test", percentCodec.encode0(None))
        self.assertIsNone("Null input value decoding test", percentCodec.decode0(None))
        emptyInput = "".encode("utf-8")
        self.assertEqual(
            "Empty input value encoding test",
            percentCodec.encode0(emptyInput),
            emptyInput,
        )
        self.assertListEqual(
            "Empty input value decoding test",
            percentCodec.decode0(emptyInput),
            emptyInput,
        )

    def testEncodeUnsupportedObject(self) -> None:
        with self.assertRaises(EncoderException):
            percentCodec = PercentCodec(1, False, None)
            percentCodec.encode1("test")

    def testEncodeNullObject(self) -> None:
        percentCodec = PercentCodec(1, False, None)
        self.assertIsNone(percentCodec.encode1(None))

    def testDecodeUnsupportedObject(self) -> None:
        with self.assertRaises(DecoderException):
            percentCodec = PercentCodec(1, False, None)
            percentCodec.decode1("test")

    def testDecodeNullObject(self) -> None:
        percentCodec = PercentCodec(1, False, None)
        self.assertIsNone(percentCodec.decode1(None))

    def testDecodeInvalidEncodedResultDecoding(self) -> None:
        input_s: str = "\u03B1\u03B2"
        percent_codec: PercentCodec = PercentCodec(1, False, None)
        encoded: typing.List[int] = percent_codec.encode0(input_s.encode("utf-8"))
        try:
            percent_codec.decode0(encoded[:-1])  # exclude one byte
        except Exception as e:
            assert isinstance(e, DecoderException) and isinstance(
                e.getCause(), IndexError
            )

    def testConfigurablePercentEncoder(self) -> None:
        input: str = "abc123_-.*\u03B1\u03B2"
        percentCodec: PercentCodec = PercentCodec(0, False, "abcdef".encode("utf-8"))
        encoded: typing.List[int] = percentCodec.encode0(input.encode("utf-8"))
        encodedS: str = encoded.decode("utf-8")
        self.assertEqual(
            "Configurable PercentCodec encoding test",
            "%61%62%63123_-.*%CE%B1%CE%B2",
            encodedS,
        )
        decoded: typing.List[int] = percentCodec.decode0(encoded)
        self.assertEqual(
            "Configurable PercentCodec decoding test", decoded.decode("utf-8"), input
        )

    @pytest.mark.skip(reason="Ignore")
    def testBasicSpace(self) -> None:
        percentCodec = PercentCodec(1, False, None)
        input = " "
        encoded = percentCodec.encode0(input.encode("UTF-8"))
        self.assertListEqual("%20".encode("UTF-8"), encoded)

    def testBasicEncodeDecode(self) -> None:
        percentCodec = PercentCodec(1, False, None)
        input = "abcdABCD"
        encoded = percentCodec.encode0(input.encode("UTF-8"))
        encodedS = encoded.decode("UTF-8")
        decoded = percentCodec.decode0(encoded)
        decodedS = decoded.decode("UTF-8")
        self.assertEqual("Basic PercentCodec encoding test", input, encodedS)
        self.assertEqual("Basic PercentCodec decoding test", input, decodedS)
