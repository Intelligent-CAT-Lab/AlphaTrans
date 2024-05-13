# Imports Begin
from src.main.org.apache.commons.csv.CSVRecord import *
from src.main.org.apache.commons.csv.CSVParser import *
from src.main.org.apache.commons.csv.CSVFormat import *
import unittest
import os
import typing
from typing import *
# Imports End

class new Function<CSVRecord,List<String>>(...) { ... }(unittest.TestCase):

    # Class Fields Begin
    # Class Fields End

    # Class Methods Begin
    def apply(self, p0: CSVRecord) -> typing.List[str]:

            return p0.toList()

    # Class Methods End


class JiraCsv290Test(unittest.TestCase):

    # Class Fields Begin
    # Class Fields End

    # Class Methods Begin
    def testPostgresqlText(self) -> None:

            self.__testHelper("psql.tsv", CSVFormat.POSTGRESQL_TEXT)

    def testPostgresqlCsv(self) -> None:

            self.__testHelper("psql.csv", CSVFormat.POSTGRESQL_CSV)

    def __testHelper(self, filename: str, format: CSVFormat) -> None:

            content: List[List[str]] = []
            try:
                csv_parser: CSVParser = CSVParser.parse3(
                    open(f"/org/apache/commons/csv/CSV-290/{filename}", "r"), format
                )
                content = list(csv_parser.stream().map(lambda x: x.to_list()).collect(Collectors.to_list()))
            except Exception as e:
                raise e
            self.assertEqual(3, len(content))
            self.assertEqual("1", content[0][0])
            self.assertEqual("abc", content[0][1])
            self.assertEqual("test line 1\ntest line 2", content[0][2])
            self.assertEqual(None, content[0][3])
            self.assertEqual("", content[0][4])
            self.assertEqual("2", content[1][0])
            self.assertEqual("\\b:\b \\t:\t \\n:\n \\r:\r", content[1][2])
            self.assertEqual("3", content[2][0])
            self.assertEqual("b,c,d", content[2][2])
            self.assertEqual("\"quoted\"", content[2][3])

    # Class Methods End


