from __future__ import annotations

# Imports Begin
from src.main.org.apache.commons.validator.routines.UrlValidator import *
from src.main.org.apache.commons.validator.routines.RegexValidator import *
from src.main.org.apache.commons.validator.routines.DomainValidator import *
from src.test.org.apache.commons.validator.ResultPair import *
import unittest
import os
import typing
from typing import *
import io
import pathlib

# Imports End


class UrlValidatorTest(unittest.TestCase):

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
    __schemes: typing.List[typing.List[str]] = None
    testScheme: typing.List[ResultPair] = None
    __printStatus: bool = None
    __printIndex: bool = None
    # Class Fields End

    # Class Methods Begin
    def testFragments_test3_decomposed(self) -> None:
        pass

    def testFragments_test2_decomposed(self) -> None:
        pass

    def testFragments_test1_decomposed(self) -> None:
        pass

    def testFragments_test0_decomposed(self) -> None:
        pass

    def testValidator283_test1_decomposed(self) -> None:
        pass

    def testValidator283_test0_decomposed(self) -> None:
        pass

    def testValidator467_test1_decomposed(self) -> None:
        pass

    def testValidator467_test0_decomposed(self) -> None:
        pass

    def testValidator420_test1_decomposed(self) -> None:
        pass

    def testValidator420_test0_decomposed(self) -> None:
        pass

    def testValidator380_test1_decomposed(self) -> None:
        pass

    def testValidator380_test0_decomposed(self) -> None:
        pass

    def testValidator382_test1_decomposed(self) -> None:
        pass

    def testValidator382_test0_decomposed(self) -> None:
        pass

    def testValidator353_test1_decomposed(self) -> None:
        pass

    def testValidator353_test0_decomposed(self) -> None:
        pass

    def testValidator375_test3_decomposed(self) -> None:
        pass

    def testValidator375_test2_decomposed(self) -> None:
        pass

    def testValidator375_test1_decomposed(self) -> None:
        pass

    def testValidator375_test0_decomposed(self) -> None:
        pass

    def testValidator363_test1_decomposed(self) -> None:
        pass

    def testValidator363_test0_decomposed(self) -> None:
        pass

    def testValidator361_test1_decomposed(self) -> None:
        pass

    def testValidator361_test0_decomposed(self) -> None:
        pass

    def testValidator290_test1_decomposed(self) -> None:
        pass

    def testValidator290_test0_decomposed(self) -> None:
        pass

    def testValidateUrl_test0_decomposed(self) -> None:
        pass

    def testValidator473_3_test0_decomposed(self) -> None:
        pass

    def testValidator473_2_test0_decomposed(self) -> None:
        pass

    def testValidator473_1_test0_decomposed(self) -> None:
        pass

    def testValidator452_test1_decomposed(self) -> None:
        pass

    def testValidator452_test0_decomposed(self) -> None:
        pass

    def testValidator464_test1_decomposed(self) -> None:
        pass

    def testValidator464_test0_decomposed(self) -> None:
        pass

    def testValidator411_test1_decomposed(self) -> None:
        pass

    def testValidator411_test0_decomposed(self) -> None:
        pass

    def testValidator342_test1_decomposed(self) -> None:
        pass

    def testValidator342_test0_decomposed(self) -> None:
        pass

    def testValidator339IDN_test1_decomposed(self) -> None:
        pass

    def testValidator339IDN_test0_decomposed(self) -> None:
        pass

    def testValidator339_test1_decomposed(self) -> None:
        pass

    def testValidator339_test0_decomposed(self) -> None:
        pass

    def testValidator309_test3_decomposed(self) -> None:
        pass

    def testValidator309_test2_decomposed(self) -> None:
        pass

    def testValidator309_test1_decomposed(self) -> None:
        pass

    def testValidator309_test0_decomposed(self) -> None:
        pass

    def testValidator391FAILS_test1_decomposed(self) -> None:
        pass

    def testValidator391FAILS_test0_decomposed(self) -> None:
        pass

    def testValidator391OK_test1_decomposed(self) -> None:
        pass

    def testValidator391OK_test0_decomposed(self) -> None:
        pass

    def testValidator276_test3_decomposed(self) -> None:
        pass

    def testValidator276_test2_decomposed(self) -> None:
        pass

    def testValidator276_test1_decomposed(self) -> None:
        pass

    def testValidator276_test0_decomposed(self) -> None:
        pass

    def testValidator288_test3_decomposed(self) -> None:
        pass

    def testValidator288_test2_decomposed(self) -> None:
        pass

    def testValidator288_test1_decomposed(self) -> None:
        pass

    def testValidator288_test0_decomposed(self) -> None:
        pass

    def testValidator248_test4_decomposed(self) -> None:
        pass

    def testValidator248_test3_decomposed(self) -> None:
        pass

    def testValidator248_test2_decomposed(self) -> None:
        pass

    def testValidator248_test1_decomposed(self) -> None:
        pass

    def testValidator248_test0_decomposed(self) -> None:
        pass

    def testValidator235_test2_decomposed(self) -> None:
        pass

    def testValidator235_test1_decomposed(self) -> None:
        pass

    def testValidator235_test0_decomposed(self) -> None:
        pass

    def testValidator218_test1_decomposed(self) -> None:
        pass

    def testValidator218_test0_decomposed(self) -> None:
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
    def main(args: typing.List[typing.List[str]]) -> None:
        pass

    @staticmethod
    def incrementTestPartsIndex(
        testPartsIndex: typing.List[int], testParts: typing.List[typing.Any]
    ) -> bool:
        pass

    def testIsValid1(self, testObjects: typing.List[typing.Any], options: int) -> None:
        pass

    def __testPartsIndextoString(self) -> str:
        pass

    # Class Methods End
