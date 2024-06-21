from __future__ import annotations
import re
import unittest
import pytest
import io
import typing
from typing import *
from src.main.org.apache.commons.csv.CSVFormat import *
from src.main.org.apache.commons.csv.CSVParser import *
from src.main.org.apache.commons.csv.CSVRecord import *
from src.main.org.apache.commons.csv.QuoteMode import *


class JiraCsv93Test(unittest.TestCase):

    __objects2: typing.List[typing.Any] = []

    __objects1: typing.List[typing.Any] = []

    @pytest.mark.test
    def testWithSetNullStringNULL(self) -> None:

        self.__every(
            CSVFormat.DEFAULT.builder().setNullString("NULL").build(),
            self.__objects2,
            'abc,NULL,NULL,"a,b,c",123',
            ["abc", None, None, "a,b,c", "123"],
        )
        self.__every(
            CSVFormat.DEFAULT.builder()
            .setNullString("NULL")
            .setQuoteMode(QuoteMode.ALL)
            .build(),
            self.__objects2,
            '"abc","NULL","NULL","a,b,c","123"',
            ["abc", None, None, "a,b,c", "123"],
        )
        self.__every(
            CSVFormat.DEFAULT.builder()
            .setNullString("NULL")
            .setQuoteMode(QuoteMode.ALL_NON_NULL)
            .build(),
            self.__objects2,
            '"abc","NULL",NULL,"a,b,c","123"',
            ["abc", "NULL", None, "a,b,c", "123"],
        )
        self.__every(
            CSVFormat.DEFAULT.builder()
            .setNullString("NULL")
            .setQuoteMode(QuoteMode.MINIMAL)
            .build(),
            self.__objects2,
            'abc,NULL,NULL,"a,b,c",123',
            ["abc", None, None, "a,b,c", "123"],
        )
        self.__every(
            CSVFormat.DEFAULT.builder()
            .setNullString("NULL")
            .setEscape0("?")
            .setQuoteMode(QuoteMode.NONE)
            .build(),
            self.__objects2,
            "abc,NULL,NULL,a?,b?,c,123",
            ["abc", None, None, "a,b,c", "123"],
        )
        self.__every(
            CSVFormat.DEFAULT.builder()
            .setNullString("NULL")
            .setQuoteMode(QuoteMode.NON_NUMERIC)
            .build(),
            self.__objects2,
            '"abc","NULL",NULL,"a,b,c",123',
            ["abc", "NULL", None, "a,b,c", "123"],
        )

    @pytest.mark.test
    def testWithSetNullStringEmptyString(self) -> None:

        self.__every(
            CSVFormat.DEFAULT.builder().setNullString("").build(),
            self.__objects1,
            'abc,,,"a,b,c",123',
            ["abc", None, None, "a,b,c", "123"],
        )
        self.__every(
            CSVFormat.DEFAULT.builder()
            .setNullString("")
            .setQuoteMode(QuoteMode.ALL)
            .build(),
            self.__objects1,
            '"abc","","","a,b,c","123"',
            ["abc", None, None, "a,b,c", "123"],
        )
        self.__every(
            CSVFormat.DEFAULT.builder()
            .setNullString("")
            .setQuoteMode(QuoteMode.ALL_NON_NULL)
            .build(),
            self.__objects1,
            '"abc","",,"a,b,c","123"',
            ["abc", "", None, "a,b,c", "123"],
        )
        self.__every(
            CSVFormat.DEFAULT.builder()
            .setNullString("")
            .setQuoteMode(QuoteMode.MINIMAL)
            .build(),
            self.__objects1,
            'abc,,,"a,b,c",123',
            ["abc", None, None, "a,b,c", "123"],
        )
        self.__every(
            CSVFormat.DEFAULT.builder()
            .setNullString("")
            .setEscape0("?")
            .setQuoteMode(QuoteMode.NONE)
            .build(),
            self.__objects1,
            "abc,,,a?,b?,c,123",
            ["abc", None, None, "a,b,c", "123"],
        )
        self.__every(
            CSVFormat.DEFAULT.builder()
            .setNullString("")
            .setQuoteMode(QuoteMode.NON_NUMERIC)
            .build(),
            self.__objects1,
            '"abc","",,"a,b,c",123',
            ["abc", "", None, "a,b,c", "123"],
        )

    @pytest.mark.test
    def testWithNotSetNullString(self) -> None:

        self.__every(
            CSVFormat.DEFAULT.builder().build(),
            self.__objects1,
            'abc,,,"a,b,c",123',
            ["abc", "", "", "a,b,c", "123"],
        )
        self.__every(
            CSVFormat.DEFAULT.builder().setQuoteMode(QuoteMode.ALL).build(),
            self.__objects1,
            '"abc","",,"a,b,c","123"',
            ["abc", "", "", "a,b,c", "123"],
        )
        self.__every(
            CSVFormat.DEFAULT.builder().setQuoteMode(QuoteMode.ALL_NON_NULL).build(),
            self.__objects1,
            '"abc","",,"a,b,c","123"',
            ["abc", "", None, "a,b,c", "123"],
        )
        self.__every(
            CSVFormat.DEFAULT.builder().setQuoteMode(QuoteMode.MINIMAL).build(),
            self.__objects1,
            'abc,,,"a,b,c",123',
            ["abc", "", "", "a,b,c", "123"],
        )
        self.__every(
            CSVFormat.DEFAULT.builder()
            .setEscape0("?")
            .setQuoteMode(QuoteMode.NONE)
            .build(),
            self.__objects1,
            "abc,,,a?,b?,c,123",
            ["abc", "", "", "a,b,c", "123"],
        )
        self.__every(
            CSVFormat.DEFAULT.builder().setQuoteMode(QuoteMode.NON_NUMERIC).build(),
            self.__objects1,
            '"abc","",,"a,b,c",123',
            ["abc", "", None, "a,b,c", "123"],
        )

    def __every(
        self,
        csvFormat: CSVFormat,
        objects: typing.List[typing.Any],
        format: str,
        data: typing.List[str],
    ) -> None:

        source = csvFormat.format(objects)
        self.assertEqual(format, source)
        csvParser = csvFormat.parse(io.StringIO(source))
        csvRecord = next(csvParser.iterator())
        for i in range(len(data)):
            self.assertEqual(csvRecord.get1(i), data[i])
