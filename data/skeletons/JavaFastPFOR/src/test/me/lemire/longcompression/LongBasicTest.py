from __future__ import annotations

# Imports Begin
from src.main.me.lemire.longcompression.differential.LongDelta import *
from src.main.me.lemire.longcompression.LongVariableByte import *
from src.test.me.lemire.longcompression.LongTestUtils import *
from src.main.me.lemire.longcompression.LongJustCopy import *
from src.main.me.lemire.longcompression.LongCODEC import *
from src.main.me.lemire.longcompression.LongAs2IntsCodec import *
from src.main.me.lemire.longcompression.IntegratedLongCODEC import *
from src.main.me.lemire.integercompression.IntWrapper import *
from src.main.me.lemire.integercompression.FastPFOR128 import *
from src.main.me.lemire.integercompression.FastPFOR import *
import unittest
import os
import typing
from typing import *
import io

# Imports End


class LongBasicTest(unittest.TestCase):

    # Class Fields Begin
    codecs: typing.List[LongCODEC] = None
    # Class Fields End

    # Class Methods Begin
    def fastPfor128Test_test0_decomposed(self) -> None:
        pass

    def fastPforTest_test0_decomposed(self) -> None:
        pass

    def varyingLengthTest2_test0_decomposed(self) -> None:
        pass

    def varyingLengthTest_test0_decomposed(self) -> None:
        pass

    def saulTest_test0_decomposed(self) -> None:
        pass

    def testUnsorted(self, codec: LongCODEC) -> None:
        pass

    def __testUnsorted3(self, codec: LongCODEC) -> None:
        pass

    def __testUnsorted2(self, codec: LongCODEC) -> None:
        pass

    @staticmethod
    def __testCodec(
        c: LongCODEC, co: LongCODEC, data: typing.List[typing.List[int]], max_: int
    ) -> None:
        pass

    @staticmethod
    def __testZeroInZeroOut(c: LongCODEC) -> None:
        pass

    @staticmethod
    def __testSpurious(c: LongCODEC) -> None:
        pass

    # Class Methods End
