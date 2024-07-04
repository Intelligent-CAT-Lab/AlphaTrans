from __future__ import annotations
import re
import decimal
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
        return super().__str__() + "[charsetName=" + self.__charset + "]"

    def getCharsetName(self) -> str:
        return self.__charset.name()

    def getCharset(self) -> str:
        return self.__charset

    def encode2(self, object: typing.Any) -> typing.Any:

        if isinstance(object, str):
            byteArray = object.encode(self.getCharset())
        elif isinstance(object, bytearray) or isinstance(object, memoryview):
            byteArray = self.__toByteArray(object)
        else:
            try:
                byteArray = object
            except Exception as e:
                raise EncoderException(str(e), e)
        return self.encodeHex0(byteArray)

    def encode1(self, array: typing.Union[bytearray, memoryview]) -> typing.List[int]:
        return list(bytes(self.encodeHexString2(array), self.getCharset()))

    def encode0(self, array: typing.List[int]) -> typing.List[int]:
        return list(bytes(self.encodeHexString0(array), self.getCharset()))

    def decode2(self, object: typing.Any) -> typing.Any:

        if isinstance(object, str):
            return self.decode2(list(object))
        elif isinstance(object, bytearray) or isinstance(object, memoryview):
            return self.decode1(object)
        elif isinstance(object, list):
            try:
                return self.decodeHex0(object)
            except Exception as e:
                raise DecoderException(str(e), e)
        else:
            raise DecoderException("Unsupported object type", None)

    def decode1(self, buffer: typing.Union[bytearray, memoryview]) -> typing.List[int]:

        return self.decodeHex0(
            list(self.__toByteArray(buffer).decode(self.getCharset()))
        )

    def decode0(self, array: typing.List[int]) -> typing.List[int]:
        return self.decodeHex0(list(bytes(array).decode(self.getCharset())))

    @staticmethod
    def Hex0(charsetName: str) -> Hex:
        return Hex(1, None, Charset.forName(charsetName))

    def __init__(self, constructorId: int, charsetName: str, charset: str) -> None:

        if constructorId == 1:
            self.__charset = charset
        else:
            self.__charset = self.DEFAULT_CHARSET

        self.DEFAULT_CHARSET_NAME = CharEncoding.UTF_8
        self.DEFAULT_CHARSET = StandardCharsets.UTF_8
        self.__DIGITS_UPPER = [
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
        self.__DIGITS_LOWER = [
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

    @staticmethod
    def _toDigit(ch: str, index: int) -> int:

        digit = int(ch, 16) if ch.isdigit() else -1
        if digit == -1:
            raise DecoderException(
                "Illegal hexadecimal character " + ch + " at index " + str(index), None
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

        toDigits = Hex.__DIGITS_LOWER if toLowerCase else Hex.__DIGITS_UPPER
        Hex.__encodeHex5(data, dataOffset, dataLen, toDigits, out, outOffset)

    @staticmethod
    def encodeHex3(
        data: typing.List[int], dataOffset: int, dataLen: int, toLowerCase: bool
    ) -> typing.List[str]:

        out: typing.List[str] = ["\0"] * (dataLen << 1)
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
        out = [""] * (dataLength << 1)
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

        len_data = len(data)

        if (len_data & 0x01) != 0:
            raise DecoderException("Odd number of characters.", None)

        outLen = len_data >> 1
        if len(out) - outOffset < outLen:
            raise DecoderException(
                "Output array is not large enough to accommodate decoded data.", None
            )

        for i in range(outOffset, outLen):
            f = Hex._toDigit(data[i * 2], i * 2) << 4
            f = f | Hex._toDigit(data[i * 2 + 1], i * 2 + 1)
            out[i] = f & 0xFF

        return outLen

    @staticmethod
    def decodeHex0(data: typing.List[str]) -> typing.List[int]:

        out = [0] * (len(data) >> 1)
        Hex.decodeHex1(data, out, 0)
        return out

    @staticmethod
    def __toByteArray(
        byteBuffer: typing.Union[bytearray, memoryview]
    ) -> typing.List[int]:

        remaining = len(byteBuffer)
        if isinstance(byteBuffer, bytearray):
            byteArray = byteBuffer
            if remaining == len(byteArray):
                return byteArray
        else:
            byteArray = list(byteBuffer)
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
            outOffset += 1
            out[outOffset] = toDigits[0x0F & data[i]]
            outOffset += 1
