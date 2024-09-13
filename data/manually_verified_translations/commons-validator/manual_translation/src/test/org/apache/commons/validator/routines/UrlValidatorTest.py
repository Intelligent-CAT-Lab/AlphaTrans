import pytest

from src.main.org.apache.commons.validator.routines.UrlValidator import *
from src.main.org.apache.commons.validator.routines.RegexValidator import *
from src.main.org.apache.commons.validator.routines.DomainValidator import *
from src.test.org.apache.commons.validator.ResultPair import ResultPair
import unittest
from urllib.parse import urlparse
from urllib.error import URLError
import sys

class UrlValidatorTest(unittest.TestCase):

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
        ResultPair("://", False)
    ]

    testUrlAuthority = [
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
        ResultPair("", False)
    ]
    testUrlPort = [
        ResultPair(":80", True),
        ResultPair(":65535", True),
        ResultPair(":65536", False),
        ResultPair(":0", True),
        ResultPair("", True),
        ResultPair(":-1", False),
        ResultPair(":65636", False),
        ResultPair(":999999999999999999", False),
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

    __schemes = ["http", "gopher", "g0-To+.", "not_valid"]

    testScheme = [
        ResultPair("http", True),
        ResultPair("ftp", False),
        ResultPair("httpd", False),
        ResultPair("gopher", True),
        ResultPair("g0-to+.", True),
        ResultPair("not_valid", False),
        ResultPair("HtTp", True),
        ResultPair("telnet", False)
    ]

    
    def setUp(self) -> None:
        super().setUp()
        for index in range(len(self.testPartsIndex) - 1):
            self.testPartsIndex[index] = 0

    
    
    def testIsValid0(self) -> None:
        self.checkTestIsValid1(self.testUrlParts, UrlValidator.ALLOW_ALL_SCHEMES)
        self.setUp()
        options = UrlValidator.ALLOW_2_SLASHES +\
            UrlValidator.ALLOW_ALL_SCHEMES +\
            UrlValidator.NO_FRAGMENTS
        self.checkTestIsValid1(self.testUrlPartsOptions, options)

    
    
    def testIsValidScheme(self) -> None:
        if self.__printStatus:
            print("\n testIsValidScheme() ")
        urlVal = UrlValidator.UrlValidator3(self.__schemes, 0)
        for sIndex in range(len(self.testScheme)):
            testPair = self.testScheme[sIndex]
            result = urlVal._isValidScheme(testPair.item)
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
    

    
    def testValidator202(self) -> None:
        schemes = ["http", "https"]
        urlValidator = UrlValidator.UrlValidator3(schemes, UrlValidator.NO_FRAGMENTS)
        self.assertTrue(
            urlValidator.isValid(
                "http://l.l.l.l.l.l.l.l.l.l.l.l.l.l.l.l.l.l.l.l.l.l" +\
                    ".l.l.l.l.l.l.l.l.l.l.l.l.l.l.l.l.l.l.l.l.l.l.l" +\
                    ".l.l.l.l.l.l.l.l.l.l.l.l.l.l.l.l.org"
            )
        )

    
    
    def testValidator204(self) -> None:
        schemes = ["http", "https"]
        urlValidator = UrlValidator.UrlValidator5(schemes)
        self.assertTrue(
            urlValidator.isValid(
                "http://tech.yahoo.com/rc/desktops/102;_ylt=Ao8yevQHlZ4On0O3ZJGXLEQFLZA5"
            )
        )

    
    
    def testValidator218(self) -> None:
        validator = UrlValidator.UrlValidator4(UrlValidator.ALLOW_2_SLASHES)
        self.assertTrue(
            validator.isValid("http://somewhere.com/pathxyz/file(1).html"),
            "parentheses should be valid in URLs"
        )

    
    
    def testValidator235(self) -> None:
        version = sys.version_info
        if version < (2, 6): 
            #Python 2.6 is the latest version available at the birth of Java 1.6
            print("Cannot run Unicode IDN tests")
            return
        
        validator = UrlValidator.UrlValidator6()
        self.assertTrue(
            validator.isValid("http://xn--d1abbgf6aiiy.xn--p1ai"),
            "xn--d1abbgf6aiiy.xn--p1ai should validate"
        )
        self.assertTrue(
            validator.isValid("http://президент.рф"),
            "президент.рф should validate"
        )
        self.assertTrue(
            validator.isValid("http://www.bücher.ch"),
            "www.bücher.ch should validate"
        )
        self.assertFalse(
            validator.isValid("http://www.\uFFFD.ch"),
            "www.\uFFFD.ch FFFD should fail"
        )
        self.assertTrue(
            validator.isValid("ftp://www.bücher.ch"),
            "www.bücher.ch should validate"
        )
        self.assertFalse(
            validator.isValid("ftp://www.\uFFFD.ch"),
            "www.\uFFFD.ch FFFD should fail"
        )

    
    
    def testValidator248(self) -> None:
        regex = RegexValidator.RegexValidator1(["localhost", ".*\\.my-testing"])
        validator = UrlValidator.UrlValidator2(regex, 0)

        self.assertTrue(
            validator.isValid("http://localhost/test/index.html"),
            "localhost URL should validate"
        )
        self.assertTrue(
            validator.isValid("http://first.my-testing/test/index.html"),
            "first.my-testing should validate"
        )
        self.assertTrue(
            validator.isValid("http://sup3r.my-testing/test/index.html"),
            "sup3r.my-testing should validate"
        )

        self.assertFalse(
            validator.isValid("http://broke.my-test/test/index.html"),
            "broke.my-test should not validate"
        )
        self.assertTrue(
            validator.isValid("http://www.apache.org/test/index.html"),
            "www.apache.org should still validate"
        )

        validator = UrlValidator.UrlValidator4(UrlValidator.ALLOW_LOCAL_URLS)

        self.assertTrue(
            validator.isValid("http://localhost/test/index.html"),
            "localhost URL should validate"
        )
        self.assertTrue(
            validator.isValid("http://machinename/test/index.html"),
            "machinename URL should validate"
        )
        self.assertTrue(
            validator.isValid("http://www.apache.org/test/index.html"),
            "www.apache.org should still validate"
        )

    
    
    def testValidator288(self) -> None:
        validator = UrlValidator.UrlValidator4(UrlValidator.ALLOW_LOCAL_URLS)

        self.assertTrue(
            validator.isValid("http://hostname"),
            "hostname should validate"
        )

        self.assertTrue(
            validator.isValid("http://hostname/test/index.html"),
            "hostname with path should validate"
        )

        self.assertTrue(
            validator.isValid("http://localhost/test/index.html"),
            "localhost URL should validate"
        )

        self.assertFalse(
            validator.isValid("http://first.my-testing/test/index.html"),
            "first.my-testing should not validate"
        )

        self.assertFalse(
            validator.isValid("http://broke.hostname/test/index.html"),
            "broke.hostname should not validate"
        )

        self.assertTrue(
            validator.isValid("http://www.apache.org/test/index.html"),
            "www.apache.org should still validate"
        )

        validator = UrlValidator.UrlValidator4(0)

        self.assertFalse(
            validator.isValid("http://hostname"),
            "hostname should no longer validate"
        )

        self.assertFalse(
            validator.isValid("http://localhost/test/index.html"),
            "localhost URL should no longer validate"
        )

        self.assertTrue(
            validator.isValid("http://www.apache.org/test/index.html"),
            "www.apache.org should still validate"
        )

    
    
    def testValidator276(self) -> None:
        validator = UrlValidator.UrlValidator6()

        self.assertTrue(
            validator.isValid("http://www.apache.org/test/index.html"),
            "http://apache.org/ should be allowed by default"
        )

        self.assertFalse(
            validator.isValid("file:///C:/some.file"),
            "file:///c:/ shouldn't be allowed by default"
        )

        self.assertFalse(
            validator.isValid("file:///C:\\some.file"),
            "file:///c:\\ shouldn't be allowed by default"
        )

        self.assertFalse(
            validator.isValid("file:///etc/hosts"),
            "file:///etc/ shouldn't be allowed by default"
        )

        self.assertFalse(
            validator.isValid("file://localhost/etc/hosts"),
            "file://localhost/etc/ shouldn't be allowed by default"
        )

        self.assertFalse(
            validator.isValid("file://localhost/c:/some.file"),
            "file://localhost/c:/ shouldn't be allowed by default"
        )

        validator = UrlValidator.UrlValidator3(
            ["http", "file"], UrlValidator.ALLOW_LOCAL_URLS
        )

        self.assertTrue(
            validator.isValid("http://www.apache.org/test/index.html"),
            "http://apache.org/ should be allowed by default"
        )

        self.assertTrue(
            validator.isValid("file:///C:/some.file"),
            "file:///c:/ should now be allowed"
        )

        self.assertFalse(
            validator.isValid("file:///C:\\some.file"),
            "file:///c:\\ should not be allowed"
        )

        self.assertTrue(
            validator.isValid("file:///etc/hosts"),
            "file:///etc/ should now be allowed"
        )

        self.assertTrue(
            validator.isValid("file://localhost/etc/hosts"),
            "file://localhost/etc/ should now be allowed"
        )

        self.assertTrue(
            validator.isValid("file://localhost/c:/some.file"),
            "file://localhost/c:/ should now be allowed"
        )

        self.assertFalse(
            validator.isValid("file://C:/some.file"),
            "file://c:/ shouldn't ever be allowed, needs file:///c:/"
        )

        self.assertFalse(
            validator.isValid("file://C:\\some.file"),
            "file://c:\\ shouldn't ever be allowed, needs file:///c:/"
        )

    
    
    def testValidator391OK(self) -> None:
        schemes = ["file"]
        urlValidator = UrlValidator.UrlValidator5(schemes)
        self.assertTrue(
            urlValidator.isValid("file:///C:/path/to/dir/"),
        )
    

    
    def testValidator391FAILS(self) -> None:
        schemes = ["file"]
        urlValidator = UrlValidator.UrlValidator5(schemes)
        self.assertTrue(
            urlValidator.isValid("file:/C:/path/to/dir/")
        )

    
    
    def testValidator309(self) -> None:
        urlValidator = UrlValidator.UrlValidator6()
        self.assertTrue(
            urlValidator.isValid("http://sample.ondemand.com/")
        )
        self.assertTrue(
            urlValidator.isValid("hTtP://sample.ondemand.CoM/")
        )
        self.assertTrue(
            urlValidator.isValid("httpS://SAMPLE.ONEMAND.COM/")
        )
        urlValidator = UrlValidator.UrlValidator5(["HTTP", "HTTPS"])
        self.assertTrue(
            urlValidator.isValid("http://sample.ondemand.com/")
        )
        self.assertTrue(
            urlValidator.isValid("hTtP://sample.ondemand.CoM/")
        )
        self.assertTrue(
            urlValidator.isValid("httpS://SAMPLE.ONEMAND.COM/")
        )

    
    
    def testValidator339(self) -> None:
        urlValidator = UrlValidator.UrlValidator6()
        self.assertTrue(
            urlValidator.isValid("http://www.cnn.com/WORLD/?hpt=sitenav")
        )  # without
        self.assertTrue(
            urlValidator.isValid("http://www.cnn.com./WORLD/?hpt=sitenav")
        )  # with
        self.assertFalse(
            urlValidator.isValid("http://www.cnn.com../")
        )  # doubly dotty
        self.assertFalse(
            urlValidator.isValid("http://www.cnn.invalid/")
        )
        self.assertFalse(
            urlValidator.isValid("http://www.cnn.invalid./")
        )  # check . does not affect invalid domains

    
    
    def testValidator339IDN(self) -> None:
        urlValidator = UrlValidator.UrlValidator6()
        self.assertTrue(
            urlValidator.isValid("http://президент.рф/WORLD/?hpt=sitenav")
        )  # without
        self.assertTrue(
            urlValidator.isValid("http://президент.рф./WORLD/?hpt=sitenav")
        )  # with
        self.assertFalse(
            urlValidator.isValid("http://президент.рф..../")
        )  # very dotty
        self.assertFalse(
            urlValidator.isValid("http://президент.рф.../")
        )  # triply dotty
        self.assertFalse(
            urlValidator.isValid("http://президент.рф../")
        )  # doubly dotty

    
    
    def testValidator342(self) -> None:
        urlValidator = UrlValidator.UrlValidator6()
        self.assertTrue(
            urlValidator.isValid("http://example.rocks/")
        )
        self.assertTrue(
            urlValidator.isValid("http://example.rocks")
        )

    
    
    def testValidator411(self) -> None:
        urlValidator = UrlValidator.UrlValidator6()
        self.assertTrue(
            urlValidator.isValid("http://example.rocks:/")
        )
        self.assertTrue(
            urlValidator.isValid("http://example.rocks:0/")
        )
        self.assertTrue(
            urlValidator.isValid("http://example.rocks:65535/")
        )
        self.assertFalse(
            urlValidator.isValid("http://example.rocks:65536/")
        )
        self.assertFalse(
            urlValidator.isValid("http://example.rocks:100000/")
        )
    

    
    def testValidator464(self) -> None:
        schemes = ["file"]
        urlValidator = UrlValidator.UrlValidator5(schemes)
        fileNAK = "file://bad ^ domain.com/label/test"
        self.assertFalse(
            urlValidator.isValid(fileNAK),
            fileNAK
        )

    
    
    def testValidator452(self) -> None:
        urlValidator = UrlValidator.UrlValidator6()
        self.assertTrue(
            urlValidator.isValid("http://[::FFFF:129.144.52.38]:80/index.html")
        )

    
    
    def testValidator473_1(self) -> None:
        with self.assertRaises(ValueError):
            UrlValidator([], None, 0, None)

    
    
    def testValidator473_2(self) -> None:
        items = []
        with self.assertRaises(ValueError):
            UrlValidator([], None, 0, DomainValidator.getInstance2(True, items))

    
    
    def testValidator473_3(self) -> None:
        items = []
        with self.assertRaises(ValueError):
            UrlValidator(
                [],
                None,
                UrlValidator.ALLOW_LOCAL_URLS,
                DomainValidator.getInstance2(False, items)
            )
    

    
    def testValidateUrl(self) -> None:
        self.assertTrue(True)

    
    
    def testValidator290(self) -> None:
        validator = UrlValidator.UrlValidator6()
        self.assertTrue(
            validator.isValid("http://xn--h1acbxfam.idn.icann.org/")
        )
        self.assertTrue(
            validator.isValid("http://test.xn--lgbbat1ad8j")
        )  # Algeria
        self.assertTrue(
            validator.isValid("http://test.xn--fiqs8s")
        )  # China
        self.assertTrue(
            validator.isValid("http://test.xn--fiqz9s")
        )  # China
        self.assertTrue(
            validator.isValid("http://test.xn--wgbh1c")
        )  # Egypt
        self.assertTrue(
            validator.isValid("http://test.xn--j6w193g")
        )  # Hong Kong
        self.assertTrue(
            validator.isValid("http://test.xn--h2brj9c")
        )  # India
        self.assertTrue(
            validator.isValid("http://test.xn--mgbbh1a71e")
        )  # India
        self.assertTrue(
            validator.isValid("http://test.xn--fpcrj9c3d")
        )  # India
        self.assertTrue(
            validator.isValid("http://test.xn--gecrj9c")
        )  # India
        self.assertTrue(
            validator.isValid("http://test.xn--s9brj9c")
        )  # India
        self.assertTrue(
            validator.isValid("http://test.xn--xkc2dl3a5ee0h")
        )  # India
        self.assertTrue(
            validator.isValid("http://test.xn--45brj9c")
        )  # India
        self.assertTrue(
            validator.isValid("http://test.xn--mgba3a4f16a")
        )  # Iran
        self.assertTrue(
            validator.isValid("http://test.xn--mgbayh7gpa")
        )  # Jordan
        self.assertTrue(
            validator.isValid("http://test.xn--mgbc0a9azcg")
        )  # Morocco
        self.assertTrue(
            validator.isValid("http://test.xn--ygbi2ammx")
        )  # Palestinian Territory
        self.assertTrue(
            validator.isValid("http://test.xn--wgbl6a")
        )  # Qatar
        self.assertTrue(
            validator.isValid("http://test.xn--p1ai")
        )  # Russia
        self.assertTrue(
            validator.isValid("http://test.xn--mgberp4a5d4ar")
        )  # Saudi Arabia
        self.assertTrue(
            validator.isValid("http://test.xn--90a3ac")
        )  # Serbia
        self.assertTrue(
            validator.isValid("http://test.xn--yfro4i67o")
        )  # Singapore
        self.assertTrue(
            validator.isValid("http://test.xn--clchc0ea0b2g2a9gcd")
        )  # Singapore
        self.assertTrue(
            validator.isValid("http://test.xn--3e0b707e")
        )  # South Korea
        self.assertTrue(
            validator.isValid("http://test.xn--fzc2c9e2c")
        )  # Sri Lanka
        self.assertTrue(
            validator.isValid("http://test.xn--xkc2al3hye2a")
        )  # Sri Lanka
        self.assertTrue(
            validator.isValid("http://test.xn--ogbpf8fl")
        )  # Syria
        self.assertTrue(
            validator.isValid("http://test.xn--kprw13d")
        )  # Taiwan
        self.assertTrue(
            validator.isValid("http://test.xn--kpry57d")
        )  # Taiwan
        self.assertTrue(
            validator.isValid("http://test.xn--o3cw4h")
        )  # Thailand
        self.assertTrue(
            validator.isValid("http://test.xn--pgbs0dh")
        )  # Tunisia
        self.assertTrue(
            validator.isValid("http://test.xn--mgbaam7a8h")
        )  # United Arab Emirates

    
    
    def testValidator361(self) -> None:
        validator = UrlValidator.UrlValidator6()
        self.assertTrue(validator.isValid("http://hello.tokyo/"))

    
    
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

    
    
    def testValidator375(self) -> None:
        validator = UrlValidator.UrlValidator6()
        url = "http://[FEDC:BA98:7654:3210:FEDC:BA98:7654:3210]:80/index.html"
        self.assertTrue(
            validator.isValid(url),
            "IPv6 address URL should validate: " + url
        )
        url = "http://[::1]:80/index.html"
        self.assertTrue(
            validator.isValid(url),
            "IPv6 address URL should validate: " + url
        )
        url = "http://FEDC:BA98:7654:3210:FEDC:BA98:7654:3210:80/index.html"
        self.assertFalse(
            validator.isValid(url),
            "IPv6 address without [] should not validate: " + url
        )

    
    
    def testValidator353(self) -> None:
        validator = UrlValidator.UrlValidator6()
        self.assertTrue(validator.isValid("http://www.apache.org:80/path"))
        self.assertTrue(validator.isValid("http://user:pass@www.apache.org:80/path"))
        self.assertTrue(validator.isValid("http://user:@www.apache.org:80/path"))
        self.assertTrue(validator.isValid("http://user@www.apache.org:80/path"))
        self.assertTrue(
            validator.isValid("http://us%00er:-._~!$&'()*+,;=@www.apache.org:80/path")
        )
        self.assertFalse(validator.isValid("http://:pass@www.apache.org:80/path"))
        self.assertFalse(validator.isValid("http://:@www.apache.org:80/path"))
        self.assertFalse(validator.isValid("http://user:pa:ss@www.apache.org/path"))
        self.assertFalse(validator.isValid("http://user:pa@ss@www.apache.org/path"))

    
    
    def testValidator382(self) -> None:
        validator = UrlValidator.UrlValidator6()
        self.assertTrue(
            validator.isValid(
                "ftp://username:password@example.com:8042" +\
                    "/over/there/index.dtb?type=animal&name=narwhal#nose"
            )
        )
    
    
    def testValidator380(self) -> None:
        validator = UrlValidator.UrlValidator6()
        self.assertTrue(validator.isValid("http://www.apache.org:80/path"))
        self.assertTrue(validator.isValid("http://www.apache.org:8/path"))
        self.assertTrue(validator.isValid("http://www.apache.org:/path"))

    
    
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
    

    
    def testValidator467(self) -> None:
        validator = UrlValidator.UrlValidator4(UrlValidator.ALLOW_2_SLASHES)
        self.assertTrue(validator.isValid("https://example.com/some_path/path/"))
        self.assertTrue(validator.isValid("https://example.com//somepath/path/"))
        self.assertTrue(validator.isValid("https://example.com//some_path/path/"))
        self.assertTrue(validator.isValid("http://example.com//_test")) # VALIDATOR-429

    
    
    def testValidator283(self) -> None:
        validator = UrlValidator.UrlValidator6()
        self.assertFalse(
            validator.isValid(
                "http://finance.yahoo.com/news/" +\
                    "Owners-54B-NY-housing-apf-2493139299.html?x=0&ap=%fr"
            )
        )
        self.assertTrue(
            validator.isValid(
                "http://finance.yahoo.com/news/" +\
                    "Owners-54B-NY-housing-apf-2493139299.html?x=0&ap=%22"
            )
        )
    

    
    def testFragments(self) -> None:
        schemes = ["http", "https"]
        urlValidator = UrlValidator.UrlValidator3(schemes, UrlValidator.NO_FRAGMENTS)
        self.assertFalse(urlValidator.isValid("http://apache.org/a/b/c#frag"))
        urlValidator = UrlValidator.UrlValidator5(schemes)
        self.assertTrue(urlValidator.isValid("http://apache.org/a/b/c#frag"))
    
    
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
            if not UrlValidatorTest.incrementTestPartsIndex(self.testPartsIndex, testObjects):
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
            maxIndex = (maxIndex and (index == (len(part) - 1)))
            if carry:
                if index < len(part) - 1:
                    index += 1
                    testPartsIndex[testPartsIndexIndex] = index
                    carry = False
                else:
                    testPartsIndex[testPartsIndexIndex] = 0
                    carry = True
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

    
    @staticmethod
    def main(args) -> None:
        uv = UrlValidator.UrlValidator6()
        for arg in args:
            try:
                uri = urlparse(arg)
                print(uri.geturl())
                print(f"URI scheme: {uri.scheme}")
                print(f"URI scheme specific part: {uri.geturl().split(':', 1)[1]}")
                rawSchemeSpecificPart = arg.split(':', 1)[1]\
                    .split('://', 1)[-1]\
                    .split('/', 1)[-1]\
                    .split('?', 1)[0]\
                    .split('#', 1)[0]
                print(f"URI raw scheme specific part: {rawSchemeSpecificPart}")
                print(f"URI auth: {uri.netloc}")
                rawAuthority = ''
                if '//' in arg:
                    rawAuthority = arg.split('//', 1)[1].split('/', 1)[0]
                print(f"URI raw auth: {rawAuthority}")
                print(f"URI userInfo: {uri.username}")
                rawUserInfo = ''
                if '@' in rawAuthority:
                    rawUserInfo = rawAuthority.split('@', 1)[0]
                print(f"URI raw userInfo: {rawUserInfo}")
                print(f"URI host: {uri.hostname}")
                print(f"URI port: {uri.port}")
                print(f"URI path: {uri.path}")
                rawPath = ''
                if '/' in arg.split('//', 1)[1]:
                    rawPath = '/' +\
                        arg.split('//', 1)[1].split('/', 1)[1]\
                            .split('?', 1)[0].split('#', 1)[0]
                print(f"URI raw path: {rawPath}")
                print(f"URI query: {uri.query}")
                rawQuery = ''
                if '?' in arg:
                    rawQuery = arg.split('?', 1)[1].split('#', 1)[0]
                print(f"URI raw query: {rawQuery}")
                print(f"URI fragment: {uri.fragment}")
                rawFragment = ''
                if '#' in arg:
                    rawFragment = arg.split('#', 1)[1]
                print(f"URI raw fragment: {rawFragment}")
            except (URLError, ValueError) as e:
                print(e)
            print(f"isValid: {uv.isValid(arg)}")