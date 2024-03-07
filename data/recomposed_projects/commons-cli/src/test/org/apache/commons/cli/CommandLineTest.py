# Imports Begin
from src.main.org.apache.commons.cli.Parser import *
from src.main.org.apache.commons.cli.Options import *
from src.main.org.apache.commons.cli.OptionBuilder import *
from src.main.org.apache.commons.cli.Option import *
from src.main.org.apache.commons.cli.GnuParser import *
from src.main.org.apache.commons.cli.DefaultParser import *
from src.main.org.apache.commons.cli.CommandLineParser import *
from src.main.org.apache.commons.cli.CommandLine import *
import unittest
import typing
from typing import *
import numbers

# Imports End


class CommandLineTest(unittest.TestCase):

    # Class Fields Begin
    # Class Fields End

    # Class Methods Begin
    def testNullhOption(self) -> None:

        options = Options()
        opt_i = Option.builder1("i").hasArg0().type(Number).build()
        opt_f = Option.builder1("f").hasArg0().build()
        options.addOption0(opt_i)
        options.addOption0(opt_f)
        parser = DefaultParser(2, False, None)
        cmd = parser.parse0(options, ["-i", "123", "-f", "foo"])
        assertNull(cmd.getOptionValue2(None))
        assertNull(cmd.getParsedOptionValue1(None))

    def testGetParsedOptionValueWithOption(self) -> None:

        options = Options()
        opt_i = Option.builder1("i").hasArg0().type(Number).build()
        opt_f = Option.builder1("f").hasArg0().build()
        options.addOption0(opt_i)
        options.addOption0(opt_f)
        parser = DefaultParser(2, False, None)
        cmd = parser.parse0(options, ["-i", "123", "-f", "foo"])
        self.assertEqual(123, cmd.getParsedOptionValue1(opt_i))
        self.assertEqual("foo", cmd.getParsedOptionValue1(opt_f))

    def testGetParsedOptionValueWithChar(self) -> None:

        options = Options()
        options.addOption0(Option.builder1("i").hasArg0().type(Number).build())
        options.addOption0(Option.builder1("f").hasArg0().build())
        parser = DefaultParser(2, False, None)
        cmd = parser.parse0(options, ["-i", "123", "-f", "foo"])
        self.assertEqual(123, cmd.getParsedOptionValue0("i"))
        self.assertEqual("foo", cmd.getParsedOptionValue0("f"))

    def testGetParsedOptionValue(self) -> None:

        options = Options()
        options.addOption0(OptionBuilder.hasArg0().withType0(Number).create2("i"))
        options.addOption0(OptionBuilder.hasArg0().create2("f"))
        parser = DefaultParser(2, False, None)
        cmd = parser.parse0(options, ["-i", "123", "-f", "foo"])
        self.assertEqual(123, cmd.getParsedOptionValue2("i"))
        self.assertEqual("foo", cmd.getParsedOptionValue2("f"))

    def testGetOptions(self) -> None:

        pass  # LLM could not translate method body

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
        option_d = OptionBuilder.withValueSeparator0().hasOptionalArgs1(2).create1("D")
        option_property = (
            OptionBuilder.withValueSeparator0()
            .hasArgs1(2)
            .withLongOpt("property")
            .create0()
        )
        options.addOption0(option_d)
        options.addOption0(option_property)
        parser = GnuParser()
        cl = parser.parse0(options, args)
        props = cl.getOptionProperties0(option_d)
        self.assertIsNotNone(props)
        self.assertEqual(4, len(props))
        self.assertEqual("value1", props["param1"])
        self.assertEqual("value2", props["param2"])
        self.assertEqual("true", props["param3"])
        self.assertEqual("value4", props["param4"])
        self.assertEqual("bar", cl.getOptionProperties0(option_property)["foo"])

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
        self.assertIsNotNone(props)
        self.assertEqual(props.size(), 4)
        self.assertEqual(props.getProperty("param1"), "value1")
        self.assertEqual(props.getProperty("param2"), "value2")
        self.assertEqual(props.getProperty("param3"), "true")
        self.assertEqual(props.getProperty("param4"), "value4")
        self.assertEqual(cl.getOptionProperties1("property").getProperty("foo"), "bar")

    def testBuilder(self) -> None:

        pass  # LLM could not translate method body

    # Class Methods End
