# Imports Begin
from src.main.org.apache.commons.csv.QuoteMode import *
from src.main.org.apache.commons.csv.CSVPrinter import *
from src.main.org.apache.commons.csv.CSVFormat import *
import unittest
import os

# Imports End


class JiraCsv203Test(unittest.TestCase):

    # Class Fields Begin
    # Class Fields End

    # Class Methods Begin
    def testWithoutQuoteMode(self) -> None:

        format = (
            CSVFormat.EXCEL.builder()
            .setNullString("N/A")
            .setIgnoreSurroundingSpaces(True)
            .build()
        )
        buffer = StringBuilder()
        with CSVPrinter(buffer, format) as printer:
            printer.printRecord1(None, "Hello", None, "World")
        self.assertEqual("N/A,Hello,N/A,World\r\n", buffer.toString())

    def testWithoutNullString(self) -> None:

        format = (
            CSVFormat.EXCEL.builder()
            .setIgnoreSurroundingSpaces(True)
            .setQuoteMode(QuoteMode.ALL)
            .build()
        )
        buffer = StringBuilder()
        with CSVPrinter(buffer, format) as printer:
            printer.printRecord1(None, "Hello", None, "World")
        self.assertEqual(',"Hello",,"World"\r\n', buffer.toString())

    def testWithEmptyValues(self) -> None:

        format = (
            CSVFormat.EXCEL.builder()
            .setNullString("N/A")
            .setIgnoreSurroundingSpaces(True)
            .setQuoteMode(QuoteMode.ALL)
            .build()
        )
        buffer = StringBuilder()
        with CSVPrinter(buffer, format) as printer:
            printer.printRecord1("", "Hello", "", "World")
        self.assertEqual('"","Hello","","World"\r\n', buffer.toString())

    def testQuoteModeNonNumeric(self) -> None:

        format = (
            CSVFormat.EXCEL.builder()
            .setNullString("N/A")
            .setIgnoreSurroundingSpaces(True)
            .setQuoteMode(QuoteMode.NON_NUMERIC)
            .build()
        )
        buffer = StringBuilder()
        try:
            printer = CSVPrinter(buffer, format)
            printer.printRecord1(None, "Hello", None, "World")
        finally:
            printer.close()
        self.assertEqual('N/A,"Hello",N/A,"World"\r\n', buffer.toString())

    def testQuoteModeMinimal(self) -> None:

        format = (
            CSVFormat.EXCEL.builder()
            .setNullString("N/A")
            .setIgnoreSurroundingSpaces(True)
            .setQuoteMode(QuoteMode.MINIMAL)
            .build()
        )
        buffer = StringBuilder()
        try:
            printer = CSVPrinter(buffer, format)
            printer.printRecord1(None, "Hello", None, "World")
        finally:
            printer.close()
        self.assertEqual("N/A,Hello,N/A,World\r\n", buffer.toString())

    def testQuoteModeAllNonNull(self) -> None:

        format = (
            CSVFormat.EXCEL.builder()
            .setNullString("N/A")
            .setIgnoreSurroundingSpaces(True)
            .setQuoteMode(QuoteMode.ALL_NON_NULL)
            .build()
        )
        buffer = StringBuilder()
        try:
            printer = CSVPrinter(buffer, format)
            printer.printRecord1(None, "Hello", None, "World")
        finally:
            printer.close()
        self.assertEqual('N/A,"Hello",N/A,"World"\r\n', buffer.toString())

    def testQuoteModeAll(self) -> None:

        format = (
            CSVFormat.EXCEL.builder()
            .setNullString("N/A")
            .setIgnoreSurroundingSpaces(True)
            .setQuoteMode(QuoteMode.ALL)
            .build()
        )
        buffer = StringBuilder()
        with CSVPrinter(buffer, format) as printer:
            printer.printRecord1(None, "Hello", None, "World")
        self.assertEqual('"N/A","Hello","N/A","World"\r\n', buffer.toString())

    # Class Methods End
