from __future__ import annotations
import copy
import re
import os
from io import BytesIO
import unittest
import pytest
from abc import ABC
import pathlib
import io
import typing
from typing import *
from src.main.org.apache.commons.csv.CSVFormat import *
from src.main.org.apache.commons.csv.CSVParser import *
from src.main.org.apache.commons.csv.CSVRecord import *
from src.main.org.apache.commons.csv.ExtendedBufferedReader import *
from src.main.org.apache.commons.csv.Lexer import *
from src.main.org.apache.commons.csv.Token import *

# from src.main.org.apache.commons.io.IOUtils import *


class Stats:

    fields: int = 0

    count: int = 0

    def __init__(self, c: int, f: int) -> None:
        self.count = c
        self.fields = f


class CSVParserFactory(ABC):

    def createParser(self) -> CSVParser:
        return CSVParser(self)


class PerformanceTest:

    __BIG_FILE: pathlib.Path = pathlib.Path(
        os.getenv("java.io.tmpdir"), "worldcitiespop.txt"
    )
    __TEST_RESRC: str = "org/apache/commons/csv/perf/worldcitiespop.txt.gz"
    __format: CSVFormat = CSVFormat.EXCEL
    ELAPSED_TIMES: typing.List[int] = [0] * max
    __num: int = 0

    __max: int = 11
    __PROPERTY_NAMES: typing.List[str] = [
        "java.version",
        "java.vendor",
        "java.vm.version",
        "java.vm.name",
        "os.name",
        "os.arch",
        "os.version",
    ]

    @staticmethod
    def main(args: typing.List[str]) -> None:
        if PerformanceTest.__BIG_FILE.exists():
            print(
                "Found test fixture %s: %,d bytes."
                % (
                    PerformanceTest.__BIG_FILE,
                    PerformanceTest.__BIG_FILE.stat().st_size,
                )
            )
        else:
            print(
                "Decompressing test fixture to: "
                + str(PerformanceTest.__BIG_FILE)
                + "..."
            )
            with io.BytesIO(PerformanceTest.__BIG_FILE.read_bytes()) as input, open(
                PerformanceTest.__BIG_FILE, "wb"
            ) as output:
                IOUtils.copy(input, output)
                print(
                    "Decompressed test fixture %s: %,d bytes."
                    % (
                        PerformanceTest.__BIG_FILE,
                        PerformanceTest.__BIG_FILE.stat().st_size,
                    )
                )
        argc = len(args)
        if argc > 0:
            PerformanceTest.__max = int(args[0])
        tests = (
            args[1:]
            if argc > 1
            else [
                "file",
                "split",
                "extb",
                "exts",
                "csv",
                "csv-path",
                "csv-path-db",
                "csv-url",
                "lexreset",
                "lexnew",
            ]
        )
        for p in PerformanceTest.__PROPERTY_NAMES:
            print("%s=%s" % (p, System.getProperty(p)))
        print("Max count: %d" % PerformanceTest.__max)
        for test in tests:
            if test == "file":
                PerformanceTest.__testReadBigFile(False)
            elif test == "split":
                PerformanceTest.__testReadBigFile(True)
            elif test == "csv":
                PerformanceTest.__testParseCommonsCSV()
            elif test == "csv-path":
                PerformanceTest.__testParsePath()
            elif test == "csv-path-db":
                PerformanceTest.__testParsePathDoubleBuffering()
            elif test == "csv-url":
                PerformanceTest.__testParseURL()
            elif test == "lexreset":
                PerformanceTest.__testCSVLexer(False, test)
            elif test == "lexnew":
                PerformanceTest.__testCSVLexer(True, test)
            elif test.startswith("CSVLexer"):
                PerformanceTest.__testCSVLexer(False, test)
            elif test == "extb":
                PerformanceTest.__testExtendedBuffer(False)
            elif test == "exts":
                PerformanceTest.__testExtendedBuffer(True)
            else:
                print("Invalid test name: %s" % test)

    @staticmethod
    def __testReadBigFile(split: bool) -> None:

        pass  # LLM could not translate this method

    @staticmethod
    def __testParseURL() -> None:
        PerformanceTest.__testParser(
            "CSV-URL",
            lambda: CSVParser.parse5(
                PerformanceTest.__BIG_FILE.toURI().toURL(),
                StandardCharsets.ISO_8859_1,
                PerformanceTest.__format,
            ),
        )

    @staticmethod
    def __testParser(msg: str, fac: CSVParserFactory) -> None:
        for i in range(PerformanceTest.__max):
            startMillis: int = 0
            stats: Stats = None
            with fac.createParser() as parser:
                startMillis = System.currentTimeMillis()
                stats = PerformanceTest.__iterate(parser)
            PerformanceTest.__show1(msg, stats, startMillis)
        PerformanceTest.__show0()

    @staticmethod
    def __testParsePathDoubleBuffering() -> None:

        pass  # LLM could not translate this method

    @staticmethod
    def __testParsePath() -> None:
        PerformanceTest.__testParser(
            "CSV-PATH",
            lambda: CSVParser.parse1(
                io.BytesIO(PerformanceTest.__BIG_FILE.read_bytes()),
                "ISO-8859-1",
                PerformanceTest.__format,
            ),
        )

    @staticmethod
    def __testParseCommonsCSV() -> None:
        PerformanceTest.__testParser(
            "CSV",
            lambda: CSVParser.CSVParser1(
                PerformanceTest.__createReader(), PerformanceTest.__format
            ),
        )

    @staticmethod
    def __testExtendedBuffer(makeString: bool) -> None:

        pass  # LLM could not translate this method

    @staticmethod
    def __testCSVLexer(newToken: bool, test: str) -> None:

        pass  # LLM could not translate this method

    @staticmethod
    def __show1(msg: str, s: Stats, start: int) -> None:
        elapsed: int = System.currentTimeMillis() - start
        System.out.printf(
            "%-20s: %5dms %d lines %d fields%n", msg, elapsed, s.count, s.fields
        )
        ELAPSED_TIMES[num] = elapsed
        num += 1

    @staticmethod
    def __show0() -> None:

        pass  # LLM could not translate this method

    @staticmethod
    def __readAll(in_: io.BufferedReader, split: bool) -> Stats:
        count = 0
        fields = 0
        record = ""
        while (record := in_.readline()) != "":
            count += 1
            fields += len(record.split(",")) if split else 1
        return Stats(count, fields)

    @staticmethod
    def __iterate(iterable: typing.Iterable[CSVRecord]) -> Stats:
        count = 0
        fields = 0
        for record in iterable:
            count += 1
            fields += record.size()
        return Stats(count, fields)

    @staticmethod
    def __getLexerCtor(clazz: str) -> typing.Callable[..., Lexer]:
        lexer = typing.cast(
            typing.Type[Lexer],
            typing.cast(
                typing.Type, __import__("src.main.org.apache.commons.csv." + clazz)
            ),
        )
        return lexer.getConstructor(CSVFormat, ExtendedBufferedReader)

    @staticmethod
    def __createTestCSVLexer(test: str, input: ExtendedBufferedReader) -> Lexer:
        return (
            PerformanceTest.__getLexerCtor(test).newInstance(
                PerformanceTest.__format, input
            )
            if test.startswith("CSVLexer")
            else Lexer(PerformanceTest.__format, input)
        )

    @staticmethod
    def __createReader() -> typing.Union[io.TextIOWrapper, io.BufferedReader]:
        return io.TextIOWrapper(
            io.BufferedReader(io.FileIO(PerformanceTest.__BIG_FILE, "r")),
            encoding="ISO-8859-1",
        )
