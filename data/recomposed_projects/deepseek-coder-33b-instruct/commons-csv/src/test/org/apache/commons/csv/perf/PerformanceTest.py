from __future__ import annotations
import re
import unittest
import pytest
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
from src.main.org.apache.commons.io.IOUtils import *


class PerformanceTest(unittest.TestCase):

    __max: int = 10
    __BIG_FILE: pathlib.Path = (
        pathlib.Path(tempfile.gettempdir()) / "worldcitiespop.txt"
    )
    __TEST_RESRC: str = "org/apache/commons/csv/perf/worldcitiespop.txt.gz"

    @pytest.mark.test
    def testReadBigFile(self) -> None:

        best_time = float("inf")
        count = 0
        for i in range(self.__max):
            start_millis = time.time() * 1000
            with self.__createBufferedReader() as in_:
                count = self.__readAll(in_)
            total_millis = time.time() * 1000 - start_millis
            best_time = min(total_millis, best_time)
            self.__println(
                f"File read in {total_millis:.0f} milliseconds: {count} lines."
            )
        self.__println(
            f"Best time out of {self.__max} is {best_time:.0f} milliseconds."
        )

    @pytest.mark.test
    def testParseBigFileRepeat(self) -> None:

        bestTime = float("inf")
        for i in range(self.__max):
            bestTime = min(self.testParseBigFile(False), bestTime)
        self.__println(
            "Best time out of {:,} is {:,} milliseconds.".format(self.__max, bestTime)
        )

    def testParseBigFile(self, traverseColumns: bool) -> int:

        startMillis = int(round(time.time() * 1000))
        try:
            reader = self.__createBufferedReader()
            count = self.__parse(reader, traverseColumns)
            totalMillis = int(round(time.time() * 1000)) - startMillis
            self.__println(
                "File parsed in {:,} milliseconds with Commons CSV: {:,} lines.".format(
                    totalMillis, count
                )
            )
            return totalMillis
        finally:
            reader.close()

    def __readAll(self, in_: io.BufferedReader) -> int:
        count = 0
        while in_.readline() != "":
            count += 1
        return count

    def __println(self, s: str) -> None:
        print(s)

    def __parse(
        self,
        reader: typing.Union[io.TextIOWrapper, io.BufferedReader],
        traverseColumns: bool,
    ) -> int:

        format = CSVFormat.builder().setIgnoreSurroundingSpaces(False).build()
        recordCount = 0
        try:
            parser = format.parse(reader)
            for record in parser:
                recordCount += 1
                if traverseColumns:
                    for value in record:
                        pass
        finally:
            parser.close()
        return recordCount

    def __createBufferedReader(self) -> io.BufferedReader:
        return io.BufferedReader(io.FileIO(self.__BIG_FILE))
