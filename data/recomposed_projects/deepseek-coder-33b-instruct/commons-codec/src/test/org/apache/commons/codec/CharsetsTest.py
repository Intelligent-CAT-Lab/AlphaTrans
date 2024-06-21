from __future__ import annotations
import re
import unittest
import pytest
import io
from src.main.org.apache.commons.codec.Charsets import *


class CharsetsTest(unittest.TestCase):

    def testUtf8(self) -> None:

        assert "UTF-8" == UTF_8.name()

    def testUtf16Le(self) -> None:

        assert "UTF-16LE" == UTF_16LE.name()

    def testUtf16Be(self) -> None:

        assert "UTF-16BE" == Charsets.UTF_16BE.name()

    def testUtf16(self) -> None:

        assert "UTF-16" == UTF_16.name()

    def testUsAscii(self) -> None:

        assert "US-ASCII" == Charsets.US_ASCII.name()

    def testIso8859_1(self) -> None:

        assert "ISO-8859-1" == Charsets.ISO_8859_1.name()

    def testToCharset(self) -> None:

        # Assert.assertEquals(Charset.defaultCharset(), Charsets.toCharset1((String) null));
        assert Charset.defaultCharset() == Charsets.toCharset1(None)

        # Assert.assertEquals(Charset.defaultCharset(), Charsets.toCharset0((Charset) null));
        assert Charset.defaultCharset() == Charsets.toCharset0(None)

        # Assert.assertEquals(Charset.defaultCharset(), Charsets.toCharset0(Charset.defaultCharset()));
        assert Charset.defaultCharset() == Charsets.toCharset0(Charset.defaultCharset())

        # Assert.assertEquals(StandardCharsets.UTF_8, Charsets.toCharset0(StandardCharsets.UTF_8));
        assert StandardCharsets.UTF_8 == Charsets.toCharset0(StandardCharsets.UTF_8)
