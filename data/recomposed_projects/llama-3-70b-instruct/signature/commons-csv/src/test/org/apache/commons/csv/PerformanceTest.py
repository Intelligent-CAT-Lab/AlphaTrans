from __future__ import annotations
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

        pass  # LLM could not translate this method

    @staticmethod
    def __testReadBigFile(split: bool) -> None:

        pass  # LLM could not translate this method

    @staticmethod
    def __testParseURL() -> None:
        PerformanceTest.__testParser(
            "CSV-URL",
            lambda: CSVParser.parse5(
                PerformanceTest.__BIG_FILE.to_uri().to_url(),
                StandardCharsets.ISO_8859_1,
                PerformanceTest.__format,
            ),
        )

    @staticmethod
    def __testParser(msg: str, fac: CSVParserFactory) -> None:

        pass  # LLM could not translate this method

    @staticmethod
    def __testParsePathDoubleBuffering() -> None:
        PerformanceTest.__testParser(
            "CSV-PATH-DB",
            lambda: CSVParser.parse3(
                ExtendedBufferedReader(
                    io.BufferedReader(io.FileIO(PerformanceTest.__BIG_FILE, "r"), 8192),
                    8192,
                ),
                PerformanceTest.__format,
            ),
        )

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
        token: Token = Token()
        dynamic: str = ""
        for i in range(PerformanceTest.__max):
            simpleName: str = None
            stats: Stats = None
            startMillis: int = None
            with ExtendedBufferedReader(
                PerformanceTest.__createReader()
            ) as input, PerformanceTest.__createTestCSVLexer(test, input) as lexer:
                if test.startswith("CSVLexer"):
                    dynamic = "!"
                simpleName = lexer.getClass().getSimpleName()
                count: int = 0
                fields: int = 0
                startMillis = System.currentTimeMillis()
                while True:
                    if newToken:
                        token = Token()
                    else:
                        token.reset()
                    lexer.nextToken(token)
                    if token.type == Token.Type.EOF:
                        break
                    elif token.type == Token.Type.EORECORD:
                        fields += 1
                        count += 1
                    elif token.type == Token.Type.INVALID:
                        raise IOException(
                            "invalid parse sequence <" + token.content.toString() + ">"
                        )
                    elif token.type == Token.Type.TOKEN:
                        fields += 1
                    elif token.type == Token.Type.COMMENT:  # not really expecting these
                        pass
                    else:
                        raise RuntimeError("Unexpected Token type: " + token.type)
                stats = Stats(count, fields)
            PerformanceTest.__show1(
                simpleName + dynamic + " " + ("new" if newToken else "reset"),
                stats,
                startMillis,
            )
        PerformanceTest.__show0()

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
        return Lexer.__format, (
            input if test.startswith("CSVLexer") else Lexer(Lexer.__format, input)
        )

    @staticmethod
    def __createReader() -> typing.Union[io.TextIOWrapper, io.BufferedReader]:
        return io.TextIOWrapper(
            io.BufferedReader(io.FileIO(PerformanceTest.__BIG_FILE, "r")),
            encoding="ISO-8859-1",
        )
