from __future__ import annotations

# Imports Begin
import typing
from typing import *
import io

# Imports End


class RoaringIntPacking:

    # Class Fields Begin
    __TWO_64: int = None
    # Class Fields End

    # Class Methods Begin
    @staticmethod
    def toUnsignedString(l: int) -> str:
        pass

    @staticmethod
    def compareUnsigned(x: int, y: int) -> int:
        pass

    @staticmethod
    def unsignedComparator() -> typing.Callable[[int, int], int]:
        pass

    @staticmethod
    def highestHigh(signedLongs: bool) -> int:
        pass

    @staticmethod
    def pack(high: int, low: int) -> int:
        pass

    @staticmethod
    def low(id_: int) -> int:
        pass

    @staticmethod
    def high(id_: int) -> int:
        pass

    # Class Methods End
