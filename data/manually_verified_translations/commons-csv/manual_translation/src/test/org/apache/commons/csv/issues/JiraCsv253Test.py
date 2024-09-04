from __future__ import annotations
import re
from io import StringIO
import unittest
import pytest
import io
import typing
from typing import *
import unittest
from src.main.org.apache.commons.csv.CSVFormat import *
from src.main.org.apache.commons.csv.CSVParser import *
from src.main.org.apache.commons.csv.CSVRecord import *
from src.main.org.apache.commons.csv.QuoteMode import *


class JiraCsv253Test(unittest.TestCase):

    def testHandleAbsentValues(self) -> None:

        source = '"John",,"Doe"\n' + ',"AA",123\n' + '"John",90,\n' + '"",,90'
        csvFormat = (
            CSVFormat.DEFAULT.builder().setQuoteMode(QuoteMode.NON_NUMERIC).build()
        )
        parser = csvFormat.parse(io.StringIO(source))
        csvRecords = parser.iterator()
        self.__assertArrayEqual(["John", None, "Doe"], next(csvRecords))
        self.__assertArrayEqual([None, "AA", "123"], next(csvRecords))
        self.__assertArrayEqual(["John", "90", None], next(csvRecords))
        self.__assertArrayEqual(["", None, "90"], next(csvRecords))

    def __assertArrayEqual(
        self, expected: typing.List[typing.List[str]], actual: CSVRecord
    ) -> None:
        for i in range(len(expected)):
            self.assertEqual(expected[i], actual.get1(i))
