import pytest

from src.main.org.apache.commons.csv.CSVRecord import *
from src.main.org.apache.commons.csv.CSVParser import *
from src.main.org.apache.commons.csv.CSVFormat import *
import unittest
from pathlib import Path

class JiraCsv290Test(unittest.TestCase):

    def __testHelper(self, filename, format) -> None:
        content = []
        filePath = Path(__file__).resolve()\
            .parent.parent.parent.parent.parent.parent \
            / 'resources' / 'org' / 'apache' / 'commons' / 'csv' / 'CSV-290' / str(filename)
        
        content = []
        with filePath.open('r', encoding='utf-8') as file:
            csvParser = CSVParser.parse3(file, format)
            try:
                parserIterator = csvParser.iterator()
                while True:
                    try:
                        csvRecord = next(parserIterator)
                        content.append(csvRecord.toList())
                    except StopIteration:
                        break
            finally:
                csvParser.close()

        self.assertEqual(3, len(content))

        self.assertEqual("1", content[0][0])
        self.assertEqual("abc", content[0][1])
        self.assertEqual("test line 1\ntest line 2", content[0][2])  # new line
        self.assertIsNone(content[0][3])  # null
        self.assertEqual("", content[0][4])

        self.assertEqual("2", content[1][0])
        self.assertEqual("\\b:\b \\t:\t \\n:\n \\r:\r", content[1][2])  # \b, \t, \n, \r

        self.assertEqual("3", content[2][0])
        self.assertEqual("b,c,d", content[2][2])  # value has comma
        self.assertEqual("\"quoted\"", content[2][3])  # quoted
    
    
    @pytest.mark.test
    def testPostgresqlCsv(self) -> None:
        self.__testHelper("psql.csv", CSVFormat.POSTGRESQL_CSV)

    
    @pytest.mark.test
    def testPostgresqlText(self) -> None:
        self.__testHelper("psql.tsv", CSVFormat.POSTGRESQL_TEXT)
