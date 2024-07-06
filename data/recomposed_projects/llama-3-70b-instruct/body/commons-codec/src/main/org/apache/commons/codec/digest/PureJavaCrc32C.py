from __future__ import annotations
import re
import io
import typing
from typing import *


class PureJavaCrc32C:

    __T8_0_start: int = None  # LLM could not translate this field

    __crc: int = 0

    def reset(self) -> None:
        self.__crc = 0xFFFFFFFF

    def getValue(self) -> int:

        pass  # LLM could not translate this method

    def update1(self, b: int) -> None:

        pass  # LLM could not translate this method

    def update0(self, b: typing.List[int], off: int, len: int) -> None:

        pass  # LLM could not translate this method

    def __init__(self) -> None:
        self.reset()
