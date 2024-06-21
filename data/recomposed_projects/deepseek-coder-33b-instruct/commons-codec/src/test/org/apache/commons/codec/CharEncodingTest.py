from __future__ import annotations
import re
import unittest
import pytest
import io
from src.main.org.apache.commons.codec.CharEncoding import *


class CharEncodingTest(unittest.TestCase):

    def testUtf8(self) -> None:

        assert "UTF-8" == UTF_8

    def testUtf16Le(self) -> None:

        assert "UTF-16LE" == UTF_16LE

    def testUtf16Be(self) -> None:

        assert "UTF-16BE" == UTF_16BE

    def testUtf16(self) -> None:

        assert "UTF-16" == UTF_16

    def testUsAscii(self) -> None:

        assert "US-ASCII" == US_ASCII

    def testIso8859_1(self) -> None:

        assert "ISO-8859-1" == ISO_8859_1

    def testConstructor(self) -> None:

        # The Java code is creating a new instance of CharEncoding, but it doesn't seem to be doing anything with it.
        # In Python, you don't need to explicitly call a constructor, as it's done automatically when you create a new object.
        # So, the Python translation would be simply:
        CharEncoding()
