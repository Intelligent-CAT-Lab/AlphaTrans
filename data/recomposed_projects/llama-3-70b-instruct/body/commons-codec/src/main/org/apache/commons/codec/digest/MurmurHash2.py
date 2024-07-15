from __future__ import annotations
import re
import io
import typing
from typing import *
from src.main.org.apache.commons.codec.binary.StringUtils import *


class MurmurHash2:

    __R64: int = 47
    __M64: int = 0xC6A4A7935BD1E995
    __R32: int = 24
    __M32: int = 0x5BD1E995

    @staticmethod
    def hash643(text: str, from_: int, length: int) -> int:
        return MurmurHash2.hash642(text[from_ : from_ + length])

    @staticmethod
    def hash642(text: str) -> int:
        bytes: typing.List[int] = StringUtils.getBytesUtf8(text)
        return MurmurHash2.hash641(bytes, len(bytes))

    @staticmethod
    def hash641(data: typing.List[int], length: int) -> int:
        return MurmurHash2.hash640(data, length, 0xE17A1465)

    @staticmethod
    def hash640(data: typing.List[int], length: int, seed: int) -> int:
        h: int = (seed & 0xFFFFFFFF) ^ (length * MurmurHash2.__M64)

        nblocks: int = length >> 3

        for i in range(nblocks):
            index: int = i << 3
            k: int = MurmurHash2.__getLittleEndianLong(data, index)

            k *= MurmurHash2.__M64
            k ^= k >> MurmurHash2.__R64
            k *= MurmurHash2.__M64

            h ^= k
            h *= MurmurHash2.__M64

        index = nblocks << 3
        switch = length - index
        if switch == 7:
            h ^= (data[index + 6] & 0xFF) << 48
        if switch == 6:
            h ^= (data[index + 5] & 0xFF) << 40
        if switch == 5:
            h ^= (data[index + 4] & 0xFF) << 32
        if switch == 4:
            h ^= (data[index + 3] & 0xFF) << 24
        if switch == 3:
            h ^= (data[index + 2] & 0xFF) << 16
        if switch == 2:
            h ^= (data[index + 1] & 0xFF) << 8
        if switch == 1:
            h ^= data[index] & 0xFF
            h *= MurmurHash2.__M64

        h ^= h >> MurmurHash2.__R64
        h *= MurmurHash2.__M64
        h ^= h >> MurmurHash2.__R64

        return h

    @staticmethod
    def hash323(text: str, from_: int, length: int) -> int:
        return MurmurHash2.hash322(text[from_ : from_ + length])

    @staticmethod
    def hash322(text: str) -> int:
        bytes: typing.List[int] = StringUtils.getBytesUtf8(text)
        return MurmurHash2.hash321(bytes, len(bytes))

    @staticmethod
    def hash321(data: typing.List[int], length: int) -> int:
        return MurmurHash2.hash320(data, length, 0x9747B28C)

    @staticmethod
    def hash320(data: typing.List[int], length: int, seed: int) -> int:
        h: int = seed ^ length

        nblocks: int = length >> 2

        for i in range(0, nblocks):
            index: int = i << 2
            k: int = MurmurHash2.__getLittleEndianInt(data, index)
            k *= MurmurHash2.__M32
            k ^= k >> MurmurHash2.__R32
            k *= MurmurHash2.__M32
            h *= MurmurHash2.__M32
            h ^= k

        index = nblocks << 2
        switch = length - index
        if switch == 3:
            h ^= (data[index + 2] & 0xFF) << 16
        if switch == 2:
            h ^= (data[index + 1] & 0xFF) << 8
        if switch == 1:
            h ^= data[index] & 0xFF
            h *= MurmurHash2.__M32

        h ^= h >> 13
        h *= MurmurHash2.__M32
        h ^= h >> 15

        return h

    @staticmethod
    def __getLittleEndianLong(data: typing.List[int], index: int) -> int:
        return (
            ((data[index] & 0xFF))
            | ((data[index + 1] & 0xFF) << 8)
            | ((data[index + 2] & 0xFF) << 16)
            | ((data[index + 3] & 0xFF) << 24)
            | ((data[index + 4] & 0xFF) << 32)
            | ((data[index + 5] & 0xFF) << 40)
            | ((data[index + 6] & 0xFF) << 48)
            | ((data[index + 7] & 0xFF) << 56)
        )

    @staticmethod
    def __getLittleEndianInt(data: typing.List[int], index: int) -> int:

        pass  # LLM could not translate this method

    def __init__(self) -> None:
        pass
