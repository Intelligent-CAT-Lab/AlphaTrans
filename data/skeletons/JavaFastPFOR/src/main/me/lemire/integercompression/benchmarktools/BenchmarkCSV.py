from __future__ import annotations

# Imports Begin
from src.main.me.lemire.integercompression.differential.IntegratedVariableByte import *
from src.main.me.lemire.integercompression.differential.IntegratedIntegerCODEC import *
from src.main.me.lemire.integercompression.differential.IntegratedComposition import *
from src.main.me.lemire.integercompression.differential.IntegratedByteIntegerCODEC import *
from src.main.me.lemire.integercompression.differential.IntegratedBinaryPacking import *
from src.main.me.lemire.integercompression.VariableByte import *
from src.main.me.lemire.integercompression.IntegerCODEC import *
from src.main.me.lemire.integercompression.IntWrapper import *
from src.main.me.lemire.integercompression.FastPFOR128 import *
from src.main.me.lemire.integercompression.FastPFOR import *
from src.main.me.lemire.integercompression.Composition import *
from src.main.me.lemire.integercompression.ByteIntegerCODEC import *
from src.main.me.lemire.integercompression.BinaryPacking import *
import os
import typing
from typing import *
import io

# Imports End


class CompressionMode:

    # Class Fields Begin
    AS_IS: CompressionMode = None
    DELTA: CompressionMode = None
    # Class Fields End

    # Class Methods Begin
    # Class Methods End


class Format:

    # Class Fields Begin
    ONEARRAYPERFILE: Format = None
    ONEARRAYPERLINE: Format = None
    ONEINTPERLINE: Format = None
    # Class Fields End

    # Class Methods Begin
    # Class Methods End


class BenchmarkCSV:

    # Class Fields Begin
    codecs: typing.List[IntegratedIntegerCODEC] = None
    bcodecs: typing.List[IntegratedByteIntegerCODEC] = None
    regcodecs: typing.List[IntegerCODEC] = None
    regbcodecs: typing.List[ByteIntegerCODEC] = None
    # Class Fields End

    # Class Methods Begin
    @staticmethod
    def main(args: typing.List[typing.List[str]]) -> None:
        pass

    @staticmethod
    def __bytebench(
        postings: typing.List[typing.List[int]], cm: CompressionMode, verbose: bool
    ) -> None:
        pass

    @staticmethod
    def __bench(
        postings: typing.List[typing.List[int]], cm: CompressionMode, verbose: bool
    ) -> None:
        pass

    @staticmethod
    def __loadIntegers(filename: str, f: Format) -> typing.List[typing.List[int]]:
        pass

    # Class Methods End
