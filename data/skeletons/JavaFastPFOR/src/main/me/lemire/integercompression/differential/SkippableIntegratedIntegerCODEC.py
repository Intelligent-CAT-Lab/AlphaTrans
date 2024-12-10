from __future__ import annotations

# Imports Begin
from src.main.me.lemire.integercompression.IntWrapper import *
import os
import typing
from typing import *
import io
from abc import ABC

# Imports End


class SkippableIntegratedIntegerCODEC(ABC):

    # Class Fields Begin
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

    # Class Methods End
