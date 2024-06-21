from src.main.org.apache.commons.validator.routines.DomainValidator import *
import unittest
import sys
import re
import os
import datetime
import urllib.request as request

class DomainValidatorTest(unittest.TestCase):

    def __init__(self, methodName='runTest') -> None:
        super().__init__(methodName)
        self.__validator = None

    def setUp(self) -> None:
        self.__validator = DomainValidator.getInstance0()

    
    def test_ValidDomains(self) -> None:
        self.assertTrue(
            self.__validator.isValid("apache.org"),
            "apache.org should validate"
        )
        self.assertTrue(
            self.__validator.isValid("www.google.com"),
            "www.google.com should validate"
        )

        self.assertTrue(
            self.__validator.isValid("test-domain.com"),
            "test-domain.com should validate"
        )
        self.assertTrue(
            self.__validator.isValid("test---domain.com"),
            "test---domain.com should validate"
        )
        self.assertTrue(
            self.__validator.isValid("test-d-o-m-ain.com"),
            "test-d-o-m-ain.com should validate"
        )
        self.assertTrue(
            self.__validator.isValid("as.uk"),
            "two-letter domain label should validate"
        )

        self.assertTrue(
            self.__validator.isValid("ApAchE.Org"),
            "case-insensitive ApAchE.Org should validate"
        )

        self.assertTrue(
            self.__validator.isValid("z.com"),
            "single-character domain label should validate"
        )

        self.assertTrue(
            self.__validator.isValid("i.have.an-example.domain.name"),
            "i.have.an-example.domain.name should validate"
        )

    
    def test_InvalidDomains(self) -> None:
        self.assertFalse(
            self.__validator.isValid(".org"),
            "bare TLD .org shouldn't validate"
        )
        self.assertFalse(
            self.__validator.isValid(" apache.org "),
            "domain name with spaces shouldn't validate"
        )
        self.assertFalse(
            self.__validator.isValid("apa che.org"),
            "domain name containing spaces shouldn't validate"
        )
        self.assertFalse(
            self.__validator.isValid("-testdomain.name"),
            "domain name starting with dash shouldn't validate"
        )
        self.assertFalse(
            self.__validator.isValid("testdomain-.name"),
            "domain name ending with dash shouldn't validate"
        )
        self.assertFalse(
            self.__validator.isValid("---c.com"),
            "domain name starting with multiple dashes shouldn't validate"
        )
        self.assertFalse(
            self.__validator.isValid("c--.com"),
            "domain name ending with multiple dashes shouldn't validate"
        )
        self.assertFalse(
            self.__validator.isValid("apache.rog"),
            "domain name with invalid TLD shouldn't validate"
        )

        self.assertFalse(
            self.__validator.isValid("http://www.apache.org"),
            "URL shouldn't validate"
        )
        self.assertFalse(
            self.__validator.isValid(" "),
            "Empty string shouldn't validate as domain name"
        )
        self.assertFalse(
            self.__validator.isValid(None),
            "Null shouldn't validate as domain name"
        )

    
    def test_TopLevelDomains(self) -> None:
        self.assertTrue(
            self.__validator.isValidInfrastructureTld(".arpa"),
            ".arpa should validate as iTLD"
        )
        self.assertFalse(
            self.__validator.isValidInfrastructureTld(".com"),
            ".com shouldn't validate as iTLD"
        )

        self.assertTrue(
            self.__validator.isValidGenericTld(".name"),
            ".name should validate as gTLD"
        )
        self.assertFalse(
            self.__validator.isValidGenericTld(".us"),
            ".us shouldn't validate as gTLD"
        )

        self.assertTrue(
            self.__validator.isValidCountryCodeTld(".uk"),
            ".uk should validate as ccTLD"
        )
        self.assertFalse(
            self.__validator.isValidCountryCodeTld(".org"),
            ".org shouldn't validate as ccTLD"
        )

        self.assertTrue(
            self.__validator.isValidTld(".COM"),
            ".COM should validate as TLD"
        )
        self.assertTrue(
            self.__validator.isValidTld(".BiZ"),
            ".BiZ should validate as TLD"
        )

        self.assertFalse(
            self.__validator.isValid(".nope"),
            "invalid TLD shouldn't validate"
        )
        self.assertFalse(
            self.__validator.isValid(""),
            "empty string shouldn't validate as TLD"
        )
        self.assertFalse(
            self.__validator.isValid(None),
            "null shouldn't validate as TLD"
        )

    
    def test_AllowLocal(self) -> None:
        noLocal = DomainValidator.getInstance1(False)
        allowLocal = DomainValidator.getInstance1(True)

        self.assertEqual(noLocal, self.__validator)

        self.assertFalse(
            noLocal.isValid("localhost.localdomain"),
            "localhost.localdomain shouldn't validate"
        )
        self.assertFalse(noLocal.isValid("localhost"), "localhost shouldn't validate")

        self.assertTrue(
            allowLocal.isValid("localhost.localdomain"),
            "localhost.localdomain should validate"
        )
        self.assertTrue(allowLocal.isValid("localhost"), "localhost should validate")
        self.assertTrue(allowLocal.isValid("hostname"), "hostname should validate")
        self.assertTrue(allowLocal.isValid("machinename"), "machinename should validate")
        self.assertTrue(allowLocal.isValid("apache.org"), "apache.org should validate")

        self.assertFalse(
            allowLocal.isValid(" apache.org "),
            "domain name with spaces shouldn't validate"
        )

    
    def test_IDN(self) -> None:
        self.assertTrue(
            self.__validator.isValid("www.xn--bcher-kva.ch"),
            "b\u00fccher.ch in IDN should validate"
        )

    
    def test_IDNJava6OrLater(self) -> None:
        version = sys.version_info
        if version < (2, 6): 
            #Python 2.6 is the latest version available at the birth of Java 1.6
            print("Cannot run Unicode IDN tests")
            return
        self.assertTrue(
            self.__validator.isValid("www.b\u00fccher.ch"),
            "b\u00fccher.ch should validate"
        )
        self.assertTrue(
            self.__validator.isValid("xn--d1abbgf6aiiy.xn--p1ai"),
            "xn--d1abbgf6aiiy.xn--p1ai should validate"
        )
        self.assertTrue(
            self.__validator.isValid("президент.рф"),
            "президент.рф should validate"
        )
        self.assertFalse(
            self.__validator.isValid("www.\uFFFD.ch"),
            "www.\uFFFD.ch FFFD should fail"
        )

    
    def test_RFC2396domainlabel(self) -> None:
        self.assertTrue(self.__validator.isValid("a.ch"), "a.ch should validate")
        self.assertTrue(self.__validator.isValid("9.ch"), "9.ch should validate")
        self.assertTrue(self.__validator.isValid("az.ch"), "az.ch should validate")
        self.assertTrue(self.__validator.isValid("09.ch"), "09.ch should validate")
        self.assertTrue(self.__validator.isValid("9-1.ch"), "9-1.ch should validate")
        self.assertFalse(self.__validator.isValid("91-.ch"), "91-.ch should not validate")
        self.assertFalse(self.__validator.isValid("-.ch"), "-.ch should not validate")

    
    def test_RFC2396toplabel(self) -> None:
        self.assertTrue(
            self.__validator.isValidDomainSyntax("a.c"),
            "a.c (alpha) should validate"
        )
        self.assertTrue(
            self.__validator.isValidDomainSyntax("a.cc"),
            "a.cc (alpha alpha) should validate"
        )
        self.assertTrue(
            self.__validator.isValidDomainSyntax("a.c9"),
            "a.c9 (alpha alphanum) should validate"
        )
        self.assertTrue(
            self.__validator.isValidDomainSyntax("a.c-9"),
            "a.c-9 (alpha - alphanum) should validate"
        )
        self.assertTrue(
            self.__validator.isValidDomainSyntax("a.c-z"),
            "a.c-z (alpha - alpha) should validate"
        )

        self.assertFalse(
            self.__validator.isValidDomainSyntax("a.9c"),
            "a.9c (alphanum alpha) should fail"
        )
        self.assertFalse(
            self.__validator.isValidDomainSyntax("a.c-"),
            "a.c- (alpha -) should fail"
        )
        self.assertFalse(
            self.__validator.isValidDomainSyntax("a.-"),
            "a.- (-) should fail"
        )
        self.assertFalse(
            self.__validator.isValidDomainSyntax("a.-9"),
            "a.-9 (- alphanum) should fail"
        )

    
    def test_DomainNoDots(self) -> None:
        self.assertTrue(
            self.__validator.isValidDomainSyntax("a"),
            "a (alpha) should validate"
        )
        self.assertTrue(
            self.__validator.isValidDomainSyntax("9"),
            "9 (alphanum) should validate"
        )
        self.assertTrue(
            self.__validator.isValidDomainSyntax("c-z"),
            "c-z (alpha - alpha) should validate"
        )

        self.assertFalse(
            self.__validator.isValidDomainSyntax("c-"),
            "c- (alpha -) should fail"
        )
        self.assertFalse(
            self.__validator.isValidDomainSyntax("-c"),
            "-c (- alpha) should fail"
        )
        self.assertFalse(
            self.__validator.isValidDomainSyntax("-"),
            "- (-) should fail"
        )

    
    def test_Validator297(self) -> None:
        self.assertTrue(
            self.__validator.isValid("xn--d1abbgf6aiiy.xn--p1ai"),
            "xn--d1abbgf6aiiy.xn--p1ai should validate"
        )

    
    def test_Validator306(self) -> None:
        longString = "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz0123456789A"
        self.assertEqual(len(longString), 63)
        
        self.assertTrue(
            self.__validator.isValidDomainSyntax(longString + ".com"),
            "63 chars label should validate"
        )
        self.assertFalse(
            self.__validator.isValidDomainSyntax(longString + "x.com"),
            "64 chars label should fail"
        )

        self.assertTrue(
            self.__validator.isValidDomainSyntax("test." + longString),
            "63 chars TLD should validate"
        )
        self.assertFalse(
            self.__validator.isValidDomainSyntax("test.x" + longString),
            "64 chars TLD should fail"
        )

        long_domain = longString + "." + longString + "." + longString + "." + longString[:61]
        self.assertEqual(len(long_domain), 253)
        self.assertTrue(
            self.__validator.isValidDomainSyntax(long_domain),
            "253 chars domain should validate"
        )
        self.assertFalse(
            self.__validator.isValidDomainSyntax(long_domain + "x"),
            "254 chars domain should fail"
        )

    
    def test_UnicodeToASCII(self) -> None:
        asciidots = [
            "", ",", ".", # fails IDNA.toASCII, but should pass wrapped version
            "a.", # ditto
            "a.b", "a..b", "a...b", ".a", "..a",
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

    
    def test_IsIDNtoASCIIBroken(self) -> None:
        print(">>DomainValidatorTest.testIsIDNtoASCIIBroken()")
        input_str = "."
        try:
            ok = input_str == input_str.encode('ascii').decode('ascii')
        except Exception:
            ok = False
        print("toASCII is " + ("OK" if ok else "BROKEN"))
        
        props = [
            "java.version", "java.vendor", "java.vm.specification.version",
            "java.vm.specification.vendor", "java.vm.specification.name",
            "java.vm.version", "java.vm.vendor", "java.vm.name",
            "java.specification.version", "java.specification.vendor",
            "java.specification.name", "java.class.version",
        ]
        
        for t in props:
            print(f"{t}={getattr(sys, t, 'N/A')}")
        print("<<DomainValidatorTest.testIsIDNtoASCIIBroken()")
        self.assertTrue(True)

    
    def test_INFRASTRUCTURE_TLDS_sortedAndLowerCase(self) -> None:
        try:
            sorted = self.__isSortedLowerCase0("INFRASTRUCTURE_TLDS")
            self.assertTrue(sorted)
        except Exception as e:
            self.fail(f"An exception occurred: {e}")

    
    def test_COUNTRY_CODE_TLDS_sortedAndLowerCase(self) -> None:
        try:
            sorted = self.__isSortedLowerCase0("COUNTRY_CODE_TLDS")
            self.assertTrue(sorted)
        except Exception as e:
            self.fail(f"An exception occurred: {e}")

    
    def test_GENERIC_TLDS_sortedAndLowerCase(self) -> None:
        try:
            sorted = self.__isSortedLowerCase0("GENERIC_TLDS")
            self.assertTrue(sorted)
        except Exception as e:
            self.fail(f"An exception occurred: {e}")

    
    def test_LOCAL_TLDS_sortedAndLowerCase(self) -> None:
        try:
            sorted = self.__isSortedLowerCase0("LOCAL_TLDS")
            self.assertTrue(sorted)
        except Exception as e:
            self.fail(f"An exception occurred: {e}")

    
    def test_EnumIsPublic(self) -> None:
        self.assertTrue(hasattr(DomainValidator, 'ArrayType'))

    
    def test_GetArray(self) -> None:
        self.assertIsNotNone(
            DomainValidator.getTLDEntries(DomainValidator.ArrayType.COUNTRY_CODE_MINUS)
        )
        self.assertIsNotNone(
            DomainValidator.getTLDEntries(DomainValidator.ArrayType.COUNTRY_CODE_PLUS)
        )
        self.assertIsNotNone(
            DomainValidator.getTLDEntries(DomainValidator.ArrayType.GENERIC_MINUS)
        )
        self.assertIsNotNone(
            DomainValidator.getTLDEntries(DomainValidator.ArrayType.GENERIC_PLUS)
        )
        self.assertIsNotNone(
            DomainValidator.getTLDEntries(DomainValidator.ArrayType.LOCAL_MINUS)
        )
        self.assertIsNotNone(
            DomainValidator.getTLDEntries(DomainValidator.ArrayType.LOCAL_PLUS)
        )
        self.assertIsNotNone(
            DomainValidator.getTLDEntries(DomainValidator.ArrayType.COUNTRY_CODE_RO)
        )
        self.assertIsNotNone(
            DomainValidator.getTLDEntries(DomainValidator.ArrayType.GENERIC_RO)
        )
        self.assertIsNotNone(
            DomainValidator.getTLDEntries(DomainValidator.ArrayType.INFRASTRUCTURE_RO)
        )
        self.assertIsNotNone(
            DomainValidator.getTLDEntries(DomainValidator.ArrayType.LOCAL_RO)
        )
    

    @staticmethod
    def main(a) -> None:
        try:
            OK = True
            for list_ in [
                "INFRASTRUCTURE_TLDS",
                "COUNTRY_CODE_TLDS",
                "GENERIC_TLDS",
                "LOCAL_TLDS"
            ]:
                OK = OK and DomainValidatorTest.__isSortedLowerCase0(list_)

            if not OK:
                print("Fix arrays before retrying; cannot continue")
                return

            ianaTlds = set()  # keep for comparison with array contents
            dv = DomainValidator.getInstance0()

            txtFile = "target/tlds-alpha-by-domain.txt"
            timestamp = DomainValidatorTest\
                .__download(txtFile, "https://data.iana.org/TLD/tlds-alpha-by-domain.txt", 0)
            htmlFile = "target/tlds-alpha-by-domain.html"
            DomainValidatorTest\
                .__download(htmlFile, "https://www.iana.org/domains/root/db", timestamp)

            with open(txtFile, 'r', encoding='utf-8') as br:
                line = br.readline()  # header
                if line.startswith("# Version "):
                    header = line[2:]
                else:
                    raise IOError("File does not have expected Version header")

                generateUnicodeTlds = False
                
                htmlInfo = DomainValidatorTest.__getHtmlInfo(htmlFile)
                missingTLD = {}  # stores entry and comments as String[]
                missingCC = {}

                for line in br:
                    if not line.startswith("#"):
                        asciiTld = line.strip().lower()
                        if line.startswith("XN--"):
                            unicodeTld = line.lower().encode().decode('idna')
                        else:
                            unicodeTld = asciiTld

                        if not dv.isValidTld(asciiTld):
                            info = htmlInfo.get(asciiTld)
                            if info:
                                type_, comment = info
                                if type_ == "country-code":
                                    missingCC[asciiTld] = f"{unicodeTld} {comment}"
                                    if generateUnicodeTlds:
                                        missingCC[unicodeTld] = f"{unicodeTld} {comment}"
                                else:
                                    missingTLD[asciiTld] = f"{asciiTld} {comment}"
                                    if generateUnicodeTlds:
                                        missingTLD[unicodeTld] = f"{asciiTld} {comment}"
                            else:
                                print(
                                    f"Expected to find HTML info for {asciiTld}", file=sys.stderr
                                )

                        ianaTlds.add(asciiTld)
                        if generateUnicodeTlds:
                            if unicodeTld != asciiTld:
                                ianaTlds.add(unicodeTld)

            for key in sorted(htmlInfo.keys()):
                if key not in ianaTlds:
                    if DomainValidatorTest.__isNotInRootZone(key):
                        print(f"INFO: HTML entry not yet in root zone: {key}")
                    else:
                        print(f"WARN: Expected to find text entry for html: {key}", file=sys.stderr)

            if missingTLD:
                DomainValidatorTest.__printMap(header, missingTLD, "TLD")
            if missingCC:
                DomainValidatorTest.__printMap(header, missingCC, "CC")

            DomainValidatorTest.__isInIanaList0("INFRASTRUCTURE_TLDS", ianaTlds)
            DomainValidatorTest.__isInIanaList0("COUNTRY_CODE_TLDS", ianaTlds)
            DomainValidatorTest.__isInIanaList0("GENERIC_TLDS", ianaTlds)
            print("Finished checks")
        except Exception as e:
            DomainValidatorTest.fail(f"An exception occurred: {e}")

    
    @staticmethod
    def __printMap(header, map_, string):
        print(f"Entries missing from {string} List\n")
        if header:
            print(f"        // Taken from {header}")
        for key, value in map_.items():
            print(f"        \"{key}\", // {value}")
        print("\nDone")

    
    @staticmethod
    def __getHtmlInfo(file):
        try:
            info = {}
            domainPattern = re.compile(r'.*<a href="/domains/root/db/([^.]+)\.html')
            typePattern = re.compile(r'\s+<td>([^<]+)</td>')
            commentPattern = re.compile(r'\s+<td>([^<]+)</td>')

            with open(file, 'r', encoding='utf-8') as br:
                for line in br:
                    domainMatch = domainPattern.match(line)
                    if domainMatch:
                        dom = domainMatch.group(1)
                        typ = "??"
                        com = "??"
                        line = next(br).strip()
                        while not line:
                            line = next(br).strip()
                        typeMatch = typePattern.match(line)
                        if typeMatch:
                            typ = typeMatch.group(1)
                            line = next(br)
                            if re.match(r'\s+<!--.*', line):
                                while not re.match(r'.*-->.*', line):
                                    line = next(br)
                                line = next(br)
                            while not re.match(r'.*</td>.*', line):
                                line += " " + next(br)
                            commentMatch = commentPattern.match(line)
                            if commentMatch:
                                com = commentMatch.group(1)
                            if "Not assigned" not in com\
                                and "Retired" not in com and typ != "test":
                                info[dom.lower()] = (typ, com)
                        else:
                            print(f"Unexpected type: {line}", file=sys.stderr)
            return info
        except (IOError, OSError) as e:
            DomainValidatorTest.fail(f"An exception occurred: {e}")

    
    @staticmethod
    def __download(file, url, timestamp):
        try:
            HOUR = 60 * 60 * 1000  # an hour in ms
            modTime = 0
            if os.path.exists(file):
                modTime = os.path.getmtime(file)
                if modTime > (datetime.now().timestamp() * 1000) - HOUR:
                    print(f"Skipping __download - found recent {file}")
                    return modTime

            req = request.Request(url)
            if modTime > 0:
                since = datetime.utcfromtimestamp(modTime / 1000)\
                    .strftime("%a, %d %b %Y %H:%M:%S GMT")
                req.add_header("If-Modified-Since", since)
                print(f"Found {file} with date {since}")

            try:
                with request.urlopen(req) as response:
                    if response.status == 304:
                        print(f"Already have most recent {url}")
                    else:
                        print(f"downloading {url}")
                        with open(file, 'wb') as out_file:
                            out_file.write(response.read())
                        print("Done")
            except Exception as e:
                print(f"Error downloading {url}: {e}", file=sys.stderr)
                raise

            return os.path.getmtime(file)
        except (IOError, OSError) as e:
            DomainValidatorTest.fail(f"An exception occurred: {e}")

    
    @staticmethod
    def __isNotInRootZone(domain):
        tldurl = f"http://www.iana.org/domains/root/db/{domain}.html"
        rootCheck = f"target/tld_{domain}.html"
        try:
            DomainValidatorTest.__download(rootCheck, tldurl, 0)
            with open(rootCheck, 'r', encoding='utf-8') as f:
                for line in f:
                    if "This domain is not present in the root zone at this time." in line:
                        return True
        except IOError:
            pass
        return False

    
    @staticmethod
    def __isInIanaList0(arrayName, ianaTlds):
        try:
            array = getattr(DomainValidator, arrayName)
            return DomainValidatorTest.__isInIanaList1(arrayName, array, ianaTlds)
        except (IOError, OSError) as e:
            DomainValidatorTest.fail(f"An exception occurred: {e}")

    
    @staticmethod
    def __isInIanaList1(name, array, ianaTlds):
        for entry in array:
            if entry not in ianaTlds:
                print(f"{name} contains unexpected value: {entry}")
        return True

    
    @staticmethod
    def __isSortedLowerCase0(arrayName):
        try:
            array = getattr(DomainValidator, arrayName)
            return DomainValidatorTest.__isSortedLowerCase1(arrayName, array)
        except Exception as e:
            DomainValidatorTest.fail(f"An exception occurred: {e}")

    
    @staticmethod
    def __isLowerCase(string):
        return string == string.lower()

    
    @staticmethod
    def __isSortedLowerCase1(name, array):
        sorted_ = True
        strictlySorted = True
        length = len(array)
        lowerCase = DomainValidatorTest\
            .__isLowerCase(array[length - 1])  # Check the last entry
        for i in range(length - 1):
            entry = array[i]
            nextEntry = array[i + 1]
            cmp = (entry > nextEntry) - (entry < nextEntry)
            if cmp > 0:
                print(f"Out of order entry: {entry} < {nextEntry} in {name}")
                sorted_ = False
            elif cmp == 0:
                strictlySorted = False
                print(f"Duplicated entry: {entry} in {name}")
            if not DomainValidatorTest.__isLowerCase(entry):
                print(f"Non lowerCase entry: {entry} in {name}")
                lowerCase = False
        return sorted_ and strictlySorted and lowerCase
