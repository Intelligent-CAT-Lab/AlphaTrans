from __future__ import annotations

# Imports Begin
from src.main.me.lemire.integercompression.differential.SkippableIntegratedIntegerCODEC import *
from src.main.me.lemire.integercompression.differential.IntegratedIntegerCODEC import *
from src.main.me.lemire.integercompression.differential.IntegratedByteIntegerCODEC import *
from src.main.me.lemire.integercompression.IntWrapper import *
import os
import typing
from typing import *
import io

# Imports End


class IntegratedVariableByte(
    IntegratedByteIntegerCODEC, IntegratedIntegerCODEC, SkippableIntegratedIntegerCODEC
):

    # Class Fields Begin
    # Class Fields End

    # Class Methods Begin
    def headlessUncompress(
        self,
        in_: typing.List[int],
        inpos: IntWrapper,
        inlength: int,
        out: typing.List[int],
        outpos: IntWrapper,
        num: int,
        initvalue: IntWrapper,
    ) -> None:
        pass

    def headlessCompress(
        self,
        in_: typing.List[int],
        inpos: IntWrapper,
        inlength: int,
        out: typing.List[int],
        outpos: IntWrapper,
        initvalue: IntWrapper,
    ) -> None:
        pass

    def toString(self) -> str:
        pass

    def uncompress1(
        self,
        in_: typing.List[int],
        inpos: IntWrapper,
        inlength: int,
        out: typing.List[int],
        outpos: IntWrapper,
    ) -> None:
        pass

    def uncompress0(
        self,
        in_: typing.List[int],
        inpos: IntWrapper,
        inlength: int,
        out: typing.List[int],
        outpos: IntWrapper,
    ) -> None:
        pass

    def compress1(
        self,
        in_: typing.List[int],
        inpos: IntWrapper,
        inlength: int,
        out: typing.List[int],
        outpos: IntWrapper,
    ) -> None:
        pass

    def compress0(
        self,
        in_: typing.List[int],
        inpos: IntWrapper,
        inlength: int,
        out: typing.List[int],
        outpos: IntWrapper,
    ) -> None:
        pass

    def _makeBuffer(self, sizeInBytes: int) -> typing.Union[bytearray, memoryview]:
        pass

    @staticmethod
    def __extract7bitsmaskless(i: int, val: int) -> int:
        pass

    @staticmethod
    def __extract7bits(i: int, val: int) -> int:
        pass

    # Class Methods End
