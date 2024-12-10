from __future__ import annotations

# Imports Begin
from src.main.me.lemire.integercompression.synth.ClusteredDataGenerator import *
from src.main.me.lemire.integercompression.differential.XorBinaryPacking import *
from src.main.me.lemire.integercompression.differential.IntegratedVariableByte import *
from src.main.me.lemire.integercompression.differential.IntegratedIntegerCODEC import *
from src.main.me.lemire.integercompression.differential.IntegratedComposition import *
from src.main.me.lemire.integercompression.differential.IntegratedByteIntegerCODEC import *
from src.main.me.lemire.integercompression.differential.IntegratedBinaryPacking import *
from src.main.me.lemire.integercompression.differential.Delta import *
from src.main.me.lemire.integercompression.VariableByte import *
from src.main.me.lemire.integercompression.Simple9 import *
from src.main.me.lemire.integercompression.Simple16 import *
from src.main.me.lemire.integercompression.OptPFDS9 import *
from src.main.me.lemire.integercompression.OptPFDS16 import *
from src.main.me.lemire.integercompression.OptPFD import *
from src.main.me.lemire.integercompression.NewPFDS9 import *
from src.main.me.lemire.integercompression.NewPFDS16 import *
from src.main.me.lemire.integercompression.NewPFD import *
from src.main.me.lemire.integercompression.JustCopy import *
from src.main.me.lemire.integercompression.IntegerCODEC import *
from src.main.me.lemire.integercompression.IntWrapper import *
from src.main.me.lemire.integercompression.GroupSimple9 import *
from src.main.me.lemire.integercompression.FastPFOR128 import *
from src.main.me.lemire.integercompression.FastPFOR import *
from src.main.me.lemire.integercompression.DeltaZigzagVariableByte import *
from src.main.me.lemire.integercompression.DeltaZigzagBinaryPacking import *
from src.main.me.lemire.integercompression.Composition import *
from src.main.me.lemire.integercompression.ByteIntegerCODEC import *
from src.main.me.lemire.integercompression.BinaryPacking import *
from src.main.com.kamikaze.pfordelta.PForDelta import *
import os
import typing
from typing import *
import io
from io import StringIO

# Imports End


class Benchmark:

    # Class Fields Begin
    # Class Fields End

    # Class Methods Begin
    @staticmethod
    def testKamikaze(
        data: typing.List[typing.List[int]], repeat: int, verbose: bool
    ) -> None:
        pass

    @staticmethod
    def main(args: typing.List[typing.List[str]]) -> None:
        pass

    @staticmethod
    def __test(
        csvLog: typing.Union[io.TextIOWrapper, io.StringIO],
        N: int,
        nbr: int,
        repeat: int,
    ) -> None:
        pass

    @staticmethod
    def __generateTestData(
        dataGen: ClusteredDataGenerator, N: int, nbr: int, sparsity: int
    ) -> typing.List[typing.List[int]]:
        pass

    @staticmethod
    def __testByteCodec(
        csvLog: typing.Union[io.TextIOWrapper, io.StringIO],
        sparsity: int,
        c: ByteIntegerCODEC,
        data: typing.List[typing.List[int]],
        repeat: int,
        verbose: bool,
    ) -> None:
        pass

    @staticmethod
    def __testCodec(
        csvLog: typing.Union[io.TextIOWrapper, io.StringIO],
        sparsity: int,
        c: IntegerCODEC,
        data: typing.List[typing.List[int]],
        repeat: int,
        verbose: bool,
    ) -> None:
        pass

    # Class Methods End
