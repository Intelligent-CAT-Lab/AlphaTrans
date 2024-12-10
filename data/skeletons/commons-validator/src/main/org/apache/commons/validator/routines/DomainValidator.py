from __future__ import annotations

# Imports Begin
from src.main.org.apache.commons.validator.routines.RegexValidator import *
import os
import typing
from typing import *
import io

# Imports End


class ArrayType:

    # Class Fields Begin
    GENERIC_PLUS: ArrayType = None
    GENERIC_MINUS: ArrayType = None
    COUNTRY_CODE_PLUS: ArrayType = None
    COUNTRY_CODE_MINUS: ArrayType = None
    GENERIC_RO: ArrayType = None
    COUNTRY_CODE_RO: ArrayType = None
    INFRASTRUCTURE_RO: ArrayType = None
    LOCAL_RO: ArrayType = None
    LOCAL_PLUS: ArrayType = None
    LOCAL_MINUS: ArrayType = None
    # Class Fields End

    # Class Methods Begin
    # Class Methods End


class IDNBUGHOLDER:

    # Class Fields Begin
    __IDN_TOASCII_PRESERVES_TRAILING_DOTS: bool = None
    # Class Fields End

    # Class Methods Begin
    @staticmethod
    def __keepsTrailingDot() -> bool:
        pass

    # Class Methods End


class Item:

    # Class Fields Begin
    type: ArrayType = None
    values: typing.List[typing.List[str]] = None
    # Class Fields End

    # Class Methods Begin
    def __init__(self, type_: ArrayType, values: typing.List[typing.List[str]]) -> None:
        pass

    # Class Methods End


class LazyHolder:

    # Class Fields Begin
    __DOMAIN_VALIDATOR: DomainValidator = None
    __DOMAIN_VALIDATOR_WITH_LOCAL: DomainValidator = None
    # Class Fields End

    # Class Methods Begin
    # Class Methods End


class DomainValidator:

    # Class Fields Begin
    mycountryCodeTLDsMinus: typing.List[typing.List[str]] = None
    mycountryCodeTLDsPlus: typing.List[typing.List[str]] = None
    mygenericTLDsPlus: typing.List[typing.List[str]] = None
    mygenericTLDsMinus: typing.List[typing.List[str]] = None
    mylocalTLDsPlus: typing.List[typing.List[str]] = None
    mylocalTLDsMinus: typing.List[typing.List[str]] = None
    __COUNTRY_CODE_TLDS: typing.List[typing.List[str]] = None
    __LOCAL_TLDS: typing.List[typing.List[str]] = None
    __inUse: bool = None
    __countryCodeTLDsPlus: typing.List[typing.List[str]] = None
    __genericTLDsPlus: typing.List[typing.List[str]] = None
    __countryCodeTLDsMinus: typing.List[typing.List[str]] = None
    __genericTLDsMinus: typing.List[typing.List[str]] = None
    __localTLDsMinus: typing.List[typing.List[str]] = None
    __localTLDsPlus: typing.List[typing.List[str]] = None
    __INFRASTRUCTURE_TLDS: typing.List[typing.List[str]] = None
    __GENERIC_TLDS: typing.List[typing.List[str]] = None
    __MAX_DOMAIN_LENGTH: int = None
    __EMPTY_STRING_ARRAY: typing.List[typing.List[str]] = None
    __serialVersionUID: int = None
    __DOMAIN_LABEL_REGEX: str = None
    __TOP_LABEL_REGEX: str = None
    __DOMAIN_NAME_REGEX: str = None
    __UNEXPECTED_ENUM_VALUE: str = None
    __allowLocal: bool = None
    __domainRegex: RegexValidator = None
    __hostnameRegex: RegexValidator = None
    # Class Fields End

    # Class Methods Begin
    @staticmethod
    def unicodeToASCII(input_: str) -> str:
        pass

    def getOverrides(self, table: ArrayType) -> typing.List[typing.List[str]]:
        pass

    @staticmethod
    def getTLDEntries(table: ArrayType) -> typing.List[typing.List[str]]:
        pass

    @staticmethod
    def updateTLDOverride(
        table: ArrayType, tlds: typing.List[typing.List[str]]
    ) -> None:
        pass

    def isAllowLocal(self) -> bool:
        pass

    def isValidLocalTld(self, lTld: str) -> bool:
        pass

    def isValidCountryCodeTld(self, ccTld: str) -> bool:
        pass

    def isValidGenericTld(self, gTld: str) -> bool:
        pass

    def isValidInfrastructureTld(self, iTld: str) -> bool:
        pass

    def isValidTld(self, tld: str) -> bool:
        pass

    def isValidDomainSyntax(self, domain: str) -> bool:
        pass

    def isValid(self, domain: str) -> bool:
        pass

    def __init__(
        self, constructorId: int, items: typing.List[Item], allowLocal: bool
    ) -> None:
        pass

    @staticmethod
    def getInstance2(allowLocal: bool, items: typing.List[Item]) -> DomainValidator:
        pass

    @staticmethod
    def getInstance1(allowLocal: bool) -> DomainValidator:
        pass

    @staticmethod
    def getInstance0() -> DomainValidator:
        pass

    @staticmethod
    def __arrayContains(sortedArray: typing.List[typing.List[str]], key: str) -> bool:
        pass

    @staticmethod
    def __isOnlyASCII(input_: str) -> bool:
        pass

    def __chompLeadingDot(self, str_: str) -> str:
        pass

    # Class Methods End
