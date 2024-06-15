from __future__ import annotations
import unittest
import pytest
import io
from src.main.org.apache.commons.cli.CommandLine import *
from src.main.org.apache.commons.cli.DefaultParser import *
from src.main.org.apache.commons.cli.Option import *
from src.main.org.apache.commons.cli.Options import *
from src.main.org.apache.commons.cli.ParseException import *


class BugCLI252Test(unittest.TestCase):

    def testExactOptionNameMatch(self) -> None:

        # Create an instance of DefaultParser
        parser = DefaultParser(2, False, None)

        # Call the parse0 method
        try:
            parser.parse0(self.__getOptions(), ["--prefix"])
        except ParseException as e:
            print("ParseException: ", e)

    def testAmbiquousOptionName(self) -> None:

        try:
            DefaultParser(2, False, None).parse0(self.__getOptions(), ["--pref"])
        except ParseException as e:
            print(e)

    def __getOptions(self) -> Options:

        options = Options()
        options.addOption0(Option.builder0().longOpt("prefix").build())
        options.addOption0(Option.builder0().longOpt("prefixplusplus").build())
        return options
