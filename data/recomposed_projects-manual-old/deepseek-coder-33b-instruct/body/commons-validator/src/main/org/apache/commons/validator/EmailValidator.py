from __future__ import annotations
import re
import numbers
import io
from src.main.org.apache.commons.validator.routines.InetAddressValidator import *
from src.main.org.apache.commons.validator.routines.DomainValidator import *


class EmailValidator:

    __EMAIL_VALIDATOR: EmailValidator = None
    __TLD_PATTERN: re.Pattern = re.compile(r"^([a-zA-Z]+)$")
    __IP_DOMAIN_PATTERN: re.Pattern = re.compile(r"^\[(.*)\]$")
    __QUOTED_USER: str = r'("[^"]*")'
    __SPECIAL_CHARS: str = "\\p{Cntrl}\\(\\)<>@,;:'\\\\\\\"\\.\\[\\]"
    __VALID_CHARS: str = "[^\\s" + __SPECIAL_CHARS + "]"
    __WORD: str = f"(({__VALID_CHARS}|')+|{__QUOTED_USER})"
    __ATOM: str = f"{__VALID_CHARS}+"
    __ATOM_PATTERN: re.Pattern = re.compile(f"({__ATOM})")
    __DOMAIN_PATTERN: re.Pattern = re.compile(f"^{__ATOM}(.{__ATOM})*\\s*$")
    __USER_PATTERN: re.Pattern = re.compile(f"^\\s*{__WORD}(.{__WORD})*$")

    @staticmethod
    def initialize_fields() -> None:
        EmailValidator.__EMAIL_VALIDATOR: EmailValidator = EmailValidator()

    def _stripComments(self, emailStr: str) -> str:

        result = emailStr
        commentPat = r"^((?:[^\"\\]|\\.)*(?:\"(?:[^\"\\]|\\.)*\"(?:[^\"\\]|\\.)*)*)\\((?:[^()\\]|\\.)*\\)/"
        commentMatcher = re.compile(commentPat)

        while commentMatcher.match(result):
            result = re.sub(commentPat, r"\1 ", result)

        return result

    def _isValidSymbolicDomain(self, domain: str) -> bool:

        domain_segment = [""] * 10
        match = True
        i = 0
        atom_matcher = re.match(self.__ATOM_PATTERN, domain)
        while match:
            match = atom_matcher is not None
            if match:
                domain_segment[i] = atom_matcher.group(1)
                l = len(domain_segment[i]) + 1
                domain = "" if l >= len(domain) else domain[l:]

                i += 1
            atom_matcher = re.match(self.__ATOM_PATTERN, domain)

        len_ = i

        if len_ < 2:
            return False

        tld = domain_segment[len_ - 1]
        if len(tld) > 1:
            if not re.match(self.__TLD_PATTERN, tld):
                return False
        else:
            return False

        return True

    def _isValidIpAddress(self, ipAddress: str) -> bool:

        ipAddressMatcher = re.match(self.__IP_DOMAIN_PATTERN, ipAddress)
        if ipAddressMatcher is None:
            return False

        for i in range(1, 5):  # CHECKSTYLE IGNORE MagicNumber
            ipSegment = ipAddressMatcher.group(i)
            if ipSegment is None or len(ipSegment) <= 0:
                return False

            try:
                iIpSegment = int(ipSegment)
            except ValueError:
                return False

            if iIpSegment > 255:  # CHECKSTYLE IGNORE MagicNumber
                return False

        return True

    def _isValidUser(self, user: str) -> bool:
        return bool(self.__USER_PATTERN.match(user))

    def _isValidDomain(self, domain: str) -> bool:

        symbolic = False

        ip_domain_matcher = re.match(self.__IP_DOMAIN_PATTERN, domain)

        if ip_domain_matcher:
            inet_address_validator = InetAddressValidator.getInstance()
            if inet_address_validator.isValid(ip_domain_matcher.group(1)):
                return True
        else:
            symbolic = re.match(self.__DOMAIN_PATTERN, domain) is not None

        if symbolic:
            if not self._isValidSymbolicDomain(domain):
                return False
        else:
            return False

        return True

    def isValid(self, email: str) -> bool:

        if email is None:
            return False

        if email.endswith("."):  # check this first - it's cheap
            return False

        emailMatcher = re.match(self.__EMAIL_REGEX, email)
        if not emailMatcher:
            return False

        if not self._isValidUser(emailMatcher.group(1)):
            return False

        if not self._isValidDomain(emailMatcher.group(2)):
            return False

        return True

    def __init__(self) -> None:
        super().__init__()

    @staticmethod
    def getInstance() -> EmailValidator:
        return EmailValidator.__EMAIL_VALIDATOR


EmailValidator.initialize_fields()
