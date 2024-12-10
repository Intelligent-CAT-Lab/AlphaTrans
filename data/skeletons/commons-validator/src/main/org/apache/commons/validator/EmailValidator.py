from __future__ import annotations

# Imports Begin
from src.main.org.apache.commons.validator.routines.DomainValidator import *
from src.main.org.apache.commons.validator.routines.InetAddressValidator import *
import io

# Imports End


class EmailValidator:

    # Class Fields Begin
    __SPECIAL_CHARS: str = None
    __VALID_CHARS: str = None
    __QUOTED_USER: str = None
    __ATOM: str = None
    __WORD: str = None
    __IP_DOMAIN_PATTERN: re.Pattern = None
    __TLD_PATTERN: re.Pattern = None
    __USER_PATTERN: re.Pattern = None
    __DOMAIN_PATTERN: re.Pattern = None
    __ATOM_PATTERN: re.Pattern = None
    __EMAIL_VALIDATOR: EmailValidator = None
    # Class Fields End

    # Class Methods Begin
    def _stripComments(self, emailStr: str) -> str:
        pass

    def _isValidSymbolicDomain(self, domain: str) -> bool:
        pass

    def _isValidIpAddress(self, ipAddress: str) -> bool:
        pass

    def _isValidUser(self, user: str) -> bool:
        pass

    def _isValidDomain(self, domain: str) -> bool:
        pass

    def isValid(self, email: str) -> bool:
        pass

    def __init__(self) -> None:
        pass

    @staticmethod
    def getInstance() -> EmailValidator:
        pass

    # Class Methods End
