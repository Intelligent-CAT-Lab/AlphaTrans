from __future__ import annotations

# Imports Begin
import typing
from typing import *
import io

# Imports End


class PureJavaCrc32:

    # Class Fields Begin
    __T: typing.List[int] = None
    __crc: int = None
    # Class Fields End

    # Class Methods Begin
    def update(self, b: int) -> None:
        pass

    def update(self, b: typing.List[int], offset: int, len_: int) -> None:
        pass

    def reset(self) -> None:
        pass

    def getValue(self) -> int:
        pass

    def update1(self, b: int) -> None:
        pass

    def update0(self, b: typing.List[int], offset: int, len_: int) -> None:
        pass

    def __init__(self) -> None:
        pass

    def ___reset(self) -> None:
        pass

    # Class Methods End
