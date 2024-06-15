import pytest

# Imports Begin
from src.main.org.apache.commons.cli.PosixParser import *
from src.main.org.apache.commons.cli.Options import *
from src.main.org.apache.commons.cli.OptionBuilder import *
from src.main.org.apache.commons.cli.Option import *
from src.main.org.apache.commons.cli.CommandLineParser import *
from src.main.org.apache.commons.cli.CommandLine import *
import unittest

# Imports End


class BugCLI148Test(unittest.TestCase):

    # Class Fields Begin
    __options: Options = None
    # Class Fields End

    # Class Methods Begin
    def setUp(self) -> None:
        self.__options = Options()
        self.__options.addOption0(OptionBuilder.hasArg0().create1('t'))
        self.__options.addOption0(OptionBuilder.hasArg0().create1('s'))

    
    @pytest.mark.test
    def testWorkaround1(self) -> None:
        try:
            parser = PosixParser()
            args = ["-t-something"]

            commandLine = parser.parse0(self.__options, args)
            self.assertEqual("-something", commandLine.getOptionValue0('t'))
        except Exception as e:
            self.fail(f"An exception occurred: {e}")

    
    @pytest.mark.test
    def testWorkaround2(self) -> None:
        try:
            parser = PosixParser()
            args = ["-t", "\"-something\""]

            commandLine = parser.parse0(self.__options, args)
            self.assertEqual("-something", commandLine.getOptionValue0('t'))
        except Exception as e:
            self.fail(f"An exception occurred: {e}")

    # Class Methods End
