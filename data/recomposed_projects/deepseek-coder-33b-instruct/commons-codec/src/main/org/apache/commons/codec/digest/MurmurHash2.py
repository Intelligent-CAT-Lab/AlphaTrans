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

        # Extract the substring from the text
        sub_text = text[from_ : from_ + length]

        # Call the hash642 method with the substring
        return MurmurHash2.hash642(sub_text)

    @staticmethod
    def hash642(text: str) -> int:

        # Convert the string to bytes using UTF-8 encoding
        bytes = StringUtils.getBytesUtf8(text)

        # Convert the bytes to a list of integers
        data = list(bytes)

        # Get the length of the data
        length = len(data)

        # Call the hash641 method
        return MurmurHash2.hash641(data, length)

    @staticmethod
    def hash641(data: typing.List[int], length: int) -> int:

        return MurmurHash2.hash640(data, length, 0xE17A1465)

    @staticmethod
    def hash640(data: typing.List[int], length: int, seed: int) -> int:

        pass  # LLM could not translate this method

    @staticmethod
    def hash323(text: str, from_: int, length: int) -> int:

        return MurmurHash2.hash322(text[from_ : from_ + length])

    @staticmethod
    def hash322(text: str) -> int:

        # Convert the string to bytes using UTF-8 encoding
        bytes = StringUtils.getBytesUtf8(text)

        # Convert the bytes to a list of integers
        data = list(bytes)

        # Call the hash321 method with the data and its length
        return MurmurHash2.hash321(data, len(data))

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
    def __getLittleEndianInt(data: typing.List[int], index: int) -> int:
        pass

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

        pass  # LLM could not translate this method
