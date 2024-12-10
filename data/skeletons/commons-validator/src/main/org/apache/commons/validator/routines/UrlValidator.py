from __future__ import annotations

# Imports Begin
from src.main.org.apache.commons.validator.routines.RegexValidator import *
from src.main.org.apache.commons.validator.routines.DomainValidator import *
from src.main.org.apache.commons.validator.util.Flags import *
from src.main.org.apache.commons.validator.routines.InetAddressValidator import *
from src.main.org.apache.commons.validator.GenericValidator import *
import typing
from typing import *
import io
import pathlib

# Imports End


class UrlValidator:

    # Class Fields Begin
    __SCHEME_REGEX: str = None
    __SCHEME_PATTERN: re.Pattern = None
    __AUTHORITY_CHARS_REGEX: str = None
    __IPV6_REGEX: str = None
    __USERINFO_CHARS_REGEX: str = None
    __USERINFO_FIELD_REGEX: str = None
    __AUTHORITY_REGEX: str = None
    __AUTHORITY_PATTERN: re.Pattern = None
    __PARSE_AUTHORITY_IPV6: int = None
    __PARSE_AUTHORITY_HOST_IP: int = None
    __PARSE_AUTHORITY_PORT: int = None
    __PARSE_AUTHORITY_EXTRA: int = None
    __PATH_REGEX: str = None
    __PATH_PATTERN: re.Pattern = None
    __QUERY_REGEX: str = None
    __QUERY_PATTERN: re.Pattern = None
    __options: int = None
    __allowedSchemes: typing.Set[str] = None
    __authorityValidator: RegexValidator = None
    __DEFAULT_SCHEMES: typing.List[typing.List[str]] = None
    __DEFAULT_URL_VALIDATOR: UrlValidator = None
    __domainValidator: DomainValidator = None
    __serialVersionUID: int = None
    __MAX_UNSIGNED_16_BIT_INT: int = None
    ALLOW_ALL_SCHEMES: int = None
    ALLOW_2_SLASHES: int = None
    NO_FRAGMENTS: int = None
    ALLOW_LOCAL_URLS: int = None
    # Class Fields End

    # Class Methods Begin
    def _countToken(self, token: str, target: str) -> int:
        pass

    def _isValidFragment(self, fragment: str) -> bool:
        pass

    def _isValidQuery(self, query: str) -> bool:
        pass

    def _isValidPath(self, path: str) -> bool:
        pass

    def _isValidAuthority(self, authority: str) -> bool:
        pass

    def _isValidScheme(self, scheme: str) -> bool:
        pass

    def isValid(self, value: str) -> bool:
        pass

    @staticmethod
    def UrlValidator6() -> UrlValidator:
        pass

    @staticmethod
    def UrlValidator5(schemes: typing.List[typing.List[str]]) -> UrlValidator:
        pass

    @staticmethod
    def UrlValidator4(options: int) -> UrlValidator:
        pass

    @staticmethod
    def UrlValidator3(
        schemes: typing.List[typing.List[str]], options: int
    ) -> UrlValidator:
        pass

    @staticmethod
    def UrlValidator2(authorityValidator: RegexValidator, options: int) -> UrlValidator:
        pass

    @staticmethod
    def UrlValidator1(
        schemes: typing.List[typing.List[str]],
        authorityValidator: RegexValidator,
        options: int,
    ) -> UrlValidator:
        pass

    def __init__(
        self,
        schemes: typing.List[typing.List[str]],
        authorityValidator: RegexValidator,
        options: int,
        domainValidator: DomainValidator,
    ) -> None:
        pass

    @staticmethod
    def getInstance() -> UrlValidator:
        pass

    def __isOff(self, flag: int) -> bool:
        pass

    @staticmethod
    def __isOn1(flag: int, options: int) -> bool:
        pass

    def __isOn0(self, flag: int) -> bool:
        pass

    # Class Methods End
