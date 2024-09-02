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
        self.__test(CSVFormat.POSTGRESQL_TEXT, "PostgreSQLText")

    def testPostgreSqlCsv(self) -> None:
        self.__test(CSVFormat.POSTGRESQL_CSV, "PostgreSQLCsv")

    def testOracle(self) -> None:
        self.__test(CSVFormat.ORACLE, "Oracle")

    def testMySQL(self) -> None:
        self.__test(CSVFormat.MYSQL, "MySQL")

    def testMongoDbTsv(self) -> None:
        self.__test(CSVFormat.MONGODB_TSV, "MongoDBTsv")

    def testMongoDbCsv(self) -> None:
        self.__test(CSVFormat.MONGODB_CSV, "MongoDBCsv")

    def testExcel(self) -> None:
        self.__test(CSVFormat.EXCEL, "Excel")

    def testDefault(self) -> None:
        self.assertEqual(CSVFormat.DEFAULT, getattr(Predefined, "Default").getFormat())
        self.assertEqual(CSVFormat.DEFAULT, CSVFormat.valueOf("Default"))

    def __test(self, format_: CSVFormat, enumName: str) -> None:
        self.assertEqual(format_, getattr(Predefined, enumName).getFormat())
        self.assertEqual(format_, CSVFormat.valueOf(enumName))
