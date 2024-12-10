from __future__ import annotations
import time
import re
import tempfile
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

import gzip
import shutil
import pathlib
import tempfile



@unittest.skip("excluded by pom.xml")
class PerformanceTest(unittest.TestCase):

    __max: int = 10
    __BIG_FILE: pathlib.Path = (
        pathlib.Path(tempfile.gettempdir()) / "worldcitiespop.txt"
    )
    __TEST_RESRC = Path(__file__).resolve()\
        .parent.parent.parent.parent.parent.parent \
        / 'resources' / 'org' / 'apache' / 'commons' / 'csv' / 'perf' / 'worldcitiespop.txt.gz'
    
    # Function to copy and decompress the file
    def copy_and_decompress(src: pathlib.Path, dst: pathlib.Path) -> None:
        with gzip.open(src, 'rb') as f_in:
            with open(dst, 'wb') as f_out:
                shutil.copyfileobj(f_in, f_out)

    def testReadBigFile(self) -> None:

        best_time = float("inf")
        count = 0
        for i in range(self.__max):
            in_ = self.__createBufferedReader()
            try:
                start_millis = time.time() * 1000
                count = self.__readAll(in_)
            finally:
                in_.close()
            total_millis = time.time() * 1000 - start_millis
            best_time = min(total_millis, best_time)
            self.__println(
                f"File read in {total_millis:.0f} milliseconds: {count} lines."
            )
        self.__println(
            f"Best time out of {self.__max} is {best_time:.0f} milliseconds."
        )

    def testParseBigFileRepeat(self) -> None:

        bestTime = float("inf")
        for i in range(self.__max):
            bestTime = min(self._testParseBigFile(False), bestTime)
        self.__println(
            "Best time out of {} is {} milliseconds.".format(self.__max, bestTime)
        )

    def _testParseBigFile(self, traverseColumns: bool) -> int:

        start_millis = int(round(time.time() * 1000))
        reader = self.__createBufferedReader()
        try:
            count = self.__parse(reader, traverseColumns)
            total_millis = int(round(time.time() * 1000)) - start_millis
            self.__println(
                "File parsed in {} milliseconds with Commons CSV: {} lines.".format(
                    total_millis, count
                )
            )
            return total_millis
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

        format = CSVFormat.DEFAULT.builder().setIgnoreSurroundingSpaces(False).build()
        recordCount = 0
        parser = format.parse(reader)
        try:
            for record in parser:
                recordCount += 1
                if traverseColumns:
                    for value in record:
                        pass
        finally:
            parser.close()
        return recordCount

    def __createBufferedReader(self) -> io.BufferedReader:
        return PerformanceTest.__BIG_FILE.open('rb')


# Perform the copy and decompression
PerformanceTest.copy_and_decompress(
    PerformanceTest._PerformanceTest__TEST_RESRC,
    PerformanceTest._PerformanceTest__BIG_FILE
)