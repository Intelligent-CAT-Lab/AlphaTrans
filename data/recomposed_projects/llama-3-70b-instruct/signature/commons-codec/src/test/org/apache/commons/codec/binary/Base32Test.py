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
            self.__BASE32HEX_IMPOSSIBLE_CASES,
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
            self.__BASE32_IMPOSSIBLE_CASES_CHUNKED,
        )

    def testBase32ImpossibleSamples(self) -> None:
        self.__testImpossibleCases(
            Base32(0, None, False, BaseNCodec.PAD_DEFAULT, CodecPolicy.STRICT),
            self.BASE32_IMPOSSIBLE_CASES,
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
            if not allInOne == singly:
                self.fail()

    def testRandomBytesHex(self) -> None:
        for i in range(20):
            codec = Base32.Base321(True)
            b = BaseNTestData.randomData(codec, i)
            self.assertEqual(
                "" + str(i) + " " + str(codec.lineLength),
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
                len(b[1]),
                codec.getEncodedLength(b[0]),
            )

    def testIsInAlphabet(self) -> None:
        b32 = Base32.Base321(True)
        self.assertFalse(b32.isInAlphabet0(0))
        self.assertFalse(b32.isInAlphabet0(1))
        self.assertFalse(b32.isInAlphabet0(-1))
        self.assertFalse(b32.isInAlphabet0(-15))
        self.assertFalse(b32.isInAlphabet0(-32))
        self.assertFalse(b32.isInAlphabet0(127))
        self.assertFalse(b32.isInAlphabet0(128))
        self.assertFalse(b32.isInAlphabet0(255))

        b32 = Base32.Base321(False)
        for c in range(ord("2"), ord("7") + 1):
            self.assertTrue(b32.isInAlphabet0(c))
        for c in range(ord("A"), ord("Z") + 1):
            self.assertTrue(b32.isInAlphabet0(c))
        for c in range(ord("a"), ord("z") + 1):
            self.assertTrue(b32.isInAlphabet0(c))
        self.assertFalse(b32.isInAlphabet0(ord("1")))
        self.assertFalse(b32.isInAlphabet0(ord("8")))
        self.assertFalse(b32.isInAlphabet0(ord("A") - 1))
        self.assertFalse(b32.isInAlphabet0(ord("Z") + 1))

        b32 = Base32.Base321(True)
        for c in range(ord("0"), ord("9") + 1):
            self.assertTrue(b32.isInAlphabet0(c))
        for c in range(ord("A"), ord("V") + 1):
            self.assertTrue(b32.isInAlphabet0(c))
        for c in range(ord("a"), ord("v") + 1):
            self.assertTrue(b32.isInAlphabet0(c))
        self.assertFalse(b32.isInAlphabet0(ord("0") - 1))
        self.assertFalse(b32.isInAlphabet0(ord("9") + 1))
        self.assertFalse(b32.isInAlphabet0(ord("A") - 1))
        self.assertFalse(b32.isInAlphabet0(ord("V") + 1))
        self.assertFalse(b32.isInAlphabet0(ord("a") - 1))
        self.assertFalse(b32.isInAlphabet0(ord("v") + 1))

    def testEmptyBase32(self) -> None:
        empty: typing.List[int] = []
        result: typing.List[int] = Base32.Base320().encode0(empty)
        self.assertEqual("empty Base32 encode", 0, len(result))
        self.assertIsNone("empty Base32 encode", Base32.Base320().encode0(None))
        result = Base32.Base320().encode1(empty, 0, 1)
        self.assertEqual("empty Base32 encode with offset", 0, len(result))
        self.assertIsNone(
            "empty Base32 encode with offset", Base32.Base320().encode0(None)
        )

        empty = []
        result = Base32.Base320().decode0(empty)
        self.assertEqual("empty Base32 decode", 0, len(result))
        self.assertIsNone("empty Base32 encode", Base32.Base320().decode0(None))

    def testConstructors(self) -> None:
        base32: Base32
        base32 = Base32.Base320()
        base32 = Base32.Base324(-1)
        base32 = Base32.Base325(-1, [])
        base32 = Base32.Base325(32, [])
        base32 = Base32.Base326(32, [], False)
        base32 = Base32.Base325(-1, ["A"])
        try:
            base32 = Base32.Base325(32, None)
            self.fail("Should have rejected null line separator")
        except ValueError as ignored:
            pass
        try:
            base32 = Base32.Base325(32, ["A"])
            self.fail("Should have rejected attempt to use 'A' as a line separator")
        except ValueError as ignored:
            pass
        try:
            base32 = Base32.Base325(32, ["="])
            self.fail("Should have rejected attempt to use '=' as a line separator")
        except ValueError as ignored:
            pass
        base32 = Base32.Base325(32, ["$"])  # OK
        try:
            base32 = Base32.Base325(32, ["A", "$"])
            self.fail("Should have rejected attempt to use 'A$' as a line separator")
        except ValueError as ignored:
            pass
        try:
            base32 = Base32.Base327(32, ["\n"], False, "A")
            self.fail("Should have rejected attempt to use 'A' as padding")
        except ValueError as ignored:
            pass
        try:
            base32 = Base32.Base327(32, ["\n"], False, " ")
            self.fail("Should have rejected attempt to use ' ' as padding")
        except ValueError as ignored:
            pass
        base32 = Base32.Base325(32, [" ", "$", "\n", "\r", "\t"])  # OK
        self.assertIsNotNone(base32)

    def testCodec200(self) -> None:
        codec = Base32.Base322(True, 87)  # should be allowed
        self.assertIsNotNone(codec)

    def testBase32SamplesNonDefaultPadding(self) -> None:

        pass  # LLM could not translate this method

    def testBase32BinarySamplesReverse(self) -> None:
        codec = Base32.Base320()
        for element in self.__BASE32_BINARY_TEST_CASES:
            self.assertArrayEquals(element[0], codec.decode3(element[1]))

    def testBase32BinarySamples(self) -> None:
        codec = Base32.Base320()
        for element in self.__BASE32_BINARY_TEST_CASES:
            expected = element[2] if len(element) > 2 else element[1]
            self.assertEqual(expected.upper(), codec.encodeAsString(element[0]))

    def testBase32Samples(self) -> None:
        codec = Base32.Base320()
        for element in self.__BASE32_TEST_CASES:
            self.assertEqual(
                element[1], codec.encodeAsString(element[0].encode(self.__CHARSET_UTF8))
            )

    def testBase32HexSamplesReverseLowercase(self) -> None:
        codec = Base32.Base321(True)
        for element in self.__BASE32HEX_TEST_CASES:
            self.assertEqual(
                element[0],
                codec.decode3(element[1].lower()).decode(self.__CHARSET_UTF8),
            )

    def testBase32HexSamplesReverse(self) -> None:
        codec = Base32.Base321(True)
        for element in self.__BASE32HEX_TEST_CASES:
            self.assertEqual(
                element[0], str(codec.decode3(element[1]), self.__CHARSET_UTF8)
            )

    def testBase32HexSamples(self) -> None:
        codec = Base32.Base321(True)
        for element in self.__BASE32HEX_TEST_CASES:
            self.assertEqual(
                element[1], codec.encodeAsString(element[0].encode(self.__CHARSET_UTF8))
            )

    def testBase32Chunked(self) -> None:
        codec = Base32.Base324(20)
        for element in self.__BASE32_TEST_CASES_CHUNKED:
            self.assertEqual(
                element[1], codec.encodeAsString(element[0].encode(self.__CHARSET_UTF8))
            )

    @staticmethod
    def __assertBase32DecodingOfTrailingBits(nbits: int) -> None:
        codec = Base32(0, None, False, BaseNCodec.PAD_DEFAULT, CodecPolicy.STRICT)
        assertTrue(codec.isStrictDecoding())
        assertEquals(CodecPolicy.STRICT, codec.getCodecPolicy())
        defaultCodec = Base32.Base320()
        assertFalse(defaultCodec.isStrictDecoding())
        assertEquals(CodecPolicy.LENIENT, defaultCodec.getCodecPolicy())

        length = nbits // 5
        encoded = [0] * 8
        encoded[:length] = [Base32Test.__ENCODE_TABLE[0]] * length
        encoded[length:] = [ord("=")] * (8 - length)
        discard = nbits % 8
        emptyBitsMask = (1 << discard) - 1
        invalid = length == 1 or length == 3 or length == 6
        last = length - 1
        for i in range(32):
            encoded[last] = Base32Test.__ENCODE_TABLE[i]
            if invalid or (i & emptyBitsMask) != 0:
                try:
                    codec.decode0(encoded)
                    fail("Final base-32 digit should not be allowed")
                except ValueError as ex:
                    pass
                decoded = defaultCodec.decode0(encoded)
                assertFalse(Arrays.equals(encoded, defaultCodec.encode0(decoded)))
            else:
                decoded = codec.decode0(encoded)
                bitsEncoded = i >> discard
                assertEquals(
                    "Invalid decoding of last character", bitsEncoded, decoded[-1]
                )
                assertArrayEquals(encoded, codec.encode0(decoded))

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
