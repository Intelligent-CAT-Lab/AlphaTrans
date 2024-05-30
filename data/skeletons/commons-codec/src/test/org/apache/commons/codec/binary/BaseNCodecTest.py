from __future__ import annotations

# Imports Begin
from src.main.org.apache.commons.codec.binary.BaseNCodec import *
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


class BaseNCodecTest:

    # Class Fields Begin
    # Class Fields End

    # Class Methods Begin
    def testEnsureBufferSizeThrowsOnOverflow(self) -> None:
        pass

    def testEnsureBufferSizeExpandsToBeyondMaxBufferSize(self) -> None:
        pass

    def testEnsureBufferSizeExpandsToMaxBufferSize(self) -> None:
        pass

    def testEnsureBufferSize(self) -> None:
        pass

    def testProvidePaddingByte(self) -> None:
        pass

    def testContainsAlphabetOrPad(self) -> None:
        pass

    def testIsInAlphabetString(self) -> None:
        pass

    def testIsInAlphabetByteArrayBoolean(self) -> None:
        pass

    def testIsInAlphabetByte(self) -> None:
        pass

    def testIsWhiteSpace(self) -> None:
        pass

    def testBaseNCodec(self) -> None:
        pass

    def testContextToString(self) -> None:
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
