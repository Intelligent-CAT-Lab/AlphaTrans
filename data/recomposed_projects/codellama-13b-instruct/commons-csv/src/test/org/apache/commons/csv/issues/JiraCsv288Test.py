# Imports Begin
from src.main.org.apache.commons.csv.CSVRecord import *
from src.main.org.apache.commons.csv.CSVPrinter import *
from src.main.org.apache.commons.csv.CSVParser import *
from src.main.org.apache.commons.csv.CSVFormat import *
import unittest
import io

# Imports End


class JiraCsv288Test(unittest.TestCase):

    # Class Fields Begin
    # Class Fields End

    # Class Methods Begin
    def testParseWithTwoCharDelimiterEndsWithDelimiter(self) -> None:

        pass  # LLM could not translate method body

    def testParseWithTwoCharDelimiter4(self) -> None:

        pass  # LLM could not translate method body

    def testParseWithTwoCharDelimiter3(self) -> None:

        pass  # LLM could not translate method body

    def testParseWithTwoCharDelimiter2(self) -> None:

        pass  # LLM could not translate method body

    def testParseWithTwoCharDelimiter1(self) -> None:

        pass  # LLM could not translate method body

    def testParseWithTriplePipeDelimiter(self) -> None:

        in_str = "a|||b|||c|||d||||||f"
        in_io = io.StringIO(in_str)
        string_builder = StringBuilder()
        with CSVPrinter(
            string_builder, CSVFormat.EXCEL
        ) as csv_printer, CSVParser.parse3(
            in_io, CSVFormat.Builder.create0().setDelimiter1("|||").build()
        ) as csv_parser:
            for csv_record in csv_parser:
                self.__print(csv_record, csv_printer)
                self.assertEqual("a,b,c,d,,f", string_builder.getvalue())

    def testParseWithSinglePipeDelimiterEndsWithDelimiter(self) -> None:

        in_ = io.StringIO("a|b|c|d||f|")
        string_builder = io.StringIO()
        with CSVPrinter(string_builder, CSVFormat.EXCEL) as csv_printer, CSVParser(
            in_, CSVFormat.Builder.create0().setDelimiter1("|").build()
        ) as csv_parser:
            for csv_record in csv_parser:
                self.__print(csv_record, csv_printer)
                self.assertEqual("a,b,c,d,,f,", string_builder.getvalue())

    def testParseWithDoublePipeDelimiterQuoted(self) -> None:

        pass  # LLM could not translate method body

    def testParseWithDoublePipeDelimiterEndsWithDelimiter(self) -> None:

        in_ = io.StringIO("a||b||c||d||||f||")
        string_builder = io.StringIO()
        with CSVPrinter(string_builder, CSVFormat.EXCEL) as csv_printer, CSVParser(
            in_, CSVFormat.Builder.create0().setDelimiter1("||").build()
        ) as csv_parser:
            for csv_record in csv_parser:
                self.__print(csv_record, csv_printer)
                self.assertEqual("a,b,c,d,,f,", string_builder.getvalue())

    def testParseWithDoublePipeDelimiterDoubleCharValue(self) -> None:

        in_ = io.StringIO("a||bb||cc||dd||f")
        string_builder = io.StringIO()
        with CSVPrinter(string_builder, CSVFormat.EXCEL) as csv_printer, CSVParser(
            in_, CSVFormat.Builder.create0().setDelimiter1("||").build()
        ) as csv_parser:
            for csv_record in csv_parser:
                self.__print(csv_record, csv_printer)
                self.assertEqual("a,bb,cc,dd,f", string_builder.getvalue())

    def testParseWithDoublePipeDelimiter(self) -> None:

        pass  # LLM could not translate method body

    def testParseWithABADelimiter(self) -> None:

        in_ = io.StringIO("a|~|b|~|c|~|d|~||~|f")
        string_builder = io.StringIO()
        with CSVPrinter(string_builder, CSVFormat.EXCEL) as csv_printer, CSVParser(
            in_, CSVFormat.Builder.create0().setDelimiter1("|~|").build()
        ) as parser:
            for csv_record in parser:
                self.__print(csv_record, csv_printer)
                self.assertEqual("a,b,c,d,,f", string_builder.getvalue())

    def __print(self, csvRecord: CSVRecord, csvPrinter: CSVPrinter) -> None:

        for value in csvRecord:
            csvPrinter.print(value)

    # Class Methods End
