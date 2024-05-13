# Imports Begin
from src.main.org.apache.commons.csv.CSVRecord import *
from src.main.org.apache.commons.csv.CSVPrinter import *
from src.main.org.apache.commons.csv.CSVParser import *
from src.main.org.apache.commons.csv.CSVFormat import *
import unittest
import os
# Imports End

class new Consumer<CSVRecord>(...) { ... }(unittest.TestCase):

    # Class Fields Begin
    # Class Fields End

    # Class Methods Begin
    def accept(self, record: CSVRecord) -> None:

            self.assertTrue(record.get1(0) == "foo \\")
            self.assertTrue(record.get1(1) == "bar")

    # Class Methods End


class JiraCsv249Test(unittest.TestCase):

    # Class Fields Begin
    # Class Fields End

    # Class Methods Begin
    def testJiraCsv249(self) -> None:

            csv_format = CSVFormat.DEFAULT.builder().setEscape0('\\').build()
            string_writer = StringWriter()
            try:
                printer = CSVPrinter(string_writer, csv_format)
                printer.printRecord1("foo \\", "bar")
            finally:
                string_writer.close()
            string_reader = StringReader(string_writer.toString())
            records = []
            try:
                parser = CSVParser.CSVParser1(string_reader, csv_format)
                records = parser.getRecords()
            finally:
                string_reader.close()
            for record in records:
                self.assertEqual("foo \\", record.get1(0))
                self.assertEqual("bar", record.get1(1))

    # Class Methods End


