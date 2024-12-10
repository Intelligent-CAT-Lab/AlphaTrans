from __future__ import annotations
import re
import os
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

        self.assertTrue("Option g is not set", self.__cmd.hasOption2("g"))
        self.assertEqual(["val1", "val2"], self.__cmd.getOptionValues2("g"))

    def testShortArgsWithValue(self) -> None:

        self.assertTrue("Option b is not set", self.__cmd.hasOption2("b"))
        self.assertEqual("foo", self.__cmd.getOptionValue4("b"))
        self.assertEqual(1, len(self.__cmd.getOptionValues2("b")))

        self.assertTrue("Option d is not set", self.__cmd.hasOption2("d"))
        self.assertEqual("bar", self.__cmd.getOptionValue4("d"))
        self.assertEqual(1, len(self.__cmd.getOptionValues2("d")))

    def testShortArgs(self) -> None:

        self.assertTrue("Option a is not set", self.__cmd.hasOption2("a"))
        self.assertTrue("Option c is not set", self.__cmd.hasOption2("c"))

        self.assertIsNone(self.__cmd.getOptionValues2("a"))
        self.assertIsNone(self.__cmd.getOptionValues2("c"))

    def testMultipleArgValues(self) -> None:

        self.assertTrue("Option e is not set", self.__cmd.hasOption2("e"))
        self.assertEqual(["one", "two"], self.__cmd.getOptionValues2("e"))

    def testExtraArgs(self) -> None:

        self.assertEqual(self.__cmd.getArgs(), ["arg1", "arg2", "arg3"])

    def testComplexValues(self) -> None:

        self.assertTrue("Option i is not set", self.__cmd.hasOption2("i"))
        self.assertTrue("Option h is not set", self.__cmd.hasOption2("h"))
        self.assertEqual(["val1", "val2"], self.__cmd.getOptionValues2("h"))

    def testCharSeparator(self) -> None:

        assert self.__cmd.hasOption2("j")
        assert self.__cmd.hasOption0("j")
        assert self.__cmd.getOptionValues2("j") == ["key=value", "key=value"]
        assert self.__cmd.getOptionValues0("j") == ["key=value", "key=value"]

        assert self.__cmd.hasOption2("k")
        assert self.__cmd.hasOption0("k")
        assert self.__cmd.getOptionValues2("k") == ["key1=value1", "key2=value2"]
        assert self.__cmd.getOptionValues0("k") == ["key1=value1", "key2=value2"]

        assert self.__cmd.hasOption2("m")
        assert self.__cmd.hasOption0("m")
        assert self.__cmd.getOptionValues2("m") == ["key=value"]
        assert self.__cmd.getOptionValues0("m") == ["key=value"]

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
