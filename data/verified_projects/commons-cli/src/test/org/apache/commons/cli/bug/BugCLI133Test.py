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
    def test_Order(self) -> None:
        try:
            optionA = Option.Option1("a", "first")
            opts = Options()
            opts.addOption0(optionA)
            posixParser = PosixParser()
            line = posixParser.parse0(opts, None)
            self.assertFalse(line.hasOption2(None))
        except ParseException as e:
            self.fail(f"ParseException occurred: {e}")

    # Class Methods End
