from __future__ import annotations

# Imports Begin
from src.main.org.apache.commons.validator.routines.DomainValidator import *
from src.main.org.apache.commons.validator.routines.InetAddressValidator import *
import io

# Imports End


class EmailValidator:

    # Class Fields Begin
    __serialVersionUID: int = None
    __SPECIAL_CHARS: str = None
    __VALID_CHARS: str = None
    __QUOTED_USER: str = None
    __WORD: str = None
    __EMAIL_REGEX: str = None
    __IP_DOMAIN_REGEX: str = None
    __USER_REGEX: str = None
    __EMAIL_PATTERN: re.Pattern = None
    __IP_DOMAIN_PATTERN: re.Pattern = None
    __USER_PATTERN: re.Pattern = None
    __MAX_USERNAME_LEN: int = None
    __allowTld: bool = None
    __EMAIL_VALIDATOR: EmailValidator = None
    __EMAIL_VALIDATOR_WITH_TLD: EmailValidator = None
    __EMAIL_VALIDATOR_WITH_LOCAL: EmailValidator = None
    __EMAIL_VALIDATOR_WITH_LOCAL_WITH_TLD: EmailValidator = None
    __domainValidator: DomainValidator = None
    # Class Fields End

    # Class Methods Begin
    def _isValidUser(self, user: str) -> bool:
        pass

    def _isValidDomain(self, domain: str) -> bool:
        pass

    def isValid(self, email: str) -> bool:
        pass

    @staticmethod
    def EmailValidator0(allowLocal: bool) -> EmailValidator:
        pass

    def __init__(
        self,
        constructorId: int,
        allowLocal: bool,
        allowTld: bool,
        domainValidator: DomainValidator,
    ) -> None:
        pass

    @staticmethod
    def getInstance2(allowLocal: bool) -> EmailValidator:
        pass

    @staticmethod
    def getInstance1(allowLocal: bool, allowTld: bool) -> EmailValidator:
        pass

    @staticmethod
    def getInstance0() -> EmailValidator:
        pass

    # Class Methods End
