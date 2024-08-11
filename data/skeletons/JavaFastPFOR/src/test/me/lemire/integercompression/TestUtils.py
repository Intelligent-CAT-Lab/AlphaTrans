from __future__ import annotations

# Imports Begin
from src.main.me.lemire.integercompression.Util import *
from src.main.me.lemire.integercompression.SkippableIntegerCODEC import *
from src.main.me.lemire.integercompression.IntegerCODEC import *
from src.main.me.lemire.integercompression.IntWrapper import *
from src.main.me.lemire.integercompression.ByteIntegerCODEC import *
import unittest
import os
import typing
from typing import *
import io

# Imports End


class TestUtils(unittest.TestCase):

    # Class Fields Begin
    # Class Fields End

    # Class Methods Begin
    def testPackingw_test0_decomposed(self) -> None:
        pass

    def testPacking_test0_decomposed(self) -> None:
        pass

    @staticmethod
    def _uncompressHeadless(
        codec: SkippableIntegerCODEC, data: typing.List[int], len_: int
    ) -> typing.List[int]:
        pass

    @staticmethod
    def _compressHeadless(
        codec: SkippableIntegerCODEC, data: typing.List[int]
    ) -> typing.List[int]:
        pass

    @staticmethod
    def _uncompress1(
        codec: ByteIntegerCODEC, data: typing.List[int], len_: int
    ) -> typing.List[int]:
        pass

    @staticmethod
    def _compress0(codec: ByteIntegerCODEC, data: typing.List[int]) -> typing.List[int]:
        pass

    @staticmethod
    def _uncompress0(
        codec: IntegerCODEC, data: typing.List[int], len_: int
    ) -> typing.List[int]:
        pass

    @staticmethod
    def compress1(codec: IntegerCODEC, data: typing.List[int]) -> typing.List[int]:
        pass

    @staticmethod
    def assertSymmetry(codec: IntegerCODEC, orig: typing.List[int]) -> None:
        pass

    @staticmethod
    def _dumpIntArrayAsHex(data: typing.List[int], label: str) -> None:
        pass

    @staticmethod
    def _dumpIntArray(data: typing.List[int], label: str) -> None:
        pass

    # Class Methods End
