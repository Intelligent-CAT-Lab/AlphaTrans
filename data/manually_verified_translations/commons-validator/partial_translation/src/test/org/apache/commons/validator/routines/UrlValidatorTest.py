from __future__ import annotations
import re
import unittest
import pytest
import pathlib
import io
import typing
from typing import *
import os
import unittest
from src.test.org.apache.commons.validator.ResultPair import *
from src.main.org.apache.commons.validator.routines.DomainValidator import *
from src.main.org.apache.commons.validator.routines.RegexValidator import *
from src.main.org.apache.commons.validator.routines.UrlValidator import *


class UrlValidatorTest(unittest.TestCase):

    __schemes: typing.List[str] = ["http", "gopher", "g0-To+.", "not_valid"]
    __printIndex: bool = False
    __printStatus: bool = False
    testScheme: List[ResultPair] = [
        ResultPair("http", True),
        ResultPair("ftp", False),
        ResultPair("httpd", False),
        ResultPair("gopher", True),
        ResultPair("g0-to+.", True),
        ResultPair("not_valid", False),  # underscore not allowed
        ResultPair("HtTp", True),
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
        ResultPair(":65535", True),  # max possible
        ResultPair(":65536", False),  # max possible +1
        ResultPair(":0", True),
        ResultPair("", True),
        ResultPair(":-1", False),
        ResultPair(":65636", False),
        ResultPair(":999999999999999999", False),
        ResultPair(":65a", False),
    ]
    testUrlAuthority: List[ResultPair] = [
        ResultPair("www.google.com", True),
        ResultPair("www.google.com.", True),
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
        ResultPair("go.a1a", False),
        ResultPair("go.cc", True),
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

    def testFragments(self) -> None:

        schemes = ["http", "https"]
        urlValidator = UrlValidator.UrlValidator3(schemes, UrlValidator.NO_FRAGMENTS)
        self.assertFalse(urlValidator.isValid("http://apache.org/a/b/c#frag"))
        urlValidator = UrlValidator.UrlValidator5(schemes)
        self.assertTrue(urlValidator.isValid("http://apache.org/a/b/c#frag"))

    def testValidator283(self) -> None:

        validator = UrlValidator.UrlValidator6()

        self.assertFalse(
            validator.isValid(
                "http://finance.yahoo.com/news/Owners-54B-NY-housing-apf-2493139299.html?x=0&ap=%fr"
            )
        )

        self.assertTrue(
            validator.isValid(
                "http://finance.yahoo.com/news/Owners-54B-NY-housing-apf-2493139299.html?x=0&ap=%22"
            )
        )

    def testValidator467(self) -> None:

        validator = UrlValidator.UrlValidator4(UrlValidator.ALLOW_2_SLASHES)

        self.assertTrue(validator.isValid("https://example.com/some_path/path/"))
        self.assertTrue(validator.isValid("https://example.com//somepath/path/"))
        self.assertTrue(validator.isValid("https://example.com//some_path/path/"))
        self.assertTrue(validator.isValid("http://example.com//_test"))

    def testValidator420(self) -> None:

        validator = UrlValidator.UrlValidator6()
        self.assertFalse(
            validator.isValid("http://example.com/serach?address=Main Avenue")
        )
        self.assertTrue(
            validator.isValid("http://example.com/serach?address=Main%20Avenue")
        )
        self.assertTrue(
            validator.isValid("http://example.com/serach?address=Main+Avenue")
        )

    def testValidator380(self) -> None:

        validator = UrlValidator.UrlValidator6()
        self.assertTrue(validator.isValid("http://www.apache.org:80/path"))
        self.assertTrue(validator.isValid("http://www.apache.org:8/path"))
        self.assertTrue(validator.isValid("http://www.apache.org:/path"))

    def testValidator382(self) -> None:

        validator = UrlValidator.UrlValidator6()
        self.assertTrue(
            validator.isValid(
                "ftp://username:password@example.com:8042/over/there/index.dtb?type=animal&name=narwhal#nose"
            )
        )

    def testValidator353(self) -> None:

        validator = UrlValidator.UrlValidator6()

        self.assertTrue(validator.isValid("http://www.apache.org:80/path"))
        self.assertTrue(validator.isValid("http://user:pass@www.apache.org:80/path"))
        self.assertTrue(validator.isValid("http://user:@www.apache.org:80/path"))
        self.assertTrue(validator.isValid("http://user@www.apache.org:80/path"))
        self.assertTrue(
            validator.isValid("http://us%00er:-._~w@www.apache.org:80/path")
        )
        self.assertFalse(validator.isValid("http://:pass@www.apache.org:80/path"))
        self.assertFalse(validator.isValid("http://:@www.apache.org:80/path"))
        self.assertFalse(validator.isValid("http://user:pa:ss@www.apache.org/path"))
        self.assertFalse(validator.isValid("http://user:pa@ss@www.apache.org/path"))

    def testValidator375(self) -> None:

        validator = UrlValidator.UrlValidator6()
        url = "http://[FEDC:BA98:7654:3210:FEDC:BA98:7654:3210]:80/index.html"
        self.assertTrue(
            validator.isValid(url), "IPv6 address URL should validate: " + url
        )
        url = "http://[::1]:80/index.html"
        self.assertTrue(
            validator.isValid(url), "IPv6 address URL should validate: " + url
        )
        url = "http://FEDC:BA98:7654:3210:FEDC:BA98:7654:3210:80/index.html"
        self.assertFalse(
            validator.isValid(url),
            "IPv6 address without [] should not validate: " + url,
        )

    def testValidator363(self) -> None:

        urlValidator = UrlValidator.UrlValidator6()

        self.assertTrue(urlValidator.isValid("http://www.example.org/a/b/hello..world"))
        self.assertTrue(urlValidator.isValid("http://www.example.org/a/hello..world"))
        self.assertTrue(urlValidator.isValid("http://www.example.org/hello.world/"))
        self.assertTrue(urlValidator.isValid("http://www.example.org/hello..world/"))
        self.assertTrue(urlValidator.isValid("http://www.example.org/hello.world"))
        self.assertTrue(urlValidator.isValid("http://www.example.org/hello..world"))
        self.assertTrue(urlValidator.isValid("http://www.example.org/..world"))
        self.assertTrue(urlValidator.isValid("http://www.example.org/.../world"))
        self.assertFalse(urlValidator.isValid("http://www.example.org/../world"))
        self.assertFalse(urlValidator.isValid("http://www.example.org/.."))
        self.assertFalse(urlValidator.isValid("http://www.example.org/../"))
        self.assertFalse(urlValidator.isValid("http://www.example.org/./.."))
        self.assertFalse(urlValidator.isValid("http://www.example.org/././.."))
        self.assertTrue(urlValidator.isValid("http://www.example.org/..."))
        self.assertTrue(urlValidator.isValid("http://www.example.org/.../"))
        self.assertTrue(urlValidator.isValid("http://www.example.org/.../.."))

    def testValidator361(self) -> None:

        validator = UrlValidator.UrlValidator6()
        self.assertTrue(validator.isValid("http://hello.tokyo/"))

    def testValidator290(self) -> None:

        validator = UrlValidator.UrlValidator6()

        self.assertTrue(validator.isValid("http://xn--h1acbxfam.idn.icann.org/"))
        self.assertTrue(validator.isValid("http://test.xn--lgbbat1ad8j"))
        self.assertTrue(validator.isValid("http://test.xn--fiqs8s"))
        self.assertTrue(validator.isValid("http://test.xn--fiqz9s"))
        self.assertTrue(validator.isValid("http://test.xn--wgbh1c"))
        self.assertTrue(validator.isValid("http://test.xn--j6w193g"))
        self.assertTrue(validator.isValid("http://test.xn--h2brj9c"))
        self.assertTrue(validator.isValid("http://test.xn--mgbbh1a71e"))
        self.assertTrue(validator.isValid("http://test.xn--fpcrj9c3d"))
        self.assertTrue(validator.isValid("http://test.xn--gecrj9c"))
        self.assertTrue(validator.isValid("http://test.xn--s9brj9c"))
        self.assertTrue(validator.isValid("http://test.xn--xkc2dl3a5ee0h"))
        self.assertTrue(validator.isValid("http://test.xn--45brj9c"))
        self.assertTrue(validator.isValid("http://test.xn--mgba3a4f16a"))
        self.assertTrue(validator.isValid("http://test.xn--mgbayh7gpa"))
        self.assertTrue(validator.isValid("http://test.xn--mgbc0a9azcg"))
        self.assertTrue(validator.isValid("http://test.xn--ygbi2ammx"))
        self.assertTrue(validator.isValid("http://test.xn--wgbl6a"))
        self.assertTrue(validator.isValid("http://test.xn--p1ai"))
        self.assertTrue(validator.isValid("http://test.xn--mgberp4a5d4ar"))
        self.assertTrue(validator.isValid("http://test.xn--90a3ac"))
        self.assertTrue(validator.isValid("http://test.xn--yfro4i67o"))
        self.assertTrue(validator.isValid("http://test.xn--clchc0ea0b2g2a9gcd"))
        self.assertTrue(validator.isValid("http://test.xn--3e0b707e"))
        self.assertTrue(validator.isValid("http://test.xn--fzc2c9e2c"))
        self.assertTrue(validator.isValid("http://test.xn--xkc2al3hye2a"))
        self.assertTrue(validator.isValid("http://test.xn--ogbpf8fl"))
        self.assertTrue(validator.isValid("http://test.xn--kprw13d"))
        self.assertTrue(validator.isValid("http://test.xn--kpry57d"))
        self.assertTrue(validator.isValid("http://test.xn--o3cw4h"))
        self.assertTrue(validator.isValid("http://test.xn--pgbs0dh"))
        self.assertTrue(validator.isValid("http://test.xn--mgbaam7a8h"))

    def testValidateUrl(self) -> None:
        self.assertTrue(True)

    def testValidator473_3(self) -> None:

        items = []
        with pytest.raises(ValueError):
            UrlValidator(
                [],
                None,
                UrlValidator.ALLOW_LOCAL_URLS,
                DomainValidator.getInstance2(False, items),
            )

    def testValidator473_2(self) -> None:

        items = []
        with pytest.raises(ValueError):
            UrlValidator([], None, 0, DomainValidator.getInstance2(True, items))

    def testValidator473_1(self) -> None:

        with pytest.raises(ValueError):
            UrlValidator([], None, 0, None)

    def testValidator452(self) -> None:

        urlValidator = UrlValidator.UrlValidator6()
        self.assertTrue(
            urlValidator.isValid("http://[::FFFF:129.144.52.38]:80/index.html")
        )

    def testValidator464(self) -> None:

        schemes = ["file"]
        urlValidator = UrlValidator.UrlValidator5(schemes)
        fileNAK = "file://bad ^ domain.com/label/test"
        self.assertFalse(urlValidator.isValid(fileNAK))

    def testValidator411(self) -> None:

        urlValidator = UrlValidator.UrlValidator6()
        self.assertTrue(urlValidator.isValid("http://example.rocks:/"))
        self.assertTrue(urlValidator.isValid("http://example.rocks:0/"))
        self.assertTrue(urlValidator.isValid("http://example.rocks:65535/"))
        self.assertFalse(urlValidator.isValid("http://example.rocks:65536/"))
        self.assertFalse(urlValidator.isValid("http://example.rocks:100000/"))

    def testValidator342(self) -> None:

        urlValidator = UrlValidator.UrlValidator6()
        self.assertTrue(urlValidator.isValid("http://example.rocks/"))
        self.assertTrue(urlValidator.isValid("http://example.rocks"))

    def testValidator339IDN(self) -> None:

        urlValidator = UrlValidator.UrlValidator6()
        self.assertTrue(urlValidator.isValid("http://президент.рф/WORLD/?hpt=sitenav"))
        self.assertTrue(urlValidator.isValid("http://президент.рф./WORLD/?hpt=sitenav"))
        self.assertFalse(urlValidator.isValid("http://президент.рф..../"))
        self.assertFalse(urlValidator.isValid("http://президент.рф.../"))
        self.assertFalse(urlValidator.isValid("http://президент.рф../"))

    def testValidator339(self) -> None:

        urlValidator = UrlValidator.UrlValidator6()
        self.assertTrue(urlValidator.isValid("http://www.cnn.com/WORLD/?hpt=sitenav"))
        self.assertTrue(urlValidator.isValid("http://www.cnn.com./WORLD/?hpt=sitenav"))
        self.assertFalse(urlValidator.isValid("http://www.cnn.com../"))
        self.assertFalse(urlValidator.isValid("http://www.cnn.invalid/"))
        self.assertFalse(urlValidator.isValid("http://www.cnn.invalid./"))

    def testValidator309(self) -> None:

        urlValidator = UrlValidator.UrlValidator6()
        self.assertTrue(urlValidator.isValid("http://sample.ondemand.com/"))
        self.assertTrue(urlValidator.isValid("hTtP://sample.ondemand.CoM/"))
        self.assertTrue(urlValidator.isValid("httpS://SAMPLE.ONEMAND.COM/"))

        urlValidator = UrlValidator.UrlValidator5(["HTTP", "HTTPS"])
        self.assertTrue(urlValidator.isValid("http://sample.ondemand.com/"))
        self.assertTrue(urlValidator.isValid("hTtP://sample.ondemand.CoM/"))
        self.assertTrue(urlValidator.isValid("httpS://SAMPLE.ONEMAND.COM/"))

    def testValidator391FAILS(self) -> None:

        schemes = ["file"]
        urlValidator = UrlValidator.UrlValidator5(schemes)
        self.assertTrue(urlValidator.isValid("file:/C:/path/to/dir/"))

    def testValidator391OK(self) -> None:

        schemes = ["file"]
        urlValidator = UrlValidator.UrlValidator5(schemes)
        self.assertTrue(urlValidator.isValid("file:///C:/path/to/dir/"))

    def testValidator276(self) -> None:

        validator = UrlValidator.UrlValidator6()
        self.assertTrue(
            "http://apache.org/ should be allowed by default",
            validator.isValid("http://www.apache.org/test/index.html"),
        )
        self.assertFalse(
            "file:///c:/ shouldn't be allowed by default",
            validator.isValid("file:///C:/some.file"),
        )
        self.assertFalse(
            "file:///c:\\ shouldn't be allowed by default",
            validator.isValid("file:///C:\\some.file"),
        )
        self.assertFalse(
            "file:///etc/ shouldn't be allowed by default",
            validator.isValid("file:///etc/hosts"),
        )
        self.assertFalse(
            "file://localhost/etc/ shouldn't be allowed by default",
            validator.isValid("file://localhost/etc/hosts"),
        )
        self.assertFalse(
            "file://localhost/c:/ shouldn't be allowed by default",
            validator.isValid("file://localhost/c:/some.file"),
        )
        validator = UrlValidator.UrlValidator3(
            ["http", "file"], UrlValidator.ALLOW_LOCAL_URLS
        )
        self.assertTrue(
            "http://apache.org/ should be allowed by default",
            validator.isValid("http://www.apache.org/test/index.html"),
        )
        self.assertTrue(
            "file:///c:/ should now be allowed",
            validator.isValid("file:///C:/some.file"),
        )
        self.assertFalse(
            "file:///c:\\ should not be allowed",
            validator.isValid("file:///C:\\some.file"),
        )
        self.assertTrue(
            "file:///etc/ should now be allowed", validator.isValid("file:///etc/hosts")
        )
        self.assertTrue(
            "file://localhost/etc/ should now be allowed",
            validator.isValid("file://localhost/etc/hosts"),
        )
        self.assertTrue(
            "file://localhost/c:/ should now be allowed",
            validator.isValid("file://localhost/c:/some.file"),
        )
        self.assertFalse(
            "file://c:/ shouldn't ever be allowed, needs file:///c:/",
            validator.isValid("file://C:/some.file"),
        )
        self.assertFalse(
            "file://c:\\ shouldn't ever be allowed, needs file:///c:/",
            validator.isValid("file://C:\\some.file"),
        )

    def testValidator288(self) -> None:

        validator = UrlValidator.UrlValidator4(UrlValidator.ALLOW_LOCAL_URLS)
        self.assertTrue(validator.isValid("http://hostname"))
        self.assertTrue(validator.isValid("http://hostname/test/index.html"))
        self.assertTrue(validator.isValid("http://localhost/test/index.html"))
        self.assertFalse(validator.isValid("http://first.my-testing/test/index.html"))
        self.assertFalse(validator.isValid("http://broke.hostname/test/index.html"))
        self.assertTrue(validator.isValid("http://www.apache.org/test/index.html"))

        validator = UrlValidator.UrlValidator4(0)
        self.assertFalse(validator.isValid("http://hostname"))
        self.assertFalse(validator.isValid("http://localhost/test/index.html"))
        self.assertTrue(validator.isValid("http://www.apache.org/test/index.html"))

    def testValidator248(self) -> None:

        regex = RegexValidator.RegexValidator1(["localhost", ".*\\.my-testing"])
        validator = UrlValidator.UrlValidator2(regex, 0)
        self.assertTrue(validator.isValid("http://localhost/test/index.html"))
        self.assertTrue(validator.isValid("http://first.my-testing/test/index.html"))
        self.assertTrue(validator.isValid("http://sup3r.my-testing/test/index.html"))
        self.assertFalse(validator.isValid("http://broke.my-test/test/index.html"))
        self.assertTrue(validator.isValid("http://www.apache.org/test/index.html"))
        validator = UrlValidator.UrlValidator4(UrlValidator.ALLOW_LOCAL_URLS)
        self.assertTrue(validator.isValid("http://localhost/test/index.html"))
        self.assertTrue(validator.isValid("http://machinename/test/index.html"))
        self.assertTrue(validator.isValid("http://www.apache.org/test/index.html"))

    def testValidator235(self) -> None:

        version = platform.python_version()
        if version.split(".")[1] < "6":
            print("Cannot run Unicode IDN tests")
            return  # Cannot run the test

        validator = UrlValidator.UrlValidator6()
        self.assertTrue(
            validator.isValid("http://xn--d1abbgf6aiiy.xn--p1ai"),
            "xn--d1abbgf6aiiy.xn--p1ai should validate",
        )
        self.assertTrue(
            validator.isValid("http://президент.рф"), "президент.рф should validate"
        )
        self.assertTrue(
            validator.isValid("http://www.b\u00fccher.ch"),
            "www.b\u00fccher.ch should validate",
        )
        self.assertFalse(
            validator.isValid("http://www.\uFFFD.ch"), "www.\uFFFD.ch FFFD should fail"
        )
        self.assertTrue(
            validator.isValid("ftp://www.b\u00fccher.ch"),
            "www.b\u00fccher.ch should validate",
        )
        self.assertFalse(
            validator.isValid("ftp://www.\uFFFD.ch"), "www.\uFFFD.ch FFFD should fail"
        )

    def testValidator218(self) -> None:

        validator = UrlValidator.UrlValidator4(UrlValidator.ALLOW_2_SLASHES)
        self.assertTrue(
            validator.isValid("http://somewhere.com/pathxyz/file(1).html"),
            "parentheses should be valid in URLs",
        )

    def testValidator204(self) -> None:

        schemes = ["http", "https"]
        urlValidator = UrlValidator.UrlValidator5(schemes)
        self.assertTrue(
            urlValidator.isValid(
                "http://tech.yahoo.com/rc/desktops/102;_ylt=Ao8yevQHlZ4On0O3ZJGXLEQFLZA5"
            )
        )

    def testValidator202(self) -> None:

        schemes = ["http", "https"]
        urlValidator = UrlValidator.UrlValidator3(schemes, UrlValidator.NO_FRAGMENTS)
        self.assertTrue(
            urlValidator.isValid(
                "http://l.l.l.l.l.l.l.l.l.l.l.l.l.l.l.l.l.l.l.l.l.l.l.l.l.l.l.l.l.l.l.l.l.l.l.l.l.l.l.l.l.l.l.l.l.l.l.l.l.l.l.l.l.l.l.l.l.l.l.org"
            )
        )

    def testIsValidScheme(self) -> None:

        if self.__printStatus:
            print("\n testIsValidScheme() ")

        urlVal = UrlValidator.UrlValidator3(self.__schemes, 0)

        for testPair in self.testScheme:
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

        self.testIsValid1(self.testUrlParts, UrlValidator.ALLOW_ALL_SCHEMES)
        self.setUp()
        options = (
            UrlValidator.ALLOW_2_SLASHES
            + UrlValidator.ALLOW_ALL_SCHEMES
            + UrlValidator.NO_FRAGMENTS
        )
        self.testIsValid1(self.testUrlPartsOptions, options)

    def setUp(self) -> None:
        for index in range(len(self.testPartsIndex) - 1):
            self.testPartsIndex[index] = 0

    @staticmethod
    def main(args: typing.List[typing.List[str]]) -> None:

        uv = UrlValidator.UrlValidator6()
        for arg in args:
            try:
                uri = urlparse(arg)
                uri = uri._replace(scheme=uri.scheme.lower(), netloc=uri.netloc.lower())
                print(uri.geturl())
                print("URI scheme: %s" % uri.scheme)
                print("URI scheme specific part: %s" % uri.netloc)
                print("URI raw scheme specific part: %s" % uri.netloc)
                print("URI auth: %s" % uri.netloc)
                print("URI raw auth: %s" % uri.netloc)
                print("URI userInfo: %s" % uri.username)
                print("URI raw userInfo: %s" % uri.username)
                print("URI host: %s" % uri.hostname)
                print("URI port: %s" % uri.port)
                print("URI path: %s" % uri.path)
                print("URI raw path: %s" % uri.path)
                print("URI query: %s" % uri.query)
                print("URI raw query: %s" % uri.query)
                print("URI fragment: %s" % uri.fragment)
                print("URI raw fragment: %s" % uri.fragment)
            except ValueError as e:
                print(e)
            print("isValid: %s" % uv.isValid(arg))

    @staticmethod
    def incrementTestPartsIndex(
        testPartsIndex: typing.List[int], testParts: typing.List[typing.Any]
    ) -> bool:

        carry = True  # add 1 to lowest order part.
        maxIndex = True
        for testPartsIndexIndex in range(len(testPartsIndex) - 1, -1, -1):
            index = testPartsIndex[testPartsIndexIndex]
            part = testParts[testPartsIndexIndex]
            maxIndex &= index == (len(part) - 1)
            if carry:
                if index < len(part) - 1:
                    index += 1
                    testPartsIndex[testPartsIndexIndex] = index
                    carry = False
                else:
                    testPartsIndex[testPartsIndexIndex] = 0
                    carry = True

        return not maxIndex

    def testIsValid1(self, testObjects: typing.List[typing.Any], options: int) -> None:

        urlVal = UrlValidator.UrlValidator1(None, None, options)
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

    def __testPartsIndextoString(self) -> str:

        carryMsg = "{"
        for testPartsIndexIndex in range(len(self.testPartsIndex)):
            carryMsg += str(self.testPartsIndex[testPartsIndexIndex])
            if testPartsIndexIndex < len(self.testPartsIndex) - 1:
                carryMsg += ","
            else:
                carryMsg += "}"
        return carryMsg
