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

        cl = parser.parse0(self._options, args)

        self.assertEqual(
            'Confirm -b "arg" strips quotes', "quoted string", cl.getOptionValue4("b")
        )

    def testShortOptionQuoteHandlingWithoutStrip(self) -> None:

        parser = DefaultParser.builder().setStripLeadingAndTrailingQuotes(False).build()
        args = ["-b", '"quoted string"']

        cl = parser.parse0(self._options, args)

        self.assertEqual(
            'Confirm -b "arg" keeps quotes', '"quoted string"', cl.getOptionValue4("b")
        )

    def testShortOptionConcatenatedQuoteHandling(self) -> None:

        args = ['-b"quoted string"']

        cl = self._parser.parse0(self._options, args)

        self.assertEqual(
            'Confirm -b"arg" keeps quotes', '"quoted string"', cl.getOptionValue4("b")
        )

    def testLongOptionWithEqualsQuoteHandlingWithStrip(self) -> None:

        parser = DefaultParser.builder().setStripLeadingAndTrailingQuotes(True).build()
        args = ['--bfile="quoted string"']

        cl = parser.parse0(self._options, args)

        self.assertEqual(
            'Confirm --bfile="arg" strips quotes',
            "quoted string",
            cl.getOptionValue4("b"),
        )

    def testLongOptionWithEqualsQuoteHandlingWithoutStrip(self) -> None:

        parser = DefaultParser.builder().setStripLeadingAndTrailingQuotes(False).build()
        args = ['--bfile="quoted string"']

        cl = parser.parse0(self._options, args)

        self.assertEqual(
            'Confirm --bfile="arg" keeps quotes',
            '"quoted string"',
            cl.getOptionValue4("b"),
        )

    def testLongOptionWithEqualsQuoteHandling(self) -> None:

        args = ['--bfile="quoted string"']

        cl = self._parser.parse0(self._options, args)

        self.assertEqual(
            'Confirm --bfile="arg" strips quotes',
            '"quoted string"',
            cl.getOptionValue4("b"),
        )

    def testLongOptionQuoteHandlingWithStrip(self) -> None:

        parser = DefaultParser.builder().setStripLeadingAndTrailingQuotes(True).build()
        args = ["--bfile", '"quoted string"']

        cl = parser.parse0(self._options, args)

        self.assertEqual(
            'Confirm --bfile "arg" strips quotes',
            "quoted string",
            cl.getOptionValue4("b"),
        )

    def testLongOptionQuoteHandlingWithoutStrip(self) -> None:

        parser = DefaultParser.builder().setStripLeadingAndTrailingQuotes(False).build()
        args = ["--bfile", '"quoted string"']

        cl = parser.parse0(self._options, args)

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

        self._parser = DefaultParser(2, False, None)
