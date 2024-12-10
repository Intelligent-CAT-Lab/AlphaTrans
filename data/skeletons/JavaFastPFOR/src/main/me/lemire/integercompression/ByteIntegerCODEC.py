from __future__ import annotations

# Imports Begin
from src.main.me.lemire.integercompression.IntWrapper import *
import os
import typing
from typing import *
import io
from abc import ABC

# Imports End


class ByteIntegerCODEC(ABC):

    # Class Fields Begin
    # Class Fields End

    # Class Methods Begin
    def uncompress1(
        self,
        in_: typing.List[int],
        inpos: IntWrapper,
        inlength: int,
        out: typing.List[int],
        outpos: IntWrapper,
    ) -> None:
        pass

    def compress1(
        self,
        in_: typing.List[int],
        inpos: IntWrapper,
        inlength: int,
        out: typing.List[int],
        outpos: IntWrapper,
    ) -> None:
        pass

    # Class Methods End
