# Imports Begin
from src.main.org.apache.commons.cli.PosixParser import *
from src.main.org.apache.commons.cli.ParserTestCase import *
from src.main.org.apache.commons.cli.CommandLineParser import *
import unittest
import os

# Imports End


class PosixParserTest(unittest.TestCase, ParserTestCase):

    # Class Fields Begin
    # Class Fields End

    # Class Methods Begin
    def testUnambiguousPartialLongOption4(self) -> None:

        pass

    def testShortWithEqual(self) -> None:

        pass

    def testNegativeOption(self) -> None:

        pass

    def testLongWithUnexpectedArgument1(self) -> None:

        pass

    def testLongWithoutEqualSingleDash(self) -> None:

        pass

    def testLongWithEqualSingleDash(self) -> None:

        pass

    def testDoubleDash2(self) -> None:

        pass

    def testAmbiguousPartialLongOption4(self) -> None:

        pass

    def testAmbiguousLongWithoutEqualSingleDash(self) -> None:

        pass

    def setUp(self) -> None:

        super().setUp()
        self.parser = PosixParser()

    # Class Methods End
