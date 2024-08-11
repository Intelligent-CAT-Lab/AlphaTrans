from __future__ import annotations

# Imports Begin
from src.main.org.apache.commons.codec.binary.CharSequenceUtils import *
import unittest
import os
import typing
from typing import *
import io
from abc import ABC

# Imports End


class TestData:

    # Class Fields Begin
    source: str = None
    ignoreCase: bool = None
    toffset: int = None
    other: str = None
    ooffset: int = None
    len: int = None
    expected: bool = None
    throwable: typing.Type[BaseException] = None
    # Class Fields End

    # Class Methods Begin
    def toString(self) -> str:
        pass

    def __init__(
        self,
        constructorId: int,
        expected: bool,
        ooffset: int,
        source: str,
        throwable: typing.Type[BaseException],
        toffset: int,
        ignoreCase: bool,
        other: str,
        len_: int,
    ) -> None:
        pass

    # Class Methods End


class RunTest(ABC):

    # Class Fields Begin
    # Class Fields End

    # Class Methods Begin
    def run(self, data: TestData, id_: str) -> None:
        pass

    def invoke(self) -> bool:
        pass

    # Class Methods End


class CharSequenceUtilsTest(unittest.TestCase):

    # Class Fields Begin
    __TEST_DATA: typing.List[TestData] = None
    # Class Fields End

    # Class Methods Begin
    def testConstructor_test0_decomposed(self) -> None:
        pass

    def testRegionMatches_test0_decomposed(self) -> None:
        pass

    # Class Methods End
