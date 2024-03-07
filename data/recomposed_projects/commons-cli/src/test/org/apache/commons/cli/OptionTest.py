# Imports Begin
from src.main.org.apache.commons.cli.Option import *
import unittest
import typing
from typing import *

# Imports End


class DefaultOption(unittest.TestCase, Option):

    # Class Fields Begin
    __serialVersionUID: int = 1
    __defaultValue: str = None
    # Class Fields End

    # Class Methods Begin
    def getValue0(self) -> str:

        return (
            super().getValue0()
            if super().getValue0() is not None
            else self.__defaultValue
        )

    def __init__(self, opt: str, description: str, defaultValue: str) -> None:

        super().__init__(-1, None, None, None, False, None)
        self.__defaultValue = defaultValue

    # Class Methods End


class OptionTest(unittest.TestCase):

    # Class Fields Begin
    # Class Fields End

    # Class Methods Begin
    def testSubclass(self) -> None:

        pass  # LLM could not translate method body

    def testHashCode(self) -> None:

        pass  # LLM could not translate method body

    def testHasArgs(self) -> None:

        pass  # LLM could not translate method body

    def testHasArgName(self) -> None:

        pass  # LLM could not translate method body

    def testGetValue(self) -> None:

        pass  # LLM could not translate method body

    def testClone(self) -> None:

        pass  # LLM could not translate method body

    def testClear(self) -> None:

        pass  # LLM could not translate method body

    def testBuilderMethods(self) -> None:

        pass  # LLM could not translate method body

    def testBuilderInvalidOptionName4(self) -> None:

        Option.builder1("invalid@")

    def testBuilderInvalidOptionName3(self) -> None:

        Option.builder1("invalid?")

    def testBuilderInvalidOptionName2(self) -> None:

        self.builder0().option("invalid@")

    def testBuilderInvalidOptionName1(self) -> None:

        self.option("invalid?")

    def testBuilderInsufficientParams2(self) -> None:

        Option.builder1(None).desc("desc").build()

    def testBuilderInsufficientParams1(self) -> None:

        self.builder0().desc("desc").build()

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

        pass  # LLM could not translate method body

    # Class Methods End


class TestOption(unittest.TestCase, Option):

    # Class Fields Begin
    __serialVersionUID: int = 1
    # Class Fields End

    # Class Methods Begin
    def addValue(self, value: str) -> bool:

        self.addValueForProcessing(value)
        return True

    def __init__(self, opt: str, hasArg: bool, description: str) -> None:

        super().__init__(-1, opt, None, description, hasArg, None)

    # Class Methods End
