from __future__ import annotations
import re
import io
from src.main.org.apache.commons.validator.routines.InetAddressValidator import *
from src.main.org.apache.commons.validator.routines.DomainValidator import *


class EmailValidator:

    __EMAIL_VALIDATOR: EmailValidator = None
    __TLD_PATTERN: re.Pattern = re.compile("^([a-zA-Z]+)$")
    __IP_DOMAIN_PATTERN: re.Pattern = re.compile("^\\[(.*)\\]$")
    __QUOTED_USER: str = '("[^"]*")'
    __SPECIAL_CHARS: str = "\\p{Cntrl}\\(\\)<>@,;:'\\\\\\\"\\.\\[\\]"

    __VALID_CHARS: str = None  # LLM could not translate this field

    __WORD: str = None  # LLM could not translate this field

    __ATOM: str = None  # LLM could not translate this field

    __ATOM_PATTERN: re.Pattern = re.compile(f"({__ATOM})")

    __DOMAIN_PATTERN: re.Pattern = None  # LLM could not translate this field

    __USER_PATTERN: re.Pattern = None  # LLM could not translate this field

    @staticmethod
    def initialize_fields() -> None:
        EmailValidator.__EMAIL_VALIDATOR: EmailValidator = EmailValidator()

    def _stripComments(self, emailStr: str) -> str:

        result = emailStr
        commentPat = r"^((?:[^\"\\]|\\\\.)*(?:\"(?:[^\"\\]|\\\\.)*\"(?:[^\"\\]|\\\\.)*)*)\\((?:[^()\\\\]|\\\\.)*\\)/"
        commentMatcher = re.compile(commentPat)

        while commentMatcher.match(result):
            result = re.sub(commentPat, r"\1 ", result, count=1)

        return result

    def _isValidSymbolicDomain(self, domain: str) -> bool:

        domain_segment = [""] * 10
        match = True
        i = 0
        atom_matcher = self.__ATOM_PATTERN.match(domain)
        while match:
            match = atom_matcher is not None
            if match:
                domain_segment[i] = atom_matcher.group(1)
                l = len(domain_segment[i]) + 1
                domain = "" if l >= len(domain) else domain[l:]

                i += 1
                atom_matcher = self.__ATOM_PATTERN.match(domain)

        len_ = i

        if len_ < 2:
            return False

        tld = domain_segment[len_ - 1]
        if len(tld) > 1:
            if not self.__TLD_PATTERN.match(tld):
                return False
        else:
            return False

        return True

    def _isValidIpAddress(self, ipAddress: str) -> bool:

        ipAddressMatcher = re.match(self.__IP_DOMAIN_PATTERN, ipAddress)
        if ipAddressMatcher is None:
            return False

        for i in range(
            1, 5
        ):  # Python uses 0-based indexing, so we need to adjust the range
            ipSegment = ipAddressMatcher.group(i)
            if ipSegment is None or len(ipSegment) <= 0:
                return False

            try:
                iIpSegment = int(ipSegment)
            except ValueError:
                return False

            if iIpSegment > 255:
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

        if email.endswith("."):
            return False

        email_matcher = self.__EMAIL_PATTERN.match(email)
        if not email_matcher:
            return False

        if not self._isValidUser(email_matcher.group(1)):
            return False

        if not self._isValidDomain(email_matcher.group(2)):
            return False

        return True

    def __init__(self) -> None:
        super().__init__()

    @staticmethod
    def getInstance() -> EmailValidator:
        return EmailValidator.__EMAIL_VALIDATOR


EmailValidator.initialize_fields()
