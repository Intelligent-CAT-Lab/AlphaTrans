from __future__ import annotations

# Imports Begin
from src.main.me.lemire.integercompression.differential.IntegratedIntegerCODEC import *
from src.main.me.lemire.integercompression.IntWrapper import *
import os
import typing
from typing import *
import io

# Imports End


class IntegratedComposition(IntegratedIntegerCODEC):

    # Class Fields Begin
    F1: IntegratedIntegerCODEC = None
    F2: IntegratedIntegerCODEC = None
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

    def __init__(self, f1: IntegratedIntegerCODEC, f2: IntegratedIntegerCODEC) -> None:
        pass

    # Class Methods End
