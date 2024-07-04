from __future__ import annotations
import re
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
        return super().__str__() + "[charsetName=" + self.__charset + "]"

    def getCharsetName(self) -> str:
        return self.__charset

    def getCharset(self) -> str:
        return self.__charset

    def encode2(self, object: typing.Any) -> typing.Any:

        byteArray = None
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
            return self.decode0(list(object))
        elif isinstance(object, io.BytesIO):
            return self.decode1(object.getbuffer())
        else:
            try:
                return self.decodeHex0(list(object))
            except Exception as e:
                raise DecoderException(str(e), e)

    def decode1(self, buffer: typing.Union[bytearray, memoryview]) -> typing.List[int]:

        # Convert bytearray or memoryview to bytes
        byte_array = bytes(buffer)

        # Get the charset
        charset = self.getCharset()

        # Decode the byte array to a string using the charset
        decoded_string = byte_array.decode(charset)

        # Convert the string to a list of characters
        char_list = list(decoded_string)

        # Decode the hexadecimal string
        return self.decodeHex0(char_list)

    def decode0(self, array: typing.List[int]) -> typing.List[int]:

        # Convert the byte array to a string using the charset
        str_data = bytes(array).decode(self.getCharset())

        # Convert the string to a list of characters
        char_data = list(str_data)

        # Call the decodeHex0 method with the list of characters
        return self.decodeHex0(char_data)

    @staticmethod
    def Hex0(charsetName: str) -> Hex:
        return Hex(1, None, charsetName)

    def __init__(self, constructorId: int, charsetName: str, charset: str) -> None:

        if constructorId == 1:
            self.__charset = charset
        else:
            self.__charset = self.DEFAULT_CHARSET

    @staticmethod
    def _toDigit(ch: str, index: int) -> int:

        digit = int(ch, 16)
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

        hex_chars = Hex.encodeHex1(data, toLowerCase)
        return "".join(hex_chars)

    @staticmethod
    def encodeHexString0(data: typing.List[int]) -> str:

        hex_chars = [
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
        encoded_data = Hex.encodeHex0(data)
        hex_string = "".join(hex_chars[b] for b in encoded_data)
        return hex_string

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

        out = ["0"] * (dataLen << 1)
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
        out = ["\0"] * (dataLength << 1)
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

        for i in range(outOffset, len(out)):
            j = (i - outOffset) * 2
            f = Hex._toDigit(data[j], j) << 4
            f = f | Hex._toDigit(data[j + 1], j + 1)
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
        if isinstance(byteBuffer, memoryview):
            byteArray = byteBuffer.tobytes()
            if remaining == len(byteArray):
                return byteArray
        else:
            byteArray = byteBuffer

        return list(byteArray)

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
