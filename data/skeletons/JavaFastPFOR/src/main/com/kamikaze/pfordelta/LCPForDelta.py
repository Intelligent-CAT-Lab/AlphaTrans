from __future__ import annotations

# Imports Begin
from src.main.com.kamikaze.pfordelta.Simple16WithHardCodes import *
from src.main.com.kamikaze.pfordelta.Simple16 import *
from src.main.com.kamikaze.pfordelta.PForDeltaUnpack128WIthIntBuffer import *
from src.main.com.kamikaze.pfordelta.PForDeltaUnpack128 import *
import os
import typing
from typing import *
import numbers
import io

# Imports End


class LCPForDelta:

    # Class Fields Begin
    __POSSIBLE_B: typing.List[int] = None
    __POSSIBLE_B_BITS: int = None
    __MAX_BITS: int = None
    __HEADER_NUM: int = None
    __HEADER_SIZE: int = None
    __MASK: typing.List[int] = None
    __compBuffer: typing.List[int] = None
    # Class Fields End

    # Class Methods Begin
    @staticmethod
    def _readBitsWithBuffer(in_: typing.List[int], inOffset: int, bits: int) -> int:
        pass

    @staticmethod
    def readBits(in_: typing.List[int], inOffset: int, bits: int) -> int:
        pass

    @staticmethod
    def writeBits(out: typing.List[int], val: int, outOffset: int, bits: int) -> None:
        pass

    @staticmethod
    def _decompressBlockByS16WithIntBufferIntegrated(
        outDecompBlock: typing.List[int],
        inCompBlock: typing.Union[array.array, typing.List[int]],
        blockSize: int,
        expPosBuffer: typing.List[int],
        oribits: int,
    ) -> None:
        pass

    @staticmethod
    def _decompressBlockByS16WithIntBuffer(
        outDecompBlock: typing.List[int],
        inCompBlock: typing.Union[array.array, typing.List[int]],
        blockSize: int,
    ) -> None:
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
    def _decompressBBitSlotsWithHardCodesWithIntBuffer(
        outDecompSlots: typing.List[int],
        inCompBlock: typing.Union[array.array, typing.List[int]],
        blockSize: int,
        bits: int,
    ) -> int:
        pass

    @staticmethod
    def _decompressBBitSlotsWithHardCodes(
        outDecompSlots: typing.List[int],
        inCompBlock: typing.List[int],
        blockSize: int,
        bits: int,
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
    def checkBigNumbers(
        inputBlock: typing.List[int], blockSize: int, bits: int
    ) -> bool:
        pass

    @staticmethod
    def estimateCompressedSize(
        inputBlock: typing.List[int], blockSize: int, bits: int
    ) -> int:
        pass

    @staticmethod
    def _decompressOneBlockWithSizeWithIntBuffer(
        decompBlock: typing.List[int],
        inBlock: typing.Union[array.array, typing.List[int]],
        blockSize: int,
        expPosBuffer: typing.List[int],
        expHighBitsBuffer: typing.List[int],
        inBlockLen: int,
    ) -> None:
        pass

    @staticmethod
    def _decompressOneBlockWithSize(
        decompBlock: typing.List[int],
        inBlock: typing.List[int],
        blockSize: int,
        expPosBuffer: typing.List[int],
        expHighBitsBuffer: typing.List[int],
        inBlockLen: int,
    ) -> None:
        pass

    @staticmethod
    def decompressOneBlock(
        decompBlock: typing.List[int], inBlock: typing.List[int], blockSize: int
    ) -> None:
        pass

    def _compressOneBlockCore2(
        self, inputBlock: typing.List[int], blockSize: int, bits: int
    ) -> int:
        pass

    def compressOneBlockCore(
        self, inputBlock: typing.List[int], blockSize: int, bits: int
    ) -> int:
        pass

    def compress(self, inBlock: typing.List[int], blockSize: int) -> int:
        pass

    def _setCompBuffer(self, buffer: typing.List[int]) -> None:
        pass

    def _getCompBuffer(self) -> typing.List[int]:
        pass

    @staticmethod
    def __compressBlockByS16(
        outCompBlock: typing.List[int],
        outStartOffsetInBits: int,
        inBlock: typing.List[int],
        blockSize: int,
        oriBlockSize: int,
        oriInputBlock: typing.List[int],
    ) -> int:
        pass

    # Class Methods End
