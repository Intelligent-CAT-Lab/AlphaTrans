from __future__ import annotations

# Imports Begin
from src.main.org.apache.commons.codec.binary.CharSequenceUtils import *
import typing
from typing import *
import io

# Imports End


class StringUtils:

    # Class Fields Begin
    # Class Fields End

    # Class Methods Begin
    @staticmethod
    def newStringUtf8(bytes_: typing.List[int]) -> str:
        pass

    @staticmethod
    def newStringUtf16Le(bytes_: typing.List[int]) -> str:
        pass

    @staticmethod
    def newStringUtf16Be(bytes_: typing.List[int]) -> str:
        pass

    @staticmethod
    def newStringUtf16(bytes_: typing.List[int]) -> str:
        pass

    @staticmethod
    def newStringUsAscii(bytes_: typing.List[int]) -> str:
        pass

    @staticmethod
    def newStringIso8859_1(bytes_: typing.List[int]) -> str:
        pass

    @staticmethod
    def newString1(bytes_: typing.List[int], charsetName: str) -> str:
        pass

    @staticmethod
    def getBytesUtf8(string: str) -> typing.List[int]:
        pass

    @staticmethod
    def getBytesUtf16Le(string: str) -> typing.List[int]:
        pass

    @staticmethod
    def getBytesUtf16Be(string: str) -> typing.List[int]:
        pass

    @staticmethod
    def getBytesUtf16(string: str) -> typing.List[int]:
        pass

    @staticmethod
    def getBytesUsAscii(string: str) -> typing.List[int]:
        pass

    @staticmethod
    def getBytesUnchecked(string: str, charsetName: str) -> typing.List[int]:
        pass

    @staticmethod
    def getBytesIso8859_1(string: str) -> typing.List[int]:
        pass

    @staticmethod
    def getByteBufferUtf8(string: str) -> typing.Union[bytearray, memoryview]:
        pass

    @staticmethod
    def equals(cs1: str, cs2: str) -> bool:
        pass

    @staticmethod
    def __newString0(bytes_: typing.List[int], charset: str) -> str:
        pass

    @staticmethod
    def __newIllegalStateException(
        charsetName: str, e: typing.Union[UnicodeEncodeError, ValueError]
    ) -> RuntimeError:
        pass

    @staticmethod
    def __getBytes(string: str, charset: str) -> typing.List[int]:
        pass

    @staticmethod
    def __getByteBuffer(
        string: str, charset: str
    ) -> typing.Union[bytearray, memoryview]:
        pass

    # Class Methods End
