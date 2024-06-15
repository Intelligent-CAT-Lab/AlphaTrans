import pytest

# Imports Begin
from src.main.org.apache.commons.cli.PosixParser import *
from src.main.org.apache.commons.cli.CommandLineParser import *
import unittest
from src.test.org.apache.commons.cli.ParserTestCase import ParserTestCase

# Imports End


class PosixParserTest(ParserTestCase):

    # Class Fields Begin
    # Class Fields End

    # Class Methods Begin
    @classmethod
    def setUpClass(cls):
        pass


    def setUp(self) -> None:
        super().setUp(PosixParser())


    @unittest.skip("not supported by the PosixParser")
    @pytest.mark.test
    def testAmbiguousLongWithoutEqualSingleDash(self) -> None:
        try:
            pass
        except Exception as e:
            self.fail(f"An exception occurred: {e}")
    
    
    @unittest.skip("not supported by the PosixParser")
    @pytest.mark.test
    def testAmbiguousPartialLongOption4(self) -> None:
        try:
            pass
        except Exception as e:
            self.fail(f"An exception occurred: {e}")
    
    
    @unittest.skip("not supported by the PosixParser")
    @pytest.mark.test
    def testDoubleDash2(self) -> None:
        try:
            pass
        except Exception as e:
            self.fail(f"An exception occurred: {e}")

    
    @unittest.skip("not supported by the PosixParser")
    @pytest.mark.test
    def testLongWithEqualSingleDash(self) -> None:
        try:
            pass
        except Exception as e:
            self.fail(f"An exception occurred: {e}")

    
    @unittest.skip("not supported by the PosixParser")
    @pytest.mark.test
    def testLongWithoutEqualSingleDash(self) -> None:
        try:
            pass
        except Exception as e:
            self.fail(f"An exception occurred: {e}")

    
    @unittest.skip("not supported by the PosixParser")
    @pytest.mark.test
    def testLongWithUnexpectedArgument1(self) -> None:
        try:
            pass
        except Exception as e:
            self.fail(f"An exception occurred: {e}")

    
    @unittest.skip("not supported by the PosixParser (CLI-184)")
    @pytest.mark.test
    def testNegativeOption(self) -> None:
        try:
            pass
        except Exception as e:
            self.fail(f"An exception occurred: {e}")

    
    @unittest.skip("not supported by the PosixParser")
    @pytest.mark.test
    def testShortWithEqual(self) -> None:
        try:
            pass
        except Exception as e:
            self.fail(f"An exception occurred: {e}")

    
    @unittest.skip("not supported by the PosixParser")
    @pytest.mark.test
    def testUnambiguousPartialLongOption4(self) -> None:
        try:
            pass
        except Exception as e:
            self.fail(f"An exception occurred: {e}")

    # Class Methods End
