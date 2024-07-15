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

        # Create an instance of DefaultParser
        parser = DefaultParser(2, False, None)

        # Call the parse0 method with the options and arguments
        parser.parse0(self.__getOptions(), ["--prefix"])

    def testAmbiquousOptionName(self) -> None:

        # Create an instance of DefaultParser
        parser = DefaultParser(2, False, None)

        # Call the parse0 method with the options and arguments
        try:
            parser.parse0(self.__getOptions(), ["--pref"])
        except ParseException as e:
            # Check if the exception is an AmbiguousOptionException
            if isinstance(e, AmbiguousOptionException):
                pass  # or handle the exception as needed
            else:
                raise e

    def __getOptions(self) -> Options:

        options = Options()
        options.addOption0(Option.builder0().longOpt("prefix").build())
        options.addOption0(Option.builder0().longOpt("prefixplusplus").build())
        return options
