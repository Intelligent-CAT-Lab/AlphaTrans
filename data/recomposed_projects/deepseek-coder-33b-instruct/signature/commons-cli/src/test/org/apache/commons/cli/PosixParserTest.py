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

        # Setup
        options = self._options
        parser = self._parser

        # Test
        args = ["-abc"]
        try:
            cmd = parser.parse(options, args)
            self.fail("Expected exception")
        except ParseException as ex:
            self.assertEquals("Unrecognized option: -b", ex.getMessage())

        args = ["-a", "-bc"]
        try:
            cmd = parser.parse(options, args)
            self.fail("Expected exception")
        except ParseException as ex:
            self.assertEquals("Unrecognized option: -b", ex.getMessage())

        args = ["-ab", "-c"]
        try:
            cmd = parser.parse(options, args)
            self.fail("Expected exception")
        except ParseException as ex:
            self.assertEquals("Unrecognized option: -c", ex.getMessage())

        args = ["-a", "-b", "-c"]
        cmd = parser.parse(options, args)
        self.assertFalse("Confirm -abc is set", cmd.hasOption("abc"))
        self.assertTrue("Confirm -a is set", cmd.hasOption("a"))
        self.assertTrue("Confirm -b is set", cmd.hasOption("b"))
        self.assertTrue("Confirm -c is set", cmd.hasOption("c"))

    @pytest.mark.skip(reason="Ignore")
    def testShortWithEqual(self) -> None:

        # Create a list of options
        options = self._options.get_options()

        # Create a list of arguments
        arguments = ["-a", "--bbb", "-c", "--ddd", "-e", "--fff"]

        # Parse the arguments
        cmd = self._parser.parse(self._options, arguments)

        # Assert that the parsed arguments are equal to the expected arguments
        self.assertEqual(cmd.get_option_values("a"), ["a"])
        self.assertEqual(cmd.get_option_values("bbb"), ["bbb"])
        self.assertEqual(cmd.get_option_values("c"), ["c"])
        self.assertEqual(cmd.get_option_values("ddd"), ["ddd"])
        self.assertEqual(cmd.get_option_values("e"), ["e"])
        self.assertEqual(cmd.get_option_values("fff"), ["fff"])

    @pytest.mark.skip(reason="Ignore")
    def testNegativeOption(self) -> None:

        # Create a mock object for the CommandLineParser
        mock_parser = unittest.mock.Mock(spec=CommandLineParser)

        # Set the return value for the parse method
        mock_parser.parse.return_value = None

        # Set the parser to the mock object
        self._parser = mock_parser

        # Call the method with some parameters
        self._parser.parse(["-x"], self._options)

        # Check that the parse method was called with the correct parameters
        mock_parser.parse.assert_called_once_with(["-x"], self._options)

    @pytest.mark.skip(reason="Ignore")
    def testLongWithUnexpectedArgument1(self) -> None:

        # Create a mock object for the CommandLineParser
        mock_parser = unittest.mock.Mock(spec=CommandLineParser)

        # Set the return value for the parse method
        mock_parser.parse.return_value = None

        # Create an instance of PosixParser and set the parser
        posix_parser = PosixParser()
        posix_parser._parser = mock_parser

        # Call the method with some arguments
        posix_parser.testLongWithUnexpectedArgument1()

        # Assert that the parse method was called with the expected arguments
        mock_parser.parse.assert_called_once_with(None, None)

    @pytest.mark.skip(reason="Ignore")
    def testLongWithoutEqualSingleDash(self) -> None:

        # Create a list of options
        options = self._options.get_options()

        # Create a list of arguments
        arguments = ["-p", "--property", "--longopt"]

        # Parse the arguments
        cmd = self._parser.parse(self._options, arguments)

        # Assert that the parsed command line has the expected number of arguments
        self.assertEqual(3, cmd.get_arg_list().size())

        # Assert that the parsed command line has the expected options
        self.assertTrue(cmd.has_option("p"))
        self.assertTrue(cmd.has_option("property"))
        self.assertTrue(cmd.has_option("longopt"))

    @pytest.mark.skip(reason="Ignore")
    def testLongWithEqualSingleDash(self) -> None:

        # Create a new Options object
        options = self._options = Options()

        # Create a new PosixParser object
        parser = self._parser = PosixParser()

        # Add an option to the Options object
        options.addOption("p", False, "longopt")

        # Parse the arguments
        cmdLine = parser.parse(options, ["--longopt"], False)

        # Assert that the option was found
        self.assertTrue(cmdLine.hasOption("longopt"))

        # Assert that the option value is None
        self.assertIsNone(cmdLine.getOptionValue("longopt"))

    @pytest.mark.skip(reason="Ignore")
    def testDoubleDash2(self) -> None:

        # Create a list of arguments
        args = ["--", "-opt", "value"]

        # Create a new instance of PosixParser
        parser = PosixParser()

        # Call the method to be tested
        try:
            parser.parse(self._options, args, False)
        except Exception as e:
            # If an exception is thrown, fail the test
            self.fail("Exception thrown: " + str(e))

    @pytest.mark.skip(reason="Ignore")
    def testAmbiguousPartialLongOption4(self) -> None:

        # Set up the options
        options = self._options
        options.addOption("p", "Option p")
        options.addOption("attr", "Option attr")

        # Create a parser
        parser = PosixParser()

        # Parse the arguments
        cl = parser.parse(options, ["-pattr"])

        # Assert the result
        self.assertTrue(cl.hasOption("p"))
        self.assertTrue(cl.hasOption("attr"))
        self.assertEquals(0, len(cl.getArgs()))

    @pytest.mark.skip(reason="Ignore")
    def testAmbiguousLongWithoutEqualSingleDash(self) -> None:

        # Create a list of options
        options = self._options.get_options()

        # Create a list of arguments
        arguments = ["-abc"]

        # Parse the arguments
        cl = self._parser.parse(self._options, arguments, False)

        # Get the matched option
        matched_option = cl.get_option_values()

        # Check if the matched option is not None
        assert matched_option is not None

        # Check if the matched option is equal to the expected option
        assert matched_option == "-a"

        # Check if the matched option is ambiguous
        assert cl.has_ambiguous_option()

    def setUp(self) -> None:
        super().setUp()
        self._parser = PosixParser()
