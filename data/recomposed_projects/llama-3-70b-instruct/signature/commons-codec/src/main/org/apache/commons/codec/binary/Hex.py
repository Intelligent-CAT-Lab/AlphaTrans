from __future__ import annotations
import re
import os
import decimal
from io import BytesIO
import io
import typing
from typing import *
from src.main.org.apache.commons.codec.BinaryDecoder import *
from src.main.org.apache.commons.codec.BinaryEncoder import *
from src.main.org.apache.commons.codec.CharEncoding import *
from src.main.org.apache.commons.codec.DecoderException import *
from src.main.org.apache.commons.codec.EncoderException import *


class Hex(BinaryDecoder, BinaryEncoder):

    DEFAULT_CHARSET_NAME: str = CharEncoding.UTF_8
    DEFAULT_CHARSET: str = "UTF-8"
    __charset: str = ""

    __DIGITS_UPPER: typing.List[str] = [
        "0",
        "1",
        "2",
        "3",
        "4",
        "5",
        "6",
        "7",
        "8",
        "9",
        "A",
        "B",
        "C",
        "D",
        "E",
        "F",
    ]
    __DIGITS_LOWER: typing.List[str] = [
        "0",
        "1",
        "2",
        "3",
        "4",
        "5",
        "6",
        "7",
        "8",
        "9",
        "a",
        "b",
        "c",
        "d",
        "e",
        "f",
    ]

    def toString(self) -> str:
        return super().toString() + "[charsetName=" + self.__charset + "]"

    def getCharsetName(self) -> str:
        return self.__charset.name()

    def getCharset(self) -> str:
        return self.__charset

    def encode2(self, object: typing.Any) -> typing.Any:
        byteArray: typing.List[int]
        if isinstance(object, str):
            byteArray = object.encode(self.getCharset())
        elif isinstance(object, io.BytesIO):
            byteArray = Hex.__toByteArray(object)
        else:
            try:
                byteArray = object
            except TypeError as e:
                raise EncoderException(e.args[0], e)
        return Hex.encodeHex0(byteArray)

    def encode1(self, array: typing.Union[bytearray, memoryview]) -> typing.List[int]:
        return Hex.encodeHexString2(array).encode(self.getCharset())

    def encode0(self, array: typing.List[int]) -> typing.List[int]:
        return Hex.encodeHexString0(array).getBytes(self.getCharset())

    def decode2(self, object: typing.Any) -> typing.Any:
        if isinstance(object, str):
            return self.decode2(list(object))
        if isinstance(object, list):
            return self.decode0(object)
        if isinstance(object, io.BytesIO):
            return self.decode1(object)
        try:
            return self.decodeHex0(object)
        except TypeError as e:
            raise DecoderException(e.args[0], e)

    def decode1(self, buffer: typing.Union[bytearray, memoryview]) -> typing.List[int]:
        return Hex.decodeHex0(
            str(Hex.__toByteArray(buffer), self.getCharset()).toCharArray()
        )

    def decode0(self, array: typing.List[int]) -> typing.List[int]:
        return self.decodeHex0(str(array, self.getCharset()).toCharArray())

    @staticmethod
    def Hex0(charsetName: str) -> Hex:
        return Hex(1, None, Charset.forName(charsetName))

    def __init__(self, constructorId: int, charsetName: str, charset: str) -> None:
        if constructorId == 1:
            self.__charset = charset
        else:
            self.__charset = DEFAULT_CHARSET

    @staticmethod
    def _toDigit(ch: str, index: int) -> int:
        digit = int(ch, 16)
        if digit == -1:
            raise DecoderException(
                "Illegal hexadecimal character " + ch + " at index " + index, None
            )
        return digit

    @staticmethod
    def encodeHexString3(
        data: typing.Union[bytearray, memoryview], toLowerCase: bool
    ) -> str:
        return "".join(Hex.encodeHex7(data, toLowerCase))

    @staticmethod
    def encodeHexString2(data: typing.Union[bytearray, memoryview]) -> str:
        return "".join(Hex.encodeHex6(data))

    @staticmethod
    def encodeHexString1(data: typing.List[int], toLowerCase: bool) -> str:
        return "".join(Hex.encodeHex1(data, toLowerCase))

    @staticmethod
    def encodeHexString0(data: typing.List[int]) -> str:
        return "".join(Hex.encodeHex0(data))

    @staticmethod
    def _encodeHex8(
        byteBuffer: typing.Union[bytearray, memoryview], toDigits: typing.List[str]
    ) -> typing.List[str]:
        return Hex._encodeHex2(Hex.__toByteArray(byteBuffer), toDigits)

    @staticmethod
    def encodeHex7(
        data: typing.Union[bytearray, memoryview], toLowerCase: bool
    ) -> typing.List[str]:
        return Hex._encodeHex8(
            data, Hex.__DIGITS_LOWER if toLowerCase else Hex.__DIGITS_UPPER
        )

    @staticmethod
    def encodeHex6(data: typing.Union[bytearray, memoryview]) -> typing.List[str]:
        return Hex.encodeHex7(data, True)

    @staticmethod
    def encodeHex4(
        data: typing.List[int],
        dataOffset: int,
        dataLen: int,
        toLowerCase: bool,
        out: typing.List[str],
        outOffset: int,
    ) -> None:
        Hex.__encodeHex5(
            data,
            dataOffset,
            dataLen,
            Hex.__DIGITS_LOWER if toLowerCase else Hex.__DIGITS_UPPER,
            out,
            outOffset,
        )

    @staticmethod
    def encodeHex3(
        data: typing.List[int], dataOffset: int, dataLen: int, toLowerCase: bool
    ) -> typing.List[str]:
        out: typing.List[str] = [None] * (dataLen << 1)
        Hex.__encodeHex5(
            data,
            dataOffset,
            dataLen,
            Hex.__DIGITS_LOWER if toLowerCase else Hex.__DIGITS_UPPER,
            out,
            0,
        )
        return out

    @staticmethod
    def _encodeHex2(
        data: typing.List[int], toDigits: typing.List[str]
    ) -> typing.List[str]:
        dataLength = len(data)
        out = [None] * (dataLength << 1)
        Hex.__encodeHex5(data, 0, dataLength, toDigits, out, 0)
        return out

    @staticmethod
    def encodeHex1(data: typing.List[int], toLowerCase: bool) -> typing.List[str]:
        return Hex._encodeHex2(
            data, Hex.__DIGITS_LOWER if toLowerCase else Hex.__DIGITS_UPPER
        )

    @staticmethod
    def encodeHex0(data: typing.List[int]) -> typing.List[str]:
        return Hex.encodeHex1(data, True)

    @staticmethod
    def decodeHex2(data: str) -> typing.List[int]:
        return Hex.decodeHex0(list(data))

    @staticmethod
    def decodeHex1(
        data: typing.List[str], out: typing.List[int], outOffset: int
    ) -> int:

        pass  # LLM could not translate this method

    @staticmethod
    def decodeHex0(data: typing.List[str]) -> typing.List[int]:
        out = [0] * (len(data) >> 1)
        decodeHex1(data, out, 0)
        return out

    @staticmethod
    def __toByteArray(
        byteBuffer: typing.Union[bytearray, memoryview]
    ) -> typing.List[int]:
        remaining = byteBuffer.remaining()
        if byteBuffer.hasArray():
            byteArray = byteBuffer.array()
            if remaining == len(byteArray):
                byteBuffer.position(remaining)
                return byteArray
        byteArray = [0] * remaining
        byteBuffer.get(byteArray)
        return byteArray

    @staticmethod
    def __encodeHex5(
        data: typing.List[int],
        dataOffset: int,
        dataLen: int,
        toDigits: typing.List[str],
        out: typing.List[str],
        outOffset: int,
    ) -> None:
        for i in range(dataOffset, dataOffset + dataLen):
            out[outOffset] = toDigits[(0xF0 & data[i]) >> 4]
            out[outOffset + 1] = toDigits[0x0F & data[i]]
            outOffset += 2
