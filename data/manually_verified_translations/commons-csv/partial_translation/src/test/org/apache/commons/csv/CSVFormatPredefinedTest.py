from __future__ import annotations
import re
import unittest
import pytest
import io
import enum
import os
import unittest
from src.main.org.apache.commons.csv.CSVFormat import *


class CSVFormatPredefinedTest(unittest.TestCase):

    def testTDF(self) -> None:
        self.__test(CSVFormat.TDF, "TDF")

    def testRFC4180(self) -> None:
        self.__test(CSVFormat.RFC4180, "RFC4180")

    def testPostgreSqlText(self) -> None:
        self.__test(CSVFormat.POSTGRESQL_TEXT, "POSTGRESQL_TEXT")

    def testPostgreSqlCsv(self) -> None:
        self.__test(CSVFormat.POSTGRESQL_CSV, "POSTGRESQL_CSV")

    def testOracle(self) -> None:
        self.__test(CSVFormat.ORACLE, "ORACLE")

    def testMySQL(self) -> None:
        self.__test(CSVFormat.MYSQL, "MYSQL")

    def testMongoDbTsv(self) -> None:
        self.__test(CSVFormat.MONGODB_TSV, "MONGODB_TSV")

    def testMongoDbCsv(self) -> None:
        self.__test(CSVFormat.MONGODB_CSV, "MONGODB_CSV")

    def testExcel(self) -> None:
        self.__test(CSVFormat.EXCEL, "EXCEL")

    def testDefault(self) -> None:
        self.assertEqual(CSVFormat.DEFAULT, Predefined.valueOf("Default").getFormat())
        self.assertEqual(CSVFormat.DEFAULT, CSVFormat.valueOf("Default"))

    def __test(self, format_: CSVFormat, enumName: str) -> None:
        self.assertEqual(format_, Predefined.valueOf(enumName).getFormat())
        self.assertEqual(format_, CSVFormat.valueOf(enumName))
