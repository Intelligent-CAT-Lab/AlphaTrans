from __future__ import annotations
import re
import unittest
import pytest
import io
import unittest
from src.main.org.apache.commons.csv.CSVFormat import *
from src.main.org.apache.commons.csv.QuoteMode import *


class JiraCsv263Test(unittest.TestCase):

    def testPrintFromReaderWithQuotes(self) -> None:
        format: CSVFormat = (
            CSVFormat.RFC4180.builder()
            .setDelimiter0(",")
            .setQuote0('"')
            .setEscape0("?")
            .setQuoteMode(QuoteMode.NON_NUMERIC)
            .build()
        )
        out: StringBuilder = StringBuilder()

        atStartOnly: Reader = StringReader('"a,b,c\r\nx,y,z')
        format.print2(atStartOnly, out, True)
        self.assertEqual('"""a,b,c\r\nx,y,z"', out.toString())

        atEndOnly: Reader = StringReader('a,b,c\r\nx,y,z"')
        out.setLength(0)
        format.print2(atEndOnly, out, True)
        self.assertEqual('"a,b,c\r\nx,y,z"""', out.toString())

        atBeginEnd: Reader = StringReader('"a,b,c\r\nx,y,z"')
        out.setLength(0)
        format.print2(atBeginEnd, out, True)
        self.assertEqual('"""a,b,c\r\nx,y,z"""', out.toString())

        embeddedBeginMiddle: Reader = StringReader('"a",b,c\r\nx,"y",z')
        out.setLength(0)
        format.print2(embeddedBeginMiddle, out, True)
        self.assertEqual('"""a"",b,c\r\nx,""y"",z"', out.toString())

        embeddedMiddleEnd: Reader = StringReader('a,"b",c\r\nx,y,"z"')
        out.setLength(0)
        format.print2(embeddedMiddleEnd, out, True)
        self.assertEqual('"a,""b"",c\r\nx,y,""z"""', out.toString())

        nested: Reader = StringReader('a,"b "and" c",d')
        out.setLength(0)
        format.print2(nested, out, True)
        self.assertEqual('"a,""b ""and"" c"",d"', out.toString())
