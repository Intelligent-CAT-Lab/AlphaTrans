from __future__ import annotations
import unittest
import pytest
import io
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
        assert not cl.hasOption2("p"), "Confirm -p is set"
        assert cl.hasOption2("attr"), "Confirm -attr is set"
        assert cl.getOptionValue4("attr") == "p", "Confirm arg of -attr"
        assert len(cl.getArgs()) == 0, "Confirm all arguments recognized"

    def testOptionAndOptionWithArgument(self) -> None:

        args = ["-p", "-attr", "p"]

        cl = self.__parser.parse0(self.__options, args)
        assert cl.hasOption2("p") == True, "Confirm -p is set"
        assert cl.hasOption2("attr") == True, "Confirm -attr is set"
        assert cl.getOptionValue4("attr") == "p", "Confirm arg of -attr"
        assert len(cl.getArgs()) == 0, "Confirm all arguments recognized"

    def testOption(self) -> None:

        args = ["-p"]

        cl = self.__parser.parse0(self.__options, args)
        assert cl.hasOption2("p"), "Confirm -p is set"
        assert not cl.hasOption2("attr"), "Confirm -attr is not set"
        assert len(cl.getArgs()) == 0, "Confirm all arguments recognized"

    def setUp(self) -> None:

        self.__options = Options()
        self.__options.addOption1("p", False, "Option p")
        self.__options.addOption1("attr", True, "Option accepts argument")

        self.__parser = PosixParser()
