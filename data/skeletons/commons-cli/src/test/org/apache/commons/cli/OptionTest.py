from __future__ import annotations

# Imports Begin
from src.main.org.apache.commons.cli.Option import *
import unittest
import typing
from typing import *
import io

# Imports End


class DefaultOption(Option):

    # Class Fields Begin
    __serialVersionUID: int = None
    __defaultValue: str = None
    # Class Fields End

    # Class Methods Begin
    def getValue0(self) -> str:
        pass

    def __init__(self, opt: str, description: str, defaultValue: str) -> None:
        pass

    # Class Methods End


class TestOption(Option):

    # Class Fields Begin
    __serialVersionUID: int = None
    # Class Fields End

    # Class Methods Begin
    def addValue(self, value: str) -> bool:
        pass

    def __init__(self, opt: str, hasArg: bool, description: str) -> None:
        pass

    # Class Methods End


class OptionTest(unittest.TestCase):

    # Class Fields Begin
    # Class Fields End

    # Class Methods Begin
    def testSubclass(self) -> None:
        pass

    def testHashCode(self) -> None:
        pass

    def testHasArgs(self) -> None:
        pass

    def testHasArgName(self) -> None:
        pass

    def testGetValue(self) -> None:
        pass

    def testClone(self) -> None:
        pass

    def testClear(self) -> None:
        pass

    def testBuilderMethods(self) -> None:
        pass

    def testBuilderInvalidOptionName4(self) -> None:
        pass

    def testBuilderInvalidOptionName3(self) -> None:
        pass

    def testBuilderInvalidOptionName2(self) -> None:
        pass

    def testBuilderInvalidOptionName1(self) -> None:
        pass

    def testBuilderInsufficientParams2(self) -> None:
        pass

    def testBuilderInsufficientParams1(self) -> None:
        pass

    @staticmethod
    def __checkOption(
        option: Option,
        opt: str,
        description: str,
        longOpt: str,
        numArgs: int,
        argName: str,
        required: bool,
        optionalArg: bool,
        valueSeparator: str,
        cls: typing.Type[typing.Any],
    ) -> None:
        pass

    # Class Methods End
