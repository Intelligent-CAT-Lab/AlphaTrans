from __future__ import annotations

# Imports Begin
import typing
from typing import *
import io
from io import StringIO

# Imports End


class B64:

    # Class Fields Begin
    B64T_STRING: str = None
    B64T_ARRAY: typing.List[str] = None
    # Class Fields End

    # Class Methods Begin
    @staticmethod
    def getRandomSalt(num: int, random: random.Random) -> str:
        pass

    @staticmethod
    def b64from24bit(
        b2: int,
        b1: int,
        b0: int,
        outLen: int,
        buffer: typing.Union[typing.List[str], io.StringIO],
    ) -> None:
        pass

    # Class Methods End
