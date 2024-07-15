from __future__ import annotations
import re
import typing
from typing import *
from io import StringIO
import unittest
import pytest
import io
import unittest
from src.main.org.apache.commons.csv.CSVFormat import *
from src.main.org.apache.commons.csv.CSVParser import *
from src.main.org.apache.commons.csv.CSVPrinter import *
from src.main.org.apache.commons.csv.CSVRecord import *


class JiraCsv288Test(unittest.TestCase):

    def testParseWithTwoCharDelimiterEndsWithDelimiter(self) -> None:
        in0: typing.Union[io.TextIOWrapper, io.BufferedReader] = io.StringIO(
            "a~|b~|c~|d~|~|f~|"
        )
        stringBuilder: io.StringIO = io.StringIO()
        csvPrinter: CSVPrinter = CSVPrinter(
            stringBuilder, CSVFormat.Builder.create0().setDelimiter1("~|").build()
        )
        csvParser: CSVParser = CSVParser.parse3(
            in0, CSVFormat.Builder.create0().setDelimiter1("~|").build()
        )
        for csvRecord in csvParser:
            self.__print(csvRecord, csvPrinter)
            self.assertEqual("a,b,c,d,,f,", stringBuilder.getvalue())

    def testParseWithTwoCharDelimiter4(self) -> None:
        in_ = io.StringIO("a~|b~|c~|d~|~|f~~||g")
        stringBuilder = io.StringIO()
        with CSVPrinter(
            stringBuilder, CSVFormat.Builder.create0().setDelimiter1("~|").build()
        ) as csvPrinter:
            with CSVParser.parse3(
                in_, CSVFormat.Builder.create0().setDelimiter1("~|").build()
            ) as csvParser:
                for csvRecord in csvParser:
                    self.__print(csvRecord, csvPrinter)
                    self.assertEqual("a,b,c,d,,f~,|g", stringBuilder.getvalue())

    def testParseWithTwoCharDelimiter3(self) -> None:
        in_ = io.StringIO("a~|b~|c~|d~|~|f|")
        stringBuilder = io.StringIO()
        with CSVPrinter(
            stringBuilder, CSVFormat.Builder.create0().setDelimiter1("~|").build()
        ) as csvPrinter:
            with CSVParser.parse3(
                in_, CSVFormat.Builder.create0().setDelimiter1("~|").build()
            ) as csvParser:
                for csvRecord in csvParser:
                    self.__print(csvRecord, csvPrinter)
                    self.assertEqual("a,b,c,d,,f|", stringBuilder.getvalue())

    def testParseWithTwoCharDelimiter2(self) -> None:
        in_ = io.StringIO("a~|b~|c~|d~|~|f~")
        stringBuilder = io.StringIO()
        with CSVPrinter(
            stringBuilder, CSVFormat.Builder.create0().setDelimiter1("~|").build()
        ) as csvPrinter:
            with CSVParser.parse3(
                in_, CSVFormat.Builder.create0().setDelimiter1("~|").build()
            ) as csvParser:
                for csvRecord in csvParser:
                    self.__print(csvRecord, csvPrinter)
                    self.assertEqual("a,b,c,d,,f~", stringBuilder.getvalue())

    def testParseWithTwoCharDelimiter1(self) -> None:
        in_ = io.StringIO("a~|b~|c~|d~|~|f")
        stringBuilder = io.StringIO()
        with CSVPrinter(
            stringBuilder, CSVFormat.Builder.create0().setDelimiter1("~|").build()
        ) as csvPrinter:
            with CSVParser.parse3(
                in_, CSVFormat.Builder.create0().setDelimiter1("~|").build()
            ) as csvParser:
                for csvRecord in csvParser:
                    self.__print(csvRecord, csvPrinter)
                    self.assertEqual("a,b,c,d,,f", stringBuilder.getvalue())

    def testParseWithTriplePipeDelimiter(self) -> None:
        in_ = io.StringIO("a|||b|||c|||d||||||f")
        stringBuilder = io.StringIO()
        with CSVPrinter(
            stringBuilder, CSVFormat.Builder.create0().setDelimiter1("|||").build()
        ) as csvPrinter:
            with CSVParser.parse3(
                in_, CSVFormat.Builder.create0().setDelimiter1("|||").build()
            ) as csvParser:
                for csvRecord in csvParser:
                    self.__print(csvRecord, csvPrinter)
                    self.assertEqual("a,b,c,d,,f", stringBuilder.getvalue())

    def testParseWithSinglePipeDelimiterEndsWithDelimiter(self) -> None:
        in0: typing.Union[io.TextIOWrapper, io.BufferedReader] = io.StringIO(
            "a|b|c|d||f|"
        )
        stringBuilder: io.StringIO = io.StringIO()
        csvPrinter: CSVPrinter = CSVPrinter(
            stringBuilder, CSVFormat.Builder.create0().setDelimiter1("|").build()
        )
        csvParser: CSVParser = CSVParser.parse3(
            in0, CSVFormat.Builder.create0().setDelimiter1("|").build()
        )
        for csvRecord in csvParser:
            self.__print(csvRecord, csvPrinter)
            self.assertEqual("a,b,c,d,,f,", stringBuilder.getvalue())

    def testParseWithDoublePipeDelimiterQuoted(self) -> None:
        in_ = io.StringIO('a||"b||c"||d||||f')
        stringBuilder = io.StringIO()
        with CSVPrinter(
            stringBuilder, CSVFormat.Builder.create0().setDelimiter1("||").build()
        ) as csvPrinter:
            with CSVParser.parse3(
                in_, CSVFormat.Builder.create0().setDelimiter1("||").build()
            ) as csvParser:
                for csvRecord in csvParser:
                    self.__print(csvRecord, csvPrinter)
                    self.assertEqual("a,b||c,d,,f", stringBuilder.getvalue())

    def testParseWithDoublePipeDelimiterEndsWithDelimiter(self) -> None:
        in0: typing.Union[io.TextIOWrapper, io.BufferedReader] = io.StringIO(
            "a||b||c||d||||f||"
        )
        stringBuilder: io.StringIO = io.StringIO()
        with CSVPrinter(
            stringBuilder, CSVFormat.Builder.create0().setDelimiter1("||").build()
        ) as csvPrinter:
            with CSVParser.parse3(
                in0, CSVFormat.Builder.create0().setDelimiter1("||").build()
            ) as csvParser:
                for csvRecord in csvParser:
                    self.__print(csvRecord, csvPrinter)
                    self.assertEqual("a,b,c,d,,f,", stringBuilder.getvalue())

    def testParseWithDoublePipeDelimiterDoubleCharValue(self) -> None:
        in0: typing.Union[io.TextIOWrapper, io.BufferedReader] = io.StringIO(
            "a||bb||cc||dd||f"
        )
        stringBuilder: io.StringIO = io.StringIO()
        csvPrinter: CSVPrinter = CSVPrinter(
            stringBuilder, CSVFormat.Builder.create0().setDelimiter1("||").build()
        )
        csvParser: CSVParser = CSVParser.parse3(
            in0, CSVFormat.Builder.create0().setDelimiter1("||").build()
        )
        for csvRecord in csvParser:
            self.__print(csvRecord, csvPrinter)
            self.assertEqual("a,bb,cc,dd,f", stringBuilder.getvalue())

    def testParseWithDoublePipeDelimiter(self) -> None:
        in0 = io.StringIO("a||b||c||d||||f")
        stringBuilder = io.StringIO()
        with CSVPrinter(
            stringBuilder, CSVFormat.Builder.create0().setDelimiter1("||").build()
        ) as csvPrinter:
            with CSVParser.parse3(
                in0, CSVFormat.Builder.create0().setDelimiter1("||").build()
            ) as csvParser:
                for csvRecord in csvParser:
                    self.__print(csvRecord, csvPrinter)
                    self.assertEqual("a,b,c,d,,f", stringBuilder.getvalue())

    def testParseWithABADelimiter(self) -> None:

        pass  # LLM could not translate this method

    def __print(self, csvRecord: CSVRecord, csvPrinter: CSVPrinter) -> None:
        for value in csvRecord:
            csvPrinter.print(value)
