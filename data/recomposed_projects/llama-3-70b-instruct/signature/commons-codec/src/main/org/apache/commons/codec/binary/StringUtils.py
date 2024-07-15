from __future__ import annotations
import time
import re
import io
import typing
from typing import *
from src.main.org.apache.commons.codec.binary.CharSequenceUtils import *


class StringUtils:

    @staticmethod
    def newStringUtf8(bytes: typing.List[int]) -> str:
        return StringUtils.__newString0(bytes, "UTF-8")

    @staticmethod
    def newStringUtf16Le(bytes: typing.List[int]) -> str:
        return StringUtils.__newString0(bytes, "UTF-16LE")

    @staticmethod
    def newStringUtf16Be(bytes: typing.List[int]) -> str:
        return StringUtils.__newString0(bytes, "UTF-16BE")

    @staticmethod
    def newStringUtf16(bytes: typing.List[int]) -> str:
        return StringUtils.__newString0(bytes, "UTF-16")

    @staticmethod
    def newStringUsAscii(bytes: typing.List[int]) -> str:
        return StringUtils.__newString0(bytes, "US-ASCII")

    @staticmethod
    def newStringIso8859_1(bytes: typing.List[int]) -> str:
        return StringUtils.__newString0(bytes, "ISO-8859-1")

    @staticmethod
    def newString1(bytes: typing.List[int], charsetName: str) -> str:
        if bytes is None:
            return None
        try:
            return str(bytes, charsetName)
        except LookupError as e:
            raise StringUtils.__newRuntimeError(charsetName, e)

    @staticmethod
    def getBytesUtf8(string: str) -> typing.List[int]:
        return StringUtils.__getBytes(string, "UTF-8")

    @staticmethod
    def getBytesUtf16Le(string: str) -> typing.List[int]:
        return StringUtils.__getBytes(string, "UTF-16LE")

    @staticmethod
    def getBytesUtf16Be(string: str) -> typing.List[int]:
        return StringUtils.__getBytes(string, "UTF-16BE")

    @staticmethod
    def getBytesUtf16(string: str) -> typing.List[int]:
        return StringUtils.__getBytes(string, "UTF-16")

    @staticmethod
    def getBytesUsAscii(string: str) -> typing.List[int]:
        return StringUtils.__getBytes(string, "US-ASCII")

    @staticmethod
    def getBytesUnchecked(string: str, charsetName: str) -> typing.List[int]:
        if string is None:
            return None
        try:
            return string.encode(charsetName)
        except UnicodeEncodeError as e:
            raise StringUtils.__newRuntimeError(charsetName, e)

    @staticmethod
    def getBytesIso8859_1(string: str) -> typing.List[int]:
        return StringUtils.__getBytes(string, "ISO-8859-1")

    @staticmethod
    def getByteBufferUtf8(string: str) -> typing.Union[bytearray, memoryview]:
        return StringUtils.__getByteBuffer(string, "UTF-8")

    @staticmethod
    def equals(cs1: str, cs2: str) -> bool:
        if cs1 == cs2:
            return True
        if cs1 is None or cs2 is None:
            return False
        if isinstance(cs1, str) and isinstance(cs2, str):
            return cs1 == cs2
        return len(cs1) == len(cs2) and CharSequenceUtils.regionMatches(
            cs1, False, 0, cs2, 0, len(cs1)
        )

    @staticmethod
    def __newString0(bytes: typing.List[int], charset: str) -> str:
        return bytes.decode(charset) if bytes is not None else None

    @staticmethod
    def __newRuntimeError(
        charsetName: str, e: typing.Union[UnicodeEncodeError, UnicodeDecodeError]
    ) -> RuntimeError:
        return RuntimeError(charsetName + ": " + str(e))

    @staticmethod
    def __getBytes(string: str, charset: str) -> typing.List[int]:
        if string is None:
            return None
        return string.encode(charset)

    @staticmethod
    def __getByteBuffer(
        string: str, charset: str
    ) -> typing.Union[bytearray, memoryview]:
        if string is None:
            return None
        return bytearray(string.encode(charset))
