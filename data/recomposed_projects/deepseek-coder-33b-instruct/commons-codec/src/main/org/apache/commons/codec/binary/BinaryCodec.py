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
    __BITS: List[int] = [
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

        # The Java method 'toAsciiBytes' is not defined in the provided partial Python translation.
        # Assuming that 'toAsciiBytes' is a method that converts a list of integers to a list of ASCII bytes,
        # we can use the built-in 'chr' function in Python to convert each integer to a character,
        # and then encode the character to bytes using 'encode' method.

        return [ord(chr(i)) for i in raw]

    def decode1(self, ascii: typing.Any) -> typing.Any:

        if ascii is None:
            return self.__EMPTY_BYTE_ARRAY
        if isinstance(ascii, list):
            return self.fromAscii0(ascii)
        if isinstance(ascii, str):
            return self.fromAscii1(list(ascii))
        if isinstance(ascii, tuple):
            return self.fromAscii1(list(ascii))
        raise DecoderException("argument not a byte array", None)

    def decode0(self, ascii: typing.List[int]) -> typing.List[int]:

        return self.fromAscii0(ascii)

    @staticmethod
    def toAsciiString(raw: typing.List[int]) -> str:

        # Convert each byte to its corresponding ASCII character
        ascii_chars = [chr(b) for b in raw]

        # Join the ASCII characters into a single string
        ascii_string = "".join(ascii_chars)

        return ascii_string

    @staticmethod
    def toAsciiChars(raw: typing.List[int]) -> typing.List[str]:

        if BinaryCodec.__isEmpty(raw):
            return BinaryCodec.__EMPTY_CHAR_ARRAY

        rawLength = len(raw)
        l_ascii = [""] * (rawLength << 3)

        for ii, jj in enumerate(range(len(l_ascii) - 1, -1, -1)):
            for bits in range(len(BinaryCodec.__BITS)):
                if (raw[ii] & BinaryCodec.__BITS[bits]) == 0:
                    l_ascii[jj - bits] = "0"
                else:
                    l_ascii[jj - bits] = "1"

        return l_ascii

    @staticmethod
    def toAsciiBytes(raw: typing.List[int]) -> typing.List[int]:

        if BinaryCodec.__isEmpty(raw):
            return BinaryCodec.__EMPTY_BYTE_ARRAY

        rawLength = len(raw)
        l_ascii = [0] * (rawLength << 3)

        for ii, jj in enumerate(range(len(l_ascii) - 1, -1, -1)):
            for bits in range(len(BinaryCodec.__BITS)):
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

        for ii, jj in enumerate(range(asciiLength - 1, -1, -1)):
            for bits in range(len(BinaryCodec.__BITS)):
                if ascii[jj - bits] == "1":
                    l_raw[ii] |= BinaryCodec.__BITS[bits]

        return l_raw

    @staticmethod
    def fromAscii0(ascii: typing.List[int]) -> typing.List[int]:

        if BinaryCodec.__isEmpty(ascii):
            return BinaryCodec.__EMPTY_BYTE_ARRAY

        asciiLength = len(ascii)
        l_raw = [0] * (asciiLength >> 3)

        for ii, jj in enumerate(range(asciiLength - 1, -1, -8)):
            for bits in range(len(BinaryCodec.__BITS)):
                if ascii[jj - bits] == ord("1"):
                    l_raw[ii] |= BinaryCodec.__BITS[bits]

        return l_raw

    @staticmethod
    def __isEmpty(array: typing.List[int]) -> bool:

        return array is None or len(array) == 0
