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

        atEndOnly = io.StringIO('a,b,c\r\nx,y,z"')
        out = io.StringIO()
        format.print2(atEndOnly, out, True)
        self.assertEqual('"a,b,c\r\nx,y,z"""', out.getvalue())

        atBeginEnd = io.StringIO('"a,b,c\r\nx,y,z"')
        out = io.StringIO()
        format.print2(atBeginEnd, out, True)
        self.assertEqual('"""a,b,c\r\nx,y,z"""', out.getvalue())

        embeddedBeginMiddle = io.StringIO('"a",b,c\r\nx,"y",z')
        out = io.StringIO()
        format.print2(embeddedBeginMiddle, out, True)
        self.assertEqual('"""a"",b,c\r\nx,""y"",z"', out.getvalue())

        embeddedMiddleEnd = io.StringIO('a,"b",c\r\nx,y,"z"')
        out = io.StringIO()
        format.print2(embeddedMiddleEnd, out, True)
        self.assertEqual('"a,""b"",c\r\nx,y,""z"""', out.getvalue())

        nested = io.StringIO('a,"b "and" c",d')
        out = io.StringIO()
        format.print2(nested, out, True)
        self.assertEqual("\"a,\"\"b \"\"and\"\" c\"\",d\"", out.getvalue())
