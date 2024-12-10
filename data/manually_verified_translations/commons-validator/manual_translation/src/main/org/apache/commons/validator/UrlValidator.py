from __future__ import annotations
import re
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

    _defaultSchemes: List[str] = ["http", "https", "ftp"]
    NO_FRAGMENTS: int = 1 << 2
    ALLOW_2_SLASHES: int = 1 << 1
    ALLOW_ALL_SCHEMES: int = 1 << 0
    __allowedSchemes: typing.Set[str] = set()
    __options: Flags = None

    __ALPHA_CHARS: str = "a-zA-Z"
    __PORT_PATTERN: re.Pattern = re.compile("^:(\\d{1,5})$")
    __LEGAL_ASCII_PATTERN: re.Pattern = re.compile("^[\x00-\x7F]+$")
    __QUERY_PATTERN: re.Pattern = re.compile("^(.*)$")
    __PATH_PATTERN: re.Pattern = re.compile("^(/[-\\w:@&?=+,.!/~*'%$_;]*)?$")
    __PARSE_AUTHORITY_EXTRA: int = 3
    __PARSE_AUTHORITY_PORT: int = 2
    __PARSE_AUTHORITY_HOST_IP: int = 1

    __AUTHORITY_CHARS_REGEX: str = "\\w\\-\\.\\\\d"
    __AUTHORITY_REGEX: str = "^([" + __AUTHORITY_CHARS_REGEX + "]*)(:\\d*)?(.*)?"
    __AUTHORITY_PATTERN: re.Pattern = re.compile(__AUTHORITY_REGEX, re.UNICODE)

    __SCHEME_PATTERN: re.Pattern = re.compile("^[a-zA-Z][a-zA-Z0-9+\\-\\.]*", re.UNICODE)

    __PARSE_URL_FRAGMENT: int = 9
    __PARSE_URL_QUERY: int = 7
    __PARSE_URL_PATH: int = 5
    __PARSE_URL_AUTHORITY: int = 4
    __PARSE_URL_SCHEME: int = 2
    __URL_REGEX: str = "^(([^:/?#]+):)?(//([^/?#]*))?([^?#]*)(\\?([^#]*))?(#(.*))?"
    __URL_PATTERN: re.Pattern = re.compile(__URL_REGEX)
    __SPECIAL_CHARS: str = "; / @ & = , . ? : + $"
    __serialVersionUID: int = 24137157400029593

    __SPECIAL_CHARS: str = ";/@&=,.?:+$"
    __VALID_CHARS: str = "[^\\s" + __SPECIAL_CHARS + "]"

    __ATOM: str = __VALID_CHARS + '+'

    __DOMAIN_PATTERN: re.Pattern = re.compile("^" + __ATOM + "(\\." + __ATOM + ")*$")

    __ALPHA_PATTERN: re.Pattern = re.compile("^[" + __ALPHA_CHARS + "]")

    __ATOM_PATTERN: re.Pattern = re.compile("^(" + __ATOM + ").*?$")

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

        return self.__options.isOff(self.NO_FRAGMENTS)

    def _isValidQuery(self, query: str) -> bool:

        if query is None:
            return True

        return bool(self.__QUERY_PATTERN.match(query))

    def _isValidPath(self, path: str) -> bool:

        if path is None:
            return False

        if not self.__PATH_PATTERN.match(path):
            return False

        slash2Count = self._countToken("//", path)
        if self.__options.isOff(self.ALLOW_2_SLASHES) and (slash2Count > 0):
            return False

        slashCount = self._countToken("/", path)
        dot2Count = self._countToken("..", path)
        if dot2Count > 0 and (slashCount - slash2Count - 1) <= dot2Count:
            return False

        return True

    def _isValidAuthority(self, authority: str) -> bool:

        if authority is None:
            return False
        
        inetAddressValidator = InetAddressValidator.getInstance()

        authorityMatcher = UrlValidator.__AUTHORITY_PATTERN.match(authority)
        if not authorityMatcher:
            return False
        
        hostname = False
        hostIP = authorityMatcher.group(UrlValidator.__PARSE_AUTHORITY_HOST_IP)
        ipV4Address = inetAddressValidator.isValid(hostIP)

        if not ipV4Address:
            hostname = UrlValidator.__DOMAIN_PATTERN.match(hostIP) is not None

        if hostname:
            chars = list(hostIP)
            size = 1
            for char in chars:
                if char == '.':
                    size += 1
            domainSegment = [None] * size
            match = True
            segmentCount = 0
            segmentLength = 0

            while match:
                atomMatcher = UrlValidator.__ATOM_PATTERN.match(hostIP)
                match = atomMatcher is not None
                if match:
                    domainSegment[segmentCount] = atomMatcher.group(1)
                    segmentLength = len(domainSegment[segmentCount]) + 1
                    hostIP = "" if segmentLength >= len(hostIP) else hostIP[segmentLength:]
                    segmentCount += 1

            topLevel = domainSegment[segmentCount - 1]
            if len(topLevel) < 2 or len(topLevel) > 4:
                return False

            if not UrlValidator.__ALPHA_PATTERN.match(topLevel[0]):
                return False

            if segmentCount < 2:
                return False

        if not hostname and not ipV4Address:
            return False

        port = authorityMatcher.group(UrlValidator.__PARSE_AUTHORITY_PORT)
        if port is not None and not UrlValidator.__PORT_PATTERN.match(port):
            return False

        extra = authorityMatcher.group(UrlValidator.__PARSE_AUTHORITY_EXTRA)
        if extra is not None:
            if len(extra) > 0:
                return False

        return True

    def _isValidScheme(self, scheme: str) -> bool:

        if scheme is None:
            return False

        if not re.match(self.__SCHEME_PATTERN, scheme):
            return False

        if (
            self.__options.isOff(self.ALLOW_ALL_SCHEMES)
            and scheme.lower() not in self.__allowedSchemes
        ):
            return False

        return True

    def isValid(self, value: str) -> bool:

        if value is None:
            return False

        if not self.__LEGAL_ASCII_PATTERN.match(value):
            return False

        urlMatcher = self.__URL_PATTERN.match(value)
        if not urlMatcher:
            return False

        if not self._isValidScheme(urlMatcher.group(self.__PARSE_URL_SCHEME)):
            return False

        if not self._isValidAuthority(urlMatcher.group(self.__PARSE_URL_AUTHORITY)):
            return False

        if not self._isValidPath(urlMatcher.group(self.__PARSE_URL_PATH)):
            return False

        if not self._isValidQuery(urlMatcher.group(self.__PARSE_URL_QUERY)):
            return False

        if not self._isValidFragment(urlMatcher.group(self.__PARSE_URL_FRAGMENT)):
            return False

        return True

    @staticmethod
    def UrlValidator3() -> UrlValidator:
        return UrlValidator.UrlValidator2(None)

    @staticmethod
    def UrlValidator2(schemes: typing.List[typing.List[str]]) -> UrlValidator:
        return UrlValidator(schemes, 0)

    @staticmethod
    def UrlValidator1(options: int) -> UrlValidator:
        return UrlValidator(None, options)

    def __init__(self, schemes: typing.List[typing.List[str]], options: int) -> None:

        self.__options = Flags(1, options)

        if self.__options.isOn(self.ALLOW_ALL_SCHEMES):
            return

        if schemes is None:
            schemes = self._defaultSchemes

        self.__allowedSchemes.update(schemes)
