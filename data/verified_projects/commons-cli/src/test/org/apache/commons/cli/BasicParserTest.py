import pytest

# Imports Begin
from src.main.org.apache.commons.cli.CommandLineParser import *
from src.main.org.apache.commons.cli.BasicParser import *
import unittest
from src.test.org.apache.commons.cli.ParserTestCase import ParserTestCase

# Imports End


class BasicParserTest(ParserTestCase):

    # Class Fields Begin
    # Class Fields End

    # Class Methods Begin
    @classmethod
    def setUpClass(cls):
        pass

    def setUp(self) -> None:
        super().setUp(BasicParser())

    @unittest.skip("not supported by the BasicParser")
    @pytest.mark.test
    def testAmbiguousLongWithoutEqualSingleDash(self) -> None:
        try:
            pass
        except Exception as e:
            self.fail(f"An exception occurred: {e}")

    @unittest.skip("not supported by the BasicParser")
    @pytest.mark.test
    def testAmbiguousPartialLongOption1(self) -> None:
        try:
            pass
        except Exception as e:
            self.fail(f"An exception occurred: {e}")

    @unittest.skip("not supported by the BasicParser")
    @pytest.mark.test
    def testAmbiguousPartialLongOption2(self) -> None:
        try:
            pass
        except Exception as e:
            self.fail(f"An exception occurred: {e}")

    @unittest.skip("not supported by the BasicParser")
    @pytest.mark.test
    def testAmbiguousPartialLongOption3(self) -> None:
        try:
            pass
        except Exception as e:
            self.fail(f"An exception occurred: {e}")

    @unittest.skip("not supported by the BasicParser")
    @pytest.mark.test
    def testAmbiguousPartialLongOption4(self) -> None:
        try:
            pass
        except Exception as e:
            self.fail(f"An exception occurred: {e}")

    @unittest.skip("not supported by the BasicParser")
    @pytest.mark.test
    def testBursting(self) -> None:
        try:
            pass
        except Exception as e:
            self.fail(f"An exception occurred: {e}")

    @unittest.skip("not supported by the BasicParser")
    @pytest.mark.test
    def testDoubleDash2(self) -> None:
        try:
            pass
        except Exception as e:
            self.fail(f"An exception occurred: {e}")

    @unittest.skip("not supported by the BasicParser")
    @pytest.mark.test
    def testLongOptionWithEqualsQuoteHandling(self) -> None:
        try:
            pass
        except Exception as e:
            self.fail(f"An exception occurred: {e}")

    @unittest.skip("not supported by the BasicParser")
    @pytest.mark.test
    def testLongWithEqualDoubleDash(self) -> None:
        try:
            pass
        except Exception as e:
            self.fail(f"An exception occurred: {e}")

    @unittest.skip("not supported by the BasicParser")
    @pytest.mark.test
    def testLongWithEqualSingleDash(self) -> None:
        try:
            pass
        except Exception as e:
            self.fail(f"An exception occurred: {e}")

    @unittest.skip("not supported by the BasicParser")
    @pytest.mark.test
    def testLongWithoutEqualSingleDash(self) -> None:
        try:
            pass
        except Exception as e:
            self.fail(f"An exception occurred: {e}")

    @unittest.skip("not supported by the BasicParser")
    @pytest.mark.test
    def testMissingArgWithBursting(self) -> None:
        try:
            pass
        except Exception as e:
            self.fail(f"An exception occurred: {e}")

    @unittest.skip("not supported by the BasicParser (CLI-184)")
    @pytest.mark.test
    def testNegativeOption(self) -> None:
        try:
            pass
        except Exception as e:
            self.fail(f"An exception occurred: {e}")

    @unittest.skip("not supported by the BasicParser")
    @pytest.mark.test
    def testPartialLongOptionSingleDash(self) -> None:
        try:
            pass
        except Exception as e:
            self.fail(f"An exception occurred: {e}")

    @unittest.skip("not supported by the BasicParser")
    @pytest.mark.test
    def testPropertiesOption1(self) -> None:
        try:
            pass
        except Exception as e:
            self.fail(f"An exception occurred: {e}")
    
    @unittest.skip("not supported by the BasicParser")
    @pytest.mark.test
    def testPropertiesOption2(self) -> None:
        try:
            pass
        except Exception as e:
            self.fail(f"An exception occurred: {e}")

    @unittest.skip("not supported by the BasicParser")
    @pytest.mark.test
    def testShortOptionConcatenatedQuoteHandling(self) -> None:
        try:
            pass
        except Exception as e:
            self.fail(f"An exception occurred: {e}")

    @unittest.skip("not supported by the BasicParser")
    @pytest.mark.test
    def testShortWithEqual(self) -> None:
        try:
            pass
        except Exception as e:
            self.fail(f"An exception occurred: {e}")

    @unittest.skip("not supported by the BasicParser")
    @pytest.mark.test
    def testShortWithoutEqual(self) -> None:
        try:
            pass
        except Exception as e:
            self.fail(f"An exception occurred: {e}")

    @unittest.skip("not supported by the BasicParser")
    @pytest.mark.test
    def testStopBursting(self) -> None:
        try:
            pass
        except Exception as e:
            self.fail(f"An exception occurred: {e}")

    @unittest.skip("not supported by the BasicParser")
    @pytest.mark.test
    def testStopBursting2(self) -> None:
        try:
            pass
        except Exception as e:
            self.fail(f"An exception occurred: {e}")

    @unittest.skip("not supported by the BasicParser")
    @pytest.mark.test
    def testUnambiguousPartialLongOption1(self) -> None:
        try:
            pass
        except Exception as e:
            self.fail(f"An exception occurred: {e}")

    @unittest.skip("not supported by the BasicParser")
    @pytest.mark.test
    def testUnambiguousPartialLongOption2(self) -> None:
        try:
            pass
        except Exception as e:
            self.fail(f"An exception occurred: {e}")

    @unittest.skip("not supported by the BasicParser")
    @pytest.mark.test
    def testUnambiguousPartialLongOption3(self) -> None:
        try:
            pass
        except Exception as e:
            self.fail(f"An exception occurred: {e}")

    @unittest.skip("not supported by the BasicParser")
    @pytest.mark.test
    def testUnambiguousPartialLongOption4(self) -> None:
        try:
            pass
        except Exception as e:
            self.fail(f"An exception occurred: {e}")

    @unittest.skip("not supported by the BasicParser")
    @pytest.mark.test
    def testUnrecognizedOptionWithBursting(self) -> None:
        try:
            pass
        except Exception as e:
            self.fail(f"An exception occurred: {e}")
    

    # Class Methods End
