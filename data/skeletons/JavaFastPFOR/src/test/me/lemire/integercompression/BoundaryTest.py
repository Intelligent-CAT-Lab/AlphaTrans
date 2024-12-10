from __future__ import annotations

# Imports Begin
from src.main.me.lemire.integercompression.differential.IntegratedVariableByte import *
from src.main.me.lemire.integercompression.differential.IntegratedIntegerCODEC import *
from src.main.me.lemire.integercompression.differential.IntegratedComposition import *
from src.main.me.lemire.integercompression.differential.IntegratedBinaryPacking import *
from src.main.me.lemire.integercompression.VariableByte import *
from src.main.me.lemire.integercompression.IntegerCODEC import *
from src.main.me.lemire.integercompression.IntWrapper import *
from src.main.me.lemire.integercompression.Composition import *
from src.main.me.lemire.integercompression.BinaryPacking import *
import unittest
import os
import io

# Imports End


class BoundaryTest(unittest.TestCase):

    # Class Fields Begin
    # Class Fields End

    # Class Methods Begin
    def testComposition_test1_decomposed(self) -> None:
        pass

    def testComposition_test0_decomposed(self) -> None:
        pass

    def testIntegratedComposition_test1_decomposed(self) -> None:
        pass

    def testIntegratedComposition_test0_decomposed(self) -> None:
        pass

    @staticmethod
    def __testBoundary(c: IntegerCODEC) -> None:
        pass

    @staticmethod
    def __around256(c: IntegerCODEC) -> None:
        pass

    @staticmethod
    def __around128(c: IntegerCODEC) -> None:
        pass

    @staticmethod
    def __around32(c: IntegerCODEC) -> None:
        pass

    @staticmethod
    def __compressAndUncompress(length: int, c: IntegerCODEC) -> None:
        pass

    # Class Methods End
