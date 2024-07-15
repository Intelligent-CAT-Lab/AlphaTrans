from __future__ import annotations

# Imports Begin
from src.main.me.lemire.integercompression.Util import *
from src.main.me.lemire.integercompression.SkippableIntegerCODEC import *
from src.main.me.lemire.integercompression.IntegerCODEC import *
from src.main.me.lemire.integercompression.IntWrapper import *
from src.main.me.lemire.integercompression.BitPacking import *
import os
import typing
from typing import *
import io

# Imports End


class FastPFOR128(IntegerCODEC, SkippableIntegerCODEC):

    # Class Fields Begin
    OVERHEAD_OF_EACH_EXCEPT: int = None
    DEFAULT_PAGE_SIZE: int = None
    BLOCK_SIZE: int = None
    pageSize: int = None
    dataTobePacked: typing.List[typing.List[int]] = None
    byteContainer: typing.Union[bytearray, memoryview] = None
    dataPointers: typing.List[int] = None
    freqs: typing.List[int] = None
    bestbbestcexceptmaxb: typing.List[int] = None
    # Class Fields End

    # Class Methods Begin
    def toString(self) -> str:
        pass

    def uncompress(
        self,
        in_: typing.List[int],
        inpos: IntWrapper,
        inlength: int,
        out: typing.List[int],
        outpos: IntWrapper,
    ) -> None:
        pass

    def compress(
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
        mynvalue: int,
    ) -> None:
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

    def _makeBuffer(self, sizeInBytes: int) -> typing.Union[bytearray, memoryview]:
        pass

    @staticmethod
    def FastPFOR1281() -> FastPFOR128:
        pass

    def __init__(self, pagesize: int) -> None:
        pass

    def __decodePage(
        self,
        in_: typing.List[int],
        inpos: IntWrapper,
        out: typing.List[int],
        outpos: IntWrapper,
        thissize: int,
    ) -> None:
        pass

    def __encodePage(
        self,
        in_: typing.List[int],
        inpos: IntWrapper,
        thissize: int,
        out: typing.List[int],
        outpos: IntWrapper,
    ) -> None:
        pass

    def __getBestBFromData(self, in_: typing.List[int], pos: int) -> None:
        pass

    def _makeBuffer(self) -> typing.Union[bytearray, memoryview]:
        pass

    def toString(self) -> str:
        pass

    def uncompress(self) -> None:
        pass

    def compress(self) -> None:
        pass

    def headlessUncompress(self) -> None:
        pass

    def headlessCompress(self) -> None:
        pass

    @staticmethod
    def FastPFOR1281() -> FastPFOR128:
        pass

    def __init__(self) -> None:
        pass

    def __decodePage(self) -> None:
        pass

    def __encodePage(self) -> None:
        pass

    def __getBestBFromData(self) -> None:
        pass

    # Class Methods End
