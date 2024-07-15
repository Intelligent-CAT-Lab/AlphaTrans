from __future__ import annotations

# Imports Begin
from src.main.org.apache.commons.cli.PosixParser import *
from src.main.org.apache.commons.cli.Parser import *
from src.main.org.apache.commons.cli.Options import *
from src.main.org.apache.commons.cli.OptionGroup import *
from src.main.org.apache.commons.cli.OptionBuilder import *
from src.main.org.apache.commons.cli.Option import *
from src.main.org.apache.commons.cli.CommandLine import *
from src.main.org.apache.commons.cli.AlreadySelectedException import *
import unittest
import io

# Imports End


class OptionGroupTest(unittest.TestCase):

    # Class Fields Begin
    __options: Options = None
    __parser: Parser = None
    # Class Fields End

    # Class Methods Begin
    def testValidLongOnlyOptions(self) -> None:
        pass

    def testTwoValidOptions(self) -> None:
        pass

    def testTwoValidLongOptions(self) -> None:
        pass

    def testTwoOptionsFromGroupWithProperties(self) -> None:
        pass

    def testTwoOptionsFromGroup(self) -> None:
        pass

    def testTwoOptionsFromDifferentGroup(self) -> None:
        pass

    def testTwoLongOptionsFromGroup(self) -> None:
        pass

    def testToString(self) -> None:
        pass

    def testSingleOptionFromGroup(self) -> None:
        pass

    def testSingleOption(self) -> None:
        pass

    def testSingleLongOption(self) -> None:
        pass

    def testNoOptionsExtraArgs(self) -> None:
        pass

    def testGetNames(self) -> None:
        pass

    def setUp(self) -> None:
        pass

    # Class Methods End
