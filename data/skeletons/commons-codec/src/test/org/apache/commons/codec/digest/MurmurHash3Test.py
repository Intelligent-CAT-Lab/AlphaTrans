from __future__ import annotations

# Imports Begin
from src.main.org.apache.commons.codec.digest.MurmurHash3 import *
from src.main.org.apache.commons.codec.binary.StringUtils import *
import unittest
import typing
from typing import *
import io

# Imports End


class MurmurHash3Test(unittest.TestCase):

    # Class Fields Begin
    __RANDOM_BYTES: typing.List[int] = None
    __TEST_HASH64: str = None
    __RANDOM_INTS: typing.List[int] = None
    # Class Fields End

    # Class Methods Begin
    def testIncrementalHashWithUnprocessedBytesAndHugeLengthArray(self) -> None:
        pass

    def testIncrementalHash32x86(self) -> None:
        pass

    def testIncrementalHash32(self) -> None:
        pass

    def testHash128x64WithOffsetLengthAndNegativeSeed(self) -> None:
        pass

    def testHash128x64WithOffsetLengthAndSeed(self) -> None:
        pass

    def testHash128x64(self) -> None:
        pass

    def testHash128String(self) -> None:
        pass

    def testHash128WithOffsetLengthAndNegativeSeed(self) -> None:
        pass

    def testHash128WithOffsetLengthAndSeed(self) -> None:
        pass

    def testHash128(self) -> None:
        pass

    def testHash64InNotEqualToHash128(self) -> None:
        pass

    def testHash64WithPrimitives(self) -> None:
        pass

    def testHash64WithOffsetAndLength(self) -> None:
        pass

    def testHash64(self) -> None:
        pass

    def testHash32x86WithTrailingNegativeSignedBytes(self) -> None:
        pass

    def testHash32x86WithOffsetLengthAndSeed(self) -> None:
        pass

    def testhash32x86(self) -> None:
        pass

    def testHash32WithTrailingNegativeSignedBytesIsInvalid(self) -> None:
        pass

    def testHash32String(self) -> None:
        pass

    def testHash32WithOffsetLengthAndSeed(self) -> None:
        pass

    def testHash32WithLengthAndSeed(self) -> None:
        pass

    def testHash32WithLength(self) -> None:
        pass

    def testHash32(self) -> None:
        pass

    def testHash32LongSeed(self) -> None:
        pass

    def testHash32Long(self) -> None:
        pass

    def testHash32LongLongSeed(self) -> None:
        pass

    def testHash32LongLong(self) -> None:
        pass

    @staticmethod
    def __createRandomBlocks(maxLength: int) -> typing.List[int]:
        pass

    @staticmethod
    def __assertIncrementalHash32x86(
        bytes_: typing.List[int], seed: int, blocks: typing.List[int]
    ) -> None:
        pass

    @staticmethod
    def __assertIncrementalHash32(
        bytes_: typing.List[int], seed: int, blocks: typing.List[int]
    ) -> None:
        pass

    @staticmethod
    def __negativeBytes(bytes_: typing.List[int], start: int, length: int) -> bool:
        pass

    @staticmethod
    def __createLongTestData() -> typing.List[int]:
        pass

    # Class Methods End
