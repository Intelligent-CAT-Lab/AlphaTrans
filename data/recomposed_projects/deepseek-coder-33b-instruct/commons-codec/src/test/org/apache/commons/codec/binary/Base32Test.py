from __future__ import annotations
import re
import random
import unittest
import pytest
import io
import typing
from typing import *
import os
from src.main.org.apache.commons.codec.CodecPolicy import *
from src.main.org.apache.commons.codec.DecoderException import *
from src.main.org.apache.commons.codec.binary.Base32 import *
from src.main.org.apache.commons.codec.binary.BaseNCodec import *
from src.test.org.apache.commons.codec.binary.BaseNTestData import *
from src.main.org.apache.commons.codec.binary.Hex import *


class Base32Test(unittest.TestCase):

    BASE32_IMPOSSIBLE_CASES: List[str] = [
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
        ord("A"),
        ord("B"),
        ord("C"),
        ord("D"),
        ord("E"),
        ord("F"),
        ord("G"),
        ord("H"),
        ord("I"),
        ord("J"),
        ord("K"),
        ord("L"),
        ord("M"),
        ord("N"),
        ord("O"),
        ord("P"),
        ord("Q"),
        ord("R"),
        ord("S"),
        ord("T"),
        ord("U"),
        ord("V"),
        ord("W"),
        ord("X"),
        ord("Y"),
        ord("Z"),
        ord("2"),
        ord("3"),
        ord("4"),
        ord("5"),
        ord("6"),
        ord("7"),
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

    def testBase32DecodingOfTrailing35Bits(self) -> None:

        def __assertBase32DecodingOfTrailingBits(nbits: int) -> None:
            pass

        __assertBase32DecodingOfTrailingBits(35)

    def testBase32DecodingOfTrailing30Bits(self) -> None:

        def __assertBase32DecodingOfTrailingBits(nbits: int) -> None:
            pass

        __assertBase32DecodingOfTrailingBits(30)

    def testBase32DecodingOfTrailing25Bits(self) -> None:

        def __assertBase32DecodingOfTrailingBits(nbits: int) -> None:
            pass

        __assertBase32DecodingOfTrailingBits(25)

    def testBase32DecodingOfTrailing20Bits(self) -> None:

        def __assertBase32DecodingOfTrailingBits(nbits: int) -> None:
            pass

        __assertBase32DecodingOfTrailingBits(20)

    def testBase32DecodingOfTrailing15Bits(self) -> None:

        def __assertBase32DecodingOfTrailingBits(nbits: int) -> None:
            pass

        __assertBase32DecodingOfTrailingBits(15)

    def testBase32DecodingOfTrailing10Bits(self) -> None:

        def __assertBase32DecodingOfTrailingBits(nbits: int) -> None:
            pass

        __assertBase32DecodingOfTrailingBits(10)

    def testBase32DecodingOfTrailing5Bits(self) -> None:

        def __assertBase32DecodingOfTrailingBits(nbits: int) -> None:
            pass

        __assertBase32DecodingOfTrailingBits(5)

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
            unencoded = bytearray(i)
            allInOne = codec.encode0(unencoded)
            codec = Base32.Base320()
            for j in range(len(unencoded)):
                codec.encode2(unencoded, j, 1, context)
            codec.encode2(unencoded, 0, -1, context)
            singly = bytearray(len(allInOne))
            codec.readResults(singly, 0, 100, context)
            if allInOne != singly:
                self.fail()

    def testRandomBytesHex(self) -> None:

        for i in range(20):
            codec = Base32.Base321(True)
            b = BaseNTestData.randomData(codec, i)
            assert str(i) + " " + str(codec.lineLength) == codec.getEncodedLength(b[0])

    def testRandomBytesChunked(self) -> None:

        for i in range(20):
            codec = Base32.Base324(10)
            b = BaseNTestData.randomData(codec, i)
            assert str(i) + " " + str(codec.lineLength) + " " + str(b[1].length) == str(
                codec.getEncodedLength(b[0])
            )

    def testRandomBytes(self) -> None:

        for i in range(20):
            codec = Base32.Base320()
            b = BaseNTestData.randomData(codec, i)
            assert str(i) + " " + str(codec.lineLength) == codec.getEncodedLength(b[0])

    def testIsInAlphabet(self) -> None:

        b32 = Base32.Base321(True)
        assert not b32.isInAlphabet0(0)
        assert not b32.isInAlphabet0(1)
        assert not b32.isInAlphabet0(-1)
        assert not b32.isInAlphabet0(-15)
        assert not b32.isInAlphabet0(-32)
        assert not b32.isInAlphabet0(127)
        assert not b32.isInAlphabet0(128)
        assert not b32.isInAlphabet0(255)

        b32 = Base32.Base321(False)
        for c in range(ord("2"), ord("7") + 1):
            assert b32.isInAlphabet0(c)
        for c in range(ord("A"), ord("Z") + 1):
            assert b32.isInAlphabet0(c)
        for c in range(ord("a"), ord("z") + 1):
            assert b32.isInAlphabet0(c)
        assert not b32.isInAlphabet0(ord("1"))
        assert not b32.isInAlphabet0(ord("8"))
        assert not b32.isInAlphabet0(ord("A") - 1)
        assert not b32.isInAlphabet0(ord("Z") + 1)

        b32 = Base32.Base321(True)
        for c in range(ord("0"), ord("9") + 1):
            assert b32.isInAlphabet0(c)
        for c in range(ord("A"), ord("V") + 1):
            assert b32.isInAlphabet0(c)
        for c in range(ord("a"), ord("v") + 1):
            assert b32.isInAlphabet0(c)
        assert not b32.isInAlphabet0(ord("0") - 1)
        assert not b32.isInAlphabet0(ord("9") + 1)
        assert not b32.isInAlphabet0(ord("A") - 1)
        assert not b32.isInAlphabet0(ord("V") + 1)
        assert not b32.isInAlphabet0(ord("a") - 1)
        assert not b32.isInAlphabet0(ord("v") + 1)

    def testEmptyBase32(self) -> None:

        empty: bytearray = bytearray()
        result: bytearray = Base32.Base320().encode0(empty)
        assert len(result) == 0, "empty Base32 encode"
        assert Base32.Base320().encode0(None) is None, "empty Base32 encode"
        result = Base32.Base320().encode1(empty, 0, 1)
        assert len(result) == 0, "empty Base32 encode with offset"
        assert Base32.Base320().encode0(None) is None, "empty Base32 encode with offset"

        empty = bytearray(0)
        result = Base32.Base320().decode0(empty)
        assert len(result) == 0, "empty Base32 decode"
        assert Base32.Base320().decode0(None) is None, "empty Base32 decode"

    def testConstructors(self) -> None:

        base32 = Base32.Base320()
        base32 = Base32.Base324(-1)
        base32 = Base32.Base325(-1, bytearray())
        base32 = Base32.Base325(32, bytearray())
        base32 = Base32.Base326(32, bytearray(), False)
        base32 = Base32.Base325(-1, bytearray(b"A"))
        try:
            base32 = Base32.Base325(32, None)
            self.fail("Should have rejected null line separator")
        except ValueError:
            pass
        try:
            base32 = Base32.Base325(32, bytearray(b"A"))
            self.fail("Should have rejected attempt to use 'A' as a line separator")
        except ValueError:
            pass
        try:
            base32 = Base32.Base325(32, bytearray(b"="))
            self.fail("Should have rejected attempt to use '=' as a line separator")
        except ValueError:
            pass
        base32 = Base32.Base325(32, bytearray(b"$"))  # OK
        try:
            base32 = Base32.Base325(32, bytearray(b"A$"))
            self.fail("Should have rejected attempt to use 'A$' as a line separator")
        except ValueError:
            pass
        try:
            base32 = Base32.Base327(32, bytearray(b"\n"), False, ord("A"))
            self.fail("Should have rejected attempt to use 'A' as padding")
        except ValueError:
            pass
        try:
            base32 = Base32.Base327(32, bytearray(b"\n"), False, ord(" "))
            self.fail("Should have rejected attempt to use ' ' as padding")
        except ValueError:
            pass
        base32 = Base32.Base325(32, bytearray(b" $\n\r\t"))  # OK
        assert base32 is not None

    def testCodec200(self) -> None:

        codec = Base32.Base322(True, ord("W"))  # should be allowed
        assert codec is not None

    def testBase32SamplesNonDefaultPadding(self) -> None:

        codec = Base32.Base323(0x25)  # '%' <=> 0x25

        for element in self.__BASE32_PAD_TEST_CASES:
            assert element[1] == codec.encodeAsString(
                element[0].encode(self.__CHARSET_UTF8)
            )

    def testBase32BinarySamplesReverse(self) -> None:

        codec = Base32.Base320()
        for element in self.__BASE32_BINARY_TEST_CASES:
            assert self.arrays_equal(element[0], codec.decode3(element[1]))

    def arrays_equal(self, a: List[int], b: List[int]) -> bool:
        return a == b

    def testBase32BinarySamples(self) -> None:

        codec = Base32.Base320()
        for element in self.__BASE32_BINARY_TEST_CASES:
            if len(element) > 2:
                expected = element[2]
            else:
                expected = element[1]
            assert expected.upper() == codec.encodeAsString(element[0])

    def testBase32Samples(self) -> None:

        codec = Base32.Base320()
        for element in self.__BASE32_TEST_CASES:
            assert element[1] == codec.encodeAsString(
                element[0].encode(self.__CHARSET_UTF8)
            )

    def testBase32HexSamplesReverseLowercase(self) -> None:

        codec = Base32.Base321(True)
        for element in self.__BASE32HEX_TEST_CASES:
            decoded = codec.decode3(element[1].lower())
            decoded_str = decoded.decode(self.__CHARSET_UTF8)
            assert element[0] == decoded_str

    def testBase32HexSamplesReverse(self) -> None:

        codec = Base32.Base321(True)
        for element in self.__BASE32HEX_TEST_CASES:
            decoded = codec.decode3(element[1])
            decoded_str = str(decoded, self.__CHARSET_UTF8)
            assert decoded_str == element[0]

    def testBase32HexSamples(self) -> None:

        codec = Base32.Base321(True)
        for element in self.__BASE32HEX_TEST_CASES:
            assert element[1] == codec.encodeAsString(
                element[0].encode(self.__CHARSET_UTF8)
            )

    def testBase32Chunked(self) -> None:

        codec = Base32.Base324(20)
        for element in self.__BASE32_TEST_CASES_CHUNKED:
            assert element[1] == codec.encodeAsString(
                element[0].encode(self.__CHARSET_UTF8)
            )

    @staticmethod
    def __assertBase32DecodingOfTrailingBits(nbits: int) -> None:

        codec = Base32(0, None, False, BaseNCodec.PAD_DEFAULT, CodecPolicy.STRICT)
        assert codec.isStrictDecoding()
        assert CodecPolicy.STRICT == codec.getCodecPolicy()
        defaultCodec = Base32.Base320()
        assert not defaultCodec.isStrictDecoding()
        assert CodecPolicy.LENIENT == defaultCodec.getCodecPolicy()

        length = nbits // 5
        encoded = bytearray(8)
        encoded[:length] = [Base32Test.__ENCODE_TABLE[0]] * length
        encoded[length:] = [ord("=")] * (len(encoded) - length)
        discard = nbits % 8
        emptyBitsMask = (1 << discard) - 1
        invalid = length == 1 or length == 3 or length == 6
        last = length - 1
        for i in range(32):
            encoded[last] = Base32Test.__ENCODE_TABLE[i]
            if invalid or (i & emptyBitsMask) != 0:
                try:
                    codec.decode0(encoded)
                    assert False, "Final base-32 digit should not be allowed"
                except ValueError:
                    pass
                decoded = defaultCodec.decode0(encoded)
                assert not list(encoded) == list(defaultCodec.encode0(decoded))
            else:
                decoded = codec.decode0(encoded)
                bitsEncoded = i >> discard
                assert bitsEncoded == decoded[-1], "Invalid decoding of last character"
                assert list(encoded) == list(codec.encode0(decoded))

    def __testImpossibleCases(
        self, codec: Base32, impossible_cases: typing.List[str]
    ) -> None:

        for impossible in impossible_cases:
            try:
                codec.decode3(impossible)
                self.fail()
            except ValueError:
                pass
