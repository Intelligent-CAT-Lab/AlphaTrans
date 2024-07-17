import pytest

from src.main.org.apache.commons.csv.CSVRecord import *
from src.main.org.apache.commons.csv.CSVPrinter import *
from src.main.org.apache.commons.csv.CSVParser import *
from src.main.org.apache.commons.csv.CSVFormat import *
import unittest
import io

class JiraCsv249Test(unittest.TestCase):

    @pytest.mark.test
    def testJiraCsv249(self) -> None:
        csvFormat = CSVFormat.DEFAULT.builder().setEscape0('\\').build()
        stringWriter = io.StringIO()
        printer = CSVPrinter(stringWriter, csvFormat)
        try:
            printer.printRecord1("foo \\", "bar")
        finally:
            stringWriter.close()
        stringReader = io.StringIO(stringWriter.getvalue())
        records = []
        parser = CSVParser.CSVParser1(stringReader, csvFormat)
        try:
            records = parser.getRecords()
        finally:
            stringReader.close()
        for record in records:
            self.assertEqual("foo \\", record.get1(0))
            self.assertEqual("bar", record.get1(1))
