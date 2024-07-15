from __future__ import annotations
import re
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

        pass  # LLM could not translate this method

    @staticmethod
    def crypt0(original: typing.List[int]) -> str:
        return UnixCrypt.crypt1(original, None)

    @staticmethod
    def __permOp(a: int, b: int, n: int, m: int, results: typing.List[int]) -> None:
        t = (a >> n ^ b) & m
        a ^= t << n
        b ^= t
        results[0] = a
        results[1] = b

    @staticmethod
    def __intToFourBytes(iValue: int, b: typing.List[int], offset: int) -> None:
        b[offset] = iValue & 0xFF
        b[offset + 1] = iValue >> 8 & 0xFF
        b[offset + 2] = iValue >> 16 & 0xFF
        b[offset + 3] = iValue >> 24 & 0xFF

    @staticmethod
    def __hPermOp(a: int, n: int, m: int) -> int:
        t = (a << 16 - n ^ a) & m
        a = a ^ t ^ t >> 16 - n
        return a

    @staticmethod
    def __fourBytesToInt(b: typing.List[int], offset: int) -> int:
        value = UnixCrypt.__byteToUnsigned(b[offset])
        offset += 1
        value |= UnixCrypt.__byteToUnsigned(b[offset]) << 8
        offset += 1
        value |= UnixCrypt.__byteToUnsigned(b[offset]) << 16
        offset += 1
        value |= UnixCrypt.__byteToUnsigned(b[offset]) << 24
        offset += 1
        return value

    @staticmethod
    def __desSetKey(key: typing.List[int]) -> typing.List[int]:

        pass  # LLM could not translate this method

    @staticmethod
    def __dEncrypt(
        el: int, r: int, s: int, e0: int, e1: int, sArr: typing.List[int]
    ) -> int:
        v: int = r ^ r >> 16
        u: int = v & e0
        v &= e1
        u = u ^ u << 16 ^ r ^ sArr[s]
        t: int = v ^ v << 16 ^ r ^ sArr[s + 1]
        t = t >> 4 | t << 28
        el ^= (
            UnixCrypt.__SPTRANS[1][t & 0x3F]
            | UnixCrypt.__SPTRANS[3][t >> 8 & 0x3F]
            | UnixCrypt.__SPTRANS[5][t >> 16 & 0x3F]
            | UnixCrypt.__SPTRANS[7][t >> 24 & 0x3F]
            | UnixCrypt.__SPTRANS[0][u & 0x3F]
            | UnixCrypt.__SPTRANS[2][u >> 8 & 0x3F]
            | UnixCrypt.__SPTRANS[4][u >> 16 & 0x3F]
            | UnixCrypt.__SPTRANS[6][u >> 24 & 0x3F]
        )
        return el

    @staticmethod
    def __byteToUnsigned(b: int) -> int:
        value = b
        return value + 256 if value < 0 else value

    @staticmethod
    def __body(
        schedule: typing.List[int], eSwap0: int, eSwap1: int
    ) -> typing.List[int]:
        left = 0
        right = 0
        t = 0
        for j in range(0, 25):
            for i in range(0, 32, 4):
                left = UnixCrypt.__dEncrypt(left, right, i, eSwap0, eSwap1, schedule)
                right = UnixCrypt.__dEncrypt(
                    right, left, i + 2, eSwap0, eSwap1, schedule
                )
            t = left
            left = right
            right = t
        t = right
        right = left >> 1 | left << 31
        left = t >> 1 | t << 31
        results = [0] * 2
        UnixCrypt.__permOp(right, left, 1, 0x55555555, results)
        right = results[0]
        left = results[1]
        UnixCrypt.__permOp(left, right, 8, 0xFF00FF, results)
        left = results[0]
        right = results[1]
        UnixCrypt.__permOp(right, left, 2, 0x33333333, results)
        right = results[0]
        left = results[1]
        UnixCrypt.__permOp(left, right, 16, 65535, results)
        left = results[0]
        right = results[1]
        UnixCrypt.__permOp(right, left, 4, 0xF0F0F0F, results)
        right = results[0]
        left = results[1]
        out = [0] * 2
        out[0] = left
        out[1] = right
        return out
