from __future__ import annotations

# Imports Begin
from src.main.me.lemire.longcompression.SkippableLongCODEC import *
from src.main.me.lemire.integercompression.IntWrapper import *
import os
import typing
from typing import *
import io

# Imports End


class SkippableLongComposition(SkippableLongCODEC):

    # Class Fields Begin
    F1: SkippableLongCODEC = None
    F2: SkippableLongCODEC = None
    # Class Fields End

    # Class Methods Begin
    def toString(self) -> str:
        pass

    def headlessUncompress(
        self,
        in_: typing.List[int],
        inpos: IntWrapper,
        inlength: int,
        out: typing.List[int],
        outpos: IntWrapper,
        num: int,
    ) -> None:
        pass

    def headlessCompress(
        self,
        in_: typing.List[int],
        inpos: IntWrapper,
        inlength: int,
        out: typing.List[int],
        outpos: IntWrapper,
    ) -> None:
        pass

    def __init__(self, f1: SkippableLongCODEC, f2: SkippableLongCODEC) -> None:
        pass

    # Class Methods End
