from __future__ import annotations
import re
import mock
import sys
from io import StringIO
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

        # Set up the command line arguments
        args = ["-abc"]

        # Create a mock for System.err
        mock_err = io.StringIO()

        # Set System.err to the mock
        sys.stderr = mock_err

        # Call the method under test
        with pytest.raises(UnrecognizedOptionException):
            self._parser.parse(self._options, args)

        # Reset System.err
        sys.stderr = sys.__stderr__

        # Check the output
        assert mock_err.getvalue() == "Unrecognized option: -abc\n"

    @pytest.mark.skip(reason="Ignore")
    def testUnambiguousPartialLongOption4(self) -> None:

        options = self.getOptions()
        parser = self._parser

        argv = ["--opt"]
        try:
            cmd = parser.parse(options, argv)
            self.fail("Expected exception not thrown")
        except ParseException as ex:
            self.assertEquals("Unrecognized option: --opt", ex.getMessage())

        argv = ["--optio"]
        try:
            cmd = parser.parse(options, argv)
            self.fail("Expected exception not thrown")
        except ParseException as ex:
            self.assertEquals("Unrecognized option: --optio", ex.getMessage())

        argv = ["--option"]
        try:
            cmd = parser.parse(options, argv)
            self.fail("Expected exception not thrown")
        except ParseException as ex:
            self.assertEquals("Unrecognized option: --option", ex.getMessage())

        argv = ["--option-"]
        try:
            cmd = parser.parse(options, argv)
            self.fail("Expected exception not thrown")
        except ParseException as ex:
            self.assertEquals("Unrecognized option: --option-", ex.getMessage())

        argv = ["--option-n"]
        try:
            cmd = parser.parse(options, argv)
            self.fail("Expected exception not thrown")
        except ParseException as ex:
            self.assertEquals("Unrecognized option: --option-n", ex.getMessage())

        argv = ["--option-na"]
        try:
            cmd = parser.parse(options, argv)
            self.fail("Expected exception not thrown")
        except ParseException as ex:
            self.assertEquals("Unrecognized option: --option-na", ex.getMessage())

        argv = ["--option-nam"]
        try:
            cmd = parser.parse(options, argv)
            self.fail("Expected exception not thrown")
        except ParseException as ex:
            self.assertEquals("Unrecognized option: --option-nam", ex.getMessage())

        argv = ["--option-name"]
        try:
            cmd = parser.parse(options, argv)
            self.fail("Expected exception not thrown")
        except ParseException as ex:
            self.assertEquals("Unrecognized option: --option-name", ex.getMessage())

    @pytest.mark.skip(reason="Ignore")
    def testUnambiguousPartialLongOption3(self) -> None:

        # Create a list of options
        options = self.getOptions()

        # Create a command line
        cl = self.getCommandLine(GnuParser(), options, "--ambig")

        # Assert that the command line has the expected number of arguments
        self.assertEquals(1, len(cl.getArgs()))
        self.assertEquals("ambig", cl.getArgs()[0])

        # Assert that the command line has the expected number of options
        self.assertEquals(0, cl.getOptions().size())

    @pytest.mark.skip(reason="Ignore")
    def testUnambiguousPartialLongOption2(self) -> None:

        options = self.getOptions()
        parser = self._parser

        argv = ["--opt"]
        try:
            cmd = parser.parse(options, argv)
            self.fail("Expected exception not thrown")
        except ParseException as ex:
            self.assertEquals("Unrecognized option: --opt", ex.getMessage())

        argv = ["--optio"]
        try:
            cmd = parser.parse(options, argv)
            self.fail("Expected exception not thrown")
        except ParseException as ex:
            self.assertEquals("Unrecognized option: --optio", ex.getMessage())

        argv = ["--option"]
        try:
            cmd = parser.parse(options, argv)
            self.fail("Expected exception not thrown")
        except ParseException as ex:
            self.assertEquals("Unrecognized option: --option", ex.getMessage())

        argv = ["--option2"]
        try:
            cmd = parser.parse(options, argv)
            self.fail("Expected exception not thrown")
        except ParseException as ex:
            self.assertEquals("Unrecognized option: --option2", ex.getMessage())

        argv = ["--option23"]
        try:
            cmd = parser.parse(options, argv)
            self.fail("Expected exception not thrown")
        except ParseException as ex:
            self.assertEquals("Unrecognized option: --option23", ex.getMessage())

    @pytest.mark.skip(reason="Ignore")
    def testUnambiguousPartialLongOption1(self) -> None:

        options = self.getOptions()
        parser = self._parser

        argv = ["--opt"]
        try:
            cmd = parser.parse(options, argv)
            self.fail("Expected exception not thrown")
        except ParseException as ex:
            self.assertEquals("Unrecognized option: --opt", ex.getMessage())

        argv = ["--optio"]
        try:
            cmd = parser.parse(options, argv)
            self.fail("Expected exception not thrown")
        except ParseException as ex:
            self.assertEquals("Unrecognized option: --optio", ex.getMessage())

        argv = ["--option"]
        try:
            cmd = parser.parse(options, argv)
            self.fail("Expected exception not thrown")
        except ParseException as ex:
            self.assertEquals("Unrecognized option: --option", ex.getMessage())

        argv = ["--option="]
        try:
            cmd = parser.parse(options, argv)
            self.fail("Expected exception not thrown")
        except ParseException as ex:
            self.assertEquals("Missing argument for option: option", ex.getMessage())

        argv = ["--option", "value"]
        try:
            cmd = parser.parse(options, argv)
            self.fail("Expected exception not thrown")
        except ParseException as ex:
            self.assertEquals("option doesn't have an argument", ex.getMessage())

    @pytest.mark.skip(reason="Ignore")
    def testStopBursting2(self) -> None:

        # Create a list of options
        options = self.getOptions()

        # Create a command line
        cl = self.getCommandLine(GnuParser(), options, "--longopt1", "--longopt2")

        # Assert that the command line is not null
        self.assertNotNull("confirm that cl is not null", cl)

        # Assert that the command line has 2 arguments
        self.assertEquals("confirm the number of arguments", 2, cl.getArgs().length)

        # Assert that the command line has 2 options
        self.assertEquals("confirm the number of options", 2, cl.getOptions().length)

        # Assert that the command line has the expected argument
        self.assertTrue(
            "confirm the presence of the expected argument", cl.hasOption("longopt1")
        )
        self.assertTrue(
            "confirm the presence of the expected argument", cl.hasOption("longopt2")
        )

        # Assert that the command line has the expected option
        self.assertTrue(
            "confirm the presence of the expected option",
            cl.getOptionValue("longopt1").equals("true"),
        )
        self.assertTrue(
            "confirm the presence of the expected option",
            cl.getOptionValue("longopt2").equals("true"),
        )

    @pytest.mark.skip(reason="Ignore")
    def testStopBursting(self) -> None:

        # Create a mock command line
        command_line = "--stop-bursting"

        # Parse the command line
        cmd = self._parser.parse(self._options, command_line.split(" "))

        # Check if the stop-bursting option is set
        self.assertTrue(cmd.hasOption("stop-bursting"))

        # Check if the stop-bursting option has the correct argument
        self.assertEqual(cmd.getOptionValue("stop-bursting"), "true")

    @pytest.mark.skip(reason="Ignore")
    def testShortWithUnexpectedArgument(self) -> None:

        # Create a command line with a short option that is not expected
        command_line = self._parser.parse(self._options, ["-x"])

        # Check that the command line has an unexpected argument
        self.assertTrue(command_line.hasOption("x"))

    @pytest.mark.skip(reason="Ignore")
    def testPartialLongOptionSingleDash(self) -> None:

        # Create a list of options
        options = self.getOptions()

        # Create a command line
        cl = self.getCommandLine(GnuParser(), options, ["--longopt"])

        # Assert that the command line has the expected number of arguments
        self.assertEquals(1, len(cl.getArgs()))

        # Assert that the command line has the expected option
        self.assertTrue(cl.hasOption("longopt"))

        # Assert that the command line has the expected value for the option
        self.assertEquals("", cl.getOptionValue("longopt"))

    @pytest.mark.skip(reason="Ignore")
    def testNegativeOption(self) -> None:

        # Create a list of options
        options = self.getOptions()

        # Create a command line without any arguments
        cl = self.getCommandLine(options, "")

        # Assert that the command line does not have an option
        self.assertFalse(cl.hasOption("p"))

    @pytest.mark.skip(reason="Ignore")
    def testMissingArgWithBursting(self) -> None:

        # Create a list of options
        options = self.getOptions()

        # Create a command line without an argument
        cl = self.getCommandLine(GnuParser(), options, ["-a"])

        # Assert that the argument is missing
        self.assertTrue(cl.getOptionValue("a") is None)

        # Assert that the argument is missing
        self.assertTrue(cl.getOptionValue("b") is None)

        # Assert that the argument is missing
        self.assertTrue(cl.getOptionValue("c") is None)

    @pytest.mark.skip(reason="Ignore")
    def testLongWithUnexpectedArgument2(self) -> None:

        # Create a command line parser
        parser = GnuParser()

        # Create a list of options
        options = self.getOptions()

        # Create a command line
        cl = self.getCommandLine(parser, options, "--longopt1")

        # Assert that the command line is not None
        assert cl is not None

        # Assert that the command line has one argument
        self.assertEquals(1, len(cl.getArgs()))

        # Assert that the command line argument is "--unexpected"
        self.assertEquals("--unexpected", cl.getArgs()[0])

    @pytest.mark.skip(reason="Ignore")
    def testLongWithUnexpectedArgument1(self) -> None:

        # Create a command line parser
        parser = GnuParser()

        # Define the command line options
        options = self.getOptions()

        # Parse the command line arguments
        command_line = parser.parse(self.getArguments(), options)

        # Check if the command line has the expected arguments
        self.assertTrue(command_line.hasOption("longopt"))
        self.assertTrue(command_line.hasOption("unexpected"))

        # Check if the command line has the unexpected argument
        self.assertFalse(command_line.hasOption("unexpected"))

    @pytest.mark.skip(reason="Ignore")
    def testLongWithoutEqualSingleDash(self) -> None:

        # Create a command line
        cmd_line = "--longopt"

        # Parse the command line
        cmd = self._parser._parser.parse(
            self._parser._tokenize(cmd_line), self._options
        )

        # Assert that the command line has the expected option
        self.assertTrue(cmd.hasOption("longopt"))

        # Assert that the command line does not have an argument for the option
        self.assertFalse(cmd.getOptionValue("longopt"))

    @pytest.mark.skip(reason="Ignore")
    def testDoubleDash2(self) -> None:

        # Create a list of arguments
        args = ["--", "-q"]

        # Create a new CommandLine instance
        cl = self._parser.parse(self._options, args)

        # Assert that the argument list is not empty
        self.assertFalse(cl.getArgs().hasMoreElements())

        # Assert that the option list is not empty
        self.assertFalse(cl.getOptions().hasMoreElements())

    @pytest.mark.skip(reason="Ignore")
    def testBursting(self) -> None:

        # Create a list of options
        options = ["-a", "-b", "-c"]

        # Create a list of arguments
        arguments = ["arg1", "arg2", "arg3"]

        # Create a list of expected results
        expected_results = ["result1", "result2", "result3"]

        # Iterate over the options, arguments, and expected results
        for option, argument, expected_result in zip(
            options, arguments, expected_results
        ):

            # Create a command line string
            command_line = f"{option} {argument}"

            # Parse the command line string
            command_line = self._parser.parse(self._options, command_line.split())

            # Get the result
            result = command_line.getOptionValue(option)

            # Check if the result is equal to the expected result
            self.assertEqual(result, expected_result)

    @pytest.mark.skip(reason="Ignore")
    def testAmbiguousPartialLongOption4(self) -> None:

        options = self.getOptions()
        parser = self._parser

        try:
            cmdLine = parser.parse(self._options, self._arguments)
            self.assertTrue(
                "Option with long name 'opt' is ambiguous; could be 'optC', 'optA', 'optB'",
                False,
            )
        except Exception as e:
            self.assertTrue(
                "Option with long name 'opt' is ambiguous; could be 'optC', 'optA', 'optB'",
                True,
            )

    @pytest.mark.skip(reason="Ignore")
    def testAmbiguousPartialLongOption3(self) -> None:

        # Create a command line
        cl = CommandLine()

        # Create options
        option1 = Option("p", "longopt")
        option2 = Option("r", "longopt")

        # Add options to the command line
        cl.addOption(option1)
        cl.addOption(option2)

        # Create a parser
        parser = GnuParser()

        # Parse the command line
        try:
            parser.parse(cl.getArgs(), cl)
        except AmbiguousOptionException as e:
            self.fail("Unexpected exception: " + e.getMessage())
        except UnrecognizedOptionException as e:
            self.fail("Unexpected exception: " + e.getMessage())
        except ParseException as e:
            self.fail("Unexpected exception: " + e.getMessage())

    @pytest.mark.skip(reason="Ignore")
    def testAmbiguousPartialLongOption2(self) -> None:

        # Create a command line
        cl = CommandLine()

        # Create options
        option1 = Option("p", "longopt")
        option2 = Option("r", "longopt")

        # Add options to the command line
        cl.addOption(option1)
        cl.addOption(option2)

        # Create a parser
        parser = GnuParser()

        # Parse the command line
        try:
            parser.parse(cl.getArgs(), cl)
        except AmbiguousOptionException as e:
            self.fail("Unexpected exception: " + e.getMessage())
        except UnrecognizedOptionException as e:
            self.fail("Unexpected exception: " + e.getMessage())
        except ParseException as e:
            self.fail("Unexpected exception: " + e.getMessage())

    @pytest.mark.skip(reason="Ignore")
    def testAmbiguousPartialLongOption1(self) -> None:

        options = self.getOptions()
        parser = self._parser

        try:
            cmdLine = parser.parse(self._options, self._arguments, False)
            self.assertTrue("Encoding is not supported", False)
        except Exception:
            pass

        try:
            cmdLine = parser.parse(self._options, self._arguments, True)
            self.assertTrue("Encoding is not supported", False)
        except ValueError:
            pass

        self.assertEquals(cmdLine.getOptionValue("e"), "utf-8")
        self.assertEquals(cmdLine.getOptionValue("encoding"), "utf-8")

    @pytest.mark.skip(reason="Ignore")
    def testAmbiguousLongWithoutEqualSingleDash(self) -> None:

        options = self.getOptions()
        commandLine = self.parse("--ambiguous -ab")

        self.assertTrue(commandLine.hasOption("ambiguous"))
        self.assertTrue(commandLine.hasOption("a"))
        self.assertTrue(commandLine.hasOption("b"))
        self.assertEquals(0, commandLine.getOptionValue("ambiguous"))
        self.assertEquals(0, commandLine.getOptionValue("a"))
        self.assertEquals(0, commandLine.getOptionValue("b"))

    def setUp(self) -> None:

        super().setUp()
        self._parser = GnuParser()
