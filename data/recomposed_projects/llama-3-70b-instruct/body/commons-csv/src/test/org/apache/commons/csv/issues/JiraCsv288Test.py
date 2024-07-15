from __future__ import annotations
import re
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
        with io.StringIO("a~|b~|c~|d~|~|f~|") as in_:
            with io.StringIO() as stringBuilder:
                with CSVPrinter(
                    stringBuilder,
                    CSVFormat.Builder.create0().setDelimiter1("~|").build(),
                ) as csvPrinter:
                    with CSVParser.parse3(
                        in_, CSVFormat.Builder.create0().setDelimiter1("~|").build()
                    ) as csvParser:
                        for csvRecord in csvParser:
                            self.__print(csvRecord, csvPrinter)
                            self.assertEqual("a,b,c,d,,f,", stringBuilder.getvalue())

    def testParseWithTwoCharDelimiter4(self) -> None:
        with io.StringIO("a~|b~|c~|d~|~|f~~||g") as in_:
            with io.StringIO() as stringBuilder:
                with CSVPrinter(
                    stringBuilder,
                    CSVFormat.Builder.create0().setDelimiter1("~|").build(),
                ) as csvPrinter:
                    with CSVParser.parse3(
                        in_, CSVFormat.Builder.create0().setDelimiter1("~|").build()
                    ) as csvParser:
                        for csvRecord in csvParser:
                            self.__print(csvRecord, csvPrinter)
                            self.assertEqual("a,b,c,d,,f~,|g", stringBuilder.getvalue())

    def testParseWithTwoCharDelimiter3(self) -> None:
        with io.StringIO("a~|b~|c~|d~|~|f|") as in_:
            with io.StringIO() as out:
                with CSVPrinter(
                    out, CSVFormat.Builder.create0().setDelimiter1("~|").build()
                ) as csvPrinter:
                    with CSVParser.parse3(
                        in_, CSVFormat.Builder.create0().setDelimiter1("~|").build()
                    ) as csvParser:
                        for csvRecord in csvParser:
                            self.__print(csvRecord, csvPrinter)
                            self.assertEqual("a,b,c,d,,f|", out.getvalue())

    def testParseWithTwoCharDelimiter2(self) -> None:
        with io.StringIO("a~|b~|c~|d~|~|f~") as in_:
            with io.StringIO() as out:
                with CSVPrinter(
                    out, CSVFormat.Builder.create0().setDelimiter1("~|").build()
                ) as csvPrinter:
                    with CSVParser.parse3(
                        in_, CSVFormat.Builder.create0().setDelimiter1("~|").build()
                    ) as csvParser:
                        for csvRecord in csvParser:
                            self.__print(csvRecord, csvPrinter)
                            self.assertEqual("a,b,c,d,,f~", out.getvalue())

    def testParseWithTwoCharDelimiter1(self) -> None:
        with io.StringIO("a~|b~|c~|d~|~|f") as in_:
            with io.StringIO() as out:
                with CSVPrinter(
                    out, CSVFormat.Builder.create0().setDelimiter1("~|").build()
                ) as csvPrinter:
                    with CSVParser.parse3(
                        in_, CSVFormat.Builder.create0().setDelimiter1("~|").build()
                    ) as csvParser:
                        for csvRecord in csvParser:
                            self.__print(csvRecord, csvPrinter)
                            self.assertEqual("a,b,c,d,,f", out.getvalue())

    def testParseWithTriplePipeDelimiter(self) -> None:
        with io.StringIO("a|||b|||c|||d||||||f") as in_:
            with io.StringIO() as out:
                with CSVPrinter(
                    out, CSVFormat.Builder.create0().setDelimiter1("|||").build()
                ) as csvPrinter:
                    with CSVParser.parse3(
                        in_, CSVFormat.Builder.create0().setDelimiter1("|||").build()
                    ) as csvParser:
                        for csvRecord in csvParser:
                            self.__print(csvRecord, csvPrinter)
                            self.assertEqual("a,b,c,d,,f", out.getvalue())

    def testParseWithSinglePipeDelimiterEndsWithDelimiter(self) -> None:
        with io.StringIO("a|b|c|d||f|") as in_:
            with io.StringIO() as out:
                with CSVPrinter(
                    out, CSVFormat.Builder.create0().setDelimiter1("|").build()
                ) as csvPrinter:
                    with CSVParser.parse3(
                        in_, CSVFormat.Builder.create0().setDelimiter1("|").build()
                    ) as csvParser:
                        for csvRecord in csvParser:
                            self.__print(csvRecord, csvPrinter)
                            self.assertEqual("a,b,c,d,,f,", out.getvalue())

    def testParseWithDoublePipeDelimiterQuoted(self) -> None:
        with io.StringIO('a||"b||c"||d||||f') as in_:
            with CSVPrinter(
                io.StringIO(), CSVFormat.Builder.create0().setDelimiter1("||").build()
            ) as csvPrinter:
                with CSVParser.parse3(
                    in_, CSVFormat.Builder.create0().setDelimiter1("||").build()
                ) as csvParser:
                    for csvRecord in csvParser:
                        self.__print(csvRecord, csvPrinter)
                        self.assertEqual("a,b||c,d,,f", csvPrinter.toString())

    def testParseWithDoublePipeDelimiterEndsWithDelimiter(self) -> None:
        with io.StringIO("a||b||c||d||||f||") as in_:
            with CSVPrinter(
                io.StringIO(), CSVFormat.Builder.create0().setDelimiter1("||").build()
            ) as csvPrinter:
                with CSVParser.parse3(
                    in_, CSVFormat.Builder.create0().setDelimiter1("||").build()
                ) as csvParser:
                    for csvRecord in csvParser:
                        self.__print(csvRecord, csvPrinter)
                        self.assertEqual("a,b,c,d,,f,", csvPrinter.toString())

    def testParseWithDoublePipeDelimiterDoubleCharValue(self) -> None:
        in1: Reader = StringReader("a||bb||cc||dd||f")
        stringBuilder: StringBuilder = StringBuilder()
        with CSVPrinter(
            stringBuilder, CSVFormat.Builder.create0().setDelimiter1("||").build()
        ) as csvPrinter:
            with CSVParser.parse3(
                in1, CSVFormat.Builder.create0().setDelimiter1("||").build()
            ) as csvParser:
                for csvRecord in csvParser:
                    self.__print(csvRecord, csvPrinter)
                    self.assertEqual("a,bb,cc,dd,f", stringBuilder.toString())

    def testParseWithDoublePipeDelimiter(self) -> None:
        with io.StringIO("a||b||c||d||||f") as in_:
            with io.StringIO() as out:
                with CSVPrinter(
                    out, CSVFormat.Builder.create0().setDelimiter1("||").build()
                ) as csvPrinter:
                    with CSVParser.parse3(
                        in_, CSVFormat.Builder.create0().setDelimiter1("||").build()
                    ) as csvParser:
                        for csvRecord in csvParser:
                            self.__print(csvRecord, csvPrinter)
                            self.assertEqual("a,b,c,d,,f", out.getvalue())

    def testParseWithABADelimiter(self) -> None:
        in1: Reader = StringReader("a|~|b|~|c|~|d|~||~|f")
        stringBuilder: StringBuilder = StringBuilder()
        with CSVPrinter(
            stringBuilder, CSVFormat.Builder.create0().setDelimiter1("|~|").build()
        ) as csvPrinter:
            with CSVParser.parse3(
                in1, CSVFormat.Builder.create0().setDelimiter1("|~|").build()
            ) as parser:
                for csvRecord in parser:
                    self.__print(csvRecord, csvPrinter)
                    self.assertEqual("a,b,c,d,,f", stringBuilder.toString())

    def __print(self, csvRecord: CSVRecord, csvPrinter: CSVPrinter) -> None:
        for value in csvRecord:
            csvPrinter.print(value)
