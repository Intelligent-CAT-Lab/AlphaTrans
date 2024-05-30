from __future__ import annotations

# Imports Begin
from src.main.org.apache.commons.csv.CSVRecord import *
from src.main.org.apache.commons.csv.CSVParser import *
from src.main.org.apache.commons.csv.CSVFormat import *
import typing
import io
import pathlib

# Imports End


class CSVFileParserTest:

    # Class Fields Begin
    __BASE_DIR: pathlib.Path = None
    # Class Fields End

    # Class Methods Begin
    def testCSVUrl(self, testFile: pathlib.Path) -> None:
        pass

    def testCSVFile(self, testFile: pathlib.Path) -> None:
        pass

    @staticmethod
    def generateData() -> typing.Iterable[pathlib.Path]:
        pass

    def __readTestData(self, reader: io.BufferedReader) -> str:
        pass

    # Class Methods End
