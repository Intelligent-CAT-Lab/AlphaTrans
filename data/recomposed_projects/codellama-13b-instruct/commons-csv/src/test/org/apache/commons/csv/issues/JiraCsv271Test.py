# Imports Begin
from src.main.org.apache.commons.csv.CSVPrinter import *
from src.main.org.apache.commons.csv.CSVFormat import *
import unittest
import typing
from typing import *

# Imports End


class JiraCsv271Test(unittest.TestCase):

    # Class Fields Begin
    # Class Fields End

    # Class Methods Begin
    def testJiraCsv271_withList(self) -> None:

        csv_format = CSVFormat.DEFAULT
        string_writer = StringWriter()
        try:
            printer = CSVPrinter(string_writer, csv_format)
            printer.print("a")
            printer.printRecord0(["b", "c"])
        except Exception as e:
            self.assertTrue(False, f"Unexpected exception: {e}")
        self.assertEqual("a,b,c\r\n", string_writer.toString())

    def testJiraCsv271_withArray(self) -> None:

        csv_format = CSVFormat.DEFAULT
        string_writer = StringWriter()
        try:
            printer = CSVPrinter(string_writer, csv_format)
            printer.print("a")
            printer.printRecord1("b", "c")
        except Exception:
            self.assertTrue(False, "Exception occurred")
        self.assertEqual("a,b,c\r\n", string_writer.toString())

    # Class Methods End
