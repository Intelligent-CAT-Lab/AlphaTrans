from __future__ import annotations
import re
from io import StringIO
import unittest
import pytest
import io
import unittest
from src.main.org.apache.commons.csv.CSVFormat import *
from src.main.org.apache.commons.csv.CSVPrinter import *
from src.main.org.apache.commons.csv.QuoteMode import *


class JiraCsv203Test(unittest.TestCase):

    def testWithoutQuoteMode(self) -> None:

        format_ = (
            CSVFormat.EXCEL.builder()
            .setNullString("N/A")
            .setIgnoreSurroundingSpaces(True)
            .build()
        )
        buffer = io.StringIO()
        with CSVPrinter(buffer, format_) as printer:
            printer.printRecord1(None, "Hello", None, "World")
        self.assertEqual("N/A,Hello,N/A,World\r\n", buffer.getvalue())

    def testWithoutNullString(self) -> None:

        format_ = (
            CSVFormat.EXCEL.builder()
            .setIgnoreSurroundingSpaces(True)
            .setQuoteMode(QuoteMode.ALL)
            .build()
        )
        buffer = io.StringIO()
        with CSVPrinter(buffer, format_) as printer:
            printer.printRecord1(None, "Hello", None, "World")
        self.assertEqual(',"Hello",,"World"\r\n', buffer.getvalue())

    def testWithEmptyValues(self) -> None:

        format_ = (
            CSVFormat.EXCEL.builder()
            .setNullString("N/A")
            .setIgnoreSurroundingSpaces(True)
            .setQuoteMode(QuoteMode.ALL)
            .build()
        )
        buffer = io.StringIO()
        with CSVPrinter(buffer, format_) as printer:
            printer.printRecord1("", "Hello", "", "World")
        self.assertEqual('"","Hello","","World"\r\n', buffer.getvalue())

    def testQuoteModeNonNumeric(self) -> None:

        format_ = (
            CSVFormat.EXCEL.builder()
            .setNullString("N/A")
            .setIgnoreSurroundingSpaces(True)
            .setQuoteMode(QuoteMode.NON_NUMERIC)
            .build()
        )
        buffer = io.StringIO()
        with CSVPrinter(buffer, format_) as printer:
            printer.printRecord1(None, "Hello", None, "World")
        self.assertEqual('N/A,"Hello",N/A,"World"\r\n', buffer.getvalue())

    def testQuoteModeMinimal(self) -> None:

        format_ = (
            CSVFormat.EXCEL.builder()
            .setNullString("N/A")
            .setIgnoreSurroundingSpaces(True)
            .setQuoteMode(QuoteMode.MINIMAL)
            .build()
        )
        buffer = io.StringIO()
        with CSVPrinter(buffer, format_) as printer:
            printer.printRecord1(None, "Hello", None, "World")
        self.assertEqual("N/A,Hello,N/A,World\r\n", buffer.getvalue())

    def testQuoteModeAllNonNull(self) -> None:

        format_ = (
            CSVFormat.EXCEL.builder()
            .setNullString("N/A")
            .setIgnoreSurroundingSpaces(True)
            .setQuoteMode(QuoteMode.ALL_NON_NULL)
            .build()
        )
        buffer = io.StringIO()
        with CSVPrinter(buffer, format_) as printer:
            printer.printRecord1(None, "Hello", None, "World")
        self.assertEqual('N/A,"Hello",N/A,"World"\r\n', buffer.getvalue())

    def testQuoteModeAll(self) -> None:

        format_ = (
            CSVFormat.EXCEL.builder()
            .setNullString("N/A")
            .setIgnoreSurroundingSpaces(True)
            .setQuoteMode(QuoteMode.ALL)
            .build()
        )
        buffer = io.StringIO()
        with CSVPrinter(buffer, format_) as printer:
            printer.printRecord1(None, "Hello", None, "World")
        self.assertEqual('"N/A","Hello","N/A","World"\r\n', buffer.getvalue())
