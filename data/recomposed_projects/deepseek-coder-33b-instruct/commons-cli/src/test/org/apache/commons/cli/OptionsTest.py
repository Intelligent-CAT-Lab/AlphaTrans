from __future__ import annotations
import unittest
import pytest
import io
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
        assert s is not None, "null string returned"
        assert "foo" in s.lower(), "foo option missing"
        assert "bar" in s.lower(), "bar option missing"

    def testSimple(self) -> None:

        opts = Options()

        opts.addOption1("a", False, "toggle -a")
        opts.addOption1("b", True, "toggle -b")

        assert opts.hasOption("a")
        assert opts.hasOption("b")

    def testMissingOptionsException(self) -> None:

        options = Options()
        options.addOption0(OptionBuilder.isRequired0().create2("f"))
        options.addOption0(OptionBuilder.isRequired0().create2("x"))

        try:
            PosixParser().parse0(options, [])
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

        assert opts.hasOption("a")
        assert opts.hasOption("b")

    def testHelpOptions(self) -> None:

        longOnly1 = OptionBuilder.withLongOpt("long-only1").create0()
        longOnly2 = OptionBuilder.withLongOpt("long-only2").create0()
        shortOnly1 = OptionBuilder.create2("1")
        shortOnly2 = OptionBuilder.create2("2")
        bothA = OptionBuilder.withLongOpt("bothA").create2("a")
        bothB = OptionBuilder.withLongOpt("bothB").create2("b")

        options = Options()
        options.addOption0(longOnly1)
        options.addOption0(longOnly2)
        options.addOption0(shortOnly1)
        options.addOption0(shortOnly2)
        options.addOption0(bothA)
        options.addOption0(bothB)

        allOptions = [longOnly1, longOnly2, shortOnly1, shortOnly2, bothA, bothB]

        helpOptions = options.helpOptions()

        assert all(
            option in helpOptions for option in allOptions
        ), "Everything in all should be in help"
        assert all(
            option in allOptions for option in helpOptions
        ), "Everything in help should be in all"

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

        assert options.getOptionGroups() is not None
        assert len(options.getOptionGroups()) == 2

    def testGetMatchingOpts(self) -> None:

        options = Options()
        options.addOption0(OptionBuilder.withLongOpt("version").create0())
        options.addOption0(OptionBuilder.withLongOpt("verbose").create0())

        assert len(options.getMatchingOptions("foo")) == 0
        assert len(options.getMatchingOptions("version")) == 1
        assert len(options.getMatchingOptions("ver")) == 2

    def testDuplicateSimple(self) -> None:

        opts = Options()
        opts.addOption1("a", False, "toggle -a")
        opts.addOption1("a", True, "toggle -a*")

        assert "last one in wins" == opts.getOption("a").getDescription(), "toggle -a*"

    def testDuplicateLong(self) -> None:

        opts = Options()
        opts.addOption3("a", "--a", False, "toggle -a")
        opts.addOption3("a", "--a", False, "toggle -a*")
        assert "last one in wins", "toggle -a*" == opts.getOption("a").getDescription()
