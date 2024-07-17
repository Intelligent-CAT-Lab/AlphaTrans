import pytest

from src.main.org.apache.commons.csv.QuoteMode import *
from src.main.org.apache.commons.csv.CSVPrinter import *
from src.main.org.apache.commons.csv.CSVFormat import *
import unittest

class JiraCsv203Test(unittest.TestCase):

    @pytest.mark.test
    def testQuoteModeAll(self) -> None:
        format = CSVFormat.EXCEL\
            .builder()\
            .setNullString("N/A")\
            .setIgnoreSurroundingSpaces(True)\
            .setQuoteMode(QuoteMode.ALL)\
            .build()
        buffer = []
        printer = CSVPrinter(buffer, format)
        try:
            printer.printRecord1(None, "Hello", None, "World")
        finally:
            printer.close()
        self.assertEqual(
            "\"N/A\",\"Hello\",\"N/A\",\"World\"\r\n",
            ''.join(buffer)
        )
    
    
    @pytest.mark.test
    def testQuoteModeAllNonNull(self) -> None:
        format = CSVFormat.EXCEL\
            .builder()\
            .setNullString("N/A")\
            .setIgnoreSurroundingSpaces(True)\
            .setQuoteMode(QuoteMode.ALL_NON_NULL)\
            .build()
        buffer = []
        printer = CSVPrinter(buffer, format)
        try:
            printer.printRecord1(None, "Hello", None, "World")
        finally:
            printer.close()
        self.assertEqual(
            "N/A,\"Hello\",N/A,\"World\"\r\n",
            ''.join(buffer)
        )

    
    @pytest.mark.test
    def testQuoteModeMinimal(self) -> None:
        format = CSVFormat.EXCEL\
            .builder()\
            .setNullString("N/A")\
            .setIgnoreSurroundingSpaces(True)\
            .setQuoteMode(QuoteMode.MINIMAL)\
            .build()
        buffer = []
        printer = CSVPrinter(buffer, format)
        try:
            printer.printRecord1(None, "Hello", None, "World")
        finally:
            printer.close()
        self.assertEqual(
            "N/A,Hello,N/A,World\r\n",
            ''.join(buffer)
        )

    
    @pytest.mark.test
    def testQuoteModeNonNumeric(self) -> None:
        format = CSVFormat.EXCEL\
            .builder()\
            .setNullString("N/A")\
            .setIgnoreSurroundingSpaces(True)\
            .setQuoteMode(QuoteMode.NON_NUMERIC)\
            .build()
        buffer = []
        printer = CSVPrinter(buffer, format)
        try:
            printer.printRecord1(None, "Hello", None, "World")
        finally:
            printer.close()
        self.assertEqual(
            "N/A,\"Hello\",N/A,\"World\"\r\n",
            ''.join(buffer)
        )
    
    
    @pytest.mark.test
    def testWithEmptyValues(self) -> None:
        format = CSVFormat.EXCEL\
            .builder()\
            .setNullString("N/A")\
            .setIgnoreSurroundingSpaces(True)\
            .setQuoteMode(QuoteMode.ALL)\
            .build()
        buffer = []
        printer = CSVPrinter(buffer, format)
        try:
            printer.printRecord1("", "Hello", "", "World")
        finally:
            printer.close()
        self.assertEqual(
            "\"\",\"Hello\",\"\",\"World\"\r\n",
            ''.join(buffer)
        )

    
    @pytest.mark.test
    def testWithoutNullString(self) -> None:
        format = CSVFormat.EXCEL\
            .builder()\
            .setIgnoreSurroundingSpaces(True)\
            .setQuoteMode(QuoteMode.ALL)\
            .build()
        buffer = []
        printer = CSVPrinter(buffer, format)
        try:
            printer.printRecord1(None, "Hello", None, "World")
        finally:
            printer.close()
        self.assertEqual(
            ",\"Hello\",,\"World\"\r\n",
            ''.join(buffer)
        )

    
    @pytest.mark.test
    def testWithoutQuoteMode(self) -> None:
        format = CSVFormat.EXCEL\
            .builder()\
            .setNullString("N/A")\
            .setIgnoreSurroundingSpaces(True)\
            .build()
        buffer = []
        printer = CSVPrinter(buffer, format)
        try:
            printer.printRecord1(None, "Hello", None, "World")
        finally:
            printer.close()
        self.assertEqual(
            "N/A,Hello,N/A,World\r\n",
            ''.join(buffer)
        )
