# Imports Begin
from src.main.org.apache.commons.cli.ParserTestCase import *
from src.main.org.apache.commons.cli.Options import *
from src.main.org.apache.commons.cli.DefaultParser import *
from src.main.org.apache.commons.cli.CommandLineParser import *
from src.main.org.apache.commons.cli.CommandLine import *
import unittest
import ParserTestCase

# Imports End


class DefaultParserTest(ParserTestCase):

    # Class Fields Begin
    # Class Fields End

    # Class Methods Begin
    def setUp(self) -> None:
        super().setUp()
        self.__parser = DefaultParser(2, False, None)

    def test_Builder(self) -> None:
        parser = DefaultParser.builder()\
                              .setStripLeadingAndTrailingQuotes(False)\
                              .setAllowPartialMatching(False)\
                              .build()
        self.assertTrue(isinstance(parser, DefaultParser))

    def test_LongOptionQuoteHandlingWithoutStrip(self) -> None:
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

    def test_LongOptionQuoteHandlingWithStrip(self) -> None:
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

    def test_LongOptionWithEqualsQuoteHandling(self) -> None:
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

    def test_LongOptionWithEqualsQuoteHandlingWithoutStrip(self) -> None:
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

    def test_LongOptionWithEqualsQuoteHandlingWithStrip(self) -> None:
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

    def test_ShortOptionConcatenatedQuoteHandling(self) -> None:
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

    def test_ShortOptionQuoteHandlingWithoutStrip(self) -> None:
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

    
    def test_ShortOptionQuoteHandlingWithStrip(self) -> None:
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
