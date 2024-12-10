from __future__ import annotations

# Imports Begin
from src.main.org.apache.commons.codec.EncoderException import *
from src.main.org.apache.commons.codec.DecoderException import *
from src.main.org.apache.commons.codec.CharEncoding import *
from src.main.org.apache.commons.codec.BinaryEncoder import *
from src.main.org.apache.commons.codec.BinaryDecoder import *
import typing
from typing import *
import io

# Imports End


class Hex(BinaryDecoder, BinaryEncoder):

    # Class Fields Begin
    __charset: str = None
    DEFAULT_CHARSET: str = None
    DEFAULT_CHARSET_NAME: str = None
    __DIGITS_LOWER: typing.List[str] = None
    __DIGITS_UPPER: typing.List[str] = None
    # Class Fields End

    # Class Methods Begin
    def toString(self) -> str:
        pass

    def encode(self, object_: typing.Any) -> typing.Any:
        pass

    def encode(self, array: typing.List[int]) -> typing.List[int]:
        pass

    def decode(self, object_: typing.Any) -> typing.Any:
        pass

    def decode(self, array: typing.List[int]) -> typing.List[int]:
        pass

    def getCharsetName(self) -> str:
        pass

    def getCharset(self) -> str:
        pass

    def encode2(self, object_: typing.Any) -> typing.Any:
        pass

    def encode1(self, array: typing.Union[bytearray, memoryview]) -> typing.List[int]:
        pass

    def encode(self, array: typing.Union[bytearray, memoryview]) -> typing.List[int]:
        pass

    def encode0(self, array: typing.List[int]) -> typing.List[int]:
        pass

    def decode2(self, object_: typing.Any) -> typing.Any:
        pass

    def decode1(self, buffer: typing.Union[bytearray, memoryview]) -> typing.List[int]:
        pass

    def decode(self, buffer: typing.Union[bytearray, memoryview]) -> typing.List[int]:
        pass

    def decode0(self, array: typing.List[int]) -> typing.List[int]:
        pass

    @staticmethod
    def Hex0(charsetName: str) -> Hex:
        pass

    def __init__(self, constructorId: int, charsetName: str, charset: str) -> None:
        pass

    @staticmethod
    def _toDigit(ch: str, index: int) -> int:
        pass

    @staticmethod
    def encodeHexString3(
        data: typing.Union[bytearray, memoryview], toLowerCase: bool
    ) -> str:
        pass

    @staticmethod
    def encodeHexString2(data: typing.Union[bytearray, memoryview]) -> str:
        pass

    @staticmethod
    def encodeHexString1(data: typing.List[int], toLowerCase: bool) -> str:
        pass

    @staticmethod
    def encodeHexString0(data: typing.List[int]) -> str:
        pass

    @staticmethod
    def _encodeHex8(
        byteBuffer: typing.Union[bytearray, memoryview], toDigits: typing.List[str]
    ) -> typing.List[str]:
        pass

    @staticmethod
    def encodeHex7(
        data: typing.Union[bytearray, memoryview], toLowerCase: bool
    ) -> typing.List[str]:
        pass

    @staticmethod
    def encodeHex6(data: typing.Union[bytearray, memoryview]) -> typing.List[str]:
        pass

    @staticmethod
    def encodeHex4(
        data: typing.List[int],
        dataOffset: int,
        dataLen: int,
        toLowerCase: bool,
        out: typing.List[str],
        outOffset: int,
    ) -> None:
        pass

    @staticmethod
    def encodeHex3(
        data: typing.List[int], dataOffset: int, dataLen: int, toLowerCase: bool
    ) -> typing.List[str]:
        pass

    @staticmethod
    def _encodeHex2(
        data: typing.List[int], toDigits: typing.List[str]
    ) -> typing.List[str]:
        pass

    @staticmethod
    def encodeHex1(data: typing.List[int], toLowerCase: bool) -> typing.List[str]:
        pass

    @staticmethod
    def encodeHex0(data: typing.List[int]) -> typing.List[str]:
        pass

    @staticmethod
    def decodeHex2(data: str) -> typing.List[int]:
        pass

    @staticmethod
    def decodeHex1(
        data: typing.List[str], out: typing.List[int], outOffset: int
    ) -> int:
        pass

    @staticmethod
    def decodeHex0(data: typing.List[str]) -> typing.List[int]:
        pass

    @staticmethod
    def __toByteArray(
        byteBuffer: typing.Union[bytearray, memoryview]
    ) -> typing.List[int]:
        pass

    @staticmethod
    def __encodeHex5(
        data: typing.List[int],
        dataOffset: int,
        dataLen: int,
        toDigits: typing.List[str],
        out: typing.List[str],
        outOffset: int,
    ) -> None:
        pass

    # Class Methods End
