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


class JiraCsv93Test(unittest.TestCase):

    __objects2: typing.List[typing.Any] = ["abc", "NULL", None, "a,b,c", 123]
    __objects1: typing.List[typing.Any] = ["abc", "", None, "a,b,c", 123]

    def testWithSetNullStringNULL(self) -> None:

        pass  # LLM could not translate this method

    def testWithSetNullStringEmptyString(self) -> None:

        pass  # LLM could not translate this method

    def testWithNotSetNullString(self) -> None:

        pass  # LLM could not translate this method

    def __every(
        self,
        csvFormat: CSVFormat,
        objects: typing.List[typing.Any],
        format: str,
        data: typing.List[str],
    ) -> None:
        source = csvFormat.format(objects)
        self.assertEqual(format, csvFormat.format(objects))
        with csvFormat.parse(io.StringIO(source)) as csvParser:
            csvRecord = next(csvParser.iterator())
            for i in range(len(data)):
                self.assertEqual(csvRecord.get1(i), data[i])
