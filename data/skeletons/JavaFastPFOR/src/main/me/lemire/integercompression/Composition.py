from __future__ import annotations

# Imports Begin
from src.main.me.lemire.integercompression.IntegerCODEC import *
from src.main.me.lemire.integercompression.IntWrapper import *
import os
import typing
from typing import *
import io

# Imports End


class Composition(IntegerCODEC):

    # Class Fields Begin
    F1: IntegerCODEC = None
    F2: IntegerCODEC = None
    # Class Fields End

    # Class Methods Begin
    def toString(self) -> str:
        pass

    def uncompress0(
        self,
        in_: typing.List[int],
        inpos: IntWrapper,
        inlength: int,
        out: typing.List[int],
        outpos: IntWrapper,
    ) -> None:
        pass

    def compress0(
        self,
        in_: typing.List[int],
        inpos: IntWrapper,
        inlength: int,
        out: typing.List[int],
        outpos: IntWrapper,
    ) -> None:
        pass

    def __init__(self, f1: IntegerCODEC, f2: IntegerCODEC) -> None:
        pass

    # Class Methods End
