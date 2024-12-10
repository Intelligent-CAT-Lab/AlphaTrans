from __future__ import annotations

# Imports Begin
from src.main.org.apache.commons.codec.binary.BaseNCodec import *
import unittest
import os
import typing
from typing import *
import io

# Imports End


class NoOpBaseNCodec(BaseNCodec):

    # Class Fields Begin
    # Class Fields End

    # Class Methods Begin
    def _isInAlphabet0(self, value: int) -> bool:
        pass

    def decode1(
        self, pArray: typing.List[int], i: int, length: int, context: Context
    ) -> None:
        pass

    def encode2(
        self, pArray: typing.List[int], i: int, length: int, context: Context
    ) -> None:
        pass

    def __init__(self) -> None:
        pass

    # Class Methods End


class BaseNCodecTest(unittest.TestCase):

    # Class Fields Begin
    codec: BaseNCodec = None
    # Class Fields End

    # Class Methods Begin
    def testEnsureBufferSizeThrowsOnOverflow_test2_decomposed(self) -> None:
        pass

    def testEnsureBufferSizeThrowsOnOverflow_test1_decomposed(self) -> None:
        pass

    def testEnsureBufferSizeThrowsOnOverflow_test0_decomposed(self) -> None:
        pass

    def testEnsureBufferSizeExpandsToBeyondMaxBufferSize_test0_decomposed(self) -> None:
        pass

    def testEnsureBufferSizeExpandsToMaxBufferSize_test0_decomposed(self) -> None:
        pass

    def testEnsureBufferSize_test9_decomposed(self) -> None:
        pass

    def testEnsureBufferSize_test8_decomposed(self) -> None:
        pass

    def testEnsureBufferSize_test7_decomposed(self) -> None:
        pass

    def testEnsureBufferSize_test6_decomposed(self) -> None:
        pass

    def testEnsureBufferSize_test5_decomposed(self) -> None:
        pass

    def testEnsureBufferSize_test4_decomposed(self) -> None:
        pass

    def testEnsureBufferSize_test3_decomposed(self) -> None:
        pass

    def testEnsureBufferSize_test2_decomposed(self) -> None:
        pass

    def testEnsureBufferSize_test1_decomposed(self) -> None:
        pass

    def testEnsureBufferSize_test0_decomposed(self) -> None:
        pass

    def testProvidePaddingByte_test1_decomposed(self) -> None:
        pass

    def testProvidePaddingByte_test0_decomposed(self) -> None:
        pass

    def testContainsAlphabetOrPad_test7_decomposed(self) -> None:
        pass

    def testContainsAlphabetOrPad_test6_decomposed(self) -> None:
        pass

    def testContainsAlphabetOrPad_test5_decomposed(self) -> None:
        pass

    def testContainsAlphabetOrPad_test4_decomposed(self) -> None:
        pass

    def testContainsAlphabetOrPad_test3_decomposed(self) -> None:
        pass

    def testContainsAlphabetOrPad_test2_decomposed(self) -> None:
        pass

    def testContainsAlphabetOrPad_test1_decomposed(self) -> None:
        pass

    def testContainsAlphabetOrPad_test0_decomposed(self) -> None:
        pass

    def testIsInAlphabetString_test0_decomposed(self) -> None:
        pass

    def testIsInAlphabetByteArrayBoolean_test0_decomposed(self) -> None:
        pass

    def testIsInAlphabetByte_test0_decomposed(self) -> None:
        pass

    def testIsWhiteSpace_test0_decomposed(self) -> None:
        pass

    def testBaseNCodec_test0_decomposed(self) -> None:
        pass

    def testContextToString_test2_decomposed(self) -> None:
        pass

    def testContextToString_test1_decomposed(self) -> None:
        pass

    def testContextToString_test0_decomposed(self) -> None:
        pass

    def setUp(self) -> None:
        pass

    @staticmethod
    def getPresumableFreeMemory() -> int:
        pass

    @staticmethod
    def __assumeCanAllocateBufferSize(size: int) -> None:
        pass

    @staticmethod
    def __assertEnsureBufferSizeExpandsToMaxBufferSize(
        exceedMaxBufferSize: bool,
    ) -> None:
        pass

    # Class Methods End
