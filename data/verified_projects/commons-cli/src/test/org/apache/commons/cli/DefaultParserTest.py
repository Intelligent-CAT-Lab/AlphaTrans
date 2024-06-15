# Imports Begin
from src.main.org.apache.commons.cli.Options import *
from src.main.org.apache.commons.cli.DefaultParser import *
from src.main.org.apache.commons.cli.CommandLineParser import *
from src.main.org.apache.commons.cli.CommandLine import *
from src.test.org.apache.commons.cli.ParserTestCase import ParserTestCase

# Imports End


class DefaultParserTest(ParserTestCase):

    # Class Fields Begin
    # Class Fields End

    # Class Methods Begin
    @classmethod
    def setUpClass(cls):
        pass

    def setUp(self) -> None:
        super().setUp(DefaultParser(2, False, None))

    def testBuilder(self) -> None:
        parser = DefaultParser.builder()\
                              .setStripLeadingAndTrailingQuotes(False)\
                              .setAllowPartialMatching(False)\
                              .build()
        self.assertTrue(isinstance(parser, DefaultParser))

    def testLongOptionQuoteHandlingWithoutStrip(self) -> None:
        try:
            parser = DefaultParser.builder().setStripLeadingAndTrailingQuotes(False).build()
            args = ["--bfile", "\"quoted string\""]
            cl = parser.parse0(self.options, args)
            self.assertEqual(
                "\"quoted string\"",
                cl.getOptionValue4("b"),
                "Confirm --bfile \"arg\" keeps quotes"
            )
        except Exception as e:
            self.fail(f"An exception occurred: {e}")

    def testLongOptionQuoteHandlingWithStrip(self) -> None:
        try:
            parser = DefaultParser.builder().setStripLeadingAndTrailingQuotes(True).build()
            args = ["--bfile", "\"quoted string\""]
            cl = parser.parse0(self.options, args)
            self.assertEqual(
                "quoted string",
                cl.getOptionValue4("b"),
                "Confirm --bfile \"arg\" strips quotes"
            )
        except Exception as e:
            self.fail(f"An exception occurred: {e}")

    def testLongOptionWithEqualsQuoteHandling(self) -> None:
        try:
            args = ["--bfile=\"quoted string\""]
            cl = self.__parser.parse0(self.options, args)
            self.assertEqual(
                "\"quoted string\"",
                cl.getOptionValue4("b"),
                "Confirm --bfile=\"arg\" strips quotes"
            )
        except Exception as e:
            self.fail(f"An exception occurred: {e}")

    def testLongOptionWithEqualsQuoteHandlingWithoutStrip(self) -> None:
        try:
            parser = DefaultParser.builder().setStripLeadingAndTrailingQuotes(False).build()
            args = ["--bfile=\"quoted string\""]
            cl = parser.parse0(self.options, args)
            self.assertEqual(
                "\"quoted string\"",
                cl.getOptionValue4("b"),
                "Confirm --bfile=\"arg\" keeps quotes"
            )
        except Exception as e:
            self.fail(f"An exception occurred: {e}")

    def testLongOptionWithEqualsQuoteHandlingWithStrip(self) -> None:
        try:
            parser = DefaultParser.builder().setStripLeadingAndTrailingQuotes(True).build()
            args = ["--bfile=\"quoted string\""]
            cl = parser.parse0(self.options, args)
            self.assertEqual(
                "\"quoted string\"",
                cl.getOptionValue4("b"),
                "Confirm --bfile=\"arg\" keeps quotes"
            )
        except Exception as e:
            self.fail(f"An exception occurred: {e}")

    def testShortOptionConcatenatedQuoteHandling(self) -> None:
        try:
            args = ["-b", "\"quoted string\""]
            cl = self.__parser.parse0(self.options, args)
            self.assertEqual(
                "\"quoted string\"", 
                cl.getOptionValue4("b"), 
                "Confirm -b\"arg\" keeps quotes"
            )
        except Exception as e:
            self.fail(f"An exception occurred: {e}")

    def testShortOptionQuoteHandlingWithoutStrip(self) -> None:
        try:
            parser = DefaultParser.builder().setStripLeadingAndTrailingQuotes(False).build()
            args = ["-b", "\"quoted string\""]
            cl = parser.parse0(self.options, args)
            self.assertEqual(
                "\"quoted string\"", 
                cl.getOptionValue4("b"),
                "Confirm -b \"arg\" keeps quotes"
            )
        except Exception as e:
            self.fail(f"An exception occurred: {e}")

    
    def testShortOptionQuoteHandlingWithStrip(self) -> None:
        try:
            parser = DefaultParser.builder().setStripLeadingAndTrailingQuotes(True).build()
            args = ["-b", "\"quoted string\""]
            cl = parser.parse0(self.options, args)
            self.assertEqual(
                "quoted string", 
                cl.getOptionValue4("b"), 
                "Confirm -b \"arg\" strips quotes"
            )
        except Exception as e:
            self.fail(f"An exception occurred: {e}")

    # Class Methods End
