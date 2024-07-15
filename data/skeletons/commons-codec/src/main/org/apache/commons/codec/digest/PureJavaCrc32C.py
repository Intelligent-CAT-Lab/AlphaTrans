from __future__ import annotations

# Imports Begin
import typing
from typing import *
import io

# Imports End


class PureJavaCrc32C:

    # Class Fields Begin
    __T8_0_start: int = None
    __T8_1_start: int = None
    __T8_2_start: int = None
    __T8_3_start: int = None
    __T8_4_start: int = None
    __T8_5_start: int = None
    __T8_6_start: int = None
    __T8_7_start: int = None
    __T: typing.List[int] = None
    __crc: int = None
    # Class Fields End

    # Class Methods Begin
    def update(self, b: int) -> None:
        pass

    def update(self, b: typing.List[int], off: int, len_: int) -> None:
        pass

    def reset(self) -> None:
        pass

    def getValue(self) -> int:
        pass

    def update1(self, b: int) -> None:
        pass

    def update0(self, b: typing.List[int], off: int, len_: int) -> None:
        pass

    def __init__(self) -> None:
        pass

    # Class Methods End
