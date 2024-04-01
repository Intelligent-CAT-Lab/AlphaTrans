# Imports Begin
from src.main.org.apache.commons.cli.ParserTestCase import *
from src.main.org.apache.commons.cli.GnuParser import *
from src.main.org.apache.commons.cli.CommandLineParser import *
import unittest

# Imports End


class GnuParserTest(unittest.TestCase, ParserTestCase):

    # Class Fields Begin
    # Class Fields End

    # Class Methods Begin
    def testUnrecognizedOptionWithBursting(self) -> None:

        pass

    def testUnambiguousPartialLongOption4(self) -> None:

        pass

    def testUnambiguousPartialLongOption3(self) -> None:

        pass

    def testUnambiguousPartialLongOption2(self) -> None:

        pass

    def testUnambiguousPartialLongOption1(self) -> None:

        pass

    def testStopBursting2(self) -> None:

        pass

    def testStopBursting(self) -> None:

        pass

    def testShortWithUnexpectedArgument(self) -> None:

        pass

    def testPartialLongOptionSingleDash(self) -> None:

        pass

    def testNegativeOption(self) -> None:

        pass

    def testMissingArgWithBursting(self) -> None:

        pass

    def testLongWithUnexpectedArgument2(self) -> None:

        pass

    def testLongWithUnexpectedArgument1(self) -> None:

        pass

    def testLongWithoutEqualSingleDash(self) -> None:

        pass

    def testDoubleDash2(self) -> None:

        pass

    def testBursting(self) -> None:

        pass

    def testAmbiguousPartialLongOption4(self) -> None:

        pass

    def testAmbiguousPartialLongOption3(self) -> None:

        pass

    def testAmbiguousPartialLongOption2(self) -> None:

        pass

    def testAmbiguousPartialLongOption1(self) -> None:

        pass

    def testAmbiguousLongWithoutEqualSingleDash(self) -> None:

        pass

    def setUp(self) -> None:

        super().setUp()
        self.parser = GnuParser()

    # Class Methods End
