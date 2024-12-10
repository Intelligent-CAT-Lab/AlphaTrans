from __future__ import annotations
import re
import unittest
import pytest
import io
import unittest
from src.main.org.apache.commons.cli.CommandLine import *
from src.main.org.apache.commons.cli.DefaultParser import *
from src.main.org.apache.commons.cli.Option import *
from src.main.org.apache.commons.cli.Options import *


class BugCLI265Test(unittest.TestCase):

    __options: Options = None

    __parser: DefaultParser = None

    def testshouldParseShortOptionWithValue(self) -> None:

        shortOptionWithValue = ["-t1", "path/to/my/db"]

        commandLine = self.__parser.parse0(self.__options, shortOptionWithValue)

        self.assertEqual("path/to/my/db", commandLine.getOptionValue4("t1"))
        self.assertFalse(commandLine.hasOption2("last"))

    def testshouldParseShortOptionWithoutValue(self) -> None:

        two_short_options = ["-t1", "-last"]

        command_line = self.__parser.parse0(self.__options, two_short_options)

        self.assertTrue(command_line.hasOption2("t1"))
        self.assertNotEqual(
            "Second option has been used as value for first option",
            "-last",
            command_line.getOptionValue4("t1"),
        )
        self.assertTrue(
            "Second option has not been detected", command_line.hasOption2("last")
        )

    def testshouldParseConcatenatedShortOptions(self) -> None:

        concatenatedShortOptions = ["-t1", "-ab"]

        commandLine = self.__parser.parse0(self.__options, concatenatedShortOptions)

        self.assertTrue(commandLine.hasOption2("t1"))
        self.assertIsNone(commandLine.getOptionValue4("t1"))
        self.assertTrue(commandLine.hasOption2("a"))
        self.assertTrue(commandLine.hasOption2("b"))
        self.assertFalse(commandLine.hasOption2("last"))

    def setUp(self) -> None:

        self.__parser = DefaultParser(1, False, None)

        optionT1 = (
            Option.Builder.builder1("t1")
            .hasArg0()
            .numberOfArgs(1)
            .optionalArg(True)
            .argName("t1_path")
            .build()
        )
        optionA = Option.Builder.builder1("a").hasArg1(False).build()
        optionB = Option.Builder.builder1("b").hasArg1(False).build()
        optionLast = Option.Builder.builder1("last").hasArg1(False).build()

        self.__options = (
            Options()
            .addOption0(optionT1)
            .addOption0(optionA)
            .addOption0(optionB)
            .addOption0(optionLast)
        )
