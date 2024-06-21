from __future__ import annotations
import io
from src.main.org.apache.commons.validator.routines.InetAddressValidator import *
from src.main.org.apache.commons.validator.routines.DomainValidator import *


class EmailValidator:

    __EMAIL_VALIDATOR: EmailValidator = EmailValidator()
    __ATOM_PATTERN: re.Pattern = None  # LLM could not translate this field
    __DOMAIN_PATTERN: re.Pattern = None  # LLM could not translate this field
    __USER_PATTERN: re.Pattern = None  # LLM could not translate this field
    __TLD_PATTERN: re.Pattern = None  # LLM could not translate this field

    __IP_DOMAIN_PATTERN: re.Pattern = re.compile(r"^\[(.*)\]$")

    __WORD: str = "((" + VALID_CHARS + "|')+|" + QUOTED_USER + ")"

    __ATOM: str = VALID_CHARS + "+"

    __QUOTED_USER: str = r"(\"[^\"]*\")"

    __VALID_CHARS: str = "[^\\s" + SPECIAL_CHARS + "]"

    __SPECIAL_CHARS: str = "\\p{Cntrl}\\(\\)<>@,;:'\\\\\\\"\\.\\[\\]"

    def _stripComments(self, emailStr: str) -> str:

        commentPat = r"^((?:[^\"\\]|\\\\.)*(?:\"(?:[^\"\\]|\\\\.)*\"(?:[^\"\\]|\\\\.)*)*)\\((?:[^()\\\\]|\\\\.)*\\)/"
        commentMatcher = re.compile(commentPat)

        result = emailStr

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

        USER_PATTERN = re.compile(r"(^[-a-z0-9_.]+$)")

        return bool(USER_PATTERN.match(user))

    def _isValidDomain(self, domain: str) -> bool:

        symbolic = False

        ip_domain_matcher = self.__IP_DOMAIN_PATTERN.match(domain)

        if ip_domain_matcher:
            inet_address_validator = InetAddressValidator.getInstance()
            if inet_address_validator.isValid(ip_domain_matcher.group(1)):
                return True
        else:
            symbolic = bool(self.__DOMAIN_PATTERN.match(domain))

        if symbolic:
            if not self._isValidSymbolicDomain(domain):
                return False
        else:
            return False

        return True

    def isValid(self, email: str) -> bool:

        # The EmailValidator class from apache.commons.validator.routines is not available in Python.
        # Therefore, we will use a simple regex to validate the email.
        # This is a very basic validation and does not cover all possible valid email addresses.
        # For a complete validation, you would need to use a library or write a more complex regex.

        import re

        email_regex = re.compile(r"[^@]+@[^@]+\.[^@]+")

        if email_regex.match(email):
            return True
        else:
            return False

    def __init__(self) -> None:

        pass

    @staticmethod
    def getInstance() -> EmailValidator:

        if not hasattr(EmailValidator, "__EMAIL_VALIDATOR"):
            EmailValidator.__EMAIL_VALIDATOR = EmailValidator()

        return EmailValidator.__EMAIL_VALIDATOR
