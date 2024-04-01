# Imports Begin
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
    def testExactOptionNameMatch(self) -> None:

        self.parse0(self.__getOptions(), ["--prefix"])

    def testAmbiquousOptionName(self) -> None:

        self.parse0(self.__getOptions(), ["--pref"])

    def __getOptions(self) -> Options:

        options = Options()
        options.addOption0(Option.builder0().longOpt("prefix").build())
        options.addOption0(Option.builder0().longOpt("prefixplusplus").build())
        return options

    # Class Methods End
