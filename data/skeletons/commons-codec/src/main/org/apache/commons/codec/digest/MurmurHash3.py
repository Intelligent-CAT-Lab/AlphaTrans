from __future__ import annotations

# Imports Begin
from src.main.org.apache.commons.codec.binary.StringUtils import *
import typing
from typing import *
import io

# Imports End


class IncrementalHash32x86:

    # Class Fields Begin
    __unprocessedLength: int = None
    __totalLen: int = None
    __hash: int = None
    __BLOCK_SIZE: int = None
    __unprocessed: typing.List[int] = None
    # Class Fields End

    # Class Methods Begin
    def end(self) -> int:
        pass

    def add(self, data: typing.List[int], offset: int, length: int) -> None:
        pass

    def start(self, seed: int) -> None:
        pass

    @staticmethod
    def __orBytes(b1: int, b2: int, b3: int, b4: int) -> int:
        pass

    def finalise(
        self,
        hash_: int,
        unprocessedLength: int,
        unprocessed: typing.List[int],
        totalLen: int,
    ) -> int:
        pass

    # Class Methods End


class IncrementalHash32(IncrementalHash32x86):

    # Class Fields Begin
    # Class Fields End

    # Class Methods Begin
    def finalise(
        self,
        hash_: int,
        unprocessedLength: int,
        unprocessed: typing.List[int],
        totalLen: int,
    ) -> int:
        pass

    # Class Methods End


class MurmurHash3:

    # Class Fields Begin
    NULL_HASHCODE: int = None
    DEFAULT_SEED: int = None
    LONG_BYTES: int = None
    INTEGER_BYTES: int = None
    SHORT_BYTES: int = None
    __C1_32: int = None
    __C2_32: int = None
    __R1_32: int = None
    __R2_32: int = None
    __M_32: int = None
    __N_32: int = None
    __C1: int = None
    __C2: int = None
    __R1: int = None
    __R2: int = None
    __R3: int = None
    __M: int = None
    __N1: int = None
    __N2: int = None
    # Class Fields End

    # Class Methods Begin
    @staticmethod
    def hash1282(
        data: typing.List[int], offset: int, length: int, seed: int
    ) -> typing.List[int]:
        pass

    @staticmethod
    def hash1281(data: str) -> typing.List[int]:
        pass

    @staticmethod
    def hash645(data: typing.List[int], offset: int, length: int, seed: int) -> int:
        pass

    @staticmethod
    def hash644(data: typing.List[int], offset: int, length: int) -> int:
        pass

    @staticmethod
    def hash643(data: typing.List[int]) -> int:
        pass

    @staticmethod
    def hash642(data: int) -> int:
        pass

    @staticmethod
    def hash641(data: int) -> int:
        pass

    @staticmethod
    def hash640(data: int) -> int:
        pass

    @staticmethod
    def hash328(data: typing.List[int], offset: int, length: int, seed: int) -> int:
        pass

    @staticmethod
    def hash327(data: typing.List[int], length: int, seed: int) -> int:
        pass

    @staticmethod
    def hash326(data: typing.List[int], length: int) -> int:
        pass

    @staticmethod
    def hash325(data: str) -> int:
        pass

    @staticmethod
    def hash324(data: typing.List[int]) -> int:
        pass

    @staticmethod
    def hash128x641(
        data: typing.List[int], offset: int, length: int, seed: int
    ) -> typing.List[int]:
        pass

    @staticmethod
    def hash128x640(data: typing.List[int]) -> typing.List[int]:
        pass

    @staticmethod
    def hash1280(data: typing.List[int]) -> typing.List[int]:
        pass

    @staticmethod
    def hash32x861(data: typing.List[int], offset: int, length: int, seed: int) -> int:
        pass

    @staticmethod
    def hash32x860(data: typing.List[int]) -> int:
        pass

    @staticmethod
    def hash323(data: int, seed: int) -> int:
        pass

    @staticmethod
    def hash322(data: int) -> int:
        pass

    @staticmethod
    def hash321(data1: int, data2: int, seed: int) -> int:
        pass

    @staticmethod
    def hash320(data1: int, data2: int) -> int:
        pass

    @staticmethod
    def __fmix64(hash_: int) -> int:
        pass

    @staticmethod
    def __fmix32(hash_: int) -> int:
        pass

    @staticmethod
    def __mix32(k: int, hash_: int) -> int:
        pass

    @staticmethod
    def __getLittleEndianInt(data: typing.List[int], index: int) -> int:
        pass

    @staticmethod
    def __getLittleEndianLong(data: typing.List[int], index: int) -> int:
        pass

    @staticmethod
    def __hash128x64Internal(
        data: typing.List[int], offset: int, length: int, seed: int
    ) -> typing.List[int]:
        pass

    def __init__(self) -> None:
        pass

    # Class Methods End
