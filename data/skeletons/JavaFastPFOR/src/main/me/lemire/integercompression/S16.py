from __future__ import annotations

# Imports Begin
import os
import typing
from typing import *
import io

# Imports End


class S16:

    # Class Fields Begin
    __S16_NUMSIZE: int = None
    __S16_BITSSIZE: int = None
    __S16_NUM: typing.List[int] = None
    __S16_BITS: typing.List[typing.List[int]] = None
    __SHIFTED_S16_BITS: typing.List[typing.List[int]] = None
    # Class Fields End

    # Class Methods Begin
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

    @staticmethod
    def estimatecompress(in_: typing.List[int], currentPos: int, inlength: int) -> int:
        pass

    @staticmethod
    def compress(
        in_: typing.List[int],
        currentPos: int,
        inlength: int,
        out: typing.List[int],
        tmpoutpos: int,
    ) -> int:
        pass

    @staticmethod
    def __shiftme(x: typing.List[typing.List[int]]) -> typing.List[typing.List[int]]:
        pass

    @staticmethod
    def __fakecompressblock(in_: typing.List[int], inOffset: int, n: int) -> int:
        pass

    # Class Methods End
