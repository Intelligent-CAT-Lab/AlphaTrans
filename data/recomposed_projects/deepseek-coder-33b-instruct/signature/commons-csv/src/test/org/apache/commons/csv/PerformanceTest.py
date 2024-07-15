from __future__ import annotations
import time
import copy
import re
import tempfile
import sys
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

        # Here you need to implement the logic to create a CSVParser.
        # Since the Java method is abstract and doesn't have any implementation,
        # I can't provide a direct translation.
        # You need to implement this method according to your requirements.

        pass


class PerformanceTest:

    __BIG_FILE: pathlib.Path = (
        pathlib.Path(tempfile.gettempdir()) / "worldcitiespop.txt"
    )
    __TEST_RESRC: str = "org/apache/commons/csv/perf/worldcitiespop.txt.gz"
    __format: CSVFormat = CSVFormat.EXCEL
    __max: int = 11
    __num: int = 0

    __PROPERTY_NAMES: typing.List[str] = [
        "java.version",  # Java Runtime Environment version
        "java.vendor",  # Java Runtime Environment vendor
        "java.vm.version",  # Java Virtual Machine implementation version
        "java.vm.name",  # Java Virtual Machine implementation name
        "os.name",  # Operating system name
        "os.arch",  # Operating system architecture
        "os.version",  # Operating system version
    ]

    @staticmethod
    def main(args: typing.List[str]) -> None:

        PerformanceTest.__BIG_FILE = (
            pathlib.Path(tempfile.gettempdir()) / "worldcitiespop.txt"
        )
        PerformanceTest.__TEST_RESRC = (
            "org/apache/commons/csv/perf/worldcitiespop.txt.gz"
        )
        PerformanceTest.__format = CSVFormat.EXCEL
        PerformanceTest.__max = 11
        PerformanceTest.__PROPERTY_NAMES = [
            "java.version",
            "java.vendor",
            "java.vm.version",
            "java.vm.name",
            "os.name",
            "os.arch",
            "os.version",
        ]

        if PerformanceTest.__BIG_FILE.exists():
            print(
                f"Found test fixture {PerformanceTest.__BIG_FILE}: {PerformanceTest.__BIG_FILE.stat().st_size} bytes."
            )
        else:
            print(f"Decompressing test fixture to: {PerformanceTest.__BIG_FILE}...")
            with gzip.open(
                io.BytesIO(
                    pkgutil.get_data(
                        "src.main.org.apache.commons.csv.perf", "worldcitiespop.txt.gz"
                    )
                ),
                "rb",
            ) as input, open(PerformanceTest.__BIG_FILE, "wb") as output:
                shutil.copyfileobj(input, output)
            print(
                f"Decompressed test fixture {PerformanceTest.__BIG_FILE}: {PerformanceTest.__BIG_FILE.stat().st_size} bytes."
            )

        argc = len(args)
        if argc > 0:
            PerformanceTest.__max = int(args[0])

        if argc > 1:
            tests = args[1:]
        else:
            tests = [
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

        for p in PerformanceTest.__PROPERTY_NAMES:
            print(f"{p}={os.getenv(p)}")
        print(f"Max count: {PerformanceTest.__max}\n")

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
                print(f"Invalid test name: {test}")

    @staticmethod
    def __testReadBigFile(split: bool) -> None:

        for i in range(PerformanceTest.__max):
            startMillis = int(round(time.time() * 1000))
            with PerformanceTest.__createReader() as in_:
                stats = PerformanceTest.__readAll(in_, split)
            PerformanceTest.__show1(
                "file+split" if split else "file", stats, startMillis
            )
        PerformanceTest.__show0()

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

        max = 11  # skip first test

        for i in range(max):
            startMillis = None
            stats = None
            try:
                parser = fac.createParser()
                startMillis = int(time.time() * 1000)
                stats = PerformanceTest.__iterate(parser)
            except Exception as e:
                print(f"Exception occurred: {e}")
            finally:
                PerformanceTest.__show1(msg, stats, startMillis)
        PerformanceTest.__show0()

    @staticmethod
    def __testParsePathDoubleBuffering() -> None:

        PerformanceTest.__testParser(
            "CSV-PATH-DB",
            lambda: CSVParser.parse3(
                ExtendedBufferedReader(
                    io.open(PerformanceTest.__BIG_FILE, "r", encoding="ISO-8859-1")
                ),
                PerformanceTest.__format,
            ),
        )

    @staticmethod
    def __testParsePath() -> None:

        PerformanceTest.__testParser(
            "CSV-PATH",
            lambda: CSVParser.parse1(
                open(PerformanceTest.__BIG_FILE, "r", encoding="ISO-8859-1"),
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

        PerformanceTest.__max = 11  # skip first test

        for i in range(PerformanceTest.__max):
            fields = 0
            lines = 0
            startMillis = int(time.time() * 1000)
            try:
                in_ = ExtendedBufferedReader(PerformanceTest.__createReader())
                if makeString:
                    sb = ""
                    while True:
                        read = in_.read0()
                        if read == -1:
                            break
                        sb += chr(read)
                        if read == ord(","):  # count delimiters
                            fields += 1
                            sb = ""
                        elif read == ord("\n"):
                            lines += 1
                            sb = ""
                else:
                    while True:
                        read = in_.read0()
                        if read == -1:
                            break
                        if read == ord(","):  # count delimiters
                            fields += 1
                        elif read == ord("\n"):
                            lines += 1
                fields += lines  # EOL is a delimiter too
            finally:
                in_.close()
            PerformanceTest.__show1(
                "Extended" + (" toString" if makeString else ""),
                Stats(lines, fields),
                startMillis,
            )
        PerformanceTest.__show0()

    @staticmethod
    def __testCSVLexer(newToken: bool, test: str) -> None:

        token = Token()
        dynamic = ""
        for i in range(PerformanceTest.__max):
            simpleName = None
            stats = None
            startMillis = None
            try:
                input = ExtendedBufferedReader(PerformanceTest.__createReader())
                lexer = PerformanceTest.__createTestCSVLexer(test, input)
                if test.startswith("CSVLexer"):
                    dynamic = "!"
                simpleName = lexer.getClass().getSimpleName()
                count = 0
                fields = 0
                startMillis = int(round(time.time() * 1000))
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
                            "invalid parse sequence <" + token.content + ">"
                        )
                    elif token.type == Token.Type.TOKEN:
                        fields += 1
                    elif token.type == Token.Type.COMMENT:
                        pass
                    else:
                        raise RuntimeError("Unexpected Token type: " + token.type)
                stats = Stats(count, fields)
            finally:
                input.close()
            PerformanceTest.__show1(
                simpleName + dynamic + " " + ("new" if newToken else "reset"),
                stats,
                startMillis,
            )
        PerformanceTest.__show0()

    @staticmethod
    def __show1(msg: str, s: Stats, start: int) -> None:

        elapsed = int(round(time.time() * 1000)) - start
        print(f"{msg:<20s}: {elapsed}ms {s.count} lines {s.fields} fields")
        PerformanceTest.__ELAPSED_TIMES[PerformanceTest.__num] = elapsed
        PerformanceTest.__num += 1

    @staticmethod
    def __show0() -> None:

        if PerformanceTest.__num > 1:
            tot = 0
            for i in range(1, PerformanceTest.__num):  # skip first test
                tot += PerformanceTest.__ELAPSED_TIMES[i]
            print(
                "%-20s: %5dms%n%n"
                % ("Average(not first)", tot / (PerformanceTest.__num - 1))
            )
        PerformanceTest.__num = 0  # ready for next set

    @staticmethod
    def __readAll(in_: io.BufferedReader, split: bool) -> Stats:

        count = 0
        fields = 0
        record = in_.readline()
        while record:
            count += 1
            fields += len(record.split(",")) if split else 1
            record = in_.readline()
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

        lexer = getattr(
            __import__("src.main.org.apache.commons.csv", fromlist=[clazz]), clazz
        )
        return lexer.__init__

    @staticmethod
    def __createTestCSVLexer(test: str, input: ExtendedBufferedReader) -> Lexer:

        if test.startswith("CSVLexer"):
            return PerformanceTest.__getLexerCtor(test)(PerformanceTest.__format, input)
        else:
            return Lexer(PerformanceTest.__format, input)

    @staticmethod
    def __createReader() -> typing.Union[io.TextIOWrapper, io.BufferedReader]:

        BIG_FILE = pathlib.Path(tempfile.gettempdir()) / "worldcitiespop.txt"
        return io.TextIOWrapper(io.FileIO(BIG_FILE), encoding="ISO-8859-1")
