from __future__ import annotations
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

    __IDN_TOASCII_PRESERVES_TRAILING_DOTS: bool = keepsTrailingDot()

    @staticmethod
    def __keepsTrailingDot() -> bool:

        input = "a."  # must be a valid name
        return input == IDN.toASCII(input)


class Item:

    values: typing.List[str] = None
    type: ArrayType = None

    def __init__(self, type: ArrayType, values: typing.List[str]) -> None:

        self.type = type
        self.values = values


class LazyHolder:

    __DOMAIN_VALIDATOR_WITH_LOCAL: DomainValidator = DomainValidator(1, None, True)

    __DOMAIN_VALIDATOR: DomainValidator = DomainValidator(1, None, False)


class DomainValidator:

    mylocalTLDsMinus: typing.List[str] = None
    mylocalTLDsPlus: typing.List[str] = None
    mygenericTLDsMinus: typing.List[str] = None
    mygenericTLDsPlus: typing.List[str] = None
    mycountryCodeTLDsPlus: typing.List[str] = None
    mycountryCodeTLDsMinus: typing.List[str] = None

    __localTLDsPlus: List[str] = []

    __localTLDsMinus: List[str] = []

    __genericTLDsMinus: List[str] = []

    __countryCodeTLDsMinus: List[str] = []

    __genericTLDsPlus: List[str] = []

    __countryCodeTLDsPlus: List[str] = []

    __inUse: bool = False

    __LOCAL_TLDS: typing.List[str] = ["localdomain", "localhost"]
    __COUNTRY_CODE_TLDS: typing.List[str] = None  # LLM could not translate this field
    __GENERIC_TLDS: typing.List[str] = None  # LLM could not translate this field

    __INFRASTRUCTURE_TLDS: typing.List[str] = ["arpa"]

    __hostnameRegex: RegexValidator = RegexValidator.RegexValidator3(DOMAIN_LABEL_REGEX)

    __domainRegex: RegexValidator = RegexValidator.RegexValidator3(DOMAIN_NAME_REGEX)
    __allowLocal: bool = None

    __UNEXPECTED_ENUM_VALUE: str = "Unexpected enum value: "

    __DOMAIN_NAME_REGEX: str = (
        "^(?:"
        + DomainValidator.__DOMAIN_LABEL_REGEX
        + "\\.)+"
        + "("
        + DomainValidator.__TOP_LABEL_REGEX
        + ")\\.?$"
    )

    __TOP_LABEL_REGEX: str = r"\p{Alpha}(?>[\p{Alnum}-]{0,61}\p{Alnum})?"

    __DOMAIN_LABEL_REGEX: str = r"\p{Alnum}(?>[\p{Alnum}-]{0,61}\p{Alnum})?"

    __serialVersionUID: int = -4407125112880174009

    __EMPTY_STRING_ARRAY: typing.List[str] = []

    __MAX_DOMAIN_LENGTH: int = 253

    @staticmethod
    def unicodeToASCII(input: str) -> str:

        if DomainValidator.__isOnlyASCII(input):  # skip possibly expensive processing
            return input

        try:
            ascii = input.encode("idna").decode("utf-8")
            if IDNBUGHOLDER.IDN_TOASCII_PRESERVES_TRAILING_DOTS:
                return ascii

            length = len(input)
            if length == 0:  # check there is a last character
                return input

            lastChar = input[length - 1]  # fetch original last char
            if lastChar in [
                ".",
                "\u3002",
                "\uFF0E",
                "\uFF61",
            ]:  # ".", ideographic full stop, fullwidth full stop, halfwidth ideographic full stop
                return ascii + "."  # restore the missing stop
            else:
                return ascii

        except Exception:  # input is not valid
            return input

    def getOverrides(self, table: ArrayType) -> typing.List[str]:

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
    def getTLDEntries(table: ArrayType) -> typing.List[str]:

        if table == ArrayType.COUNTRY_CODE_MINUS:
            array = DomainValidator.__countryCodeTLDsMinus
        elif table == ArrayType.COUNTRY_CODE_PLUS:
            array = DomainValidator.__countryCodeTLDsPlus
        elif table == ArrayType.GENERIC_MINUS:
            array = DomainValidator.__genericTLDsMinus
        elif table == ArrayType.GENERIC_PLUS:
            array = DomainValidator.__genericTLDsPlus
        elif table == ArrayType.LOCAL_MINUS:
            array = DomainValidator.__localTLDsMinus
        elif table == ArrayType.LOCAL_PLUS:
            array = DomainValidator.__localTLDsPlus
        elif table == ArrayType.GENERIC_RO:
            array = DomainValidator.__GENERIC_TLDS
        elif table == ArrayType.COUNTRY_CODE_RO:
            array = DomainValidator.__COUNTRY_CODE_TLDS
        elif table == ArrayType.INFRASTRUCTURE_RO:
            array = DomainValidator.__INFRASTRUCTURE_TLDS
        elif table == ArrayType.LOCAL_RO:
            array = DomainValidator.__LOCAL_TLDS
        else:
            raise ValueError(DomainValidator.__UNEXPECTED_ENUM_VALUE + str(table))

        return array.copy()  # clone the array

    @staticmethod
    def updateTLDOverride(table: ArrayType, tlds: typing.List[str]) -> None:

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
            raise ValueError("Cannot update the table: " + table.name)
        else:
            raise ValueError(DomainValidator.__UNEXPECTED_ENUM_VALUE + table.name)

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

        key = self.__chompLeadingDot(self.unicodeToASCII(gTld).lower())
        return (
            self.__arrayContains(self.__GENERIC_TLDS, key)
            or self.__arrayContains(self.mygenericTLDsPlus, key)
        ) and not self.__arrayContains(self.mygenericTLDsMinus, key)

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

        if constructorId == 0:

            self.allowLocal = allowLocal

            ccMinus = self.mycountryCodeTLDsMinus
            ccPlus = self.mycountryCodeTLDsPlus
            genMinus = self.mygenericTLDsMinus
            genPlus = self.mygenericTLDsPlus
            localMinus = self.mylocalTLDsMinus
            localPlus = self.mylocalTLDsPlus

            for item in items:
                copy = [i.lower() for i in item.values]
                copy.sort()
                if item.type == "COUNTRY_CODE_MINUS":
                    ccMinus = copy
                elif item.type == "COUNTRY_CODE_PLUS":
                    ccPlus = copy
                elif item.type == "GENERIC_MINUS":
                    genMinus = copy
                elif item.type == "GENERIC_PLUS":
                    genPlus = copy
                elif item.type == "LOCAL_MINUS":
                    localMinus = copy
                elif item.type == "LOCAL_PLUS":
                    localPlus = copy

            self.mycountryCodeTLDsMinus = ccMinus
            self.mycountryCodeTLDsPlus = ccPlus
            self.mygenericTLDsMinus = genMinus
            self.mygenericTLDsPlus = genPlus
            self.mylocalTLDsMinus = localMinus
            self.mylocalTLDsPlus = localPlus

        else:

            self.allowLocal = allowLocal
            self.mycountryCodeTLDsMinus = self.mycountryCodeTLDsMinus
            self.mycountryCodeTLDsPlus = self.mycountryCodeTLDsPlus
            self.mygenericTLDsPlus = self.mygenericTLDsPlus
            self.mygenericTLDsMinus = self.mygenericTLDsMinus
            self.mylocalTLDsPlus = self.mylocalTLDsPlus
            self.mylocalTLDsMinus = self.mylocalTLDsMinus

    @staticmethod
    def getInstance2(allowLocal: bool, items: typing.List[Item]) -> DomainValidator:

        DomainValidator.__inUse = True
        return DomainValidator(0, items, allowLocal)

    @staticmethod
    def getInstance1(allowLocal: bool) -> DomainValidator:

        DomainValidator.__inUse = True
        if allowLocal:
            return DomainValidator.LazyHolder.DOMAIN_VALIDATOR_WITH_LOCAL
        return DomainValidator.LazyHolder.DOMAIN_VALIDATOR

    @staticmethod
    def getInstance0() -> DomainValidator:

        DomainValidator.__inUse = True
        return DomainValidator.LazyHolder.DOMAIN_VALIDATOR

    @staticmethod
    def __arrayContains(sortedArray: typing.List[str], key: str) -> bool:

        # Python's bisect module provides support for maintaining a list in sorted order without having to sort the list after each insertion.
        import bisect

        i = bisect.bisect_left(sortedArray, key)
        if i != len(sortedArray) and sortedArray[i] == key:
            return True

        return False

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
