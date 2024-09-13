from __future__ import annotations
import re
import typing
from typing import *
import io
from src.main.org.apache.commons.validator.routines.RegexValidator import *


class InetAddressValidator:

    __IPV4_REGEX: str = "^(\\d{1,3})\\.(\\d{1,3})\\.(\\d{1,3})\\.(\\d{1,3})$"
    __VALIDATOR: InetAddressValidator = None
    __IPV6_MAX_HEX_DIGITS_PER_GROUP: int = 4
    __IPV6_MAX_HEX_GROUPS: int = 8
    __serialVersionUID: int = -919201640201914789
    __BASE_16: int = 16
    __MAX_UNSIGNED_SHORT: int = 0xFFFF
    __IPV4_MAX_OCTET_VALUE: int = 255

    @staticmethod
    def initialize_fields() -> None:
        InetAddressValidator.__VALIDATOR: InetAddressValidator = InetAddressValidator()

    def isValidInet6Address(self, inet6Address: str) -> bool:

        parts = inet6Address.split("/", -1)
        if len(parts) > 2:
            return False
        if len(parts) == 2:
            if parts[1].isdigit():
                bits = int(parts[1])
                if bits < 0 or bits > 128:
                    return False
            else:
                return False
        parts = parts[0].split("%", -1)
        if len(parts) > 2:
            return False
        elif len(parts) == 2:
            if not parts[1].isalnum():
                return False
        inet6Address = parts[0]
        containsCompressedZeroes = "::" in inet6Address
        if containsCompressedZeroes and (inet6Address.count("::") != 1):
            return False
        if (inet6Address.startswith(":") and not inet6Address.startswith("::")) or (
            inet6Address.endswith(":") and not inet6Address.endswith("::")
        ):
            return False
        octets = inet6Address.split(":")
        if containsCompressedZeroes:
            octetList = list(octets)
            if inet6Address.endswith("::"):
                octetList.append("")
            elif inet6Address.startswith("::") and len(octetList) > 0:
                octetList.pop(0)
            octets = octetList
        if len(octets) > self.__IPV6_MAX_HEX_GROUPS:
            return False
        validOctets = 0
        emptyOctets = 0
        for index in range(len(octets)):
            octet = octets[index]
            if len(octet) == 0:
                emptyOctets += 1
                if emptyOctets > 1:
                    return False
            else:
                emptyOctets = 0
                if index == len(octets) - 1 and "." in octet:
                    if not self.isValidInet4Address(octet):
                        return False
                    validOctets += 2
                    continue
                if len(octet) > self.__IPV6_MAX_HEX_DIGITS_PER_GROUP:
                    return False
                try:
                    octetInt = int(octet, self.__BASE_16)
                except ValueError:
                    return False
                if octetInt < 0 or octetInt > self.__MAX_UNSIGNED_SHORT:
                    return False
            validOctets += 1
        if validOctets > self.__IPV6_MAX_HEX_GROUPS or (
            validOctets < self.__IPV6_MAX_HEX_GROUPS and not containsCompressedZeroes
        ):
            return False
        return True

    def isValidInet4Address(self, inet4Address: str) -> bool:

        groups = self.__ipv4Validator.match(inet4Address)

        if groups is None:
            return False

        for ipSegment in groups:
            if ipSegment is None or len(ipSegment) == 0:
                return False

            try:
                iIpSegment = int(ipSegment)
            except ValueError:
                return False

            if iIpSegment > self.__IPV4_MAX_OCTET_VALUE:
                return False

            if len(ipSegment) > 1 and ipSegment.startswith("0"):
                return False

        return True

    def isValid(self, inetAddress: str) -> bool:

        return self.isValidInet4Address(inetAddress) or self.isValidInet6Address(
            inetAddress
        )

    @staticmethod
    def getInstance() -> InetAddressValidator:
        return InetAddressValidator.__VALIDATOR


InetAddressValidator.initialize_fields()
