from __future__ import annotations
import re
import io
from src.main.org.apache.commons.validator.routines.InetAddressValidator import *
from src.main.org.apache.commons.validator.routines.DomainValidator import *


class EmailValidator:

    __USER_PATTERN: re.Pattern = None  # LLM could not translate this field

    __TLD_PATTERN: re.Pattern = re.compile("^([a-zA-Z]+)$")
    __IP_DOMAIN_PATTERN: re.Pattern = re.compile("^\\[(.*)\\]$")
    __QUOTED_USER: str = r"(\"[^\"]*\")"
    __SPECIAL_CHARS: str = "\\p{Cntrl}\\(\\)<>@,;:'\\\\\\\"\\.\\[\\]"
    __EMAIL_VALIDATOR: EmailValidator = None
    __VALID_CHARS: str = None
    __WORD: str = None
    __ATOM: str = __VALID_CHARS + "+"
    __DOMAIN_PATTERN: re.Pattern = None

    @staticmethod
    def initialize_fields() -> None:
        EmailValidator.__EMAIL_VALIDATOR: EmailValidator = EmailValidator()

        EmailValidator.__VALID_CHARS: str = (
            "[^\\s" + EmailValidator.__SPECIAL_CHARS + "]"
        )

        EmailValidator.__WORD: str = (
            "(("
            + EmailValidator.__VALID_CHARS
            + "|')+|"
            + EmailValidator.__QUOTED_USER
            + ")"
        )

        EmailValidator.__DOMAIN_PATTERN: re.Pattern = re.compile(
            "^" + EmailValidator.__ATOM + "(\\." + EmailValidator.__ATOM + ")*\\s*$"
        )

    def _stripComments(self, emailStr: str) -> str:

        result = emailStr
        commentPat = r"^((?:[^\"\\]|\\\\.)*(?:\"(?:[^\"\\]|\\\\.)*\"(?:[^\"\\]|\\\\.)*)*)\\((?:[^()\\\\]|\\\\.)*\\)/"
        commentMatcher = re.compile(commentPat)

        while commentMatcher.match(result):
            result = re.sub(commentPat, r"\1 ", result, count=1)

        return result

    def _isValidSymbolicDomain(self, domain: str) -> bool:

        domain_segment = [None] * 10
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

        ipAddressMatcher = re.match(EmailValidator.__IP_DOMAIN_PATTERN, ipAddress)
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
        return bool(re.match(r"^\s*\w+(?:\.\w+)*$", user))

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

        # Check if the email is valid
        if not org.apache.commons.validator.routines.EmailValidator.getInstance0().isValid(
            email
        ):
            return False

        return True

    def __init__(self) -> None:
        super().__init__()

    @staticmethod
    def getInstance() -> EmailValidator:
        return EmailValidator.__EMAIL_VALIDATOR


EmailValidator.initialize_fields()
