from __future__ import annotations
import unittest
import pytest
import io
from src.main.org.apache.commons.cli.CommandLine import *
from src.main.org.apache.commons.cli.DefaultParser import *
from src.main.org.apache.commons.cli.Option import *
from src.main.org.apache.commons.cli.Options import *


class BugCLI265Test(unittest.TestCase):

    __options: Options = None
    __parser: DefaultParser = None

    def shouldParseShortOptionWithValue(self) -> None:

        shortOptionWithValue = ["-t1", "path/to/my/db"]

        commandLine = self.__parser.parse0(self.__options, shortOptionWithValue)

        assert commandLine.getOptionValue4("t1") == "path/to/my/db"
        assert not commandLine.hasOption2("last")

    def shouldParseShortOptionWithoutValue(self) -> None:

        two_short_options = ["-t1", "-last"]

        command_line = self.__parser.parse0(self.__options, two_short_options)

        assert command_line.hasOption2("t1")
        assert (
            command_line.getOptionValue4("t1") != "-last"
        ), "Second option has been used as value for first option"
        assert command_line.hasOption2("last"), "Second option has not been detected"

    def shouldParseConcatenatedShortOptions(self) -> None:

        concatenatedShortOptions = ["-t1", "-ab"]

        commandLine = self.__parser.parse0(self.__options, concatenatedShortOptions)

        assert commandLine.hasOption2("t1")
        assert commandLine.getOptionValue4("t1") is None
        assert commandLine.hasOption2("a")
        assert commandLine.hasOption2("b")
        assert not commandLine.hasOption2("last")

    def setUp(self) -> None:

        parser = DefaultParser(2, False, None)

        optionT1 = (
            Option.builder1("t1")
            .hasArg0()
            .numberOfArgs(1)
            .optionalArg(True)
            .argName("t1_path")
            .build()
        )
        optionA = Option.builder1("a").hasArg1(False).build()
        optionB = Option.builder1("b").hasArg1(False).build()
        optionLast = Option.builder1("last").hasArg1(False).build()

        options = (
            Options()
            .addOption0(optionT1)
            .addOption0(optionA)
            .addOption0(optionB)
            .addOption0(optionLast)
        )

        self.__parser = parser
        self.__options = options
