from __future__ import annotations
import re
from io import BytesIO
from io import StringIO
import unittest
import pytest
import io
import unittest
from src.main.org.apache.commons.codec.Charsets import *


class CharsetsTest(unittest.TestCase):

    def testUtf8(self) -> None:

        self.assertEqual("UTF-8", Charsets.UTF_8.name())

    def testUtf16Le(self) -> None:

        self.assertEqual("UTF-16LE", Charsets.UTF_16LE.name())

    def testUtf16Be(self) -> None:

        self.assertEqual("UTF-16BE", Charsets.UTF_16BE.name())

    def testUtf16(self) -> None:

        self.assertEqual("UTF-16", Charsets.UTF_16.name())

    def testUsAscii(self) -> None:

        self.assertEqual("US-ASCII", Charsets.US_ASCII.name())

    def testIso8859_1(self) -> None:

        self.assertEqual("ISO-8859-1", Charsets.ISO_8859_1.name())

    def testToCharset(self) -> None:

        self.assertEqual(io.open(io.StringIO()).encoding, Charsets.toCharset1(None))
        self.assertEqual(io.open(io.BytesIO()).encoding, Charsets.toCharset0(None))
        self.assertEqual(
            io.open(io.BytesIO()).encoding,
            Charsets.toCharset0(io.open(io.BytesIO()).encoding),
        )
        self.assertEqual("utf-8", Charsets.toCharset0("utf-8"))
