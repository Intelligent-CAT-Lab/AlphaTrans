from __future__ import annotations

# Imports Begin
import os
import typing
from typing import *
import numbers
import io

# Imports End


class Simple16WithHardCodes:

    # Class Fields Begin
    __S16_NUMSIZE: int = None
    __S16_BITSSIZE: int = None
    __S16_NUM: typing.List[int] = None
    __S16_BITS: typing.List[typing.List[int]] = None
    # Class Fields End

    # Class Methods Begin
    @staticmethod
    def _s16DecompressOneNumberWithHardCodesIntegrated(
        out: typing.List[int],
        outOffset: int,
        value: int,
        numIdx: int,
        oribits: int,
        expPos: typing.List[int],
    ) -> int:
        pass

    @staticmethod
    def _s16DecompressOneNumberWithHardCodes(
        out: typing.List[int], outOffset: int, value: int, numIdx: int
    ) -> int:
        pass

    @staticmethod
    def _s16DecompressWithIntBufferIntegratedBackup(
        out: typing.List[int],
        outOffset: int,
        value: int,
        n: int,
        expPos: typing.List[int],
        oribits: int,
    ) -> int:
        pass

    @staticmethod
    def _s16DecompressWithIntBufferIntegrated2(
        out: typing.List[int],
        outOffset: int,
        value: int,
        n: int,
        expPos: typing.List[int],
        oribits: int,
    ) -> int:
        pass

    @staticmethod
    def _s16DecompressWithIntBufferIntegrated(
        out: typing.List[int],
        outOffset: int,
        value: int,
        n: int,
        expPos: typing.List[int],
        oribits: int,
    ) -> int:
        pass

    @staticmethod
    def _s16DecompressWithIntBufferWithHardCodes(
        out: typing.List[int], outOffset: int, value: int, n: int
    ) -> int:
        pass

    @staticmethod
    def _s16DecompressWithIntBuffer(
        out: typing.List[int], outOffset: int, value: int, n: int
    ) -> int:
        pass

    @staticmethod
    def _s16DecompressWithIntBufferBackup(
        out: typing.List[int], outOffset: int, value: int, n: int
    ) -> int:
        pass

    @staticmethod
    def _s16Decompress(
        out: typing.List[int],
        outOffset: int,
        in_: typing.List[int],
        inOffset: int,
        n: int,
    ) -> int:
        pass

    @staticmethod
    def _s16CompressBackup(
        out: typing.List[int],
        outOffset: int,
        in_: typing.List[int],
        inOffset: int,
        n: int,
        blockSize: int,
        oriBlockSize: int,
        oriInputBlock: typing.List[int],
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
        oriBlockSize: int,
        oriInputBlock: typing.List[int],
    ) -> int:
        pass

    @staticmethod
    def __readBitsForS16(
        in_: typing.List[int], inIntOffset: int, inWithIntOffset: int, bits: int
    ) -> int:
        pass

    # Class Methods End
