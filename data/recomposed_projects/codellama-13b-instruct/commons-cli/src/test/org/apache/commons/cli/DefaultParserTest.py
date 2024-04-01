# Imports Begin
from src.main.org.apache.commons.cli.ParserTestCase import *
from src.main.org.apache.commons.cli.Options import *
from src.main.org.apache.commons.cli.DefaultParser import *
from src.main.org.apache.commons.cli.CommandLineParser import *
from src.main.org.apache.commons.cli.CommandLine import *
import unittest

# Imports End


class DefaultParserTest(unittest.TestCase, ParserTestCase):

    # Class Fields Begin
    # Class Fields End

    # Class Methods Begin
    def testShortOptionQuoteHandlingWithStrip(self) -> None:

        parser = DefaultParser.builder().setStripLeadingAndTrailingQuotes(True).build()
        args = ["-b", '"quoted string"']
        cl = parser.parse0(options, args)
        self.assertEqual(
            'Confirm -b "arg" strips quotes', "quoted string", cl.getOptionValue4("b")
        )

    def testShortOptionQuoteHandlingWithoutStrip(self) -> None:

        parser = DefaultParser.builder().setStripLeadingAndTrailingQuotes(False).build()
        args = ["-b", '"quoted string"']
        cl = parser.parse0(options, args)
        self.assertEqual(
            'Confirm -b "arg" keeps quotes', '"quoted string"', cl.getOptionValue4("b")
        )

    def testShortOptionConcatenatedQuoteHandling(self) -> None:

        args = ['-b"quoted string"']
        cl = self.parse0(self.options, args)
        assert cl.getOptionValue4("b") == '"quoted string"'

    def testLongOptionWithEqualsQuoteHandlingWithStrip(self) -> None:

        parser = DefaultParser.builder().setStripLeadingAndTrailingQuotes(True).build()
        args = ['--bfile="quoted string"']
        cl = parser.parse0(options, args)
        self.assertEqual(
            'Confirm --bfile="arg" strips quotes',
            "quoted string",
            cl.getOptionValue4("b"),
        )

    def testLongOptionWithEqualsQuoteHandlingWithoutStrip(self) -> None:

        parser = DefaultParser.builder().setStripLeadingAndTrailingQuotes(False).build()
        args = ['--bfile="quoted string"']
        cl = parser.parse0(options, args)
        self.assertEqual(
            'Confirm --bfile="arg" keeps quotes',
            '"quoted string"',
            cl.getOptionValue4("b"),
        )

    def testLongOptionWithEqualsQuoteHandling(self) -> None:

        args = ['--bfile="quoted string"']
        cl = self.parse0(self.options, args)
        self.assertEqual(
            'Confirm --bfile="arg" strips quotes',
            '"quoted string"',
            cl.getOptionValue4("b"),
        )

    def testLongOptionQuoteHandlingWithStrip(self) -> None:

        parser = DefaultParser.builder().setStripLeadingAndTrailingQuotes(True).build()
        args = ["--bfile", '"quoted string"']
        cl = parser.parse0(options, args)
        self.assertEqual(
            'Confirm --bfile "arg" strips quotes',
            "quoted string",
            cl.getOptionValue4("b"),
        )

    def testLongOptionQuoteHandlingWithoutStrip(self) -> None:

        parser = DefaultParser.builder().setStripLeadingAndTrailingQuotes(False).build()
        args = ["--bfile", '"quoted string"']
        cl = parser.parse0(options, args)
        self.assertEqual(
            'Confirm --bfile "arg" keeps quotes',
            '"quoted string"',
            cl.getOptionValue4("b"),
        )

    def testBuilder(self) -> None:

        pass  # LLM could not translate method body

    def setUp(self) -> None:

        super().setUp()
        self.parser = DefaultParser(2, False, None)

    # Class Methods End
