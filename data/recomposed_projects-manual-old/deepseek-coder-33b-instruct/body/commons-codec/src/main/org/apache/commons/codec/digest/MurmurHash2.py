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

        substring = text[from_ : from_ + length]
        return MurmurHash2.hash642(substring)

    @staticmethod
    def hash642(text: str) -> int:

        bytes = StringUtils.getBytesUtf8(text)
        return MurmurHash2.hash641(bytes, len(bytes))

    @staticmethod
    def hash641(data: typing.List[int], length: int) -> int:
        return MurmurHash2.hash640(data, length, 0xE17A1465)

    @staticmethod
    def hash640(data: typing.List[int], length: int, seed: int) -> int:

        h = (seed & 0xFFFFFFFF) ^ (length * MurmurHash2.__M64)

        nblocks = length >> 3

        for i in range(nblocks):
            index = i << 3
            k = MurmurHash2.__getLittleEndianLong(data, index)

            k *= MurmurHash2.__M64
            k ^= k >> MurmurHash2.__R64
            k *= MurmurHash2.__M64

            h ^= k
            h *= MurmurHash2.__M64

        index = nblocks << 3
        switch_case = length - index
        if switch_case >= 1:
            h ^= (data[index + 6] & 0xFF) << 48
        if switch_case >= 2:
            h ^= (data[index + 5] & 0xFF) << 40
        if switch_case >= 3:
            h ^= (data[index + 4] & 0xFF) << 32
        if switch_case >= 4:
            h ^= (data[index + 3] & 0xFF) << 24
        if switch_case >= 5:
            h ^= (data[index + 2] & 0xFF) << 16
        if switch_case >= 6:
            h ^= (data[index + 1] & 0xFF) << 8
        if switch_case >= 7:
            h ^= data[index] & 0xFF
            h *= MurmurHash2.__M64

        h ^= h >> MurmurHash2.__R64
        h *= MurmurHash2.__M64
        h ^= h >> MurmurHash2.__R64

        return h

    @staticmethod
    def hash323(text: str, from_: int, length: int) -> int:

        substring = text[from_ : from_ + length]
        return MurmurHash2.hash322(substring)

    @staticmethod
    def hash322(text: str) -> int:

        bytes = StringUtils.getBytesUtf8(text)
        return MurmurHash2.hash321(bytes, len(bytes))

    @staticmethod
    def hash321(data: typing.List[int], length: int) -> int:

        return MurmurHash2.hash320(data, length, 0x9747B28C)

    @staticmethod
    def hash320(data: typing.List[int], length: int, seed: int) -> int:

        h = seed ^ length

        nblocks = length >> 2

        for i in range(nblocks):
            index = i << 2
            k = MurmurHash2.__getLittleEndianInt(data, index)
            k *= MurmurHash2.__M32
            k ^= k >> MurmurHash2.__R32
            k *= MurmurHash2.__M32
            h *= MurmurHash2.__M32
            h ^= k

        index = nblocks << 2
        match length - index:
            case 3:
                h ^= (data[index + 2] & 0xFF) << 16
            case 2:
                h ^= (data[index + 1] & 0xFF) << 8
            case 1:
                h ^= data[index] & 0xFF
                h *= MurmurHash2.__M32

        h ^= h >> 13
        h *= MurmurHash2.__M32
        h ^= h >> 15

        return h

    @staticmethod
    def __getLittleEndianLong(data: typing.List[int], index: int) -> int:

        return (
            (data[index] & 0xFF)
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
        return (
            (data[index] & 0xFF)
            | ((data[index + 1] & 0xFF) << 8)
            | ((data[index + 2] & 0xFF) << 16)
            | ((data[index + 3] & 0xFF) << 24)
        )

    def __init__(self) -> None:
        pass
