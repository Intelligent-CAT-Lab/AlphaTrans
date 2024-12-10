from __future__ import annotations

# Imports Begin
from src.main.org.apache.commons.validator.routines.RegexValidator import *
import io

# Imports End


class InetAddressValidator:

    # Class Fields Begin
    __IPV4_MAX_OCTET_VALUE: int = None
    __MAX_UNSIGNED_SHORT: int = None
    __BASE_16: int = None
    __serialVersionUID: int = None
    __IPV4_REGEX: str = None
    __IPV6_MAX_HEX_GROUPS: int = None
    __IPV6_MAX_HEX_DIGITS_PER_GROUP: int = None
    __VALIDATOR: InetAddressValidator = None
    __ipv4Validator: RegexValidator = None
    # Class Fields End

    # Class Methods Begin
    def isValidInet6Address(self, inet6Address: str) -> bool:
        pass

    def isValidInet4Address(self, inet4Address: str) -> bool:
        pass

    def isValid(self, inetAddress: str) -> bool:
        pass

    @staticmethod
    def getInstance() -> InetAddressValidator:
        pass

    # Class Methods End
