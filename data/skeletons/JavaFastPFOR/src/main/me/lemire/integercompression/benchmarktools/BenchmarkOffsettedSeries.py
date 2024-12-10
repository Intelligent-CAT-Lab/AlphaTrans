from __future__ import annotations

# Imports Begin
from src.main.me.lemire.integercompression.differential.XorBinaryPacking import *
from src.main.me.lemire.integercompression.differential.IntegratedBinaryPacking import *
from src.main.me.lemire.integercompression.benchmarktools.PerformanceLogger import *
from src.main.me.lemire.integercompression.JustCopy import *
from src.main.me.lemire.integercompression.IntegerCODEC import *
from src.main.me.lemire.integercompression.IntWrapper import *
from src.main.me.lemire.integercompression.FastPFOR128 import *
from src.main.me.lemire.integercompression.FastPFOR import *
from src.main.me.lemire.integercompression.DeltaZigzagVariableByte import *
from src.main.me.lemire.integercompression.DeltaZigzagBinaryPacking import *
from src.main.me.lemire.integercompression.BinaryPacking import *
import typing
from typing import *
import io
from io import StringIO

# Imports End


class BenchmarkOffsettedSeries:

    # Class Fields Begin
    __DEFAULT_MEAN: int = None
    __DEFAULT_RANGE: int = None
    __DEFAULT_REPEAT: int = None
    __DEFAULT_WARMUP: int = None
    # Class Fields End

    # Class Methods Begin
    @staticmethod
    def main(args: typing.List[typing.List[str]]) -> None:
        pass

    @staticmethod
    def run(
        csvWriter: typing.Union[io.TextIOWrapper, io.StringIO], count: int, length: int
    ) -> None:
        pass

    @staticmethod
    def __sortDataChunks(
        src: typing.List[typing.List[int]],
    ) -> typing.List[typing.List[int]]:
        pass

    @staticmethod
    def __deltaDataChunks(
        src: typing.List[typing.List[int]],
    ) -> typing.List[typing.List[int]]:
        pass

    @staticmethod
    def __generateDataChunks(
        seed: int, count: int, length: int, mean: int, range_: int
    ) -> typing.List[typing.List[int]]:
        pass

    @staticmethod
    def __generateSineDataChunks(
        seed: int, count: int, length: int, mean: int, range_: int, freq: int
    ) -> typing.List[typing.List[int]]:
        pass

    @staticmethod
    def __getMaxLen(data: typing.List[typing.List[int]]) -> int:
        pass

    @staticmethod
    def __decompress(
        logger: PerformanceLogger,
        codec: IntegerCODEC,
        src: typing.List[int],
        srcLen: int,
        dst: typing.List[int],
    ) -> int:
        pass

    @staticmethod
    def __compress(
        logger: PerformanceLogger,
        codec: IntegerCODEC,
        src: typing.List[int],
        dst: typing.List[int],
    ) -> int:
        pass

    @staticmethod
    def __checkArray(
        expected: typing.List[int],
        actualArray: typing.List[int],
        actualLen: int,
        codec: IntegerCODEC,
    ) -> None:
        pass

    @staticmethod
    def __benchmark2(
        csvWriter: typing.Union[io.TextIOWrapper, io.StringIO],
        dataName: str,
        codecName: str,
        codec: IntegerCODEC,
        data: typing.List[typing.List[int]],
        repeat: int,
    ) -> None:
        pass

    @staticmethod
    def __benchmark1(
        csvWriter: typing.Union[io.TextIOWrapper, io.StringIO],
        dataName: str,
        codecs: typing.List[IntegerCODEC],
        data: typing.List[typing.List[int]],
        repeat: int,
        warmup: int,
    ) -> None:
        pass

    @staticmethod
    def __benchmark0(
        csvWriter: typing.Union[io.TextIOWrapper, io.StringIO],
        codecs: typing.List[IntegerCODEC],
        count: int,
        length: int,
        mean: int,
        range_: int,
    ) -> None:
        pass

    @staticmethod
    def __benchmarkSine(
        csvWriter: typing.Union[io.TextIOWrapper, io.StringIO],
        codecs: typing.List[IntegerCODEC],
        count: int,
        length: int,
        mean: int,
        range_: int,
        freq: int,
    ) -> None:
        pass

    # Class Methods End
