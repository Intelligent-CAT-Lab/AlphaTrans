from __future__ import annotations

# Imports Begin
from src.main.org.apache.commons.csv.QuoteMode import *
from src.main.org.apache.commons.csv.CSVRecord import *
from src.main.org.apache.commons.csv.CSVParser import *
from src.main.org.apache.commons.csv.CSVFormat import *
import unittest
import typing
from typing import *
import io

# Imports End


class JiraCsv93Test(unittest.TestCase):

    # Class Fields Begin
    __objects1: typing.List[typing.Any] = None
    __objects2: typing.List[typing.Any] = None
    # Class Fields End

    # Class Methods Begin
    def testWithSetNullStringNULL(self) -> None:
        pass

    def testWithSetNullStringEmptyString(self) -> None:
        pass

    def testWithNotSetNullString(self) -> None:
        pass

    def __every(
        self,
        csvFormat: CSVFormat,
        objects: typing.List[typing.Any],
        format: str,
        data: typing.List[str],
    ) -> None:
        pass

    # Class Methods End
