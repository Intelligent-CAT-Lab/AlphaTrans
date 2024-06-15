import pytest

# Imports Begin
from src.main.org.apache.commons.cli.PosixParser import *
from src.main.org.apache.commons.cli.Options import *
from src.main.org.apache.commons.cli.CommandLineParser import *
from src.main.org.apache.commons.cli.CommandLine import *
import unittest

# Imports End


class ArgumentIsOptionTest(unittest.TestCase):

    # Class Methods Begin
    def setUp(self) -> None:

        self.__options = Options().addOption1("p", False, "Option p")\
            .addOption1("attr", True, "Option accepts argument")
        self.__parser = PosixParser()
    
    @pytest.mark.test
    def testOption(self) -> None:

        try:
            args = ["-p"]
            cl = self.__parser.parse0(self.__options, args)
            self.assertTrue(cl.hasOption2("p"), "Confirm -p is set")
            self.assertFalse(cl.hasOption2("attr"), "Confirm -attr is not set")
            self.assertEqual(0, len(cl.getArgs()), "Confirm all arguments recognized")
        except Exception as e:
            self.fail(f"An exception occurred: {e}")

    @pytest.mark.test
    def testOptionAndOptionWithArgument(self) -> None:

        try:
            args = ["-p", "-attr", "p"]
            cl = self.__parser.parse0(self.__options, args)
            self.assertTrue(cl.hasOption2("p"), "Confirm -p is set")
            self.assertTrue(cl.hasOption2("attr"), "Confirm -attr is set")
            self.assertEqual("p", cl.getOptionValue4("attr"), "Confirm arg of -attr")
            self.assertEqual(0, len(cl.getArgs()), "Confirm all arguments recognized")
        except Exception as e:
            self.fail(f"An exception occurred: {e}")

    @pytest.mark.test
    def testOptionWithArgument(self) -> None:

        try:
            args = ["-attr", "p"]
            cl = self.__parser.parse0(self.__options, args)
            self.assertFalse(cl.hasOption2("p"), "Confirm -p is not set")
            self.assertTrue(cl.hasOption2("attr"), "Confirm -attr is set")
            self.assertEqual("p", cl.getOptionValue4("attr"), "Confirm arg of -attr")
            self.assertEqual(0, len(cl.getArgs()), "Confirm all arguments recognized")
        except Exception as e:
            self.fail(f"An exception occurred: {e}")

    # Class Methods End
