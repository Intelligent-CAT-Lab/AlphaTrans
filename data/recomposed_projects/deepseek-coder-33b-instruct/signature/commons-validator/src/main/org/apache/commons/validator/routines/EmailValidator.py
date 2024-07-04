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
    __IP_DOMAIN_REGEX: str = "^\\[(.*)\\]$"
    __EMAIL_REGEX: str = "^(.+)@(\\S+)$"
    __QUOTED_USER: str = r"(\"(\\\\\"|[^\"])*\")"
    __VALID_CHARS: str = "(\\\\.)|[^\\s\\\\p{Cntrl}\\(\\)<>@,;:'\\\\\\\"\\.\\[\\]]"
    __SPECIAL_CHARS: str = "\\p{Cntrl}\\(\\)<>@,;:'\\\\\\\"\\.\\[\\]"
    __serialVersionUID: int = 1705927040799295880
    __WORD: str = None
    __USER_REGEX: str = None

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

        EmailValidator.__WORD: str = (
            "(("
            + EmailValidator.__VALID_CHARS
            + "|')+|"
            + EmailValidator.__QUOTED_USER
            + ")"
        )

        EmailValidator.__USER_REGEX: str = (
            "^" + EmailValidator.__WORD + "(\\." + EmailValidator.__WORD + ")*$"
        )

    def _isValidUser(self, user: str) -> bool:

        if user is None or len(user) > self.__MAX_USERNAME_LEN:
            return False

        return bool(self.__USER_PATTERN.match(user))

    def _isValidDomain(self, domain: str) -> bool:

        ip_domain_matcher = re.match(self.__IP_DOMAIN_REGEX, domain)

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

        if email.endswith("."):  # check this first - it's cheap
            return False

        email_matcher = self.__EMAIL_PATTERN.match(email)
        if not email_matcher:
            return False

        if not self._isValidUser(email_matcher.group(1)):
            return False

        if not self._isValidDomain(email_matcher.group(2)):
            return False

        return True

    @staticmethod
    def EmailValidator0(allowLocal: bool) -> EmailValidator:
        return EmailValidator(1, allowLocal, False, None)

    def __init__(
        self,
        constructorId: int,
        allowLocal: bool,
        allowTld: bool,
        domainValidator: DomainValidator,
    ) -> None:

        self.__allowTld = allowTld

        if constructorId == 0:
            if domainValidator is None:
                raise ValueError("DomainValidator cannot be null")
            elif domainValidator.isAllowLocal() != allowLocal:
                raise ValueError("DomainValidator must agree with allowLocal setting")
            else:
                self.__domainValidator = domainValidator
        else:
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
        if EmailValidator.__EMAIL_VALIDATOR is None:
            EmailValidator.__EMAIL_VALIDATOR = EmailValidator(1, False, False, None)
        return EmailValidator.__EMAIL_VALIDATOR


EmailValidator.initialize_fields()
