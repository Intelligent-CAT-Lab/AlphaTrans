from __future__ import annotations
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

    _defaultSchemes: typing.List[str] = ["http", "https", "ftp"]

    NO_FRAGMENTS: int = 1 << 2

    ALLOW_2_SLASHES: int = 1 << 1

    ALLOW_ALL_SCHEMES: int = 1 << 0

    __allowedSchemes: typing.Set[str] = set()
    __options: Flags = None
    __ALPHA_PATTERN: re.Pattern = None  # LLM could not translate this field
    __ATOM_PATTERN: re.Pattern = None  # LLM could not translate this field

    __PORT_PATTERN: re.Pattern = re.compile("^:(\\d{1,5})$")
    __DOMAIN_PATTERN: re.Pattern = None  # LLM could not translate this field

    __LEGAL_ASCII_PATTERN: re.Pattern = re.compile("^[\x00-\x7F]+$")
    __QUERY_PATTERN: re.Pattern = None  # LLM could not translate this field

    __PATH_PATTERN: re.Pattern = re.compile("^(/[-\\w:@&?=+,.!/~*'%$_;]*)?$")

    __PARSE_AUTHORITY_EXTRA: int = 3

    __PARSE_AUTHORITY_PORT: int = 2

    __PARSE_AUTHORITY_HOST_IP: int = 1
    __AUTHORITY_PATTERN: re.Pattern = None  # LLM could not translate this field

    __AUTHORITY_REGEX: str = r"^([" + AUTHORITY_CHARS_REGEX + r"]*)(:\d*)?(.*)?"
    __SCHEME_PATTERN: re.Pattern = None  # LLM could not translate this field

    __PARSE_URL_FRAGMENT: int = 9

    __PARSE_URL_QUERY: int = 7

    __PARSE_URL_PATH: int = 5

    __PARSE_URL_AUTHORITY: int = 4

    __PARSE_URL_SCHEME: int = 2

    __URL_PATTERN: re.Pattern = re.compile(URL_REGEX)

    __URL_REGEX: str = "^(([^:/?#]+):)?(//([^/?#]*))?([^?#]*)(\\?([^#]*))?(#(.*))?"

    __ATOM: str = VALID_CHARS + "+"

    __AUTHORITY_CHARS_REGEX: str = "\\p{Alnum}\\-\\."

    __VALID_CHARS: str = "[^\\s" + SPECIAL_CHARS + "]"

    __SPECIAL_CHARS: str = "; / @ & = , . ? : + $"

    __ALPHA_CHARS: str = "a-zA-Z"

    __serialVersionUID: int = 24137157400029593

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

        return self.__QUERY_PATTERN.match(query) is not None

    def _isValidPath(self, path: str) -> bool:

        if path is None:
            return False

        if not self.__PATH_PATTERN.match(path):
            return False

        slash2Count = self._countToken("//", path)
        if not self.__options.isOff(self.ALLOW_2_SLASHES) and (slash2Count > 0):
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

        authorityMatcher = re.match(self.__AUTHORITY_PATTERN, authority)
        if not authorityMatcher:
            return False

        hostname = False
        hostIP = authorityMatcher.group(self.__PARSE_AUTHORITY_HOST_IP)
        ipV4Address = inetAddressValidator.isValid(hostIP)

        if not ipV4Address:
            hostname = re.match(self.__DOMAIN_PATTERN, hostIP) is not None

        if hostname:
            chars = list(hostIP)
            size = 1
            for i in range(len(chars)):
                if chars[i] == ".":
                    size += 1
            domainSegment = [None] * size
            match = True
            segmentCount = 0
            segmentLength = 0

            while match:
                atomMatcher = re.match(self.__ATOM_PATTERN, hostIP)
                match = atomMatcher is not None
                if match:
                    domainSegment[segmentCount] = atomMatcher.group(1)
                    segmentLength = len(domainSegment[segmentCount]) + 1
                    hostIP = (
                        hostIP[segmentLength:] if segmentLength < len(hostIP) else ""
                    )

                    segmentCount += 1

            topLevel = domainSegment[segmentCount - 1]
            if len(topLevel) < 2 or len(topLevel) > 4:
                return False

            if not re.match(self.__ALPHA_PATTERN, topLevel[0]):
                return False

            if segmentCount < 2:
                return False

        if not hostname and not ipV4Address:
            return False

        port = authorityMatcher.group(self.__PARSE_AUTHORITY_PORT)
        if port is not None and re.match(self.__PORT_PATTERN, port) is None:
            return False

        extra = authorityMatcher.group(self.__PARSE_AUTHORITY_EXTRA)
        if not GenericValidator.isBlankOrNull(extra):
            return False

        return True

    def _isValidScheme(self, scheme: str) -> bool:

        if scheme is None:
            return False

        if not self.__SCHEME_PATTERN.match(scheme):
            return False

        if (
            not self.__options.isOff(self.ALLOW_ALL_SCHEMES)
            and scheme not in self.__allowedSchemes
        ):
            return False

        return True

    def isValid(self, value: str) -> bool:

        if value is None:
            return False

        if not self.__LEGAL_ASCII_PATTERN.match(value):
            return False

        url_matcher = self.__URL_PATTERN.match(value)
        if not url_matcher:
            return False

        if not self._isValidScheme(url_matcher.group(self.__PARSE_URL_SCHEME)):
            return False

        if not self._isValidAuthority(url_matcher.group(self.__PARSE_URL_AUTHORITY)):
            return False

        if not self._isValidPath(url_matcher.group(self.__PARSE_URL_PATH)):
            return False

        if not self._isValidQuery(url_matcher.group(self.__PARSE_URL_QUERY)):
            return False

        if not self._isValidFragment(url_matcher.group(self.__PARSE_URL_FRAGMENT)):
            return False

        return True

    @staticmethod
    def UrlValidator3() -> UrlValidator:

        return UrlValidator.UrlValidator2(None)

    @staticmethod
    def UrlValidator2(schemes: typing.List[str]) -> UrlValidator:

        return UrlValidator(schemes, 0)

    @staticmethod
    def UrlValidator1(options: int) -> UrlValidator:

        return UrlValidator(None, options)

    def __init__(self, schemes: typing.List[str], options: int) -> None:

        self.__options = Flags(1, options)

        if self.__options.isOn(self.ALLOW_ALL_SCHEMES):
            return

        if schemes is None:
            schemes = self._defaultSchemes

        self.__allowedSchemes = set(schemes)
