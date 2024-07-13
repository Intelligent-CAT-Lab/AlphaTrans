from __future__ import annotations

# Imports Begin
from src.main.org.apache.commons.validator.routines.UrlValidator import *
from src.main.org.apache.commons.validator.routines.RegexValidator import *
from src.main.org.apache.commons.validator.routines.DomainValidator import *
from src.test.org.apache.commons.validator.ResultPair import *
import unittest
import typing
from typing import *
import io
import pathlib

# Imports End


class UrlValidatorTest(unittest.TestCase):

    # Class Fields Begin
    __printStatus: bool = None
    __printIndex: bool = None
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
    # Class Fields End

    # Class Methods Begin
    def testFragments(self) -> None:
        pass

    def testValidator283(self) -> None:
        pass

    def testValidator467(self) -> None:
        pass

    def testValidator420(self) -> None:
        pass

    def testValidator380(self) -> None:
        pass

    def testValidator382(self) -> None:
        pass

    def testValidator353(self) -> None:
        pass

    def testValidator375(self) -> None:
        pass

    def testValidator363(self) -> None:
        pass

    def testValidator361(self) -> None:
        pass

    def testValidator290(self) -> None:
        pass

    def testValidateUrl(self) -> None:
        pass

    def testValidator473_3(self) -> None:
        pass

    def testValidator473_2(self) -> None:
        pass

    def testValidator473_1(self) -> None:
        pass

    def testValidator452(self) -> None:
        pass

    def testValidator464(self) -> None:
        pass

    def testValidator411(self) -> None:
        pass

    def testValidator342(self) -> None:
        pass

    def testValidator339IDN(self) -> None:
        pass

    def testValidator339(self) -> None:
        pass

    def testValidator309(self) -> None:
        pass

    def testValidator391FAILS(self) -> None:
        pass

    def testValidator391OK(self) -> None:
        pass

    def testValidator276(self) -> None:
        pass

    def testValidator288(self) -> None:
        pass

    def testValidator248(self) -> None:
        pass

    def testValidator235(self) -> None:
        pass

    def testValidator218(self) -> None:
        pass

    def testValidator204(self) -> None:
        pass

    def testValidator202(self) -> None:
        pass

    def testIsValidScheme(self) -> None:
        pass

    def testIsValid0(self) -> None:
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
