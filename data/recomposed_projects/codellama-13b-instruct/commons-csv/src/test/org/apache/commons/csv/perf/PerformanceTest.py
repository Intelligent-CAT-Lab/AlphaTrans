# Imports Begin
from src.main.org.apache.commons.io.IOUtils import *
from src.main.org.apache.commons.csv.Token import *
from src.main.org.apache.commons.csv.Lexer import *
from src.main.org.apache.commons.csv.ExtendedBufferedReader import *
from src.main.org.apache.commons.csv.CSVRecord import *
from src.main.org.apache.commons.csv.CSVParser import *
from src.main.org.apache.commons.csv.CSVFormat import *
import typing
import tempfile
import unittest
import os
import io
import pathlib
# Imports End

class PerformanceTest(unittest.TestCase):

    # Class Fields Begin
    __TEST_RESRC: str = "org/apache/commons/csv/perf/worldcitiespop.txt.gz"
    __BIG_FILE: pathlib.Path = pathlib.Path(os.path.join(tempfile.gettempdir(), "worldcitiespop.txt"))
    __max: int = 10
    # Class Fields End

    # Class Methods Begin
    def testReadBigFile(self) -> None:

        best_time = float('inf')
        count = 0
        for i in range(self.max):
            try:
                start_millis = time.time() * 1000
                count = self.__readAll(self.__createBufferedReader())
                total_millis = time.time() * 1000 - start_millis
                best_time = min(best_time, total_millis)
                self.__println(f"File read in {total_millis} milliseconds: {count} lines.")
            except Exception as e:
                print(f"Error reading file: {e}")
        self.__println(f"Best time out of {self.max} is {best_time} milliseconds.")

    def testParseBigFileRepeat(self) -> None:

            best_time = self.__max
            for i in range(self.max):
                best_time = min(self.testParseBigFile(False), best_time)
            self.__println(f"Best time out of {self.max} is {best_time} milliseconds.")

    def testParseBigFile(self, traverseColumns: bool) -> int:

            start_millis = time.time() * 1000
            try:
                reader = self.__createBufferedReader()
                count = self.__parse(reader, traverseColumns)
                total_millis = (time.time() * 1000) - start_millis
                self.__println(f"File parsed in {total_millis} milliseconds with Commons CSV: {count} lines.")
                return total_millis
            except Exception as e:
                raise e

    def __readAll(self, in: io.BufferedReader) -> int:


        pass # LLM could not translate method body

    def __println(self, s: str) -> None:

            self.assertTrue(isinstance(s, str), "s must be a string")
            print(s)

    def __parse(self, reader: typing.Union[io.TextIOWrapper, io.BufferedReader], traverseColumns: bool) -> int:

        format = CSVFormat.DEFAULT.builder().setIgnoreSurroundingSpaces(False).build()
        record_count = 0
        try:
            with format.parse(reader) as parser:
                for record in parser:
                    record_count += 1
                    if traverseColumns:
                        for value in record:
                            pass
        except Exception as e:
            raise e
        return record_count

    def __createBufferedReader(self) -> io.BufferedReader:

            return io.BufferedReader(io.FileReader(self.__BIG_FILE))

    # Class Methods End


