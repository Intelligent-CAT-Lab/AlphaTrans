from __future__ import annotations

# Imports Begin
from src.main.me.lemire.integercompression.differential.SkippableIntegratedIntegerCODEC import *
from src.main.me.lemire.integercompression.IntWrapper import *
import os
import typing
from typing import *
import io

# Imports End


class SkippableIntegratedComposition(SkippableIntegratedIntegerCODEC):

    # Class Fields Begin
    F1: SkippableIntegratedIntegerCODEC = None
    F2: SkippableIntegratedIntegerCODEC = None
    # Class Fields End

    # Class Methods Begin
    def headlessUncompress(
        self,
        in_: typing.List[int],
        inpos: IntWrapper,
        inlength: int,
        out: typing.List[int],
        outpos: IntWrapper,
        num: int,
        initvalue: IntWrapper,
    ) -> None:
        pass

    def headlessCompress(
        self,
        in_: typing.List[int],
        inpos: IntWrapper,
        inlength: int,
        out: typing.List[int],
        outpos: IntWrapper,
        initvalue: IntWrapper,
    ) -> None:
        pass

    def toString(self) -> str:
        pass

    def __init__(
        self, f1: SkippableIntegratedIntegerCODEC, f2: SkippableIntegratedIntegerCODEC
    ) -> None:
        pass

    # Class Methods End
