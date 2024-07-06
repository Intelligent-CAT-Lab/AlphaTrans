from __future__ import annotations
import re
import typing
from typing import *
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
        shortOptionWithValue: typing.List[str] = ["-t1", "path/to/my/db"]
        commandLine: CommandLine = self.__parser.parse0(
            self.__options, shortOptionWithValue
        )
        self.assertEqual("path/to/my/db", commandLine.getOptionValue4("t1"))
        self.assertFalse(commandLine.hasOption2("last"))

    def testshouldParseShortOptionWithoutValue(self) -> None:
        twoShortOptions = ["-t1", "-last"]
        commandLine = self.__parser.parse0(self.__options, twoShortOptions)
        self.assertTrue(commandLine.hasOption2("t1"))
        self.assertNotEqual("-last", commandLine.getOptionValue4("t1"))
        self.assertTrue(
            "Second option has not been detected", commandLine.hasOption2("last")
        )

    def testshouldParseConcatenatedShortOptions(self) -> None:
        concatenatedShortOptions: typing.List[str] = ["-t1", "-ab"]
        commandLine: CommandLine = self.__parser.parse0(
            self.__options, concatenatedShortOptions
        )
        self.assertTrue(commandLine.hasOption2("t1"))
        self.assertIsNone(commandLine.getOptionValue4("t1"))
        self.assertTrue(commandLine.hasOption2("a"))
        self.assertTrue(commandLine.hasOption2("b"))
        self.assertFalse(commandLine.hasOption2("last"))

    def setUp(self) -> None:
        self.__parser = DefaultParser(2, False, None)

        optionT1: Option = (
            Option.builder1("t1")
            .hasArg0()
            .numberOfArgs(1)
            .optionalArg(True)
            .argName("t1_path")
            .build()
        )
        optionA: Option = Option.builder1("a").hasArg1(False).build()
        optionB: Option = Option.builder1("b").hasArg1(False).build()
        optionLast: Option = Option.builder1("last").hasArg1(False).build()

        self.__options = (
            Options()
            .addOption0(optionT1)
            .addOption0(optionA)
            .addOption0(optionB)
            .addOption0(optionLast)
        )
