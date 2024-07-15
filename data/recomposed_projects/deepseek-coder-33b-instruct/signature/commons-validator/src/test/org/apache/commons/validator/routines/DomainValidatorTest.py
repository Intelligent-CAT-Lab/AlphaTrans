from __future__ import annotations
import time
import inspect
import re
import urllib
import datetime
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

        OK = True
        for list in [
            "INFRASTRUCTURE_TLDS",
            "COUNTRY_CODE_TLDS",
            "GENERIC_TLDS",
            "LOCAL_TLDS",
        ]:
            OK &= DomainValidatorTest.__isSortedLowerCase0(list)
        if not OK:
            print("Fix arrays before retrying; cannot continue")
            return

        ianaTlds = set()  # keep for comparison with array contents
        dv = DomainValidator.getInstance0()
        txtFile = pathlib.Path("target/tlds-alpha-by-domain.txt")
        timestamp = DomainValidatorTest.__download(
            txtFile, "https://data.iana.org/TLD/tlds-alpha-by-domain.txt", 0
        )
        htmlFile = pathlib.Path("target/tlds-alpha-by-domain.html")
        DomainValidatorTest.__download(
            htmlFile, "https://www.iana.org/domains/root/db", timestamp
        )

        with open(txtFile, "r") as br:
            line = br.readline()  # header
            if line.startswith("# Version "):
                header = line[2:]
            else:
                raise IOError("File does not have expected Version header")

            generateUnicodeTlds = False  # Change this to generate Unicode TLDs as well

            htmlInfo = DomainValidatorTest.__getHtmlInfo(htmlFile)
            missingTLD = {}  # stores entry and comments as String[]
            missingCC = {}
            while (line := br.readline()) != None:
                if not line.startswith("#"):
                    unicodeTld = ""  # only different from asciiTld if that was punycode
                    asciiTld = line.lower()
                    if line.startswith("XN--"):
                        unicodeTld = IDN.toUnicode(line)
                    else:
                        unicodeTld = asciiTld
                    if not dv.isValidTld(asciiTld):
                        info = htmlInfo.get(asciiTld)
                        if info != None:
                            type = info[0]
                            comment = info[1]
                            if "country-code" == type:  # Which list to use?
                                missingCC[asciiTld] = unicodeTld + " " + comment
                                if generateUnicodeTlds:
                                    missingCC[unicodeTld] = asciiTld + " " + comment
                            else:
                                missingTLD[asciiTld] = unicodeTld + " " + comment
                                if generateUnicodeTlds:
                                    missingTLD[unicodeTld] = asciiTld + " " + comment
                        else:
                            print("Expected to find HTML info for " + asciiTld)
                    ianaTlds.add(asciiTld)
                    if generateUnicodeTlds:
                        if unicodeTld != asciiTld:
                            ianaTlds.add(unicodeTld)

            for key in sorted(htmlInfo.keys()):
                if key not in ianaTlds:
                    if DomainValidatorTest.__isNotInRootZone(key):
                        print("INFO: HTML entry not yet in root zone: " + key)
                    else:
                        print("WARN: Expected to find text entry for html: " + key)

            if missingTLD:
                DomainValidatorTest.__printMap(header, missingTLD, "TLD")
            if missingCC:
                DomainValidatorTest.__printMap(header, missingCC, "CC")

            DomainValidatorTest.__isInIanaList0("INFRASTRUCTURE_TLDS", ianaTlds)
            DomainValidatorTest.__isInIanaList0("COUNTRY_CODE_TLDS", ianaTlds)
            DomainValidatorTest.__isInIanaList0("GENERIC_TLDS", ianaTlds)

        print("Finished checks")

    def testGetArray(self) -> None:

        assert DomainValidator.getTLDEntries(ArrayType.COUNTRY_CODE_MINUS) is not None
        assert DomainValidator.getTLDEntries(ArrayType.COUNTRY_CODE_PLUS) is not None
        assert DomainValidator.getTLDEntries(ArrayType.GENERIC_MINUS) is not None
        assert DomainValidator.getTLDEntries(ArrayType.GENERIC_PLUS) is not None
        assert DomainValidator.getTLDEntries(ArrayType.LOCAL_MINUS) is not None
        assert DomainValidator.getTLDEntries(ArrayType.LOCAL_PLUS) is not None
        assert DomainValidator.getTLDEntries(ArrayType.COUNTRY_CODE_RO) is not None
        assert DomainValidator.getTLDEntries(ArrayType.GENERIC_RO) is not None
        assert DomainValidator.getTLDEntries(ArrayType.INFRASTRUCTURE_RO) is not None
        assert DomainValidator.getTLDEntries(ArrayType.LOCAL_RO) is not None

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
            print(t + "=" + os.getenv(t))
        print("<<DomainValidatorTest.testIsIDNtoASCIIBroken()")
        self.assertTrue(True)  # dummy assertion to satisfy lint

    def testUnicodeToASCII(self) -> None:

        asciidots = [
            "",
            ",",
            ".",
            "a.",
            "a.b",
            "a..b",
            "a...b",
            ".a",
            "..a",
        ]
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

        long_string = "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz0123456789A"
        self.assertEqual(63, len(long_string))  # 26 * 2 + 11

        self.assertTrue(
            "63 chars label should validate",
            self.__validator.isValidDomainSyntax(long_string + ".com"),
        )
        self.assertFalse(
            "64 chars label should fail",
            self.__validator.isValidDomainSyntax(long_string + "x.com"),
        )

        self.assertTrue(
            "63 chars TLD should validate",
            self.__validator.isValidDomainSyntax("test." + long_string),
        )
        self.assertFalse(
            "64 chars TLD should fail",
            self.__validator.isValidDomainSyntax("test.x" + long_string),
        )

        long_domain = (
            long_string + "." + long_string + "." + long_string + "." + long_string[:61]
        )
        self.assertEqual(253, len(long_domain))
        self.assertTrue(
            "253 chars domain should validate",
            self.__validator.isValidDomainSyntax(long_domain),
        )
        self.assertFalse(
            "254 chars domain should fail",
            self.__validator.isValidDomainSyntax(long_domain + "x"),
        )

    def testValidator297(self) -> None:

        self.assertTrue(
            self.__validator.isValid("xn--d1abbgf6aiiy.xn--p1ai"),
            "xn--d1abbgf6aiiy.xn--p1ai should validate",
        )

    def testDomainNoDots(self) -> None:

        assert self.validator.isValidDomainSyntax("a")
        assert self.validator.isValidDomainSyntax("9")
        assert self.validator.isValidDomainSyntax("c-z")

        assert not self.validator.isValidDomainSyntax("c-")
        assert not self.validator.isValidDomainSyntax("-c")
        assert not self.validator.isValidDomainSyntax("-")

    def testRFC2396toplabel(self) -> None:

        assert self.__validator.isValidDomainSyntax("a.c")
        assert self.__validator.isValidDomainSyntax("a.cc")
        assert self.__validator.isValidDomainSyntax("a.c9")
        assert self.__validator.isValidDomainSyntax("a.c-9")
        assert self.__validator.isValidDomainSyntax("a.c-z")

        assert not self.__validator.isValidDomainSyntax("a.9c")
        assert not self.__validator.isValidDomainSyntax("a.c-")
        assert not self.__validator.isValidDomainSyntax("a.-")
        assert not self.__validator.isValidDomainSyntax("a.-9")

    def testRFC2396domainlabel(self) -> None:

        assert self.__validator.isValid("a.ch")
        assert self.__validator.isValid("9.ch")
        assert self.__validator.isValid("az.ch")
        assert self.__validator.isValid("09.ch")
        assert self.__validator.isValid("9-1.ch")
        assert not self.__validator.isValid("91-.ch")
        assert not self.__validator.isValid("-.ch")

    def testIDNJava6OrLater(self) -> None:

        version = platform.python_version()
        if version.split(".")[1] < "6":
            print("Cannot run Unicode IDN tests")
            return  # Cannot run the test

        assert self.__validator.isValid("www.b�cher.ch")
        assert self.__validator.isValid("xn--d1abbgf6aiiy.xn--p1ai")
        assert self.__validator.isValid("президент.рф")
        assert not self.__validator.isValid("www.\uFFFD.ch")

    def testIDN(self) -> None:

        self.assertTrue(
            self.__validator.isValid("www.xn--bcher-kva.ch"),
            "b\u00fccher.ch in IDN should validate",
        )

    def testAllowLocal(self) -> None:

        noLocal = DomainValidator.getInstance1(False)
        allowLocal = DomainValidator.getInstance1(True)

        self.assertEqual(noLocal, self.__validator)

        self.assertFalse(
            noLocal.isValid("localhost.localdomain"),
            "localhost.localdomain should validate",
        )
        self.assertFalse(noLocal.isValid("localhost"), "localhost should validate")

        self.assertTrue(
            allowLocal.isValid("localhost.localdomain"),
            "localhost.localdomain should validate",
        )
        self.assertTrue(allowLocal.isValid("localhost"), "localhost should validate")
        self.assertTrue(allowLocal.isValid("hostname"), "hostname should validate")
        self.assertTrue(
            allowLocal.isValid("machinename"), "machinename should validate"
        )

        self.assertTrue(allowLocal.isValid("apache.org"), "apache.org should validate")
        self.assertFalse(
            allowLocal.isValid(" apache.org "),
            "domain name with spaces shouldn't validate",
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

        assert not self.__validator.isValid(".org"), "bare TLD .org shouldn't validate"
        assert not self.__validator.isValid(
            " apache.org "
        ), "domain name with spaces shouldn't validate"
        assert not self.__validator.isValid(
            "apa che.org"
        ), "domain name containing spaces shouldn't validate"
        assert not self.__validator.isValid(
            "-testdomain.name"
        ), "domain name starting with dash shouldn't validate"
        assert not self.__validator.isValid(
            "testdomain-.name"
        ), "domain name ending with dash shouldn't validate"
        assert not self.__validator.isValid(
            "---c.com"
        ), "domain name starting with multiple dashes shouldn't validate"
        assert not self.__validator.isValid(
            "c--.com"
        ), "domain name ending with multiple dashes shouldn't validate"
        assert not self.__validator.isValid(
            "apache.rog"
        ), "domain name with invalid TLD shouldn't validate"

        assert not self.__validator.isValid(
            "http://www.apache.org"
        ), "URL shouldn't validate"
        assert not self.__validator.isValid(
            " "
        ), "Empty string shouldn't validate as domain name"
        assert not self.__validator.isValid(
            None
        ), "Null shouldn't validate as domain name"

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
        lowerCase = DomainValidatorTest.__isLowerCase(array[-1])  # Check the last entry

        for i in range(length - 1):  # compare all but last entry with next
            entry = array[i]
            nextEntry = array[i + 1]
            cmp = (entry > nextEntry) - (
                entry < nextEntry
            )  # Python's equivalent of Java's compareTo

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

        f = getattr(DomainValidator, arrayName)
        isPrivate = inspect.isprivate(f)
        if isPrivate:
            f.setAccessible(True)
        array = f.get(None)
        try:
            return DomainValidatorTest.__isSortedLowerCase1(arrayName, array)
        finally:
            if isPrivate:
                f.setAccessible(False)

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

        f = getattr(DomainValidator, arrayName)
        isPrivate = inspect.isprivate(f)
        if isPrivate:
            f = getattr(DomainValidator, "_" + arrayName)
        array = f()
        try:
            return DomainValidatorTest.__isInIanaList1(arrayName, array, ianaTlds)
        finally:
            if isPrivate:
                f = getattr(DomainValidator, arrayName)

    @staticmethod
    def __closeQuietly(in_: Closeable) -> None:
        if in_ is not None:
            try:
                in_.close()
            except IOError:
                pass

    @staticmethod
    def __isNotInRootZone(domain: str) -> bool:

        tldurl = "http://www.iana.org/domains/root/db/" + domain + ".html"
        rootCheck = pathlib.Path("target", "tld_" + domain + ".html")
        in_ = None
        try:
            DomainValidatorTest.__download(rootCheck, tldurl, 0)
            in_ = io.open(rootCheck, "r")
            for inputLine in in_:
                if (
                    "This domain is not present in the root zone at this time."
                    in inputLine
                ):
                    return True
            in_.close()
        except IOError:
            pass
        finally:
            DomainValidatorTest.__closeQuietly(in_)
        return False

    @staticmethod
    def __download(f: pathlib.Path, tldurl: str, timestamp: int) -> int:

        HOUR = 60 * 60 * 1000  # an hour in ms
        if f.exists() and os.access(f, os.R_OK):
            modTime = os.path.getmtime(f)
            if modTime > (time.time() * 1000 - HOUR):
                print("Skipping download - found recent " + str(f))
                return modTime
        else:
            modTime = 0

        hc = urllib.request.urlopen(tldurl)
        if modTime > 0:
            sdf = datetime.datetime.fromtimestamp(modTime / 1e3).strftime(
                "%a, %d %b %Y %H:%M:%S %Z"
            )
            hc.addheaders = [("If-Modified-Since", sdf)]
            print("Found " + str(f) + " with date " + sdf)

        if hc.getcode() == 304:
            print("Already have most recent " + tldurl)
        else:
            print("Downloading " + tldurl)
            buff = bytearray(1024)
            is_ = hc.read(buff)

            with open(f, "wb") as fos:
                while len(is_) != 0:
                    fos.write(buff)
                    is_ = hc.read(buff)
            print("Done")

        return os.path.getmtime(f)

    @staticmethod
    def __getHtmlInfo(f: pathlib.Path) -> typing.Dict[str, typing.List[str]]:

        info = {}

        domain = re.compile('.*<a href="/domains/root/db/([^.]+)\\.html')
        type_re = re.compile("\\s+<td>([^<]+)</td>")
        comment = re.compile("\\s+<td>([^<]+)</td>")

        with open(f, "r") as br:
            for line in br:
                m = domain.match(line)
                if m:
                    dom = m.group(1)
                    typ = "??"
                    com = "??"
                    line = next(br)
                    while line.strip() == "":  # extra blank lines introduced
                        line = next(br)
                    t = type_re.match(line)
                    if t:
                        typ = t.group(1)
                        line = next(br)
                        if line.strip().startswith("<!--"):
                            while not line.strip().endswith("-->"):
                                line = next(br)
                            line = next(br)
                        while not line.strip().endswith("</td>"):
                            line += " " + next(br)
                        n = comment.match(line)
                        if n:
                            com = n.group(1)
                        if "Not assigned" in com or "Retired" in com or typ == "test":
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

        for key, value in map.items():
            print('        "' + key + '", // ' + value)

        print("\nDone")
