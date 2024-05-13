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
    __objects1: typing.List[typing.Any] = ""  # LLM could not translate field
    __objects2: typing.List[typing.Any] = ""  # LLM could not translate field
    # Class Fields End

    # Class Methods Begin
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

    def testWithNotSetNullString(self) -> None:

        self.__every(
            CSVFormat.DEFAULT,
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
        assert source == format
        with csvFormat.parse(StringIO(source)) as csvParser:
            csvRecord = csvParser.iterator().next()
            for i in range(len(data)):
                assert csvRecord.get1(i) == data[i]

    # Class Methods End
