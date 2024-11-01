import pytest

from src.main.org.apache.commons.cli.AmbiguousOptionException import *
from src.main.org.apache.commons.cli.ParseException import *
from src.main.org.apache.commons.cli.Options import *
from src.main.org.apache.commons.cli.Option import *
from src.main.org.apache.commons.cli.DefaultParser import *
from src.main.org.apache.commons.cli.CommandLine import *
import unittest


class BugCLI252Test(unittest.TestCase):

    def __getOptions(self) -> Options:
        options = Options()
        options.addOption0(Option.builder0().longOpt("prefix").build())
        options.addOption0(Option.builder0().longOpt("prefixplusplus").build())
        return options
    

    @pytest.mark.test
    def testAmbiquousOptionName(self) -> None:
        try:
            with self.assertRaises(AmbiguousOptionException):
                DefaultParser(2, False, None).parse0(self.__getOptions(), ["--pref"])
        except ParseException as e:
            self.fail(f"Unexpected ParseException occurred: {e}")

    
    @pytest.mark.test
    def testExactOptionNameMatch(self) -> None:
        try:
            DefaultParser(2, False, None).parse0(self.__getOptions(), ["--prefix"])
        except ParseException as e:
            self.fail(f"Unexpected ParseException occurred: {e}")
