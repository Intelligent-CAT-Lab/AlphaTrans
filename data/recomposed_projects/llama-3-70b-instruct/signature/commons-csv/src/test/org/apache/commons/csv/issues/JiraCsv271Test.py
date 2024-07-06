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
        csvFormat: CSVFormat = CSVFormat.DEFAULT
        stringWriter: io.StringIO = io.StringIO()
        with CSVPrinter(stringWriter, csvFormat) as printer:
            printer.print("a")
            printer.printRecord0(["b", "c"])
        self.assertEqual("a,b,c\r\n", stringWriter.getvalue())

    def testJiraCsv271_withArray(self) -> None:
        csvFormat: CSVFormat = CSVFormat.DEFAULT
        stringWriter: io.StringIO = io.StringIO()
        with CSVPrinter(stringWriter, csvFormat) as printer:
            printer.print("a")
            printer.printRecord1(["b", "c"])
        self.assertEqual("a,b,c\r\n", stringWriter.getvalue())
