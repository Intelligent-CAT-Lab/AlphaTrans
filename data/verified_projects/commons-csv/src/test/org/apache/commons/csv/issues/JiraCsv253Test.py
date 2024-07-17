import pytest

from src.main.org.apache.commons.csv.QuoteMode import *
from src.main.org.apache.commons.csv.CSVRecord import *
from src.main.org.apache.commons.csv.CSVParser import *
from src.main.org.apache.commons.csv.CSVFormat import *
import unittest
import io


class JiraCsv253Test(unittest.TestCase):

    def __assertArrayEqual(self, expected, actual) -> None:
        for i in range(len(expected)):
            self.assertEqual(
                expected[i],
                actual.get1(i),
                f"Expected {expected[i]} but got {actual.get1(i)}",
            )

    
    @pytest.mark.test
    def testHandleAbsentValues(self) -> None:
        source = "\"John\",,\"Doe\"\n" +\
            ",\"AA\",123\n" +\
            "\"John\",90,\n" +\
            "\"\",,90"
        csvFormat = CSVFormat.DEFAULT\
            .builder()\
            .setQuoteMode(QuoteMode.NON_NUMERIC)\
            .build()
        parser = csvFormat.parse(io.StringIO(source))
        try:
            csvRecords = parser.iterator()
            self.__assertArrayEqual(
                ["John", None, "Doe"],
                csvRecords.next()
            )
            self.__assertArrayEqual(
                [None, "AA", "123"],
                csvRecords.next()
            )
            self.__assertArrayEqual(
                ["John", "90", None],
                csvRecords.next()
            )
            self.__assertArrayEqual(
                ["", None, "90"],
                csvRecords.next()
            )
        finally:
            parser.close()
