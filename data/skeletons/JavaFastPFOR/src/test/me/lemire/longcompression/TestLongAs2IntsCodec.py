from __future__ import annotations

# Imports Begin
from src.main.me.lemire.longcompression.SkippableLongCODEC import *
from src.test.me.lemire.longcompression.LongTestUtils import *
from src.main.me.lemire.longcompression.LongCODEC import *
from src.main.me.lemire.longcompression.LongAs2IntsCodec import *
from src.main.me.lemire.longcompression.ByteLongCODEC import *
import unittest
import typing
from typing import *
import io

# Imports End


class TestLongAs2IntsCodec(unittest.TestCase):

    # Class Fields Begin
    codec: LongAs2IntsCodec = None
    # Class Fields End

    # Class Methods Begin
    def testCodec_intermediateHighPowerOfTwo(self) -> None:
        pass

    def testCodec_ZeroThenAllPowerOfTwo(self) -> None:
        pass

    def testCodec_allPowerOfTwo(self) -> None:
        pass

    def testCodec_ZeroMinValue(self) -> None:
        pass

    def testCodec_MinValue(self) -> None:
        pass

    def testCodec_ZeroTimes128Minus1(self) -> None:
        pass

    def testCodec_ZeroTimes127Minus1(self) -> None:
        pass

    def testCodec_ZeroTimes8Minus1(self) -> None:
        pass

    def testCodec_Minus1(self) -> None:
        pass

    def testCodec_Zero(self) -> None:
        pass

    def __checkConsistency(self, codec: LongCODEC, array: typing.List[int]) -> None:
        pass

    # Class Methods End
