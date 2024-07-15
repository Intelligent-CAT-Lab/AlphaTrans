from __future__ import annotations
import re
import os
import pathlib
import io
import typing
from typing import *
from src.main.org.apache.commons.validator.GenericValidator import *
from src.main.org.apache.commons.validator.routines.InetAddressValidator import *
from src.main.org.apache.commons.validator.util.Flags import *
from src.main.org.apache.commons.validator.routines.DomainValidator import *
from src.main.org.apache.commons.validator.routines.RegexValidator import *


class UrlValidator:

    ALLOW_LOCAL_URLS: int = 1 << 3
    NO_FRAGMENTS: int = 1 << 2
    ALLOW_2_SLASHES: int = 1 << 1
    ALLOW_ALL_SCHEMES: int = 1 << 0
    __domainValidator: DomainValidator = None

    __DEFAULT_URL_VALIDATOR: UrlValidator = None
    __DEFAULT_SCHEMES: typing.List[str] = ["http", "https", "ftp"]
    __authorityValidator: RegexValidator = None

    __allowedSchemes: typing.Set[str] = None

    __options: int = 0

    __QUERY_REGEX: str = "^(\\S*)$"
    __PATH_REGEX: str = "^(/[-\\w:@&?=+,.!/~*'%$_;\\(\\)]*)?$"
    __PARSE_AUTHORITY_EXTRA: int = 4
    __PARSE_AUTHORITY_PORT: int = 3
    __PARSE_AUTHORITY_HOST_IP: int = 2
    __PARSE_AUTHORITY_IPV6: int = 1
    __AUTHORITY_REGEX: str = None  # LLM could not translate this field

    __USERINFO_CHARS_REGEX: str = "[a-zA-Z0-9%-._~!$&'()*+,;=]"
    __IPV6_REGEX: str = "::FFFF:(?:\\d{1,3}\\.){3}\\d{1,3}|[0-9a-fA-F:]+"
    __AUTHORITY_CHARS_REGEX: str = "\\p{Alnum}\\-\\."
    __SCHEME_REGEX: str = "^\\p{Alpha}[\\p{Alnum}\\+\\-\\.]*"
    __MAX_UNSIGNED_16_BIT_INT: int = 0xFFFF
    __serialVersionUID: int = 7557161713937335013
    __QUERY_PATTERN: re.Pattern = re.compile(__QUERY_REGEX)
    __PATH_PATTERN: re.Pattern = re.compile(__PATH_REGEX)
    __AUTHORITY_PATTERN: re.Pattern = re.compile(__AUTHORITY_REGEX)
    __USERINFO_FIELD_REGEX: str = (
        __USERINFO_CHARS_REGEX + "+" + "(?::" + __USERINFO_CHARS_REGEX + "*)?@"
    )
    __SCHEME_PATTERN: re.Pattern = re.compile(__SCHEME_REGEX)

    @staticmethod
    def initialize_fields() -> None:
        UrlValidator.__DEFAULT_URL_VALIDATOR: UrlValidator = (
            UrlValidator.UrlValidator6()
        )

    def _countToken(self, token: str, target: str) -> int:
        tokenIndex = 0
        count = 0
        while tokenIndex != -1:
            tokenIndex = target.find(token, tokenIndex)
            if tokenIndex > -1:
                tokenIndex += 1
                count += 1
        return count

    def _isValidFragment(self, fragment: str) -> bool:
        if fragment is None:
            return True

        return self.__isOff(UrlValidator.NO_FRAGMENTS)

    def _isValidQuery(self, query: str) -> bool:
        if query is None:
            return True

        return self.__QUERY_PATTERN.match(query) is not None

    def _isValidPath(self, path: str) -> bool:
        if path is None:
            return False

        if not self.__PATH_PATTERN.match(path):
            return False

        try:
            uri = URI(None, "localhost", path, None)
            norm = uri.normalize().getPath()
            if norm.startswith("/../") or norm == "/..":
                return False
        except URISyntaxException:
            return False

        slash2Count = self._countToken("//", path)
        if self.__isOff(self.ALLOW_2_SLASHES) and (slash2Count > 0):
            return False

        return True

    def _isValidAuthority(self, authority: str) -> bool:
        if authority is None:
            return False
        if self.__authorityValidator is not None and self.__authorityValidator.isValid(
            authority
        ):
            return True
        authorityASCII = DomainValidator.unicodeToASCII(authority)
        authorityMatcher = self.__AUTHORITY_PATTERN.match(authorityASCII)
        if authorityMatcher is None:
            return False
        ipv6 = authorityMatcher.group(self.__PARSE_AUTHORITY_IPV6)
        if ipv6 is not None:
            inetAddressValidator = InetAddressValidator.getInstance()
            if not inetAddressValidator.isValidInet6Address(ipv6):
                return False
        else:
            hostLocation = authorityMatcher.group(self.__PARSE_AUTHORITY_HOST_IP)
            if not self.__domainValidator.isValid(hostLocation):
                inetAddressValidator = InetAddressValidator.getInstance()
                if not inetAddressValidator.isValidInet4Address(hostLocation):
                    return False
            port = authorityMatcher.group(self.__PARSE_AUTHORITY_PORT)
            if port is not None and len(port) > 0:
                try:
                    iPort = int(port)
                    if iPort < 0 or iPort > self.__MAX_UNSIGNED_16_BIT_INT:
                        return False
                except ValueError:
                    return False
        extra = authorityMatcher.group(self.__PARSE_AUTHORITY_EXTRA)
        if extra is not None and len(extra.strip()) > 0:
            return False
        return True

    def _isValidScheme(self, scheme: str) -> bool:
        if scheme is None:
            return False

        if not self.__SCHEME_PATTERN.match(scheme):
            return False

        if (
            self.__isOff(self.ALLOW_ALL_SCHEMES)
            and scheme.lower() not in self.__allowedSchemes
        ):
            return False

        return True

    def isValid(self, value: str) -> bool:
        if value is None:
            return False

        uri = URI(value)  # ensure value is a valid URI
        scheme = uri.getScheme()
        if not self._isValidScheme(scheme):
            return False

        authority = uri.getRawAuthority()
        if "file" == scheme and (
            authority is None or authority == ""
        ):  # Special case - file: allows an empty
            return True  # this is a local file - nothing more to do here
        elif "file" == scheme and authority is not None and ":" in authority:
            return False
        else:
            if not self._isValidAuthority(authority):
                return False

        if not self._isValidPath(uri.getRawPath()):
            return False

        if not self._isValidQuery(uri.getRawQuery()):
            return False

        if not self._isValidFragment(uri.getRawFragment()):
            return False

        return True

    @staticmethod
    def UrlValidator6() -> UrlValidator:
        return UrlValidator.UrlValidator5(None)

    @staticmethod
    def UrlValidator5(schemes: typing.List[str]) -> UrlValidator:
        return UrlValidator.UrlValidator3(schemes, 0)

    @staticmethod
    def UrlValidator4(options: int) -> UrlValidator:
        return UrlValidator.UrlValidator1(None, None, options)

    @staticmethod
    def UrlValidator3(schemes: typing.List[str], options: int) -> UrlValidator:
        return UrlValidator.UrlValidator1(schemes, None, options)

    @staticmethod
    def UrlValidator2(authorityValidator: RegexValidator, options: int) -> UrlValidator:
        return UrlValidator1(None, authorityValidator, options)

    @staticmethod
    def UrlValidator1(
        schemes: typing.List[str], authorityValidator: RegexValidator, options: int
    ) -> UrlValidator:
        return UrlValidator(
            schemes,
            authorityValidator,
            options,
            DomainValidator.getInstance1(
                UrlValidator.__isOn1(UrlValidator.ALLOW_LOCAL_URLS, options)
            ),
        )

    def __init__(
        self,
        schemes: typing.List[str],
        authorityValidator: RegexValidator,
        options: int,
        domainValidator: DomainValidator,
    ) -> None:
        self.__options = options
        if domainValidator is None:
            raise ValueError("DomainValidator must not be null")
        if domainValidator.isAllowLocal() != self.__isOn0(ALLOW_LOCAL_URLS):
            raise ValueError("DomainValidator disagrees with ALLOW_LOCAL_URLS setting")
        self.__domainValidator = domainValidator

        if self.__isOn0(ALLOW_ALL_SCHEMES):
            self.__allowedSchemes = set()
        else:
            if schemes is None:
                schemes = self.__DEFAULT_SCHEMES
            self.__allowedSchemes = set(schemes)

        self.__authorityValidator = authorityValidator

    @staticmethod
    def getInstance() -> UrlValidator:
        return UrlValidator.__DEFAULT_URL_VALIDATOR

    def __isOff(self, flag: int) -> bool:
        return (self.__options & flag) == 0

    @staticmethod
    def __isOn1(flag: int, options: int) -> bool:
        return (options & flag) > 0

    def __isOn0(self, flag: int) -> bool:
        return (self.__options & flag) > 0


UrlValidator.initialize_fields()
