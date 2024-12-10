from __future__ import annotations
import re
import unittest
import pytest
import pathlib
import io
import typing
from typing import *
import unittest
from src.test.org.apache.commons.validator.ResultPair import *
from src.main.org.apache.commons.validator.UrlValidator import *


class UrlTest(unittest.TestCase):

    __printIndex: bool = False
    __printStatus: bool = False
    testScheme: List[ResultPair] = [
        ResultPair("http", True),
        ResultPair("ftp", False),
        ResultPair("httpd", False),
        ResultPair("telnet", False),
    ]
    testPartsIndex: List[int] = [0, 0, 0, 0, 0]
    testUrlQuery: List[ResultPair] = [
        ResultPair("?action=view", True),
        ResultPair("?action=edit&mode=up", True),
        ResultPair("", True),
    ]
    testUrlPathOptions: List[ResultPair] = [
        ResultPair("/test1", True),
        ResultPair("/t123", True),
        ResultPair("/$23", True),
        ResultPair("/..", False),
        ResultPair("/../", False),
        ResultPair("/test1/", True),
        ResultPair("/#", False),
        ResultPair("", True),
        ResultPair("/test1/file", True),
        ResultPair("/t123/file", True),
        ResultPair("/$23/file", True),
        ResultPair("/../file", False),
        ResultPair("/..//file", False),
        ResultPair("/test1//file", True),
        ResultPair("/#/file", False),
    ]
    testPath: List[ResultPair] = [
        ResultPair("/test1", True),
        ResultPair("/t123", True),
        ResultPair("/$23", True),
        ResultPair("/..", False),
        ResultPair("/../", False),
        ResultPair("/test1/", True),
        ResultPair("", True),
        ResultPair("/test1/file", True),
        ResultPair("/..//file", False),
        ResultPair("/test1//file", False),
    ]
    testUrlPort: List[ResultPair] = [
        ResultPair(":80", True),
        ResultPair(":65535", True),
        ResultPair(":0", True),
        ResultPair("", True),
        ResultPair(":-1", False),
        ResultPair(":65636", True),
        ResultPair(":65a", False),
    ]
    testUrlAuthority: List[ResultPair] = [
        ResultPair("www.google.com", True),
        ResultPair("go.com", True),
        ResultPair("go.au", True),
        ResultPair("0.0.0.0", True),
        ResultPair("255.255.255.255", True),
        ResultPair("256.256.256.256", False),
        ResultPair("255.com", True),
        ResultPair("1.2.3.4.5", False),
        ResultPair("1.2.3.4.", False),
        ResultPair("1.2.3", False),
        ResultPair(".1.2.3.4", False),
        ResultPair("go.a", False),
        ResultPair("go.a1a", True),
        ResultPair("go.1aa", False),
        ResultPair("aaa.", False),
        ResultPair(".aaa", False),
        ResultPair("aaa", False),
        ResultPair("", False),
    ]
    testUrlScheme: List[ResultPair] = [
        ResultPair("http://", True),
        ResultPair("ftp://", True),
        ResultPair("h3t://", True),
        ResultPair("3ht://", False),
        ResultPair("http:/", False),
        ResultPair("http:", False),
        ResultPair("http/", False),
        ResultPair("://", False),
        ResultPair("", True),
    ]
    testUrlPartsOptions: typing.List[typing.Any] = [
        testUrlScheme,
        testUrlAuthority,
        testUrlPort,
        testUrlPathOptions,
        testUrlQuery,
    ]
    testUrlParts: List[
        Union[
            List[ResultPair],
            List[ResultPair],
            List[ResultPair],
            List[ResultPair],
            List[ResultPair],
        ]
    ] = [testUrlScheme, testUrlAuthority, testUrlPort, testPath, testUrlQuery]

    def setUp(self) -> None:
        for index in range(len(self.testPartsIndex) - 1):
            self.testPartsIndex[index] = 0

    @staticmethod
    def main(argv: typing.List[typing.List[str]]) -> None:

        fct = UrlTest("url test")
        fct.setUp()
        fct.testIsValid0()
        fct.testIsValidScheme()

    def testValidateUrl(self) -> None:
        self.assertTrue(True)

    @staticmethod
    def incrementTestPartsIndex(
        testPartsIndex: typing.List[int], testParts: typing.List[typing.Any]
    ) -> bool:

        carry = True  # add 1 to lowest order part.
        maxIndex = True
        for testPartsIndexIndex in range(len(testPartsIndex) - 1, -1, -1):
            index = testPartsIndex[testPartsIndexIndex]
            part = typing.cast(typing.List[ResultPair], testParts[testPartsIndexIndex])
            if carry:
                if index < len(part) - 1:
                    index += 1
                    testPartsIndex[testPartsIndexIndex] = index
                    carry = False
                else:
                    testPartsIndex[testPartsIndexIndex] = 0
                    carry = True
            maxIndex &= index == (len(part) - 1)

        return not maxIndex

    def testValidator204(self) -> None:

        schemes = ["http", "https"]
        urlValidator = UrlValidator.UrlValidator2(schemes)
        self.assertTrue(
            urlValidator.isValid(
                "http://tech.yahoo.com/rc/desktops/102;_ylt=Ao8yevQHlZ4On0O3ZJGXLEQFLZA5"
            )
        )

    def testValidator202(self) -> None:

        schemes = ["http", "https"]
        urlValidator = UrlValidator(schemes, UrlValidator.NO_FRAGMENTS)
        urlValidator.isValid(
            "http://www.logoworks.comwww.logoworks.comwww.logoworks.comwww.logoworks.comwww.logoworks.comwww.logoworks.comwww.logoworks.comwww.logoworks.comwww.logoworks.comwww.logoworks.comwww.logoworks.comwww.logoworks.comwww.logoworks.comwww.logoworks.comwww.logoworks.comwww.logoworks.comwww.logoworks.comwww.logoworks.comwww.logoworks.comwww.logoworks.comwww.logoworks.comwww.logoworks.comwww.logoworks.comwww.logoworks.comwww.log"
        )

    def _testIsValid1(self, testObjects: typing.List[typing.Any], options: int) -> None:

        urlVal = UrlValidator(None, options)
        self.assertTrue(urlVal.isValid("http://www.google.com"))
        self.assertTrue(urlVal.isValid("http://www.google.com/"))
        statusPerLine = 60
        printed = 0
        if self.__printIndex:
            statusPerLine = 6
        while self.incrementTestPartsIndex(self.testPartsIndex, testObjects):
            testBuffer = ""
            expected = True
            for testPartsIndexIndex in range(len(self.testPartsIndex)):
                index = self.testPartsIndex[testPartsIndexIndex]
                part = testObjects[testPartsIndexIndex]
                testBuffer += part[index].item
                expected &= part[index].valid
            url = testBuffer
            result = urlVal.isValid(url)
            self.assertEqual(expected, result, url)
            if self.__printStatus:
                if self.__printIndex:
                    print(self.__testPartsIndextoString())
                else:
                    if result == expected:
                        print(".", end="")
                    else:
                        print("X", end="")
                printed += 1
                if printed == statusPerLine:
                    print()
                    printed = 0
        if self.__printStatus:
            print()

    def testIsValidScheme(self) -> None:

        if self.__printStatus:
            print("\n testIsValidScheme() ")

        schemes = ["http", "gopher"]
        urlVal = UrlValidator(schemes, 0)

        for sIndex in range(len(self.testScheme)):
            testPair = self.testScheme[sIndex]
            result = urlVal._isValidScheme(testPair.item)
            self.assertEqual(testPair.valid, result)

            if self.__printStatus:
                if result == testPair.valid:
                    print(".", end="")
                else:
                    print("X", end="")

        if self.__printStatus:
            print()

    def testIsValid0(self) -> None:

        self._testIsValid1(self.testUrlParts, UrlValidator.ALLOW_ALL_SCHEMES)
        self.setUp()
        options = (
            UrlValidator.ALLOW_2_SLASHES
            + UrlValidator.ALLOW_ALL_SCHEMES
            + UrlValidator.NO_FRAGMENTS
        )

        self._testIsValid1(self.testUrlPartsOptions, options)

    def __init__(self, testName: str) -> None:
        super().__init__(testName)

    def __testPartsIndextoString(self) -> str:

        carryMsg = "{"
        for testPartsIndexIndex in range(len(self.testPartsIndex)):
            carryMsg += str(self.testPartsIndex[testPartsIndexIndex])
            if testPartsIndexIndex < len(self.testPartsIndex) - 1:
                carryMsg += ","
            else:
                carryMsg += "}"
        return carryMsg
