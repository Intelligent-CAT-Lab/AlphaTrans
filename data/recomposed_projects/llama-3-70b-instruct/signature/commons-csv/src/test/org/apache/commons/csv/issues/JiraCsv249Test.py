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
        csvFormat = CSVFormat.DEFAULT.builder().setEscape0("\\").build()
        stringWriter = io.StringIO()
        with CSVPrinter(stringWriter, csvFormat) as printer:
            printer.printRecord1(["foo \\", "bar"])
        stringReader = io.StringIO(stringWriter.getvalue())
        with CSVParser(stringReader, csvFormat) as parser:
            records = parser.getRecords()
        for record in records:
            self.assertEqual("foo \\", record.get1(0))
            self.assertEqual("bar", record.get1(1))
