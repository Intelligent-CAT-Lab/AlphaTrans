from __future__ import annotations
import re
import unittest
import pytest
import io
import typing
from typing import *
from src.main.org.apache.commons.csv.CSVFormat import *
from src.main.org.apache.commons.csv.CSVPrinter import *


class JiraCsv271Test(unittest.TestCase):

    @pytest.mark.test
    def testJiraCsv271_withList(self) -> None:

        csv_format = CSVFormat.DEFAULT
        string_writer = io.StringIO()
        with CSVPrinter(string_writer, csv_format) as printer:
            printer.print("a")
            printer.printRecord0(["b", "c"])

        self.assertEqual("a,b,c\r\n", string_writer.getvalue())

    @pytest.mark.test
    def testJiraCsv271_withArray(self) -> None:

        csv_format = CSVFormat.DEFAULT
        string_writer = io.StringIO()
        with CSVPrinter(string_writer, csv_format) as printer:
            printer.print_("a")
            printer.printRecord1("b", "c")

        self.assertEqual("a,b,c\r\n", string_writer.getvalue())
