from __future__ import annotations

# Imports Begin
from src.main.org.apache.commons.codec.digest.MurmurHash3 import *
from src.main.org.apache.commons.codec.binary.StringUtils import *
import unittest
import os
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
    def testIncrementalHashWithUnprocessedBytesAndHugeLengthArray_test3_decomposed(
        self,
    ) -> None:
        pass

    def testIncrementalHashWithUnprocessedBytesAndHugeLengthArray_test2_decomposed(
        self,
    ) -> None:
        pass

    def testIncrementalHashWithUnprocessedBytesAndHugeLengthArray_test1_decomposed(
        self,
    ) -> None:
        pass

    def testIncrementalHashWithUnprocessedBytesAndHugeLengthArray_test0_decomposed(
        self,
    ) -> None:
        pass

    def testIncrementalHash32x86_test0_decomposed(self) -> None:
        pass

    def testIncrementalHash32_test0_decomposed(self) -> None:
        pass

    def testHash128x64WithOffsetLengthAndNegativeSeed_test0_decomposed(self) -> None:
        pass

    def testHash128x64WithOffsetLengthAndSeed_test0_decomposed(self) -> None:
        pass

    def testHash128x64_test1_decomposed(self) -> None:
        pass

    def testHash128x64_test0_decomposed(self) -> None:
        pass

    def testHash128String_test0_decomposed(self) -> None:
        pass

    def testHash128WithOffsetLengthAndNegativeSeed_test0_decomposed(self) -> None:
        pass

    def testHash128WithOffsetLengthAndSeed_test0_decomposed(self) -> None:
        pass

    def testHash128_test1_decomposed(self) -> None:
        pass

    def testHash128_test0_decomposed(self) -> None:
        pass

    def testHash64InNotEqualToHash128_test0_decomposed(self) -> None:
        pass

    def testHash64WithPrimitives_test2_decomposed(self) -> None:
        pass

    def testHash64WithPrimitives_test1_decomposed(self) -> None:
        pass

    def testHash64WithPrimitives_test0_decomposed(self) -> None:
        pass

    def testHash64WithOffsetAndLength_test3_decomposed(self) -> None:
        pass

    def testHash64WithOffsetAndLength_test2_decomposed(self) -> None:
        pass

    def testHash64WithOffsetAndLength_test1_decomposed(self) -> None:
        pass

    def testHash64WithOffsetAndLength_test0_decomposed(self) -> None:
        pass

    def testHash64_test2_decomposed(self) -> None:
        pass

    def testHash64_test1_decomposed(self) -> None:
        pass

    def testHash64_test0_decomposed(self) -> None:
        pass

    def testHash32x86WithTrailingNegativeSignedBytes_test0_decomposed(self) -> None:
        pass

    def testHash32x86WithOffsetLengthAndSeed_test0_decomposed(self) -> None:
        pass

    def testhash32x86_test1_decomposed(self) -> None:
        pass

    def testhash32x86_test0_decomposed(self) -> None:
        pass

    def testHash32WithTrailingNegativeSignedBytesIsInvalid_test0_decomposed(
        self,
    ) -> None:
        pass

    def testHash32String_test0_decomposed(self) -> None:
        pass

    def testHash32WithOffsetLengthAndSeed_test0_decomposed(self) -> None:
        pass

    def testHash32WithLengthAndSeed_test1_decomposed(self) -> None:
        pass

    def testHash32WithLengthAndSeed_test0_decomposed(self) -> None:
        pass

    def testHash32WithLength_test1_decomposed(self) -> None:
        pass

    def testHash32WithLength_test0_decomposed(self) -> None:
        pass

    def testHash32_test1_decomposed(self) -> None:
        pass

    def testHash32_test0_decomposed(self) -> None:
        pass

    def testHash32LongSeed_test2_decomposed(self) -> None:
        pass

    def testHash32LongSeed_test1_decomposed(self) -> None:
        pass

    def testHash32LongSeed_test0_decomposed(self) -> None:
        pass

    def testHash32Long_test2_decomposed(self) -> None:
        pass

    def testHash32Long_test1_decomposed(self) -> None:
        pass

    def testHash32Long_test0_decomposed(self) -> None:
        pass

    def testHash32LongLongSeed_test2_decomposed(self) -> None:
        pass

    def testHash32LongLongSeed_test1_decomposed(self) -> None:
        pass

    def testHash32LongLongSeed_test0_decomposed(self) -> None:
        pass

    def testHash32LongLong_test2_decomposed(self) -> None:
        pass

    def testHash32LongLong_test1_decomposed(self) -> None:
        pass

    def testHash32LongLong_test0_decomposed(self) -> None:
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
