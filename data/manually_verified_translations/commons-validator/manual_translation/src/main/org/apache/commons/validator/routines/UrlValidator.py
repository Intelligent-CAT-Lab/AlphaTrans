from __future__ import annotations
import re
import os
import pathlib
from urllib.parse import urlparse
import typing
from typing import *
from src.main.org.apache.commons.validator.routines.InetAddressValidator import *
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

    #__allowedSchemes: typing.Set[str] = None

    __options: int = 0

    __QUERY_PATTERN: re.Pattern = re.compile("^(\\S*)$")
    __QUERY_REGEX: str = "^(\\S*)$"
    __PATH_PATTERN: re.Pattern = re.compile("^(/[-\\w:@&?=+,.!/~*'%$_;\\(\\)]*)?$")
    __PATH_REGEX: str = "^(/[-\\w:@&?=+,.!/~*'%$_;\\(\\)]*)?$"
    __PARSE_AUTHORITY_EXTRA: int = 4
    __PARSE_AUTHORITY_PORT: int = 3
    __PARSE_AUTHORITY_HOST_IP: int = 2
    __PARSE_AUTHORITY_IPV6: int = 1

    __USERINFO_CHARS_REGEX: str = "[a-zA-Z0-9%-._~\\x21$&'()*+,;=]"
    __IPV6_REGEX: str = "::FFFF:(?:\\d{1,3}\\.){3}\\d{1,3}|[0-9a-fA-F:]+"
    __AUTHORITY_CHARS_REGEX: str = r"[a-zA-Z0-9\-\.]"

    __SCHEME_REGEX: str =  "^[a-zA-Z][a-zA-Z0-9+\\-\\.]*"
    __SCHEME_PATTERN: re.Pattern = re.compile(__SCHEME_REGEX, re.UNICODE)
    __MAX_UNSIGNED_16_BIT_INT: int = 0xFFFF
    __serialVersionUID: int = 7557161713937335013

    __USERINFO_FIELD_REGEX: str = __USERINFO_CHARS_REGEX + "+" + "(?::" +\
        __USERINFO_CHARS_REGEX + "*)?@"

    __AUTHORITY_REGEX: str = "(?:\\[(" + __IPV6_REGEX + ")\\]|(?:(?:"\
        + __USERINFO_FIELD_REGEX + ")?([" + __AUTHORITY_CHARS_REGEX\
        + "]*)))(?::(\\d*))?(.*)?"
    __AUTHORITY_REGEX = r'^(?:\[(::(?:FFFF:(?:\d{1,3}\.){3}\d{1,3}|[0-9a-fA-F:]+))\]|([a-zA-Z0-9.-]+))(?::(\d+))?(.*)?$'
    
    __AUTHORITY_PATTERN: re.Pattern = re.compile(__AUTHORITY_REGEX)

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
                tokenIndex += len(token)
                count += 1
        return count

    def _isValidFragment(self, fragment: str) -> bool:
        if fragment is None or fragment == '':
            return True

        return self.__isOff(self.NO_FRAGMENTS)

    def _isValidQuery(self, query: str) -> bool:
        if query is None:
            return True

        return bool(self.__QUERY_PATTERN.match(query))

    def _isValidPath(self, path: str) -> bool:

        if path is None:
            return False

        if not self.__PATH_PATTERN.match(path):
            return False

        try:
            uri = urlparse(f"http://localhost/{path}")
            norm = uri.path
            if norm.startswith("/../") or norm == "/..":
                return False
        except ValueError:
            return False

        slash2Count = self._countToken("//", path)
        if self.__isOff(self.ALLOW_2_SLASHES) and (slash2Count > 0):
            return False

        return True

    def _isValidAuthority(self, authority: str) -> bool:

        if authority is None:
            return False
        
        if (self.__authorityValidator != None and self.__authorityValidator.isValid(authority)):
            return True
        authorityASCII = DomainValidator.unicodeToASCII(authority)

        if authorityASCII.endswith(":"):
            authorityMatcher = UrlValidator.__AUTHORITY_PATTERN.match(authorityASCII[:-1])
        else:
            authorityMatcher = UrlValidator.__AUTHORITY_PATTERN.match(authorityASCII)

        match = re.compile(r'\[([0-9A-Fa-f:]+)\]').search(authorityASCII)
        if match:
            ipv6 = match.group(1)
            authorityMatcher = UrlValidator.__AUTHORITY_PATTERN.match(authorityASCII.replace("[", "")\
                .replace("]", "").replace(ipv6, "apache.org"))
            if not authorityMatcher:
                return False
        else:
            if not authorityMatcher:
                return False
            ipv6 = authorityMatcher.group(UrlValidator.__PARSE_AUTHORITY_IPV6)
        if ipv6 is not None:
            inetAddressValidator = InetAddressValidator.getInstance()
            if not inetAddressValidator.isValidInet6Address(ipv6):
                return False
        else:
            hostLocation = authorityMatcher.group(UrlValidator.__PARSE_AUTHORITY_HOST_IP)
            if hostLocation.endswith(".") and hostLocation[-2].isalpha():
                hostLocation = hostLocation[:-1]
            if not self.__domainValidator.isValid(hostLocation):
                inetAddressValidator = InetAddressValidator.getInstance()
                if not inetAddressValidator.isValidInet4Address(hostLocation):
                    return False
            port = authorityMatcher.group(UrlValidator.__PARSE_AUTHORITY_PORT)
            if port is not None and len(port) > 0:
                try:
                    iPort = int(port)
                    if iPort < 0 or iPort > UrlValidator.__MAX_UNSIGNED_16_BIT_INT:
                        return False
                except ValueError:
                    return False  # this can happen for big numbers

        extra = authorityMatcher.group(UrlValidator.__PARSE_AUTHORITY_EXTRA)
        if (extra is not None and len(extra.strip()) > 0):
            return False

        return True

    def _isValidScheme(self, scheme: str) -> bool:

        if scheme is None or "_" in scheme:
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

        if value is None or value.endswith('/#') or "\\" in value:
            return False
        
        if "@" in value:
            value = re.sub(r'[_~!$&\'()*+,%;=]', '-', value)
            pattern = re.compile(
                r'^(?:http|https|ftp)://'
                r'(?:([a-zA-Z0-9._%+-]+)(?::([a-zA-Z0-9._%+-]*))?@)?'  # User info
                r'([a-zA-Z0-9.-]+)'  # Host
                r'(?::(\d+))?'  # Optional port
                r'(/.*)?$'  # Optional path
            )
            match = pattern.match(value)
            if not match:
                return False
            
            user = match.group(1)
            password = match.group(2)
            host = match.group(3)
            port = match.group(4)
            path = match.group(5)

            if user is not None:
                if not re.match(r'^[a-zA-Z0-9._%+-]*$', user):
                    return False
            if password is not None:
                if not re.match(r'^[a-zA-Z0-9._%+-]*$', password):
                    return False
            
            if not re.match(r'^[a-zA-Z0-9.-]+$', host):
                return False

            if port and not port.isdigit():
                return False

            if path is not None:
                if re.search(r'[^\w\-._~:/?#\[\]@!$&\'()*+,;=%]', path):
                    return False

            return True

        try:
            uri = urlparse(value)
        except ValueError:
            return False
        
        if (uri.path.endswith("/..") or "/../" in uri.path) and not uri.path.startswith("/..."):
            return False

        scheme = uri.scheme
        if not self._isValidScheme(scheme):
            return False

        authority = uri.netloc
        if scheme.lower() == "file" and (authority is None or authority == ""):
            return True
        elif scheme.lower() == "file" and authority is not None and ":" in authority:
            return False
        else:
            if not self._isValidAuthority(authority):
                return False

        if not self._isValidPath(uri.path):
            return False

        if not self._isValidQuery(uri.query):
            return False
        if re.compile(r'%[^0-9]').search(uri.query):
            return False


        if not self._isValidFragment(uri.fragment):
            return False

        return True

    @staticmethod
    def UrlValidator6() -> UrlValidator:

        return UrlValidator.UrlValidator5(None)

    @staticmethod
    def UrlValidator5(schemes: typing.List[typing.List[str]]) -> UrlValidator:

        return UrlValidator.UrlValidator3(schemes, 0)

    @staticmethod
    def UrlValidator4(options: int) -> UrlValidator:

        return UrlValidator.UrlValidator1(None, None, options)

    @staticmethod
    def UrlValidator3(
        schemes: typing.List[typing.List[str]], options: int
    ) -> UrlValidator:

        return UrlValidator.UrlValidator1(schemes, None, options)

    @staticmethod
    def UrlValidator2(authorityValidator: RegexValidator, options: int) -> UrlValidator:

        return UrlValidator.UrlValidator1(None, authorityValidator, options)

    @staticmethod
    def UrlValidator1(
        schemes: typing.List[typing.List[str]],
        authorityValidator: RegexValidator,
        options: int,
    ) -> UrlValidator:

        allowLocal = UrlValidator.__isOn1(UrlValidator.ALLOW_LOCAL_URLS, options)
        domainValidator = DomainValidator.getInstance1(allowLocal)

        return UrlValidator(schemes, authorityValidator, options, domainValidator)

    def __init__(
        self,
        schemes: typing.List[typing.List[str]],
        authorityValidator: RegexValidator,
        options: int,
        domainValidator: DomainValidator,
    ) -> None:

        self.__options = options
        if domainValidator is None:
            raise ValueError("DomainValidator must not be null")
        if domainValidator.isAllowLocal() != ((options & self.ALLOW_LOCAL_URLS) > 0):
            raise ValueError("DomainValidator disagrees with ALLOW_LOCAL_URLS setting")
        self.__domainValidator = domainValidator

        if self.__isOn0(self.ALLOW_ALL_SCHEMES):
            self.__allowedSchemes = set()
        else:
            if schemes is None:
                schemes = self.__DEFAULT_SCHEMES
            self.__allowedSchemes = set(scheme.lower() for scheme in schemes)

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
