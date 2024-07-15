from __future__ import annotations

# Imports Begin
from src.main.me.lemire.integercompression.differential.SkippableIntegratedIntegerCODEC import *
from src.main.me.lemire.integercompression.differential.SkippableIntegratedComposition import *
from src.main.me.lemire.integercompression.differential.IntegratedVariableByte import *
from src.main.me.lemire.integercompression.differential.IntegratedIntCompressor import *
from src.main.me.lemire.integercompression.differential.IntegratedBinaryPacking import *
from src.main.me.lemire.integercompression.VariableByte import *
from src.main.me.lemire.integercompression.SkippableIntegerCODEC import *
from src.main.me.lemire.integercompression.SkippableComposition import *
from src.main.me.lemire.integercompression.IntCompressor import *
from src.main.me.lemire.integercompression.BinaryPacking import *
import unittest
import typing
from typing import *
import io

# Imports End


class IntCompressorTest(unittest.TestCase):

    # Class Fields Begin
    iic: typing.List[IntegratedIntCompressor] = None
    ic: typing.List[IntCompressor] = None
    # Class Fields End

    # Class Methods Begin
    def basicIntegratedTest(self) -> None:
        pass

    def superSimpleExample(self) -> None:
        pass

    def basicTest(self) -> None:
        pass

    # Class Methods End
