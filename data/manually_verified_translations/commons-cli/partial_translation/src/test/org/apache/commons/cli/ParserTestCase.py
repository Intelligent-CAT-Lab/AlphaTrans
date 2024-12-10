from __future__ import annotations
import re
import os
import unittest
import pytest
from abc import ABC
import io
import typing
from typing import *
import unittest
import configparser
from src.main.org.apache.commons.cli.AmbiguousOptionException import *
from src.main.org.apache.commons.cli.CommandLine import *
from src.main.org.apache.commons.cli.CommandLineParser import *
from src.main.org.apache.commons.cli.DefaultParser import *
from src.main.org.apache.commons.cli.MissingArgumentException import *
from src.main.org.apache.commons.cli.MissingOptionException import *
from src.main.org.apache.commons.cli.Option import *
from src.main.org.apache.commons.cli.OptionBuilder import *
from src.main.org.apache.commons.cli.OptionGroup import *
from src.main.org.apache.commons.cli.Options import *
from src.main.org.apache.commons.cli.ParseException import *
from src.main.org.apache.commons.cli.Parser import *
from src.main.org.apache.commons.cli.UnrecognizedOptionException import *


class ParserTestCase(ABC, unittest.TestCase):

    _options: Options = None

    _parser: CommandLineParser = None

    def testWithRequiredOption(self) -> None:

        args = ["-b", "file"]

        self._options = Options()
        self._options.addOption3("a", "enable-a", False, None)
        self._options.addOption0(
            OptionBuilder.withLongOpt("bfile").hasArg0().isRequired0().create1("b")
        )

        cl = self._parser.parse0(self._options, args)

        self.assertFalse(cl.hasOption2("a"))
        self.assertTrue(cl.hasOption2("b"))
        self.assertEqual("file", cl.getOptionValue4("b"))
        self.assertTrue(len(cl.getArgList()) == 0)

    def testUnrecognizedOptionWithBursting(self) -> None:

        args = ["-adbtoast", "foo", "bar"]

        try:
            self._parser.parse0(self._options, args)
            self.fail("UnrecognizedOptionException wasn't thrown")
        except UnrecognizedOptionException as e:
            self.assertEqual("-adbtoast", e.getOption())

    def testUnrecognizedOption(self) -> None:

        args = ["-a", "-d", "-b", "toast", "foo", "bar"]

        try:
            self._parser.parse0(self._options, args)
            self.fail("UnrecognizedOptionException wasn't thrown")
        except UnrecognizedOptionException as e:
            self.assertEqual("-d", e.getOption())

    def testUnlimitedArgs(self) -> None:

        args = ["-e", "one", "two", "-f", "alpha"]

        options = Options()
        options.addOption0(OptionBuilder.hasArgs0().create2("e"))
        options.addOption0(OptionBuilder.hasArgs0().create2("f"))

        cl = self._parser.parse0(options, args)

        self.assertTrue(cl.hasOption2("e"))
        self.assertEqual(len(cl.getOptionValues2("e")), 2)
        self.assertTrue(cl.hasOption2("f"))
        self.assertEqual(len(cl.getOptionValues2("f")), 1)

    def testUnambiguousPartialLongOption4(self) -> None:

        args = ["-ver=1"]

        self._options.addOption0(
            OptionBuilder.withLongOpt("verbose").hasOptionalArg().create0()
        )
        self._options.addOption0(OptionBuilder.withLongOpt("help").create0())

        cl = self._parser.parse0(self._options, args)

        self.assertTrue(cl.hasOption2("verbose"))
        self.assertEqual("1", cl.getOptionValue4("verbose"))

    def testUnambiguousPartialLongOption3(self) -> None:

        args = ["--verbose=1"]

        self._options.addOption0(
            OptionBuilder.withLongOpt("verbose").hasOptionalArg().create0()
        )
        self._options.addOption0(OptionBuilder.withLongOpt("help").create0())

        cl = self._parser.parse0(self._options, args)

        self.assertTrue(cl.hasOption2("verbose"))
        self.assertEqual("1", cl.getOptionValue4("verbose"))

    def testUnambiguousPartialLongOption2(self) -> None:

        args = ["-ver"]

        self._options.addOption0(OptionBuilder.withLongOpt("version").create0())
        self._options.addOption0(OptionBuilder.withLongOpt("help").create0())

        cl = self._parser.parse0(self._options, args)

        self.assertTrue(cl.hasOption2("version"))

    def testUnambiguousPartialLongOption1(self) -> None:

        args = ["--ver"]

        self._options.addOption0(OptionBuilder.withLongOpt("version").create0())
        self._options.addOption0(OptionBuilder.withLongOpt("help").create0())

        cl = self._parser.parse0(self._options, args)

        self.assertTrue(cl.hasOption2("version"))

    def testStopBursting2(self) -> None:

        args = ["-c", "foobar", "-btoast"]

        cl = self._parser.parse1(self._options, args, True)
        self.assertTrue("Confirm -c is set", cl.hasOption2("c"))
        self.assertEqual(
            "Confirm  2 extra args: " + str(len(cl.getArgList())),
            2,
            len(cl.getArgList()),
        )

        cl = self._parser.parse0(self._options, cl.getArgs())

        self.assertFalse("Confirm -c is not set", cl.hasOption2("c"))
        self.assertTrue("Confirm -b is set", cl.hasOption2("b"))
        self.assertEqual("Confirm arg of -b", "toast", cl.getOptionValue4("b"))
        self.assertEqual(
            "Confirm  1 extra arg: " + str(len(cl.getArgList())),
            1,
            len(cl.getArgList()),
        )
        self.assertEqual(
            "Confirm  value of extra arg: " + cl.getArgList()[0],
            "foobar",
            cl.getArgList()[0],
        )

    def testStopBursting(self) -> None:

        args = ["-azc"]

        cl = self._parser.parse1(self._options, args, True)
        self.assertTrue("Confirm -a is set", cl.hasOption2("a"))
        self.assertFalse("Confirm -c is not set", cl.hasOption2("c"))

        self.assertEqual(
            "Confirm  1 extra arg: " + str(len(cl.getArgList())),
            1,
            len(cl.getArgList()),
        )
        self.assertTrue("zc" in cl.getArgList())

    def testStopAtUnexpectedArg(self) -> None:

        args = ["-c", "foober", "-b", "toast"]

        cl = self._parser.parse1(self._options, args, True)
        self.assertTrue(cl.hasOption2("c"))
        self.assertEqual(len(cl.getArgList()), 3)

    def testStopAtNonOptionShort(self) -> None:

        args = ["-z", "-a", "-btoast"]

        cl = self._parser.parse1(self._options, args, True)
        self.assertFalse(cl.hasOption2("a"))
        self.assertEqual(len(cl.getArgList()), 3)

    def testStopAtNonOptionLong(self) -> None:

        args = ["--zop==1", "-abtoast", "--b=bar"]

        cl = self._parser.parse1(self._options, args, True)

        self.assertFalse(cl.hasOption2("a"), "Confirm -a is not set")
        self.assertFalse(cl.hasOption2("b"), "Confirm -b is not set")
        self.assertEqual(
            len(cl.getArgList()),
            3,
            "Confirm 3 extra args: " + str(len(cl.getArgList())),
        )

    def testStopAtExpectedArg(self) -> None:

        args = ["-b", "foo"]

        cl = self._parser.parse1(self._options, [args], True)

        self.assertTrue("Confirm -b is set", cl.hasOption0("b"))
        self.assertEqual("Confirm -b is set", "foo", cl.getOptionValue0("b"))
        self.assertTrue(
            "Confirm no extra args: " + str(len(cl.getArgList())),
            len(cl.getArgList()) == 0,
        )

    def testSingleDash(self) -> None:

        args = ["--copt", "-b", "-", "-a", "-"]

        cl = self._parser.parse0(self._options, args)

        self.assertTrue(cl.hasOption2("a"))
        self.assertTrue(cl.hasOption2("b"))
        self.assertEqual(cl.getOptionValue4("b"), "-")
        self.assertEqual(len(cl.getArgList()), 1)
        self.assertEqual(cl.getArgList()[0], "-")

    def testSimpleShort(self) -> None:

        args = ["-a", "-b", "toast", "foo", "bar"]

        cl = self._parser.parse0(self._options, args)

        self.assertTrue("Confirm -a is set", cl.hasOption2("a"))
        self.assertTrue("Confirm -b is set", cl.hasOption2("b"))
        self.assertEqual("Confirm arg of -b", "toast", cl.getOptionValue4("b"))
        self.assertEqual("Confirm size of extra args", 2, len(cl.getArgList()))

    def testSimpleLong(self) -> None:

        args = ["--enable-a", "--bfile", "toast", "foo", "bar"]

        cl = self._parser.parse0(self._options, args)

        self.assertTrue(cl.hasOption2("a"))
        self.assertTrue(cl.hasOption2("b"))
        self.assertEqual(cl.getOptionValue4("b"), "toast")
        self.assertEqual(cl.getOptionValue4("bfile"), "toast")
        self.assertEqual(len(cl.getArgList()), 2)

    def testShortWithUnexpectedArgument(self) -> None:

        args = ["-f=bar"]

        options = Options()
        options.addOption0(OptionBuilder.withLongOpt("foo").create1("f"))

        try:
            self._parser.parse0(options, args)
        except UnrecognizedOptionException as e:
            self.assertEqual("-f=bar", e.getOption())
            return

        self.fail("UnrecognizedOptionException not thrown")

    def testShortWithoutEqual(self) -> None:

        args = ["-fbar"]

        options = Options()
        options.addOption0(OptionBuilder.withLongOpt("foo").hasArg0().create1("f"))

        cl = self._parser.parse0(options, args)

        self.assertEqual("bar", cl.getOptionValue4("foo"))

    def testShortWithEqual(self) -> None:

        args = ["-f=bar"]

        options = Options()
        options.addOption0(OptionBuilder.withLongOpt("foo").hasArg0().create1("f"))

        cl = self._parser.parse0(options, args)

        self.assertEqual("bar", cl.getOptionValue4("foo"))

    def testShortOptionQuoteHandling(self) -> None:

        args = ["-b", '"quoted string"']

        cl = self._parser.parse0(self._options, args)

        self.assertEqual(
            'Confirm -b "arg" strips quotes', "quoted string", cl.getOptionValue4("b")
        )

    def testShortOptionConcatenatedQuoteHandling(self) -> None:

        args = ['-b"quoted string"']

        cl = self._parser.parse0(self._options, args)

        self.assertEqual(
            'Confirm -b"arg" strips quotes', "quoted string", cl.getOptionValue4("b")
        )

    def testReuseOptionsTwice(self) -> None:

        opts = Options()
        opts.addOption0(OptionBuilder.isRequired0().create1("v"))

        self._parser.parse0(opts, ["-v"])

        try:
            self._parser.parse0(opts, [])
            self.fail("MissingOptionException not thrown")
        except MissingOptionException:
            pass

    def testPropertyOverrideValues(self) -> None:

        opts = Options()
        opts.addOption0(OptionBuilder.hasOptionalArgs1(2).create1("i"))
        opts.addOption0(OptionBuilder.hasOptionalArgs0().create1("j"))

        args = ["-j", "found", "-i", "ink"]

        properties = configparser.ConfigParser()
        properties.set("DEFAULT", "j", "seek")

        cmd = self.__parse(self._parser, opts, args, properties)
        self.assertTrue(cmd.hasOption2("j"))
        self.assertEqual("found", cmd.getOptionValue4("j"))
        self.assertTrue(cmd.hasOption2("i"))
        self.assertEqual("ink", cmd.getOptionValue4("i"))
        self.assertFalse(cmd.hasOption2("fake"))

    def testPropertyOptionUnexpected(self) -> None:

        properties = {}
        properties["f"] = "true"

        try:
            self.__parse(self._parser, self._options, None, properties)
            self.fail("UnrecognizedOptionException expected")
        except UnrecognizedOptionException:
            pass

    def testPropertyOptionSingularValue(self) -> None:

        opts = Options()
        opts.addOption0(OptionBuilder.withLongOpt("hide").hasOptionalArgs1(2).create0())

        properties = configparser.ConfigParser()
        properties["DEFAULT"] = {"hide": "seek"}

        cmd = self.__parse(self._parser, opts, None, properties)
        self.assertTrue(cmd.hasOption2("hide"))
        self.assertEqual("seek", cmd.getOptionValue4("hide"))
        self.assertFalse(cmd.hasOption2("fake"))

    def testPropertyOptionRequired(self) -> None:

        opts = Options()
        opts.addOption0(OptionBuilder.isRequired0().create2("f"))

        properties = configparser.ConfigParser()
        properties.set("DEFAULT", "f", "true")

        cmd = self.__parse(self._parser, opts, None, properties)
        self.assertTrue(cmd.hasOption2("f"))

    def testPropertyOptionMultipleValues(self) -> None:

        opts = Options()
        opts.addOption0(OptionBuilder.hasArgs0().withValueSeparator1(",").create1("k"))

        properties = configparser.ConfigParser()
        properties.set("DEFAULT", "k", "one,two")

        values = ["one", "two"]

        cmd = self.__parse(self._parser, opts, None, properties)
        self.assertTrue(cmd.hasOption2("k"))
        self.assertEqual(values, cmd.getOptionValues0("k"))

    def testPropertyOptionGroup(self) -> None:

        opts = Options()

        group1 = OptionGroup()
        group1.addOption(Option.Option1("a", None))
        group1.addOption(Option.Option1("b", None))
        opts.addOptionGroup(group1)

        group2 = OptionGroup()
        group2.addOption(Option.Option1("x", None))
        group2.addOption(Option.Option1("y", None))
        opts.addOptionGroup(group2)

        args = ["-a"]

        properties = {}
        properties["b"] = "true"
        properties["x"] = "true"

        cmd = self.__parse(self._parser, opts, args, properties)

        self.assertTrue(cmd.hasOption2("a"))
        self.assertFalse(cmd.hasOption2("b"))
        self.assertTrue(cmd.hasOption2("x"))
        self.assertFalse(cmd.hasOption2("y"))

    def testPropertyOptionFlags(self) -> None:

        opts = Options()
        opts.addOption1("a", False, "toggle -a")
        opts.addOption3("c", "c", False, "toggle -c")
        opts.addOption0(OptionBuilder.hasOptionalArg().create1("e"))

        properties = {}
        properties["a"] = "true"
        properties["c"] = "yes"
        properties["e"] = "1"

        cmd = self.__parse(self._parser, opts, None, properties)
        self.assertTrue(cmd.hasOption2("a"))
        self.assertTrue(cmd.hasOption2("c"))
        self.assertTrue(cmd.hasOption2("e"))

        properties = {}
        properties["a"] = "false"
        properties["c"] = "no"
        properties["e"] = "0"

        cmd = self.__parse(self._parser, opts, None, properties)
        self.assertFalse(cmd.hasOption2("a"))
        self.assertFalse(cmd.hasOption2("c"))
        self.assertTrue(cmd.hasOption2("e"))

        properties = {}
        properties["a"] = "TRUE"
        properties["c"] = "nO"
        properties["e"] = "TrUe"

        cmd = self.__parse(self._parser, opts, None, properties)
        self.assertTrue(cmd.hasOption2("a"))
        self.assertFalse(cmd.hasOption2("c"))
        self.assertTrue(cmd.hasOption2("e"))

        properties = {}
        properties["a"] = "just a string"
        properties["e"] = ""

        cmd = self.__parse(self._parser, opts, None, properties)
        self.assertFalse(cmd.hasOption2("a"))
        self.assertFalse(cmd.hasOption2("c"))
        self.assertTrue(cmd.hasOption2("e"))

        properties = {}
        properties["a"] = "0"
        properties["c"] = "1"

        cmd = self.__parse(self._parser, opts, None, properties)
        self.assertFalse(cmd.hasOption2("a"))
        self.assertTrue(cmd.hasOption2("c"))

    def testPropertiesOption2(self) -> None:

        args = ["-Dparam1", "-Dparam2=value2", "-D"]

        options = Options()
        options.addOption0(
            OptionBuilder.withValueSeparator0().hasOptionalArgs1(2).create1("D")
        )

        cl = DefaultParser().parse0(options, args)

        props = cl.getOptionProperties1("D")
        assert props is not None, "null properties"
        assert len(props) == 2, f"number of properties in {props}"
        assert props.getProperty("param1") == "true", "property 1"
        assert props.getProperty("param2") == "value2", "property 2"

        argsleft = cl.getArgList()
        assert len(argsleft) == 0, "Should be no arg left"

    def testPropertiesOption1(self) -> None:

        args = ["-Jsource=1.5", "-J", "target", "1.5", "foo"]

        options = Options()
        options.addOption0(OptionBuilder.withValueSeparator0().hasArgs1(2).create1("J"))

        cl = DefaultParser().parse0(options, args)

        values = cl.getOptionValues2("J")
        assert values is not None, "null values"
        assert len(values) == 4, "number of values"
        assert values[0] == "source", "value 1"
        assert values[1] == "1.5", "value 2"
        assert values[2] == "target", "value 4"
        assert values[3] == "1.5", "value 4"

        argsleft = cl.getArgList()
        assert len(argsleft) == 1, "Should be 1 arg left"
        assert argsleft[0] == "foo", "Expecting foo"

    def testPartialLongOptionSingleDash(self) -> None:

        args = ["-ver"]

        options = Options()
        options.addOption0(OptionBuilder.withLongOpt("version").create0())
        options.addOption0(OptionBuilder.hasArg0().create1("v"))

        cl = self._parser.parse0(options, args)

        self.assertTrue(cl.hasOption2("version"))
        self.assertFalse(cl.hasOption2("v"))

    def testOptionGroupLong(self) -> None:

        group = OptionGroup()
        group.addOption(OptionBuilder.withLongOpt("foo").create0())
        group.addOption(OptionBuilder.withLongOpt("bar").create0())

        options = Options()
        options.addOptionGroup(group)

        cl = self._parser.parse0(options, ["--bar"])

        assert cl.hasOption2("bar")
        assert "selected option" == "bar", group.getSelected()

    def testOptionGroup(self) -> None:

        group = OptionGroup()
        group.addOption(OptionBuilder.create2("a"))
        group.addOption(OptionBuilder.create2("b"))

        options = Options()
        options.addOptionGroup(group)

        self._parser.parse0(options, ["-b"])

        self.assertEqual("selected option", "b", group.getSelected())

    def testOptionAndRequiredOption(self) -> None:

        args = ["-a", "-b", "file"]

        self._options.addOption3("a", "enable-a", False, "turn [a] on or off")
        self._options.addOption0(
            OptionBuilder.withLongOpt("bfile").hasArg0().isRequired0().create1("b")
        )

        cl = self._parser.parse0(self._options, args)

        self.assertTrue(cl.hasOption2("a"))
        self.assertTrue(cl.hasOption2("b"))
        self.assertEqual("file", cl.getOptionValue4("b"))
        self.assertTrue(cl.getArgList() == [])

    def testNegativeOption(self) -> None:

        args = ["-b", "-1"]

        self._options.addOption1("1", False, None)

        cl = self._parser.parse0(self._options, args)
        self.assertEqual("-1", cl.getOptionValue4("b"))

    def testNegativeArgument(self) -> None:

        args = ["-b", "-1"]

        cl = self._parser.parse0(self._options, args)
        self.assertEqual("-1", cl.getOptionValue4("b"))

    def testMultipleWithLong(self) -> None:

        args = ["--copt", "foobar", "--bfile", "toast"]

        cl = self._parser.parse1(self._options, args, True)
        self.assertTrue("Confirm -c is set", cl.hasOption2("c"))
        self.assertEqual(
            "Confirm  3 extra args: " + str(len(cl.getArgList())),
            3,
            len(cl.getArgList()),
        )

        cl = self._parser.parse0(self._options, cl.getArgs())

        self.assertFalse("Confirm -c is not set", cl.hasOption2("c"))
        self.assertTrue("Confirm -b is set", cl.hasOption2("b"))
        self.assertEqual("Confirm arg of -b", "toast", cl.getOptionValue4("b"))
        self.assertEqual(
            "Confirm  1 extra arg: " + str(len(cl.getArgList())),
            1,
            len(cl.getArgList()),
        )
        self.assertEqual(
            "Confirm  value of extra arg: " + cl.getArgList()[0],
            "foobar",
            cl.getArgList()[0],
        )

    def testMultiple(self) -> None:

        args = ["-c", "foobar", "-b", "toast"]

        cl = self._parser.parse1(self._options, args, True)
        self.assertTrue("Confirm -c is set", cl.hasOption2("c"))
        self.assertEqual(
            "Confirm  3 extra args: " + str(len(cl.getArgList())),
            3,
            len(cl.getArgList()),
        )

        cl = self._parser.parse0(self._options, cl.getArgs())

        self.assertFalse("Confirm -c is not set", cl.hasOption2("c"))
        self.assertTrue("Confirm -b is set", cl.hasOption2("b"))
        self.assertEqual("Confirm arg of -b", "toast", cl.getOptionValue4("b"))
        self.assertEqual(
            "Confirm  1 extra arg: " + str(len(cl.getArgList())),
            1,
            len(cl.getArgList()),
        )
        self.assertEqual(
            "Confirm  value of extra arg: " + cl.getArgList()[0],
            "foobar",
            cl.getArgList()[0],
        )

    def testMissingRequiredOptions(self) -> None:

        args = ["-a"]

        options = Options()
        options.addOption3("a", "enable-a", False, None)
        options.addOption0(
            OptionBuilder.withLongOpt("bfile").hasArg0().isRequired0().create1("b")
        )
        options.addOption0(
            OptionBuilder.withLongOpt("cfile").hasArg0().isRequired0().create1("c")
        )

        try:
            self._parser.parse0(options, args)
            self.fail("exception should have been thrown")
        except MissingOptionException as e:
            self.assertEqual(
                "Incorrect exception message",
                "Missing required options: b, c",
                e.getMessage(),
            )
            self.assertTrue("b" in e.getMissingOptions())
            self.assertTrue("c" in e.getMissingOptions())
        except ParseException:
            self.fail("expected to catch MissingOptionException")

    def testMissingRequiredOption(self) -> None:

        args = ["-a"]

        options = Options()
        options.addOption3("a", "enable-a", False, "turn [a] on or off")
        options.addOption0(
            OptionBuilder.withLongOpt("bfile").hasArg0().isRequired0().create1("b")
        )

        try:
            self._parser.parse0(options, args)
            self.fail("exception should have been thrown")
        except MissingOptionException as e:
            self.assertEqual(
                "Incorrect exception message",
                "Missing required option: b",
                e.getMessage(),
            )
            self.assertTrue(e.getMissingOptions().contains("b"))
        except ParseException as e:
            self.fail("expected to catch MissingOptionException")

    def testMissingRequiredGroup(self) -> None:

        group = OptionGroup()
        group.addOption(OptionBuilder.create2("a"))
        group.addOption(OptionBuilder.create2("b"))
        group.setRequired(True)

        options = Options()
        options.addOptionGroup(group)
        options.addOption0(OptionBuilder.isRequired0().create2("c"))

        try:
            self._parser.parse0(options, ["-c"])
            self.fail("MissingOptionException not thrown")
        except MissingOptionException as e:
            self.assertEqual(1, len(e.getMissingOptions()))
            self.assertTrue(isinstance(e.getMissingOptions()[0], OptionGroup))
        except ParseException:
            self.fail("Expected to catch MissingOptionException")

    def testMissingArgWithBursting(self) -> None:

        args = ["-acb"]

        caught = False

        try:
            self._parser.parse0(self._options, args)
        except MissingArgumentException as e:
            caught = True
            self.assertEqual("option missing an argument", "b", e.getOption().getOpt())

        self.assertTrue("Confirm MissingArgumentException caught", caught)

    def testMissingArg(self) -> None:

        args = ["-b"]

        caught = False

        try:
            self._parser.parse0(self._options, args)
        except MissingArgumentException as e:
            caught = True
            self.assertEqual("option missing an argument", "b", e.getOption().getOpt())

        self.assertTrue("Confirm MissingArgumentException caught", caught)

    def testLongWithUnexpectedArgument2(self) -> None:

        args = ["-foobar"]

        options = Options()
        options.addOption0(OptionBuilder.withLongOpt("foo").create1("f"))

        try:
            self._parser.parse0(options, args)
        except UnrecognizedOptionException as e:
            self.assertEqual("-foobar", e.getOption())
            return

        self.fail("UnrecognizedOptionException not thrown")

    def testLongWithUnexpectedArgument1(self) -> None:

        args = ["--foo=bar"]

        options = Options()
        options.addOption0(OptionBuilder.withLongOpt("foo").create1("f"))

        try:
            self._parser.parse0(options, args)
        except UnrecognizedOptionException as e:
            self.assertEqual("--foo=bar", e.getOption())
            return

        self.fail("UnrecognizedOptionException not thrown")

    def testLongWithoutEqualSingleDash(self) -> None:

        args = ["-foobar"]

        options = Options()
        options.addOption0(OptionBuilder.withLongOpt("foo").hasArg0().create1("f"))

        cl = DefaultParser().parse0(options, args)

        self.assertEqual("bar", cl.getOptionValue4("foo"))

    def testLongWithoutEqualDoubleDash(self) -> None:

        args = ["--foobar"]

        options = Options()
        options.addOption0(OptionBuilder.withLongOpt("foo").hasArg0().create1("f"))

        cl = DefaultParser().parse1(options, args, True)

        self.assertFalse(
            cl.hasOption2("foo")
        )  # foo isn't expected to be recognized with a double dash

    def testLongWithEqualSingleDash(self) -> None:

        args = ["-foo=bar"]

        options = Options()
        options.addOption0(OptionBuilder.withLongOpt("foo").hasArg0().create1("f"))

        cl = DefaultParser().parse0(options, args)

        self.assertEqual("bar", cl.getOptionValue4("foo"))

    def testLongWithEqualDoubleDash(self) -> None:

        args = ["--foo=bar"]

        options = Options()
        options.addOption0(OptionBuilder.withLongOpt("foo").hasArg0().create1("f"))

        cl = DefaultParser().parse0(options, args)

        self.assertEqual("bar", cl.getOptionValue4("foo"))

    def testLongOptionWithEqualsQuoteHandling(self) -> None:

        args = ['--bfile="quoted string"']

        cl = self._parser.parse0(self._options, args)

        self.assertEqual(
            'Confirm --bfile="arg" strips quotes',
            "quoted string",
            cl.getOptionValue4("b"),
        )

    def testLongOptionQuoteHandling(self) -> None:

        args = ["--bfile", '"quoted string"']

        cl = self._parser.parse0(self._options, args)

        self.assertEqual(
            'Confirm --bfile "arg" strips quotes',
            "quoted string",
            cl.getOptionValue4("b"),
        )

    def testDoubleDash2(self) -> None:

        self._options.addOption0(OptionBuilder.hasArg0().create1("n"))
        self._options.addOption0(OptionBuilder.create1("m"))

        try:
            self._parser.parse0(self._options, ["-n", "--", "-m"])
            self.fail("MissingArgumentException not thrown for option -n")
        except MissingArgumentException as e:
            self.assertIsNotNone(e.getOption(), "option null")
            self.assertEqual("n", e.getOpt())

    def testDoubleDash1(self) -> None:

        args = ["--copt", "--", "-b", "toast"]

        cl = self._parser.parse0(self._options, args)

        self.assertTrue("Confirm -c is set", cl.hasOption2("c"))
        self.assertFalse("Confirm -b is not set", cl.hasOption2("b"))
        self.assertEqual(
            "Confirm 2 extra args: " + str(len(cl.getArgList())),
            2,
            len(cl.getArgList()),
        )

    def testBursting(self) -> None:

        args = ["-acbtoast", "foo", "bar"]

        cl = self._parser.parse0(self._options, args)

        self.assertTrue("Confirm -a is set", cl.hasOption2("a"))
        self.assertTrue("Confirm -b is set", cl.hasOption2("b"))
        self.assertTrue("Confirm -c is set", cl.hasOption2("c"))
        self.assertEqual("Confirm arg of -b", "toast", cl.getOptionValue4("b"))
        self.assertEqual("Confirm size of extra args", 2, len(cl.getArgList()))

    def testArgumentStartingWithHyphen(self) -> None:

        args = ["-b", "-foo"]

        cl = self._parser.parse0(self._options, args)
        self.assertEqual("-foo", cl.getOptionValue4("b"))

    def testAmbiguousPartialLongOption4(self) -> None:

        args = ["-ver=1"]

        self._options.addOption0(OptionBuilder.withLongOpt("version").create0())
        self._options.addOption0(
            OptionBuilder.withLongOpt("verbose").hasOptionalArg().create0()
        )

        caught = False

        try:
            self._parser.parse0(self._options, args)
        except AmbiguousOptionException as e:
            caught = True
            self.assertEqual("Partial option", "-ver", e.getOption())
            self.assertIsNotNone("Matching options null", e.getMatchingOptions())
            self.assertEqual("Matching options size", 2, len(e.getMatchingOptions()))

        self.assertTrue("Confirm MissingArgumentException caught", caught)

    def testAmbiguousPartialLongOption3(self) -> None:

        args = ["--ver=1"]

        self._options.addOption0(OptionBuilder.withLongOpt("version").create0())
        self._options.addOption0(
            OptionBuilder.withLongOpt("verbose").hasOptionalArg().create0()
        )

        caught = False

        try:
            self._parser.parse0(self._options, args)
        except AmbiguousOptionException as e:
            caught = True
            self.assertEqual("Partial option", "--ver", e.getOption())
            self.assertIsNotNone("Matching options null", e.getMatchingOptions())
            self.assertEqual("Matching options size", 2, len(e.getMatchingOptions()))

        self.assertTrue("Confirm MissingArgumentException caught", caught)

    def testAmbiguousPartialLongOption2(self) -> None:

        args = ["-ver"]

        self._options.addOption0(OptionBuilder.withLongOpt("version").create0())
        self._options.addOption0(OptionBuilder.withLongOpt("verbose").create0())

        caught = False

        try:
            self._parser.parse0(self._options, args)
        except AmbiguousOptionException as e:
            caught = True
            self.assertEqual("Partial option", "-ver", e.getOption())
            self.assertIsNotNone("Matching options null", e.getMatchingOptions())
            self.assertEqual("Matching options size", 2, len(e.getMatchingOptions()))

        self.assertTrue("Confirm MissingArgumentException caught", caught)

    def testAmbiguousPartialLongOption1(self) -> None:

        args = ["--ver"]

        self._options.addOption0(OptionBuilder.withLongOpt("version").create0())
        self._options.addOption0(OptionBuilder.withLongOpt("verbose").create0())

        caught = False

        try:
            self._parser.parse0(self._options, args)
        except AmbiguousOptionException as e:
            caught = True
            self.assertEqual("Partial option", "--ver", e.getOption())
            self.assertIsNotNone("Matching options null", e.getMatchingOptions())
            self.assertEqual("Matching options size", 2, len(e.getMatchingOptions()))

        self.assertTrue("Confirm MissingArgumentException caught", caught)

    def testAmbiguousLongWithoutEqualSingleDash(self) -> None:

        args = ["-b", "-foobar"]

        options = Options()
        options.addOption0(
            OptionBuilder.withLongOpt("foo").hasOptionalArg().create1("f")
        )
        options.addOption0(
            OptionBuilder.withLongOpt("bar").hasOptionalArg().create1("b")
        )

        cl = self._parser.parse0(options, args)

        self.assertTrue(cl.hasOption2("b"))
        self.assertTrue(cl.hasOption2("f"))
        self.assertEqual("bar", cl.getOptionValue4("foo"))

    def setUp(self) -> None:

        self._options = Options()
        self._options.addOption3("a", "enable-a", False, "turn [a] on or off")
        self._options.addOption3("b", "bfile", True, "set the value of [b]")
        self._options.addOption3("c", "copt", False, "turn [c] on or off")

    def __parse(
        self,
        parser: CommandLineParser,
        opts: Options,
        args: typing.List[typing.List[str]],
        properties: typing.Union[configparser.ConfigParser, typing.Dict],
    ) -> CommandLine:

        if isinstance(parser, Parser):
            return parser.parse2(opts, args, properties)
        elif isinstance(parser, DefaultParser):
            return parser.parse2(opts, args, properties)
        else:
            raise NotImplementedError("Default options not supported by this parser")
