from __future__ import annotations
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
        input: str = "a."  # must be a valid name
        return input == IDN.toASCII(input)


class Item:

    values: typing.List[str] = None

    type: ArrayType = None

    def __init__(self, type: ArrayType, values: typing.List[str]) -> None:
        self.type = type
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

    mylocalTLDsMinus: typing.List[str] = None

    mylocalTLDsPlus: typing.List[str] = None

    mygenericTLDsMinus: typing.List[str] = None

    mygenericTLDsPlus: typing.List[str] = None

    mycountryCodeTLDsPlus: typing.List[str] = None

    mycountryCodeTLDsMinus: typing.List[str] = None

    __localTLDsPlus: typing.List[str] = None
    __localTLDsMinus: typing.List[str] = None
    __genericTLDsMinus: typing.List[str] = None
    __countryCodeTLDsMinus: typing.List[str] = None
    __inUse: bool = False
    __LOCAL_TLDS: typing.List[str] = ["localdomain", "localhost"]
    __COUNTRY_CODE_TLDS: typing.List[str] = [
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
        "bj",
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
        "xn--mgbai9azgqp6j",
        "xn--mgbayh7gpa",
        "xn--mgbbh1a",
        "xn--mgbbh1a71e",
        "xn--mgbc0a9azcg",
        "xn--mgbcpq6gpa1a",
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
        "xn--qxa6a",
        "xn--qxam",
        "xn--rvc1e0am3e",
        "xn--s9brj9c",
        "xn--wgbh1c",
        "xn--wgbl6a",
        "xn--xkc2al3hye2a",
        "xn--xkc2dl3a5ee0h",
        "xn--y9a3aq",
        "xn--yfro4i67o",
        "xn--ygbi2ammx",
        "ye",
        "yt",
        "za",
        "zm",
        "zw",
    ]
    __GENERIC_TLDS: typing.List[str] = None  # LLM could not translate this field

    __INFRASTRUCTURE_TLDS: typing.List[str] = ["arpa"]
    __allowLocal: bool = False

    __UNEXPECTED_ENUM_VALUE: str = "Unexpected enum value: "
    __TOP_LABEL_REGEX: str = "\\p{Alpha}(?>[\\p{Alnum}-]{0,61}\\p{Alnum})?"
    __DOMAIN_LABEL_REGEX: str = "\\p{Alnum}(?>[\\p{Alnum}-]{0,61}\\p{Alnum})?"
    __serialVersionUID: int = -4407125112880174009
    __EMPTY_STRING_ARRAY: typing.List[str] = []
    __MAX_DOMAIN_LENGTH: int = 253
    __genericTLDsPlus: typing.List[str] = __EMPTY_STRING_ARRAY
    __countryCodeTLDsPlus: typing.List[str] = __EMPTY_STRING_ARRAY
    __hostnameRegex: RegexValidator = RegexValidator(__DOMAIN_LABEL_REGEX)
    __DOMAIN_NAME_REGEX: str = (
        f"^(?:{__DOMAIN_LABEL_REGEX}\\.)+({__TOP_LABEL_REGEX})\\.?$"
    )
    __domainRegex: RegexValidator = RegexValidator.RegexValidator3(__DOMAIN_NAME_REGEX)

    @staticmethod
    def unicodeToASCII(input: str) -> str:
        if DomainValidator.__isOnlyASCII(input):  # skip possibly expensive processing
            return input
        try:
            ascii = IDN.toASCII(input)
            if IDNBUGHOLDER.__IDN_TOASCII_PRESERVES_TRAILING_DOTS:
                return ascii
            length = len(input)
            if length == 0:  # check there is a last character
                return input
            lastChar = input[length - 1]  # fetch original last char
            if (
                lastChar == "\u002E"
                or lastChar == "\u3002"
                or lastChar == "\uFF0E"
                or lastChar == "\uFF61"
            ):
                return ascii + "."  # restore the missing stop
            else:
                return ascii
        except ValueError:  # input is not valid
            return input

    def getOverrides(self, table: ArrayType) -> typing.List[str]:
        array: typing.List[str]
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
            raise ValueError(self.__UNEXPECTED_ENUM_VALUE + table)
        return array.copy()  # clone the array

    @staticmethod
    def getTLDEntries(table: ArrayType) -> typing.List[str]:

        pass  # LLM could not translate this method

    @staticmethod
    def updateTLDOverride(table: ArrayType, tlds: typing.List[str]) -> None:
        if DomainValidator.__inUse:
            raise RuntimeError("Can only invoke this method before calling getInstance")
        copy: typing.List[str] = [None] * len(tlds)
        for i in range(len(tlds)):
            copy[i] = tlds[i].lower()
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
        elif (
            table == ArrayType.COUNTRY_CODE_RO
            or table == ArrayType.GENERIC_RO
            or table == ArrayType.INFRASTRUCTURE_RO
            or table == ArrayType.LOCAL_RO
        ):
            raise ValueError("Cannot update the table: " + table)
        else:
            raise ValueError(DomainValidator.__UNEXPECTED_ENUM_VALUE + table)

    def isAllowLocal(self) -> bool:
        return self.__allowLocal

    def isValidLocalTld(self, lTld: str) -> bool:
        key = self.__chompLeadingDot(DomainValidator.unicodeToASCII(lTld).lower())
        return (
            DomainValidator.__arrayContains(DomainValidator.__LOCAL_TLDS, key)
            or DomainValidator.__arrayContains(self.mylocalTLDsPlus, key)
        ) and not DomainValidator.__arrayContains(self.mylocalTLDsMinus, key)

    def isValidCountryCodeTld(self, ccTld: str) -> bool:
        key = self.__chompLeadingDot(DomainValidator.unicodeToASCII(ccTld).lower())
        return (
            DomainValidator.__arrayContains(DomainValidator.__COUNTRY_CODE_TLDS, key)
            or DomainValidator.__arrayContains(self.mycountryCodeTLDsPlus, key)
        ) and not DomainValidator.__arrayContains(self.mycountryCodeTLDsMinus, key)

    def isValidGenericTld(self, gTld: str) -> bool:

        pass  # LLM could not translate this method

    def isValidInfrastructureTld(self, iTld: str) -> bool:
        key = self.__chompLeadingDot(DomainValidator.unicodeToASCII(iTld).lower())
        return DomainValidator.__arrayContains(
            DomainValidator.__INFRASTRUCTURE_TLDS, key
        )

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
        domain = DomainValidator.unicodeToASCII(domain)
        if len(domain) > DomainValidator.__MAX_DOMAIN_LENGTH:
            return False
        groups = self.__domainRegex.match(domain)
        return (groups is not None and len(groups) > 0) or self.__hostnameRegex.isValid(
            domain
        )

    def isValid(self, domain: str) -> bool:
        if domain is None:
            return False
        domain = DomainValidator.unicodeToASCII(domain)
        if len(domain) > DomainValidator.__MAX_DOMAIN_LENGTH:
            return False
        groups = self.__domainRegex.match(domain)
        if groups is not None and len(groups) > 0:
            return self.isValidTld(groups[0])
        return self.__allowLocal and self.__hostnameRegex.isValid(domain)

    def __init__(
        self, constructorId: int, items: typing.List[Item], allowLocal: bool
    ) -> None:

        pass  # LLM could not translate this method

    @staticmethod
    def getInstance2(allowLocal: bool, items: typing.List[Item]) -> DomainValidator:
        DomainValidator.__inUse = True
        return DomainValidator(0, items, allowLocal)

    @staticmethod
    def getInstance1(allowLocal: bool) -> DomainValidator:
        DomainValidator.__inUse = True
        if allowLocal:
            return LazyHolder.__DOMAIN_VALIDATOR_WITH_LOCAL
        return LazyHolder.__DOMAIN_VALIDATOR

    @staticmethod
    def getInstance0() -> DomainValidator:
        DomainValidator.__inUse = True
        return LazyHolder.__DOMAIN_VALIDATOR

    @staticmethod
    def __arrayContains(sortedArray: typing.List[str], key: str) -> bool:
        return sortedArray.index(key) >= 0

    @staticmethod
    def __isOnlyASCII(input: str) -> bool:
        if input is None:
            return True
        for i in range(len(input)):
            if ord(input[i]) > 0x7F:
                return False
        return True

    def __chompLeadingDot(self, str: str) -> str:
        if str.startswith("."):
            return str[1:]
        return str


IDNBUGHOLDER.initialize_fields()

LazyHolder.initialize_fields()
