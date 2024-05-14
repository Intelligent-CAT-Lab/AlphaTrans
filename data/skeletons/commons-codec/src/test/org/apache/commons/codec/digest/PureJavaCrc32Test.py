# Imports Begin
from src.main.org.apache.commons.codec.digest.PureJavaCrc32 import *
import typing

# Imports End


class PureJavaCrc32Test:

    # Class Fields Begin
    __theirs: typing.Any = None
    __ours: PureJavaCrc32 = None
    # Class Fields End

    # Class Methods Begin
    def testCorrectness(self) -> None:
        pass

    def __checkSame(self) -> None:
        pass

    def __checkOnBytes(self, bytes: typing.List[int], print: bool) -> None:
        pass

    # Class Methods End


class Table:

    # Class Fields Begin
    __tables: typing.List[typing.List[int]] = None
    # Class Fields End

    # Class Methods Begin
    def toString(self) -> str:
        pass

    @staticmethod
    def main(args: typing.List[str]) -> None:
        pass

    def __init__(self, nBits: int, nTables: int, polynomial: int) -> None:
        pass

    def toStrings(self, nameformat: str) -> typing.List[str]:
        pass

    # Class Methods End


class PerformanceTest:

    # Class Fields Begin
    MAX_LEN: int = None
    BYTES_PER_SIZE: int = None
    zip: typing.Type[typing.Any] = None
    CRCS: typing.List[typing.Type[typing.Any]] = None
    # Class Fields End

    # Class Methods Begin
    @staticmethod
    def main(args: typing.List[str]) -> None:
        pass

    @staticmethod
    def __printSystemProperties(out: typing.IO) -> None:
        pass

    @staticmethod
    def __doBench2(
        clazz: typing.Type[typing.Any],
        numThreads: int,
        bytes: typing.List[int],
        size: int,
    ) -> BenchResult:
        pass

    @staticmethod
    def __doBench1(
        crcs: typing.List[typing.Type[typing.Any]],
        bytes: typing.List[int],
        size: int,
        out: typing.IO,
    ) -> None:
        pass

    @staticmethod
    def __doBench0(crcs: typing.List[typing.Type[typing.Any]], out: typing.IO) -> None:
        pass

    @staticmethod
    def __printCell(s: str, width: int, out: typing.IO) -> None:
        pass

    # Class Methods End


class BenchResult:

    # Class Fields Begin
    value: int = None
    mbps: float = None
    # Class Fields End

    # Class Methods Begin
    def __init__(self, value: int, mbps: float) -> None:
        pass

    # Class Methods End


class Thread:

    # Class Fields Begin
    crc: typing.Any = None
    # Class Fields End

    # Class Methods Begin
    def run(self) -> None:
        pass

    # Class Methods End
