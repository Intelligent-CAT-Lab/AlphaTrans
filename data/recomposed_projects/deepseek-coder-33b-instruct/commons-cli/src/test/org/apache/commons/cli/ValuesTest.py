from __future__ import annotations
import unittest
import pytest
import io
from src.main.org.apache.commons.cli.CommandLine import *
from src.main.org.apache.commons.cli.CommandLineParser import *
from src.main.org.apache.commons.cli.Option import *
from src.main.org.apache.commons.cli.OptionBuilder import *
from src.main.org.apache.commons.cli.Options import *
from src.main.org.apache.commons.cli.PosixParser import *


class ValuesTest(unittest.TestCase):

    __cmd: CommandLine = None

    def testTwoArgValues(self) -> None:

        assert self.__cmd.hasOption2("g"), "Option g is not set"
        assert self.__cmd.getOptionValues2("g") == [
            "val1",
            "val2",
        ], "Option g values are not equal to ['val1', 'val2']"

    def testShortArgsWithValue(self) -> None:

        assert self.__cmd.hasOption2("b"), "Option b is not set"
        assert self.__cmd.getOptionValue4("b") == "foo", "Option b value is not foo"
        assert (
            len(self.__cmd.getOptionValues2("b")) == 1
        ), "Option b values length is not 1"

        assert self.__cmd.hasOption2("d"), "Option d is not set"
        assert self.__cmd.getOptionValue4("d") == "bar", "Option d value is not bar"
        assert (
            len(self.__cmd.getOptionValues2("d")) == 1
        ), "Option d values length is not 1"

    def testShortArgs(self) -> None:

        assert self.__cmd.hasOption2("a"), "Option a is not set"
        assert self.__cmd.hasOption2("c"), "Option c is not set"

        assert self.__cmd.getOptionValues2("a") is None, "Option a has values"
        assert self.__cmd.getOptionValues2("c") is None, "Option c has values"

    def testMultipleArgValues(self) -> None:

        assert self.__cmd.hasOption2("e"), "Option e is not set"
        assert self.__cmd.getOptionValues2("e") == [
            "one",
            "two",
        ], "Option e values are not as expected"

    def testExtraArgs(self) -> None:

        assert self.__cmd.getArgs() == ["arg1", "arg2", "arg3"], "Extra args"

    def testComplexValues(self) -> None:

        assert self.__cmd.hasOption2("i"), "Option i is not set"
        assert self.__cmd.hasOption2("h"), "Option h is not set"
        assert self.__cmd.getOptionValues2("h") == [
            "val1",
            "val2",
        ], "Option h does not have the expected values"

    def testCharSeparator(self) -> None:

        assert self.__cmd.hasOption2("j") == True, "Option j is not set"
        assert self.__cmd.hasOption0("j") == True, "Option j is not set"
        assert self.__cmd.getOptionValues2("j") == [
            "key",
            "value",
            "key",
            "value",
        ], "Option j values are not correct"
        assert self.__cmd.getOptionValues0("j") == [
            "key",
            "value",
            "key",
            "value",
        ], "Option j values are not correct"

        assert self.__cmd.hasOption2("k") == True, "Option k is not set"
        assert self.__cmd.hasOption0("k") == True, "Option k is not set"
        assert self.__cmd.getOptionValues2("k") == [
            "key1",
            "value1",
            "key2",
            "value2",
        ], "Option k values are not correct"
        assert self.__cmd.getOptionValues0("k") == [
            "key1",
            "value1",
            "key2",
            "value2",
        ], "Option k values are not correct"

        assert self.__cmd.hasOption2("m") == True, "Option m is not set"
        assert self.__cmd.hasOption0("m") == True, "Option m is not set"
        assert self.__cmd.getOptionValues2("m") == [
            "key",
            "value",
        ], "Option m values are not correct"
        assert self.__cmd.getOptionValues0("m") == [
            "key",
            "value",
        ], "Option m values are not correct"

    def setUp(self) -> None:

        options = Options()

        options.addOption1("a", False, "toggle -a")
        options.addOption1("b", True, "set -b")
        options.addOption3("c", "c", False, "toggle -c")
        options.addOption3("d", "d", True, "set -d")

        options.addOption0(
            OptionBuilder.withLongOpt("e")
            .hasArgs0()
            .withDescription("set -e ")
            .create1("e")
        )
        options.addOption3("f", "f", False, "jk")
        options.addOption0(
            OptionBuilder.withLongOpt("g")
            .hasArgs1(2)
            .withDescription("set -g")
            .create1("g")
        )
        options.addOption0(
            OptionBuilder.withLongOpt("h")
            .hasArg0()
            .withDescription("set -h")
            .create1("h")
        )
        options.addOption0(
            OptionBuilder.withLongOpt("i").withDescription("set -i").create1("i")
        )
        options.addOption0(
            OptionBuilder.withLongOpt("j")
            .hasArgs0()
            .withDescription("set -j")
            .withValueSeparator1("=")
            .create1("j")
        )
        options.addOption0(
            OptionBuilder.withLongOpt("k")
            .hasArgs0()
            .withDescription("set -k")
            .withValueSeparator1("=")
            .create1("k")
        )
        options.addOption0(
            OptionBuilder.withLongOpt("m")
            .hasArgs0()
            .withDescription("set -m")
            .withValueSeparator0()
            .create1("m")
        )

        args = [
            "-a",
            "-b",
            "foo",
            "--c",
            "--d",
            "bar",
            "-e",
            "one",
            "two",
            "-f",
            "arg1",
            "arg2",
            "-g",
            "val1",
            "val2",
            "arg3",
            "-h",
            "val1",
            "-i",
            "-h",
            "val2",
            "-jkey=value",
            "-j",
            "key=value",
            "-kkey1=value1",
            "-kkey2=value2",
            "-mkey=value",
        ]

        parser = PosixParser()

        self.__cmd = parser.parse0(options, args)
