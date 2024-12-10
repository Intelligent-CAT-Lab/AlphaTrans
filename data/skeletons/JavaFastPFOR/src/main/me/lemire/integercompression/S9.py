from __future__ import annotations

# Imports Begin
from src.main.me.lemire.integercompression.Util import *
import os
import typing
from typing import *
import io

# Imports End


class S9:

    # Class Fields Begin
    __bitLength: typing.List[int] = None
    __codeNum: typing.List[int] = None
    # Class Fields End

    # Class Methods Begin
    @staticmethod
    def uncompress(
        in_: typing.List[int],
        tmpinpos: int,
        inlength: int,
        out: typing.List[int],
        currentPos: int,
        outlength: int,
    ) -> None:
        pass

    @staticmethod
    def compress(
        in_: typing.List[int],
        currentPos: int,
        inlength: int,
        out: typing.List[int],
        tmpoutpos: int,
    ) -> int:
        pass

    @staticmethod
    def estimatecompress(in_: typing.List[int], currentPos: int, inlength: int) -> int:
        pass

    # Class Methods End
