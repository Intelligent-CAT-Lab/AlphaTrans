import pytest

from src.main.org.apache.commons.csv.CSVRecord import *
from src.main.org.apache.commons.csv.CSVParser import *
from src.main.org.apache.commons.csv.CSVFormat import *
import time
import unittest
import os
import io
import sys
from pathlib import Path

class PerformanceTest(unittest.TestCase):

    __TEST_RESRC = Path(__file__).resolve()\
        .parent.parent.parent.parent.parent.parent \
        / 'resources' / 'org' / 'apache' / 'commons' / 'csv' / 'perf' / 'worldcitiespop.txt.gz'

    __BIG_FILE = Path(os.getenv('TMPDIR', '/tmp')) / "worldcitiespop.txt"

    __max = 10

    
    def __createBufferedReader(self) -> io.BufferedReader:
        return PerformanceTest.__BIG_FILE.open('rb')


    def __parse(self, reader, traverseColumns) -> int:
        format = CSVFormat.DEFAULT\
            .builder().setIgnoreSurroundingSpaces(False).build()
        recordCount = 0
        parser = format.parse(reader)
        try:
            parserIterator = parser.iterator()
            while True:
                try:
                    record = parserIterator.next()
                    recordCount += 1
                    if traverseColumns:
                        recordIterator = record.iterator()
                        while True:
                            try:
                                value = next(recordIterator)
                            except StopIteration:
                                break
                except StopIteration:
                    break             
        finally:
            parser.close()
        return recordCount

    
    def __println(self, s) -> None:
        print(s)
    
    
    def __readAll(self, inBufferedReader) -> int:
        count = 0
        for line in io.TextIOWrapper(inBufferedReader):
            count += 1
        return count

    
    @pytest.mark.test
    def testParseBigFile(self, traverseColumns) -> int:
        startMillis = time.time() * 1000
        reader = self.__createBufferedReader()
        try:
            count = self.__parse(reader, traverseColumns)
            totalMillis = (time.time() * 1000) - startMillis
            self.__println(
                f"File parsed in {totalMillis} milliseconds with Commons CSV: {count} lines."
            )
            return totalMillis
        finally:
            reader.close()

    
    @pytest.mark.test
    def testParseBigFileRepeat(self) -> None:
        bestTime = sys.maxsize
        for i in range(self.__max):
            bestTime = min(self.testParseBigFile(False), bestTime)
        self.__println(f"Best time out of {self.__max} is {bestTime} milliseconds.")

    
    @pytest.mark.test
    def testReadBigFile(self) -> None:
        bestTime = sys.maxsize
        count = 0
        for i in range(self.__max):
            startMillis = 0
            inBufferedReader = self.__createBufferedReader()
            try:
                startMillis = time.time() * 1000
                count = self.__readAll(inBufferedReader)
            finally:
                inBufferedReader.close()
            totalMillis = time.time() * 1000 - startMillis
            bestTime = min(bestTime, totalMillis)
            self.__println(
                f"File read in {totalMillis} milliseconds: {count} lines."
            )
        self.__println(
            f"Best time out of {self.__max} is {bestTime} milliseconds."
        )
