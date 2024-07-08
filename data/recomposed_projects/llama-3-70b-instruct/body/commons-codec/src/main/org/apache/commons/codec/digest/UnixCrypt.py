from __future__ import annotations
import re
import random
from abc import ABC
import io
import typing
from typing import *
from src.main.org.apache.commons.codec.digest.B64 import *


class UnixCrypt:

    __SPTRANS: typing.List[typing.List[int]] = (
        None  # LLM could not translate this field
    )

    __SKB: typing.List[typing.List[int]] = None  # LLM could not translate this field

    __SHIFT2: typing.List[bool] = [
        False,
        False,
        True,
        True,
        True,
        True,
        True,
        True,
        False,
        True,
        True,
        True,
        True,
        True,
        True,
        False,
    ]
    __SALT_CHARS: typing.List[str] = (
        "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789./"
    )
    __COV2CHAR: typing.List[int] = [
        46,
        47,
        48,
        49,
        50,
        51,
        52,
        53,
        54,
        55,
        56,
        57,
        65,
        66,
        67,
        68,
        69,
        70,
        71,
        72,
        73,
        74,
        75,
        76,
        77,
        78,
        79,
        80,
        81,
        82,
        83,
        84,
        85,
        86,
        87,
        88,
        89,
        90,
        97,
        98,
        99,
        100,
        101,
        102,
        103,
        104,
        105,
        106,
        107,
        108,
        109,
        110,
        111,
        112,
        113,
        114,
        115,
        116,
        117,
        118,
        119,
        120,
        121,
        122,
    ]
    __CON_SALT: typing.List[int] = [
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        1,
        2,
        3,
        4,
        5,
        6,
        7,
        8,
        9,
        10,
        11,
        5,
        6,
        7,
        8,
        9,
        10,
        11,
        12,
        13,
        14,
        15,
        16,
        17,
        18,
        19,
        20,
        21,
        22,
        23,
        24,
        25,
        26,
        27,
        28,
        29,
        30,
        31,
        32,
        33,
        34,
        35,
        36,
        37,
        32,
        33,
        34,
        35,
        36,
        37,
        38,
        39,
        40,
        41,
        42,
        43,
        44,
        45,
        46,
        47,
        48,
        49,
        50,
        51,
        52,
        53,
        54,
        55,
        56,
        57,
        58,
        59,
        60,
        61,
        62,
        63,
        0,
        0,
        0,
        0,
        0,
    ]

    @staticmethod
    def crypt3(original: str, salt: str) -> str:
        return UnixCrypt.crypt1(original.encode("utf-8"), salt)

    @staticmethod
    def crypt2(original: str) -> str:
        return UnixCrypt.crypt0(original.encode("utf-8"))

    @staticmethod
    def crypt1(original: typing.List[int], salt: str) -> str:
        if salt is None:
            randomGenerator = ThreadLocalRandom.current()
            numSaltChars = len(UnixCrypt.__SALT_CHARS)
            salt = (
                UnixCrypt.__SALT_CHARS[randomGenerator.nextInt(numSaltChars)]
                + UnixCrypt.__SALT_CHARS[randomGenerator.nextInt(numSaltChars)]
            )
        elif not salt.matches("^[" + B64.B64T_STRING + "]{2,}$"):
            raise ValueError("Invalid salt value: " + salt)

        buffer = StringBuilder("             ")
        charZero = salt.charAt(0)
        charOne = salt.charAt(1)
        buffer.setCharAt(0, charZero)
        buffer.setCharAt(1, charOne)
        eSwap0 = UnixCrypt.__CON_SALT[charZero]
        eSwap1 = UnixCrypt.__CON_SALT[charOne] << 4
        key = [0] * 8

        originalLength = len(original)
        for i in range(min(len(key), originalLength)):
            iChar = original[i]
            key[i] = iChar << 1

        schedule = UnixCrypt.__desSetKey(key)
        out = UnixCrypt.__body(schedule, eSwap0, eSwap1)
        b = [0] * 9
        UnixCrypt.__intToFourBytes(out[0], b, 0)
        UnixCrypt.__intToFourBytes(out[1], b, 4)
        b[8] = 0
        i = 2
        y = 0
        u = 128
        while i < 13:
            j = 0
            c = 0
            while j < 6:
                c <<= 1
                if (b[y] & u) != 0:
                    c |= 0x1
                u >>= 1
                if u == 0:
                    y += 1
                    u = 128
                buffer.setCharAt(i, chr(UnixCrypt.__COV2CHAR[c]))
                j += 1
            i += 1
        return buffer.toString()

    @staticmethod
    def crypt0(original: typing.List[int]) -> str:
        return UnixCrypt.crypt1(original, None)

    @staticmethod
    def __permOp(a: int, b: int, n: int, m: int, results: typing.List[int]) -> None:

        pass  # LLM could not translate this method

    @staticmethod
    def __intToFourBytes(iValue: int, b: typing.List[int], offset: int) -> None:

        pass  # LLM could not translate this method

    @staticmethod
    def __hPermOp(a: int, n: int, m: int) -> int:

        pass  # LLM could not translate this method

    @staticmethod
    def __fourBytesToInt(b: typing.List[int], offset: int) -> int:

        pass  # LLM could not translate this method

    @staticmethod
    def __desSetKey(key: typing.List[int]) -> typing.List[int]:

        pass  # LLM could not translate this method

    @staticmethod
    def __dEncrypt(
        el: int, r: int, s: int, e0: int, e1: int, sArr: typing.List[int]
    ) -> int:

        pass  # LLM could not translate this method

    @staticmethod
    def __byteToUnsigned(b: int) -> int:

        pass  # LLM could not translate this method

    @staticmethod
    def __body(
        schedule: typing.List[int], eSwap0: int, eSwap1: int
    ) -> typing.List[int]:

        pass  # LLM could not translate this method
