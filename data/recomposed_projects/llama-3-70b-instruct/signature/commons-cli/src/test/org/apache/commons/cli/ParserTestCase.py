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

        options = Options()
        options.addOption3("a", "enable-a", False, None)
        options.addOption0(
            OptionBuilder.withLongOpt("bfile").hasArg0().isRequired0().create1("b")
        )

        cl = self._parser.parse0(options, args)

        self.assertFalse("Confirm -a is NOT set", cl.hasOption2("a"))
        self.assertTrue("Confirm -b is set", cl.hasOption2("b"))
        self.assertEqual("Confirm arg of -b", "file", cl.getOptionValue4("b"))
        self.assertTrue("Confirm NO of extra args", cl.getArgList().isEmpty())

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

        self.assertTrue("Confirm -e is set", cl.hasOption2("e"))
        self.assertEqual("number of arg for -e", 2, len(cl.getOptionValues2("e")))
        self.assertTrue("Confirm -f is set", cl.hasOption2("f"))
        self.assertEqual("number of arg for -f", 1, len(cl.getOptionValues2("f")))

    def testUnambiguousPartialLongOption4(self) -> None:
        args = ["-ver=1"]

        options = Options()
        options.addOption0(
            OptionBuilder.withLongOpt("verbose").hasOptionalArg().create0()
        )
        options.addOption0(OptionBuilder.withLongOpt("help").create0())

        cl = parser.parse0(options, args)

        self.assertTrue("Confirm --verbose is set", cl.hasOption2("verbose"))
        self.assertEqual("1", cl.getOptionValue4("verbose"))

    def testUnambiguousPartialLongOption3(self) -> None:
        args = ["--ver=1"]

        options = Options()
        options.addOption0(
            OptionBuilder.withLongOpt("verbose").hasOptionalArg().create0()
        )
        options.addOption0(OptionBuilder.withLongOpt("help").create0())

        cl = parser.parse0(options, args)

        self.assertTrue("Confirm --verbose is set", cl.hasOption2("verbose"))
        self.assertEqual("1", cl.getOptionValue4("verbose"))

    def testUnambiguousPartialLongOption2(self) -> None:
        args = ["-ver"]

        options = Options()
        options.addOption0(OptionBuilder.withLongOpt("version").create0())
        options.addOption0(OptionBuilder.withLongOpt("help").create0())

        cl = self._parser.parse0(options, args)

        self.assertTrue("Confirm --version is set", cl.hasOption2("version"))

    def testUnambiguousPartialLongOption1(self) -> None:
        args = ["--ver"]

        options = Options()
        options.addOption0(OptionBuilder.withLongOpt("version").create0())
        options.addOption0(OptionBuilder.withLongOpt("help").create0())

        cl = self._parser.parse0(options, args)

        self.assertTrue("Confirm --version is set", cl.hasOption2("version"))

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
            "Confirm  1 extra arg: " + str(cl.getArgList().size()),
            1,
            cl.getArgList().size(),
        )
        self.assertTrue(cl.getArgList().contains("zc"))

    def testStopAtUnexpectedArg(self) -> None:
        args = ["-c", "foober", "-b", "toast"]

        cl = self._parser.parse1(self._options, args, True)
        self.assertTrue("Confirm -c is set", cl.hasOption2("c"))
        self.assertEqual(
            "Confirm  3 extra args: " + str(cl.getArgList().size()),
            3,
            cl.getArgList().size(),
        )

    def testStopAtNonOptionShort(self) -> None:
        args = ["-z", "-a", "-btoast"]

        cl = self._parser.parse1(self._options, args, True)
        self.assertFalse("Confirm -a is not set", cl.hasOption2("a"))
        self.assertEqual(
            "Confirm  3 extra args: " + str(cl.getArgList().size()),
            3,
            cl.getArgList().size(),
        )

    def testStopAtNonOptionLong(self) -> None:
        args = ["--zop==1", "-abtoast", "--b=bar"]

        cl = self._parser.parse1(self._options, args, True)

        self.assertFalse("Confirm -a is not set", cl.hasOption2("a"))
        self.assertFalse("Confirm -b is not set", cl.hasOption2("b"))
        self.assertEqual(
            "Confirm  3 extra args: " + str(cl.getArgList().size()),
            3,
            cl.getArgList().size(),
        )

    def testStopAtExpectedArg(self) -> None:
        args: typing.List[str] = ["-b", "foo"]

        cl: CommandLine = self._parser.parse1(self._options, args, True)

        self.assertTrue("Confirm -b is set", cl.hasOption0("b"))
        self.assertEqual("Confirm -b is set", "foo", cl.getOptionValue0("b"))
        self.assertTrue(
            "Confirm no extra args: " + cl.getArgList().size(),
            cl.getArgList().isEmpty(),
        )

    def testSingleDash(self) -> None:
        args = ["--copt", "-b", "-", "-a", "-"]

        cl = self._parser.parse0(self._options, args)

        self.assertTrue("Confirm -a is set", cl.hasOption2("a"))
        self.assertTrue("Confirm -b is set", cl.hasOption2("b"))
        self.assertEqual("Confirm arg of -b", "-", cl.getOptionValue4("b"))
        self.assertEqual(
            "Confirm 1 extra arg: " + str(cl.getArgList().size()),
            1,
            cl.getArgList().size(),
        )
        self.assertEqual(
            "Confirm value of extra arg: " + cl.getArgList().get(0),
            "-",
            cl.getArgList().get(0),
        )

    def testSimpleShort(self) -> None:
        args = ["-a", "-b", "toast", "foo", "bar"]

        cl = self._parser.parse0(self._options, args)

        self.assertTrue("Confirm -a is set", cl.hasOption2("a"))
        self.assertTrue("Confirm -b is set", cl.hasOption2("b"))
        self.assertEqual("Confirm arg of -b", "toast", cl.getOptionValue4("b"))
        self.assertEqual("Confirm size of extra args", 2, cl.getArgList().size())

    def testSimpleLong(self) -> None:
        args = ["--enable-a", "--bfile", "toast", "foo", "bar"]

        cl = self._parser.parse0(self._options, args)

        self.assertTrue("Confirm -a is set", cl.hasOption2("a"))
        self.assertTrue("Confirm -b is set", cl.hasOption2("b"))
        self.assertEqual("Confirm arg of -b", "toast", cl.getOptionValue4("b"))
        self.assertEqual("Confirm arg of --bfile", "toast", cl.getOptionValue4("bfile"))
        self.assertEqual("Confirm size of extra args", 2, cl.getArgList().size())

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

        cl = parser.parse0(options, args)

        self.assertEqual("bar", cl.getOptionValue4("foo"))

    def testShortWithEqual(self) -> None:
        args = ["-f=bar"]

        options = Options()
        options.addOption0(OptionBuilder.withLongOpt("foo").hasArg0().create1("f"))

        cl = parser.parse0(options, args)

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
        except MissingOptionException as e:
            pass

    def testPropertyOverrideValues(self) -> None:
        opts = Options()
        opts.addOption0(OptionBuilder.hasOptionalArgs1(2).create1("i"))
        opts.addOption0(OptionBuilder.hasOptionalArgs0().create1("j"))

        args = ["-j", "found", "-i", "ink"]

        properties = {}
        properties["j"] = "seek"

        cmd = self.__parse(self._parser, opts, args, properties)
        self.assertTrue(cmd.hasOption2("j"))
        self.assertEqual("found", cmd.getOptionValue4("j"))
        self.assertTrue(cmd.hasOption2("i"))
        self.assertEqual("ink", cmd.getOptionValue4("i"))
        self.assertFalse(cmd.hasOption2("fake"))

    def testPropertyOptionUnexpected(self) -> None:
        opts = Options()
        properties = configparser.ConfigParser()
        properties["f"] = "true"
        try:
            self.__parse(self._parser, opts, None, properties)
            self.fail("UnrecognizedOptionException expected")
        except UnrecognizedOptionException as e:
            pass

    def testPropertyOptionSingularValue(self) -> None:
        opts = Options()
        opts.addOption0(OptionBuilder.hasOptionalArgs1(2).withLongOpt("hide").create0())

        properties = Properties()
        properties.setProperty("hide", "seek")

        cmd = self.__parse(self._parser, opts, None, properties)
        self.assertTrue(cmd.hasOption2("hide"))
        self.assertEqual("seek", cmd.getOptionValue4("hide"))
        self.assertFalse(cmd.hasOption2("fake"))

    def testPropertyOptionRequired(self) -> None:
        opts = Options()
        opts.addOption0(OptionBuilder.isRequired0().create2("f"))

        properties = configparser.ConfigParser()
        properties.setProperty("f", "true")

        cmd = self.__parse(self._parser, opts, None, properties)
        self.assertTrue(cmd.hasOption2("f"))

    def testPropertyOptionMultipleValues(self) -> None:
        opts = Options()
        opts.addOption0(OptionBuilder.hasArgs0().withValueSeparator1(",").create1("k"))

        properties = Properties()
        properties.setProperty("k", "one,two")

        values = ["one", "two"]

        cmd = self.__parse(self._parser, opts, None, properties)
        self.assertTrue(cmd.hasOption2("k"))
        self.assertArrayEquals(values, cmd.getOptionValues0("k"))

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

        properties = Properties()
        properties.setProperty("a", "true")
        properties.setProperty("c", "yes")
        properties.setProperty("e", "1")

        cmd = self.__parse(self._parser, opts, None, properties)
        self.assertTrue(cmd.hasOption2("a"))
        self.assertTrue(cmd.hasOption2("c"))
        self.assertTrue(cmd.hasOption2("e"))

        properties = Properties()
        properties.setProperty("a", "false")
        properties.setProperty("c", "no")
        properties.setProperty("e", "0")

        cmd = self.__parse(self._parser, opts, None, properties)
        self.assertFalse(cmd.hasOption2("a"))
        self.assertFalse(cmd.hasOption2("c"))
        self.assertTrue(cmd.hasOption2("e"))  # this option accepts an argument

        properties = Properties()
        properties.setProperty("a", "TRUE")
        properties.setProperty("c", "nO")
        properties.setProperty("e", "TrUe")

        cmd = self.__parse(self._parser, opts, None, properties)
        self.assertTrue(cmd.hasOption2("a"))
        self.assertFalse(cmd.hasOption2("c"))
        self.assertTrue(cmd.hasOption2("e"))

        properties = Properties()
        properties.setProperty("a", "just a string")
        properties.setProperty("e", "")

        cmd = self.__parse(self._parser, opts, None, properties)
        self.assertFalse(cmd.hasOption2("a"))
        self.assertFalse(cmd.hasOption2("c"))
        self.assertTrue(cmd.hasOption2("e"))

        properties = Properties()
        properties.setProperty("a", "0")
        properties.setProperty("c", "1")

        cmd = self.__parse(self._parser, opts, None, properties)
        self.assertFalse(cmd.hasOption2("a"))
        self.assertTrue(cmd.hasOption2("c"))

    def testPropertiesOption2(self) -> None:
        args: typing.List[str] = ["-Dparam1", "-Dparam2=value2", "-D"]

        options: Options = Options()
        options.addOption0(
            OptionBuilder.withValueSeparator0().hasOptionalArgs1(2).create1("D")
        )

        cl: CommandLine = parser.parse0(options, args)

        props: typing.Union[configparser.ConfigParser, typing.Dict] = (
            cl.getOptionProperties1("D")
        )
        self.assertIsNotNone("null properties", props)
        self.assertEqual("number of properties in " + props, 2, props.size())
        self.assertEqual("property 1", "true", props.getProperty("param1"))
        self.assertEqual("property 2", "value2", props.getProperty("param2"))

        argsleft: typing.List[typing.Any] = cl.getArgList()
        self.assertEqual("Should be no arg left", 0, argsleft.size())

    def testPropertiesOption1(self) -> None:
        args = ["-Jsource=1.5", "-J", "target", "1.5", "foo"]

        options = Options()
        options.addOption0(OptionBuilder.withValueSeparator0().hasArgs1(2).create1("J"))

        cl = parser.parse0(options, args)

        values = list(cl.getOptionValues2("J"))
        self.assertIsNotNone("null values", values)
        self.assertEqual("number of values", 4, len(values))
        self.assertEqual("value 1", "source", values[0])
        self.assertEqual("value 2", "1.5", values[1])
        self.assertEqual("value 3", "target", values[2])
        self.assertEqual("value 4", "1.5", values[3])

        argsleft = cl.getArgList()
        self.assertEqual("Should be 1 arg left", 1, len(argsleft))
        self.assertEqual("Expecting foo", "foo", argsleft[0])

    def testPartialLongOptionSingleDash(self) -> None:
        args = ["-ver"]

        options = Options()
        options.addOption0(OptionBuilder.withLongOpt("version").create0())
        options.addOption0(OptionBuilder.hasArg0().create1("v"))

        cl = self._parser.parse0(options, args)

        self.assertTrue("Confirm --version is set", cl.hasOption2("version"))
        self.assertFalse("Confirm -v is not set", cl.hasOption2("v"))

    def testOptionGroupLong(self) -> None:
        group = OptionGroup()
        group.addOption(OptionBuilder.withLongOpt("foo").create0())
        group.addOption(OptionBuilder.withLongOpt("bar").create0())

        options = Options()
        options.addOptionGroup(group)

        cl = self._parser.parse0(options, ["--bar"])

        self.assertTrue(cl.hasOption2("bar"))
        self.assertEqual("selected option", "bar", group.getSelected())

    def testOptionGroup(self) -> None:
        group: OptionGroup = OptionGroup()
        group.addOption(OptionBuilder.create2("a"))
        group.addOption(OptionBuilder.create2("b"))

        options: Options = Options()
        options.addOptionGroup(group)

        self._parser.parse0(options, ["-b"])

        self.assertEqual("selected option", "b", group.getSelected())

    def testOptionAndRequiredOption(self) -> None:
        args = ["-a", "-b", "file"]

        options = Options()
        options.addOption3("a", "enable-a", False, None)
        options.addOption0(
            OptionBuilder.withLongOpt("bfile").hasArg0().isRequired0().create1("b")
        )

        cl = self._parser.parse0(options, args)

        self.assertTrue("Confirm -a is set", cl.hasOption2("a"))
        self.assertTrue("Confirm -b is set", cl.hasOption2("b"))
        self.assertEqual("Confirm arg of -b", "file", cl.getOptionValue4("b"))
        self.assertTrue("Confirm NO of extra args", cl.getArgList().isEmpty())

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
        args: typing.List[str] = ["-c", "foobar", "-b", "toast"]

        cl: CommandLine = self._parser.parse1(self._options, args, True)
        self.assertTrue("Confirm -c is set", cl.hasOption2("c"))
        self.assertEqual(
            "Confirm  3 extra args: " + cl.getArgList().size(),
            3,
            cl.getArgList().size(),
        )

        cl = self._parser.parse0(self._options, cl.getArgs())

        self.assertFalse("Confirm -c is not set", cl.hasOption2("c"))
        self.assertTrue("Confirm -b is set", cl.hasOption2("b"))
        self.assertEqual("Confirm arg of -b", "toast", cl.getOptionValue4("b"))
        self.assertEqual(
            "Confirm  1 extra arg: " + cl.getArgList().size(), 1, cl.getArgList().size()
        )
        self.assertEqual(
            "Confirm  value of extra arg: " + cl.getArgList().get(0),
            "foobar",
            cl.getArgList().get(0),
        )

    def testMissingRequiredOptions(self) -> None:
        args: typing.List[str] = ["-a"]

        options: Options = Options()
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
            self.assertTrue(e.getMissingOptions().contains("b"))
            self.assertTrue(e.getMissingOptions().contains("c"))
        except ParseException as e:
            self.fail("expected to catch MissingOptionException")

    def testMissingRequiredOption(self) -> None:
        args: typing.List[str] = ["-a"]

        options: Options = Options()
        options.addOption3("a", "enable-a", False, None)
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
        group: OptionGroup = OptionGroup()
        group.addOption(OptionBuilder.create2("a"))
        group.addOption(OptionBuilder.create2("b"))
        group.setRequired(True)

        options: Options = Options()
        options.addOptionGroup(group)
        options.addOption0(OptionBuilder.isRequired0().create2("c"))

        try:
            self._parser.parse0(options, ["-c"])
            self.fail("MissingOptionException not thrown")
        except MissingOptionException as e:
            self.assertEqual(1, len(e.getMissingOptions()))
            self.assertTrue(isinstance(e.getMissingOptions()[0], OptionGroup))
        except ParseException as e:
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

        cl = parser.parse0(options, args)

        self.assertEqual("bar", cl.getOptionValue4("foo"))

    def testLongWithoutEqualDoubleDash(self) -> None:
        args = ["--foobar"]

        options = Options()
        options.addOption0(OptionBuilder.withLongOpt("foo").hasArg0().create1("f"))

        cl = parser.parse1(options, args, True)

        self.assertFalse(
            cl.hasOption2("foo")
        )  # foo isn't expected to be recognized with a double dash

    def testLongWithEqualSingleDash(self) -> None:
        args = ["-foo=bar"]

        options = Options()
        options.addOption0(OptionBuilder.withLongOpt("foo").hasArg0().create1("f"))

        cl = parser.parse0(options, args)

        self.assertEqual("bar", cl.getOptionValue4("foo"))

    def testLongWithEqualDoubleDash(self) -> None:
        args = ["--foo=bar"]

        options = Options()
        options.addOption0(OptionBuilder.withLongOpt("foo").hasArg0().create1("f"))

        cl = parser.parse0(options, args)

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
        options = Options()
        options.addOption0(OptionBuilder.hasArg0().create1("n"))
        options.addOption0(OptionBuilder.create1("m"))

        try:
            self._parser.parse0(options, ["-n", "--", "-m"])
            self.fail("MissingArgumentException not thrown for option -n")
        except MissingArgumentException as e:
            self.assertIsNotNone("option null", e.getOption())
            self.assertEqual("n", e.getOption().getOpt())

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
        self.assertEqual("Confirm size of extra args", 2, cl.getArgList().size())

    def testArgumentStartingWithHyphen(self) -> None:
        args = ["-b", "-foo"]

        cl = self._parser.parse0(self._options, args)
        self.assertEqual("-foo", cl.getOptionValue4("b"))

    def testAmbiguousPartialLongOption4(self) -> None:
        args = ["-ver=1"]

        options = Options()
        options.addOption0(OptionBuilder.withLongOpt("version").create0())
        options.addOption0(
            OptionBuilder.withLongOpt("verbose").hasOptionalArg().create0()
        )

        caught = False

        try:
            self._parser.parse0(options, args)
        except AmbiguousOptionException as e:
            caught = True
            self.assertEqual("-ver", e.getOption())
            self.assertIsNotNone(e.getMatchingOptions())
            self.assertEqual(2, len(e.getMatchingOptions()))

        self.assertTrue(caught)

    def testAmbiguousPartialLongOption3(self) -> None:
        args = ["--ver=1"]

        options = Options()
        options.addOption0(OptionBuilder.withLongOpt("version").create0())
        options.addOption0(
            OptionBuilder.withLongOpt("verbose").hasOptionalArg().create0()
        )

        caught = False

        try:
            self._parser.parse0(options, args)
        except AmbiguousOptionException as e:
            caught = True
            self.assertEqual("--ver", e.getOption())
            self.assertIsNotNone(e.getMatchingOptions())
            self.assertEqual(2, len(e.getMatchingOptions()))

        self.assertTrue(caught)

    def testAmbiguousPartialLongOption2(self) -> None:
        args = ["-ver"]

        options = Options()
        options.addOption0(OptionBuilder.withLongOpt("version").create0())
        options.addOption0(OptionBuilder.withLongOpt("verbose").create0())

        caught = False

        try:
            self._parser.parse0(options, args)
        except AmbiguousOptionException as e:
            caught = True
            self.assertEqual("-ver", e.getOption())
            self.assertIsNotNone(e.getMatchingOptions())
            self.assertEqual(2, len(e.getMatchingOptions()))

        self.assertTrue(caught)

    def testAmbiguousPartialLongOption1(self) -> None:
        args = ["--ver"]

        options = Options()
        options.addOption0(OptionBuilder.withLongOpt("version").create0())
        options.addOption0(OptionBuilder.withLongOpt("verbose").create0())

        caught = False

        try:
            self._parser.parse0(options, args)
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

        cl = parser.parse0(options, args)

        self.assertTrue(cl.hasOption2("b"))
        self.assertTrue(cl.hasOption2("f"))
        self.assertEqual("bar", cl.getOptionValue4("foo"))

    def setUp(self) -> None:
        self._options = (
            Options()
            .addOption3("a", "enable-a", False, "turn [a] on or off")
            .addOption3("b", "bfile", True, "set the value of [b]")
            .addOption3("c", "copt", False, "turn [c] on or off")
        )

    def __parse(
        self,
        parser: CommandLineParser,
        opts: Options,
        args: typing.List[str],
        properties: typing.Union[configparser.ConfigParser, typing.Dict],
    ) -> CommandLine:
        if isinstance(parser, Parser):
            return parser.parse2(opts, args, properties)
        if isinstance(parser, DefaultParser):
            return parser.parse2(opts, args, properties)
        raise NotImplementedError("Default options not supported by this parser")
