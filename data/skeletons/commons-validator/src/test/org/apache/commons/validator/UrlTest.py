from __future__ import annotations

# Imports Begin
from src.main.org.apache.commons.validator.UrlValidator import *
from src.test.org.apache.commons.validator.ResultPair import *
import unittest
import os
import typing
from typing import *
import io
import pathlib

# Imports End


class UrlTest(unittest.TestCase):

    # Class Fields Begin
    testUrlScheme: typing.List[ResultPair] = None
    testUrlAuthority: typing.List[ResultPair] = None
    testUrlPort: typing.List[ResultPair] = None
    testPath: typing.List[ResultPair] = None
    testUrlPathOptions: typing.List[ResultPair] = None
    testUrlQuery: typing.List[ResultPair] = None
    testUrlParts: typing.List[typing.Any] = None
    testUrlPartsOptions: typing.List[typing.Any] = None
    testPartsIndex: typing.List[int] = None
    testScheme: typing.List[ResultPair] = None
    __printStatus: bool = None
    __printIndex: bool = None
    # Class Fields End

    # Class Methods Begin
    def testValidateUrl_test0_decomposed(self) -> None:
        pass

    def testValidator204_test1_decomposed(self) -> None:
        pass

    def testValidator204_test0_decomposed(self) -> None:
        pass

    def testValidator202_test1_decomposed(self) -> None:
        pass

    def testValidator202_test0_decomposed(self) -> None:
        pass

    def testIsValidScheme_test2_decomposed(self) -> None:
        pass

    def testIsValidScheme_test1_decomposed(self) -> None:
        pass

    def testIsValidScheme_test0_decomposed(self) -> None:
        pass

    def testIsValid0_test2_decomposed(self) -> None:
        pass

    def testIsValid0_test1_decomposed(self) -> None:
        pass

    def testIsValid0_test0_decomposed(self) -> None:
        pass

    def setUp(self) -> None:
        pass

    @staticmethod
    def main(argv: typing.List[typing.List[str]]) -> None:
        pass

    @staticmethod
    def incrementTestPartsIndex(
        testPartsIndex: typing.List[int], testParts: typing.List[typing.Any]
    ) -> bool:
        pass

    def testIsValid1(self, testObjects: typing.List[typing.Any], options: int) -> None:
        pass

    def __init__(self, testName: str) -> None:
        pass

    def __testPartsIndextoString(self) -> str:
        pass

    # Class Methods End
