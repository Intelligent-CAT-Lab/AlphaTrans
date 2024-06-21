from __future__ import annotations
import re
import unittest
import pytest
import io
import enum
import os
from src.main.org.apache.commons.csv.CSVFormat import *


class CSVFormatPredefinedTest(unittest.TestCase):

    @pytest.mark.test
    def testTDF(self) -> None:

        # Call the private test method with the TDF format and "TDF" as the enumName
        self.__test(CSVFormat.TDF, "TDF")

    @pytest.mark.test
    def testRFC4180(self) -> None:

        # Call the private test method with the RFC4180 format and "RFC4180" as the enumName
        self.__test(CSVFormat.RFC4180, "RFC4180")

    @pytest.mark.test
    def testPostgreSqlText(self) -> None:

        # Call the private test method with the appropriate parameters
        self.__test(CSVFormat.POSTGRESQL_TEXT, "POSTGRESQL_TEXT")

    @pytest.mark.test
    def testPostgreSqlCsv(self) -> None:

        # Call the private test method with the appropriate parameters
        self.__test(CSVFormat.POSTGRESQL_CSV, "PostgreSQLCsv")

    @pytest.mark.test
    def testOracle(self) -> None:

        # Call the private test method with CSVFormat.ORACLE and "Oracle" as arguments
        self.__test(CSVFormat.ORACLE, "Oracle")

    @pytest.mark.test
    def testMySQL(self) -> None:

        # Call the private test method with the MySQL format and the enum name "MySQL"
        self.__test(CSVFormat.MYSQL, "MySQL")

    @pytest.mark.test
    def testMongoDbTsv(self) -> None:

        # Call the private test method with the MongoDB_TSV format and "MongoDBTsv" enum name
        self.__test(CSVFormat.MONGODB_TSV, "MongoDBTsv")

    @pytest.mark.test
    def testMongoDbCsv(self) -> None:

        # Call the private test method with the MongoDB_CSV format and "MongoDBCsv" enum name
        self.__test(CSVFormat.MONGODB_CSV, "MongoDBCsv")

    @pytest.mark.test
    def testExcel(self) -> None:

        # Call the private test method with the Excel format and the enum name "Excel"
        self.__test(CSVFormat.EXCEL, "Excel")

    @pytest.mark.test
    def testDefault(self) -> None:

        # Call the private method test with CSVFormat.DEFAULT and "Default" as arguments
        self.__test(CSVFormat.DEFAULT, "Default")

    def __test(self, format: CSVFormat, enumName: str) -> None:

        # Check if the format is equal to the format returned by the valueOf method of the Predefined class
        self.assertEqual(format, CSVFormat.Predefined.valueOf(enumName).getFormat())

        # Check if the format is equal to the format returned by the valueOf method of the CSVFormat class
        self.assertEqual(format, CSVFormat.valueOf(enumName))
