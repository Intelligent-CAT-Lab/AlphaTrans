import pytest

from src.main.org.apache.commons.csv.CSVPrinter import *
from src.main.org.apache.commons.csv.CSVFormat import *
import unittest
import io


class JiraCsv271Test(unittest.TestCase):

    @pytest.mark.test
    def testJiraCsv271_withArray(self) -> None:
        csvFormat = CSVFormat.DEFAULT
        stringWriter = io.StringIO()
        printer = CSVPrinter(stringWriter, csvFormat)
        try:
            printer.print("a")
            printer.printRecord1("b", "c")
        finally:
            printer.close()
        self.assertEqual("a,b,c\r\n", stringWriter.getvalue())

    
    @pytest.mark.test
    def testJiraCsv271_withList(self) -> None:
        csvFormat = CSVFormat.DEFAULT
        stringWriter = io.StringIO()
        printer = CSVPrinter(stringWriter, csvFormat)
        try:
            printer.print("a")
            printer.printRecord0(["b", "c"])
        finally:
            printer.close()
        self.assertEqual("a,b,c\r\n", stringWriter.getvalue())
