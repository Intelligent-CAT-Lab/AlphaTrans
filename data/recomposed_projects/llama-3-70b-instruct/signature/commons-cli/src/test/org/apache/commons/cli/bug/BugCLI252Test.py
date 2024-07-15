from __future__ import annotations
import re
import unittest
import pytest
import io
import unittest
from src.main.org.apache.commons.cli.CommandLine import *
from src.main.org.apache.commons.cli.DefaultParser import *
from src.main.org.apache.commons.cli.Option import *
from src.main.org.apache.commons.cli.Options import *
from src.main.org.apache.commons.cli.ParseException import *


class BugCLI252Test(unittest.TestCase):

    def testExactOptionNameMatch(self) -> None:
        DefaultParser(2, False, None).parse0(self.__getOptions(), ["--prefix"])

    def testAmbiquousOptionName(self) -> None:
        with self.assertRaises(AmbiguousOptionException):
            DefaultParser(2, False, None).parse0(self.__getOptions(), ["--pref"])

    def __getOptions(self) -> Options:
        options = Options()
        options.addOption0(Builder().longOpt("prefix").build())
        options.addOption0(Builder().longOpt("prefixplusplus").build())
        return options
