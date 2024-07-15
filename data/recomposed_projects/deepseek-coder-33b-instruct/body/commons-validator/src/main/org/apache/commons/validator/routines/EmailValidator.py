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
    __IP_DOMAIN_PATTERN: re.Pattern = re.compile("^\\[(.*)\\]$")
    __EMAIL_PATTERN: re.Pattern = re.compile("^(.+)@(\\S+)$")
    __IP_DOMAIN_REGEX: str = "^\\[(.*)\\]$"
    __EMAIL_REGEX: str = "^(.+)@(\\S+)$"
    __QUOTED_USER: str = '("(\\\\"|[^"])*")'
    __SPECIAL_CHARS: str = "\\p{Cntrl}\\(\\)<>@,;:'\\\\\\\"\\.\\[\\]"
    __serialVersionUID: int = 1705927040799295880
    __VALID_CHARS: str = "(\\\\.)|[^\\s" + __SPECIAL_CHARS + "]"
    __WORD: str = "((" + __VALID_CHARS + "|')+|" + __QUOTED_USER + ")"
    __USER_PATTERN: re.Pattern = re.compile("^" + __WORD + "(\\." + __WORD + ")*$")
    __USER_REGEX: str = "^" + __WORD + "(\\." + __WORD + ")*$"

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

        return self.__USER_PATTERN.match(user) is not None

    def _isValidDomain(self, domain: str) -> bool:

        ipDomainMatcher = re.match(self.__IP_DOMAIN_REGEX, domain)

        if ipDomainMatcher:
            inetAddressValidator = InetAddressValidator.getInstance()
            return inetAddressValidator.isValid(ipDomainMatcher.group(1))
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

        emailMatcher = re.match(self.__EMAIL_REGEX, email)
        if not emailMatcher:
            return False

        if not self._isValidUser(emailMatcher.group(1)):
            return False

        if not self._isValidDomain(emailMatcher.group(2)):
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

        self.__allowTld = allowTld
        if constructorId == 0:
            if domainValidator is None:
                raise ValueError("DomainValidator cannot be null")
            else:
                if domainValidator.isAllowLocal() != allowLocal:
                    raise ValueError(
                        "DomainValidator must agree with allowLocal setting"
                    )
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
        return EmailValidator.__EMAIL_VALIDATOR


EmailValidator.initialize_fields()
