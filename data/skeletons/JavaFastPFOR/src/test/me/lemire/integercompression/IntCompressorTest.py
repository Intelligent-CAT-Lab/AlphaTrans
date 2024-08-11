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
import os
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
    def basicIntegratedTest_test0_decomposed(self) -> None:
        pass

    def superSimpleExample_test3_decomposed(self) -> None:
        pass

    def superSimpleExample_test2_decomposed(self) -> None:
        pass

    def superSimpleExample_test1_decomposed(self) -> None:
        pass

    def superSimpleExample_test0_decomposed(self) -> None:
        pass

    def basicTest_test0_decomposed(self) -> None:
        pass

    # Class Methods End
