from __future__ import annotations
import re
import os
import unittest
import pytest
import io
import unittest
from src.main.org.apache.commons.cli.CommandLine import *
from src.main.org.apache.commons.cli.Option import *
from src.main.org.apache.commons.cli.Options import *
from src.main.org.apache.commons.cli.ParseException import *
from src.main.org.apache.commons.cli.PosixParser import *


class BugCLI133Test(unittest.TestCase):

    def testOrder(self) -> None:

        optionA = Option.Option1("a", "first")
        opts = Options()
        opts.addOption0(optionA)
        posixParser = Parser()
        line = posixParser.parse0(opts, None)
        self.assertFalse(line.hasOption2(None))
