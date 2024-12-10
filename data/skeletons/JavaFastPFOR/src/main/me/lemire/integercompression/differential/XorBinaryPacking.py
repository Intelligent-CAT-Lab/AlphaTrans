from __future__ import annotations

# Imports Begin
from src.main.me.lemire.integercompression.differential.IntegratedIntegerCODEC import *
from src.main.me.lemire.integercompression.IntWrapper import *
from src.main.me.lemire.integercompression.BitPacking import *
import os
import typing
from typing import *
import io

# Imports End


class XorBinaryPacking(IntegratedIntegerCODEC):

    # Class Fields Begin
    __BLOCK_LENGTH: int = None
    # Class Fields End

    # Class Methods Begin
    def toString(self) -> str:
        pass

    def uncompress0(
        self,
        inBuf: typing.List[int],
        inPos: IntWrapper,
        inLen: int,
        outBuf: typing.List[int],
        outPos: IntWrapper,
    ) -> None:
        pass

    def compress0(
        self,
        inBuf: typing.List[int],
        inPos: IntWrapper,
        inLen: int,
        outBuf: typing.List[int],
        outPos: IntWrapper,
    ) -> None:
        pass

    @staticmethod
    def __xorUnpack(
        inBuf: typing.List[int],
        inOff: int,
        outBuf: typing.List[int],
        outOff: int,
        validBits: int,
        context: int,
        work: typing.List[int],
    ) -> int:
        pass

    @staticmethod
    def __xorPack(
        inBuf: typing.List[int],
        inOff: int,
        outBuf: typing.List[int],
        outOff: int,
        validBits: int,
        context: int,
        work: typing.List[int],
    ) -> int:
        pass

    @staticmethod
    def __xorMaxBits(
        buf: typing.List[int], offset: int, length: int, context: int
    ) -> int:
        pass

    # Class Methods End
