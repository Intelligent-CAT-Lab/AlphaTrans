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
import enum
from src.main.org.apache.commons.validator.routines.DomainValidator import *


class DomainValidatorTest(unittest.TestCase):

    __validator: DomainValidator = None

    def setUp(self) -> None:
        self.__validator = DomainValidator.getInstance0()

    @staticmethod
    def main(a: typing.List[typing.List[str]]) -> None:

        OK = True
        for list_ in [
            "INFRASTRUCTURE_TLDS",
            "COUNTRY_CODE_TLDS",
            "GENERIC_TLDS",
            "LOCAL_TLDS",
        ]:
            OK &= DomainValidatorTest.__isSortedLowerCase0(list_)
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

            for line in br:
                if not line.startswith("#"):
                    unicodeTld = ""  # only different from asciiTld if that was punycode
                    asciiTld = line.lower()
                    if line.startswith("XN--"):
                        unicodeTld = IDN.toUnicode(line)
                    else:
                        unicodeTld = asciiTld

                    if not dv.isValidTld(asciiTld):
                        info = htmlInfo.get(asciiTld)
                        if info is not None:
                            type_ = info[0]
                            comment = info[1]
                            if "country-code" == type_:  # Which list to use?
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
                    if generateUnicodeTlds and unicodeTld != asciiTld:
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

        # Check if the enum is public
        self.assertTrue(inspect.isclass(DomainValidator.ArrayType))
        self.assertTrue(inspect.isclass(DomainValidator.DomainType))
        self.assertTrue(inspect.isclass(DomainValidator.IPType))
        self.assertTrue(inspect.isclass(DomainValidator.InetAddressValidator))
        self.assertTrue(inspect.isclass(DomainValidator.PublicSuffixType))

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
            ".",  # fails IDN.toASCII, but should pass wrapped version
            "a.",  # ditto
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

        self.validator = DomainValidator()

        self.assertTrue(
            self.validator.isValidDomainSyntax("a"), "a (alpha) should validate"
        )
        self.assertTrue(
            self.validator.isValidDomainSyntax("9"), "9 (alphanum) should validate"
        )
        self.assertTrue(
            self.validator.isValidDomainSyntax("c-z"),
            "c-z (alpha - alpha) should validate",
        )

        self.assertFalse(
            self.validator.isValidDomainSyntax("c-"), "c- (alpha -) should fail"
        )
        self.assertFalse(
            self.validator.isValidDomainSyntax("-c"), "-c (- alpha) should fail"
        )
        self.assertFalse(self.validator.isValidDomainSyntax("-"), "- (-) should fail")

    def testRFC2396toplabel(self) -> None:

        validator = DomainValidator()

        self.assertTrue(validator.isValidDomainSyntax("a.c"))
        self.assertTrue(validator.isValidDomainSyntax("a.cc"))
        self.assertTrue(validator.isValidDomainSyntax("a.c9"))
        self.assertTrue(validator.isValidDomainSyntax("a.c-9"))
        self.assertTrue(validator.isValidDomainSyntax("a.c-z"))

        self.assertFalse(validator.isValidDomainSyntax("a.9c"))
        self.assertFalse(validator.isValidDomainSyntax("a.c-"))
        self.assertFalse(validator.isValidDomainSyntax("a.-"))
        self.assertFalse(validator.isValidDomainSyntax("a.-9"))

    def testRFC2396domainlabel(self) -> None:

        self.assertTrue(self.__validator.isValid("a.ch"))
        self.assertTrue(self.__validator.isValid("9.ch"))
        self.assertTrue(self.__validator.isValid("az.ch"))
        self.assertTrue(self.__validator.isValid("09.ch"))
        self.assertTrue(self.__validator.isValid("9-1.ch"))
        self.assertFalse(self.__validator.isValid("91-.ch"))
        self.assertFalse(self.__validator.isValid("-.ch"))

    def testIDNJava6OrLater(self) -> None:

        version = platform.python_version()
        if version.split(".")[0] < "3":
            print("Cannot run Unicode IDN tests")
            return  # Cannot run the test

        self.assertTrue(
            self.__validator.isValid("www.b�cher.ch"), "b�cher.ch should validate"
        )
        self.assertTrue(
            self.__validator.isValid("xn--d1abbgf6aiiy.xn--p1ai"),
            "xn--d1abbgf6aiiy.xn--p1ai should validate",
        )
        self.assertTrue(
            self.__validator.isValid("президент.рф"), "президент.рф should validate"
        )
        self.assertFalse(
            self.__validator.isValid("www.\uFFFD.ch"), "www.\uFFFD.ch FFFD should fail"
        )

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

        self.validator = DomainValidator()

        self.assertTrue(
            self.validator.isValidInfrastructureTld(".arpa"),
            ".arpa should validate as iTLD",
        )
        self.assertFalse(
            self.validator.isValidInfrastructureTld(".com"),
            ".com shouldn't validate as iTLD",
        )

        self.assertTrue(
            self.validator.isValidGenericTld(".name"), ".name should validate as gTLD"
        )
        self.assertFalse(
            self.validator.isValidGenericTld(".us"), ".us shouldn't validate as gTLD"
        )

        self.assertTrue(
            self.validator.isValidCountryCodeTld(".uk"), ".uk should validate as ccTLD"
        )
        self.assertFalse(
            self.validator.isValidCountryCodeTld(".org"),
            ".org shouldn't validate as ccTLD",
        )

        self.assertTrue(
            self.validator.isValidTld(".COM"), ".COM should validate as TLD"
        )
        self.assertTrue(
            self.validator.isValidTld(".BiZ"), ".BiZ should validate as TLD"
        )

        self.assertFalse(
            self.validator.isValid(".nope"), "invalid TLD shouldn't validate"
        )
        self.assertFalse(
            self.validator.isValid(""), "empty string shouldn't validate as TLD"
        )
        self.assertFalse(self.validator.isValid(None), "null shouldn't validate as TLD")

    def testInvalidDomains(self) -> None:

        self.validator = DomainValidator()

        self.assertFalse(
            self.validator.isValid(".org"), "bare TLD .org shouldn't validate"
        )
        self.assertFalse(
            self.validator.isValid(" apache.org "),
            "domain name with spaces shouldn't validate",
        )
        self.assertFalse(
            self.validator.isValid("apa che.org"),
            "domain name containing spaces shouldn't validate",
        )
        self.assertFalse(
            self.validator.isValid("-testdomain.name"),
            "domain name starting with dash shouldn't validate",
        )
        self.assertFalse(
            self.validator.isValid("testdomain-.name"),
            "domain name ending with dash shouldn't validate",
        )
        self.assertFalse(
            self.validator.isValid("---c.com"),
            "domain name starting with multiple dashes shouldn't validate",
        )
        self.assertFalse(
            self.validator.isValid("c--.com"),
            "domain name ending with multiple dashes shouldn't validate",
        )
        self.assertFalse(
            self.validator.isValid("apache.rog"),
            "domain name with invalid TLD shouldn't validate",
        )

        self.assertFalse(
            self.validator.isValid("http://www.apache.org"), "URL shouldn't validate"
        )
        self.assertFalse(
            self.validator.isValid(" "),
            "Empty string shouldn't validate as domain name",
        )
        self.assertFalse(
            self.validator.isValid(None), "Null shouldn't validate as domain name"
        )

    def testValidDomains(self) -> None:

        self.__validator = DomainValidator()

        self.assertTrue(self.__validator.isValid("apache.org"))
        self.assertTrue(self.__validator.isValid("www.google.com"))

        self.assertTrue(self.__validator.isValid("test-domain.com"))
        self.assertTrue(self.__validator.isValid("test---domain.com"))
        self.assertTrue(self.__validator.isValid("test-d-o-m-ain.com"))
        self.assertTrue(self.__validator.isValid("as.uk"))

        self.assertTrue(self.__validator.isValid("ApAchE.Org"))

        self.assertTrue(self.__validator.isValid("z.com"))

        self.assertTrue(self.__validator.isValid("i.have.an-example.domain.name"))

    @staticmethod
    def __isSortedLowerCase1(name: str, array: typing.List[typing.List[str]]) -> bool:

        sorted = True
        strictlySorted = True
        length = len(array)
        lowerCase = DomainValidatorTest.__isLowerCase(
            array[length - 1]
        )  # Check the last entry

        for i in range(length - 1):  # compare all but last entry with next
            entry = array[i]
            nextEntry = array[i + 1]
            cmp = entry.compareTo(nextEntry)

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
        name: str, array: typing.List[typing.List[str]], ianaTlds: typing.Set[str]
    ) -> bool:

        for i in range(len(array)):
            for j in range(len(array[i])):
                if array[i][j] not in ianaTlds:
                    print(name + " contains unexpected value: " + array[i][j])

        return True

    @staticmethod
    def __isInIanaList0(arrayName: str, ianaTlds: typing.Set[str]) -> bool:

        f = DomainValidator.__dict__[arrayName]
        isPrivate = inspect.isprivate(f)
        if isPrivate:
            f.setAccessible(True)
        array = f.get(None)
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
                    while re.match("^\\s*$", line):  # extra blank lines introduced
                        line = next(br)
                    t = type_re.match(line)
                    if t:
                        typ = t.group(1)
                        line = next(br)
                        if re.match("\\s+<!--.*", line):
                            while not re.match(".*-->.*", line):
                                line = next(br)
                            line = next(br)
                        while not re.match(".*</td>.*", line):
                            line += " " + next(br)
                        n = comment.match(line)
                        if n:
                            com = n.group(1)
                        if (
                            com.contains("Not assigned")
                            or com.contains("Retired")
                            or typ.equals("test")
                        ):
                            pass
                        else:
                            info[dom.lower()] = [typ, com]
                    else:
                        print("Unexpected type: " + line)
        return info

    @staticmethod
    def __printMap(header: str, map_: typing.Dict[str, str], string: str) -> None:

        print("Entries missing from " + string + " List\n")

        if header is not None:
            print("        // Taken from " + header)

        for key, value in map_.items():
            print('        "' + key + '", // ' + value)

        print("\nDone")
