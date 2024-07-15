from __future__ import annotations
import re
import os
import unittest
import pytest
import io
import unittest
from src.main.org.apache.commons.cli.CommandLine import *
from src.main.org.apache.commons.cli.CommandLineParser import *
from src.main.org.apache.commons.cli.MissingArgumentException import *
from src.main.org.apache.commons.cli.Option import *
from src.main.org.apache.commons.cli.Options import *
from src.main.org.apache.commons.cli.PosixParser import *


class BugCLI71Test(unittest.TestCase):

    __parser: CommandLineParser = None

    __options: Options = None

    def testMistakenArgument(self) -> None:

        # Create a list of arguments
        args = ["-a", "Caesar", "-k", "A"]

        # Parse the arguments
        line = self.__parser.parse0(self.__options, args)

        # Change the arguments
        args = ["-a", "Caesar", "-k", "a"]

        # Parse the new arguments
        line = self.__parser.parse0(self.__options, args)

        # Assert that the option values are as expected
        self.assertEqual("Caesar", line.getOptionValue4("a"))
        self.assertEqual("a", line.getOptionValue4("k"))

    def testLackOfError(self) -> None:

        args = ["-k", "-a", "Caesar"]
        try:
            self.__parser.parse0(self.__options, args)
            self.fail("MissingArgumentException expected")
        except MissingArgumentException as e:
            self.assertEqual("option missing an argument", "k", e.getOption().getOpt())

    def testGetsDefaultIfOptional(self) -> None:

        # Define the arguments
        args = ["-k", "-a", "Caesar"]

        # Set the option 'k' as optional
        self.__options.getOption("k").setOptionalArg(True)

        # Parse the arguments
        line = self.__parser.parse0(self.__options, args)

        # Assert that the value of option 'a' is 'Caesar'
        self.assertEqual("Caesar", line.getOptionValue4("a"))

        # Assert that the value of option 'k' is 'a'
        self.assertEqual("a", line.getOptionValue1("k", "a"))

    def testBasic(self) -> None:

        # Define the arguments
        args = ["-a", "Caesar", "-k", "A"]

        # Parse the arguments
        line = self.__parser.parse0(self.__options, args)

        # Assert the option values
        self.assertEqual("Caesar", line.getOptionValue4("a"))
        self.assertEqual("A", line.getOptionValue4("k"))

    def setUp(self) -> None:

        self.options = Options()

        algorithm = Option(
            0, "a", "algo", "the algorithm which it to perform executing", True, None
        )
        algorithm.setArgName("algorithm name")
        self.options.addOption0(algorithm)

        key = Option(
            0, "k", "key", "the key the setted algorithm uses to process", True, None
        )
        key.setArgName("value")
        self.options.addOption0(key)

        self.parser = PosixParser()
