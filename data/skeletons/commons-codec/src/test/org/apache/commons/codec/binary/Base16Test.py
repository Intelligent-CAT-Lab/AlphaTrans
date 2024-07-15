from __future__ import annotations

# Imports Begin
from src.main.org.apache.commons.codec.binary.StringUtils import *
from src.test.org.apache.commons.codec.binary.BaseNTestData import *
from src.main.org.apache.commons.codec.binary.BaseNCodec import *
from src.test.org.apache.commons.codec.binary.Base16TestData import *
from src.main.org.apache.commons.codec.binary.Base16 import *
from src.main.org.apache.commons.codec.EncoderException import *
from src.main.org.apache.commons.codec.DecoderException import *
from src.main.org.apache.commons.codec.CodecPolicy import *
import unittest
import typing
from typing import *
import io

# Imports End


class Base16Test(unittest.TestCase):

    # Class Fields Begin
    __CHARSET_UTF8: str = None
    __random: random.Random = None
    # Class Fields End

    # Class Methods Begin
    def testLenientDecoding(self) -> None:
        pass

    def testStrictDecoding(self) -> None:
        pass

    def testDecodeSingleBytesOptimisation(self) -> None:
        pass

    def testDecodeSingleBytes(self) -> None:
        pass

    def testIsInAlphabet(self) -> None:
        pass

    def checkEncodeLengthBounds(self) -> None:
        pass

    def testStringToByteVariations(self) -> None:
        pass

    def testByteToStringVariations(self) -> None:
        pass

    def testTriplets(self) -> None:
        pass

    def testSingletons(self) -> None:
        pass

    def testPairs(self) -> None:
        pass

    def testObjectEncode(self) -> None:
        pass

    def testObjectEncodeWithValidParameter(self) -> None:
        pass

    def testObjectEncodeWithInvalidParameter(self) -> None:
        pass

    def testObjectDecodeWithValidParameter(self) -> None:
        pass

    def testObjectDecodeWithInvalidParameter(self) -> None:
        pass

    def testNonBase16Test(self) -> None:
        pass

    def testKnownEncodings(self) -> None:
        pass

    def testKnownDecodings(self) -> None:
        pass

    def testEncodeDecodeSmall(self) -> None:
        pass

    def testEncodeDecodeRandom(self) -> None:
        pass

    def testEmptyBase16(self) -> None:
        pass

    def testConstructor_LowerCase_DecodingPolicy(self) -> None:
        pass

    def testConstructor_LowerCase(self) -> None:
        pass

    def testConstructors(self) -> None:
        pass

    def testCodec68(self) -> None:
        pass

    def testBase16(self) -> None:
        pass

    def getRandom(self) -> random.Random:
        pass

    def __toString(self, data: typing.List[int]) -> str:
        pass

    # Class Methods End
