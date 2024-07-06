from __future__ import annotations
import time
import re
import unittest
import pytest
import pathlib
import io
import typing
from typing import *
import os
import unittest
from src.main.org.apache.commons.validator.routines.DomainValidator import *


class DomainValidatorTest(unittest.TestCase):

    __validator: DomainValidator = None

    def setUp(self) -> None:
        self.__validator = DomainValidator.getInstance0()

    @staticmethod
    def main(a: typing.List[str]) -> None:

        pass  # LLM could not translate this method

    def testGetArray(self) -> None:
        self.assertIsNotNone(
            DomainValidator.getTLDEntries(ArrayType.COUNTRY_CODE_MINUS)
        )
        self.assertIsNotNone(DomainValidator.getTLDEntries(ArrayType.COUNTRY_CODE_PLUS))
        self.assertIsNotNone(DomainValidator.getTLDEntries(ArrayType.GENERIC_MINUS))
        self.assertIsNotNone(DomainValidator.getTLDEntries(ArrayType.GENERIC_PLUS))
        self.assertIsNotNone(DomainValidator.getTLDEntries(ArrayType.LOCAL_MINUS))
        self.assertIsNotNone(DomainValidator.getTLDEntries(ArrayType.LOCAL_PLUS))
        self.assertIsNotNone(DomainValidator.getTLDEntries(ArrayType.COUNTRY_CODE_RO))
        self.assertIsNotNone(DomainValidator.getTLDEntries(ArrayType.GENERIC_RO))
        self.assertIsNotNone(DomainValidator.getTLDEntries(ArrayType.INFRASTRUCTURE_RO))
        self.assertIsNotNone(DomainValidator.getTLDEntries(ArrayType.LOCAL_RO))

    def testEnumIsPublic(self) -> None:

        pass  # LLM could not translate this method

    def test_LOCAL_TLDS_sortedAndLowerCase(self) -> None:
        sorted = self.__isSortedLowerCase0("LOCAL_TLDS")
        self.assertTrue(sorted)

    def test_GENERIC_TLDS_sortedAndLowerCase(self) -> None:
        sorted = self.__isSortedLowerCase0("GENERIC_TLDS")
        self.assertTrue(sorted)

    def test_COUNTRY_CODE_TLDS_sortedAndLowerCase(self) -> None:
        sorted = self.__isSortedLowerCase0("COUNTRY_CODE_TLDS")
        self.assertTrue(sorted)

    def test_INFRASTRUCTURE_TLDS_sortedAndLowerCase(self) -> None:
        sorted = self.__isSortedLowerCase0("INFRASTRUCTURE_TLDS")
        self.assertTrue(sorted)

    def testIsIDNtoASCIIBroken(self) -> None:
        print(">>DomainValidatorTest.testIsIDNtoASCIIBroken()")
        input = "."
        ok = input == IDN.toASCII(input)
        print("IDN.toASCII is " + ("OK" if ok else "BROKEN"))
        props = [
            "java.version",  #    Java Runtime Environment version
            "java.vendor",  # Java Runtime Environment vendor
            "java.vm.specification.version",  #   Java Virtual Machine specification version
            "java.vm.specification.vendor",  #    Java Virtual Machine specification vendor
            "java.vm.specification.name",  #  Java Virtual Machine specification name
            "java.vm.version",  # Java Virtual Machine implementation version
            "java.vm.vendor",  #  Java Virtual Machine implementation vendor
            "java.vm.name",  #    Java Virtual Machine implementation name
            "java.specification.version",  #  Java Runtime Environment specification version
            "java.specification.vendor",  #   Java Runtime Environment specification vendor
            "java.specification.name",  # Java Runtime Environment specification name
            "java.class.version",  #  Java class format version number
        ]
        for t in props:
            print(t + "=" + System.getProperty(t))
        print("<<DomainValidatorTest.testIsIDNtoASCIIBroken()")
        self.assertTrue(True)  # dummy assertion to satisfy lint

    def testUnicodeToASCII(self) -> None:
        asciidots = ["", ",", ".", "a.", "a.b", "a..b", "a...b", ".a", "..a"]
        for s in asciidots:
            self.assertEqual(s, DomainValidator.unicodeToASCII(s))
        otherDots = [
            ["b\u3002", "b."],
            ["b\uFF0E", "b."],
            ["b\uFF61", "b."],
            ["\u3002", "."],
            ["\uFF0E", "."],
            ["\uFF61", "."],
        ]
        for s in otherDots:
            self.assertEqual(s[1], DomainValidator.unicodeToASCII(s[0]))

    def testValidator306(self) -> None:
        longString = "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz0123456789A"
        self.assertEqual(63, len(longString))  # 26 * 2 + 11

        self.assertTrue(
            "63 chars label should validate",
            self.__validator.isValidDomainSyntax(longString + ".com"),
        )
        self.assertFalse(
            "64 chars label should fail",
            self.__validator.isValidDomainSyntax(longString + "x.com"),
        )

        self.assertTrue(
            "63 chars TLD should validate",
            self.__validator.isValidDomainSyntax("test." + longString),
        )
        self.assertFalse(
            "64 chars TLD should fail",
            self.__validator.isValidDomainSyntax("test.x" + longString),
        )

        longDomain = (
            longString + "." + longString + "." + longString + "." + longString[0:61]
        )
        self.assertEqual(253, len(longDomain))
        self.assertTrue(
            "253 chars domain should validate",
            self.__validator.isValidDomainSyntax(longDomain),
        )
        self.assertFalse(
            "254 chars domain should fail",
            self.__validator.isValidDomainSyntax(longDomain + "x"),
        )

    def testValidator297(self) -> None:
        self.assertTrue(
            "xn--d1abbgf6aiiy.xn--p1ai should validate",
            self.__validator.isValid("xn--d1abbgf6aiiy.xn--p1ai"),
        )  # This uses a valid TLD

    def testDomainNoDots(self) -> None:
        self.assertTrue(
            "a (alpha) should validate", self.__validator.isValidDomainSyntax("a")
        )
        self.assertTrue(
            "9 (alphanum) should validate", self.__validator.isValidDomainSyntax("9")
        )
        self.assertTrue(
            "c-z (alpha - alpha) should validate",
            self.__validator.isValidDomainSyntax("c-z"),
        )

        self.assertFalse(
            "c- (alpha -) should fail", self.__validator.isValidDomainSyntax("c-")
        )
        self.assertFalse(
            "-c (- alpha) should fail", self.__validator.isValidDomainSyntax("-c")
        )
        self.assertFalse("- (-) should fail", self.__validator.isValidDomainSyntax("-"))

    def testRFC2396toplabel(self) -> None:
        self.assertTrue(
            "a.c (alpha) should validate", self.__validator.isValidDomainSyntax("a.c")
        )
        self.assertTrue(
            "a.cc (alpha alpha) should validate",
            self.__validator.isValidDomainSyntax("a.cc"),
        )
        self.assertTrue(
            "a.c9 (alpha alphanum) should validate",
            self.__validator.isValidDomainSyntax("a.c9"),
        )
        self.assertTrue(
            "a.c-9 (alpha - alphanum) should validate",
            self.__validator.isValidDomainSyntax("a.c-9"),
        )
        self.assertTrue(
            "a.c-z (alpha - alpha) should validate",
            self.__validator.isValidDomainSyntax("a.c-z"),
        )

        self.assertFalse(
            "a.9c (alphanum alpha) should fail",
            self.__validator.isValidDomainSyntax("a.9c"),
        )
        self.assertFalse(
            "a.c- (alpha -) should fail", self.__validator.isValidDomainSyntax("a.c-")
        )
        self.assertFalse(
            "a.- (-) should fail", self.__validator.isValidDomainSyntax("a.-")
        )
        self.assertFalse(
            "a.-9 (- alphanum) should fail",
            self.__validator.isValidDomainSyntax("a.-9"),
        )

    def testRFC2396domainlabel(self) -> None:
        self.assertTrue("a.ch should validate", self.__validator.isValid("a.ch"))
        self.assertTrue("9.ch should validate", self.__validator.isValid("9.ch"))
        self.assertTrue("az.ch should validate", self.__validator.isValid("az.ch"))
        self.assertTrue("09.ch should validate", self.__validator.isValid("09.ch"))
        self.assertTrue("9-1.ch should validate", self.__validator.isValid("9-1.ch"))
        self.assertFalse(
            "91-.ch should not validate", self.__validator.isValid("91-.ch")
        )
        self.assertFalse("-.ch should not validate", self.__validator.isValid("-.ch"))

    def testIDNJava6OrLater(self) -> None:
        version: str = System.getProperty("java.version")
        if version.compareTo("1.6") < 0:
            System.out.println("Cannot run Unicode IDN tests")
            return  # Cannot run the test
        # xn--d1abbgf6aiiy.xn--p1ai http://президент.рф
        assertTrue(
            "b\u00fccher.ch should validate", validator.isValid("www.b\u00fccher.ch")
        )
        assertTrue(
            "xn--d1abbgf6aiiy.xn--p1ai should validate",
            validator.isValid("xn--d1abbgf6aiiy.xn--p1ai"),
        )
        assertTrue("президент.рф should validate", validator.isValid("президент.рф"))
        assertFalse(
            "www.\uFFFD.ch FFFD should fail", validator.isValid("www.\uFFFD.ch")
        )

    def testIDN(self) -> None:
        self.assertTrue(
            "b\u00fccher.ch in IDN should validate",
            self.__validator.isValid("www.xn--bcher-kva.ch"),
        )

    def testAllowLocal(self) -> None:
        noLocal: DomainValidator = DomainValidator.getInstance1(False)
        allowLocal: DomainValidator = DomainValidator.getInstance1(True)

        self.assertEqual(noLocal, self.__validator)

        self.assertFalse(
            "localhost.localdomain should validate",
            noLocal.isValid("localhost.localdomain"),
        )
        self.assertFalse("localhost should validate", noLocal.isValid("localhost"))

        self.assertTrue(
            "localhost.localdomain should validate",
            allowLocal.isValid("localhost.localdomain"),
        )
        self.assertTrue("localhost should validate", allowLocal.isValid("localhost"))
        self.assertTrue("hostname should validate", allowLocal.isValid("hostname"))
        self.assertTrue(
            "machinename should validate", allowLocal.isValid("machinename")
        )

        self.assertTrue("apache.org should validate", allowLocal.isValid("apache.org"))
        self.assertFalse(
            "domain name with spaces shouldn't validate",
            allowLocal.isValid(" apache.org "),
        )

    def testTopLevelDomains(self) -> None:
        self.assertTrue(
            ".arpa should validate as iTLD",
            self.__validator.isValidInfrastructureTld(".arpa"),
        )
        self.assertFalse(
            ".com shouldn't validate as iTLD",
            self.__validator.isValidInfrastructureTld(".com"),
        )

        self.assertTrue(
            ".name should validate as gTLD", self.__validator.isValidGenericTld(".name")
        )
        self.assertFalse(
            ".us shouldn't validate as gTLD", self.__validator.isValidGenericTld(".us")
        )

        self.assertTrue(
            ".uk should validate as ccTLD",
            self.__validator.isValidCountryCodeTld(".uk"),
        )
        self.assertFalse(
            ".org shouldn't validate as ccTLD",
            self.__validator.isValidCountryCodeTld(".org"),
        )

        self.assertTrue(
            ".COM should validate as TLD", self.__validator.isValidTld(".COM")
        )
        self.assertTrue(
            ".BiZ should validate as TLD", self.__validator.isValidTld(".BiZ")
        )

        self.assertFalse(
            "invalid TLD shouldn't validate", self.__validator.isValid(".nope")
        )  # TODO this is not guaranteed invalid forever
        self.assertFalse(
            "empty string shouldn't validate as TLD", self.__validator.isValid("")
        )
        self.assertFalse(
            "null shouldn't validate as TLD", self.__validator.isValid(None)
        )

    def testInvalidDomains(self) -> None:
        self.assertFalse(
            "bare TLD .org shouldn't validate", self.__validator.isValid(".org")
        )
        self.assertFalse(
            "domain name with spaces shouldn't validate",
            self.__validator.isValid(" apache.org "),
        )
        self.assertFalse(
            "domain name containing spaces shouldn't validate",
            self.__validator.isValid("apa che.org"),
        )
        self.assertFalse(
            "domain name starting with dash shouldn't validate",
            self.__validator.isValid("-testdomain.name"),
        )
        self.assertFalse(
            "domain name ending with dash shouldn't validate",
            self.__validator.isValid("testdomain-.name"),
        )
        self.assertFalse(
            "domain name starting with multiple dashes shouldn't validate",
            self.__validator.isValid("---c.com"),
        )
        self.assertFalse(
            "domain name ending with multiple dashes shouldn't validate",
            self.__validator.isValid("c--.com"),
        )
        self.assertFalse(
            "domain name with invalid TLD shouldn't validate",
            self.__validator.isValid("apache.rog"),
        )

        self.assertFalse(
            "URL shouldn't validate", self.__validator.isValid("http://www.apache.org")
        )
        self.assertFalse(
            "Empty string shouldn't validate as domain name",
            self.__validator.isValid(" "),
        )
        self.assertFalse(
            "Null shouldn't validate as domain name", self.__validator.isValid(None)
        )

    def testValidDomains(self) -> None:
        self.assertTrue(
            "apache.org should validate", self.__validator.isValid("apache.org")
        )
        self.assertTrue(
            "www.google.com should validate", self.__validator.isValid("www.google.com")
        )

        self.assertTrue(
            "test-domain.com should validate",
            self.__validator.isValid("test-domain.com"),
        )
        self.assertTrue(
            "test---domain.com should validate",
            self.__validator.isValid("test---domain.com"),
        )
        self.assertTrue(
            "test-d-o-m-ain.com should validate",
            self.__validator.isValid("test-d-o-m-ain.com"),
        )
        self.assertTrue(
            "two-letter domain label should validate", self.__validator.isValid("as.uk")
        )

        self.assertTrue(
            "case-insensitive ApAchE.Org should validate",
            self.__validator.isValid("ApAchE.Org"),
        )

        self.assertTrue(
            "single-character domain label should validate",
            self.__validator.isValid("z.com"),
        )

        self.assertTrue(
            "i.have.an-example.domain.name should validate",
            self.__validator.isValid("i.have.an-example.domain.name"),
        )

    @staticmethod
    def __isSortedLowerCase1(name: str, array: typing.List[str]) -> bool:
        sorted = True
        strictlySorted = True
        length = len(array)
        lowerCase = DomainValidatorTest.__isLowerCase(
            array[length - 1]
        )  # Check the last entry
        for i in range(0, length - 1):  # compare all but last entry with next
            entry = array[i]
            nextEntry = array[i + 1]
            cmp = entry.__cmp__(nextEntry)
            if cmp > 0:  # out of order
                print(
                    "Out of order entry: " + entry + " < " + nextEntry + " in " + name
                )
                sorted = False
            elif cmp == 0:
                strictlySorted = False
                print("Duplicated entry: " + entry + " in " + name)
            if not DomainValidatorTest.__isLowerCase(entry):
                print("Non lowerCase entry: " + entry + " in " + name)
                lowerCase = False
        return sorted and strictlySorted and lowerCase

    @staticmethod
    def __isLowerCase(string: str) -> bool:
        return string == string.lower()

    @staticmethod
    def __isSortedLowerCase0(arrayName: str) -> bool:
        f = DomainValidator.__dict__[arrayName]
        isPrivate = f.__private__
        if isPrivate:
            f.__private__ = False
        array = f.__get__(None)
        try:
            return DomainValidatorTest.__isSortedLowerCase1(arrayName, array)
        finally:
            if isPrivate:
                f.__private__ = True

    @staticmethod
    def __isInIanaList1(
        name: str, array: typing.List[str], ianaTlds: typing.Set[str]
    ) -> bool:
        for i in range(len(array)):
            if array[i] not in ianaTlds:
                print(name + " contains unexpected value: " + array[i])
        return True

    @staticmethod
    def __isInIanaList0(arrayName: str, ianaTlds: typing.Set[str]) -> bool:
        f = DomainValidator.__class__.getDeclaredField(arrayName)
        isPrivate = Modifier.isPrivate(f.getModifiers())
        if isPrivate:
            f.setAccessible(True)
        array = typing.cast(typing.List[str], f.get(None))
        try:
            return DomainValidatorTest.__isInIanaList1(arrayName, array, ianaTlds)
        finally:
            if isPrivate:
                f.setAccessible(False)

    @staticmethod
    def __closeQuietly(in_: Closeable) -> None:
        if in_ is not None:
            try:
                in_.close()
            except IOException:
                pass

    @staticmethod
    def __isNotInRootZone(domain: str) -> bool:
        tldurl = "http://www.iana.org/domains/root/db/" + domain + ".html"
        rootCheck = pathlib.Path("target", "tld_" + domain + ".html")
        in_: typing.Optional[io.BufferedReader] = None
        try:
            DomainValidatorTest.__download(rootCheck, tldurl, 0)
            in_ = io.BufferedReader(io.FileIO(rootCheck))
            inputLine: str
            while (inputLine := in_.readline()) != b"":
                if inputLine.decode().contains(
                    "This domain is not present in the root zone at this time."
                ):
                    return True
            in_.close()
        except io.IOError as e:
            pass
        finally:
            DomainValidatorTest.__closeQuietly(in_)
        return False

    @staticmethod
    def __download(f: pathlib.Path, tldurl: str, timestamp: int) -> int:

        pass  # LLM could not translate this method

    @staticmethod
    def __getHtmlInfo(f: pathlib.Path) -> typing.Dict[str, typing.List[str]]:
        info: typing.Dict[str, typing.List[str]] = {}

        domain: typing.Pattern[str] = re.compile(
            '.*<a href="/domains/root/db/([^.]+)\\.html'
        )
        type: typing.Pattern[str] = re.compile("\\s+<td>([^<]+)</td>")
        comment: typing.Pattern[str] = re.compile("\\s+<td>([^<]+)</td>")

        with open(f, "r") as br:
            line: str
            while (line := br.readline()) != "":
                m: typing.Match[str] = domain.match(line)
                if m:
                    dom: str = m.group(1)
                    typ: str = "??"
                    com: str = "??"
                    line = br.readline()
                    while re.match("^\\s*$", line):  # extra blank lines introduced
                        line = br.readline()
                    t: typing.Match[str] = type.match(line)
                    if t:
                        typ = t.group(1)
                        line = br.readline()
                        if re.match("\\s+<!--.*", line):
                            while not re.match(".*-->.*", line):
                                line = br.readline()
                            line = br.readline()
                        while not re.match(".*</td>.*", line):
                            line += " " + br.readline()
                        n: typing.Match[str] = comment.match(line)
                        if n:
                            com = n.group(1)
                        if (
                            com.__contains__("Not assigned")
                            or com.__contains__("Retired")
                            or typ == "test"
                        ):
                            pass
                        else:
                            info[dom.lower()] = [typ, com]
                    else:
                        print("Unexpected type: " + line)
        return info

    @staticmethod
    def __printMap(header: str, map: typing.Dict[str, str], string: str) -> None:
        print("Entries missing from " + string + " List\n")
        if header is not None:
            print("        // Taken from " + header)
        for me in map.items():
            print('        "' + me[0] + '", // ' + me[1])
        print("\nDone")
