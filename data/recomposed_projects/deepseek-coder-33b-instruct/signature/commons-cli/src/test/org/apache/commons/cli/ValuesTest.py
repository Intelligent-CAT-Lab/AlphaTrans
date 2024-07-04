from __future__ import annotations
import re
import os
import typing
from typing import *
import unittest
import pytest
import io
import unittest
from src.main.org.apache.commons.cli.CommandLine import *
from src.main.org.apache.commons.cli.CommandLineParser import *
from src.main.org.apache.commons.cli.Option import *
from src.main.org.apache.commons.cli.OptionBuilder import *
from src.main.org.apache.commons.cli.Options import *
from src.main.org.apache.commons.cli.PosixParser import *


class ValuesTest(unittest.TestCase):

    __cmd: CommandLine = None

    def testTwoArgValues(self) -> None:

        # Assuming that the hasOption2 method returns a boolean indicating whether the option is set
        assert self.__cmd.hasOption2("g"), "Option g is not set"

        # Assuming that the getOptionValues2 method returns a list of option values
        assert self.__cmd.getOptionValues2("g") == [
            "val1",
            "val2",
        ], "Option values are not as expected"

    def testShortArgsWithValue(self) -> None:

        # Assuming cmd is an instance of CommandLine
        self.assertTrue("Option b is not set", self.__cmd.hasOption2("b"))
        self.assertEqual("foo", self.__cmd.getOptionValue4("b"))
        self.assertEqual(1, len(self.__cmd.getOptionValues2("b")))

        self.assertTrue("Option d is not set", self.__cmd.hasOption2("d"))
        self.assertEqual("bar", self.__cmd.getOptionValue4("d"))
        self.assertEqual(1, len(self.__cmd.getOptionValues2("d")))

    def testShortArgs(self) -> None:

        assert self.__cmd.hasOption2("a") == True, "Option a is not set"
        assert self.__cmd.hasOption2("c") == True, "Option c is not set"

        assert self.__cmd.getOptionValues2("a") == None
        assert self.__cmd.getOptionValues2("c") == None

    def testMultipleArgValues(self) -> None:

        # Assuming that the CommandLine class has a method to check if an option is set
        self.assertTrue("Option e is not set", self.__cmd.hasOption2("e"))

        # Assuming that the CommandLine class has a method to get the values of an option
        self.assertListEqual(["one", "two"], self.__cmd.getOptionValues2("e"))

    def testExtraArgs(self) -> None:

        # Assuming that the CommandLine class has a method to set the arguments
        self.__cmd.setArgs(["arg1", "arg2", "arg3"])

        # Assuming that the CommandLine class has a method to get the arguments
        self.assertEqual(self.__cmd.getArgs(), ["arg1", "arg2", "arg3"], "Extra args")

    def testComplexValues(self) -> None:

        # assertTrue("Option i is not set", cmd.hasOption2("i"))
        self.assertTrue(self.__cmd.hasOption2("i"))

        # assertTrue("Option h is not set", cmd.hasOption2("h"))
        self.assertTrue(self.__cmd.hasOption2("h"))

        # assertArrayEquals(new String[] {"val1", "val2"}, cmd.getOptionValues2("h"))
        self.assertListEqual(self.__cmd.getOptionValues2("h"), ["val1", "val2"])

    def testCharSeparator(self) -> None:

        assert self.__cmd.hasOption2("j") == True
        assert self.__cmd.hasOption0("j") == True
        assert self.__cmd.getOptionValues2("j") == ["key", "value", "key", "value"]
        assert self.__cmd.getOptionValues0("j") == ["key", "value", "key", "value"]

        assert self.__cmd.hasOption2("k") == True
        assert self.__cmd.hasOption0("k") == True
        assert self.__cmd.getOptionValues2("k") == ["key1", "value1", "key2", "value2"]
        assert self.__cmd.getOptionValues0("k") == ["key1", "value1", "key2", "value2"]

        assert self.__cmd.hasOption2("m") == True
        assert self.__cmd.hasOption0("m") == True
        assert self.__cmd.getOptionValues2("m") == ["key", "value"]
        assert self.__cmd.getOptionValues0("m") == ["key", "value"]

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
