from __future__ import annotations

# Imports Begin
from src.main.org.apache.commons.codec.digest.B64 import *
import typing
from typing import *
import io

# Imports End


class UnixCrypt:

    # Class Fields Begin
    __SPTRANS: typing.List[typing.List[int]] = None
    __CON_SALT: typing.List[int] = None
    __COV2CHAR: typing.List[int] = None
    __SALT_CHARS: typing.List[str] = None
    __SHIFT2: typing.List[bool] = None
    __SKB: typing.List[typing.List[int]] = None
    # Class Fields End

    # Class Methods Begin
    @staticmethod
    def crypt3(original: str, salt: str) -> str:
        pass

    @staticmethod
    def crypt2(original: str) -> str:
        pass

    @staticmethod
    def crypt1(original: typing.List[int], salt: str) -> str:
        pass

    @staticmethod
    def crypt0(original: typing.List[int]) -> str:
        pass

    @staticmethod
    def __permOp(a: int, b: int, n: int, m: int, results: typing.List[int]) -> None:
        pass

    @staticmethod
    def __intToFourBytes(iValue: int, b: typing.List[int], offset: int) -> None:
        pass

    @staticmethod
    def __hPermOp(a: int, n: int, m: int) -> int:
        pass

    @staticmethod
    def __fourBytesToInt(b: typing.List[int], offset: int) -> int:
        pass

    @staticmethod
    def __desSetKey(key: typing.List[int]) -> typing.List[int]:
        pass

    @staticmethod
    def __dEncrypt(
        el: int, r: int, s: int, e0: int, e1: int, sArr: typing.List[int]
    ) -> int:
        pass

    @staticmethod
    def __byteToUnsigned(b: int) -> int:
        pass

    @staticmethod
    def __body(
        schedule: typing.List[int], eSwap0: int, eSwap1: int
    ) -> typing.List[int]:
        pass

    # Class Methods End
