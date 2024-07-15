from __future__ import annotations
import re
import unittest
import pytest
import io
import unittest
from src.main.org.apache.commons.cli.CommandLine import *
from src.main.org.apache.commons.cli.CommandLineParser import *
from src.main.org.apache.commons.cli.DefaultParser import *
from src.main.org.apache.commons.cli.Options import *
from src.test.org.apache.commons.cli.ParserTestCase import *


class DefaultParserTest(ParserTestCase, unittest.TestCase):

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

        # Define the arguments
        args = ['-b"quoted string"']

        # Create an instance of the parser
        parser = DefaultParser()

        # Create an instance of the options
        options = Options()

        # Parse the arguments
        cl = parser.parse0(options, args)

        # Assert the result
        self.assertEqual(
            'Confirm -b"arg" keeps quotes', '"quoted string"', cl.getOptionValue4("b")
        )

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

        # Define the arguments
        args = ['--bfile="quoted string"']

        # Create an instance of the parser
        parser = DefaultParser()

        # Create an instance of the options
        options = Options()

        # Parse the arguments
        cl = parser.parse0(options, args)

        # Assert that the option value is as expected
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
        parser = (
            DefaultParser.builder()
            .setStripLeadingAndTrailingQuotes(False)
            .setAllowPartialMatching(False)
            .build()
        )
        self.assertEqual(DefaultParser, type(parser))

    def setUp(self) -> None:

        super().setUp()
        self._parser = DefaultParser(2, False, None)
