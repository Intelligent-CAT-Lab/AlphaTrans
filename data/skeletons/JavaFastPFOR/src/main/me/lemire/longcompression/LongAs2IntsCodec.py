from __future__ import annotations

# Imports Begin
from src.main.me.lemire.longcompression.RoaringIntPacking import *
from src.main.me.lemire.longcompression.LongCODEC import *
from src.main.me.lemire.integercompression.VariableByte import *
from src.main.me.lemire.integercompression.IntegerCODEC import *
from src.main.me.lemire.integercompression.IntWrapper import *
from src.main.me.lemire.integercompression.Composition import *
from src.main.me.lemire.integercompression.BinaryPacking import *
import os
import typing
from typing import *
import io

# Imports End


class LongAs2IntsCodec(LongCODEC):

    # Class Fields Begin
    highPartsCodec: IntegerCODEC = None
    lowPartsCodec: IntegerCODEC = None
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

    def compress0(
        self,
        in_: typing.List[int],
        inpos: IntWrapper,
        inlength: int,
        out: typing.List[int],
        outpos: IntWrapper,
    ) -> None:
        pass

    @staticmethod
    def LongAs2IntsCodec1() -> LongAs2IntsCodec:
        pass

    def __init__(
        self, highPartsCodec: IntegerCODEC, lowPartsCodec: IntegerCODEC
    ) -> None:
        pass

    # Class Methods End
