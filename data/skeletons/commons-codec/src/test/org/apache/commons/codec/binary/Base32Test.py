from __future__ import annotations

# Imports Begin
from src.main.org.apache.commons.codec.binary.Hex import *
from src.test.org.apache.commons.codec.binary.BaseNTestData import *
from src.main.org.apache.commons.codec.binary.BaseNCodec import *
from src.main.org.apache.commons.codec.binary.Base32 import *
from src.main.org.apache.commons.codec.DecoderException import *
from src.main.org.apache.commons.codec.CodecPolicy import *
import unittest
import os
import typing
from typing import *
import io

# Imports End


class Base32Test(unittest.TestCase):

    # Class Fields Begin
    __BASE32_TEST_CASES_CHUNKED: typing.List[typing.List[str]] = None
    __BASE32_PAD_TEST_CASES: typing.List[typing.List[str]] = None
    __CHARSET_UTF8: str = None
    __BASE32_TEST_CASES: typing.List[typing.List[str]] = None
    BASE32_IMPOSSIBLE_CASES: typing.List[str] = None
    __BASE32_IMPOSSIBLE_CASES_CHUNKED: typing.List[str] = None
    __BASE32HEX_IMPOSSIBLE_CASES: typing.List[str] = None
    __ENCODE_TABLE: typing.List[int] = None
    __BASE32_BINARY_TEST_CASES: typing.List[typing.List[typing.Any]] = None
    __BASE32HEX_TEST_CASES: typing.List[typing.List[str]] = None
    # Class Fields End

    # Class Methods Begin
    def testBase32DecodingOfTrailing35Bits(self) -> None:
        pass

    def testBase32DecodingOfTrailing30Bits(self) -> None:
        pass

    def testBase32DecodingOfTrailing25Bits(self) -> None:
        pass

    def testBase32DecodingOfTrailing20Bits(self) -> None:
        pass

    def testBase32DecodingOfTrailing15Bits(self) -> None:
        pass

    def testBase32DecodingOfTrailing10Bits(self) -> None:
        pass

    def testBase32DecodingOfTrailing5Bits(self) -> None:
        pass

    def testBase32HexImpossibleSamples(self) -> None:
        pass

    def testBase32ImpossibleChunked(self) -> None:
        pass

    def testBase32ImpossibleSamples(self) -> None:
        pass

    def testSingleCharEncoding(self) -> None:
        pass

    def testRandomBytesHex(self) -> None:
        pass

    def testRandomBytesChunked(self) -> None:
        pass

    def testRandomBytes(self) -> None:
        pass

    def testIsInAlphabet(self) -> None:
        pass

    def testEmptyBase32(self) -> None:
        pass

    def testConstructors(self) -> None:
        pass

    def testCodec200(self) -> None:
        pass

    def testBase32SamplesNonDefaultPadding(self) -> None:
        pass

    def testBase32BinarySamplesReverse(self) -> None:
        pass

    def testBase32BinarySamples(self) -> None:
        pass

    def testBase32Samples(self) -> None:
        pass

    def testBase32HexSamplesReverseLowercase(self) -> None:
        pass

    def testBase32HexSamplesReverse(self) -> None:
        pass

    def testBase32HexSamples(self) -> None:
        pass

    def testBase32Chunked(self) -> None:
        pass

    @staticmethod
    def __assertBase32DecodingOfTrailingBits(nbits: int) -> None:
        pass

    def __testImpossibleCases(
        self, codec: Base32, impossible_cases: typing.List[str]
    ) -> None:
        pass

    # Class Methods End
