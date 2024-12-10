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
            "quoted string", cl.getOptionValue4("b"), 'Confirm -b "arg" strips quotes'
        )

    def testShortOptionQuoteHandlingWithoutStrip(self) -> None:

        parser = DefaultParser.builder().setStripLeadingAndTrailingQuotes(False).build()
        args = ["-b", '"quoted string"']

        cl = parser.parse0(self._options, args)

        self.assertEqual(
            '"quoted string"', cl.getOptionValue4("b"), 'Confirm -b "arg" keeps quotes'
        )

    def testShortOptionConcatenatedQuoteHandling(self) -> None:

        args = ['-b"quoted string"']

        cl = self._parser.parse0(self._options, args)

        self.assertEqual(
            '"quoted string"', cl.getOptionValue4("b"), 'Confirm -b"arg" keeps quotes'
        )

    def testLongOptionWithEqualsQuoteHandlingWithStrip(self) -> None:

        parser = DefaultParser.builder().setStripLeadingAndTrailingQuotes(True).build()
        args = ['--bfile="quoted string"']

        cl = parser.parse0(self._options, args)

        self.assertEqual(
            "quoted string",
            cl.getOptionValue4("b"),
            'Confirm --bfile="arg" strips quotes'
        )

    def testLongOptionWithEqualsQuoteHandlingWithoutStrip(self) -> None:

        parser = DefaultParser.builder().setStripLeadingAndTrailingQuotes(False).build()
        args = ['--bfile="quoted string"']

        cl = parser.parse0(self._options, args)

        self.assertEqual(
            '"quoted string"',
            cl.getOptionValue4("b"),
            'Confirm --bfile="arg" keeps quotes'
        )

    def testLongOptionWithEqualsQuoteHandling(self) -> None:

        args = ['--bfile="quoted string"']

        cl = self._parser.parse0(self._options, args)

        self.assertEqual(
            '"quoted string"',
            cl.getOptionValue4("b"),
            'Confirm --bfile="arg" strips quotes'
        )

    def testLongOptionQuoteHandlingWithStrip(self) -> None:

        parser = DefaultParser.builder().setStripLeadingAndTrailingQuotes(True).build()
        args = ["--bfile", '"quoted string"']

        cl = parser.parse0(self._options, args)

        self.assertEqual(
            "quoted string",
            cl.getOptionValue4("b"),
            'Confirm --bfile "arg" strips quotes'
        )

    def testLongOptionQuoteHandlingWithoutStrip(self) -> None:

        parser = DefaultParser.builder().setStripLeadingAndTrailingQuotes(False).build()
        args = ["--bfile", '"quoted string"']

        cl = parser.parse0(self._options, args)

        self.assertEqual(
            '"quoted string"',
            cl.getOptionValue4("b"),
            'Confirm --bfile "arg" keeps quotes'
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
