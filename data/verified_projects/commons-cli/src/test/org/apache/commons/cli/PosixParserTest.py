import pytest

from src.main.org.apache.commons.cli.PosixParser import *
from src.main.org.apache.commons.cli.CommandLineParser import *
import unittest
from src.test.org.apache.commons.cli.ParserTestCase import ParserTestCase



class PosixParserTest(ParserTestCase):

    __test__ = True

    def setUp(self) -> None:
        super().setUp()
        self._parser = PosixParser()


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
