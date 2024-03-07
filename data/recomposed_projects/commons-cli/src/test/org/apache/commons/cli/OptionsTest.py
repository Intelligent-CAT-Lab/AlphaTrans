# Imports Begin
from src.main.org.apache.commons.cli.PosixParser import *
from src.main.org.apache.commons.cli.ParseException import *
from src.main.org.apache.commons.cli.Options import *
from src.main.org.apache.commons.cli.OptionGroup import *
from src.main.org.apache.commons.cli.OptionBuilder import *
from src.main.org.apache.commons.cli.Option import *
from src.main.org.apache.commons.cli.MissingOptionException import *
from src.main.org.apache.commons.cli.CommandLine import *
import unittest
import os

# Imports End


class OptionsTest(unittest.TestCase):

    # Class Fields Begin
    # Class Fields End

    # Class Methods Begin
    def testToString(self) -> None:

        options = Options()
        options.addOption3("f", "foo", True, "Foo")
        options.addOption3("b", "bar", False, "Bar")
        s = options.toString()
        self.assertIsNotNone(s)
        self.assertTrue("foo" in s.lower())
        self.assertTrue("bar" in s.lower())

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

        pass  # LLM could not translate method body

    def testHelpOptions(self) -> None:

        long_only1 = OptionBuilder.withLongOpt("long-only1").create0()
        long_only2 = OptionBuilder.withLongOpt("long-only2").create0()
        short_only1 = OptionBuilder.create2("1")
        short_only2 = OptionBuilder.create2("2")
        both_a = OptionBuilder.withLongOpt("bothA").create2("a")
        both_b = OptionBuilder.withLongOpt("bothB").create2("b")
        options = Options()
        options.addOption0(long_only1)
        options.addOption0(long_only2)
        options.addOption0(short_only1)
        options.addOption0(short_only2)
        options.addOption0(both_a)
        options.addOption0(both_b)
        all_options = [long_only1, long_only2, short_only1, short_only2, both_a, both_b]
        help_options = options.helpOptions()
        self.assertTrue(
            "Everything in all should be in help", help_options.containsAll(all_options)
        )
        self.assertTrue(
            "Everything in help should be in all", all_options.containsAll(help_options)
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
        assert options.getOptionGroups() is not None
        assert len(options.getOptionGroups()) == 2

    def testGetMatchingOpts(self) -> None:

        options = Options()
        options.addOption0(OptionBuilder.withLongOpt("version").create0())
        options.addOption0(OptionBuilder.withLongOpt("verbose").create0())
        assert options.getMatchingOptions("foo") == []
        assert len(options.getMatchingOptions("version")) == 1
        assert len(options.getMatchingOptions("ver")) == 2

    def testDuplicateSimple(self) -> None:

        pass  # LLM could not translate method body

    def testDuplicateLong(self) -> None:

        pass  # LLM could not translate method body

    # Class Methods End
