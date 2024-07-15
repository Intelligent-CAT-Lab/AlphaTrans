from __future__ import annotations
import re
import typing
from typing import *
import numbers
import io
from src.main.org.apache.commons.validator.routines.InetAddressValidator import *
from src.main.org.apache.commons.validator.routines.DomainValidator import *


class EmailValidator:

    __EMAIL_VALIDATOR: EmailValidator = None
    __TLD_PATTERN: re.Pattern = re.compile("^([a-zA-Z]+)$")
    __IP_DOMAIN_PATTERN: re.Pattern = re.compile("^\\[(.*)\\]$")
    __WORD: str = "((" + VALID_CHARS + "|')+|" + QUOTED_USER + ")"
    __QUOTED_USER: str = '("[^"]*")'
    __SPECIAL_CHARS: str = "\\p{Cntrl}\\(\\)<>@,;:'\\\\\\\"\\.\\[\\]"
    __USER_PATTERN: re.Pattern = re.compile("^\\s*" + __WORD + "(\\." + __WORD + ")*$")
    __VALID_CHARS: str = "[^\\s" + __SPECIAL_CHARS + "]"
    __ATOM: str = __VALID_CHARS + "+"
    __ATOM_PATTERN: re.Pattern = re.compile("(" + __ATOM + ")")
    __DOMAIN_PATTERN: re.Pattern = re.compile(
        "^" + __ATOM + "(\\." + __ATOM + ")*\\s*$"
    )

    @staticmethod
    def initialize_fields() -> None:
        EmailValidator.__EMAIL_VALIDATOR: EmailValidator = EmailValidator()

    def _stripComments(self, emailStr: str) -> str:
        result = emailStr
        commentPat = '^((?:[^"\\\\]|\\\\.)*(?:"(?:[^"\\\\]|\\\\.)*"(?:[^"\\\\]|\111111\\\\.)*)*)\\((?:[^()\\\\]|\\\\.)*\\)/'
        commentMatcher = re.compile(commentPat)

        while commentMatcher.match(result):
            result = re.sub(commentPat, "\1 ", result)
        return result

    def _isValidSymbolicDomain(self, domain: str) -> bool:
        domain_segment: List[str] = [None] * 10
        match: bool = True
        i: int = 0
        atom_matcher: re.Match = self.__ATOM_PATTERN.matcher(domain)
        while match:
            match = atom_matcher.matches()
            if match:
                domain_segment[i] = atom_matcher.group(1)
                l: int = len(domain_segment[i]) + 1
                domain = "" if l >= len(domain) else domain[l:]

                i += 1

        len: int = i

        if len < 2:
            return False

        tld: str = domain_segment[len - 1]
        if len(tld) > 1:
            if not self.__TLD_PATTERN.matcher(tld).matches():
                return False
        else:
            return False

        return True

    def _isValidIpAddress(self, ipAddress: str) -> bool:
        ipAddressMatcher = self.__IP_DOMAIN_PATTERN.matcher(ipAddress)
        for i in range(1, 5):  # CHECKSTYLE IGNORE MagicNumber
            ipSegment = ipAddressMatcher.group(i)
            if ipSegment is None or len(ipSegment) <= 0:
                return False

            iIpSegment = 0

            try:
                iIpSegment = int(ipSegment)
            except ValueError as e:
                return False

            if iIpSegment > 255:  # CHECKSTYLE IGNORE MagicNumber
                return False
        return True

    def _isValidUser(self, user: str) -> bool:
        return self.__USER_PATTERN.matcher(user).matches()

    def _isValidDomain(self, domain: str) -> bool:
        symbolic = False

        ipDomainMatcher = self.__IP_DOMAIN_PATTERN.match(domain)

        if ipDomainMatcher:
            inetAddressValidator = InetAddressValidator.getInstance()
            if inetAddressValidator.isValid(ipDomainMatcher.group(1)):
                return True
        else:
            symbolic = self.__DOMAIN_PATTERN.match(domain)

        if symbolic:
            if not self._isValidSymbolicDomain(domain):
                return False
        else:
            return False

        return True

    def isValid(self, email: str) -> bool:
        return (
            org.apache.commons.validator.routines.EmailValidator.getInstance0().isValid(
                email
            )
        )

    def __init__(self) -> None:
        super().__init__()

    @staticmethod
    def getInstance() -> EmailValidator:
        return EmailValidator.__EMAIL_VALIDATOR


EmailValidator.initialize_fields()
