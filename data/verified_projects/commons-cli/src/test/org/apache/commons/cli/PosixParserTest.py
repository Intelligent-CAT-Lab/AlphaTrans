# Imports Begin
from src.main.org.apache.commons.cli.PosixParser import *
from src.main.org.apache.commons.cli.ParserTestCase import *
from src.main.org.apache.commons.cli.CommandLineParser import *
import unittest
import os
import ParserTestCase

# Imports End


class PosixParserTest(ParserTestCase):

    # Class Fields Begin
    # Class Fields End

    # Class Methods Begin
    @classmethod
    def setUpClass(cls):
        pass


    def setUp(self) -> None:
        super().setUp()
        self.__parser = PosixParser()


    @unittest.skip("not supported by the PosixParser")
    def test_AmbiguousLongWithoutEqualSingleDash(self) -> None:
        try:
            pass
        except Exception as e:
            self.fail(f"An exception occurred: {e}")
    
    
    @unittest.skip("not supported by the PosixParser")
    def test_AmbiguousPartialLongOption4(self) -> None:
        try:
            pass
        except Exception as e:
            self.fail(f"An exception occurred: {e}")
    
    
    @unittest.skip("not supported by the PosixParser")
    def test_DoubleDash2(self) -> None:
        try:
            pass
        except Exception as e:
            self.fail(f"An exception occurred: {e}")

    
    @unittest.skip("not supported by the PosixParser")
    def test_LongWithEqualSingleDash(self) -> None:
        try:
            pass
        except Exception as e:
            self.fail(f"An exception occurred: {e}")

    
    @unittest.skip("not supported by the PosixParser")
    def test_LongWithoutEqualSingleDash(self) -> None:
        try:
            pass
        except Exception as e:
            self.fail(f"An exception occurred: {e}")

    
    @unittest.skip("not supported by the PosixParser")
    def test_LongWithUnexpectedArgument1(self) -> None:
        try:
            pass
        except Exception as e:
            self.fail(f"An exception occurred: {e}")

    
    @unittest.skip("not supported by the PosixParser (CLI-184)")
    def test_NegativeOption(self) -> None:
        try:
            pass
        except Exception as e:
            self.fail(f"An exception occurred: {e}")

    
    @unittest.skip("not supported by the PosixParser")
    def test_ShortWithEqual(self) -> None:
        try:
            pass
        except Exception as e:
            self.fail(f"An exception occurred: {e}")

    
    @unittest.skip("not supported by the PosixParser")
    def test_UnambiguousPartialLongOption4(self) -> None:
        try:
            pass
        except Exception as e:
            self.fail(f"An exception occurred: {e}")

    # Class Methods End
