from __future__ import annotations
import time
import copy
import re
import enum
import io
import typing
from typing import *
import os
from src.main.org.apache.commons.validator.routines.RegexValidator import *


class ArrayType:

    LOCAL_MINUS: ArrayType = None

    LOCAL_PLUS: ArrayType = None

    LOCAL_RO: ArrayType = None

    INFRASTRUCTURE_RO: ArrayType = None

    COUNTRY_CODE_RO: ArrayType = None

    GENERIC_RO: ArrayType = None

    COUNTRY_CODE_MINUS: ArrayType = None

    COUNTRY_CODE_PLUS: ArrayType = None

    GENERIC_MINUS: ArrayType = None

    GENERIC_PLUS: ArrayType = None


class IDNBUGHOLDER:

    __IDN_TOASCII_PRESERVES_TRAILING_DOTS: bool = None

    @staticmethod
    def initialize_fields() -> None:
        IDNBUGHOLDER.__IDN_TOASCII_PRESERVES_TRAILING_DOTS: bool = (
            IDNBUGHOLDER.__keepsTrailingDot()
        )

    @staticmethod
    def __keepsTrailingDot() -> bool:

        input = "a."  # must be a valid name
        return input == IDN.toASCII(input)


class Item:

    values: typing.List[typing.List[str]] = None

    type: ArrayType = None

    def __init__(self, type_: ArrayType, values: typing.List[typing.List[str]]) -> None:
        self.type = type_
        self.values = values


class LazyHolder:

    __DOMAIN_VALIDATOR_WITH_LOCAL: DomainValidator = None
    __DOMAIN_VALIDATOR: DomainValidator = None

    @staticmethod
    def initialize_fields() -> None:
        LazyHolder.__DOMAIN_VALIDATOR_WITH_LOCAL: DomainValidator = DomainValidator(
            1, None, True
        )

        LazyHolder.__DOMAIN_VALIDATOR: DomainValidator = DomainValidator(1, None, False)


class DomainValidator:

    mylocalTLDsMinus: typing.List[typing.List[str]] = None

    mylocalTLDsPlus: typing.List[typing.List[str]] = None

    mygenericTLDsMinus: typing.List[typing.List[str]] = None

    mygenericTLDsPlus: typing.List[typing.List[str]] = None

    mycountryCodeTLDsPlus: typing.List[typing.List[str]] = None

    mycountryCodeTLDsMinus: typing.List[typing.List[str]] = None

    __localTLDsPlus: typing.List[str] = []
    __localTLDsMinus: typing.List[str] = []
    __genericTLDsMinus: List[str] = []
    __countryCodeTLDsMinus: typing.List[str] = []
    __genericTLDsPlus: List[str] = []
    __countryCodeTLDsPlus: typing.List[str] = []
    __inUse: bool = False
    __LOCAL_TLDS: List[str] = ["localdomain", "localhost"]
    __COUNTRY_CODE_TLDS: List[str] = [
        "ac",
        "ad",
        "ae",
        "af",
        "ag",
        "ai",
        "al",
        "am",
        "ao",
        "aq",
        "ar",
        "as",
        "at",
        "au",
        "aw",
        "ax",
        "az",
        "ba",
        "bb",
        "bd",
        "be",
        "bf",
        "bg",
        "bh",
        "bi",
        "bm",
        "bn",
        "bo",
        "br",
        "bs",
        "bt",
        "bv",
        "bw",
        "by",
        "bz",
        "ca",
        "cc",
        "cd",
        "cf",
        "cg",
        "ch",
        "ci",
        "ck",
        "cl",
        "cm",
        "cn",
        "co",
        "cr",
        "cu",
        "cv",
        "cw",
        "cx",
        "cy",
        "cz",
        "de",
        "dj",
        "dk",
        "dm",
        "do",
        "dz",
        "ec",
        "ee",
        "eg",
        "er",
        "es",
        "et",
        "eu",
        "fi",
        "fj",
        "fk",
        "fm",
        "fo",
        "fr",
        "ga",
        "gb",
        "gd",
        "ge",
        "gf",
        "gg",
        "gh",
        "gi",
        "gl",
        "gm",
        "gn",
        "gp",
        "gq",
        "gr",
        "gs",
        "gt",
        "gu",
        "gw",
        "gy",
        "hk",
        "hm",
        "hn",
        "hr",
        "ht",
        "hu",
        "id",
        "ie",
        "il",
        "im",
        "in",
        "io",
        "iq",
        "ir",
        "is",
        "it",
        "je",
        "jm",
        "jo",
        "jp",
        "ke",
        "kg",
        "kh",
        "ki",
        "km",
        "kn",
        "kp",
        "kr",
        "kw",
        "ky",
        "kz",
        "la",
        "lb",
        "lc",
        "li",
        "lk",
        "lr",
        "ls",
        "lt",
        "lu",
        "lv",
        "ly",
        "ma",
        "mc",
        "md",
        "me",
        "mg",
        "mh",
        "mk",
        "ml",
        "mm",
        "mn",
        "mo",
        "mp",
        "mq",
        "mr",
        "ms",
        "mt",
        "mu",
        "mv",
        "mw",
        "mx",
        "my",
        "mz",
        "na",
        "nc",
        "ne",
        "nf",
        "ng",
        "ni",
        "nl",
        "no",
        "np",
        "nr",
        "nu",
        "nz",
        "om",
        "pa",
        "pe",
        "pf",
        "pg",
        "ph",
        "pk",
        "pl",
        "pm",
        "pn",
        "pr",
        "ps",
        "pt",
        "pw",
        "py",
        "qa",
        "re",
        "ro",
        "rs",
        "ru",
        "rw",
        "sa",
        "sb",
        "sc",
        "sd",
        "se",
        "sg",
        "sh",
        "si",
        "sj",
        "sk",
        "sl",
        "sm",
        "sn",
        "so",
        "sr",
        "ss",
        "st",
        "su",
        "sv",
        "sx",
        "sy",
        "sz",
        "tc",
        "td",
        "tf",
        "tg",
        "th",
        "tj",
        "tk",
        "tl",
        "tm",
        "tn",
        "to",
        "tr",
        "tt",
        "tv",
        "tw",
        "tz",
        "ua",
        "ug",
        "uk",
        "us",
        "uy",
        "uz",
        "va",
        "vc",
        "ve",
        "vg",
        "vi",
        "vn",
        "vu",
        "wf",
        "ws",
        "xn--2scrj9c",
        "xn--3e0b707e",
        "xn--3hcrj9c",
        "xn--45br5cyl",
        "xn--45brj9c",
        "xn--54b7fta0cc",
        "xn--80ao21a",
        "xn--90a3ac",
        "xn--90ais",
        "xn--clchc0ea0b2g2a9gcd",
        "xn--d1alf",
        "xn--e1a4c",
        "xn--fiqs8s",
        "xn--fiqz9s",
        "xn--fpcrj9c3d",
        "xn--fzc2c9e2c",
        "xn--gecrj9c",
        "xn--h2breg3eve",
        "xn--h2brj9c",
        "xn--h2brj9c8c",
        "xn--j1amh",
        "xn--j6w193g",
        "xn--kprw13d",
        "xn--kpry57d",
        "xn--l1acc",
        "xn--lgbbat1ad8j",
        "xn--mgb9awbf",
        "xn--mgba3a4f16a",
        "xn--mgbaam7a8h",
        "xn--mgbah1a3hjkrd",
        "xn--mgbayh7gpa",
        "xn--mgbbh1a",
        "xn--mgbbh1a71e",
        "xn--mgbc0a9azcg",
        "xn--mgbcpq6gpa1a",
        "xn--mgberp4a5d4ar",
        "xn--mgbgu82a",
        "xn--mgbpl2fh",
        "xn--mgbtx2b",
        "xn--mgbx4cd0ab",
        "xn--mix891f",
        "xn--node",
        "xn--o3cw4h",
        "xn--ogbpf8fl",
        "xn--p1ai",
        "xn--pgbs0dh",
        "xn--q7ce6a",
        "xn--qxam",
        "xn--rvc1e0am3e",
        "xn--s9brj9c",
        "xn--wgbh1c",
        "xn--wgbl6a",
        "xn--xkc2al3hye2a",
        "xn--xkc2dl3a5ee0h",
        "xn--y9a3aq",
        "xn--yfro4i67o",
        "ye",
        "yt",
        "za",
        "zm",
        "zw",
    ]
    __GENERIC_TLDS: typing.List[typing.List[str]] = (
        None  # LLM could not translate this field
    )

    __INFRASTRUCTURE_TLDS: List[str] = ["arpa"]
    __DOMAIN_LABEL_REGEX: str = r"\p{Alnum}(?>[\p{Alnum}-]{0,61}\p{Alnum})?"
    __allowLocal: bool = False

    __UNEXPECTED_ENUM_VALUE: str = "Unexpected enum value: "
    __TOP_LABEL_REGEX: str = r"\p{Alpha}(?>[\p{Alnum}-]{0,61}\p{Alnum})?"
    __serialVersionUID: int = -4407125112880174009
    __EMPTY_STRING_ARRAY: List[str] = []
    __MAX_DOMAIN_LENGTH: int = 253

    __DOMAIN_NAME_REGEX: str = None  # LLM could not translate this field

    @staticmethod
    def unicodeToASCII(input_: str) -> str:

        if DomainValidator.__isOnlyASCII(input_):  # skip possibly expensive processing
            return input_

        try:
            ascii_ = input_.encode("idna").decode("utf-8")
            if IDNBUGHOLDER.__IDN_TOASCII_PRESERVES_TRAILING_DOTS:
                return ascii_

            length = len(input_)
            if length == 0:  # check there is a last character
                return input_

            lastChar = input_[-1]  # fetch original last char
            if lastChar in [
                ".",
                "\u3002",
                "\uFF0E",
                "\uFF61",
            ]:  # ".", ideographic full stop, fullwidth full stop, halfwidth ideographic full stop
                return ascii_ + "."  # restore the missing stop
            else:
                return ascii_
        except Exception:  # input is not valid
            return input_

    def getOverrides(self, table: ArrayType) -> typing.List[typing.List[str]]:

        if table == ArrayType.COUNTRY_CODE_MINUS:
            array = self.mycountryCodeTLDsMinus
        elif table == ArrayType.COUNTRY_CODE_PLUS:
            array = self.mycountryCodeTLDsPlus
        elif table == ArrayType.GENERIC_MINUS:
            array = self.mygenericTLDsMinus
        elif table == ArrayType.GENERIC_PLUS:
            array = self.mygenericTLDsPlus
        elif table == ArrayType.LOCAL_MINUS:
            array = self.mylocalTLDsMinus
        elif table == ArrayType.LOCAL_PLUS:
            array = self.mylocalTLDsPlus
        else:
            raise ValueError(self.__UNEXPECTED_ENUM_VALUE + str(table))

        return array.copy()  # clone the array

    @staticmethod
    def getTLDEntries(table: ArrayType) -> typing.List[typing.List[str]]:

        pass  # LLM could not translate this method

    @staticmethod
    def updateTLDOverride(
        table: ArrayType, tlds: typing.List[typing.List[str]]
    ) -> None:

        if DomainValidator.__inUse:
            raise RuntimeError("Can only invoke this method before calling getInstance")

        copy = [tld.lower() for tld in tlds]
        copy.sort()

        if table == ArrayType.COUNTRY_CODE_MINUS:
            DomainValidator.__countryCodeTLDsMinus = copy
        elif table == ArrayType.COUNTRY_CODE_PLUS:
            DomainValidator.__countryCodeTLDsPlus = copy
        elif table == ArrayType.GENERIC_MINUS:
            DomainValidator.__genericTLDsMinus = copy
        elif table == ArrayType.GENERIC_PLUS:
            DomainValidator.__genericTLDsPlus = copy
        elif table == ArrayType.LOCAL_MINUS:
            DomainValidator.__localTLDsMinus = copy
        elif table == ArrayType.LOCAL_PLUS:
            DomainValidator.__localTLDsPlus = copy
        elif table in [
            ArrayType.COUNTRY_CODE_RO,
            ArrayType.GENERIC_RO,
            ArrayType.INFRASTRUCTURE_RO,
            ArrayType.LOCAL_RO,
        ]:
            raise ValueError("Cannot update the table: " + table)
        else:
            raise ValueError(DomainValidator.__UNEXPECTED_ENUM_VALUE + table)

    def isAllowLocal(self) -> bool:
        return self.__allowLocal

    def isValidLocalTld(self, lTld: str) -> bool:

        key = self.__chompLeadingDot(self.unicodeToASCII(lTld).lower())
        return (
            self.__arrayContains(self.__LOCAL_TLDS, key)
            or self.__arrayContains(self.mylocalTLDsPlus, key)
        ) and not self.__arrayContains(self.mylocalTLDsMinus, key)

    def isValidCountryCodeTld(self, ccTld: str) -> bool:

        key = self.__chompLeadingDot(self.unicodeToASCII(ccTld).lower())
        return (
            self.__arrayContains(self.__COUNTRY_CODE_TLDS, key)
            or self.__arrayContains(self.mycountryCodeTLDsPlus, key)
        ) and not self.__arrayContains(self.mycountryCodeTLDsMinus, key)

    def isValidGenericTld(self, gTld: str) -> bool:

        pass  # LLM could not translate this method

    def isValidInfrastructureTld(self, iTld: str) -> bool:

        key = self.__chompLeadingDot(self.unicodeToASCII(iTld).lower())
        return self.__arrayContains(self.__INFRASTRUCTURE_TLDS, key)

    def isValidTld(self, tld: str) -> bool:

        if self.__allowLocal and self.isValidLocalTld(tld):
            return True
        return (
            self.isValidInfrastructureTld(tld)
            or self.isValidGenericTld(tld)
            or self.isValidCountryCodeTld(tld)
        )

    def isValidDomainSyntax(self, domain: str) -> bool:

        if domain is None:
            return False

        domain = self.unicodeToASCII(domain)

        if len(domain) > self.__MAX_DOMAIN_LENGTH:
            return False

        groups = self.__domainRegex.match(domain)

        return (groups is not None and len(groups) > 0) or self.__hostnameRegex.isValid(
            domain
        )

    def isValid(self, domain: str) -> bool:

        if domain is None:
            return False
        domain = self.unicodeToASCII(domain)
        if len(domain) > self.__MAX_DOMAIN_LENGTH:
            return False
        groups = self.__domainRegex.match(domain)
        if groups is not None and len(groups) > 0:
            return self.isValidTld(groups[0])
        return self.__allowLocal and self.__hostnameRegex.isValid(domain)

    def __init__(
        self, constructorId: int, items: typing.List[Item], allowLocal: bool
    ) -> None:

        self.__allowLocal = allowLocal

        ccMinus = self.__countryCodeTLDsMinus
        ccPlus = self.__countryCodeTLDsPlus
        genMinus = self.__genericTLDsMinus
        genPlus = self.__genericTLDsPlus
        localMinus = self.__localTLDsMinus
        localPlus = self.__localTLDsPlus

        for item in items:
            copy = [value.lower() for value in item.values]
            copy.sort()
            if item.type == ArrayType.COUNTRY_CODE_MINUS:
                ccMinus = copy
            elif item.type == ArrayType.COUNTRY_CODE_PLUS:
                ccPlus = copy
            elif item.type == ArrayType.GENERIC_MINUS:
                genMinus = copy
            elif item.type == ArrayType.GENERIC_PLUS:
                genPlus = copy
            elif item.type == ArrayType.LOCAL_MINUS:
                localMinus = copy
            elif item.type == ArrayType.LOCAL_PLUS:
                localPlus = copy

        self.mycountryCodeTLDsMinus = ccMinus
        self.mycountryCodeTLDsPlus = ccPlus
        self.mygenericTLDsMinus = genMinus
        self.mygenericTLDsPlus = genPlus
        self.mylocalTLDsMinus = localMinus
        self.mylocalTLDsPlus = localPlus

    @staticmethod
    def getInstance2(allowLocal: bool, items: typing.List[Item]) -> DomainValidator:

        DomainValidator.__inUse = True
        return DomainValidator(0, items, allowLocal)

    @staticmethod
    def getInstance1(allowLocal: bool) -> DomainValidator:

        DomainValidator.__inUse = True

        if allowLocal:
            return LazyHolder.__DOMAIN_VALIDATOR_WITH_LOCAL
        else:
            return LazyHolder.__DOMAIN_VALIDATOR

    @staticmethod
    def getInstance0() -> DomainValidator:
        DomainValidator.__inUse = True
        return LazyHolder.__DOMAIN_VALIDATOR

    @staticmethod
    def __arrayContains(sortedArray: typing.List[typing.List[str]], key: str) -> bool:

        # Flatten the list of lists into a single list
        flat_list = [item for sublist in sortedArray for item in sublist]

        # Use binary search to find the key in the sorted array
        return DomainValidator.__binary_search(flat_list, key) >= 0

    @staticmethod
    def __isOnlyASCII(input_: str) -> bool:

        if input_ is None:
            return True

        for i in range(len(input_)):
            if ord(input_[i]) > 0x7F:
                return False

        return True

    def __chompLeadingDot(self, str_: str) -> str:
        if str_.startswith("."):
            return str_[1:]
        return str_


IDNBUGHOLDER.initialize_fields()

LazyHolder.initialize_fields()
