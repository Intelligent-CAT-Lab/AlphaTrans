import pytest

from src.main.org.apache.commons.validator.UrlValidator import *
from src.test.org.apache.commons.validator.ResultPair import ResultPair
import unittest

class UrlTest(unittest.TestCase):

    __printStatus = False
    __printIndex = False

    testUrlScheme = [
        ResultPair("http://", True),
        ResultPair("ftp://", True),
        ResultPair("h3t://", True),
        ResultPair("3ht://", False),
        ResultPair("http:/", False),
        ResultPair("http:", False),
        ResultPair("http/", False),
        ResultPair("://", False),
        ResultPair("", True)
    ]
    testUrlAuthority = [
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
        ResultPair("", False)
    ]
    testUrlPort = [
        ResultPair(":80", True),
        ResultPair(":65535", True),
        ResultPair(":0", True),
        ResultPair("", True),
        ResultPair(":-1", False),
        ResultPair(":65636", True),
        ResultPair(":65a", False)
    ]
    testPath = [
        ResultPair("/test1", True),
        ResultPair("/t123", True),
        ResultPair("/$23", True),
        ResultPair("/..", False),
        ResultPair("/../", False),
        ResultPair("/test1/", True),
        ResultPair("", True),
        ResultPair("/test1/file", True),
        ResultPair("/..//file", False),
        ResultPair("/test1//file", False)
    ]
    testUrlPathOptions = [
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
        ResultPair("/#/file", False)
    ]

    testUrlQuery = [
        ResultPair("?action=view", True),
        ResultPair("?action=edit&mode=up", True),
        ResultPair("", True)
    ]

    testUrlParts = [
        testUrlScheme,
        testUrlAuthority,
        testUrlPort,
        testPath,
        testUrlQuery
    ]
    testUrlPartsOptions = [
        testUrlScheme,
        testUrlAuthority,
        testUrlPort,
        testUrlPathOptions,
        testUrlQuery
    ]
    testPartsIndex = [0, 0, 0, 0, 0]

    testScheme = [
        ResultPair("http", True),
        ResultPair("ftp", False),
        ResultPair("httpd", False),
        ResultPair("telnet", False)
    ]
    

    def setUp(self) -> None:
        super().setUp()
        for index in range(len(self.testPartsIndex) - 1):
            self.testPartsIndex[index] = 0

    
    @pytest.mark.test
    def testIsValid0(self) -> None:
        self.checkTestIsValid1(self.testUrlParts, UrlValidator.ALLOW_ALL_SCHEMES)
        self.setUp()
        options = UrlValidator.ALLOW_2_SLASHES +\
            UrlValidator.ALLOW_ALL_SCHEMES +\
            UrlValidator.NO_FRAGMENTS
        self.checkTestIsValid1(self.testUrlPartsOptions, options)
    

    @pytest.mark.test
    def testIsValidScheme(self) -> None:
        if self.__printStatus:
            print("\n testIsValidScheme() ")
        schemes = ["http", "gopher"]
        urlVal = UrlValidator(schemes, 0)
        for sIndex in range(len(self.testScheme)):
            testPair = self.testScheme[sIndex]
            result = urlVal.isValidScheme(testPair.item)
            self.assertEqual(
                testPair.valid,
                result,
                testPair.item
            )
            if self.__printStatus:
                if result == testPair.valid:
                    print('.', end='')
                else:
                    print('X', end='')
        if self.__printStatus:
            print()
    

    @pytest.mark.test
    def testValidator202(self) -> None:
        schemes = ["http", "https"]
        urlValidator = UrlValidator(schemes, UrlValidator.NO_FRAGMENTS)
        urlValidator.isValid(
            "http://www.logoworks.comwww.logoworks.comwww.logoworks.comwww.logoworks." +\
                "comwww.logoworks.comwww.logoworks.comwww.logoworks.comwww.logoworks." +\
                "comwww.logoworks.comwww.logoworks.comwww.logoworks.comwww.logoworks." +\
                "comwww.logoworks.comwww.logoworks.comwww.logoworks.comwww.logoworks." +\
                "comwww.logoworks.comwww.logoworks.comwww.logoworks.comwww.logoworks." +\
                "comwww.logoworks.comwww.logoworks.comwww.logoworks.comwww.logoworks." +\
                "comwww.logoworks.comwww.logoworks.comwww.logoworks.comwww.logoworks." +\
                "comwww.logoworks.comwww.log"
        )


    @pytest.mark.test
    def testValidator204(self) -> None:
        schemes = ["http", "https"]
        urlValidator = UrlValidator.UrlValidator2(schemes)
        self.assertTrue(
            urlValidator.isValid(
                "http://tech.yahoo.com/rc/desktops/102;_ylt=Ao8yevQHlZ4On0O3ZJGXLEQFLZA5"
            )
        )
    

    @pytest.mark.test
    def testValidateUrl(self) -> None:
        self.assertTrue(True)
    

    @staticmethod
    def main(argv) -> None:
        fct = UrlTest()
        fct.setUp()
        fct.testIsValid0()
        fct.testIsValidScheme()


    def checkTestIsValid1(self, testObjects, options) -> None:
        urlVal = UrlValidator.UrlValidator1(None, None, options)
        self.assertTrue(urlVal.isValid("http://www.google.com"))
        self.assertTrue(urlVal.isValid("http://www.google.com/"))
        statusPerLine = 60
        printed = 0
        if self.__printIndex:
            statusPerLine = 6
        while True:
            testBuffer = []
            expected = True
            for testPartsIndexIndex in range(len(self.testPartsIndex)):
                index = self.testPartsIndex[testPartsIndexIndex]
                part = testObjects[testPartsIndexIndex]
                testBuffer.append(part[index].item)
                expected = (expected and part[index].valid)
            url = ''.join(testBuffer)
            result = urlVal.isValid(url)
            self.assertEqual(
                expected,
                result,
                url
            )
            if self.__printStatus:
                if self.__printIndex:
                    print(self.__testPartsIndextoString(), end='')
                else:
                    if result == expected:
                        print('.', end='')
                    else:
                        print('X', end='')
                printed += 1
                if printed == statusPerLine:
                    print()
                    printed = 0
            if not UrlTest.incrementTestPartsIndex(self.testPartsIndex, testObjects):
                break
        if self.__printStatus:
            print()
    

    @staticmethod
    def incrementTestPartsIndex(testPartsIndex, testParts) -> bool:
        carry = True
        maxIndex = True
        for testPartsIndexIndex in range(len(testPartsIndex) - 1, -1, -1):
            index = testPartsIndex[testPartsIndexIndex]
            part = testParts[testPartsIndexIndex]
            if carry:
                if index < len(part) - 1:
                    index += 1
                    testPartsIndex[testPartsIndexIndex] = index
                    carry = False
                else:
                    testPartsIndex[testPartsIndexIndex] = 0
                    carry = True
            maxIndex = (maxIndex and (index == (len(part) - 1)))
        
        return not maxIndex


    def __testPartsIndextoString(self) -> str:
        carryMsg = ['{']
        for testPartsIndexIndex in range(len(self.testPartsIndex)):
            carryMsg.append(str(self.testPartsIndex[testPartsIndexIndex]))
            if testPartsIndexIndex < len(self.testPartsIndex) - 1:
                carryMsg.append(',')
            else:
                carryMsg.append('}')
        return ''.join(carryMsg)
        
