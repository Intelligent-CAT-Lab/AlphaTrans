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
    __ATOM: str = None
    __URL_REGEX: str = None
    __URL_PATTERN: re.Pattern = None
    __PARSE_URL_SCHEME: int = None
    __PARSE_URL_AUTHORITY: int = None
    __PARSE_URL_PATH: int = None
    __PARSE_URL_QUERY: int = None
    __PARSE_URL_FRAGMENT: int = None
    __SCHEME_PATTERN: re.Pattern = None
    __AUTHORITY_REGEX: str = None
    __AUTHORITY_PATTERN: re.Pattern = None
    __PARSE_AUTHORITY_HOST_IP: int = None
    __PARSE_AUTHORITY_PORT: int = None
    __PARSE_AUTHORITY_EXTRA: int = None
    __PATH_PATTERN: re.Pattern = None
    __QUERY_PATTERN: re.Pattern = None
    __LEGAL_ASCII_PATTERN: re.Pattern = None
    __DOMAIN_PATTERN: re.Pattern = None
    __PORT_PATTERN: re.Pattern = None
    __ATOM_PATTERN: re.Pattern = None
    __ALPHA_PATTERN: re.Pattern = None
    __options: Flags = None
    __allowedSchemes: typing.Set[str] = None
    _defaultSchemes: typing.List[typing.List[str]] = None
    __serialVersionUID: int = None
    ALLOW_ALL_SCHEMES: int = None
    ALLOW_2_SLASHES: int = None
    NO_FRAGMENTS: int = None
    __ALPHA_CHARS: str = None
    __SPECIAL_CHARS: str = None
    __VALID_CHARS: str = None
    __AUTHORITY_CHARS_REGEX: str = None
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
    def UrlValidator3() -> UrlValidator:
        pass

    @staticmethod
    def UrlValidator2(schemes: typing.List[typing.List[str]]) -> UrlValidator:
        pass

    @staticmethod
    def UrlValidator1(options: int) -> UrlValidator:
        pass

    def __init__(self, schemes: typing.List[typing.List[str]], options: int) -> None:
        pass

    # Class Methods End
