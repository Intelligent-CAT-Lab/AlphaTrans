from __future__ import annotations
import time
import re
import os
import unittest
import pytest
import pathlib
import io
import typing
from typing import *
import unittest
from src.main.org.apache.commons.csv.CSVFormat import *
from src.main.org.apache.commons.csv.CSVParser import *
from src.main.org.apache.commons.csv.CSVRecord import *
from src.main.org.apache.commons.csv.ExtendedBufferedReader import *
from src.main.org.apache.commons.csv.Lexer import *
from src.main.org.apache.commons.csv.Token import *

# from src.main.org.apache.commons.io.IOUtils import *


class PerformanceTest(unittest.TestCase):

    __max: int = 10
    __BIG_FILE: pathlib.Path = pathlib.Path(
        os.getenv("java.io.tmpdir"), "worldcitiespop.txt"
    )
    __TEST_RESRC: str = "org/apache/commons/csv/perf/worldcitiespop.txt.gz"

    def testReadBigFile(self) -> None:
        bestTime: int = 9223372036854775807
        count: int
        for i in range(0, self.__max):
            startMillis: int
            with self.__createBufferedReader() as in_:
                startMillis = int(round(time.time() * 1000))
                count = self.__readAll(in_)
            totalMillis: int = int(round(time.time() * 1000)) - startMillis
            bestTime = min(totalMillis, bestTime)
            self.__println(
                str.format(
                    "File read in %,d milliseconds: %,d lines.", totalMillis, count
                )
            )
        self.__println(
            str.format(
                "Best time out of %,d is %,d milliseconds.", self.__max, bestTime
            )
        )

    def testParseBigFileRepeat(self) -> None:
        bestTime: int = 9223372036854775807
        for i in range(0, self.__max):
            bestTime = min(self.testParseBigFile(False), bestTime)
        self.__println(
            str.format(
                "Best time out of %,d is %,d milliseconds.", self.__max, bestTime
            )
        )

    def testParseBigFile(self, traverseColumns: bool) -> int:
        startMillis = int(round(time.time() * 1000))
        try:
            with self.__createBufferedReader() as reader:
                count = self.__parse(reader, traverseColumns)
                totalMillis = int(round(time.time() * 1000)) - startMillis
                self.__println(
                    f"File parsed in {totalMillis:,} milliseconds with Commons CSV: {count:,} lines."
                )
                return totalMillis
        except Exception as e:
            raise e

    def __readAll(self, in_: io.BufferedReader) -> int:
        count = 0
        while in_.readline() != None:
            count += 1
        return count

    def __println(self, s: str) -> None:
        print(s)

    def __parse(
        self,
        reader: typing.Union[io.TextIOWrapper, io.BufferedReader],
        traverseColumns: bool,
    ) -> int:
        format = CSVFormat.DEFAULT.builder().setIgnoreSurroundingSpaces(False).build()
        recordCount = 0
        with CSVParser(format.parse(reader)) as parser:
            for record in parser:
                recordCount += 1
                if traverseColumns:
                    for value in record:
                        pass
        return recordCount

    def __createBufferedReader(self) -> io.BufferedReader:
        return io.BufferedReader(io.FileIO(self.__BIG_FILE))
