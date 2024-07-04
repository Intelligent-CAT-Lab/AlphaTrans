from __future__ import annotations
import re
from io import StringIO
import unittest
import pytest
import io
import unittest
from src.main.org.apache.commons.csv.CSVFormat import *
from src.main.org.apache.commons.csv.QuoteMode import *


class JiraCsv263Test(unittest.TestCase):

    def testPrintFromReaderWithQuotes(self) -> None:

        format = (
            CSVFormat.RFC4180.builder()
            .setDelimiter0(",")
            .setQuote0('"')
            .setEscape0("?")
            .setQuoteMode(QuoteMode.NON_NUMERIC)
            .build()
        )
        out = io.StringIO()

        atStartOnly = io.StringIO('"a,b,c\r\nx,y,z')
        format.print2(atStartOnly, out, True)
        self.assertEqual('"""a,b,c\r\nx,y,z"', out.getvalue())

        out.seek(0)
        out.truncate(0)
        atEndOnly = io.StringIO('a,b,c\r\nx,y,z"')
        format.print2(atEndOnly, out, True)
        self.assertEqual('"a,b,c\r\nx,y,z"""', out.getvalue())

        out.seek(0)
        out.truncate(0)
        atBeginEnd = io.StringIO('"a,b,c\r\nx,y,z"')
        format.print2(atBeginEnd, out, True)
        self.assertEqual('"""a,b,c\r\nx,y,z"""', out.getvalue())

        out.seek(0)
        out.truncate(0)
        embeddedBeginMiddle = io.StringIO('"a",b,c\r\nx,"y",z')
        format.print2(embeddedBeginMiddle, out, True)
        self.assertEqual('"""a"",b,c\r\nx,""y"",z"', out.getvalue())

        out.seek(0)
        out.truncate(0)
        embeddedMiddleEnd = io.StringIO('a,"b",c\r\nx,y,"z"')
        format.print2(embeddedMiddleEnd, out, True)
        self.assertEqual('"a,""b"",c\r\nx,y,""z"""', out.getvalue())

        out.seek(0)
        out.truncate(0)
        nested = io.StringIO('a,"b "and" c",d')
        format.print2(nested, out, True)
        self.assertEqual('"a,""b "and" c",d"', out.getvalue())
