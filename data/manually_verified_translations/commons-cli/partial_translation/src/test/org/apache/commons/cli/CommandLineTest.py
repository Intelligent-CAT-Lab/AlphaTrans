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

        options = Options()
        optI = OptionBuilder.builder1("i").hasArg0().type_(int).build()
        optF = OptionBuilder.builder1("f").hasArg0().build()
        options.addOption0(optI)
        options.addOption0(optF)
        parser = DefaultParser(2, False, None)
        cmd = parser.parse0(options, ["-i", "123", "-f", "foo"])
        self.assertIsNone(cmd.getOptionValue2(None))
        self.assertIsNone(cmd.getParsedOptionValue1(None))

    def testGetParsedOptionValueWithOption(self) -> None:

        options = Options()
        optI = OptionBuilder.builder1("i").hasArg0().type_(Number).build()
        optF = OptionBuilder.builder1("f").hasArg0().build()
        options.addOption0(optI)
        options.addOption0(optF)

        parser = DefaultParser(2, False, None)
        cmd = parser.parse0(options, ["-i", "123", "-f", "foo"])

        self.assertEqual(123, int(cmd.getParsedOptionValue1(optI)))
        self.assertEqual("foo", cmd.getParsedOptionValue1(optF))

    def testGetParsedOptionValueWithChar(self) -> None:

        options = Options()
        options.addOption0(Option.builder1("i").hasArg0().type_(int).build())
        options.addOption0(Option.builder1("f").hasArg0().build())

        parser = DefaultParser(2, False, None)
        cmd = parser.parse0(options, ["-i", "123", "-f", "foo"])

        self.assertEqual(123, cmd.getParsedOptionValue0("i"))
        self.assertEqual("foo", cmd.getParsedOptionValue0("f"))

    def testGetParsedOptionValue(self) -> None:

        options = Options()
        options.addOption0(OptionBuilder.hasArg0().withType0(int).create2("i"))
        options.addOption0(OptionBuilder.hasArg0().create2("f"))

        parser = DefaultParser(2, False, None)
        cmd = parser.parse0(options, ["-i", "123", "-f", "foo"])

        self.assertEqual(123, cmd.getParsedOptionValue2("i"))
        self.assertEqual("foo", cmd.getParsedOptionValue2("f"))

    def testGetOptions(self) -> None:

        cmd = CommandLine()
        assert cmd.getOptions() is not None
        assert len(cmd.getOptions()) == 0

        cmd._addOption(Option.Option1("a", None))
        cmd._addOption(Option.Option1("b", None))
        cmd._addOption(Option.Option1("c", None))

        assert len(cmd.getOptions()) == 3

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
        assert props is not None, "null properties"
        assert len(props) == 4, "number of properties in " + str(props)
        assert props.getProperty("param1") == "value1", "property 1"
        assert props.getProperty("param2") == "value2", "property 2"
        assert props.getProperty("param3") == "true", "property 3"
        assert props.getProperty("param4") == "value4", "property 4"

        assert (
            cl.getOptionProperties0(optionProperty).getProperty("foo") == "bar"
        ), "property with long format"

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
        assert props is not None, "null properties"
        assert len(props) == 4, "number of properties in " + str(props)
        assert props.getProperty("param1") == "value1", "property 1"
        assert props.getProperty("param2") == "value2", "property 2"
        assert props.getProperty("param3") == "true", "property 3"
        assert props.getProperty("param4") == "value4", "property 4"

        assert (
            cl.getOptionProperties1("property").getProperty("foo") == "bar"
        ), "property with long format"

    def testBuilder(self) -> None:

        builder = Builder()
        builder.addArg("foo").addArg("bar")
        builder.addOption(Option.builder1("T").build())
        cmd = builder.build()

        self.assertEqual("foo", cmd.getArgs()[0])
        self.assertEqual("bar", cmd.getArgList()[1])
        self.assertEqual("T", cmd.getOptions()[0].getOpt())
