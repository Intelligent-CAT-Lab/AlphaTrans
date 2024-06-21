from __future__ import annotations
import re
import unittest
import pytest
import io
from src.main.org.apache.commons.csv.CSVFormat import *
from src.main.org.apache.commons.csv.CSVPrinter import *
from src.main.org.apache.commons.csv.QuoteMode import *


class JiraCsv203Test(unittest.TestCase):

    @pytest.mark.test
    def testWithoutQuoteMode(self) -> None:

        format = (
            CSVFormat.EXCEL.builder()
            .setNullString("N/A")
            .setIgnoreSurroundingSpaces(True)
            .build()
        )
        buffer = io.StringIO()
        with CSVPrinter(buffer, format) as printer:
            printer.printRecord1(None, "Hello", None, "World")
        self.assertEqual("N/A,Hello,N/A,World\r\n", buffer.getvalue())

    @pytest.mark.test
    def testWithoutNullString(self) -> None:

        format = (
            CSVFormat.builder()
            .setIgnoreSurroundingSpaces(True)
            .setQuoteMode(QuoteMode.ALL)
            .build()
        )
        buffer = StringIO()
        printer = CSVPrinter(buffer, format)
        printer.printRecord1(None, "Hello", None, "World")
        self.assertEqual(',"Hello",,"World"\r\n', buffer.getvalue())

    @pytest.mark.test
    def testWithEmptyValues(self) -> None:

        format = (
            CSVFormat.EXCEL.builder()
            .setNullString("N/A")
            .setIgnoreSurroundingSpaces(True)
            .setQuoteMode(QuoteMode.ALL)
            .build()
        )
        buffer = io.StringIO()
        with CSVPrinter(buffer, format) as printer:
            printer.printRecord1("", "Hello", "", "World")
        self.assertEqual('"","Hello","","World"\r\n', buffer.getvalue())

    @pytest.mark.test
    def testQuoteModeNonNumeric(self) -> None:

        format = (
            CSVFormat.EXCEL.builder()
            .setNullString("N/A")
            .setIgnoreSurroundingSpaces(True)
            .setQuoteMode(QuoteMode.NON_NUMERIC)
            .build()
        )
        buffer = io.StringIO()
        with CSVPrinter(buffer, format) as printer:
            printer.printRecord1(None, "Hello", None, "World")
        self.assertEqual('N/A,"Hello",N/A,"World"\r\n', buffer.getvalue())

    @pytest.mark.test
    def testQuoteModeMinimal(self) -> None:

        format = (
            CSVFormat.EXCEL.builder()
            .setNullString("N/A")
            .setIgnoreSurroundingSpaces(True)
            .setQuoteMode(QuoteMode.MINIMAL)
            .build()
        )
        buffer = io.StringIO()
        with CSVPrinter(buffer, format) as printer:
            printer.printRecord1(None, "Hello", None, "World")
        self.assertEqual("N/A,Hello,N/A,World\r\n", buffer.getvalue())

    @pytest.mark.test
    def testQuoteModeAllNonNull(self) -> None:

        format = (
            CSVFormat.EXCEL.builder()
            .setNullString("N/A")
            .setIgnoreSurroundingSpaces(True)
            .setQuoteMode(QuoteMode.ALL_NON_NULL)
            .build()
        )
        buffer = io.StringIO()
        printer = CSVPrinter(buffer, format)
        printer.printRecord1(None, "Hello", None, "World")
        self.assertEqual('N/A,"Hello",N/A,"World"\r\n', buffer.getvalue())

    @pytest.mark.test
    def testQuoteModeAll(self) -> None:

        format = (
            CSVFormat.EXCEL.builder()
            .setNullString("N/A")
            .setIgnoreSurroundingSpaces(True)
            .setQuoteMode(QuoteMode.ALL)
            .build()
        )
        buffer = io.StringIO()
        with CSVPrinter(buffer, format) as printer:
            printer.printRecord1(None, "Hello", None, "World")
        self.assertEqual('"N/A","Hello","N/A","World"\r\n', buffer.getvalue())
