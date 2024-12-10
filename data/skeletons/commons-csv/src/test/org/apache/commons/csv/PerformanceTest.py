from __future__ import annotations

# Imports Begin
# from src.main.org.apache.commons.io.IOUtils import *
from src.main.org.apache.commons.csv.Token import *
from src.main.org.apache.commons.csv.Lexer import *
from src.main.org.apache.commons.csv.ExtendedBufferedReader import *
from src.main.org.apache.commons.csv.CSVRecord import *
from src.main.org.apache.commons.csv.CSVParser import *
from src.main.org.apache.commons.csv.CSVFormat import *
import typing
from typing import *
import io
from io import IOBase
import pathlib
from abc import ABC

# Imports End


class Stats:

    # Class Fields Begin
    count: int = None
    fields: int = None
    # Class Fields End

    # Class Methods Begin
    def __init__(self, c: int, f: int) -> None:
        pass

    # Class Methods End


class CSVParserFactory(ABC):

    # Class Fields Begin
    # Class Fields End

    # Class Methods Begin
    def createParser(self) -> CSVParser:
        pass

    # Class Methods End


class PerformanceTest:

    # Class Fields Begin
    __PROPERTY_NAMES: typing.List[typing.List[str]] = None
    __max: int = None
    __num: int = None
    __ELAPSED_TIMES: typing.List[int] = None
    __format: CSVFormat = None
    __TEST_RESRC: str = None
    __BIG_FILE: pathlib.Path = None
    # Class Fields End

    # Class Methods Begin
    @staticmethod
    def main(args: typing.List[typing.List[str]]) -> None:
        pass

    @staticmethod
    def __testReadBigFile(split: bool) -> None:
        pass

    @staticmethod
    def __testParseURL() -> None:
        pass

    @staticmethod
    def __testParser(msg: str, fac: CSVParserFactory) -> None:
        pass

    @staticmethod
    def __testParsePathDoubleBuffering() -> None:
        pass

    @staticmethod
    def __testParsePath() -> None:
        pass

    @staticmethod
    def __testParseCommonsCSV() -> None:
        pass

    @staticmethod
    def __testExtendedBuffer(makeString: bool) -> None:
        pass

    @staticmethod
    def __testCSVLexer(newToken: bool, test: str) -> None:
        pass

    @staticmethod
    def __show1(msg: str, s: Stats, start: int) -> None:
        pass

    @staticmethod
    def __show0() -> None:
        pass

    @staticmethod
    def __readAll(in_: io.BufferedReader, split: bool) -> Stats:
        pass

    @staticmethod
    def __iterate(iterable: typing.Iterable[CSVRecord]) -> Stats:
        pass

    @staticmethod
    def __getLexerCtor(clazz: str) -> typing.Callable[..., Lexer]:
        pass

    @staticmethod
    def __createTestCSVLexer(test: str, input_: ExtendedBufferedReader) -> Lexer:
        pass

    @staticmethod
    def __createReader() -> (
        typing.Union[io.TextIOWrapper, io.BufferedReader, io.TextIOBase]
    ):
        pass

    # Class Methods End
