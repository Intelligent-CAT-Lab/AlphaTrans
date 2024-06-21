from __future__ import annotations
import re
import unittest
import pytest
import io
from src.main.org.apache.commons.csv.CSVFormat import *
from src.main.org.apache.commons.csv.CSVParser import *
from src.main.org.apache.commons.csv.CSVPrinter import *
from src.main.org.apache.commons.csv.CSVRecord import *


class JiraCsv288Test(unittest.TestCase):


    @pytest.mark.test
    def testParseWithTwoCharDelimiterEndsWithDelimiter(self) -> None:
        
        in_ = io.StringIO("a~|b~|c~|d~|~|f~|")
        stringBuilder = io.StringIO()
        csvFormat = CSVFormat.Builder.create0().setDelimiter1("~|").build()
        csvPrinter = CSVPrinter(stringBuilder, csvFormat)
        csvParser = CSVParser.parse3(in_, csvFormat)

        for csvRecord in csvParser:
            self.__print(csvRecord, csvPrinter)
            self.assertEqual("a,b,c,d,,f,", stringBuilder.getvalue())

    @pytest.mark.test
    def testParseWithTwoCharDelimiter4(self) -> None:
        
        in_ = io.StringIO("a~|b~|c~|d~|~|f~~||g")
        stringBuilder = io.StringIO()
        csvFormat = CSVFormat.Builder.create0().setDelimiter1("~|").build()
        csvPrinter = CSVPrinter(stringBuilder, csvFormat)
        csvParser = CSVParser.parse3(in_, csvFormat)

        for csvRecord in csvParser:
            self.__print(csvRecord, csvPrinter)
            self.assertEqual("a,b,c,d,,f~,|g", stringBuilder.getvalue())

    @pytest.mark.test
    def testParseWithTwoCharDelimiter3(self) -> None:
        
        in_ = io.StringIO("a~|b~|c~|d~|~|f|")
        stringBuilder = io.StringIO()
        csvFormat = CSVFormat.Builder.create0().setDelimiter1("~|").build()
        csvPrinter = CSVPrinter(stringBuilder, csvFormat)
        csvParser = CSVParser.parse3(in_, csvFormat)

        for csvRecord in csvParser:
            self.__print(csvRecord, csvPrinter)
            self.assertEqual("a,b,c,d,,f|", stringBuilder.getvalue())

    @pytest.mark.test
    def testParseWithTwoCharDelimiter2(self) -> None:
        
        in_ = io.StringIO("a~|b~|c~|d~|~|f~")
        stringBuilder = io.StringIO()
        csvFormat = CSVFormat.Builder.create0().setDelimiter1("~|").build()
        csvPrinter = CSVPrinter(stringBuilder, csvFormat)
        csvParser = CSVParser.parse3(in_, csvFormat)

        for csvRecord in csvParser:
            self.__print(csvRecord, csvPrinter)
            self.assertEqual("a,b,c,d,,f~", stringBuilder.getvalue())

    @pytest.mark.test
    def testParseWithTwoCharDelimiter1(self) -> None:
        
        in_ = io.StringIO("a~|b~|c~|d~|~|f")
        stringBuilder = io.StringIO()
        csvFormat = CSVFormat.Builder.create0().setDelimiter1("~|").build()
        csvPrinter = CSVPrinter(stringBuilder, csvFormat)
        csvParser = CSVParser.parse3(in_, csvFormat)

        for csvRecord in csvParser:
            self.__print(csvRecord, csvPrinter)
            self.assertEqual("a,b,c,d,,f", stringBuilder.getvalue())

    @pytest.mark.test
    def testParseWithTriplePipeDelimiter(self) -> None:
        
        in_ = io.StringIO("a|||b|||c|||d||||||f")
        stringBuilder = io.StringIO()
        try:
            csvPrinter = CSVPrinter(stringBuilder, CSVFormat.Builder.create0().setDelimiter1("|||").build())
            csvParser = CSVParser.parse3(in_, CSVFormat.Builder.create0().setDelimiter1("|||").build())
            for csvRecord in csvParser:
                self.__print(csvRecord, csvPrinter)
                self.assertEqual("a,b,c,d,,f", stringBuilder.getvalue())
        finally:
            in_.close()
            stringBuilder.close()

    @pytest.mark.test
    def testParseWithSinglePipeDelimiterEndsWithDelimiter(self) -> None:
        
        in_ = io.StringIO("a|b|c|d||f|")
        stringBuilder = io.StringIO()
        csvFormat = CSVFormat.Builder.create0().setDelimiter1("|").build()
        csvPrinter = CSVPrinter(stringBuilder, csvFormat)
        csvParser = CSVParser.parse3(in_, csvFormat)

        for csvRecord in csvParser:
            self.__print(csvRecord, csvPrinter)
            self.assertEqual("a,b,c,d,,f,", stringBuilder.getvalue())

    @pytest.mark.test
    def testParseWithDoublePipeDelimiterQuoted(self) -> None:
        
        in_ = io.StringIO("a||\"b||c\"||d||||f")
        string_builder = io.StringIO()
        try:
            csv_printer = CSVPrinter(string_builder, CSVFormat.Builder.create0().setDelimiter1("||").build())
            csv_parser = CSVParser.parse3(in_, CSVFormat.Builder.create0().setDelimiter1("||").build())
            for csv_record in csv_parser:
                self.__print(csv_record, csv_printer)
                self.assertEqual("a,b||c,d,,f", string_builder.getvalue())
        finally:
            in_.close()
            string_builder.close()

    @pytest.mark.test
    def testParseWithDoublePipeDelimiterEndsWithDelimiter(self) -> None:
        
        in_ = io.StringIO("a||b||c||d||||f||")
        string_builder = io.StringIO()
        try:
            csv_printer = CSVPrinter(string_builder, CSVFormat.Builder.create0().setDelimiter1("||").build())
            csv_parser = CSVParser.parse3(in_, CSVFormat.Builder.create0().setDelimiter1("||").build())
            for csv_record in csv_parser:
                self.__print(csv_record, csv_printer)
                self.assertEqual("a,b,c,d,,f,", string_builder.getvalue())
        finally:
            in_.close()
            string_builder.close()

    @pytest.mark.test
    def testParseWithDoublePipeDelimiterDoubleCharValue(self) -> None:
        
        in_ = io.StringIO("a||bb||cc||dd||f")
        stringBuilder = io.StringIO()
        try:
            csvPrinter = CSVPrinter(stringBuilder, CSVFormat.Builder.create0().setDelimiter1("||").build())
            csvParser = CSVParser.parse3(in_, CSVFormat.Builder.create0().setDelimiter1("||").build())
            for csvRecord in csvParser:
                self.__print(csvRecord, csvPrinter)
                self.assertEqual("a,bb,cc,dd,f", stringBuilder.getvalue())
        finally:
            in_.close()
            stringBuilder.close()

    @pytest.mark.test
    def testParseWithDoublePipeDelimiter(self) -> None:
        
        in_ = io.StringIO("a||b||c||d||||f")
        stringBuilder = io.StringIO()
        csvFormat = CSVFormat.Builder.create0().setDelimiter1("||").build()

        csvPrinter = CSVPrinter(stringBuilder, csvFormat)
        csvParser = CSVParser.parse3(in_, csvFormat)

        for csvRecord in csvParser:
            self.__print(csvRecord, csvPrinter)
            self.assertEqual("a,b,c,d,,f", stringBuilder.getvalue())

    @pytest.mark.test
    def testParseWithABADelimiter(self) -> None:
        
        in_ = io.StringIO("a|~|b|~|c|~|d|~||~|f")
        stringBuilder = io.StringIO()
        try:
            csvPrinter = CSVPrinter(stringBuilder, CSVFormat.Builder.create0().setDelimiter1("|~|").build())
            parser = CSVParser.parse3(in_, CSVFormat.Builder.create0().setDelimiter1("|~|").build())
            for csvRecord in parser:
                self.__print(csvRecord, csvPrinter)
                self.assertEqual("a,b,c,d,,f", stringBuilder.getvalue())
        finally:
            in_.close()
            stringBuilder.close()
    def __print(self, csvRecord: CSVRecord, csvPrinter: CSVPrinter) -> None:
        
        if csvPrinter.format is None:
            raise ValueError("CSVFormat is not set")

        if csvPrinter.appendable is None:
            raise ValueError("Appendable is not set")

        for value in csvRecord:
            csvPrinter.print(value)
