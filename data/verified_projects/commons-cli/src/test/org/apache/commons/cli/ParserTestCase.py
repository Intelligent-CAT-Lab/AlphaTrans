import pytest

from src.main.org.apache.commons.cli.UnrecognizedOptionException import *
from src.main.org.apache.commons.cli.Parser import *
from src.main.org.apache.commons.cli.ParseException import *
from src.main.org.apache.commons.cli.Options import *
from src.main.org.apache.commons.cli.OptionGroup import *
from src.main.org.apache.commons.cli.OptionBuilder import *
from src.main.org.apache.commons.cli.Option import *
from src.main.org.apache.commons.cli.MissingOptionException import *
from src.main.org.apache.commons.cli.MissingArgumentException import *
from src.main.org.apache.commons.cli.DefaultParser import *
from src.main.org.apache.commons.cli.CommandLineParser import *
from src.main.org.apache.commons.cli.CommandLine import *
from src.main.org.apache.commons.cli.AmbiguousOptionException import *
import unittest
import typing
from typing import *
from abc import ABC


class ParserTestCase(unittest.TestCase, ABC):

    __test__ = False
    _parser = None
    _options = None
    
    
    def __parse(
        self,
        parser: CommandLineParser,
        opts: Options,
        args: typing.List[str],
        properties: typing.Union[
            configparser.ConfigParser, typing.Dict
        ],
    ) -> CommandLine:
        
        if isinstance(parser, Parser) or isinstance(parser, DefaultParser):
            return parser.parse2(opts, args, properties)
        raise RuntimeError(
            "Default options not supported by this parser"
        )
    
    
    def setUp(self) -> None:
        # self._parser = parser
        self._options = Options()\
            .addOption3("a", "enable-a", False, "turn [a] on or off")\
            .addOption3("b", "bfile", True, "set the value of [b]")\
            .addOption3("c", "copt", False, "turn [c] on or off")
    

    @pytest.mark.test
    def testAmbiguousLongWithoutEqualSingleDash(self) -> None:
        try:
            args = ["-b", "-foobar"]

            options = Options()
            options.addOption0(
                OptionBuilder.withLongOpt("foo").hasOptionalArg().create1('f')
            )
            options.addOption0(
                OptionBuilder.withLongOpt("bar").hasOptionalArg().create1('b')
            )

            cl = self._parser.parse0(options, args)

            self.assertTrue(cl.hasOption2("b"))
            self.assertTrue(cl.hasOption2("f"))
            self.assertEqual("bar", cl.getOptionValue4("foo"))
        except Exception as e:
            self.fail(f"An exception occurred: {e}")
    
    
    @pytest.mark.test
    def testAmbiguousPartialLongOption1(self) -> None:
        try:
            args = ["--ver"]

            options = Options()
            options.addOption0(OptionBuilder.withLongOpt("version").create0())
            options.addOption0(OptionBuilder.withLongOpt("verbose").create0())

            caught = False
            try:
                self._parser.parse0(options, args)
            except AmbiguousOptionException as e:
                caught = True
                self.assertEqual("--ver", e.getOption(), "Partial option")
                self.assertIsNotNone(e.getMatchingOptions(), "Matching options null")
                self.assertEqual(2, len(e.getMatchingOptions()), "Matching options size")
            
            self.assertTrue("Confirm MissingArgumentException caught", caught)
        except Exception as e:
            self.fail(f"An exception occurred: {e}")
    
    
    @pytest.mark.test
    def testAmbiguousPartialLongOption2(self) -> None:
        try:
            args = ["-ver"]

            options = Options()
            options.addOption0(OptionBuilder.withLongOpt("version").create0())
            options.addOption0(OptionBuilder.withLongOpt("verbose").create0())

            caught = False
            try:
                self._parser.parse0(options, args)
            except AmbiguousOptionException as e:
                caught = True
                self.assertEqual("-ver", e.getOption(), "Partial option")
                self.assertIsNotNone(e.getMatchingOptions(), "Matching options null")
                self.assertEqual(2, len(e.getMatchingOptions()), "Matching options size")
            
            self.assertTrue("Confirm MissingArgumentException caught", caught)
        except Exception as e:
            self.fail(f"An exception occurred: {e}")
    
    
    @pytest.mark.test
    def testAmbiguousPartialLongOption3(self) -> None:
        try:
            args = ["--ver=1"]

            options = Options()
            options.addOption0(OptionBuilder.withLongOpt("version").create0())
            options.addOption0(OptionBuilder.withLongOpt("verbose").hasOptionalArg().create0())

            caught = False
            try:
                self._parser.parse0(options, args)
            except AmbiguousOptionException as e:
                caught = True
                self.assertEqual("--ver", e.getOption(), "Partial option")
                self.assertIsNotNone(e.getMatchingOptions(), "Matching options null")
                self.assertEqual(2, len(e.getMatchingOptions()), "Matching options size")
            
            self.assertTrue("Confirm MissingArgumentException caught", caught)
        except Exception as e:
            self.fail(f"An exception occurred: {e}")

    
    @pytest.mark.test
    def testAmbiguousPartialLongOption4(self) -> None:
        try:
            args = ["-ver=1"]

            options = Options()
            options.addOption0(OptionBuilder.withLongOpt("version").create0())
            options.addOption0(OptionBuilder.withLongOpt("verbose").hasOptionalArg().create0())

            caught = False
            try:
                self._parser.parse0(options, args)
            except AmbiguousOptionException as e:
                caught = True
                self.assertEqual("-ver", e.getOption(), "Partial option")
                self.assertIsNotNone(e.getMatchingOptions(), "Matching options null")
                self.assertEqual(2, len(e.getMatchingOptions()), "Matching options size")
            
            self.assertTrue("Confirm MissingArgumentException caught", caught)
        except Exception as e:
            self.fail(f"An exception occurred: {e}")
    
    
    @pytest.mark.test
    def testArgumentStartingWithHyphen(self) -> None:
        try:
            args = ["-b", "-foo"]

            cl = self._parser.parse0(self._options, args)
            self.assertEqual("-foo", cl.getOptionValue4("b"))
        except Exception as e:
            self.fail(f"An exception occurred: {e}")
    
    
    @pytest.mark.test
    def testBursting(self) -> None:
        try:
            args = ["-acbtoast", "foo", "bar"]

            cl = self._parser.parse0(self._options, args)

            self.assertTrue(cl.hasOption2("a"), "Confirm -a is set")
            self.assertTrue(cl.hasOption2("b"), "Confirm -b is set")
            self.assertTrue(cl.hasOption2("c"), "Confirm -c is set")
            self.assertEqual("toast", cl.getOptionValue4("b"), "Confirm arg of -b")
            self.assertEqual(2, len(cl.getArgList()), "Confirm size of extra args")
        except Exception as e:
            self.fail(f"An exception occurred: {e}")
    
    
    @pytest.mark.test
    def testDoubleDash1(self) -> None:
        try:
            args = ["--copt", "--", "-b", "toast"]

            cl = self._parser.parse0(self._options, args)

            self.assertTrue(cl.hasOption2("c"), "Confirm -c is set")
            self.assertFalse(cl.hasOption2("b"), "Confirm -b is not set")
            self.assertEqual(2, len(cl.getArgList()), "Confirm 2 extra args: " + str(len(cl.getArgList())))
        except Exception as e:
            self.fail(f"An exception occurred: {e}")
    
    
    @pytest.mark.test
    def testDoubleDash2(self) -> None:
        try:    
            options = Options()
            options.addOption0(OptionBuilder.hasArg0().create1("n"))
            options.addOption0(OptionBuilder.create1("m"))

            try:
                self._parser.parse0(options, ["-n", "--", "-m"])
                self.fail("MissingArgumentException not thrown for option -n")
            except MissingArgumentException as e:
                self.assertIsNotNone(e.getOption())
                self.assertEqual("n", e.getOption().getOpt())
        except Exception as e:
            self.fail(f"An exception occurred: {e}")
    
    
    @pytest.mark.test
    def testLongOptionQuoteHandling(self) -> None:
        try:
            args = ["--bfile", "\"quoted string\""]

            cl = self._parser.parse0(self._options, args)

            self.assertEqual(
                "quoted string",
                cl.getOptionValue4("b"),
                "Confirm --bfile \"arg\" strips quotes"
            )
        except Exception as e:
            self.fail(f"An exception occurred: {e}")

    
    @pytest.mark.test
    def testLongOptionWithEqualsQuoteHandling(self) -> None:
        try:
            args = ["--bfile=\"quoted string\""]

            cl = self._parser.parse0(self._options, args)

            self.assertEqual(
                "quoted string",
                cl.getOptionValue4("b"),
                "Confirm --bfile=\"arg\" strips quotes"
            )
        except Exception as e:
            self.fail(f"An exception occurred: {e}")
    
    
    @pytest.mark.test
    def testLongWithEqualDoubleDash(self) -> None:
        try:
            args = ["--foo=bar"]

            options = Options()
            options.addOption0(OptionBuilder.withLongOpt("foo").hasArg0().create1('f'))

            cl = self._parser.parse0(options, args)

            self.assertEqual("bar", cl.getOptionValue4("foo"))
        except Exception as e:
            self.fail(f"An exception occurred: {e}")
    
    
    @pytest.mark.test
    def testLongWithEqualSingleDash(self) -> None:
        try:
            args = ["-foo=bar"]

            options = Options()
            options.addOption0(OptionBuilder.withLongOpt("foo").hasArg0().create1('f'))

            cl = self._parser.parse0(options, args)

            self.assertEqual("bar", cl.getOptionValue4("foo"))
        except Exception as e:
            self.fail(f"An exception occurred: {e}")
    
    
    @pytest.mark.test
    def testLongWithoutEqualDoubleDash(self) -> None:
        try:
            args = ["--foobar"]

            options = Options()
            options.addOption0(OptionBuilder.withLongOpt("foo").hasArg0().create1('f'))

            cl = self._parser.parse1(options, args, True)

            self.assertFalse(cl.hasOption2("foo"))
        except Exception as e:
            self.fail(f"An exception occurred: {e}")
    
    
    @pytest.mark.test
    def testLongWithoutEqualSingleDash(self) -> None:
        try:
            args = ["-foobar"]

            options = Options()
            options.addOption0(OptionBuilder.withLongOpt("foo").hasArg0().create1('f'))

            cl = self._parser.parse0(options, args)

            self.assertEqual("bar", cl.getOptionValue4("foo"))
        except Exception as e:
            self.fail(f"An exception occurred: {e}")
    
    
    @pytest.mark.test
    def testLongWithUnexpectedArgument1(self) -> None:
        try:
            args = ["--foo=bar"]

            options = Options()
            options.addOption0(OptionBuilder.withLongOpt("foo").create1("f"))

            try:
                self._parser.parse0(options, args)
            except UnrecognizedOptionException as e:
                self.assertEqual("--foo=bar", e.getOption())
                return
            
            self.fail("UnrecognizedOptionException not thrown")
        except Exception as e:
            self.fail(f"An exception occurred: {e}")
    
    
    @pytest.mark.test
    def testLongWithUnexpectedArgument2(self) -> None:
        try:
            args = ["-foobar"]

            options = Options()
            options.addOption0(OptionBuilder.withLongOpt("foo").create1("f"))

            try:
                self._parser.parse0(options, args)
            except UnrecognizedOptionException as e:
                self.assertEqual("-foobar", e.getOption())
                return
            
            self.fail("UnrecognizedOptionException not thrown")
        except Exception as e:
            self.fail(f"An exception occurred: {e}")
    
    
    @pytest.mark.test
    def testMissingArg(self) -> None:
        try:
            args = ["-b"]

            caught = False

            try:
                self._parser.parse0(self._options, args)
            except MissingArgumentException as e:
                caught = True
                self.assertEqual("b", e.getOption().getOpt(), "option missing an argument")
            
            self.assertTrue(caught, "Confirm MissingArgumentException caught")
        except Exception as e:
            self.fail(f"An exception occurred: {e}")


    @pytest.mark.test
    def testMissingArgWithBursting(self) -> None:
        try:
            args = ["-acb"]

            caught = False

            try:
                self._parser.parse0(self._options, args)
            except MissingArgumentException as e:
                caught = True
                self.assertEqual("b", e.getOption().getOpt(), "option missing an argument")
            
            self.assertTrue(caught, "Confirm MissingArgumentException caught")
        except Exception as e:
            self.fail(f"An exception occurred: {e}")
    
    
    @pytest.mark.test
    def testMissingRequiredGroup(self) -> None:
        try:
            group = OptionGroup()
            group.addOption(OptionBuilder.create2('a'))
            group.addOption(OptionBuilder.create2('b'))
            group.setRequired(True)

            options = Options()
            options.addOptionGroup(group)
            options.addOption0(OptionBuilder.isRequired0().create2('c'))

            try:
                self._parser.parse0(options, ["-c"])
                self.fail("MissingOptionException not thrown")
            except MissingOptionException as e:
                self.assertEqual(1, len(e.getMissingOptions()))
                self.assertTrue(isinstance(e.getMissingOptions()[0], OptionGroup))
            except ParseException as e:
                self.fail("Expected to catch MissingOptionException")
        except Exception as e:
            self.fail(f"An exception occurred: {e}")
    
    
    @pytest.mark.test
    def testMissingRequiredOption(self) -> None:
        args = ["-a"]

        options = Options()
        options.addOption3("a", "enable-a", False, None)
        options.addOption0(
            OptionBuilder.withLongOpt("bfile").hasArg0().isRequired0().create1('b')
        )

        try:
            self._parser.parse0(options, args)
            self.fail("exception should have been thrown")
        except MissingOptionException as e:
            self.assertEqual(
                "Missing required option: b",
                e.args[0],
                "Incorrect exception message"
            )
            self.assertTrue("b" in e.getMissingOptions())
        except ParseException as e:
            self.fail("expected to catch MissingOptionException")

    
    @pytest.mark.test
    def testMissingRequiredOptions(self) -> None:
        args = ["-a"]

        options = Options()
        options.addOption3("a", "enable-a", False, None)
        options.addOption0(
            OptionBuilder.withLongOpt("bfile").hasArg0().isRequired0().create1('b')
        )
        options.addOption0(
            OptionBuilder.withLongOpt("cfile").hasArg0().isRequired0().create1('c')
        )

        try:
            self._parser.parse0(options, args)
            self.fail("exception should have been thrown")
        except MissingOptionException as e:
            self.assertEqual(
                "Missing required options: b, c",
                e.args[0],
                "Incorrect exception message"
            )
            self.assertTrue("b" in e.getMissingOptions())
            self.assertTrue("c" in e.getMissingOptions())
        except ParseException as e:
            self.fail("expected to catch MissingOptionException")

    
    @pytest.mark.test
    def testMultiple(self) -> None:
        try:
            args = ["-c", "foobar", "-b", "toast"]

            cl = self._parser.parse1(self._options, args, True)
            self.assertTrue(cl.hasOption2("c"), "Confirm -c is set")
            self.assertEqual(
                3,
                len(cl.getArgList()),
                "Confirm  3 extra args: " + str(len(cl.getArgList())),
            )

            cl = self._parser.parse0(self._options, cl.getArgs())

            self.assertFalse(cl.hasOption2("c"), "Confirm -c is not set")
            self.assertTrue(cl.hasOption2("b"), "Confirm -b is set")
            self.assertEqual("toast", cl.getOptionValue4("b"), "Confirm arg of -b")
            self.assertEqual(
                1,
                len(cl.getArgList()),
                "Confirm  1 extra arg: " + str(len(cl.getArgList())), 
            )
            self.assertEqual(
                "foobar",
                cl.getArgList()[0],
                "Confirm  value of extra arg: " + str(cl.getArgList()[0])
            )
        except Exception as e:
            self.fail(f"An exception occurred: {e}")
    
    
    @pytest.mark.test
    def testMultipleWithLong(self) -> None:
        try:
            args = ["--copt", "foobar", "--bfile", "toast"]

            cl = self._parser.parse1(self._options, args, True)
            self.assertTrue(cl.hasOption2("c"), "Confirm -c is set")
            self.assertEqual(
                3,
                len(cl.getArgList()),
                "Confirm  3 extra args: " + str(len(cl.getArgList())),
            )

            cl = self._parser.parse0(self._options, cl.getArgs())

            self.assertFalse(cl.hasOption2("c"), "Confirm -c is not set")
            self.assertTrue(cl.hasOption2("b"), "Confirm -b is set")
            self.assertEqual("toast", cl.getOptionValue4("b"), "Confirm arg of -b")
            self.assertEqual(
                1,
                len(cl.getArgList()),
                "Confirm  1 extra arg: " + str(len(cl.getArgList())), 
            )
            self.assertEqual(
                "foobar",
                cl.getArgList()[0],
                "Confirm  value of extra arg: " + str(cl.getArgList()[0])
            )
        except Exception as e:
            self.fail(f"An exception occurred: {e}")
    
    
    @pytest.mark.test
    def testNegativeArgument(self) -> None:
        try:
            args = ["-b", "-1"]

            cl = self._parser.parse0(self._options, args)
            self.assertEqual("-1", cl.getOptionValue4("b"))
        except Exception as e:
            self.fail(f"An exception occurred: {e}")
    
    
    @pytest.mark.test
    def testNegativeOption(self) -> None:
        try:
            args = ["-b", "-1"]

            self._options.addOption1("1", False, None)

            cl = self._parser.parse0(self._options, args)
            self.assertEqual("-1", cl.getOptionValue4("b"))
        except Exception as e:
            self.fail(f"An exception occurred: {e}")

    
    @pytest.mark.test
    def testOptionAndRequiredOption(self) -> None:
        try:
            args = ["-a", "-b", "file"]

            options = Options()
            options.addOption3("a", "enable-a", False, None)
            options.addOption0(
                OptionBuilder.withLongOpt("bfile").hasArg0().isRequired0().create1("b")
            )

            cl = self._parser.parse0(options, args)

            self.assertTrue(cl.hasOption2("a"), "Confirm -a is set")
            self.assertTrue(cl.hasOption2("b"), "Confirm -b is set")
            self.assertEqual("file", cl.getOptionValue4("b"), "Confirm arg of -b")
            self.assertEqual(0, len(cl.getArgList()), "Confirm NO of extra args")
        except Exception as e:
            self.fail(f"An exception occurred: {e}")


    @pytest.mark.test
    def testOptionGroup(self) -> None:
        try:
            group = OptionGroup()
            group.addOption(OptionBuilder.create2("a"))
            group.addOption(OptionBuilder.create2("b"))

            options = Options()
            options.addOptionGroup(group)

            self._parser.parse0(options, ["-b"])

            self.assertEqual("b", group.getSelected(), "selected option", ) 
        except Exception as e:
            self.fail(f"An exception occurred: {e}")
    
    
    @pytest.mark.test
    def testOptionGroupLong(self) -> None:
        try:
            group = OptionGroup()
            group.addOption(OptionBuilder.withLongOpt("foo").create0())
            group.addOption(OptionBuilder.withLongOpt("bar").create0())

            options = Options()
            options.addOptionGroup(group)

            cl = self._parser.parse0(options, ["--bar"])

            self.assertTrue(cl.hasOption2("bar"))
            self.assertEqual("bar", group.getSelected(), "selected option")
        except Exception as e:
            self.fail(f"An exception occurred: {e}")
    
    
    @pytest.mark.test
    def testPartialLongOptionSingleDash(self) -> None:
        try:
            args = ["-ver"]

            options = Options()
            options.addOption0(OptionBuilder.withLongOpt("version").create0())
            options.addOption0(OptionBuilder.hasArg0().create1("v"))

            cl = self._parser.parse0(options, args)

            self.assertTrue(cl.hasOption2("version"), "Confirm --version is set")
            self.assertFalse(cl.hasOption2("v"), "Confirm -v is not set")
        except Exception as e:
            self.fail(f"An exception occurred: {e}")

    
    @pytest.mark.test
    def testPropertiesOption1(self) -> None:
        try:
            args = ["-Jsource=1.5", "-J", "target", "1.5", "foo"]

            options = Options()
            options.addOption0(OptionBuilder.withValueSeparator0().hasArgs1(2).create1("J"))

            cl = self._parser.parse0(options, args)

            values = cl.getOptionValues2("J")
            self.assertIsNotNone("null values", values)
            self.assertEqual(4, len(values), "number of values")
            self.assertEqual("source", values[0], "value 1")
            self.assertEqual("1.5", values[1], "value 2")
            self.assertEqual("target", values[2], "value 3")
            self.assertEqual("1.5", values[3], "value 4")

            argsleft = cl.getArgList()
            self.assertEqual(1, len(argsleft), "Should be 1 arg left")
            self.assertEqual("foo", argsleft[0], "Expecting foo")
        except Exception as e:
            self.fail(f"An exception occurred: {e}")
    
    
    @pytest.mark.test
    def testPropertiesOption2(self) -> None:
        try:
            args = ["-Dparam1", "-Dparam2=value2", "-D"]

            options = Options()
            options.addOption0(
                OptionBuilder.withValueSeparator0().hasOptionalArgs1(2).create1('D')
            )

            cl = self._parser.parse0(options, args)

            props = cl.getOptionProperties1("D")
            self.assertIsNotNone(props, "null properties")
            self.assertEqual(2, len(props), "number of properties in " + str(props))
            self.assertEqual("true", props.get("param1"), "property 1")
            self.assertEqual("value2", props.get("param2"), "property 2")

            argsleft = cl.getArgList()
            self.assertEqual(0, len(argsleft), "Should be no arg left")
        except Exception as e:
            self.fail(f"An exception occurred: {e}")
    
    
    @pytest.mark.test
    def testPropertyOptionFlags(self) -> None:
        try:
            opts = Options()
            opts.addOption1("a", False, "toggle -a")
            opts.addOption3("c", "c", False, "toggle -c")
            opts.addOption0(OptionBuilder.hasOptionalArg().create1("e"))

            properties = {"a": "true", "c": "yes", "e": "1"}

            cmd = self.__parse(self._parser, opts, None, properties)
            self.assertTrue(cmd.hasOption2("a"))
            self.assertTrue(cmd.hasOption2("c"))
            self.assertTrue(cmd.hasOption2("e"))

            properties = {"a": "false", "c": "no", "e": "0"}

            cmd = self.__parse(self._parser, opts, None, properties)
            self.assertFalse(cmd.hasOption2("a"))
            self.assertFalse(cmd.hasOption2("c"))
            self.assertTrue(cmd.hasOption2("e"))  # this option accepts an argument

            properties = {"a": "TRUE", "c": "nO", "e": "TrUe"}

            cmd = self.__parse(self._parser, opts, None, properties)
            self.assertTrue(cmd.hasOption2("a"))
            self.assertFalse(cmd.hasOption2("c"))
            self.assertTrue(cmd.hasOption2("e"))

            properties = {"a": "just a string", "e": ""}

            cmd = self.__parse(self._parser, opts, None, properties)
            self.assertFalse(cmd.hasOption2("a"))
            self.assertFalse(cmd.hasOption2("c"))
            self.assertTrue(cmd.hasOption2("e"))

            properties = {"a": "0", "c": "1"}

            cmd = self.__parse(self._parser, opts, None, properties)
            self.assertFalse(cmd.hasOption2("a"))
            self.assertTrue(cmd.hasOption2("c"))
        except Exception as e:
            self.fail(f"An exception occurred: {e}")
    
    
    @pytest.mark.test
    def testPropertyOptionGroup(self) -> None:
        try:
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

            properties = {"b": "true", "x": "true"}

            cmd = self.__parse(self._parser, opts, args, properties)
            
            self.assertTrue(cmd.hasOption2("a"))
            self.assertFalse(cmd.hasOption2("b"))
            self.assertTrue(cmd.hasOption2("x"))
            self.assertFalse(cmd.hasOption2("y"))
        except Exception as e:
            self.fail(f"An exception occurred: {e}")

    
    @pytest.mark.test
    def testPropertyOptionMultipleValues(self) -> None:
        try:
            opts = Options()
            opts.addOption0(OptionBuilder.hasArgs0().withValueSeparator1(",").create1('k'))

            properties = {"k": "one,two"}
            
            values = ["one", "two"]

            cmd = self.__parse(self._parser, opts, None, properties)

            self.assertTrue(cmd.hasOption2("k"))
            self.assertEqual(values, cmd.getOptionValues0('k'))
        except Exception as e:
            self.fail(f"An exception occurred: {e}")
    
    
    @pytest.mark.test
    def testPropertyOptionRequired(self) -> None:
        try:
            opts = Options()
            opts.addOption0(OptionBuilder.isRequired0().create2("f"))

            properties = {"f": "true"}

            cmd = self.__parse(self._parser, opts, None, properties)
            self.assertTrue(cmd.hasOption2("f"))
        except Exception as e:
            self.fail(f"An exception occurred: {e}")
    
    
    @pytest.mark.test
    def testPropertyOptionSingularValue(self) -> None:
        try:
            opts = Options()
            opts.addOption0(OptionBuilder.hasOptionalArgs1(2).withLongOpt("hide").create0())

            properties = {"hide": "seek"}

            cmd = self.__parse(self._parser, opts, None, properties)
            self.assertTrue(cmd.hasOption2("hide"))
            self.assertEqual("seek", cmd.getOptionValue4("hide"))
            self.assertFalse(cmd.hasOption2("fake"))
        except Exception as e:
            self.fail(f"An exception occurred: {e}")
    
    
    @pytest.mark.test
    def testPropertyOptionUnexpected(self) -> None:
        try:
            opts = Options()

            properties = {"f": "true"}

            try:
                self.__parse(self._parser, opts, None, properties)
                self.fail("UnrecognizedOptionException expected")
            except UnrecognizedOptionException:
                pass
        except Exception as e:
            self.fail(f"An exception occurred: {e}")

    
    @pytest.mark.test
    def testPropertyOverrideValues(self) -> None:
        try:
            opts = Options()
            opts.addOption0(OptionBuilder.hasOptionalArgs1(2).create1('i'))
            opts.addOption0(OptionBuilder.hasOptionalArgs0().create1('j'))

            args = ["-j", "found", "-i", "ink"]

            properties = {"j": "seek"}

            cmd = self.__parse(self._parser, opts, args, properties)
            self.assertTrue(cmd.hasOption2("j"))
            self.assertEqual("found", cmd.getOptionValue4("j"))
            self.assertTrue(cmd.hasOption2("i"))
            self.assertEqual("ink", cmd.getOptionValue4("i"))
            self.assertFalse(cmd.hasOption2("fake"))
        except Exception as e:
            self.fail(f"An exception occurred: {e}")
    
    
    @pytest.mark.test
    def testReuseOptionsTwice(self) -> None:
        try:
            opts = Options()
            opts.addOption0(OptionBuilder.isRequired0().create1('v'))

            self._parser.parse0(opts, ["-v"])

            try:
                self._parser.parse0(opts, [])
                self.fail("MissingOptionException not thrown")
            except MissingOptionException:
                pass
        except Exception as e:
            self.fail(f"An exception occurred: {e}")
    
    
    @pytest.mark.test
    def testShortOptionConcatenatedQuoteHandling(self) -> None:
        try:
            args = ["-b\"quoted string\""]

            cl = self._parser.parse0(self._options, args)

            self.assertEqual(
                "quoted string",
                cl.getOptionValue4("b"),
                "Confirm -b\"arg\" strips quotes"
            )
        except Exception as e:
            self.fail(f"An exception occurred: {e}")
    
    
    @pytest.mark.test
    def testShortOptionQuoteHandling(self) -> None:
        try:
            args = ["-b", "\"quoted string\""]

            cl = self._parser.parse0(self._options, args)

            self.assertEqual(
                "quoted string",
                cl.getOptionValue4("b"),
                "Confirm -b \"arg\" strips quotes"
            )
        except Exception as e:
            self.fail(f"An exception occurred: {e}")

    
    @pytest.mark.test
    def testShortWithEqual(self) -> None:
        try:
            args = ["-f=bar"]

            options = Options()
            options.addOption0(OptionBuilder.withLongOpt("foo").hasArg0().create1('f'))

            cl = self._parser.parse0(options, args)

            self.assertEqual("bar", cl.getOptionValue4("foo"))
        except Exception as e:
            self.fail(f"An exception occurred: {e}")
    
    
    @pytest.mark.test
    def testShortWithoutEqual(self) -> None:
        try:
            args = ["-fbar"]

            options = Options()
            options.addOption0(OptionBuilder.withLongOpt("foo").hasArg0().create1('f'))

            cl = self._parser.parse0(options, args)

            self.assertEqual("bar", cl.getOptionValue4("foo"))
        except Exception as e:
            self.fail(f"An exception occurred: {e}")
    
    
    @pytest.mark.test
    def testShortWithUnexpectedArgument(self) -> None:
        try:
            args = ["-f=bar"]

            options = Options()
            options.addOption0(OptionBuilder.withLongOpt("foo").create1('f'))

            try:
                self._parser.parse0(options, args)
            except UnrecognizedOptionException as e:
                self.assertEqual("-f=bar", e.getOption())
                return
            
            self.fail("UnrecognizedOptionException not thrown")
        except Exception as e:
            self.fail(f"An exception occurred: {e}")

    
    @pytest.mark.test
    def testSimpleLong(self) -> None:
        try:
            args = ["--enable-a", "--bfile", "toast", "foo", "bar"]

            cl = self._parser.parse0(self._options, args)

            self.assertTrue(cl.hasOption2("a"), "Confirm -a is set")
            self.assertTrue(cl.hasOption2("b"), "Confirm -b is set")
            self.assertEqual("toast", cl.getOptionValue4("b"), "Confirm arg of -b")
            self.assertEqual("toast", cl.getOptionValue4("bfile"), "Confirm arg of --bfile")
            self.assertEqual(2, len(cl.getArgList()), "Confirm size of extra args")
        except Exception as e:
            self.fail(f"An exception occurred: {e}")

    
    @pytest.mark.test
    def testSimpleShort(self) -> None:
        try:
            args = ["-a", "-b", "toast", "foo", "bar"]

            cl = self._parser.parse0(self._options, args)

            self.assertTrue(cl.hasOption2("a"), "Confirm -a is set")
            self.assertTrue(cl.hasOption2("b"), "Confirm -b is set")
            self.assertEqual("toast", cl.getOptionValue4("b"), "Confirm arg of -b")
            self.assertEqual(2, len(cl.getArgList()), "Confirm size of extra args")
        except Exception as e:
            self.fail(f"An exception occurred: {e}")
    
    
    @pytest.mark.test
    def testSingleDash(self) -> None:
        try:
            args = ["--copt", "-b", "-", "-a", "-"]

            cl = self._parser.parse0(self._options, args)

            self.assertTrue(cl.hasOption2("a"), "Confirm -a is set")
            self.assertTrue(cl.hasOption2("b"), "Confirm -b is set")
            self.assertEqual("-", cl.getOptionValue4("b"), "Confirm arg of -b")
            self.assertEqual(
                1,
                len(cl.getArgList()),
                "Confirm 1 extra arg: " + str(len(cl.getArgList()))
            )
            self.assertEqual(
                "-",
                cl.getArgList()[0],
                "Confirm value of extra arg: " + str(cl.getArgList()[0])
            )
        except Exception as e:
            self.fail(f"An exception occurred: {e}")
    
    
    @pytest.mark.test
    def testStopAtExpectedArg(self) -> None:
        try:
            args = ["-b", "foo"]

            cl = self._parser.parse1(self._options, args, True)

            self.assertTrue(cl.hasOption0("b"), "Confirm -b is set")
            self.assertEqual("foo", cl.getOptionValue0("b"), "Confirm -b is set")
            self.assertEqual(
                0,
                len(cl.getArgList()),
                "Confirm no extra args: " + str(len(cl.getArgList()))
            )
        except Exception as e:
            self.fail(f"An exception occurred: {e}")
    
    
    @pytest.mark.test
    def testStopAtNonOptionLong(self) -> None:
        try:
            args = ["--zop==1", "-abtoast", "--b=bar"]

            cl = self._parser.parse1(self._options, args, True)

            self.assertFalse(cl.hasOption2("a"), "Confirm -a is not set")
            self.assertFalse(cl.hasOption2("b"), "Confirm -b is not set")
            self.assertEqual(
                3,
                len(cl.getArgList()),
                "Confirm  3 extra args: " + str(len(cl.getArgList()))
            )
        except Exception as e:
            self.fail(f"An exception occurred: {e}")
    
    
    @pytest.mark.test
    def testStopAtNonOptionShort(self) -> None:
        try:
            args = ["-z", "-a", "-btoast"]

            cl = self._parser.parse1(self._options, args, True)
            self.assertFalse(cl.hasOption2("a"), "Confirm -a is not set")
            self.assertEqual(
                3,
                len(cl.getArgList()),
                "Confirm  3 extra args: " + str(len(cl.getArgList()))
            )
        except Exception as e:
            self.fail(f"An exception occurred: {e}")
    
    
    @pytest.mark.test
    def testStopAtUnexpectedArg(self) -> None:
        try:
            args = ["-c", "foober", "-b", "toast"]

            cl = self._parser.parse1(self._options, args, True)
            self.assertTrue(cl.hasOption2("c"), "Confirm -c is set")
            self.assertEqual(
                3,
                len(cl.getArgList()),
                "Confirm  3 extra args: " + str(len(cl.getArgList()))
            )
        except Exception as e:
            self.fail(f"An exception occurred: {e}")

    
    @pytest.mark.test
    def testStopBursting(self) -> None:
        try:
            args = ["-azc"]

            cl = self._parser.parse1(self._options, args, True)

            self.assertTrue(cl.hasOption2("a"), "Confirm -a is set")
            self.assertFalse(cl.hasOption2("c"), "Confirm -c is not set")

            self.assertEqual(
                1,
                len(cl.getArgList()),
                "Confirm  1 extra args: " + str(len(cl.getArgList()))
            )
            self.assertTrue("zc" in cl.getArgList())
        except Exception as e:
            self.fail(f"An exception occurred: {e}")
    
    
    @pytest.mark.test
    def testStopBursting2(self) -> None:
        try:
            args = ["-c", "foobar", "-btoast"]

            cl = self._parser.parse1(self._options, args, True)
            self.assertTrue(cl.hasOption2("c"), "Confirm -c is set")
            self.assertEqual(
                2,
                len(cl.getArgList()),
                "Confirm  2 extra args: " + str(len(cl.getArgList()))
            )

            cl = self._parser.parse0(self._options, cl.getArgs())

            self.assertFalse(cl.hasOption2("c"), "Confirm -c is not set")
            self.assertTrue(cl.hasOption2("b"), "Confirm -b is set")
            self.assertEqual("toast", cl.getOptionValue4("b"), "Confirm arg of -b")
            self.assertEqual(
                1,
                len(cl.getArgList()),
                "Confirm  1 extra arg: " + str(len(cl.getArgList()))
            )
            self.assertEqual(
                "foobar",
                cl.getArgList()[0],
                "Confirm  value of extra arg: " + str(cl.getArgList()[0])
            )
        except Exception as e:
            self.fail(f"An exception occurred: {e}")
    
    
    @pytest.mark.test
    def testUnambiguousPartialLongOption1(self) -> None:
        try:
            args = ["--ver"]

            options = Options()
            options.addOption0(OptionBuilder.withLongOpt("version").create0())
            options.addOption0(OptionBuilder.withLongOpt("help").create0())

            cl = self._parser.parse0(options, args)

            self.assertTrue(cl.hasOption2("version"), "Confirm --version is set")
        except Exception as e:
            self.fail(f"An exception occurred: {e}")
    
    
    @pytest.mark.test
    def testUnambiguousPartialLongOption2(self) -> None:
        try:
            args = ["-ver"]

            options = Options()
            options.addOption0(OptionBuilder.withLongOpt("version").create0())
            options.addOption0(OptionBuilder.withLongOpt("help").create0())

            cl = self._parser.parse0(options, args)

            self.assertTrue(cl.hasOption2("version"), "Confirm --version is set")
        except Exception as e:
            self.fail(f"An exception occurred: {e}")
    

    @pytest.mark.test
    def testUnambiguousPartialLongOption3(self) -> None:
        try:
            args = ["--ver=1"]

            options = Options()
            options.addOption0(
                OptionBuilder.withLongOpt("verbose").hasOptionalArg().create0()
            )
            options.addOption0(OptionBuilder.withLongOpt("help").create0())

            cl = self._parser.parse0(options, args)

            self.assertTrue(cl.hasOption2("verbose"), "Confirm --verbose is set")
            self.assertEqual("1", cl.getOptionValue4("verbose"))
        except Exception as e:
            self.fail(f"An exception occurred: {e}")

    
    @pytest.mark.test
    def testUnambiguousPartialLongOption4(self) -> None:
        try:
            args = ["-ver=1"]

            options = Options()
            options.addOption0(
                OptionBuilder.withLongOpt("verbose").hasOptionalArg().create0()
            )
            options.addOption0(OptionBuilder.withLongOpt("help").create0())

            cl = self._parser.parse0(options, args)

            self.assertTrue(cl.hasOption2("verbose"), "Confirm --verbose is set", )
            self.assertEqual("1", cl.getOptionValue4("verbose"))
        except Exception as e:
            self.fail(f"An exception occurred: {e}")

    
    @pytest.mark.test
    def testUnlimitedArgs(self) -> None:
        try:
            args = ["-e", "one", "two", "-f", "alpha"]

            options = Options()
            options.addOption0(OptionBuilder.hasArgs0().create2("e"))
            options.addOption0(OptionBuilder.hasArgs0().create2("f"))

            cl = self._parser.parse0(options, args)

            self.assertTrue(cl.hasOption2("e"), "Confirm -e is set")
            self.assertEqual(2, len(cl.getOptionValues2("e")), "number of arg for -e")
            self.assertTrue(cl.hasOption2("f"), "Confirm -f is set")
            self.assertEqual(1, len(cl.getOptionValues2("f")), "number of arg for -f")
        except Exception as e:
            self.fail(f"An exception occurred: {e}")
    
    
    @pytest.mark.test
    def testUnrecognizedOption(self) -> None:
        try:
            args = ["-a", "-d", "-b", "toast", "foo", "bar"]

            try:
                self._parser.parse0(self._options, args)
                self.fail("UnrecognizedOptionException wasn't thrown")
            except UnrecognizedOptionException as e:
                self.assertEqual("-d", e.getOption())
        except Exception as e:
            self.fail(f"An exception occurred: {e}")
    
    
    @pytest.mark.test
    def testUnrecognizedOptionWithBursting(self) -> None:
        try:
            args = ["-adbtoast", "foo", "bar"]

            try:
                self._parser.parse0(self._options, args)
                self.fail("UnrecognizedOptionException wasn't thrown")
            except UnrecognizedOptionException as e:
                self.assertEqual("-adbtoast", e.getOption())
        except Exception as e:
            self.fail(f"An exception occurred: {e}")
    
    
    @pytest.mark.test
    def testWithRequiredOption(self) -> None:
        try:
            args = ["-b", "file"]

            options = Options()
            options.addOption3("a", "enable-a", False, None)
            options.addOption0(
                OptionBuilder.withLongOpt("bfile").hasArg0().isRequired0().create1('b')
            )

            cl = self._parser.parse0(options, args)

            self.assertFalse(cl.hasOption2("a"), "Confirm -a is NOT set")
            self.assertTrue(cl.hasOption2("b"), "Confirm -b is set")
            self.assertEqual("file", cl.getOptionValue4("b"), "Confirm arg of -b")
            self.assertEqual(0, len(cl.getArgList()), "Confirm NO of extra args")
        except Exception as e:
            self.fail(f"An exception occurred: {e}")
