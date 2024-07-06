from __future__ import annotations
import re
import random
from abc import ABC
import io
import typing
from typing import *


class B64:

    B64T_STRING: str = None
    B64T_ARRAY: typing.List[str] = None

    @staticmethod
    def initialize_fields() -> None:
        B64.B64T_STRING: str = (
            "./0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
        )

        B64.B64T_ARRAY: typing.List[str] = list(B64T_STRING)

    @staticmethod
    def getRandomSalt(num: int, random: random.Random) -> str:
        saltString = ""
        for i in range(1, num + 1):
            saltString += B64T_STRING[random.randint(0, len(B64T_STRING) - 1)]
        return saltString

    @staticmethod
    def b64from24bit(b2: int, b1: int, b0: int, outLen: int, buffer: str) -> None:
        w = ((b2 << 16) & 0x00FFFFFF) | ((b1 << 8) & 0x00FFFF) | (b0 & 0xFF)
        n = outLen
        while n > 0:
            buffer += B64T_ARRAY[w & 0x3F]
            w >>= 6
            n -= 1


B64.initialize_fields()
