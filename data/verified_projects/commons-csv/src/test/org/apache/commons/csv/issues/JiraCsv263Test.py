import pytest

from src.main.org.apache.commons.csv.QuoteMode import *
from src.main.org.apache.commons.csv.CSVFormat import *
import unittest
import io


class JiraCsv263Test(unittest.TestCase):

    @pytest.mark.test
    def testPrintFromReaderWithQuotes(self) -> None:
        format = CSVFormat.RFC4180\
            .builder()\
            .setDelimiter0(',')\
            .setQuote0('"')\
            .setEscape0('?')\
            .setQuoteMode(QuoteMode.NON_NUMERIC)\
            .build()
        out = []

        atStartOnly = io.StringIO("\"a,b,c\r\nx,y,z")
        format.print2(atStartOnly, out, True)
        self.assertEqual("\"\"\"a,b,c\r\nx,y,z\"", ''.join(out))

        atEndOnly = io.StringIO("a,b,c\r\nx,y,z\"")
        out.clear()
        format.print2(atEndOnly, out, True)
        self.assertEqual("\"a,b,c\r\nx,y,z\"\"\"", ''.join(out))

        atBeginEnd = io.StringIO("\"a,b,c\r\nx,y,z\"")
        out.clear()
        format.print2(atBeginEnd, out, True)
        self.assertEqual("\"\"\"a,b,c\r\nx,y,z\"\"\"", ''.join(out))

        embeddedBeginMiddle = io.StringIO("\"a\",b,c\r\nx,\"y\",z")
        out.clear()
        format.print2(embeddedBeginMiddle, out, True)
        self.assertEqual("\"\"\"a\"\",b,c\r\nx,\"\"y\"\",z\"", ''.join(out))

        embeddedMiddleEnd = io.StringIO("a,\"b\",c\r\nx,y,\"z\"")
        out.clear()
        format.print2(embeddedMiddleEnd, out, True)
        self.assertEqual("\"a,\"\"b\"\",c\r\nx,y,\"\"z\"\"\"", ''.join(out))

        nested = io.StringIO("a,\"b \"and\" c\",d")
        out.clear()
        format.print2(nested, out, True)
        self.assertEqual("\"a,\"\"b \"\"and\"\" c\"\",d\"", ''.join(out))
