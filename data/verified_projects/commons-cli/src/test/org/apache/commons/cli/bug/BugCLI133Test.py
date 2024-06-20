import pytest

from src.main.org.apache.commons.cli.PosixParser import *
from src.main.org.apache.commons.cli.ParseException import *
from src.main.org.apache.commons.cli.Options import *
from src.main.org.apache.commons.cli.Option import *
from src.main.org.apache.commons.cli.CommandLine import *
import unittest


class BugCLI133Test(unittest.TestCase):

    @pytest.mark.test
    def testOrder(self) -> None:
        try:
            optionA = Option.Option1("a", "first")
            opts = Options()
            opts.addOption0(optionA)
            posixParser = PosixParser()
            line = posixParser.parse0(opts, None)
            self.assertFalse(line.hasOption2(None))
        except ParseException as e:
            self.fail(f"ParseException occurred: {e}")

