# Imports Begin
from src.main.org.apache.commons.cli.PosixParser import *
from src.main.org.apache.commons.cli.ParseException import *
from src.main.org.apache.commons.cli.Options import *
from src.main.org.apache.commons.cli.Option import *
from src.main.org.apache.commons.cli.CommandLine import *
import unittest
import os

# Imports End


class BugCLI133Test(unittest.TestCase):

    # Class Fields Begin
    # Class Fields End

    # Class Methods Begin
    def testOrder(self) -> None:

        option_a = self.Option1("a", "first")
        opts = Options()
        opts.addOption0(option_a)
        posix_parser = PosixParser()
        line = posix_parser.parse0(opts, None)
        self.assertFalse(line.hasOption2(None))

    # Class Methods End
