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
        self._parser = (
            DefaultParser.builder().setStripLeadingAndTrailingQuotes(True).build()
        )
        args = ["-b", '"quoted string"']

        cl = self._parser.parse0(self._options, args)

        self.assertEqual(
            'Confirm -b "arg" strips quotes', "quoted string", cl.getOptionValue4("b")
        )

    def testShortOptionQuoteHandlingWithoutStrip(self) -> None:
        self._parser = (
            DefaultParser.builder().setStripLeadingAndTrailingQuotes(False).build()
        )
        args = ["-b", '"quoted string"']
        cl = self._parser.parse0(self._options, args)
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
        self._parser = (
            DefaultParser.builder().setStripLeadingAndTrailingQuotes(True).build()
        )
        args = ['--bfile="quoted string"']
        cl = self._parser.parse0(self._options, args)
        self.assertEqual(
            'Confirm --bfile="arg" strips quotes',
            "quoted string",
            cl.getOptionValue4("b"),
        )

    def testLongOptionWithEqualsQuoteHandlingWithoutStrip(self) -> None:
        self._parser = (
            DefaultParser.builder().setStripLeadingAndTrailingQuotes(False).build()
        )
        args = ['--bfile="quoted string"']
        cl = self._parser.parse0(self._options, args)
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
        self._parser = (
            DefaultParser.builder().setStripLeadingAndTrailingQuotes(True).build()
        )
        args = ["--bfile", '"quoted string"']
        cl = self._parser.parse0(self._options, args)
        self.assertEqual(
            'Confirm --bfile "arg" strips quotes',
            "quoted string",
            cl.getOptionValue4("b"),
        )

    def testLongOptionQuoteHandlingWithoutStrip(self) -> None:
        self._parser = (
            DefaultParser.builder().setStripLeadingAndTrailingQuotes(False).build()
        )
        args = ["--bfile", '"quoted string"']
        cl = self._parser.parse0(self._options, args)
        self.assertEqual(
            'Confirm --bfile "arg" keeps quotes',
            '"quoted string"',
            cl.getOptionValue4("b"),
        )

    def testBuilder(self) -> None:
        self._parser = (
            DefaultParser.builder()
            .setStripLeadingAndTrailingQuotes(False)
            .setAllowPartialMatching(False)
            .build()
        )
        self.assertEqual(DefaultParser, self._parser.getClass())

    def setUp(self) -> None:
        self._options = Options()
        self._options.addOption3("a", "enable-a", False, "turn [a] on or off")
        self._options.addOption3("b", "bfile", True, "set the value of [b]")
        self._options.addOption3("c", "copt", False, "turn [c] on or off")
        self._parser = DefaultParser(2, False, None)
