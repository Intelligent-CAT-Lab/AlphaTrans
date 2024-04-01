# Imports Begin
from src.main.org.apache.commons.validator.UrlValidator import *
from src.main.org.apache.commons.validator.ResultPair import *
import unittest
import typing
from typing import *

# Imports End


class UrlTest(unittest.TestCase, TestCase):

    # Class Fields Begin
    __printStatus: bool = ""  # LLM could not translate field
    __printIndex: bool = ""  # LLM could not translate field
    # Class Fields End

    # Class Methods Begin
    def _setUp(self) -> None:

        for index in range(len(self.testPartsIndex) - 1):
            self.testPartsIndex[index] = 0

    @staticmethod
    def main(argv: typing.List[str]) -> None:

        pass  # LLM could not translate method body

    def testValidateUrl(self) -> None:

        self.assertTrue(True)

    @staticmethod
    def incrementTestPartsIndex(
        testPartsIndex: typing.List[int], testParts: typing.List[typing.Any]
    ) -> bool:

        pass  # LLM could not translate method body

    def testValidator204(self) -> None:

        schemes = ["http", "https"]
        urlValidator = UrlValidator.UrlValidator2(schemes)
        self.assertTrue(
            urlValidator.isValid(
                "http://tech.yahoo.com/rc/desktops/102;_ylt=Ao8yevQHlZ4On0O3ZJGXLEQFLZA5"
            )
        )

    def testValidator202(self) -> None:

        pass  # LLM could not translate method body

    def testIsValid1(self, testObjects: typing.List[typing.Any], options: int) -> None:

        urlVal = UrlValidator(None, options)
        self.assertTrue(urlVal.isValid("http://www.google.com"))
        self.assertTrue(urlVal.isValid("http://www.google.com/"))
        statusPerLine = 60
        printed = 0
        if self.__printIndex:
            statusPerLine = 6
        while self.incrementTestPartsIndex(testPartsIndex, testObjects):
            testBuffer = StringBuilder()
            expected = True
            for testPartsIndexIndex in range(len(testPartsIndex)):
                index = testPartsIndex[testPartsIndexIndex]
                part = testObjects[testPartsIndexIndex]
                testBuffer.append(part[index].item)
                expected &= part[index].valid
            url = testBuffer.toString()
            result = urlVal.isValid(url)
            self.assertEqual(url, expected, result)
            if self.__printStatus:
                if self.__printIndex:
                    print(self.__testPartsIndextoString())
                else:
                    if result == expected:
                        print(".")
                    else:
                        print("X")
                printed += 1
                if printed == statusPerLine:
                    print()
                    printed = 0
        if self.__printStatus:
            print()

    def testIsValidScheme(self) -> None:

        if self.__printStatus:
            print("\n testIsValidScheme() ", end="")
        schemes = ["http", "gopher"]
        urlVal = UrlValidator(schemes, 0)
        for sIndex in range(len(testScheme)):
            testPair = testScheme[sIndex]
            result = urlVal.isValidScheme(testPair.item)
            assert result == testPair.valid
            if self.__printStatus:
                if result == testPair.valid:
                    print(".", end="")
                else:
                    print("X", end="")
        if self.__printStatus:
            print()

    def testIsValid0(self) -> None:

        self.testIsValid1(testUrlParts, UrlValidator.ALLOW_ALL_SCHEMES)
        self._setUp()
        options = (
            UrlValidator.ALLOW_2_SLASHES
            + UrlValidator.ALLOW_ALL_SCHEMES
            + UrlValidator.NO_FRAGMENTS
        )
        self.testIsValid1(testUrlPartsOptions, options)

    def __init__(self, testName: str) -> None:

        super().__init__(testName)

    def __testPartsIndextoString(self) -> str:

        carry_msg = "{"
        for test_parts_index_index in range(len(self.test_parts_index)):
            carry_msg += str(self.test_parts_index[test_parts_index_index])
            if test_parts_index_index < len(self.test_parts_index) - 1:
                carry_msg += ","
            else:
                carry_msg += "}"
        return carry_msg

    # Class Methods End
