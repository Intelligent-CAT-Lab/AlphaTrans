from __future__ import annotations
import re
import random
import unittest
import pytest
import io
import typing
from typing import *
import os
import unittest
from src.main.org.apache.commons.codec.CodecPolicy import *
from src.main.org.apache.commons.codec.DecoderException import *
from src.main.org.apache.commons.codec.binary.Base32 import *
from src.main.org.apache.commons.codec.binary.BaseNCodec import *
from src.test.org.apache.commons.codec.binary.BaseNTestData import *
from src.main.org.apache.commons.codec.binary.Hex import *


class Base32Test(unittest.TestCase):

    BASE32_IMPOSSIBLE_CASES: typing.List[str] = [
        "MC======",
        "MZXE====",
        "MZXWB===",
        "MZXW6YB=",
        "MZXW6YTBOC======",
        "AB======",
    ]
    __BASE32_PAD_TEST_CASES: typing.List[typing.List[str]] = [
        ["", ""],
        ["f", "MY%%%%%%"],
        ["fo", "MZXQ%%%%"],
        ["foo", "MZXW6%%%"],
        ["foob", "MZXW6YQ%"],
        ["fooba", "MZXW6YTB"],
        ["foobar", "MZXW6YTBOI%%%%%%"],
    ]
    __BASE32_TEST_CASES_CHUNKED: typing.List[typing.List[str]] = [
        ["", ""],
        ["f", "MY======\r\n"],
        ["fo", "MZXQ====\r\n"],
        ["foo", "MZXW6===\r\n"],
        ["foob", "MZXW6YQ=\r\n"],
        ["fooba", "MZXW6YTB\r\n"],
        ["foobar", "MZXW6YTBOI======\r\n"],
    ]
    __BASE32HEX_TEST_CASES: typing.List[typing.List[str]] = [
        ["", ""],
        ["f", "CO======"],
        ["fo", "CPNG===="],
        ["foo", "CPNMU==="],
        ["foob", "CPNMUOG="],
        ["fooba", "CPNMUOJ1"],
        ["foobar", "CPNMUOJ1E8======"],
    ]
    __BASE32_BINARY_TEST_CASES: typing.List[typing.List[typing.Any]] = None

    __ENCODE_TABLE: typing.List[int] = [
        65,
        66,
        67,
        68,
        69,
        70,
        71,
        72,
        73,
        74,
        75,
        76,
        77,
        78,
        79,
        80,
        81,
        82,
        83,
        84,
        85,
        86,
        87,
        88,
        89,
        90,
        50,
        51,
        52,
        53,
        54,
        55,
    ]
    __BASE32HEX_IMPOSSIBLE_CASES: typing.List[str] = [
        "C2======",
        "CPN4====",
        "CPNM1===",
        "CPNMUO1=",
        "CPNMUOJ1E2======",
    ]
    __BASE32_IMPOSSIBLE_CASES_CHUNKED: typing.List[str] = [
        "M2======\r\n",
        "MZX0====\r\n",
        "MZXW0===\r\n",
        "MZXW6Y2=\r\n",
        "MZXW6YTBO2======\r\n",
    ]
    __BASE32_TEST_CASES: typing.List[typing.List[str]] = [
        ["", ""],
        ["f", "MY======"],
        ["fo", "MZXQ===="],
        ["foo", "MZXW6==="],
        ["foob", "MZXW6YQ="],
        ["fooba", "MZXW6YTB"],
        ["foobar", "MZXW6YTBOI======"],
    ]
    __CHARSET_UTF8: str = "UTF-8"

    @staticmethod
    def run_static_init():
        hex = Hex(2, None, None)
        try:
            Base32Test.__BASE32_BINARY_TEST_CASES = [
                [
                    hex.decode2("623a01735836e9a126e12fbf95e013ee6892997c"),
                    "MI5AC42YG3U2CJXBF67ZLYAT5ZUJFGL4",
                ],
                [
                    hex.decode2("623a01735836e9a126e12fbf95e013ee6892997c"),
                    "mi5ac42yg3u2cjxbf67zlyat5zujfgl4",
                ],
                [hex.decode2("739ce42108"), "OOOOIIII"],
            ]
        except DecoderException as de:
            raise Error(":(", de)

    def testBase32DecodingOfTrailing35Bits(self) -> None:
        self.__assertBase32DecodingOfTrailingBits(35)

    def testBase32DecodingOfTrailing30Bits(self) -> None:
        self.__assertBase32DecodingOfTrailingBits(30)

    def testBase32DecodingOfTrailing25Bits(self) -> None:
        self.__assertBase32DecodingOfTrailingBits(25)

    def testBase32DecodingOfTrailing20Bits(self) -> None:
        self.__assertBase32DecodingOfTrailingBits(20)

    def testBase32DecodingOfTrailing15Bits(self) -> None:
        self.__assertBase32DecodingOfTrailingBits(15)

    def testBase32DecodingOfTrailing10Bits(self) -> None:
        self.__assertBase32DecodingOfTrailingBits(10)

    def testBase32DecodingOfTrailing5Bits(self) -> None:
        self.__assertBase32DecodingOfTrailingBits(5)

    def testBase32HexImpossibleSamples(self) -> None:
        self.__testImpossibleCases(
            Base32(0, None, True, BaseNCodec.PAD_DEFAULT, CodecPolicy.STRICT),
            Base32Test.__BASE32HEX_IMPOSSIBLE_CASES,
        )

    def testBase32ImpossibleChunked(self) -> None:
        self.__testImpossibleCases(
            Base32(
                20,
                BaseNCodec.CHUNK_SEPARATOR,
                False,
                BaseNCodec.PAD_DEFAULT,
                CodecPolicy.STRICT,
            ),
            Base32Test.__BASE32_IMPOSSIBLE_CASES_CHUNKED,
        )

    def testBase32ImpossibleSamples(self) -> None:
        self.__testImpossibleCases(
            Base32(0, None, False, BaseNCodec.PAD_DEFAULT, CodecPolicy.STRICT),
            Base32Test.BASE32_IMPOSSIBLE_CASES,
        )

    def testSingleCharEncoding(self) -> None:
        for i in range(20):
            codec = Base32.Base320()
            context = Context()
            unencoded = [0] * i
            allInOne = codec.encode0(unencoded)
            codec = Base32.Base320()
            for j in range(len(unencoded)):
                codec.encode2(unencoded, j, 1, context)
            codec.encode2(unencoded, 0, -1, context)
            singly = [0] * len(allInOne)
            codec.readResults(singly, 0, 100, context)
            if not Arrays.equals(allInOne, singly):
                self.fail()

    def testRandomBytesHex(self) -> None:
        for i in range(20):
            codec = Base32.Base321(True)
            b = BaseNTestData.randomData(codec, i)
            self.assertEqual(
                "" + str(i) + " " + str(codec._lineLength),
                len(b[1]),
                codec.getEncodedLength(b[0]),
            )

    def testRandomBytesChunked(self) -> None:
        for i in range(20):
            codec = Base32.Base324(10)
            b = BaseNTestData.randomData(codec, i)
            self.assertEqual(
                str(i) + " " + str(codec.lineLength),
                len(b[1]),
                codec.getEncodedLength(b[0]),
            )

    def testRandomBytes(self) -> None:
        for i in range(20):
            codec = Base32.Base320()
            b = BaseNTestData.randomData(codec, i)
            self.assertEqual(
                "" + str(i) + " " + str(codec.lineLength),
                b[1].length,
                codec.getEncodedLength(b[0]),
            )

    def testIsInAlphabet(self) -> None:

        pass  # LLM could not translate this method

    def testEmptyBase32(self) -> None:

        pass  # LLM could not translate this method

    def testConstructors(self) -> None:

        pass  # LLM could not translate this method

    def testCodec200(self) -> None:

        pass  # LLM could not translate this method

    def testBase32SamplesNonDefaultPadding(self) -> None:

        pass  # LLM could not translate this method

    def testBase32BinarySamplesReverse(self) -> None:

        pass  # LLM could not translate this method

    def testBase32BinarySamples(self) -> None:

        pass  # LLM could not translate this method

    def testBase32Samples(self) -> None:

        pass  # LLM could not translate this method

    def testBase32HexSamplesReverseLowercase(self) -> None:

        pass  # LLM could not translate this method

    def testBase32HexSamplesReverse(self) -> None:

        pass  # LLM could not translate this method

    def testBase32HexSamples(self) -> None:

        pass  # LLM could not translate this method

    def testBase32Chunked(self) -> None:

        pass  # LLM could not translate this method

    @staticmethod
    def __assertBase32DecodingOfTrailingBits(nbits: int) -> None:

        pass  # LLM could not translate this method

    def __testImpossibleCases(
        self, codec: Base32, impossible_cases: typing.List[str]
    ) -> None:
        for impossible in impossible_cases:
            try:
                codec.decode3(impossible)
                self.fail()
            except ValueError as ex:
                pass


Base32Test.run_static_init()
