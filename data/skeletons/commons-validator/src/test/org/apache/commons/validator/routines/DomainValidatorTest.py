from __future__ import annotations

# Imports Begin
from src.main.org.apache.commons.validator.routines.DomainValidator import *
import enum
import unittest
import os
import typing
from typing import *
import io
import pathlib

# Imports End


class DomainValidatorTest(unittest.TestCase):

    # Class Fields Begin
    __validator: DomainValidator = None
    # Class Fields End

    # Class Methods Begin
    def testGetArray_test0_decomposed(self) -> None:
        pass

    def testEnumIsPublic_test0_decomposed(self) -> None:
        pass

    def test_LOCAL_TLDS_sortedAndLowerCase_test1_decomposed(self) -> None:
        pass

    def test_LOCAL_TLDS_sortedAndLowerCase_test0_decomposed(self) -> None:
        pass

    def test_GENERIC_TLDS_sortedAndLowerCase_test1_decomposed(self) -> None:
        pass

    def test_GENERIC_TLDS_sortedAndLowerCase_test0_decomposed(self) -> None:
        pass

    def test_COUNTRY_CODE_TLDS_sortedAndLowerCase_test1_decomposed(self) -> None:
        pass

    def test_COUNTRY_CODE_TLDS_sortedAndLowerCase_test0_decomposed(self) -> None:
        pass

    def test_INFRASTRUCTURE_TLDS_sortedAndLowerCase_test1_decomposed(self) -> None:
        pass

    def test_INFRASTRUCTURE_TLDS_sortedAndLowerCase_test0_decomposed(self) -> None:
        pass

    def testIsIDNtoASCIIBroken_test2_decomposed(self) -> None:
        pass

    def testIsIDNtoASCIIBroken_test1_decomposed(self) -> None:
        pass

    def testIsIDNtoASCIIBroken_test0_decomposed(self) -> None:
        pass

    def testUnicodeToASCII_test1_decomposed(self) -> None:
        pass

    def testUnicodeToASCII_test0_decomposed(self) -> None:
        pass

    def testValidator306_test3_decomposed(self) -> None:
        pass

    def testValidator306_test2_decomposed(self) -> None:
        pass

    def testValidator306_test1_decomposed(self) -> None:
        pass

    def testValidator306_test0_decomposed(self) -> None:
        pass

    def testValidator297_test0_decomposed(self) -> None:
        pass

    def testDomainNoDots_test0_decomposed(self) -> None:
        pass

    def testRFC2396toplabel_test0_decomposed(self) -> None:
        pass

    def testRFC2396domainlabel_test0_decomposed(self) -> None:
        pass

    def testIDNJava6OrLater_test2_decomposed(self) -> None:
        pass

    def testIDNJava6OrLater_test1_decomposed(self) -> None:
        pass

    def testIDNJava6OrLater_test0_decomposed(self) -> None:
        pass

    def testIDN_test0_decomposed(self) -> None:
        pass

    def testAllowLocal_test2_decomposed(self) -> None:
        pass

    def testAllowLocal_test1_decomposed(self) -> None:
        pass

    def testAllowLocal_test0_decomposed(self) -> None:
        pass

    def testTopLevelDomains_test4_decomposed(self) -> None:
        pass

    def testTopLevelDomains_test3_decomposed(self) -> None:
        pass

    def testTopLevelDomains_test2_decomposed(self) -> None:
        pass

    def testTopLevelDomains_test1_decomposed(self) -> None:
        pass

    def testTopLevelDomains_test0_decomposed(self) -> None:
        pass

    def testInvalidDomains_test0_decomposed(self) -> None:
        pass

    def testValidDomains_test0_decomposed(self) -> None:
        pass

    def setUp(self) -> None:
        pass

    @staticmethod
    def main(a: typing.List[typing.List[str]]) -> None:
        pass

    @staticmethod
    def __isSortedLowerCase1(name: str, array: typing.List[typing.List[str]]) -> bool:
        pass

    @staticmethod
    def __isLowerCase(string: str) -> bool:
        pass

    @staticmethod
    def __isSortedLowerCase0(arrayName: str) -> bool:
        pass

    @staticmethod
    def __isInIanaList1(
        name: str, array: typing.List[typing.List[str]], ianaTlds: typing.Set[str]
    ) -> bool:
        pass

    @staticmethod
    def __isInIanaList0(arrayName: str, ianaTlds: typing.Set[str]) -> bool:
        pass

    @staticmethod
    def __closeQuietly(in_: Closeable) -> None:
        pass

    @staticmethod
    def __isNotInRootZone(domain: str) -> bool:
        pass

    @staticmethod
    def __download(f: pathlib.Path, tldurl: str, timestamp: int) -> int:
        pass

    @staticmethod
    def __getHtmlInfo(f: pathlib.Path) -> typing.Dict[str, typing.List[str]]:
        pass

    @staticmethod
    def __printMap(header: str, map_: typing.Dict[str, str], string: str) -> None:
        pass

    # Class Methods End
