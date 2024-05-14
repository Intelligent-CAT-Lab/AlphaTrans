# Imports Begin
from src.main.org.apache.commons.validator.routines.DomainValidator import *
import typing
import pathlib

# Imports End


class DomainValidatorTest(TestCase):

    # Class Fields Begin
    __validator: DomainValidator = None
    # Class Fields End

    # Class Methods Begin
    def setUp(self) -> None:
        pass

    @staticmethod
    def main(a: typing.List[str]) -> None:
        pass

    def testGetArray(self) -> None:
        pass

    def testEnumIsPublic(self) -> None:
        pass

    def test_LOCAL_TLDS_sortedAndLowerCase(self) -> None:
        pass

    def test_GENERIC_TLDS_sortedAndLowerCase(self) -> None:
        pass

    def test_COUNTRY_CODE_TLDS_sortedAndLowerCase(self) -> None:
        pass

    def test_INFRASTRUCTURE_TLDS_sortedAndLowerCase(self) -> None:
        pass

    def testIsIDNtoASCIIBroken(self) -> None:
        pass

    def testUnicodeToASCII(self) -> None:
        pass

    def testValidator306(self) -> None:
        pass

    def testValidator297(self) -> None:
        pass

    def testDomainNoDots(self) -> None:
        pass

    def testRFC2396toplabel(self) -> None:
        pass

    def testRFC2396domainlabel(self) -> None:
        pass

    def testIDNJava6OrLater(self) -> None:
        pass

    def testIDN(self) -> None:
        pass

    def testAllowLocal(self) -> None:
        pass

    def testTopLevelDomains(self) -> None:
        pass

    def testInvalidDomains(self) -> None:
        pass

    def testValidDomains(self) -> None:
        pass

    @staticmethod
    def __isSortedLowerCase1(name: str, array: typing.List[str]) -> bool:
        pass

    @staticmethod
    def __isLowerCase(string: str) -> bool:
        pass

    @staticmethod
    def __isSortedLowerCase0(arrayName: str) -> bool:
        pass

    @staticmethod
    def __isInIanaList1(
        name: str, array: typing.List[str], ianaTlds: typing.Set[str]
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
    def __printMap(header: str, map: typing.Dict[str, str], string: str) -> None:
        pass

    # Class Methods End
