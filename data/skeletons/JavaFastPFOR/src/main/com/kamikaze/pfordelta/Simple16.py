from __future__ import annotations

# Imports Begin
from src.main.me.lemire.integercompression.SkippableIntegerCODEC import *
from src.main.me.lemire.integercompression.IntegerCODEC import *
from src.main.me.lemire.integercompression.IntWrapper import *
import typing
from typing import *
import io

# Imports End


class Simple16:

    # Class Fields Begin
    __S16_NUMSIZE: int = None
    __S16_BITSSIZE: int = None
    __S16_NUM: typing.List[int] = None
    __S16_BITS: typing.List[typing.List[int]] = None
    # Class Fields End

    # Class Methods Begin
    @staticmethod
    def s16Decompress(
        out: typing.List[int],
        outOffset: int,
        in_: typing.List[int],
        inOffset: int,
        n: int,
    ) -> int:
        pass

    @staticmethod
    def s16Compress(
        out: typing.List[int],
        outOffset: int,
        in_: typing.List[int],
        inOffset: int,
        n: int,
        blockSize: int,
    ) -> int:
        pass

    @staticmethod
    def __readBitsForS16(
        in_: typing.List[int], inIntOffset: int, inWithIntOffset: int, bits: int
    ) -> int:
        pass

    # Class Methods End
