from __future__ import annotations

# Imports Begin
from src.main.com.kamikaze.pfordelta.Simple16 import *
from src.main.com.kamikaze.pfordelta.PForDeltaUnpack128 import *
import typing
from typing import *
import numbers
import io

# Imports End


class PForDelta:

    # Class Fields Begin
    __POSSIBLE_B: typing.List[int] = None
    __MAX_BITS: int = None
    __HEADER_NUM: int = None
    __HEADER_SIZE: int = None
    __MASK: typing.List[int] = None
    # Class Fields End

    # Class Methods Begin
    @staticmethod
    def readBits(in_: typing.List[int], inOffset: int, bits: int) -> int:
        pass

    @staticmethod
    def decompressBBitSlotsWithHardCodes(
        decompressedSlots: typing.List[int],
        compBlock: typing.List[int],
        blockSize: int,
        bits: int,
    ) -> int:
        pass

    @staticmethod
    def writeBits(out: typing.List[int], val: int, outOffset: int, bits: int) -> None:
        pass

    @staticmethod
    def decompressBlockByS16(
        outDecompBlock: typing.List[int],
        inCompBlock: typing.List[int],
        inStartOffsetInBits: int,
        blockSize: int,
    ) -> int:
        pass

    @staticmethod
    def decompressBBitSlots(
        outDecompSlots: typing.List[int],
        inCompBlock: typing.List[int],
        blockSize: int,
        bits: int,
    ) -> int:
        pass

    @staticmethod
    def compressOneBlock(
        inputBlock: typing.List[int], bits: int, blockSize: int
    ) -> typing.List[int]:
        pass

    @staticmethod
    def checkBigNumbers(
        inputBlock: typing.List[int], bits: int, blockSize: int
    ) -> bool:
        pass

    @staticmethod
    def estimateCompressedSize(
        inputBlock: typing.List[int], bits: int, blockSize: int
    ) -> int:
        pass

    @staticmethod
    def decompressOneBlock(
        outBlock: typing.List[int], inBlock: typing.List[int], blockSize: int
    ) -> int:
        pass

    @staticmethod
    def compressOneBlockOpt(
        inBlock: typing.List[int], blockSize: int
    ) -> typing.List[int]:
        pass

    @staticmethod
    def __compressBlockByS16(
        outCompBlock: typing.List[int],
        outStartOffsetInBits: int,
        inBlock: typing.List[int],
        blockSize: int,
    ) -> int:
        pass

    # Class Methods End
