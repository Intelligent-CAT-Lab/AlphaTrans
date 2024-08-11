from __future__ import annotations

# Imports Begin
from src.main.me.lemire.longcompression.SkippableLongCODEC import *
from src.main.me.lemire.longcompression.LongVariableByte import *
from src.test.me.lemire.longcompression.LongTestUtils import *
from src.main.me.lemire.longcompression.LongCODEC import *
from src.main.me.lemire.longcompression.ByteLongCODEC import *
import unittest
import os
import typing
from typing import *
import io

# Imports End


class TestLongVariableByte(unittest.TestCase):

    # Class Fields Begin
    codec: LongVariableByte = None
    # Class Fields End

    # Class Methods Begin
    def testCodec_intermediateHighPowerOfTwo_test2_decomposed(self) -> None:
        pass

    def testCodec_intermediateHighPowerOfTwo_test1_decomposed(self) -> None:
        pass

    def testCodec_intermediateHighPowerOfTwo_test0_decomposed(self) -> None:
        pass

    def testCodec_ZeroThenAllPowerOfTwo_test0_decomposed(self) -> None:
        pass

    def testCodec_allPowerOfTwo_test0_decomposed(self) -> None:
        pass

    def testCodec_ZeroMinValue_test0_decomposed(self) -> None:
        pass

    def testCodec_MinValue_test0_decomposed(self) -> None:
        pass

    def testCodec_ZeroTimes128Minus1_test0_decomposed(self) -> None:
        pass

    def testCodec_ZeroTimes127Minus1_test0_decomposed(self) -> None:
        pass

    def testCodec_ZeroTimes8Minus1_test0_decomposed(self) -> None:
        pass

    def testCodec_ZeroMinus1_test0_decomposed(self) -> None:
        pass

    def __checkConsistency(self, codec: LongCODEC, array: typing.List[int]) -> None:
        pass

    # Class Methods End
