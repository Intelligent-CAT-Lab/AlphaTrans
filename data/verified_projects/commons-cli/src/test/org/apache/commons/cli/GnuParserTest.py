# Imports Begin
from src.main.org.apache.commons.cli.GnuParser import *
from src.main.org.apache.commons.cli.CommandLineParser import *
import unittest
from src.test.org.apache.commons.cli.ParserTestCase import ParserTestCase

# Imports End


class GnuParserTest(ParserTestCase):

    # Class Fields Begin
    # Class Fields End

    # Class Methods Begin
    @classmethod
    def setUpClass(cls):
        pass

    def setUp(self) -> None:
        super().setUp(GnuParser())

    @unittest.skip("not supported by the GnuParser")
    def test_AmbiguousLongWithoutEqualSingleDash(self) -> None:
        try:
            pass
        except Exception as e:
            self.fail(f"An exception occurred: {e}")

    @unittest.skip("not supported by the GnuParser")
    def test_AmbiguousPartialLongOption1(self) -> None:
        try:
            pass
        except Exception as e:
            self.fail(f"An exception occurred: {e}")

    @unittest.skip("not supported by the GnuParser")
    def test_AmbiguousPartialLongOption2(self) -> None:
        try:
            pass
        except Exception as e:
            self.fail(f"An exception occurred: {e}")

    @unittest.skip("not supported by the GnuParser")
    def test_AmbiguousPartialLongOption3(self) -> None:
        try:
            pass
        except Exception as e:
            self.fail(f"An exception occurred: {e}")

    @unittest.skip("not supported by the GnuParser")
    def test_AmbiguousPartialLongOption4(self) -> None:
        try:
            pass
        except Exception as e:
            self.fail(f"An exception occurred: {e}")

    @unittest.skip("not supported by the GnuParser")
    def test_Bursting(self) -> None:
        try:
            pass
        except Exception as e:
            self.fail(f"An exception occurred: {e}")

    @unittest.skip("not supported by the GnuParser")
    def test_DoubleDash2(self) -> None:
        try:
            pass
        except Exception as e:
            self.fail(f"An exception occurred: {e}")

    @unittest.skip("not supported by the GnuParser")
    def test_LongWithoutEqualSingleDash(self) -> None:
        try:
            pass
        except Exception as e:
            self.fail(f"An exception occurred: {e}")

    @unittest.skip("not supported by the GnuParser")
    def test_LongWithUnexpectedArgument1(self) -> None:
        try:
            pass
        except Exception as e:
            self.fail(f"An exception occurred: {e}")

    @unittest.skip("not supported by the GnuParser")
    def test_LongWithUnexpectedArgument2(self) -> None:
        try:
            pass
        except Exception as e:
            self.fail(f"An exception occurred: {e}")

    @unittest.skip("not supported by the GnuParser")
    def test_MissingArgWithBursting(self) -> None:
        try:
            pass
        except Exception as e:
            self.fail(f"An exception occurred: {e}")
    
    @unittest.skip("not supported by the GnuParser (CLI-184)")
    def test_NegativeOption(self) -> None:
        try:
            pass
        except Exception as e:
            self.fail(f"An exception occurred: {e}")

    @unittest.skip("not supported by the GnuParser")
    def test_PartialLongOptionSingleDash(self) -> None:
        try:
            pass
        except Exception as e:
            self.fail(f"An exception occurred: {e}")

    @unittest.skip("not supported by the GnuParser")
    def test_ShortWithUnexpectedArgument(self) -> None:
        try:
            pass
        except Exception as e:
            self.fail(f"An exception occurred: {e}")

    @unittest.skip("not supported by the GnuParser")
    def test_StopBursting(self) -> None:
        try:
            pass
        except Exception as e:
            self.fail(f"An exception occurred: {e}")

    @unittest.skip("not supported by the GnuParser")
    def test_StopBursting2(self) -> None:
        try:
            pass
        except Exception as e:
            self.fail(f"An exception occurred: {e}")

    @unittest.skip("not supported by the GnuParser")
    def test_UnambiguousPartialLongOption1(self) -> None:
        try:
            pass
        except Exception as e:
            self.fail(f"An exception occurred: {e}")

    @unittest.skip("not supported by the GnuParser")
    def test_UnambiguousPartialLongOption2(self) -> None:
        try:
            pass
        except Exception as e:
            self.fail(f"An exception occurred: {e}")

    @unittest.skip("not supported by the GnuParser")
    def test_UnambiguousPartialLongOption3(self) -> None:
        try:
            pass
        except Exception as e:
            self.fail(f"An exception occurred: {e}")

    @unittest.skip("not supported by the GnuParser")
    def test_UnambiguousPartialLongOption4(self) -> None:
        try:
            pass
        except Exception as e:
            self.fail(f"An exception occurred: {e}")

    @unittest.skip("not supported by the GnuParser")
    def test_UnrecognizedOptionWithBursting(self) -> None:
        try:
            pass
        except Exception as e:
            self.fail(f"An exception occurred: {e}")

    # Class Methods End
