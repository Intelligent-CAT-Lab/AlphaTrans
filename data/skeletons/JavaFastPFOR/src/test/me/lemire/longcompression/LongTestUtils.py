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
    def _uncompress(
        codec: ByteLongCODEC, data: typing.List[int], len_: int
    ) -> typing.List[int]:
        pass

    @staticmethod
    def _compress(codec: ByteLongCODEC, data: typing.List[int]) -> typing.List[int]:
        pass

    @staticmethod
    def _uncompress(
        codec: LongCODEC, data: typing.List[int], len_: int
    ) -> typing.List[int]:
        pass

    @staticmethod
    def _compress(codec: LongCODEC, data: typing.List[int]) -> typing.List[int]:
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

    @staticmethod
    def longToBinaryWithLeading() -> str:
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
    def _compress() -> typing.List[int]:
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

    # Class Methods End
