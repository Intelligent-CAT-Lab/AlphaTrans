from __future__ import annotations
import re
from dataclasses import field
import io
import typing
from typing import *


class PureJavaCrc32C:

    __T: typing.List[int] = None  # LLM could not translate this field

    __T8_7_start: int = 7 * 256

    __T8_6_start: int = 6 * 256

    __T8_5_start: int = 5 * 256

    __T8_4_start: int = 4 * 256

    __T8_3_start: int = 3 * 256

    __T8_2_start: int = 2 * 256

    __T8_1_start: int = 256

    __T8_0_start: int = 0 * 256
    __crc: int = None

    def reset(self) -> None:

        self.__crc = 0xFFFFFFFF

    def getValue(self) -> int:

        ret = self.__crc
        return (~ret) & 0xFFFFFFFF

    def update1(self, b: int) -> None:

        self.__crc = (self.__crc >> 8) ^ self.__T[
            self.__T8_0_start + ((self.__crc ^ b) & 0xFF)
        ]

    def update0(self, b: typing.List[int], off: int, len: int) -> None:

        pass  # LLM could not translate this method

    def __init__(self) -> None:

        self.reset()
