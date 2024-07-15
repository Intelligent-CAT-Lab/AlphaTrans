from __future__ import annotations

# Imports Begin
from src.main.org.apache.commons.cli.Options import *
from src.main.org.apache.commons.cli.Option import *
from src.main.org.apache.commons.cli.DefaultParser import *
from src.main.org.apache.commons.cli.CommandLine import *
import unittest
import io

# Imports End


class BugCLI265Test(unittest.TestCase):

    # Class Fields Begin
    __parser: DefaultParser = None
    __options: Options = None
    # Class Fields End

    # Class Methods Begin
    def shouldParseShortOptionWithValue(self) -> None:
        pass

    def shouldParseShortOptionWithoutValue(self) -> None:
        pass

    def shouldParseConcatenatedShortOptions(self) -> None:
        pass

    def setUp(self) -> None:
        pass

    # Class Methods End
