from __future__ import annotations
import re
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

        pass  # LLM could not translate this method

    def testGetParsedOptionValueWithOption(self) -> None:
        options = Options()
        optI = Option.builder1("i").hasArg0().type(Number).build()
        optF = Option.builder1("f").hasArg0().build()
        options.addOption0(optI)
        options.addOption0(optF)

        parser = DefaultParser(2, False, None)
        cmd = parser.parse0(options, ["-i", "123", "-f", "foo"])

        self.assertEqual(123, cmd.getParsedOptionValue1(optI).intValue())
        self.assertEqual("foo", cmd.getParsedOptionValue1(optF))

    def testGetParsedOptionValueWithChar(self) -> None:
        options = Options()
        options.addOption0(Option.builder1("i").hasArg0().type(Number).build())
        options.addOption0(Option.builder1("f").hasArg0().build())

        parser = DefaultParser(2, False, None)
        cmd = parser.parse0(options, ["-i", "123", "-f", "foo"])

        self.assertEqual(123, cmd.getParsedOptionValue0("i").intValue())
        self.assertEqual("foo", cmd.getParsedOptionValue0("f"))

    def testGetParsedOptionValue(self) -> None:

        pass  # LLM could not translate this method

    def testGetOptions(self) -> None:
        cmd = CommandLine()
        self.assertIsNotNone(cmd.getOptions())
        self.assertEqual(0, len(cmd.getOptions()))

        cmd._addOption(Option.Option1("a", None))
        cmd._addOption(Option.Option1("b", None))
        cmd._addOption(Option.Option1("c", None))

        self.assertEqual(3, len(cmd.getOptions()))

    def testGetOptionPropertiesWithOption(self) -> None:

        pass  # LLM could not translate this method

    def testGetOptionProperties(self) -> None:
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
        options.addOption0(
            OptionBuilder.withValueSeparator0().hasOptionalArgs1(2).create1("D")
        )
        options.addOption0(
            OptionBuilder.withValueSeparator0()
            .hasArgs1(2)
            .withLongOpt("property")
            .create0()
        )

        parser = GnuParser()
        cl = parser.parse0(options, args)

        props = cl.getOptionProperties1("D")
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
        builder = Builder()
        builder.addArg("foo").addArg("bar")
        builder.addOption(Option.builder1("T"))
        cmd = builder.build()

        self.assertEqual("foo", cmd.getArgs()[0])
        self.assertEqual("bar", cmd.getArgList()[1])
        self.assertEqual("T", cmd.getOptions()[0].getOpt())
