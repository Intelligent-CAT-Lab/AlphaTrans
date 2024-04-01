# Imports Begin
from src.main.org.apache.commons.cli.PosixParser import *
from src.main.org.apache.commons.cli.Options import *
from src.main.org.apache.commons.cli.CommandLineParser import *
from src.main.org.apache.commons.cli.CommandLine import *
import unittest
import os

# Imports End


class ArgumentIsOptionTest(unittest.TestCase):

    # Class Fields Begin
    __options: Options = None
    __parser: CommandLineParser = None
    # Class Fields End

    # Class Methods Begin
    def testOptionWithArgument(self) -> None:

        args = ["-attr", "p"]
        cl = self.__parser.parse0(self.__options, args)
        self.assertFalse("Confirm -p is set", cl.hasOption2("p"))
        self.assertTrue("Confirm -attr is set", cl.hasOption2("attr"))
        self.assertEqual("Confirm arg of -attr", "p", cl.getOptionValue4("attr"))
        self.assertEqual("Confirm all arguments recognized", 0, cl.getArgs().length)

    def testOptionAndOptionWithArgument(self) -> None:

        args = ["-p", "-attr", "p"]
        cl = self.__parser.parse0(self.__options, args)
        self.assertTrue(cl.hasOption2("p"))
        self.assertTrue(cl.hasOption2("attr"))
        self.assertEqual("p", cl.getOptionValue4("attr"))
        self.assertEqual(0, len(cl.getArgs()))

    def testOption(self) -> None:

        args = ["-p"]
        cl = self.__parser.parse0(self.__options, args)
        self.assertTrue("Confirm -p is set", cl.hasOption2("p"))
        self.assertFalse("Confirm -attr is not set", cl.hasOption2("attr"))
        self.assertEqual("Confirm all arguments recognized", 0, cl.getArgs().length)

    def setUp(self) -> None:

        self.__options = (
            Options()
            .addOption1("p", False, "Option p")
            .addOption1("attr", True, "Option accepts argument")
        )
        self.__parser = PosixParser()

    # Class Methods End
