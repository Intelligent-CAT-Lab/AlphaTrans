from __future__ import annotations

# Imports Begin
from src.main.me.lemire.integercompression.Util import *
from src.main.me.lemire.integercompression.SkippableIntegerCODEC import *
from src.main.me.lemire.integercompression.IntegerCODEC import *
from src.main.me.lemire.integercompression.IntWrapper import *
from src.main.me.lemire.integercompression.ByteIntegerCODEC import *
import unittest
import typing
from typing import *
import io

# Imports End


class TestUtils(unittest.TestCase):

    # Class Fields Begin
    # Class Fields End

    # Class Methods Begin
    def testPackingw(self) -> None:
        pass

    def testPacking(self) -> None:
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
    def _uncompress(
        codec: ByteIntegerCODEC, data: typing.List[int], len_: int
    ) -> typing.List[int]:
        pass

    @staticmethod
    def _compress(codec: ByteIntegerCODEC, data: typing.List[int]) -> typing.List[int]:
        pass

    @staticmethod
    def _uncompress(
        codec: IntegerCODEC, data: typing.List[int], len_: int
    ) -> typing.List[int]:
        pass

    @staticmethod
    def compress(codec: IntegerCODEC, data: typing.List[int]) -> typing.List[int]:
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

    @staticmethod
    def _uncompressHeadless() -> typing.List[int]:
        pass

    @staticmethod
    def _compressHeadless() -> typing.List[int]:
        pass

    @staticmethod
    def _uncompress() -> typing.List[int]:
        pass

    @staticmethod
    def _compress() -> typing.List[int]:
        pass

    @staticmethod
    def _uncompress() -> typing.List[int]:
        pass

    @staticmethod
    def compress() -> typing.List[int]:
        pass

    @staticmethod
    def assertSymmetry() -> None:
        pass

    @staticmethod
    def _dumpIntArrayAsHex() -> None:
        pass

    @staticmethod
    def _dumpIntArray() -> None:
        pass

    def testPackingw(self) -> None:
        pass

    def testPacking(self) -> None:
        pass

    # Class Methods End
