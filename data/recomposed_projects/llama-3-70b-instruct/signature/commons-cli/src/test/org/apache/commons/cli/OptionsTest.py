from __future__ import annotations
import re
import os
import typing
from typing import *
import unittest
import pytest
import io
import unittest
from src.main.org.apache.commons.cli.CommandLine import *
from src.main.org.apache.commons.cli.MissingOptionException import *
from src.main.org.apache.commons.cli.Option import *
from src.main.org.apache.commons.cli.OptionBuilder import *
from src.main.org.apache.commons.cli.OptionGroup import *
from src.main.org.apache.commons.cli.Options import *
from src.main.org.apache.commons.cli.ParseException import *
from src.main.org.apache.commons.cli.PosixParser import *


class OptionsTest(unittest.TestCase):

    def testToString(self) -> None:
        options = Options()
        options.addOption3("f", "foo", True, "Foo")
        options.addOption3("b", "bar", False, "Bar")

        s = options.toString()
        self.assertIsNotNone("null string returned", s)
        self.assertTrue("foo option missing", s.lower().contains("foo"))
        self.assertTrue("bar option missing", s.lower().contains("bar"))

    def testSimple(self) -> None:
        opts = Options()

        opts.addOption1("a", False, "toggle -a")
        opts.addOption1("b", True, "toggle -b")

        self.assertTrue(opts.hasOption("a"))
        self.assertTrue(opts.hasOption("b"))

    def testMissingOptionsException(self) -> None:
        options = Options()
        options.addOption0(OptionBuilder.isRequired0().create2("f"))
        options.addOption0(OptionBuilder.isRequired0().create2("x"))
        try:
            Parser().parse0(options, [])
            self.fail("Expected MissingOptionException to be thrown")
        except MissingOptionException as e:
            self.assertEqual("Missing required options: f, x", e.getMessage())

    def testMissingOptionException(self) -> None:
        options = Options()
        options.addOption0(OptionBuilder.isRequired0().create2("f"))
        try:
            PosixParser().parse0(options, [])
            self.fail("Expected MissingOptionException to be thrown")
        except MissingOptionException as e:
            self.assertEqual("Missing required option: f", e.getMessage())

    def testLong(self) -> None:
        opts = Options()

        opts.addOption3("a", "--a", False, "toggle -a")
        opts.addOption3("b", "--b", True, "set -b")

        self.assertTrue(opts.hasOption("a"))
        self.assertTrue(opts.hasOption("b"))

    def testHelpOptions(self) -> None:
        longOnly1: Option = OptionBuilder.withLongOpt("long-only1").create0()
        longOnly2: Option = OptionBuilder.withLongOpt("long-only2").create0()
        shortOnly1: Option = OptionBuilder.create2("1")
        shortOnly2: Option = OptionBuilder.create2("2")
        bothA: Option = OptionBuilder.withLongOpt("bothA").create2("a")
        bothB: Option = OptionBuilder.withLongOpt("bothB").create2("b")

        options: Options = Options()
        options.addOption0(longOnly1)
        options.addOption0(longOnly2)
        options.addOption0(shortOnly1)
        options.addOption0(shortOnly2)
        options.addOption0(bothA)
        options.addOption0(bothB)

        allOptions: typing.List[Option] = []
        allOptions.append(longOnly1)
        allOptions.append(longOnly2)
        allOptions.append(shortOnly1)
        allOptions.append(shortOnly2)
        allOptions.append(bothA)
        allOptions.append(bothB)

        helpOptions: typing.List[Option] = options.helpOptions()

        self.assertTrue(
            "Everything in all should be in help", helpOptions.containsAll(allOptions)
        )
        self.assertTrue(
            "Everything in help should be in all", allOptions.containsAll(helpOptions)
        )

    def testGetOptionsGroups(self) -> None:
        options = Options()

        group1 = OptionGroup()
        group1.addOption(OptionBuilder.create1("a"))
        group1.addOption(OptionBuilder.create1("b"))

        group2 = OptionGroup()
        group2.addOption(OptionBuilder.create1("x"))
        group2.addOption(OptionBuilder.create1("y"))

        options.addOptionGroup(group1)
        options.addOptionGroup(group2)

        self.assertIsNotNone(options.getOptionGroups())
        self.assertEqual(2, len(options.getOptionGroups()))

    def testGetMatchingOpts(self) -> None:
        options = Options()
        options.addOption0(OptionBuilder.withLongOpt("version").create0())
        options.addOption0(OptionBuilder.withLongOpt("verbose").create0())

        self.assertTrue(options.getMatchingOptions("foo").isEmpty())
        self.assertEqual(1, options.getMatchingOptions("version").size())
        self.assertEqual(2, options.getMatchingOptions("ver").size())

    def testDuplicateSimple(self) -> None:
        opts = Options()
        opts.addOption1("a", False, "toggle -a")
        opts.addOption1("a", True, "toggle -a*")

        self.assertEqual("last one in wins", opts.getOption("a").getDescription())

    def testDuplicateLong(self) -> None:
        opts = Options()
        opts.addOption3("a", "--a", False, "toggle -a")
        opts.addOption3("a", "--a", False, "toggle -a*")
        self.assertEqual(
            "last one in wins", "toggle -a*", opts.getOption("a").getDescription()
        )
