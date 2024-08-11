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
    BASE32_IMPOSSIBLE_CASES: typing.List[typing.List[str]] = None
    __BASE32_IMPOSSIBLE_CASES_CHUNKED: typing.List[typing.List[str]] = None
    __BASE32HEX_IMPOSSIBLE_CASES: typing.List[typing.List[str]] = None
    __ENCODE_TABLE: typing.List[int] = None
    __BASE32_BINARY_TEST_CASES: typing.List[typing.List[typing.Any]] = None
    __BASE32HEX_TEST_CASES: typing.List[typing.List[str]] = None
    # Class Fields End

    # Class Methods Begin
    def testBase32DecodingOfTrailing35Bits_test0_decomposed(self) -> None:
        pass

    def testBase32DecodingOfTrailing30Bits_test0_decomposed(self) -> None:
        pass

    def testBase32DecodingOfTrailing25Bits_test0_decomposed(self) -> None:
        pass

    def testBase32DecodingOfTrailing20Bits_test0_decomposed(self) -> None:
        pass

    def testBase32DecodingOfTrailing15Bits_test0_decomposed(self) -> None:
        pass

    def testBase32DecodingOfTrailing10Bits_test0_decomposed(self) -> None:
        pass

    def testBase32DecodingOfTrailing5Bits_test0_decomposed(self) -> None:
        pass

    def testBase32HexImpossibleSamples_test0_decomposed(self) -> None:
        pass

    def testBase32ImpossibleChunked_test0_decomposed(self) -> None:
        pass

    def testBase32ImpossibleSamples_test0_decomposed(self) -> None:
        pass

    def testSingleCharEncoding_test0_decomposed(self) -> None:
        pass

    def testRandomBytesHex_test0_decomposed(self) -> None:
        pass

    def testRandomBytesChunked_test0_decomposed(self) -> None:
        pass

    def testRandomBytes_test0_decomposed(self) -> None:
        pass

    def testIsInAlphabet_test5_decomposed(self) -> None:
        pass

    def testIsInAlphabet_test4_decomposed(self) -> None:
        pass

    def testIsInAlphabet_test3_decomposed(self) -> None:
        pass

    def testIsInAlphabet_test2_decomposed(self) -> None:
        pass

    def testIsInAlphabet_test1_decomposed(self) -> None:
        pass

    def testIsInAlphabet_test0_decomposed(self) -> None:
        pass

    def testEmptyBase32_test11_decomposed(self) -> None:
        pass

    def testEmptyBase32_test10_decomposed(self) -> None:
        pass

    def testEmptyBase32_test9_decomposed(self) -> None:
        pass

    def testEmptyBase32_test8_decomposed(self) -> None:
        pass

    def testEmptyBase32_test7_decomposed(self) -> None:
        pass

    def testEmptyBase32_test6_decomposed(self) -> None:
        pass

    def testEmptyBase32_test5_decomposed(self) -> None:
        pass

    def testEmptyBase32_test4_decomposed(self) -> None:
        pass

    def testEmptyBase32_test3_decomposed(self) -> None:
        pass

    def testEmptyBase32_test2_decomposed(self) -> None:
        pass

    def testEmptyBase32_test1_decomposed(self) -> None:
        pass

    def testEmptyBase32_test0_decomposed(self) -> None:
        pass

    def testConstructors_test7_decomposed(self) -> None:
        pass

    def testConstructors_test6_decomposed(self) -> None:
        pass

    def testConstructors_test5_decomposed(self) -> None:
        pass

    def testConstructors_test4_decomposed(self) -> None:
        pass

    def testConstructors_test3_decomposed(self) -> None:
        pass

    def testConstructors_test2_decomposed(self) -> None:
        pass

    def testConstructors_test1_decomposed(self) -> None:
        pass

    def testConstructors_test0_decomposed(self) -> None:
        pass

    def testCodec200_test1_decomposed(self) -> None:
        pass

    def testCodec200_test0_decomposed(self) -> None:
        pass

    def testBase32SamplesNonDefaultPadding_test1_decomposed(self) -> None:
        pass

    def testBase32SamplesNonDefaultPadding_test0_decomposed(self) -> None:
        pass

    def testBase32BinarySamplesReverse_test1_decomposed(self) -> None:
        pass

    def testBase32BinarySamplesReverse_test0_decomposed(self) -> None:
        pass

    def testBase32BinarySamples_test1_decomposed(self) -> None:
        pass

    def testBase32BinarySamples_test0_decomposed(self) -> None:
        pass

    def testBase32Samples_test1_decomposed(self) -> None:
        pass

    def testBase32Samples_test0_decomposed(self) -> None:
        pass

    def testBase32HexSamplesReverseLowercase_test1_decomposed(self) -> None:
        pass

    def testBase32HexSamplesReverseLowercase_test0_decomposed(self) -> None:
        pass

    def testBase32HexSamplesReverse_test1_decomposed(self) -> None:
        pass

    def testBase32HexSamplesReverse_test0_decomposed(self) -> None:
        pass

    def testBase32HexSamples_test1_decomposed(self) -> None:
        pass

    def testBase32HexSamples_test0_decomposed(self) -> None:
        pass

    def testBase32Chunked_test1_decomposed(self) -> None:
        pass

    def testBase32Chunked_test0_decomposed(self) -> None:
        pass

    @staticmethod
    def __assertBase32DecodingOfTrailingBits(nbits: int) -> None:
        pass

    def __testImpossibleCases(
        self, codec: Base32, impossible_cases: typing.List[typing.List[str]]
    ) -> None:
        pass

    # Class Methods End
