from __future__ import annotations
import re
from io import StringIO
import unittest
import pytest
import io
import typing
from typing import *
import unittest
from src.main.org.apache.commons.csv.CSVFormat import *
from src.main.org.apache.commons.csv.CSVPrinter import *


class JiraCsv271Test(unittest.TestCase):

    def testJiraCsv271_withList(self) -> None:

        csvFormat = CSVFormat.DEFAULT
        stringWriter = io.StringIO()
        try:
            printer = CSVPrinter(stringWriter, csvFormat)
            printer.print("a")
            printer.printRecord0(["b", "c"])
        finally:
            self.assertEqual("a,b,c\r\n", stringWriter.getvalue())

    def testJiraCsv271_withArray(self) -> None:

        csvFormat = CSVFormat.DEFAULT
        stringWriter = io.StringIO()
        with CSVPrinter(stringWriter, csvFormat) as printer:
            printer.print("a")
            printer.printRecord1(["b", "c"])

        self.assertEqual("a,b,c\r\n", stringWriter.getvalue())
