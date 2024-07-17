import pytest

from src.main.org.apache.commons.csv.CSVFormat import *
import unittest

class CSVFormatPredefinedTest(unittest.TestCase):

    def __test(self, format, enumName) -> None:
        self.assertEqual(
            format,
            getattr(CSVFormat.Predefined, enumName).getFormat()
        )
        self.assertEqual(
            format,
            CSVFormat.valueOf(enumName)
        )
    
    
    @pytest.mark.test
    def testDefault(self) -> None:
        self.__test(CSVFormat.DEFAULT, "Default")

    
    @pytest.mark.test
    def testExcel(self) -> None:
        self.__test(CSVFormat.EXCEL, "Excel")

    
    @pytest.mark.test
    def testMongoDbCsv(self) -> None:
        self.__test(CSVFormat.MONGODB_CSV, "MongoDBCsv")

    
    @pytest.mark.test
    def testMongoDbTsv(self) -> None:
        self.__test(CSVFormat.MONGODB_TSV, "MongoDBTsv")

    
    @pytest.mark.test
    def testMySQL(self) -> None:
        self.__test(CSVFormat.MYSQL, "MySQL")

    
    @pytest.mark.test
    def testOracle(self) -> None:
        self.__test(CSVFormat.ORACLE, "Oracle")

    
    @pytest.mark.test
    def testPostgreSqlCsv(self) -> None:
        self.__test(CSVFormat.POSTGRESQL_CSV, "PostgreSQLCsv")
    
    
    @pytest.mark.test
    def testPostgreSqlText(self) -> None:
        self.__test(CSVFormat.POSTGRESQL_TEXT, "PostgreSQLText")

    
    @pytest.mark.test
    def testRFC4180(self) -> None:
        self.__test(CSVFormat.RFC4180, "RFC4180")
    
    
    @pytest.mark.test
    def testTDF(self) -> None:
        self.__test(CSVFormat.TDF, "TDF")
