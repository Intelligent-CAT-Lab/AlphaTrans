from __future__ import annotations

# Imports Begin
from src.main.me.lemire.integercompression.differential.SkippableIntegratedIntegerCODEC import *
from src.main.me.lemire.integercompression.differential.SkippableIntegratedComposition import *
from src.main.me.lemire.integercompression.differential.IntegratedVariableByte import *
from src.main.me.lemire.integercompression.differential.IntegratedBinaryPacking import *
from src.main.me.lemire.integercompression.UncompressibleInputException import *
from src.main.me.lemire.integercompression.IntWrapper import *
import typing
from typing import *
import io

# Imports End


class IntegratedIntCompressor:

    # Class Fields Begin
    codec: SkippableIntegratedIntegerCODEC = None
    # Class Fields End

    # Class Methods Begin
    def uncompress(self, compressed: typing.List[int]) -> typing.List[int]:
        pass

    def compress(self, input_: typing.List[int]) -> typing.List[int]:
        pass

    def __init__(self, constructorId: int, c: SkippableIntegratedIntegerCODEC) -> None:
        pass

    # Class Methods End
