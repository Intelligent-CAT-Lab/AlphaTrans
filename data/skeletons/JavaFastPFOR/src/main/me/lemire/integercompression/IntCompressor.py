from __future__ import annotations

# Imports Begin
from src.main.me.lemire.integercompression.VariableByte import *
from src.main.me.lemire.integercompression.UncompressibleInputException import *
from src.main.me.lemire.integercompression.SkippableIntegerCODEC import *
from src.main.me.lemire.integercompression.SkippableComposition import *
from src.main.me.lemire.integercompression.IntWrapper import *
from src.main.me.lemire.integercompression.BinaryPacking import *
import typing
from typing import *
import io

# Imports End


class IntCompressor:

    # Class Fields Begin
    codec: SkippableIntegerCODEC = None
    # Class Fields End

    # Class Methods Begin
    def uncompress(self, compressed: typing.List[int]) -> typing.List[int]:
        pass

    def compress(self, input_: typing.List[int]) -> typing.List[int]:
        pass

    def __init__(self, constructorId: int, c: SkippableIntegerCODEC) -> None:
        pass

    # Class Methods End
