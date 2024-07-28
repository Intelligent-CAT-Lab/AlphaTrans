from __future__ import annotations
import re
import unittest
import pytest
import io
import os
import unittest
from src.main.org.apache.commons.cli.CommandLineParser import *
from src.test.org.apache.commons.cli.ParserTestCase import *
from src.main.org.apache.commons.cli.PosixParser import *


class PosixParserTest(ParserTestCase, unittest.TestCase):

    @pytest.mark.skip(reason="Ignore")
    def testUnambiguousPartialLongOption4(self) -> None:
        pass

    @pytest.mark.skip(reason="Ignore")
    def testShortWithEqual(self) -> None:
        pass

    @pytest.mark.skip(reason="Ignore")
    def testNegativeOption(self) -> None:
        pass

    @pytest.mark.skip(reason="Ignore")
    def testLongWithUnexpectedArgument1(self) -> None:
        pass

    @pytest.mark.skip(reason="Ignore")
    def testLongWithoutEqualSingleDash(self) -> None:
        pass

    @pytest.mark.skip(reason="Ignore")
    def testLongWithEqualSingleDash(self) -> None:
        pass

    @pytest.mark.skip(reason="Ignore")
    def testDoubleDash2(self) -> None:
        pass

    @pytest.mark.skip(reason="Ignore")
    def testAmbiguousPartialLongOption4(self) -> None:
        pass

    @pytest.mark.skip(reason="Ignore")
    def testAmbiguousLongWithoutEqualSingleDash(self) -> None:
        pass

    def setUp(self) -> None:

        super().setUp()
        self._parser = PosixParser()
