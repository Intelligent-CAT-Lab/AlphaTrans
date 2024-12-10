from __future__ import annotations

# Imports Begin
from src.main.me.lemire.integercompression.IntegerCODEC import *
from src.main.me.lemire.integercompression.IntWrapper import *
from src.main.me.lemire.integercompression.DeltaZigzagEncoding import *
import os
import typing
from typing import *
import io

# Imports End


class DeltaZigzagVariableByte(IntegerCODEC):

    # Class Fields Begin
    # Class Fields End

    # Class Methods Begin
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

    def toString(self) -> str:
        pass

    def _makeBuffer(self, sizeInBytes: int) -> typing.Union[bytearray, memoryview]:
        pass

    # Class Methods End
