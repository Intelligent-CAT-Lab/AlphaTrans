from __future__ import annotations
import re
import io
from src.main.org.apache.commons.validator.routines.InetAddressValidator import *
from src.main.org.apache.commons.validator.routines.DomainValidator import *


class EmailValidator:

    __domainValidator: DomainValidator = None

    __EMAIL_VALIDATOR_WITH_LOCAL_WITH_TLD: EmailValidator = None
    __EMAIL_VALIDATOR_WITH_LOCAL: EmailValidator = None
    __EMAIL_VALIDATOR_WITH_TLD: EmailValidator = None
    __EMAIL_VALIDATOR: EmailValidator = None
    __allowTld: bool = False

    __MAX_USERNAME_LEN: int = 64
    __EMAIL_REGEX: str = "^(.+)@(\\S+)$"
    __EMAIL_PATTERN: re.Pattern = re.compile(__EMAIL_REGEX)
    __IP_DOMAIN_REGEX: str = "^\\[(.*)\\]$"
    __IP_DOMAIN_PATTERN: re.Pattern = re.compile(__IP_DOMAIN_REGEX)
    __QUOTED_USER: str = '("(\\\\"|[^"])*")'
    __SPECIAL_CHARS: str = r'[\x00-\x1F\x7F-\x9F()<>@,;:\'\\\".\[\]]'
    __VALID_CHARS: str = "(\\\\.)|[^\\s"  + "]"
    __serialVersionUID: int = 1705927040799295880

    __WORD: str = "((" + __VALID_CHARS + "|')+|" + __QUOTED_USER + ")"

    __USER_REGEX: str = "^" + __WORD + "(\\." + __WORD + ")*$"
    __USER_PATTERN: re.Pattern = re.compile(__USER_REGEX)

    @staticmethod
    def initialize_fields() -> None:
        EmailValidator.__EMAIL_VALIDATOR_WITH_LOCAL_WITH_TLD: EmailValidator = (
            EmailValidator(1, True, True, None)
        )

        EmailValidator.__EMAIL_VALIDATOR_WITH_LOCAL: EmailValidator = EmailValidator(
            1, True, False, None
        )

        EmailValidator.__EMAIL_VALIDATOR_WITH_TLD: EmailValidator = EmailValidator(
            1, False, True, None
        )

        EmailValidator.__EMAIL_VALIDATOR: EmailValidator = EmailValidator(
            1, False, False, None
        )

    def _isValidUser(self, user: str) -> bool:

        if user is None or len(user) > self.__MAX_USERNAME_LEN:
            return False

        return bool(self.__USER_PATTERN.match(user))

    def _isValidDomain(self, domain: str) -> bool:

        ip_domain_matcher = self.__IP_DOMAIN_PATTERN.match(domain)

        if ip_domain_matcher:
            inet_address_validator = InetAddressValidator.getInstance()
            return inet_address_validator.isValid(ip_domain_matcher.group(1))
        if self.__allowTld:
            return self.__domainValidator.isValid(domain) or (
                not domain.startswith(".") and self.__domainValidator.isValidTld(domain)
            )
        else:
            return self.__domainValidator.isValid(domain)

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
        
        pattern = r'''
            ^                         # Start of the string
            (                         # Start of the main group
                [a-zA-Z0-9!#$%&'*+/=?^_`{|}~-]+  # Allowed characters without quotes
                (                     # Start of a group for dots
                    \.                # Literal dot
                    [a-zA-Z0-9!#$%&'*+/=?^_`{|}~-]+  # Followed by more allowed characters
                )*                    # Zero or more dots and subsequent characters
                |                     # Or
                "                     # Start of a quoted string
                (                     # Group for quoted string content
                    \\[\\\@\^]       # Escaped characters
                    |                 # Or
                    [^\\"@]          # Any character except quotes and at symbol
                )*                    # Zero or more characters
                "                     # End of quoted string
            )                         # End of the main group
            $                         # End of the string
        '''
        input = re.sub(r'\\.', '', email_matcher.group(1))
        if not re.match(pattern, input, re.VERBOSE):
            if not (input.startswith('"') and input.endswith('"')):
                return False

        if not self._isValidDomain(email_matcher.group(2)) or "_" in email_matcher.group(2):
            return False

        return True

    @staticmethod
    def EmailValidator0(allowLocal: bool) -> EmailValidator:
        return EmailValidator(0, allowLocal, False, None)

    def __init__(
        self,
        constructorId: int,
        allowLocal: bool,
        allowTld: bool,
        domainValidator: DomainValidator,
    ) -> None:

        if constructorId == 0:
            self.__allowTld = allowTld
            if domainValidator is None:
                raise ValueError("DomainValidator cannot be null")
            else:
                if domainValidator.isAllowLocal() != allowLocal:
                    raise ValueError(
                        "DomainValidator must agree with allowLocal setting"
                    )
                self.__domainValidator = domainValidator
        else:
            self.__allowTld = allowTld
            self.__domainValidator = DomainValidator.getInstance1(allowLocal)

    @staticmethod
    def getInstance2(allowLocal: bool) -> EmailValidator:

        return EmailValidator.getInstance1(allowLocal, False)

    @staticmethod
    def getInstance1(allowLocal: bool, allowTld: bool) -> EmailValidator:

        if allowLocal:
            if allowTld:
                return EmailValidator.__EMAIL_VALIDATOR_WITH_LOCAL_WITH_TLD
            else:
                return EmailValidator.__EMAIL_VALIDATOR_WITH_LOCAL
        else:
            if allowTld:
                return EmailValidator.__EMAIL_VALIDATOR_WITH_TLD
            else:
                return EmailValidator.__EMAIL_VALIDATOR

    @staticmethod
    def getInstance0() -> EmailValidator:
        return EmailValidator.__EMAIL_VALIDATOR


EmailValidator.initialize_fields()
