from __future__ import annotations
import re
import io
import typing
from typing import *


class PureJavaCrc32C:

    __T: typing.List[int] = None  # LLM could not translate this field

    __T8_7_start: int = None  # LLM could not translate this field

    __T8_6_start: int = None  # LLM could not translate this field

    __T8_5_start: int = None  # LLM could not translate this field

    __T8_4_start: int = None  # LLM could not translate this field

    __T8_3_start: int = None  # LLM could not translate this field

    __T8_2_start: int = None  # LLM could not translate this field

    __T8_1_start: int = None  # LLM could not translate this field

    __T8_0_start: int = None  # LLM could not translate this field

    __crc: int = 0

    def reset(self) -> None:
        self.__crc = 0xFFFFFFFF

    def getValue(self) -> int:
        ret = self.__crc
        return (~ret) & 0xFFFFFFFF

    def update1(self, b: int) -> None:

        pass  # LLM could not translate this method

    def update0(self, b: typing.List[int], off: int, len: int) -> None:

        pass  # LLM could not translate this method

    def __init__(self) -> None:
        self.reset()
