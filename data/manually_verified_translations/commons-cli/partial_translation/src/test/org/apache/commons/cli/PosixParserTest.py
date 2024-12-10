from __future__ import annotations
import re
import mock
import unittest
import pytest
import io
import os
import unittest
from src.main.org.apache.commons.cli.CommandLineParser import *
from src.test.org.apache.commons.cli.ParserTestCase import *
from src.main.org.apache.commons.cli.PosixParser import *


class PosixParserTest(ParserTestCase, unittest.TestCase):

    @pytest.mark.skip(reason="Ignore")
    def testUnambiguousPartialLongOption4(self) -> None:

        # Create a list of options
        options = self.getOptions()

        # Create a command line
        cl = self.getCommandLine(CommandLine.PARSER_POSIX_PORTABLE, options)

        # Add an argument to the command line
        cl.addArgument("-abc")

        # Parse the command line
        self.assertEquals(0, len(cl.getArgs()))

        # Assert that the option is present
        self.assertTrue(cl.hasOption("a"))
        self.assertTrue(cl.hasOption("b"))
        self.assertTrue(cl.hasOption("c"))

        # Assert that the option value is correct
        self.assertEquals("", cl.getOptionValue("a"))
        self.assertEquals("", cl.getOptionValue("b"))
        self.assertEquals("", cl.getOptionValue("c"))

    @pytest.mark.skip(reason="Ignore")
    def testShortWithEqual(self) -> None:

        # Create a list of arguments
        args = ["-a", "--long", "arg"]

        # Create a list of options
        options = self.getOptions()

        # Create a command line parser
        parser = PosixParser()

        # Parse the arguments
        cmd = parser.parse(self._options, args)

        # Assert that the command line has the expected number of arguments
        self.assertEquals(3, cmd.getArgs().size())

        # Assert that the command line has the expected options
        self.assertTrue(cmd.hasOption("a"))
        self.assertTrue(cmd.hasOption("long"))
        self.assertFalse(cmd.hasOption("c"))

        # Assert that the command line has the expected arguments
        self.assertEquals("arg", cmd.getOptionValue("long"))

    @pytest.mark.skip(reason="Ignore")
    def testNegativeOption(self) -> None:

        # Create a list of options
        options = self.getOptions()

        # Create a list of arguments
        arguments = ["-xyz"]

        # Create a command line parser
        parser = PosixParser()

        # Parse the arguments
        with self.assertRaises(UnrecognizedOptionException):
            cmd = parser.parse(options, arguments)

    @pytest.mark.skip(reason="Ignore")
    def testLongWithUnexpectedArgument1(self) -> None:

        # Set up the command line arguments
        args = ["-long", "arg1", "arg2"]

        # Create a mock for the command line parser
        parser = PosixParser()

        # Call the method with the mock command line parser
        with self.assertRaises(UnrecognizedOptionException):
            parser.parse(args)

    @pytest.mark.skip(reason="Ignore")
    def testLongWithoutEqualSingleDash(self) -> None:

        # Create a list of arguments
        args = ["--longopt"]

        # Parse the arguments
        cmd = self._parser.parse(self._options, args)

        # Assert that the option was recognized
        self.assertTrue(cmd.hasOption("longopt"))

        # Assert that the option has no argument
        self.assertEqual(0, len(cmd.getOptionValues("longopt")))

    @pytest.mark.skip(reason="Ignore")
    def testLongWithEqualSingleDash(self) -> None:

        # Create a list of arguments
        args = ["--long=value"]

        # Parse the arguments
        cmd = self._parser.parse(self._options, args)

        # Assert that the parsed command line has the expected number of arguments
        self.assertEqual(1, len(cmd.getOptions()))

        # Get the option from the parsed command line
        option = cmd.getOption("long")

        # Assert that the option is not None
        self.assertIsNotNone(option)

        # Assert that the option value is 'value'
        self.assertEqual("value", option.getValue())

    @pytest.mark.skip(reason="Ignore")
    def testDoubleDash2(self) -> None:

        # Create a list of arguments
        args = ["--", "-opt"]

        # Create a new instance of CommandLine
        cl = CommandLine()

        # Call the method to be tested
        self._parser.parse(args, cl)

        # Assert the expected results
        self.assertEquals(["-opt"], cl.getArgs())

    @pytest.mark.skip(reason="Ignore")
    def testAmbiguousPartialLongOption4(self) -> None:

        options = self.getOptions()
        start_index = 0
        ambiguous_option = "file"
        partial_option = "fil"
        candidates = self.getAmbiguousPartialLongOptionCandidates(
            options, partial_option
        )

        try:
            self._parser.parse(
                self.createCommandLine("--" + partial_option), options, start_index
            )
            self.fail("Expected exception")
        except AmbiguousOptionException as e:
            self.assertEquals(ambiguous_option, e.getOption())
            self.assertEquals(candidates, e.getMatchingOptions())

    @pytest.mark.skip(reason="Ignore")
    def testAmbiguousLongWithoutEqualSingleDash(self) -> None:

        # Define the options
        options = self.getOptions()

        # Create the command line
        cl = self.getCommandLine(CommandLine.PARSER_STYLE_UNIX, options, "--ambig")

        # Assert that the command line has the correct number of arguments
        self.assertEquals(0, cl.getArgs().size())

        # Assert that the command line has the correct options
        self.assertTrue(cl.hasOption("a"))
        self.assertTrue(cl.hasOption("b"))
        self.assertFalse(cl.hasOption("c"))
        self.assertFalse(cl.hasOption("d"))

        # Assert that the command line has the correct option values
        self.assertEquals("", cl.getOptionValue("a"))
        self.assertEquals("", cl.getOptionValue("b"))
        self.assertIsNone(cl.getOptionValue("c"))
        self.assertIsNone(cl.getOptionValue("d"))

    def setUp(self) -> None:

        super().setUp()
        self._parser = PosixParser()
