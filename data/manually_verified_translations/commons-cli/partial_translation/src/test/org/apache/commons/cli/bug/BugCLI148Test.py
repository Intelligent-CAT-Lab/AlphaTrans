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


class BugCLI148Test(unittest.TestCase):

    __options: Options = None

    def testWorkaround2(self) -> None:

        parser = PosixParser()
        args = ["-t", '"-something"']

        commandLine = parser.parse0(self.__options, args)
        self.assertEqual("-something", commandLine.getOptionValue0("t"))

    def testWorkaround1(self) -> None:

        parser = PosixParser()
        args = ["-t-something"]

        commandLine = parser.parse0(self.__options, args)
        self.assertEqual("-something", commandLine.getOptionValue0("t"))

    def setUp(self) -> None:

        self.__options = Options()
        self.__options.addOption0(OptionBuilder.hasArg0().create1("t"))
        self.__options.addOption0(OptionBuilder.hasArg0().create1("s"))
