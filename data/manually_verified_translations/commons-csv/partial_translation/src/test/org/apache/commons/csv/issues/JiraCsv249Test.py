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


class JiraCsv249Test(unittest.TestCase):

    def testJiraCsv249(self) -> None:

        csv_format = CSVFormat.DEFAULT.builder().setEscape0("\\").build()
        string_writer = io.StringIO()
        with CSVPrinter(string_writer, csv_format) as printer:
            printer.printRecord1(["foo \\", "bar"])
        string_reader = io.StringIO(string_writer.getvalue())
        with CSVParser.CSVParser1(string_reader, csv_format) as parser:
            records = parser.getRecords()
        for record in records:
            self.assertEqual("foo \\", record.get1(0))
            self.assertEqual("bar", record.get1(1))
