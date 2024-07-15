from __future__ import annotations
import re
import os
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
        try:
            csvPrinter = CSVPrinter(
                stringBuilder, CSVFormat.Builder.create0().setDelimiter1("~|").build()
            )
            csvParser = CSVParser.parse3(
                in_, CSVFormat.Builder.create0().setDelimiter1("~|").build()
            )
            for csvRecord in csvParser:
                self.__print(csvRecord, csvPrinter)
                self.assertEqual("a,b,c,d,,f,", stringBuilder.getvalue())
        finally:
            in_.close()
            stringBuilder.close()

    def testParseWithTwoCharDelimiter4(self) -> None:

        in_ = io.StringIO("a~|b~|c~|d~|~|f~~||g")
        string_builder = io.StringIO()
        try:
            csv_printer = CSVPrinter(string_builder, CSVFormat.EXCEL)
            csv_parser = CSVParser.parse3(
                in_, CSVFormat.Builder.create0().setDelimiter1("~|").build()
            )
            for csv_record in csv_parser:
                self.__print(csv_record, csv_printer)
                self.assertEqual("a,b,c,d,,f~,|g", string_builder.getvalue())
        finally:
            in_.close()
            string_builder.close()

    def testParseWithTwoCharDelimiter3(self) -> None:

        in_ = io.StringIO("a~|b~|c~|d~|~|f|")
        string_builder = io.StringIO()
        try:
            csv_printer = CSVPrinter(
                string_builder, CSVFormat.Builder.create0().setDelimiter1("~|").build()
            )
            csv_parser = CSVParser.parse3(
                in_, CSVFormat.Builder.create0().setDelimiter1("~|").build()
            )
            for csv_record in csv_parser:
                self.__print(csv_record, csv_printer)
                self.assertEqual("a,b,c,d,,f|", string_builder.getvalue())
        finally:
            in_.close()
            string_builder.close()

    def testParseWithTwoCharDelimiter2(self) -> None:

        in_ = io.StringIO("a~|b~|c~|d~|~|f~")
        string_builder = io.StringIO()
        try:
            csv_printer = CSVPrinter(
                string_builder, CSVFormat.Builder.create0().setDelimiter1("~|").build()
            )
            csv_parser = CSVParser.parse3(
                in_, CSVFormat.Builder.create0().setDelimiter1("~|").build()
            )
            for csv_record in csv_parser:
                self.__print(csv_record, csv_printer)
                self.assertEqual("a,b,c,d,,f~", string_builder.getvalue())
        finally:
            in_.close()
            string_builder.close()

    def testParseWithTwoCharDelimiter1(self) -> None:

        in_ = io.StringIO("a~|b~|c~|d~|~|f")
        string_builder = io.StringIO()
        try:
            csv_printer = CSVPrinter(
                string_builder, CSVFormat.Builder.create0().setDelimiter1("~|").build()
            )
            csv_parser = CSVParser.parse3(
                in_, CSVFormat.Builder.create0().setDelimiter1("~|").build()
            )
            for csv_record in csv_parser:
                self.__print(csv_record, csv_printer)
                self.assertEqual("a,b,c,d,,f", string_builder.getvalue())
        finally:
            in_.close()
            string_builder.close()

    def testParseWithTriplePipeDelimiter(self) -> None:

        in_ = io.StringIO("a|||b|||c|||d||||||f")
        stringBuilder = io.StringIO()
        try:
            csvPrinter = CSVPrinter(
                stringBuilder, CSVFormat.Builder.create0().setDelimiter1("|||").build()
            )
            csvParser = CSVParser.parse3(
                in_, CSVFormat.Builder.create0().setDelimiter1("|||").build()
            )
            for csvRecord in csvParser:
                self.__print(csvRecord, csvPrinter)
                self.assertEqual("a,b,c,d,,f", stringBuilder.getvalue())
        finally:
            in_.close()
            stringBuilder.close()

    def testParseWithSinglePipeDelimiterEndsWithDelimiter(self) -> None:

        in_ = io.StringIO("a|b|c|d||f|")
        stringBuilder = io.StringIO()
        try:
            csvPrinter = CSVPrinter(
                stringBuilder, CSVFormat.Builder.create0().setDelimiter1("|").build()
            )
            csvParser = CSVParser.parse3(
                in_, CSVFormat.Builder.create0().setDelimiter1("|").build()
            )
            for csvRecord in csvParser:
                self.__print(csvRecord, csvPrinter)
                self.assertEqual("a,b,c,d,,f,", stringBuilder.getvalue())
        finally:
            in_.close()
            stringBuilder.close()

    def testParseWithDoublePipeDelimiterQuoted(self) -> None:

        in_ = io.StringIO('a||"b||c"||d||||f')
        stringBuilder = io.StringIO()
        try:
            csvPrinter = CSVPrinter(
                stringBuilder, CSVFormat.Builder.create0().setDelimiter1("||").build()
            )
            csvParser = CSVParser.parse3(
                in_, CSVFormat.Builder.create0().setDelimiter1("||").build()
            )
            for csvRecord in csvParser:
                self.__print(csvRecord, csvPrinter)
                self.assertEqual("a,b||c,d,,f", stringBuilder.getvalue())
        finally:
            in_.close()
            stringBuilder.close()

    def testParseWithDoublePipeDelimiterEndsWithDelimiter(self) -> None:

        from io import StringIO
        from src.main.org.apache.commons.csv.CSVFormat import CSVFormat
        from src.main.org.apache.commons.csv.CSVParser import CSVParser
        from src.main.org.apache.commons.csv.CSVPrinter import CSVPrinter
        from src.main.org.apache.commons.csv.CSVRecord import CSVRecord

        in_ = StringIO("a||b||c||d||||f||")
        string_builder = StringIO()
        csv_format = CSVFormat.Builder.create0().setDelimiter1("||").build()

        with CSVPrinter(string_builder, csv_format) as csv_printer, CSVParser.parse3(
            in_, csv_format
        ) as csv_parser:
            for csv_record in csv_parser:
                self.__print(csv_record, csv_printer)
                self.assertEqual("a,b,c,d,,f,", string_builder.getvalue())

    def testParseWithDoublePipeDelimiterDoubleCharValue(self) -> None:

        in_ = io.StringIO("a||bb||cc||dd||f")
        stringBuilder = io.StringIO()
        try:
            csvPrinter = CSVPrinter(stringBuilder, CSVFormat.EXCEL)
            csvParser = CSVParser.parse3(
                in_, CSVFormat.Builder.create0().setDelimiter1("||").build()
            )
            for csvRecord in csvParser:
                self.__print(csvRecord, csvPrinter)
                self.assertEqual("a,bb,cc,dd,f", stringBuilder.getvalue())
        finally:
            in_.close()
            stringBuilder.close()

    def testParseWithDoublePipeDelimiter(self) -> None:

        in_ = io.StringIO("a||b||c||d||||f")
        stringBuilder = io.StringIO()
        try:
            csvPrinter = CSVPrinter(stringBuilder, CSVFormat.EXCEL)
            csvParser = CSVParser.parse3(
                in_, CSVFormat.Builder.create0().setDelimiter1("||").build()
            )
            for csvRecord in csvParser:
                self.__print(csvRecord, csvPrinter)
                self.assertEqual("a,b,c,d,,f", stringBuilder.getvalue())
        finally:
            in_.close()
            stringBuilder.close()

    def testParseWithABADelimiter(self) -> None:

        in_ = io.StringIO("a|~|b|~|c|~|d|~||~|f")
        stringBuilder = io.StringIO()
        try:
            csvPrinter = CSVPrinter(
                stringBuilder, CSVFormat.Builder.create0().setDelimiter1("|~|").build()
            )
            parser = CSVParser.parse3(
                in_, CSVFormat.Builder.create0().setDelimiter1("|~|").build()
            )
            for csvRecord in parser:
                self.__print(csvRecord, csvPrinter)
                self.assertEqual("a,b,c,d,,f", stringBuilder.getvalue())
        finally:
            in_.close()
            stringBuilder.close()

    def __print(self, csvRecord: CSVRecord, csvPrinter: CSVPrinter) -> None:
        for value in csvRecord:
            csvPrinter.print(value)
