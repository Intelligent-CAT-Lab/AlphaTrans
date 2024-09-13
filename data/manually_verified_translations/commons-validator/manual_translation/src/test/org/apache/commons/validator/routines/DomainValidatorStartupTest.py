from __future__ import annotations
import time
import re
import typing
from typing import *
import unittest
import pytest
import io
import os
import unittest
from src.main.org.apache.commons.validator.routines.DomainValidator import *


class DomainValidatorStartupTest(unittest.TestCase):

    def setUp(self) -> None:
        DomainValidator._DomainValidator__inUse = False
        DomainValidator._DomainValidator__localTLDsPlus = []
        DomainValidator._DomainValidator__genericTLDsPlus = []

    def testInstanceOverride(self) -> None:

        DomainValidator.updateTLDOverride(ArrayType.GENERIC_PLUS, ["gp"])
        DomainValidator.updateTLDOverride(ArrayType.GENERIC_MINUS, ["com"])
        DomainValidator.updateTLDOverride(ArrayType.COUNTRY_CODE_PLUS, ["cp"])
        DomainValidator.updateTLDOverride(ArrayType.COUNTRY_CODE_MINUS, ["ch"])

        validator = DomainValidator.getInstance1(False)
        self.assertTrue(validator.isValidGenericTld("gp"))
        self.assertFalse(validator.isValidGenericTld("com"))
        self.assertTrue(validator.isValidCountryCodeTld("cp"))
        self.assertFalse(validator.isValidCountryCodeTld("ch"))

        items = [
            Item(ArrayType.GENERIC_MINUS, [""]),
            Item(ArrayType.COUNTRY_CODE_MINUS, [""]),
        ]
        validator = DomainValidator.getInstance2(False, items)
        self.assertTrue(validator.isValidGenericTld("gp"))
        self.assertTrue(validator.isValidGenericTld("com"))
        self.assertTrue(validator.isValidCountryCodeTld("cp"))
        self.assertTrue(validator.isValidCountryCodeTld("ch"))

        validator = DomainValidator.getInstance1(False)
        self.assertTrue(validator.isValidGenericTld("gp"))
        self.assertFalse(validator.isValidGenericTld("com"))
        self.assertTrue(validator.isValidCountryCodeTld("cp"))
        self.assertFalse(validator.isValidCountryCodeTld("ch"))

    def testCannotUpdate(self) -> None:

        DomainValidator.updateTLDOverride(ArrayType.GENERIC_PLUS, ["ch"])
        dv = DomainValidator.getInstance0()
        self.assertIsNotNone(dv)

        try:
            DomainValidator.updateTLDOverride(ArrayType.GENERIC_PLUS, ["ch"])
            self.fail("Expected RuntimeError")
        except RuntimeError as re:
            self.assertEqual(
                str(re), "Can only invoke this method before calling getInstance"
            )

    def testVALIDATOR_412d(self) -> None:

        DomainValidator.updateTLDOverride(ArrayType.LOCAL_PLUS, ["local", "pvt"])
        validator = DomainValidator.getInstance1(True)
        self.assertTrue(validator.isValidLocalTld("local"))
        self.assertTrue(validator.isValidLocalTld("pvt"))
        self.assertTrue(validator.isValid("abc.local"))
        self.assertTrue(validator.isValid("abc.pvt"))

    def testVALIDATOR_412c(self) -> None:

        validator = DomainValidator.getInstance1(True)
        self.assertFalse(validator.isValidLocalTld("local"))
        self.assertFalse(validator.isValid("abc.local"))
        self.assertFalse(validator.isValidLocalTld("pvt"))
        self.assertFalse(validator.isValid("abc.pvt"))

    def testVALIDATOR_412b(self) -> None:

        DomainValidator.updateTLDOverride(ArrayType.GENERIC_PLUS, ["local", "pvt"])
        validator = DomainValidator.getInstance0()
        self.assertTrue(validator.isValidGenericTld("local"))
        self.assertTrue(validator.isValid("abc.local"))
        self.assertTrue(validator.isValidGenericTld("pvt"))
        self.assertTrue(validator.isValid("abc.pvt"))

    def testVALIDATOR_412a(self) -> None:

        validator = DomainValidator.getInstance0()

        self.assertFalse(validator.isValidGenericTld("local"))
        self.assertFalse(validator.isValid("abc.local"))
        self.assertFalse(validator.isValidGenericTld("pvt"))
        self.assertFalse(validator.isValid("abc.pvt"))

    def testUpdateGeneric5(self) -> None:

        DomainValidator.updateTLDOverride(ArrayType.GENERIC_PLUS, ["ch"])
        DomainValidator.updateTLDOverride(ArrayType.GENERIC_MINUS, ["ch"])
        DomainValidator.updateTLDOverride(ArrayType.GENERIC_MINUS, ["com"])
        DomainValidator.updateTLDOverride(ArrayType.GENERIC_MINUS, ["xx"])

        validator = DomainValidator.getInstance0()
        self.assertTrue(validator.isValidGenericTld("com"))

    def testUpdateGeneric4(self) -> None:

        DomainValidator.updateTLDOverride(ArrayType.GENERIC_PLUS, ["ch"])
        DomainValidator.updateTLDOverride(ArrayType.GENERIC_MINUS, ["ch"])
        DomainValidator.updateTLDOverride(ArrayType.GENERIC_MINUS, ["com"])

        validator = DomainValidator.getInstance0()
        self.assertFalse(validator.isValidGenericTld("com"))

    def testUpdateGeneric3(self) -> None:

        DomainValidator.updateTLDOverride(ArrayType.GENERIC_PLUS, ["ch"])
        DomainValidator.updateTLDOverride(ArrayType.GENERIC_MINUS, ["ch"])
        validator = DomainValidator.getInstance0()
        self.assertFalse(validator.isValidGenericTld("ch"))
        self.assertTrue(validator.isValidGenericTld("com"))

    def testUpdateGeneric2(self) -> None:

        DomainValidator.updateTLDOverride(ArrayType.GENERIC_PLUS, ["ch"])
        validator = DomainValidator.getInstance0()
        self.assertTrue(validator.isValidGenericTld("ch"))

    def testUpdateGeneric1(self) -> None:

        validator = DomainValidator.getInstance0()
        self.assertFalse(validator.isValidGenericTld("ch"))

    def testUpdateCountryCode3c(self) -> None:

        DomainValidator.updateTLDOverride(ArrayType.COUNTRY_CODE_MINUS, ["ch"])
        DomainValidator.updateTLDOverride(ArrayType.COUNTRY_CODE_MINUS, ["xx"])
        validator = DomainValidator.getInstance0()
        self.assertTrue(validator.isValidCountryCodeTld("ch"))

    def testUpdateCountryCode3b(self) -> None:

        DomainValidator.updateTLDOverride(ArrayType.COUNTRY_CODE_MINUS, ["ch"])
        validator = DomainValidator.getInstance0()
        self.assertFalse(validator.isValidCountryCodeTld("ch"))

    def testUpdateCountryCode3a(self) -> None:

        validator = DomainValidator.getInstance0()
        self.assertTrue(validator.isValidCountryCodeTld("ch"))

    def testUpdateCountryCode2(self) -> None:

        DomainValidator.updateTLDOverride(ArrayType.COUNTRY_CODE_PLUS, ["com"])
        DomainValidator.updateTLDOverride(ArrayType.COUNTRY_CODE_MINUS, ["com"])
        validator = DomainValidator.getInstance0()
        self.assertFalse(validator.isValidCountryCodeTld("com"))

    def testUpdateCountryCode1b(self) -> None:

        DomainValidator.updateTLDOverride(ArrayType.COUNTRY_CODE_PLUS, ["com"])
        validator = DomainValidator.getInstance0()
        self.assertTrue(validator.isValidCountryCodeTld("com"))

    def testUpdateCountryCode1a(self) -> None:

        validator = DomainValidator.getInstance0()
        self.assertFalse(validator.isValidCountryCodeTld("com"))

    def testUpdateBaseArrayLocal(self) -> None:

        with pytest.raises(ValueError):
            DomainValidator.updateTLDOverride(ArrayType.LOCAL_RO, ["com"])

    def testUpdateBaseArrayInfra(self) -> None:

        with pytest.raises(ValueError):
            DomainValidator.updateTLDOverride(ArrayType.INFRASTRUCTURE_RO, ["com"])

    def testUpdateBaseArrayGeneric(self) -> None:

        with pytest.raises(ValueError):
            DomainValidator.updateTLDOverride(ArrayType.GENERIC_RO, ["com"])

    def testUpdateBaseArrayCC(self) -> None:

        with pytest.raises(ValueError):
            DomainValidator.updateTLDOverride(ArrayType.COUNTRY_CODE_RO, ["com"])
