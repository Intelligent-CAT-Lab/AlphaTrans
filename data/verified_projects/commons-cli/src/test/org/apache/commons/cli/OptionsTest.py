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

# Imports End


class OptionsTest(unittest.TestCase):

    # Class Fields Begin
    # Class Fields End

    # Class Methods Begin
    def testDuplicateLong(self) -> None:
        opts = Options()
        opts.addOption3("a", "--a", False, "toggle -a")
        opts.addOption3("a", "--a", False, "toggle -a*")
        self.assertEqual("toggle -a*", opts.getOption("a").getDescription(), "last one in wins")


    def testDuplicateSimple(self) -> None:
        opts = Options()
        opts.addOption1("a", False, "toggle -a")
        opts.addOption1("a", True, "toggle -a*")

        self.assertEqual("toggle -a*", opts.getOption("a").getDescription(), "last one in wins")


    def testGetMatchingOpts(self) -> None:
        options = Options()
        options.addOption0(OptionBuilder.withLongOpt("version").create0())
        options.addOption0(OptionBuilder.withLongOpt("verbose").create0())

        self.assertEqual(0, len(options.getMatchingOptions("foo")))
        self.assertEqual(1, len(options.getMatchingOptions("version")))
        self.assertEqual(2, len(options.getMatchingOptions("ver")))


    def testGetOptionsGroups(self) -> None:
        options = Options()

        group1 = OptionGroup()
        group1.addOption(OptionBuilder.create1('a'))
        group1.addOption(OptionBuilder.create1('b'))

        group2 = OptionGroup()
        group2.addOption(OptionBuilder.create1('x'))
        group2.addOption(OptionBuilder.create1('y'))

        options.addOptionGroup(group1)
        options.addOptionGroup(group2)

        self.assertIsNotNone(options.getOptionGroups())
        self.assertEqual(2, len(options.getOptionGroups()))


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
        allOptionsSet = set(allOptions)
        helpOptionsSet = set(helpOptions)
        self.assertTrue(
            allOptionsSet.issubset(helpOptionsSet), "Everything in all should be in help"
        )
        self.assertTrue(
            helpOptionsSet.issubset(allOptionsSet), "Everything in help should be in all"
        )
    
    
    def testLong(self) -> None:
        opts = Options()

        opts.addOption3("a", "--a", False, "toggle -a")
        opts.addOption3("b", "--b", True, "set -b")

        self.assertTrue(opts.hasOption("a"))
        self.assertTrue(opts.hasOption("b"))


    def testMissingOptionException(self) -> None:
        try:
            options = Options()
            options.addOption0(OptionBuilder.isRequired0().create2("f"))
            try:
                PosixParser().parse0(options, [])
                self.fail("Expected MissingOptionException to be thrown")
            except MissingOptionException as e:
                self.assertEqual("Missing required option: f", e.args[0])
        except Exception as e:
            self.fail(f"An exception occurred: {e}")
    
    
    def testMissingOptionsException(self) -> None:
        try:
            options = Options()
            options.addOption0(OptionBuilder.isRequired0().create2("f"))
            options.addOption0(OptionBuilder.isRequired0().create2("x"))
            try:
                PosixParser().parse0(options, [])
                self.fail("Expected MissingOptionException to be thrown")
            except MissingOptionException as e:
                self.assertEqual("Missing required options: f, x", e.args[0])
        except Exception as e:
            self.fail(f"An exception occurred: {e}")

    
    def testSimple(self) -> None:
        opts = Options()

        opts.addOption1("a", False, "toggle -a")
        opts.addOption1("b", True, "toggle -b")
        
        self.assertTrue(opts.hasOption("a"))
        self.assertTrue(opts.hasOption("b"))
    
    
    def testToString(self) -> None:
        options = Options()
        options.addOption3("f", "foo", True, "Foo")
        options.addOption3("b", "bar", False, "Bar")

        s = options.toString()
        self.assertIsNotNone(s, "null string returned")
        self.assertTrue("foo" in s.lower(), "foo option missing")
        self.assertTrue("bar" in s.lower(), "bar option missing")


    # Class Methods End
