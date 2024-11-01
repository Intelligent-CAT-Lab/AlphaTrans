import pytest

from src.main.org.apache.commons.cli.Options import *
from src.main.org.apache.commons.cli.DefaultParser import *
from src.main.org.apache.commons.cli.CommandLineParser import *
from src.main.org.apache.commons.cli.CommandLine import *
from src.test.org.apache.commons.cli.ParserTestCase import ParserTestCase



class DefaultParserTest(ParserTestCase):

    __test__ = True

    def setUp(self) -> None:
        super().setUp()
        self._parser = DefaultParser(2, False, None)

    @pytest.mark.test
    def testBuilder(self) -> None:
        parser = DefaultParser.builder()\
                              .setStripLeadingAndTrailingQuotes(False)\
                              .setAllowPartialMatching(False)\
                              .build()
        self.assertTrue(isinstance(parser, DefaultParser))

    @pytest.mark.test
    def testLongOptionQuoteHandlingWithoutStrip(self) -> None:
        try:
            parser = DefaultParser.builder().setStripLeadingAndTrailingQuotes(False).build()
            args = ["--bfile", "\"quoted string\""]
            cl = parser.parse0(self._options, args)
            self.assertEqual(
                "\"quoted string\"",
                cl.getOptionValue4("b"),
                "Confirm --bfile \"arg\" keeps quotes"
            )
        except Exception as e:
            self.fail(f"An exception occurred: {e}")

    @pytest.mark.test
    def testLongOptionQuoteHandlingWithStrip(self) -> None:
        try:
            parser = DefaultParser.builder().setStripLeadingAndTrailingQuotes(True).build()
            args = ["--bfile", "\"quoted string\""]
            cl = parser.parse0(self._options, args)
            self.assertEqual(
                "quoted string",
                cl.getOptionValue4("b"),
                "Confirm --bfile \"arg\" strips quotes"
            )
        except Exception as e:
            self.fail(f"An exception occurred: {e}")

    @pytest.mark.test
    def testLongOptionWithEqualsQuoteHandling(self) -> None:
        try:
            args = ["--bfile=\"quoted string\""]
            cl = self._parser.parse0(self._options, args)
            self.assertEqual(
                "\"quoted string\"",
                cl.getOptionValue4("b"),
                "Confirm --bfile=\"arg\" strips quotes"
            )
        except Exception as e:
            self.fail(f"An exception occurred: {e}")

    @pytest.mark.test
    def testLongOptionWithEqualsQuoteHandlingWithoutStrip(self) -> None:
        try:
            parser = DefaultParser.builder().setStripLeadingAndTrailingQuotes(False).build()
            args = ["--bfile=\"quoted string\""]
            cl = parser.parse0(self._options, args)
            self.assertEqual(
                "\"quoted string\"",
                cl.getOptionValue4("b"),
                "Confirm --bfile=\"arg\" keeps quotes"
            )
        except Exception as e:
            self.fail(f"An exception occurred: {e}")

    @pytest.mark.test
    def testLongOptionWithEqualsQuoteHandlingWithStrip(self) -> None:
        try:
            parser = DefaultParser.builder().setStripLeadingAndTrailingQuotes(True).build()
            args = ["--bfile=\"quoted string\""]
            cl = parser.parse0(self._options, args)
            self.assertEqual(
                "quoted string",
                cl.getOptionValue4("b"),
                "Confirm --bfile=\"arg\" strips quotes"
            )
        except Exception as e:
            self.fail(f"An exception occurred: {e}")

    @pytest.mark.test
    def testShortOptionConcatenatedQuoteHandling(self) -> None:
        try:
            args = ["-b\"quoted string\""]
            cl = self._parser.parse0(self._options, args)
            self.assertEqual(
                "\"quoted string\"", 
                cl.getOptionValue4("b"), 
                "Confirm -b\"arg\" keeps quotes"
            )
        except Exception as e:
            self.fail(f"An exception occurred: {e}")

    @pytest.mark.test
    def testShortOptionQuoteHandlingWithoutStrip(self) -> None:
        try:
            parser = DefaultParser.builder().setStripLeadingAndTrailingQuotes(False).build()
            args = ["-b", "\"quoted string\""]
            cl = parser.parse0(self._options, args)
            self.assertEqual(
                "\"quoted string\"", 
                cl.getOptionValue4("b"),
                "Confirm -b \"arg\" keeps quotes"
            )
        except Exception as e:
            self.fail(f"An exception occurred: {e}")

    
    @pytest.mark.test
    def testShortOptionQuoteHandlingWithStrip(self) -> None:
        try:
            parser = DefaultParser.builder().setStripLeadingAndTrailingQuotes(True).build()
            args = ["-b", "\"quoted string\""]
            cl = parser.parse0(self._options, args)
            self.assertEqual(
                "quoted string", 
                cl.getOptionValue4("b"), 
                "Confirm -b \"arg\" strips quotes"
            )
        except Exception as e:
            self.fail(f"An exception occurred: {e}")
