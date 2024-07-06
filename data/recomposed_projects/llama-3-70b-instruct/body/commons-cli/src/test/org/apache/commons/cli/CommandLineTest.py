from __future__ import annotations
import re
import configparser
import typing
from typing import *
import numbers
import unittest
import pytest
import io
import unittest
from src.main.org.apache.commons.cli.CommandLine import *
from src.main.org.apache.commons.cli.CommandLineParser import *
from src.main.org.apache.commons.cli.DefaultParser import *
from src.main.org.apache.commons.cli.GnuParser import *
from src.main.org.apache.commons.cli.Option import *
from src.main.org.apache.commons.cli.OptionBuilder import *
from src.main.org.apache.commons.cli.Options import *
from src.main.org.apache.commons.cli.Parser import *


class CommandLineTest(unittest.TestCase):

    def testNullhOption(self) -> None:
        options: Options = Options()
        optI: Option = Option.builder1("i").hasArg0().type(Number).build()
        optF: Option = Option.builder1("f").hasArg0().build()
        options.addOption0(optI)
        options.addOption0(optF)
        parser: CommandLineParser = DefaultParser(2, False, None)
        cmd: CommandLine = parser.parse0(options, ["-i", "123", "-f", "foo"])
        self.assertIsNone(cmd.getOptionValue2(None))
        self.assertIsNone(cmd.getParsedOptionValue1(None))

    def testGetParsedOptionValueWithOption(self) -> None:

        pass  # LLM could not translate this method

    def testGetParsedOptionValueWithChar(self) -> None:

        pass  # LLM could not translate this method

    def testGetParsedOptionValue(self) -> None:
        options: Options = Options()
        options.addOption0(OptionBuilder.hasArg0().withType0(Number).create2("i"))
        options.addOption0(OptionBuilder.hasArg0().create2("f"))

        parser: CommandLineParser = DefaultParser(2, False, None)
        cmd: CommandLine = parser.parse0(options, ["-i", "123", "-f", "foo"])

        self.assertEqual(123, cmd.getParsedOptionValue2("i").intValue())
        self.assertEqual("foo", cmd.getParsedOptionValue2("f"))

    def testGetOptions(self) -> None:
        cmd: CommandLine = CommandLine()
        self.assertIsNotNone(cmd.getOptions())
        self.assertEqual(0, len(cmd.getOptions()))

        cmd._addOption(Option.Option1("a", None))
        cmd._addOption(Option.Option1("b", None))
        cmd._addOption(Option.Option1("c", None))

        self.assertEqual(3, len(cmd.getOptions()))

    def testGetOptionPropertiesWithOption(self) -> None:
        args = [
            "-Dparam1=value1",
            "-Dparam2=value2",
            "-Dparam3",
            "-Dparam4=value4",
            "-D",
            "--property",
            "foo=bar",
        ]

        options = Options()
        optionD = OptionBuilder.withValueSeparator0().hasOptionalArgs1(2).create1("D")
        optionProperty = (
            OptionBuilder.withValueSeparator0()
            .hasArgs1(2)
            .withLongOpt("property")
            .create0()
        )
        options.addOption0(optionD)
        options.addOption0(optionProperty)

        parser = GnuParser()
        cl = parser.parse0(options, args)

        props = cl.getOptionProperties0(optionD)
        self.assertIsNotNone(props)
        self.assertEqual(4, len(props))
        self.assertEqual("value1", props["param1"])
        self.assertEqual("value2", props["param2"])
        self.assertEqual("true", props["param3"])
        self.assertEqual("value4", props["param4"])

        self.assertEqual("bar", cl.getOptionProperties0(optionProperty)["foo"])

    def testGetOptionProperties(self) -> None:
        args: typing.List[str] = [
            "-Dparam1=value1",
            "-Dparam2=value2",
            "-Dparam3",
            "-Dparam4=value4",
            "-D",
            "--property",
            "foo=bar",
        ]

        options: Options = Options()
        options.addOption0(
            OptionBuilder.withValueSeparator0().hasOptionalArgs1(2).create1("D")
        )
        options.addOption0(
            OptionBuilder.withValueSeparator0()
            .hasArgs1(2)
            .withLongOpt("property")
            .create0()
        )

        parser: Parser = GnuParser()
        cl: CommandLine = parser.parse0(options, args)

        props: typing.Union[configparser.ConfigParser, typing.Dict] = (
            cl.getOptionProperties1("D")
        )
        self.assertIsNotNone("null properties", props)
        self.assertEqual("number of properties in " + props, 4, props.size())
        self.assertEqual("property 1", "value1", props.getProperty("param1"))
        self.assertEqual("property 2", "value2", props.getProperty("param2"))
        self.assertEqual("property 3", "true", props.getProperty("param3"))
        self.assertEqual("property 4", "value4", props.getProperty("param4"))

        self.assertEqual(
            "property with long format",
            "bar",
            cl.getOptionProperties1("property").getProperty("foo"),
        )

    def testBuilder(self) -> None:
        builder: Builder = Builder()
        builder.addArg("foo").addArg("bar")
        builder.addOption(Option.builder1("T").build())
        cmd: CommandLine = builder.build()

        self.assertEqual("foo", cmd.getArgs()[0])
        self.assertEqual("bar", cmd.getArgList()[1])
        self.assertEqual("T", cmd.getOptions()[0].getOpt())
