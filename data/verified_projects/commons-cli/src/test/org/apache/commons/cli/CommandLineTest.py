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
from typing import *
import numbers

# Imports End


class CommandLineTest(unittest.TestCase):

    # Class Fields Begin
    # Class Fields End

    # Class Methods Begin
    def test_Builder(self) -> None:
        builder = CommandLine.Builder()
        builder.addArg("foo").addArg("bar")
        builder.addOption(Option.builder1("T").build())
        cmd = builder.build()

        self.assertEqual("foo", cmd.getArgs()[0])
        self.assertEqual("bar", cmd.getArgList().get(1))
        self.assertEqual("T", cmd.getOptions()[0].getOpt())

    def test_GetOptionProperties(self) -> None:
        try:
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
                OptionBuilder.withValueSeparator0()\
                .hasArgs1(2)\
                .withLongOpt("property")\
                .create0()
            )
            parser = GnuParser()
            cl = parser.parse0(options, args)
            props = cl.getOptionProperties1("D")
            self.assertIsNotNone(props, "None properties")
            self.assertEqual(4, len(props), "number of properties")
            self.assertEqual("value1", props.get("param1"), "property 1")
            self.assertEqual("value2", props.get("param2"), "property 2")
            self.assertEqual("true", props.get("param3"), "property 3")
            self.assertEqual("value4", props.get("param4"), "property 4")
            self.assertEqual(cl.getOptionProperties1("property").get("foo"), "bar", "property with long format")
        except Exception as e:
            self.fail(f"An exception occurred: {e}")

    def test_GetOptionPropertiesWithOption(self) -> None:
        try:
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
                OptionBuilder.withValueSeparator0()\
                .hasArgs1(2)\
                .withLongOpt("property")\
                .create0()
            )
            options.addOption0(optionD)
            options.addOption0(optionProperty)
            parser = GnuParser()
            cl = parser.parse0(options, args)
            props = cl.getOptionProperties0(optionD)
            self.assertIsNotNone(props, "None properties")
            self.assertEqual(4, len(props), "number of properties")
            self.assertEqual("value1", props.get("param1"), "property 1")
            self.assertEqual("value2", props.get("param2"), "property 2")
            self.assertEqual("true", props.get("param3"), "property 3")
            self.assertEqual("value4", props.get("param4"), "property 4")
            self.assertEqual("bar", cl.getOptionProperties0(optionProperty).get("foo"))
        except Exception as e:
            self.fail(f"An exception occurred: {e}")

    def test_GetOptions(self) -> None:
        cmd = commandLine()
        self.assertIsNotNone(cmd.getOptions())
        self.assertEqual(0, cmd.getOptions().length)

        cmd.addOption(Option.Option1("a", None))
        cmd.addOption(Option.Option1("b", None))
        cmd.addOption(Option.Option1("c", None))

        self.assertEqual(3, cmd.getOptions().length)

    def test_GetParsedOptionValue(self) -> None:
        try:
            options = Options()
            options.addOption0(OptionBuilder.hasArg0().withType0(numbers.Number).create2("i"))
            options.addOption0(OptionBuilder.hasArg0().create2("f"))
            parser = DefaultParser(2, False, None)
            cmd = parser.parse0(options, ["-i", "123", "-f", "foo"])
            self.assertEqual(123, int(cmd.getParsedOptionValue2("i")))
            self.assertEqual("foo", cmd.getParsedOptionValue2("f"))
        except Exception as e:
            self.fail(f"An exception occurred: {e}")

    def test_NullhOption(self) -> None:
        try:
            options = Options()
            optI = Option.builder1("i").hasArg0().type(numbers.Number).build()
            optF = Option.builder1("f").hasArg0().build()
            options.addOption0(optI)
            options.addOption0(optF)
            parser = DefaultParser(2, False, None)
            cmd = parser.parse0(options, ["-i", "123", "-f", "foo"])
            self.assertIsNone(cmd.getOptionValue2(None))
            self.assertIsNone(cmd.getParsedOptionValue1(None))
        except Exception as e:
            self.fail(f"An exception occurred: {e}")

    def test_GetParsedOptionValueWithOption(self) -> None:
        try:
            options = Options()
            optI = Option.builder1("i").hasArg0().type(numbers.Number).build()
            optF = Option.builder1("f").hasArg0().build()
            options.addOption0(optI)
            options.addOption0(optF)
            parser = DefaultParser(2, False, None)
            cmd = parser.parse0(options, ["-i", "123", "-f", "foo"])
            self.assertEqual(123, int(cmd.getParsedOptionValue1(optI)))
            self.assertEqual("foo", cmd.getParsedOptionValue1(optF))
        except Exception as e:
            self.fail(f"An exception occurred: {e}")

    def test_GetParsedOptionValueWithChar(self) -> None:
        try:
            options = Options()
            options.addOption0(Option.builder1("i").hasArg0().type(numbers.Number).build())
            options.addOption0(Option.builder1("f").hasArg0().build())
            parser = DefaultParser(2, False, None)
            cmd = parser.parse0(options, ["-i", "123", "-f", "foo"])
            self.assertEqual(123, int(cmd.getParsedOptionValue0("i")))
            self.assertEqual("foo", cmd.getParsedOptionValue0("f"))
        except Exception as e:
            self.fail(f"An exception occurred: {e}")


    # Class Methods End
