# Imports Begin
from src.main.org.apache.commons.cli.PosixParser import *
from src.main.org.apache.commons.cli.Options import *
from src.main.org.apache.commons.cli.Option import *
from src.main.org.apache.commons.cli.MissingArgumentException import *
from src.main.org.apache.commons.cli.CommandLineParser import *
from src.main.org.apache.commons.cli.CommandLine import *
import unittest
import os

# Imports End


class BugCLI71Test(unittest.TestCase):

    # Class Fields Begin
    __options: Options = None
    __parser: CommandLineParser = None
    # Class Fields End

    # Class Methods Begin
    def testMistakenArgument(self) -> None:

        args = ["-a", "Caesar", "-k", "A"]
        line = self.__parser.parse0(self.__options, args)
        args = ["-a", "Caesar", "-k", "a"]
        line = self.__parser.parse0(self.__options, args)
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

        args = ["-k", "-a", "Caesar"]
        self.__options.getOption("k").setOptionalArg(True)
        line = self.__parser.parse0(self.__options, args)
        self.assertEqual("Caesar", line.getOptionValue4("a"))
        self.assertEqual("a", line.getOptionValue1("k", "a"))

    def testBasic(self) -> None:

        args = ["-a", "Caesar", "-k", "A"]
        line = self.__parser.parse0(self.__options, args)
        self.assertEqual(line.getOptionValue4("a"), "Caesar")
        self.assertEqual(line.getOptionValue4("k"), "A")

    def setUp(self) -> None:

        self.__options = Options()
        algorithm = Option(
            0, "a", "algo", "the algorithm which it to perform executing", True, None
        )
        algorithm.setArgName("algorithm name")
        self.__options.addOption0(algorithm)
        key = Option(
            0, "k", "key", "the key the setted algorithm uses to process", True, None
        )
        key.setArgName("value")
        self.__options.addOption0(key)
        self.__parser = PosixParser()

    # Class Methods End
