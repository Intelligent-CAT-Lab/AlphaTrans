from __future__ import annotations
import re
import os
import unittest
import pytest
import io
import unittest
from src.main.org.apache.commons.cli.CommandLine import *
from src.main.org.apache.commons.cli.CommandLineParser import *
from src.main.org.apache.commons.cli.Options import *
from src.main.org.apache.commons.cli.PosixParser import *


class ArgumentIsOptionTest(unittest.TestCase):

    __parser: CommandLineParser = None

    __options: Options = None

    def testOptionWithArgument(self) -> None:

        args = ["-attr", "p"]

        cl = self.__parser.parse0(self.__options, args)
        self.assertFalse(cl.hasOption2("p"))
        self.assertTrue(cl.hasOption2("attr"))
        self.assertEqual(cl.getOptionValue4("attr"), "p")
        self.assertEqual(len(cl.getArgs()), 0)

    def testOptionAndOptionWithArgument(self) -> None:

        args = ["-p", "-attr", "p"]

        cl = self.__parser.parse0(self.__options, args)
        self.assertTrue("Confirm -p is set", cl.hasOption2("p"))
        self.assertTrue("Confirm -attr is set", cl.hasOption2("attr"))
        self.assertEqual("Confirm arg of -attr", "p", cl.getOptionValue4("attr"))
        self.assertEqual("Confirm all arguments recognized", 0, len(cl.getArgs()))

    def testOption(self) -> None:

        args = ["-p"]

        cl = self.__parser.parse0(self.__options, args)
        self.assertTrue("Confirm -p is set", cl.hasOption2("p"))
        self.assertFalse("Confirm -attr is not set", cl.hasOption2("attr"))
        self.assertEqual("Confirm all arguments recognized", 0, len(cl.getArgs()))

    def setUp(self) -> None:

        self.__options = Options()
        self.__options.addOption1("p", False, "Option p")
        self.__options.addOption1("attr", True, "Option accepts argument")
        self.__parser = PosixParser()
