import pytest

from src.main.org.apache.commons.cli.PosixParser import *
from src.main.org.apache.commons.cli.Options import *
from src.main.org.apache.commons.cli.OptionBuilder import *
from src.main.org.apache.commons.cli.Option import *
from src.main.org.apache.commons.cli.CommandLineParser import *
from src.main.org.apache.commons.cli.CommandLine import *
import unittest
from typing import *


class ValuesTest(unittest.TestCase):

    def setUp(self) -> None:
        try:
            options = Options()

            options.addOption1("a", False, "toggle -a")
            options.addOption1("b", True, "set -b")
            options.addOption3("c", "c", False, "toggle -c")
            options.addOption3("d", "d", True, "set -d")

            options.addOption0(
                OptionBuilder.withLongOpt("e")
                .hasArgs0()
                .withDescription("set -e ")
                .create1('e')
            )
            options.addOption3("f", "f", False, "jk")
            options.addOption0(
                OptionBuilder.withLongOpt("g")
                .hasArgs1(2)
                .withDescription("set -g")
                .create1('g')
            )
            options.addOption0(
                OptionBuilder.withLongOpt("h")
                .hasArg0()
                .withDescription("set -h")
                .create1('h')
            )
            options.addOption0(
                OptionBuilder.withLongOpt("i").withDescription("set -i").create1('i')
            )
            options.addOption0(
                OptionBuilder.withLongOpt("j")
                .hasArgs0()
                .withDescription("set -j")
                .withValueSeparator1('=')
                .create1('j')
            )
            options.addOption0(
                OptionBuilder.withLongOpt("k")
                .hasArgs0()
                .withDescription("set -k")
                .withValueSeparator1('=')
                .create1('k')
            )
            options.addOption0(
                OptionBuilder.withLongOpt("m")
                .hasArgs0()
                .withDescription("set -m")
                .withValueSeparator0()
                .create1('m')
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
        except Exception as e:
            self.fail(f"An exception occurred when setting up the test: {e}")


    @pytest.mark.test
    def testCharSeparator(self) -> None:
        self.assertTrue(self.__cmd.hasOption2("j"), "Option j is not set")
        self.assertTrue(self.__cmd.hasOption0('j'), "Option j is not set")
        self.assertListEqual(["key", "value", "key", "value"], self.__cmd.getOptionValues2("j"))
        self.assertListEqual(["key", "value", "key", "value"], self.__cmd.getOptionValues0('j'))

        self.assertTrue(self.__cmd.hasOption2("k"), "Option k is not set")
        self.assertTrue(self.__cmd.hasOption0('k'), "Option k is not set")
        self.assertListEqual(
            ["key1", "value1", "key2", "value2"], self.__cmd.getOptionValues2("k"))
        self.assertListEqual(
            ["key1", "value1", "key2", "value2"], self.__cmd.getOptionValues0('k'))

        self.assertTrue(self.__cmd.hasOption2("m"), "Option m is not set")
        self.assertTrue(self.__cmd.hasOption0('m'), "Option m is not set")
        self.assertListEqual(["key", "value"], self.__cmd.getOptionValues2("m"))
        self.assertListEqual(["key", "value"], self.__cmd.getOptionValues0('m'))
    
    
    @pytest.mark.test
    def testComplexValues(self) -> None:
        self.assertTrue(self.__cmd.hasOption2("i"), "Option i is not set")
        self.assertTrue(self.__cmd.hasOption2("h"), "Option h is not set")
        self.assertListEqual(["val1", "val2"], self.__cmd.getOptionValues2("h"))

    
    @pytest.mark.test
    def testExtraArgs(self) -> None:
        self.assertListEqual(["arg1", "arg2", "arg3"], self.__cmd.getArgs(), "Extra args")
    
    
    @pytest.mark.test
    def testMultipleArgValues(self) -> None:
        self.assertTrue(self.__cmd.hasOption2("e"), "Option e is not set")
        self.assertListEqual(["one", "two"], self.__cmd.getOptionValues2("e"))

    
    @pytest.mark.test
    def testShortArgs(self) -> None:
        self.assertTrue(self.__cmd.hasOption2("a"), "Option a is not set")
        self.assertTrue(self.__cmd.hasOption2("c"), "Option c is not set")

        self.assertIsNone(self.__cmd.getOptionValues2("a"))
        self.assertIsNone(self.__cmd.getOptionValues2("c"))

    
    @pytest.mark.test
    def testShortArgsWithValue(self) -> None:
        self.assertTrue(self.__cmd.hasOption2("b"), "Option b is not set")
        self.assertEqual("foo", self.__cmd.getOptionValue4("b"))
        self.assertEqual(1, len(self.__cmd.getOptionValues2("b")))

        self.assertTrue(self.__cmd.hasOption2("d"), "Option d is not set")
        self.assertEqual("bar", self.__cmd.getOptionValue4("d"))
        self.assertEqual(1, len(self.__cmd.getOptionValues2("d")))
    
    
    @pytest.mark.test
    def testTwoArgValues(self) -> None:
        self.assertTrue(self.__cmd.hasOption2("g"), "Option g is not set")
        self.assertListEqual(["val1", "val2"], self.__cmd.getOptionValues2("g"))
