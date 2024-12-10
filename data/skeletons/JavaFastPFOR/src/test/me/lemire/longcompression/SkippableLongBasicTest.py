from __future__ import annotations

# Imports Begin
from src.main.me.lemire.longcompression.SkippableLongCODEC import *
from src.main.me.lemire.longcompression.LongVariableByte import *
from src.test.me.lemire.longcompression.LongTestUtils import *
from src.main.me.lemire.longcompression.LongJustCopy import *
from src.main.me.lemire.integercompression.IntWrapper import *
import unittest
import os
import typing
from typing import *
import io

# Imports End


class SkippableLongBasicTest(unittest.TestCase):

    # Class Fields Begin
    codecs: typing.List[SkippableLongCODEC] = None
    # Class Fields End

    # Class Methods Begin
    def varyingLengthTest2_test0_decomposed(self) -> None:
        pass

    def varyingLengthTest_test0_decomposed(self) -> None:
        pass

    def consistentTest_test0_decomposed(self) -> None:
        pass

    # Class Methods End
