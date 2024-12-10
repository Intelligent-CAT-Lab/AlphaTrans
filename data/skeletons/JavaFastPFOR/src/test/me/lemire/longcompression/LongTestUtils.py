from __future__ import annotations

# Imports Begin
from src.main.me.lemire.longcompression.SkippableLongCODEC import *
from src.main.me.lemire.longcompression.LongCODEC import *
from src.main.me.lemire.longcompression.ByteLongCODEC import *
from src.main.me.lemire.integercompression.IntWrapper import *
import typing
from typing import *
import io

# Imports End


class LongTestUtils:

    # Class Fields Begin
    # Class Fields End

    # Class Methods Begin
    @staticmethod
    def longToBinaryWithLeading(l: int) -> str:
        pass

    @staticmethod
    def _uncompressHeadless(
        codec: SkippableLongCODEC, data: typing.List[int], len_: int
    ) -> typing.List[int]:
        pass

    @staticmethod
    def _compressHeadless(
        codec: SkippableLongCODEC, data: typing.List[int]
    ) -> typing.List[int]:
        pass

    @staticmethod
    def _uncompress1(
        codec: ByteLongCODEC, data: typing.List[int], len_: int
    ) -> typing.List[int]:
        pass

    @staticmethod
    def _compress0(codec: ByteLongCODEC, data: typing.List[int]) -> typing.List[int]:
        pass

    @staticmethod
    def _uncompress0(
        codec: LongCODEC, data: typing.List[int], len_: int
    ) -> typing.List[int]:
        pass

    @staticmethod
    def _compress1(codec: LongCODEC, data: typing.List[int]) -> typing.List[int]:
        pass

    @staticmethod
    def assertSymmetry(codec: LongCODEC, orig: typing.List[int]) -> None:
        pass

    @staticmethod
    def _dumpIntArrayAsHex(data: typing.List[int], label: str) -> None:
        pass

    @staticmethod
    def _dumpIntArray(data: typing.List[int], label: str) -> None:
        pass

    # Class Methods End
