# Imports Begin
from src.main.org.apache.commons.codec.binary.Hex import *
from src.main.org.apache.commons.codec.binary.BaseNTestData import *
from src.main.org.apache.commons.codec.binary.BaseNCodec import *
from src.main.org.apache.commons.codec.binary.Base32 import *
from src.main.org.apache.commons.codec.DecoderException import *
from src.main.org.apache.commons.codec.CodecPolicy import *
import unittest
import os
import typing
from typing import *
from abc import ABC

# Imports End


class Base32Test(unittest.TestCase):

    # Class Fields Begin
    __BASE32_TEST_CASES_CHUNKED: List[List[str]] = [
        ["", ""],
        ["f", "MY======"],
        ["fo", "MZXQ===="],
        ["foo", "MZXW6==="],
        ["foob", "MZXW6YQ="],
        ["fooba", "MZXW6YTB"],
        ["foobar", "MZXW6YTBOI======"],
    ]
    __BASE32_PAD_TEST_CASES: List[List[str]] = [
        ["", ""],
        ["f", "MY%%%%%%"],
        ["fo", "MZXQ%%%%"],
        ["foo", "MZXW6%%%"],
        ["foob", "MZXW6YQ%"],
        ["fooba", "MZXW6YTB"],
        ["foobar", "MZXW6YTBOI%%%%%%"],
    ]
    __CHARSET_UTF8: str = ""  # LLM could not translate field
    __BASE32_TEST_CASES: List[List[str]] = [
        ["", ""],
        ["f", "MY======"],
        ["fo", "MZXQ===="],
        ["foo", "MZXW6==="],
        ["foob", "MZXW6YQ="],
        ["fooba", "MZXW6YTB"],
        ["foobar", "MZXW6YTBOI======"],
    ]
    BASE32_IMPOSSIBLE_CASES: typing.List[str] = ""  # LLM could not translate field
    __BASE32_IMPOSSIBLE_CASES_CHUNKED: List[str] = [
        "M2======\r\n",
        "MZX0====\r\n",
        "MZXW0===\r\n",
        "MZXW6Y2=\r\n",
        "MZXW6YTBO2======\r\n",
    ]
    __BASE32HEX_IMPOSSIBLE_CASES: List[str] = [
        "C2======",
        "CPN4====",
        "CPNM1===",
        "CPNMUO1=",
        "CPNMUOJ1E2======",
    ]
    __ENCODE_TABLE: bytes = b"ABCDEFGHIJKLMNOPQRSTUVWXYZ234567"
    __BASE32_BINARY_TEST_CASES: typing.List[typing.List[typing.Any]] = None
    __BASE32HEX_TEST_CASES: List[List[str]] = [
        ["", ""],
        ["f", "CO======"],
        ["fo", "CPNG===="],
        ["foo", "CPNMU==="],
        ["foob", "CPNMUOG="],
        ["fooba", "CPNMUOJ1"],
        ["foobar", "CPNMUOJ1E8======"],
    ]
    # Class Fields End

    # Class Methods Begin
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
            self.BASE32_IMPOSSIBLE_CASES_CHUNKED,
        )

    def testBase32ImpossibleSamples(self) -> None:

        self.__testImpossibleCases(
            Base32(0, None, False, BaseNCodec.PAD_DEFAULT, CodecPolicy.STRICT),
            self.BASE32_IMPOSSIBLE_CASES,
        )

    def testSingleCharEncoding(self) -> None:

        for i in range(20):
            codec = Base32.Base320()
            context = BaseNCodec.Context()
            unencoded = bytearray(i)
            all_in_one = codec.encode0(unencoded)
            codec = Base32.Base320()
            for j in range(unencoded.length):
                codec.encode2(unencoded, j, 1, context)
            codec.encode2(unencoded, 0, -1, context)
            singly = bytearray(all_in_one.length)
            codec.readResults(singly, 0, 100, context)
            if not all_in_one == singly:
                self.fail()

    def testRandomBytesHex(self) -> None:

        for i in range(20):
            codec = Base32.Base321(True)
            b = BaseNTestData.randomData(codec, i)
            self.assertEqual(
                f"{i} {codec.lineLength}", b[1].length, codec.getEncodedLength(b[0])
            )

    def testRandomBytesChunked(self) -> None:

        for i in range(20):
            codec = Base32.Base324(10)
            b = BaseNTestData.randomData(codec, i)
            self.assertEqual(
                str(i) + " " + str(codec.lineLength),
                b[1].length,
                codec.getEncodedLength(b[0]),
            )

    def testRandomBytes(self) -> None:

        for i in range(20):
            codec = Base32.Base320()
            b = BaseNTestData.randomData(codec, i)
            self.assertEqual(
                f"{i} {codec.lineLength}", b[1].length, codec.getEncodedLength(b[0])
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

        empty = b""
        result = Base32.Base320().encode0(empty)
        self.assertEqual(result, b"")
        self.assertIsNone(Base32.Base320().encode0(None))
        result = Base32.Base320().encode1(empty, 0, 1)
        self.assertEqual(result, b"")
        self.assertIsNone(Base32.Base320().encode0(None))
        empty = bytearray(0)
        result = Base32.Base320().decode0(empty)
        self.assertEqual(result, b"")
        self.assertIsNone(Base32.Base320().decode0(None))

    def testConstructors(self) -> None:

        base32: Base32
        base32 = Base32.Base320()
        base32 = Base32.Base324(-1)
        base32 = Base32.Base325(-1, b"")
        base32 = Base32.Base325(32, b"")
        base32 = Base32.Base326(32, b"", False)
        base32 = Base32.Base325(-1, b"A")
        try:
            base32 = Base32.Base325(32, None)
            self.fail("Should have rejected null line separator")
        except IllegalArgumentException:
            pass
        try:
            base32 = Base32.Base325(32, b"A")
            self.fail("Should have rejected attempt to use 'A' as a line separator")
        except IllegalArgumentException:
            pass
        try:
            base32 = Base32.Base325(32, b"=")
            self.fail("Should have rejected attempt to use '=' as a line separator")
        except IllegalArgumentException:
            pass
        base32 = Base32.Base325(32, b"$")  # OK
        try:
            base32 = Base32.Base325(32, b"A$")
            self.fail("Should have rejected attempt to use 'A$' as a line separator")
        except IllegalArgumentException:
            pass
        try:
            base32 = Base32.Base327(32, b"\n", False, b"A")
            self.fail("Should have rejected attempt to use 'A' as padding")
        except IllegalArgumentException:
            pass
        try:
            base32 = Base32.Base327(32, b"\n", False, b" ")
            self.fail("Should have rejected attempt to use ' ' as padding")
        except IllegalArgumentException:
            pass
        base32 = Base32.Base325(32, b" $")  # OK
        assert base32 is not None

    def testCodec200(self) -> None:

        codec = Base32.Base322(True, "W")
        assert codec is not None

    def testBase32SamplesNonDefaultPadding(self) -> None:

        codec = Base32.Base323(0x25)  # '%' <=> 0x25
        for element in BASE32_PAD_TEST_CASES:
            self.assertEqual(
                element[1], codec.encodeAsString(element[0].encode(self.__CHARSET_UTF8))
            )

    def testBase32BinarySamplesReverse(self) -> None:

        codec = Base32.Base320()
        for element in BASE32_BINARY_TEST_CASES:
            assertArrayEquals(element[0], codec.decode3(element[1]))

    def testBase32BinarySamples(self) -> None:

        codec = Base32.Base320()
        for element in BASE32_BINARY_TEST_CASES:
            expected = element[2] if len(element) > 2 else element[1]
            self.assertEqual(expected.upper(), codec.encodeAsString(element[0]))

    def testBase32Samples(self) -> None:

        codec = Base32.Base320()
        for element in BASE32_TEST_CASES:
            assert element[1] == codec.encodeAsString(
                element[0].encode(self.__CHARSET_UTF8)
            )

    def testBase32HexSamplesReverseLowercase(self) -> None:

        codec = Base32.Base321(True)
        for element in BASE32HEX_TEST_CASES:
            self.assertEqual(
                element[0],
                bytes(
                    codec.decode3(element[1].lower()), encoding=CHARSET_UTF8
                ).decode(),
            )

    def testBase32HexSamplesReverse(self) -> None:

        codec = Base32.Base321(True)
        for element in BASE32HEX_TEST_CASES:
            assert element[0] == bytes(codec.decode3(element[1])).decode(CHARSET_UTF8)

    def testBase32HexSamples(self) -> None:

        codec = Base32.Base321(True)
        for element in BASE32HEX_TEST_CASES:
            self.assertEqual(
                element[1], codec.encodeAsString(element[0].encode(CHARSET_UTF8))
            )

    def testBase32Chunked(self) -> None:

        codec = Base32.Base324(20)
        for element in BASE32_TEST_CASES_CHUNKED:
            self.assertEqual(
                element[1], codec.encodeAsString(element[0].encode(encoding="utf-8"))
            )

    @staticmethod
    def __assertBase32DecodingOfTrailingBits(nbits: int) -> None:

        pass  # LLM could not translate method body

    def __testImpossibleCases(
        self, codec: Base32, impossible_cases: typing.List[str]
    ) -> None:

        for impossible in impossible_cases:
            try:
                codec.decode3(impossible)
                fail()
            except IllegalArgumentException:
                pass

    # Class Methods End
