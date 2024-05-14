# Imports Begin
from src.main.org.apache.commons.cli.CommandLineParser import *
from src.main.org.apache.commons.cli.BasicParser import *
import unittest
from ParserTestCase import ParserTestCase

# Imports End


class BasicParserTest(ParserTestCase):

    # Class Fields Begin
    # Class Fields End

    # Class Methods Begin
    @classmethod
    def setUpClass(cls):
        pass

    def setUp(self) -> None:
        super().setUp()
        self.__parser = BasicParser()

    @unittest.skip("not supported by the BasicParser")
    def test_AmbiguousLongWithoutEqualSingleDash(self) -> None:
        try:
            pass
        except Exception as e:
            self.fail(f"An exception occurred: {e}")

    @unittest.skip("not supported by the BasicParser")
    def test_AmbiguousPartialLongOption1(self) -> None:
        try:
            pass
        except Exception as e:
            self.fail(f"An exception occurred: {e}")

    @unittest.skip("not supported by the BasicParser")
    def test_AmbiguousPartialLongOption2(self) -> None:
        try:
            pass
        except Exception as e:
            self.fail(f"An exception occurred: {e}")

    @unittest.skip("not supported by the BasicParser")
    def test_AmbiguousPartialLongOption3(self) -> None:
        try:
            pass
        except Exception as e:
            self.fail(f"An exception occurred: {e}")

    @unittest.skip("not supported by the BasicParser")
    def test_AmbiguousPartialLongOption4(self) -> None:
        try:
            pass
        except Exception as e:
            self.fail(f"An exception occurred: {e}")

    @unittest.skip("not supported by the BasicParser")
    def test_Bursting(self) -> None:
        try:
            pass
        except Exception as e:
            self.fail(f"An exception occurred: {e}")

    @unittest.skip("not supported by the BasicParser")
    def test_DoubleDash2(self) -> None:
        try:
            pass
        except Exception as e:
            self.fail(f"An exception occurred: {e}")

    @unittest.skip("not supported by the BasicParser")
    def test_LongOptionWithEqualsQuoteHandling(self) -> None:
        try:
            pass
        except Exception as e:
            self.fail(f"An exception occurred: {e}")

    @unittest.skip("not supported by the BasicParser")
    def test_LongWithEqualDoubleDash(self) -> None:
        try:
            pass
        except Exception as e:
            self.fail(f"An exception occurred: {e}")

    @unittest.skip("not supported by the BasicParser")
    def test_LongWithEqualSingleDash(self) -> None:
        try:
            pass
        except Exception as e:
            self.fail(f"An exception occurred: {e}")

    @unittest.skip("not supported by the BasicParser")
    def test_LongWithoutEqualSingleDash(self) -> None:
        try:
            pass
        except Exception as e:
            self.fail(f"An exception occurred: {e}")

    @unittest.skip("not supported by the BasicParser")
    def test_MissingArgWithBursting(self) -> None:
        try:
            pass
        except Exception as e:
            self.fail(f"An exception occurred: {e}")

    @unittest.skip("not supported by the BasicParser (CLI-184)")
    def test_NegativeOption(self) -> None:
        try:
            pass
        except Exception as e:
            self.fail(f"An exception occurred: {e}")

    @unittest.skip("not supported by the BasicParser")
    def test_PartialLongOptionSingleDash(self) -> None:
        try:
            pass
        except Exception as e:
            self.fail(f"An exception occurred: {e}")

    @unittest.skip("not supported by the BasicParser")
    def test_PropertiesOption1(self) -> None:
        try:
            pass
        except Exception as e:
            self.fail(f"An exception occurred: {e}")
    
    @unittest.skip("not supported by the BasicParser")
    def test_PropertiesOption2(self) -> None:
        try:
            pass
        except Exception as e:
            self.fail(f"An exception occurred: {e}")

    @unittest.skip("not supported by the BasicParser")
    def test_ShortOptionConcatenatedQuoteHandling(self) -> None:
        try:
            pass
        except Exception as e:
            self.fail(f"An exception occurred: {e}")

    @unittest.skip("not supported by the BasicParser")
    def test_ShortWithEqual(self) -> None:
        try:
            pass
        except Exception as e:
            self.fail(f"An exception occurred: {e}")

    @unittest.skip("not supported by the BasicParser")
    def test_ShortWithoutEqual(self) -> None:
        try:
            pass
        except Exception as e:
            self.fail(f"An exception occurred: {e}")

    @unittest.skip("not supported by the BasicParser")
    def test_StopBursting(self) -> None:
        try:
            pass
        except Exception as e:
            self.fail(f"An exception occurred: {e}")

    @unittest.skip("not supported by the BasicParser")
    def test_StopBursting2(self) -> None:
        try:
            pass
        except Exception as e:
            self.fail(f"An exception occurred: {e}")

    @unittest.skip("not supported by the BasicParser")
    def test_UnambiguousPartialLongOption1(self) -> None:
        try:
            pass
        except Exception as e:
            self.fail(f"An exception occurred: {e}")

    @unittest.skip("not supported by the BasicParser")
    def test_UnambiguousPartialLongOption2(self) -> None:
        try:
            pass
        except Exception as e:
            self.fail(f"An exception occurred: {e}")

    @unittest.skip("not supported by the BasicParser")
    def test_UnambiguousPartialLongOption3(self) -> None:
        try:
            pass
        except Exception as e:
            self.fail(f"An exception occurred: {e}")

    @unittest.skip("not supported by the BasicParser")
    def test_UnambiguousPartialLongOption4(self) -> None:
        try:
            pass
        except Exception as e:
            self.fail(f"An exception occurred: {e}")

    @unittest.skip("not supported by the BasicParser")
    def test_UnrecognizedOptionWithBursting(self) -> None:
        try:
            pass
        except Exception as e:
            self.fail(f"An exception occurred: {e}")
    

    # Class Methods End
