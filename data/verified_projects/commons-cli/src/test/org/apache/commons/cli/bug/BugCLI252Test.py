# Imports Begin
from src.main.org.apache.commons.cli.AmbiguousOptionException import *
from src.main.org.apache.commons.cli.ParseException import *
from src.main.org.apache.commons.cli.Options import *
from src.main.org.apache.commons.cli.Option import *
from src.main.org.apache.commons.cli.DefaultParser import *
from src.main.org.apache.commons.cli.CommandLine import *
import unittest

# Imports End


class BugCLI252Test(unittest.TestCase):

    # Class Fields Begin
    # Class Fields End

    # Class Methods Begin
    def __getOptions(self) -> Options:
        options = Options()
        options.addOption0(Option.builder0().longOpt("prefix").build())
        options.addOption0(Option.builder0().longOpt("prefixplusplus").build())
        return options
    

    def test_AmbiquousOptionName(self) -> None:
        try:
            with self.assertRaises(AmbiguousOptionException):
                DefaultParser(2, False, None).parse0(self.__getOptions(), ["--pref"])
        except ParseException as e:
            self.fail(f"Unexpected ParseException occurred: {e}")

    
    def test_ExactOptionNameMatch(self) -> None:
        try:
            DefaultParser(2, False, None).parse0(self.__getOptions(), ["--prefix"])
        except ParseException as e:
            self.fail(f"Unexpected ParseException occurred: {e}")
    # Class Methods End
