from __future__ import annotations

# Imports Begin
from src.main.org.apache.commons.validator.Field import *
from src.main.org.apache.commons.validator.Arg import *
import unittest
import os
import typing
from typing import *
import io

# Imports End


class FieldTest(unittest.TestCase):

    # Class Fields Begin
    _field: typing.Any = None
    # Class Fields End

    # Class Methods Begin
    def tearDown(self) -> None:
        pass

    def setUp(self) -> None:
        pass

    def testOverrideSomePosition(self) -> None:
        pass

    def testOverridePositionImplied(self) -> None:
        pass

    def testOverrideUsingPositionB(self) -> None:
        pass

    def testOverrideUsingPositionA(self) -> None:
        pass

    def testDefaultSomePositions(self) -> None:
        pass

    def testDefaultOnePosition(self) -> None:
        pass

    def testDefaultUsingPositions(self) -> None:
        pass

    def testDefaultPositionImplied(self) -> None:
        pass

    def testEmptyArgs(self) -> None:
        pass

    @staticmethod
    def FieldTest1() -> FieldTest:
        pass

    def __init__(self, name: str) -> None:
        pass

    def __createArg3(self, key: str, name: str, position: int) -> Arg:
        pass

    def __createArg2(self, key: str, name: str) -> Arg:
        pass

    def __createArg1(self, key: str, position: int) -> Arg:
        pass

    def __createArg0(self, key: str) -> Arg:
        pass

    # Class Methods End
