from __future__ import annotations
import re
import os
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

        in_ = io.StringIO("a~|b~|c~|d~|~|f~|")
        stringBuilder = io.StringIO()
        csvFormat = Builder.create0().setDelimiter1("~|").build()
        csvPrinter = CSVPrinter(stringBuilder, CSVFormat.EXCEL)
        csvParser = CSVParser.parse3(in_, csvFormat)

        for csvRecord in csvParser:
            self.__print_(csvRecord, csvPrinter)
            self.assertEqual("a,b,c,d,,f,", stringBuilder.getvalue())

    def testParseWithTwoCharDelimiter4(self) -> None:

        in_ = io.StringIO("a~|b~|c~|d~|~|f~~||g")
        stringBuilder = io.StringIO()
        try:
            csvPrinter = CSVPrinter(stringBuilder, CSVFormat.EXCEL)
            csvParser = CSVParser.parse3(
                in_, Builder.create0().setDelimiter1("~|").build()
            )
            for csvRecord in csvParser:
                self.__print_(csvRecord, csvPrinter)
                self.assertEqual("a,b,c,d,,f~,|g", stringBuilder.getvalue())
        finally:
            in_.close()
            stringBuilder.close()

    def testParseWithTwoCharDelimiter3(self) -> None:

        in_ = io.StringIO("a~|b~|c~|d~|~|f|")
        stringBuilder = io.StringIO()
        csvFormat = Builder.create0().setDelimiter1("~|").build()
        csvPrinter = CSVPrinter(stringBuilder, CSVFormat.EXCEL)
        csvParser = CSVParser.parse3(in_, csvFormat)

        for csvRecord in csvParser:
            self.__print_(csvRecord, csvPrinter)
            self.assertEqual("a,b,c,d,,f|", stringBuilder.getvalue())

    def testParseWithTwoCharDelimiter2(self) -> None:

        in_ = io.StringIO("a~|b~|c~|d~|~|f~")
        stringBuilder = io.StringIO()
        csvFormat = Builder.create0().setDelimiter1("~|").build()
        csvPrinter = CSVPrinter(stringBuilder, CSVFormat.EXCEL)
        csvParser = CSVParser.parse3(in_, csvFormat)

        for csvRecord in csvParser:
            self.__print_(csvRecord, csvPrinter)
            self.assertEqual("a,b,c,d,,f~", stringBuilder.getvalue())

    def testParseWithTwoCharDelimiter1(self) -> None:

        in_ = io.StringIO("a~|b~|c~|d~|~|f")
        stringBuilder = io.StringIO()
        csvFormat = Builder.create0().setDelimiter1("~|").build()
        csvPrinter = CSVPrinter(stringBuilder, CSVFormat.EXCEL)
        csvParser = CSVParser.parse3(in_, csvFormat)

        for csvRecord in csvParser:
            self.__print_(csvRecord, csvPrinter)
            self.assertEqual("a,b,c,d,,f", stringBuilder.getvalue())

    def testParseWithTriplePipeDelimiter(self) -> None:

        in_ = io.StringIO("a|||b|||c|||d||||||f")
        stringBuilder = io.StringIO()
        csvFormat = Builder.create0().setDelimiter1("|||").build()
        csvPrinter = CSVPrinter(stringBuilder, CSVFormat.EXCEL)
        csvParser = CSVParser.parse3(in_, csvFormat)

        for csvRecord in csvParser:
            self.__print_(csvRecord, csvPrinter)
            self.assertEqual("a,b,c,d,,f", stringBuilder.getvalue())

    def testParseWithSinglePipeDelimiterEndsWithDelimiter(self) -> None:

        in_ = io.StringIO("a|b|c|d||f|")
        stringBuilder = io.StringIO()
        csvFormat = Builder.create0().setDelimiter1("|").build()
        csvPrinter = CSVPrinter(stringBuilder, CSVFormat.EXCEL)
        csvParser = CSVParser.parse3(in_, csvFormat)

        for csvRecord in csvParser:
            self.__print_(csvRecord, csvPrinter)
            self.assertEqual("a,b,c,d,,f,", stringBuilder.getvalue())

    def testParseWithDoublePipeDelimiterQuoted(self) -> None:

        in_ = io.StringIO('a||"b||c"||d||||f')
        stringBuilder = io.StringIO()
        csvFormat = Builder.create0().setDelimiter1("||").build()
        csvPrinter = CSVPrinter(stringBuilder, CSVFormat.EXCEL)
        csvParser = CSVParser.parse3(in_, csvFormat)

        for csvRecord in csvParser:
            self.__print_(csvRecord, csvPrinter)
            self.assertEqual("a,b||c,d,,f", stringBuilder.getvalue())

    def testParseWithDoublePipeDelimiterEndsWithDelimiter(self) -> None:

        in_ = io.StringIO("a||b||c||d||||f||")
        stringBuilder = io.StringIO()
        csvFormat = Builder.create0().setDelimiter1("||").build()
        csvPrinter = CSVPrinter(stringBuilder, CSVFormat.EXCEL)
        csvParser = CSVParser.parse3(in_, csvFormat)

        for csvRecord in csvParser:
            self.__print_(csvRecord, csvPrinter)
            self.assertEqual("a,b,c,d,,f,", stringBuilder.getvalue())

    def testParseWithDoublePipeDelimiterDoubleCharValue(self) -> None:

        in_ = io.StringIO("a||bb||cc||dd||f")
        stringBuilder = io.StringIO()
        csvFormat = Builder.create0().setDelimiter1("||").build()
        csvPrinter = CSVPrinter(stringBuilder, CSVFormat.EXCEL)
        csvParser = CSVParser.parse3(in_, csvFormat)

        for csvRecord in csvParser:
            self.__print_(csvRecord, csvPrinter)
            self.assertEqual("a,bb,cc,dd,f", stringBuilder.getvalue())

    def testParseWithDoublePipeDelimiter(self) -> None:

        in_ = io.StringIO("a||b||c||d||||f")
        stringBuilder = io.StringIO()
        csvFormat = Builder.create0().setDelimiter1("||").build()
        csvPrinter = CSVPrinter(stringBuilder, CSVFormat.EXCEL)
        csvParser = CSVParser.parse3(in_, csvFormat)

        for csvRecord in csvParser:
            self.__print_(csvRecord, csvPrinter)
            self.assertEqual("a,b,c,d,,f", stringBuilder.getvalue())

    def testParseWithABADelimiter(self) -> None:

        in_ = io.StringIO("a|~|b|~|c|~|d|~||~|f")
        stringBuilder = io.StringIO()
        try:
            csvPrinter = CSVPrinter(stringBuilder, CSVFormat.EXCEL)
            parser = CSVParser.parse3(
                in_, Builder.create0().setDelimiter1("|~|").build()
            )
            for csvRecord in parser:
                self.__print_(csvRecord, csvPrinter)
                self.assertEqual("a,b,c,d,,f", stringBuilder.getvalue())
        finally:
            in_.close()
            stringBuilder.close()

    def __print_(self, csvRecord: CSVRecord, csvPrinter: CSVPrinter) -> None:

        for value in csvRecord:
            csvPrinter.print_(value)
