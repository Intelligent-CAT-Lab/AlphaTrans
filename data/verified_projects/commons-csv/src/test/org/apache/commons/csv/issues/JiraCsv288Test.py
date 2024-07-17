import pytest

from src.main.org.apache.commons.csv.CSVRecord import *
from src.main.org.apache.commons.csv.CSVPrinter import *
from src.main.org.apache.commons.csv.CSVParser import *
from src.main.org.apache.commons.csv.CSVFormat import *
import unittest
import io


class JiraCsv288Test(unittest.TestCase):

    def __print(self, csvRecord, csvPrinter) -> None:
        csvRecordIterator = csvRecord.iterator()
        while True:
            try:
                value = next(csvRecordIterator)
                csvPrinter.print(value)
            except StopIteration:
                break
    
    
    @pytest.mark.test
    def testParseWithABADelimiter(self) -> None:
        in_ = io.StringIO("a|~|b|~|c|~|d|~||~|f")
        stringBuilder = []
        csvPrinter = CSVPrinter(stringBuilder, CSVFormat.EXCEL)
        parser = CSVParser.parse3(
            in_,
            CSVFormat.Builder.create0().setDelimiter1("|~|").build()
        )
        try:
            parserIterator = parser.iterator()
            while True:
                try:
                    csvRecord = parserIterator.next()
                    self.__print(csvRecord, csvPrinter)
                    self.assertEqual("a,b,c,d,,f", ''.join(stringBuilder))
                except StopIteration:
                    break
        finally:
            csvPrinter.close()
            parser.close()
                

    @pytest.mark.test
    def testParseWithDoublePipeDelimiter(self) -> None:
        in_ = io.StringIO("a||b||c||d||||f")
        stringBuilder = []
        csvPrinter = CSVPrinter(stringBuilder, CSVFormat.EXCEL)
        parser = CSVParser.parse3(
            in_,
            CSVFormat.Builder.create0().setDelimiter1("||").build()
        )
        try:
            parserIterator = parser.iterator()
            while True:
                try:
                    csvRecord = parserIterator.next()
                    self.__print(csvRecord, csvPrinter)
                    self.assertEqual("a,b,c,d,,f", ''.join(stringBuilder))
                except StopIteration:
                    break
        finally:
            csvPrinter.close()
            parser.close()
    
    
    @pytest.mark.test
    def testParseWithDoublePipeDelimiterDoubleCharValue(self) -> None:
        in_ = io.StringIO("a||bb||cc||dd||f")
        stringBuilder = []
        csvPrinter = CSVPrinter(stringBuilder, CSVFormat.EXCEL)
        parser = CSVParser.parse3(
            in_,
            CSVFormat.Builder.create0().setDelimiter1("||").build()
        )
        try:
            parserIterator = parser.iterator()
            while True:
                try:
                    csvRecord = parserIterator.next()
                    self.__print(csvRecord, csvPrinter)
                    self.assertEqual("a,bb,cc,dd,f", ''.join(stringBuilder))
                except StopIteration:
                    break
        finally:
            csvPrinter.close()
            parser.close()

    
    @pytest.mark.test
    def testParseWithDoublePipeDelimiterEndsWithDelimiter(self) -> None:
        in_ = io.StringIO("a||b||c||d||||f||")
        stringBuilder = []
        csvPrinter = CSVPrinter(stringBuilder, CSVFormat.EXCEL)
        parser = CSVParser.parse3(
            in_,
            CSVFormat.Builder.create0().setDelimiter1("||").build()
        )
        try:
            parserIterator = parser.iterator()
            while True:
                try:
                    csvRecord = parserIterator.next()
                    self.__print(csvRecord, csvPrinter)
                    self.assertEqual("a,b,c,d,,f,", ''.join(stringBuilder))
                except StopIteration:
                    break
        finally:
            csvPrinter.close()
            parser.close()

    
    @pytest.mark.test
    def testParseWithDoublePipeDelimiterQuoted(self) -> None:
        in_ = io.StringIO("a||\"b||c\"||d||||f")
        stringBuilder = []
        csvPrinter = CSVPrinter(stringBuilder, CSVFormat.EXCEL)
        parser = CSVParser.parse3(
            in_,
            CSVFormat.Builder.create0().setDelimiter1("||").build()
        )
        try:
            parserIterator = parser.iterator()
            while True:
                try:
                    csvRecord = parserIterator.next()
                    self.__print(csvRecord, csvPrinter)
                    self.assertEqual("a,b||c,d,,f", ''.join(stringBuilder))
                except StopIteration:
                    break
        finally:
            csvPrinter.close()
            parser.close()
    
    
    @pytest.mark.test
    def testParseWithSinglePipeDelimiterEndsWithDelimiter(self) -> None:
        in_ = io.StringIO("a|b|c|d||f|")
        stringBuilder = []
        csvPrinter = CSVPrinter(stringBuilder, CSVFormat.EXCEL)
        parser = CSVParser.parse3(
            in_,
            CSVFormat.Builder.create0().setDelimiter1("|").build()
        )
        try:
            parserIterator = parser.iterator()
            while True:
                try:
                    csvRecord = parserIterator.next()
                    self.__print(csvRecord, csvPrinter)
                    self.assertEqual("a,b,c,d,,f,", ''.join(stringBuilder))
                except StopIteration:
                    break
        finally:
            csvPrinter.close()
            parser.close()

    
    @pytest.mark.test
    def testParseWithTriplePipeDelimiter(self) -> None:
        in_ = io.StringIO("a|||b|||c|||d||||||f")
        stringBuilder = []
        csvPrinter = CSVPrinter(stringBuilder, CSVFormat.EXCEL)
        parser = CSVParser.parse3(
            in_,
            CSVFormat.Builder.create0().setDelimiter1("|||").build()
        )
        try:
            parserIterator = parser.iterator()
            while True:
                try:
                    csvRecord = parserIterator.next()
                    self.__print(csvRecord, csvPrinter)
                    self.assertEqual("a,b,c,d,,f", ''.join(stringBuilder))
                except StopIteration:
                    break
        finally:
            csvPrinter.close()
            parser.close()

    
    @pytest.mark.test
    def testParseWithTwoCharDelimiter1(self) -> None:
        in_ = io.StringIO("a~|b~|c~|d~|~|f")
        stringBuilder = []
        csvPrinter = CSVPrinter(stringBuilder, CSVFormat.EXCEL)
        parser = CSVParser.parse3(
            in_,
            CSVFormat.Builder.create0().setDelimiter1("~|").build()
        )
        try:
            parserIterator = parser.iterator()
            while True:
                try:
                    csvRecord = parserIterator.next()
                    self.__print(csvRecord, csvPrinter)
                    self.assertEqual("a,b,c,d,,f", ''.join(stringBuilder))
                except StopIteration:
                    break
        finally:
            csvPrinter.close()
            parser.close()

    
    @pytest.mark.test
    def testParseWithTwoCharDelimiter2(self) -> None:
        in_ = io.StringIO("a~|b~|c~|d~|~|f~")
        stringBuilder = []
        csvPrinter = CSVPrinter(stringBuilder, CSVFormat.EXCEL)
        parser = CSVParser.parse3(
            in_,
            CSVFormat.Builder.create0().setDelimiter1("~|").build()
        )
        try:
            parserIterator = parser.iterator()
            while True:
                try:
                    csvRecord = parserIterator.next()
                    self.__print(csvRecord, csvPrinter)
                    self.assertEqual("a,b,c,d,,f~", ''.join(stringBuilder))
                except StopIteration:
                    break
        finally:
            csvPrinter.close()
            parser.close()
    
    
    @pytest.mark.test
    def testParseWithTwoCharDelimiter3(self) -> None:
        in_ = io.StringIO("a~|b~|c~|d~|~|f|")
        stringBuilder = []
        csvPrinter = CSVPrinter(stringBuilder, CSVFormat.EXCEL)
        parser = CSVParser.parse3(
            in_,
            CSVFormat.Builder.create0().setDelimiter1("~|").build()
        )
        try:
            parserIterator = parser.iterator()
            while True:
                try:
                    csvRecord = parserIterator.next()
                    self.__print(csvRecord, csvPrinter)
                    self.assertEqual("a,b,c,d,,f|", ''.join(stringBuilder))
                except StopIteration:
                    break
        finally:
            csvPrinter.close()
            parser.close()

    
    @pytest.mark.test
    def testParseWithTwoCharDelimiter4(self) -> None:
        in_ = io.StringIO("a~|b~|c~|d~|~|f~~||g")
        stringBuilder = []
        csvPrinter = CSVPrinter(stringBuilder, CSVFormat.EXCEL)
        parser = CSVParser.parse3(
            in_,
            CSVFormat.Builder.create0().setDelimiter1("~|").build()
        )
        try:
            parserIterator = parser.iterator()
            while True:
                try:
                    csvRecord = parserIterator.next()
                    self.__print(csvRecord, csvPrinter)
                    self.assertEqual("a,b,c,d,,f~,|g", ''.join(stringBuilder))
                except StopIteration:
                    break
        finally:
            csvPrinter.close()
            parser.close()
    
    
    @pytest.mark.test
    def testParseWithTwoCharDelimiterEndsWithDelimiter(self) -> None:
        in_ = io.StringIO("a~|b~|c~|d~|~|f~|")
        stringBuilder = []
        csvPrinter = CSVPrinter(stringBuilder, CSVFormat.EXCEL)
        parser = CSVParser.parse3(
            in_,
            CSVFormat.Builder.create0().setDelimiter1("~|").build()
        )
        try:
            parserIterator = parser.iterator()
            while True:
                try:
                    csvRecord = parserIterator.next()
                    self.__print(csvRecord, csvPrinter)
                    self.assertEqual("a,b,c,d,,f,", ''.join(stringBuilder))
                except StopIteration:
                    break
        finally:
            csvPrinter.close()
            parser.close()
