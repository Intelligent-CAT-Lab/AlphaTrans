from __future__ import annotations
import re
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
    __charset: str = None

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

        return self.__charset

    def getCharset(self) -> str:

        return self.__charset

    def encode2(self, object: typing.Any) -> typing.Any:

        if isinstance(object, str):
            byteArray = object.encode(self.getCharset())
        elif isinstance(object, io.BytesIO):
            byteArray = self.__toByteArray(object.getbuffer())
        else:
            try:
                byteArray = typing.cast(bytearray, object)
            except ValueError as e:
                raise EncoderException(str(e))

        return self.encodeHex0(byteArray)

    def encode1(self, array: typing.Union[bytearray, memoryview]) -> typing.List[int]:

        # The encodeHexString2 method is not defined in the provided partial Python translation.
        # Assuming it returns a string, we can convert it to bytes using the getCharset method.
        # If the getCharset method is not defined, we can use a default encoding like 'utf-8'.

        try:
            return list(self.encodeHexString2(array).encode(self.getCharset()))
        except UnicodeEncodeError:
            return list(self.encodeHexString2(array).encode("utf-8"))

    def encode0(self, array: typing.List[int]) -> typing.List[int]:

        # Convert the byte array to a string using the charset
        byte_string = self.encodeHexString0(array)
        byte_array = byte_string.encode(self.getCharset())

        # Convert the byte array to a list of integers
        byte_list = list(byte_array)

        return byte_list

    def decode2(self, object: typing.Any) -> typing.Any:

        if isinstance(object, str):
            return self.decode2(list(object))
        elif isinstance(object, bytearray):
            return self.decode0(object)
        elif isinstance(object, memoryview):
            return self.decode1(object)
        else:
            try:
                return self.decodeHex0(list(object))
            except Exception as e:
                raise DecoderException(str(e))

    def decode1(self, buffer: typing.Union[bytearray, memoryview]) -> typing.List[int]:

        # Convert bytearray or memoryview to string using the charset
        str_data = str(self.__toByteArray(buffer), self.getCharset())

        # Convert string to list of characters
        char_list = list(str_data)

        # Use decodeHex0 method to decode the hexadecimal string
        return self.decodeHex0(char_list)

    def decode0(self, array: typing.List[int]) -> typing.List[int]:

        # Convert byte array to string
        str_array = "".join(map(chr, array))

        # Convert string to char array
        char_array = list(str_array)

        # Call decodeHex0 method
        return self.decodeHex0(char_array)

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

        digit = (
            int(ch, 16)
            if ch.isdigit()
            else ord(ch.lower()) - ord("a") + 10 if "a" <= ch.lower() <= "f" else -1
        )

        if digit == -1:
            raise DecoderException(
                "Illegal hexadecimal character " + ch + " at index " + str(index), None
            )
        return digit

    @staticmethod
    def encodeHexString3(
        data: typing.Union[bytearray, memoryview], toLowerCase: bool
    ) -> str:

        # Call the encodeHex7 method to get the hexadecimal representation
        hex_data = Hex.encodeHex7(data, toLowerCase)

        # Convert the list of hexadecimal strings to a single string
        hex_string = "".join(hex_data)

        return hex_string

    @staticmethod
    def encodeHexString2(data: typing.Union[bytearray, memoryview]) -> str:

        # Call the encodeHex6 method to get the hexadecimal representation
        hex_data = Hex.encodeHex6(data)

        # Convert the list of hexadecimal strings to a single string
        hex_string = "".join(hex_data)

        return hex_string

    @staticmethod
    def encodeHexString1(data: typing.List[int], toLowerCase: bool) -> str:

        hex_string = Hex.encodeHex1(data, toLowerCase)
        return "".join(hex_string)

    @staticmethod
    def encodeHexString0(data: typing.List[int]) -> str:

        # Call the encodeHex0 method to get the hexadecimal representation
        hex_data = Hex.encodeHex0(data)

        # Convert the list of hexadecimal characters to a string
        hex_string = "".join(hex_data)

        return hex_string

    @staticmethod
    def _encodeHex8(
        byteBuffer: typing.Union[bytearray, memoryview], toDigits: typing.List[str]
    ) -> typing.List[str]:

        # Convert byteBuffer to bytearray
        byteArray = bytearray(byteBuffer)

        # Call _encodeHex2 method
        return Hex._encodeHex2(byteArray, toDigits)

    @staticmethod
    def encodeHex7(
        data: typing.Union[bytearray, memoryview], toLowerCase: bool
    ) -> typing.List[str]:

        if toLowerCase:
            toDigits = Hex.__DIGITS_LOWER
        else:
            toDigits = Hex.__DIGITS_UPPER

        return Hex._encodeHex8(data, toDigits)

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

        out = [""] * (dataLen << 1)
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
    def __encodeHex5(
        data: typing.List[int],
        dataOffset: int,
        dataLen: int,
        toDigits: typing.List[str],
        out: typing.List[str],
        outOffset: int,
    ) -> None:
        for i in range(dataLen):
            out[outOffset + (i << 1)] = toDigits[(0xF0 & data[dataOffset + i]) >> 4]
            out[outOffset + (i << 1) + 1] = toDigits[0x0F & data[dataOffset + i]]

    @staticmethod
    def encodeHex1(data: typing.List[int], toLowerCase: bool) -> typing.List[str]:

        if toLowerCase:
            return Hex._encodeHex2(data, Hex.__DIGITS_LOWER)
        else:
            return Hex._encodeHex2(data, Hex.__DIGITS_UPPER)

    @staticmethod
    def encodeHex0(data: typing.List[int]) -> typing.List[str]:

        return Hex.encodeHex1(data, True)

    @staticmethod
    def decodeHex2(data: str) -> typing.List[int]:

        def decodeHex0(data: typing.List[str]) -> typing.List[int]:
            pass

        return decodeHex0(list(data))

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

        byteArray = byteBuffer[:remaining]
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
