from __future__ import annotations
import re
import typing
from typing import *
import numbers
import io
from src.main.org.apache.commons.validator.routines.RegexValidator import *


class InetAddressValidator:

    __VALIDATOR: InetAddressValidator = None
    __IPV6_MAX_HEX_DIGITS_PER_GROUP: int = 4
    __IPV6_MAX_HEX_GROUPS: int = 8
    __IPV4_REGEX: str = "^(\\d{1,3})\\.(\\d{1,3})\\.(\\d{1,3})\\.(\\d{1,3})$"
    __serialVersionUID: int = -919201640201914789
    __BASE_16: int = 16
    __MAX_UNSIGNED_SHORT: int = 0xFFFF
    __IPV4_MAX_OCTET_VALUE: int = 255
    __ipv4Validator: RegexValidator = RegexValidator.RegexValidator3(__IPV4_REGEX)

    @staticmethod
    def initialize_fields() -> None:
        InetAddressValidator.__VALIDATOR: InetAddressValidator = InetAddressValidator()

    def isValidInet6Address(self, inet6Address: str) -> bool:
        parts: List[str] = inet6Address.split("/", -1)
        if len(parts) > 2:
            return False  # can only have one prefix specifier
        if len(parts) == 2:
            if parts[1].matches("\\d{1,3}"):  # Need to eliminate signs
                bits: int = int(parts[1])  # cannot fail because of RE check
                if bits < 0 or bits > 128:
                    return False  # out of range
            else:
                return False  # not a valid number
        parts = parts[0].split("%", -1)
        if len(parts) > 2:
            return False
        elif len(parts) == 2:
            if not parts[1].matches("[^\\s/%]+"):
                return False  # invalid id
        inet6Address = parts[0]
        containsCompressedZeroes: bool = inet6Address.contains("::")
        if containsCompressedZeroes and (
            inet6Address.indexOf("::") != inet6Address.lastIndexOf("::")
        ):
            return False
        if (inet6Address.startsWith(":") and not inet6Address.startsWith("::")) or (
            inet6Address.endsWith(":") and not inet6Address.endsWith("::")
        ):
            return False
        octets: List[str] = inet6Address.split(":")
        if containsCompressedZeroes:
            octetList: List[str] = list(octets)
            if inet6Address.endsWith("::"):
                octetList.append("")
            elif inet6Address.startsWith("::") and not octetList.isEmpty():
                octetList.remove(0)
            octets = octetList.toArray()
        if len(octets) > self.__IPV6_MAX_HEX_GROUPS:
            return False
        validOctets: int = 0
        emptyOctets: int = 0  # consecutive empty chunks
        for index in range(len(octets)):
            octet: str = octets[index]
            if len(octet) == 0:
                emptyOctets += 1
                if emptyOctets > 1:
                    return False
            else:
                emptyOctets = 0
                if index == len(octets) - 1 and octet.contains("."):
                    if not self.isValidInet4Address(octet):
                        return False
                    validOctets += 2
                    continue
                if len(octet) > self.__IPV6_MAX_HEX_DIGITS_PER_GROUP:
                    return False
                octetInt: int = 0
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
        groups: typing.List[str] = self.__ipv4Validator.match(inet4Address)

        if groups is None:
            return False

        for ipSegment in groups:
            if ipSegment is None or len(ipSegment) == 0:
                return False

            iIpSegment: int = 0

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
