from __future__ import annotations

# Imports Begin
from src.main.me.lemire.integercompression.SkippableIntegerCODEC import *
from src.main.me.lemire.integercompression.IntegerCODEC import *
from src.main.me.lemire.integercompression.IntWrapper import *
import os
import typing
from typing import *
import io

# Imports End


class Simple16(IntegerCODEC, SkippableIntegerCODEC):

    # Class Fields Begin
    __S16_NUMSIZE: int = None
    __S16_BITSSIZE: int = None
    __S16_NUM: typing.List[int] = None
    __S16_BITS: typing.List[typing.List[int]] = None
    __SHIFTED_S16_BITS: typing.List[typing.List[int]] = None
    # Class Fields End

    # Class Methods Begin
    def toString(self) -> str:
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

    def compress0(
        self,
        in_: typing.List[int],
        inpos: IntWrapper,
        inlength: int,
        out: typing.List[int],
        outpos: IntWrapper,
    ) -> None:
        pass

    def headlessUncompress(
        self,
        in_: typing.List[int],
        inpos: IntWrapper,
        inlength: int,
        out: typing.List[int],
        outpos: IntWrapper,
        num: int,
    ) -> None:
        pass

    @staticmethod
    def uncompress(
        in_: typing.List[int],
        tmpinpos: int,
        inlength: int,
        out: typing.List[int],
        currentPos: int,
        outlength: int,
    ) -> None:
        pass

    @staticmethod
    def decompressblock(
        out: typing.List[int],
        outOffset: int,
        in_: typing.List[int],
        inOffset: int,
        n: int,
    ) -> int:
        pass

    @staticmethod
    def compressblock(
        out: typing.List[int],
        outOffset: int,
        in_: typing.List[int],
        inOffset: int,
        n: int,
    ) -> int:
        pass

    def headlessCompress(
        self,
        in_: typing.List[int],
        inpos: IntWrapper,
        inlength: int,
        out: typing.List[int],
        outpos: IntWrapper,
    ) -> None:
        pass

    @staticmethod
    def __shiftme(x: typing.List[typing.List[int]]) -> typing.List[typing.List[int]]:
        pass

    # Class Methods End
