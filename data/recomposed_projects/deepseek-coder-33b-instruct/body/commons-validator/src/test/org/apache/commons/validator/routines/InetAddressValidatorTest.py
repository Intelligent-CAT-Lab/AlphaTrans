from __future__ import annotations
import re
import os
from abc import ABC
import unittest
import pytest
import io
import unittest
from src.main.org.apache.commons.validator.routines.InetAddressValidator import *


class InetAddressValidatorTest(unittest.TestCase):

    __validator: InetAddressValidator = None

    def setUp(self) -> None:
        self.__validator = InetAddressValidator()

    def testIPv6(self) -> None:

        pass  # LLM could not translate this method

    def testBrokenInetAddresses(self) -> None:

        self.assertFalse(self.__validator.isValid("124.14.32.abc"))
        self.assertFalse(self.__validator.isValid("124.14.32.01"))
        self.assertFalse(self.__validator.isValid("23.64.12"))
        self.assertFalse(self.__validator.isValid("26.34.23.77.234"))
        self.assertFalse(self.__validator.isValid(""))

    def testReservedInetAddresses(self) -> None:

        self.assertTrue(
            "localhost IP should be valid", self.__validator.isValid("127.0.0.1")
        )
        self.assertTrue(
            "broadcast IP should be valid", self.__validator.isValid("255.255.255.255")
        )

    def testInetAddressesByClass(self) -> None:

        validator = InetAddressValidator()

        self.assertTrue("class A IP should be valid", validator.isValid("24.25.231.12"))
        self.assertFalse(
            "illegal class A IP should be invalid", validator.isValid("2.41.32.324")
        )

        self.assertTrue("class B IP should be valid", validator.isValid("135.14.44.12"))
        self.assertFalse(
            "illegal class B IP should be invalid", validator.isValid("154.123.441.123")
        )

        self.assertTrue(
            "class C IP should be valid", validator.isValid("213.25.224.32")
        )
        self.assertFalse(
            "illegal class C IP should be invalid", validator.isValid("201.543.23.11")
        )

        self.assertTrue("class D IP should be valid", validator.isValid("229.35.159.6"))
        self.assertFalse(
            "illegal class D IP should be invalid", validator.isValid("231.54.11.987")
        )

        self.assertTrue("class E IP should be valid", validator.isValid("248.85.24.92"))
        self.assertFalse(
            "illegal class E IP should be invalid", validator.isValid("250.21.323.48")
        )

    def testVALIDATOR_445(self) -> None:

        valid = [
            "2001:0000:1234:0000:0000:C1C0:ABCD:0876",
            "2001:0000:1234:0000:0000:C1C0:ABCD:0876/123",
            "2001:0000:1234:0000:0000:C1C0:ABCD:0876/0",
            "2001:0000:1234:0000:0000:C1C0:ABCD:0876%0",
            "2001:0000:1234:0000:0000:C1C0:ABCD:0876%abcdefgh",
        ]
        invalid = [
            "2001:0000:1234:0000:0000:C1C0:ABCD:0876/129",  # too big
            "2001:0000:1234:0000:0000:C1C0:ABCD:0876/-0",  # sign not allowed
            "2001:0000:1234:0000:0000:C1C0:ABCD:0876/+0",  # sign not allowed
            "2001:0000:1234:0000:0000:C1C0:ABCD:0876/10O",  # non-digit
            "2001:0000:1234:0000:0000:C1C0:ABCD:0876/0%0",  # /bits before %node-id
            "2001:0000:1234:0000:0000:C1C0:ABCD:0876%abc defgh",  # space in node id
            "2001:0000:1234:0000:0000:C1C0:ABCD:0876%abc%defgh",  # '%' in node id
        ]
        for item in valid:
            self.assertTrue(self.__validator.isValid(item), f"{item} should be valid")
        for item in invalid:
            self.assertFalse(
                self.__validator.isValid(item), f"{item} should be invalid"
            )

    def testVALIDATOR_419(self) -> None:

        addr = "0:0:0:0:0:0:13.1.68.3"
        self.assertTrue(self.__validator.isValid(addr))
        addr = "0:0:0:0:0:FFFF:129.144.52.38"
        self.assertTrue(self.__validator.isValid(addr))
        addr = "::13.1.68.3"
        self.assertTrue(self.__validator.isValid(addr))
        addr = "::FFFF:129.144.52.38"
        self.assertTrue(self.__validator.isValid(addr))

        addr = "::ffff:192.168.1.1:192.168.1.1"
        self.assertFalse(self.__validator.isValid(addr))
        addr = "::192.168.1.1:192.168.1.1"
        self.assertFalse(self.__validator.isValid(addr))

    def testVALIDATOR_335(self) -> None:

        self.assertTrue(
            self.__validator.isValid("2001:0438:FFFE:0000:0000:0000:0000:0A35"),
            "2001:0438:FFFE:0000:0000:0000:0000:0A35 should be valid",
        )

    def testInetAddressesFromTheWild(self) -> None:

        self.assertTrue(
            "www.apache.org IP should be valid",
            self.__validator.isValid("140.211.11.130"),
        )
        self.assertTrue(
            "www.l.google.com IP should be valid",
            self.__validator.isValid("72.14.253.103"),
        )
        self.assertTrue(
            "fsf.org IP should be valid", self.__validator.isValid("199.232.41.5")
        )
        self.assertTrue(
            "appscs.ign.com IP should be valid",
            self.__validator.isValid("216.35.123.87"),
        )

    def __init__(self, name: str) -> None:
        super().__init__(name)
        self.__validator = InetAddressValidator()
