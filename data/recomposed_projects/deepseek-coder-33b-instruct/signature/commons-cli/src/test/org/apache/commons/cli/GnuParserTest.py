from __future__ import annotations
import re
import unittest
import pytest
import io
import unittest
from src.main.org.apache.commons.cli.CommandLineParser import *
from src.main.org.apache.commons.cli.GnuParser import *
from src.test.org.apache.commons.cli.ParserTestCase import *


class GnuParserTest(ParserTestCase, unittest.TestCase):

    @pytest.mark.skip(reason="Ignore")
    def testUnrecognizedOptionWithBursting(self) -> None:

        # Create a list of options
        options = self._options.get_options()

        # Create a list of arguments
        arguments = ["-x"]

        # Try to parse the arguments
        try:
            cmd = self._parser.parse(self._options, arguments)
        except UnrecognizedOptionException as e:
            # If an UnrecognizedOptionException is thrown, check that the option is not recognized
            self.assertFalse(self._options.has_option(e.get_option()))
        except Exception as e:
            # If any other exception is thrown, fail the test
            self.fail("Unexpected exception: " + str(e))

    @pytest.mark.skip(reason="Ignore")
    def testUnambiguousPartialLongOption4(self) -> None:

        # Setup
        options = self._options
        parser = self._parser

        # Test
        try:
            cmdLine = parser.parse(options, ["--ambiguous-partial-long-option-4"])
            self.assertTrue(cmdLine.hasOption("ambiguous-partial-long-option-4"))
        except Exception as e:
            self.fail(str(e))

    @pytest.mark.skip(reason="Ignore")
    def testUnambiguousPartialLongOption3(self) -> None:

        # Setup
        options = self._options
        parser = self._parser

        # Test
        try:
            cmdLine = parser.parse(options, ["--ambiguous-partial-long-option-3"])
            self.assertTrue(cmdLine.hasOption("ambiguous-partial-long-option-3"))
        except Exception as e:
            self.fail(str(e))

    @pytest.mark.skip(reason="Ignore")
    def testUnambiguousPartialLongOption2(self) -> None:

        # Setup
        options = self._options
        parser = self._parser

        # Test
        args = ["-longopt"]
        cmd = parser.parse(options, args)
        self.assertTrue(cmd.hasOption("longopt"))
        self.assertFalse(cmd.hasOption("long"))

        args = ["-longopt", "--long"]
        cmd = parser.parse(options, args)
        self.assertTrue(cmd.hasOption("longopt"))
        self.assertTrue(cmd.hasOption("long"))

        args = ["--longopt", "--long"]
        cmd = parser.parse(options, args)
        self.assertTrue(cmd.hasOption("longopt"))
        self.assertTrue(cmd.hasOption("long"))

        args = ["--longopt", "-long"]
        cmd = parser.parse(options, args)
        self.assertTrue(cmd.hasOption("longopt"))
        self.assertTrue(cmd.hasOption("long"))

    @pytest.mark.skip(reason="Ignore")
    def testUnambiguousPartialLongOption1(self) -> None:

        # Create a new GnuParser instance
        parser = GnuParser()

        # Create a new Options instance
        options = Options()

        # Add an option to the Options instance
        options.addOption("p", "longOption", False, "This is a long option")

        # Parse the arguments using the GnuParser instance
        cmd = parser.parse(options, ["-longOption"])

        # Assert that the option was found in the command line
        self.assertTrue(cmd.hasOption("longOption"))

    @pytest.mark.skip(reason="Ignore")
    def testStopBursting2(self) -> None:

        # Create a new GnuParser instance
        parser = GnuParser()

        # Create a new Options instance
        options = Options()

        # Add an option to the options
        options.addOption("a", False, "Option a")

        # Parse the arguments
        cmd = parser.parse(options, ["--stop-bursting"])

        # Check if the option is present in the command line
        assert cmd.hasOption("stop-bursting")

        # Check if the option is not present in the command line
        assert not cmd.hasOption("a")

    @pytest.mark.skip(reason="Ignore")
    def testStopBursting(self) -> None:

        # Create a new GnuParser instance
        parser = GnuParser()

        # Create a new Options instance
        options = Options()

        # Add an option to the options
        options.addOption("a", False, "Option a")

        # Parse the arguments
        cmd = parser.parse(options, ["-a"])

        # Assert that the option is present
        self.assertTrue(cmd.hasOption("a"))

        # Stop the bursting
        parser.stopBursting()

        # Parse the arguments again
        cmd = parser.parse(options, ["-a"])

        # Assert that the option is not present
        self.assertFalse(cmd.hasOption("a"))

    @pytest.mark.skip(reason="Ignore")
    def testShortWithUnexpectedArgument(self) -> None:

        # Create a GnuParser instance
        parser = GnuParser()

        # Create a Options instance
        options = Options()

        # Add an option to the Options instance
        options.addOption("p", False, "Option p")

        # Parse the arguments
        try:
            cmd = parser.parse(options, ["-p", "--unexpected"])
        except ParseException as e:
            # Check if the exception message is as expected
            self.assertEqual("Unexpected argument: --unexpected", str(e))
        else:
            self.fail("Expected ParseException")

    @pytest.mark.skip(reason="Ignore")
    def testPartialLongOptionSingleDash(self) -> None:

        # Create a new GnuParser instance
        parser = GnuParser()

        # Create a new Options instance
        options = Options()

        # Add an option to the Options instance
        options.addOption("p", "partial", False, "Partial option")

        # Parse the arguments using the GnuParser instance
        cmd = parser.parse(options, ["-partial".split()])

        # Assert that the option was parsed correctly
        self.assertTrue(cmd.hasOption("partial"))

    @pytest.mark.skip(reason="Ignore")
    def testNegativeOption(self) -> None:

        # Create a new GnuParser instance
        parser = GnuParser()

        # Define some options
        options = Options()
        options.addOption("p", "option", True, "test option")
        options.addOption("attr", "attrName", True, "attributeName")

        # Define some arguments
        arguments = ["-p", "value", "-attr", "attrValue"]

        try:
            # Parse the arguments
            cmd = parser.parse(options, arguments)

            # Check if the parsed command line has the expected options
            self.assertTrue(cmd.hasOption("p"))
            self.assertTrue(cmd.hasOption("attr"))

            # Check if the parsed command line has the expected option values
            self.assertEqual(cmd.getOptionValue("p"), "value")
            self.assertEqual(cmd.getOptionValue("attr"), "attrValue")

        except Exception as e:
            # If an exception is thrown, fail the test
            self.fail(str(e))

    @pytest.mark.skip(reason="Ignore")
    def testMissingArgWithBursting(self) -> None:

        # Create a new GnuParser instance
        parser = GnuParser()

        # Create a new Options instance
        options = Options()

        # Add an option to the options
        options.addOption("p", False, "Option p")

        # Parse the arguments with the parser
        try:
            cmd = parser.parse(options, ["-pb"])
        except Exception as e:
            # Handle the exception
            print(f"Exception occurred: {e}")

    @pytest.mark.skip(reason="Ignore")
    def testLongWithUnexpectedArgument2(self) -> None:

        # Create a GnuParser instance
        parser = GnuParser()

        # Create a Options instance
        options = Options()

        # Add an option to the Options instance
        options.addOption("p", "property", True, "use value for given property")

        # Parse the arguments
        command_line = parser.parse(options, ["-p", "value"])

        # Assert that the option value is as expected
        self.assertEqual("value", command_line.getOptionValue("property"))

    @pytest.mark.skip(reason="Ignore")
    def testLongWithUnexpectedArgument1(self) -> None:

        # Create a GnuParser instance
        parser = GnuParser()

        # Create a Options instance
        options = Options()

        # Add an option to the Options instance
        options.addOption("p", "property", True, "use value for given property")

        # Parse the arguments
        try:
            cmd = parser.parse(options, ["-foobar".split(" ")])
        except Exception as e:
            # Check if the exception is of type UnrecognizedOptionException
            if isinstance(e, UnrecognizedOptionException):
                # If it is, then the test passes
                pass
            else:
                # If it's not, then the test fails
                raise e

    @pytest.mark.skip(reason="Ignore")
    def testLongWithoutEqualSingleDash(self) -> None:

        # Create a list of options
        options = self._options.get_options()

        # Create a list of arguments
        arguments = ["-longopt"]

        # Parse the arguments
        cmd = self._parser.parse(self._options, arguments)

        # Assert that the option is present
        self.assertTrue(cmd.has_option("longopt"))

        # Assert that the option value is None
        self.assertIsNone(cmd.get_option_value("longopt"))

    @pytest.mark.skip(reason="Ignore")
    def testDoubleDash2(self) -> None:

        # Create a list of arguments
        args = ["--", "-opt", "value"]

        # Create a new GnuParser instance
        parser = GnuParser()

        # Parse the arguments
        try:
            cmd = parser.parse(self._options, args)
        except Exception as e:
            self.fail("Unexpected exception: " + str(e))

        # Assert that the parsed command line has the expected number of arguments
        self.assertEqual(2, cmd.getArgs().size())

        # Assert that the parsed command line has the expected argument value
        self.assertEqual("value", cmd.getArgs()[0])

    @pytest.mark.skip(reason="Ignore")
    def testBursting(self) -> None:

        # Your code here
        pass

    @pytest.mark.skip(reason="Ignore")
    def testAmbiguousPartialLongOption4(self) -> None:

        # Create a new GnuParser instance
        parser = GnuParser()

        # Create a new Options instance
        options = Options()

        # Add options to the Options instance
        options.addOption("p", "longopt", True, "description")
        options.addOption("r", "longopt2", True, "description2")

        # Create a list of arguments
        args = ["-plongvalue", "--longopt2", "longvalue2"]

        # Parse the arguments using the GnuParser instance
        cmd = parser.parse(options, args)

        # Assert that the parsed command line has the expected number of arguments
        self.assertEqual(cmd.getArgs().length, 0)

        # Assert that the parsed command line has the expected option value
        self.assertEqual(cmd.getOptionValue("longopt"), "longvalue")
        self.assertEqual(cmd.getOptionValue("longopt2"), "longvalue2")

    @pytest.mark.skip(reason="Ignore")
    def testAmbiguousPartialLongOption3(self) -> None:

        # Create a new GnuParser instance
        parser = GnuParser()

        # Create a new Options instance
        options = Options()

        # Add an option to the Options instance
        options.addOption("p", "longOption", True, "description")

        # Parse the command line arguments
        commandLine = parser.parse(options, ["-plongOption", "value"])

        # Assert that the option value is as expected
        self.assertEqual("value", commandLine.getOptionValue("longOption"))

    @pytest.mark.skip(reason="Ignore")
    def testAmbiguousPartialLongOption2(self) -> None:

        # Create a new GnuParser instance
        parser = GnuParser()

        # Create a new Options instance
        options = Options()

        # Add an option to the Options instance
        options.addOption("p", "longOption", True, "description")

        # Parse the command line arguments
        commandLine = parser.parse(options, ["-plongOption", "value"])

        # Assert that the option value is as expected
        self.assertEqual("value", commandLine.getOptionValue("longOption"))

    @pytest.mark.skip(reason="Ignore")
    def testAmbiguousPartialLongOption1(self) -> None:

        # Create a new GnuParser instance
        parser = GnuParser()

        # Create a new Options instance
        options = Options()

        # Add an option to the Options instance
        options.addOption("p", "longOption", True, "description")

        # Parse the command line arguments
        commandLine = parser.parse(options, ["-plongOption", "value"])

        # Assert that the option was parsed correctly
        self.assertTrue(commandLine.hasOption("longOption"))
        self.assertEqual(commandLine.getOptionValue("longOption"), "value")

    @pytest.mark.skip(reason="Ignore")
    def testAmbiguousLongWithoutEqualSingleDash(self) -> None:

        # Create a list of options
        options = self._options.get_options()

        # Create a list of arguments
        arguments = ["-abc"]

        # Parse the arguments
        cl = self._parser.parse(self._options, arguments)

        # Assert that the argument was parsed correctly
        self.assertTrue(cl.has_option("a"))
        self.assertTrue(cl.has_option("b"))
        self.assertTrue(cl.has_option("c"))
        self.assertFalse(cl.has_option("d"))

    def setUp(self) -> None:
        super().setUp()
        self._parser = GnuParser()
