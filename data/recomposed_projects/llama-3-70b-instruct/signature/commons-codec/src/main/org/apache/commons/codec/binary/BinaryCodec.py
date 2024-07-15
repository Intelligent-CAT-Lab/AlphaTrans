from __future__ import annotations
import re
import io
import typing
from typing import *
from src.main.org.apache.commons.codec.BinaryDecoder import *
from src.main.org.apache.commons.codec.BinaryEncoder import *
from src.main.org.apache.commons.codec.DecoderException import *
from src.main.org.apache.commons.codec.EncoderException import *


class BinaryCodec(BinaryDecoder, BinaryEncoder):

    __BIT_7: int = 0x80
    __BIT_6: int = 0x40
    __BIT_5: int = 0x20
    __BIT_4: int = 0x10
    __BIT_3: int = 0x08
    __BIT_2: int = 0x04
    __BIT_1: int = 0x02
    __BIT_0: int = 1
    __EMPTY_BYTE_ARRAY: typing.List[int] = []
    __EMPTY_CHAR_ARRAY: typing.List[str] = []
    __BITS: typing.List[int] = [
        __BIT_0,
        __BIT_1,
        __BIT_2,
        __BIT_3,
        __BIT_4,
        __BIT_5,
        __BIT_6,
        __BIT_7,
    ]

    def toByteArray(self, ascii: str) -> typing.List[int]:
        if ascii is None:
            return self.__EMPTY_BYTE_ARRAY
        return self.fromAscii1(list(ascii))

    def encode1(self, raw: typing.Any) -> typing.Any:
        if not isinstance(raw, list):
            raise EncoderException("argument not a byte array", None)
        return self.toAsciiChars(raw)

    def encode0(self, raw: typing.List[int]) -> typing.List[int]:
        return self.toAsciiBytes(raw)

    def decode1(self, ascii: typing.Any) -> typing.Any:

        pass  # LLM could not translate this method

    def decode0(self, ascii: typing.List[int]) -> typing.List[int]:
        return self.fromAscii0(ascii)

    @staticmethod
    def toAsciiString(raw: typing.List[int]) -> str:
        return "".join([chr(x) for x in raw])

    @staticmethod
    def toAsciiChars(raw: typing.List[int]) -> typing.List[str]:
        if BinaryCodec.__isEmpty(raw):
            return BinaryCodec.__EMPTY_CHAR_ARRAY
        rawLength: int = len(raw)
        l_ascii: typing.List[str] = [""] * (rawLength << 3)
        jj: int = len(l_ascii) - 1
        for ii in range(0, rawLength):
            for bits in range(0, len(BinaryCodec.__BITS)):
                if (raw[ii] & BinaryCodec.__BITS[bits]) == 0:
                    l_ascii[jj - bits] = "0"
                else:
                    l_ascii[jj - bits] = "1"
            jj -= 8
        return l_ascii

    @staticmethod
    def toAsciiBytes(raw: typing.List[int]) -> typing.List[int]:
        if BinaryCodec.__isEmpty(raw):
            return BinaryCodec.__EMPTY_BYTE_ARRAY
        rawLength: int = len(raw)
        l_ascii: typing.List[int] = [0] * (rawLength << 3)
        for ii in range(0, rawLength):
            jj: int = l_ascii.length - 1 - (ii << 3)
            for bits in range(0, len(BinaryCodec.__BITS)):
                if (raw[ii] & BinaryCodec.__BITS[bits]) == 0:
                    l_ascii[jj - bits] = ord("0")
                else:
                    l_ascii[jj - bits] = ord("1")
        return l_ascii

    @staticmethod
    def fromAscii1(ascii: typing.List[str]) -> typing.List[int]:
        if ascii is None or len(ascii) == 0:
            return BinaryCodec.__EMPTY_BYTE_ARRAY
        asciiLength = len(ascii)
        l_raw = [0] * (asciiLength >> 3)
        for ii in range(0, len(l_raw)):
            jj = asciiLength - 1 - ii * 8
            for bits in range(0, len(BinaryCodec.__BITS)):
                if ascii[jj - bits] == "1":
                    l_raw[ii] |= BinaryCodec.__BITS[bits]
        return l_raw

    @staticmethod
    def fromAscii0(ascii: typing.List[int]) -> typing.List[int]:
        if BinaryCodec.__isEmpty(ascii):
            return BinaryCodec.__EMPTY_BYTE_ARRAY
        asciiLength = len(ascii)
        l_raw = [0] * (asciiLength >> 3)
        for ii in range(0, l_raw.length):
            jj = asciiLength - 1 - ii * 8
            for bits in range(0, len(BinaryCodec.__BITS)):
                if ascii[jj - bits] == "1":
                    l_raw[ii] |= BinaryCodec.__BITS[bits]
        return l_raw

    @staticmethod
    def __isEmpty(array: typing.List[int]) -> bool:
        return array is None or len(array) == 0
