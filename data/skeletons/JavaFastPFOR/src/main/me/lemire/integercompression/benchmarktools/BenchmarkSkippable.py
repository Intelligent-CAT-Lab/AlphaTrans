from __future__ import annotations

# Imports Begin
from src.main.me.lemire.integercompression.synth.ClusteredDataGenerator import *
from src.main.me.lemire.integercompression.differential.SkippableIntegratedIntegerCODEC import *
from src.main.me.lemire.integercompression.differential.SkippableIntegratedComposition import *
from src.main.me.lemire.integercompression.differential.IntegratedVariableByte import *
from src.main.me.lemire.integercompression.differential.IntegratedBinaryPacking import *
from src.main.me.lemire.integercompression.differential.Delta import *
from src.main.me.lemire.integercompression.VariableByte import *
from src.main.me.lemire.integercompression.SkippableIntegerCODEC import *
from src.main.me.lemire.integercompression.SkippableComposition import *
from src.main.me.lemire.integercompression.Simple9 import *
from src.main.me.lemire.integercompression.Simple16 import *
from src.main.me.lemire.integercompression.OptPFDS9 import *
from src.main.me.lemire.integercompression.OptPFDS16 import *
from src.main.me.lemire.integercompression.OptPFD import *
from src.main.me.lemire.integercompression.NewPFDS9 import *
from src.main.me.lemire.integercompression.NewPFDS16 import *
from src.main.me.lemire.integercompression.NewPFD import *
from src.main.me.lemire.integercompression.JustCopy import *
from src.main.me.lemire.integercompression.IntWrapper import *
from src.main.me.lemire.integercompression.FastPFOR128 import *
from src.main.me.lemire.integercompression.FastPFOR import *
from src.main.me.lemire.integercompression.BinaryPacking import *
import os
import typing
from typing import *
import io
from io import StringIO

# Imports End


class BenchmarkSkippable:

    # Class Fields Begin
    codecs: typing.List[typing.Any] = None
    # Class Fields End

    # Class Methods Begin
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
    def __testCodec(
        csvLog: typing.Union[io.TextIOWrapper, io.StringIO],
        sparsity: int,
        c: typing.Any,
        data: typing.List[typing.List[int]],
        repeat: int,
        verbose: bool,
    ) -> None:
        pass

    @staticmethod
    def __decompressFromSkipTable(
        c: typing.Any,
        compressed: typing.List[int],
        compressedpos: IntWrapper,
        metadata: typing.List[int],
        blocksize: int,
        data: typing.List[int],
    ) -> int:
        pass

    @staticmethod
    def __compressWithSkipTable(
        c: typing.Any,
        data: typing.List[int],
        output: typing.List[int],
        outpos: IntWrapper,
        metadata: typing.List[int],
        blocksize: int,
    ) -> int:
        pass

    # Class Methods End
