# Imports Begin
from src.main.org.apache.commons.validator.routines.DomainValidator import *
import unittest
import typing
from typing import *

# Imports End


class DomainValidatorStartupTest(unittest.TestCase):

    # Class Fields Begin
    # Class Fields End

    # Class Methods Begin
    def testInstanceOverride(self) -> None:

        DomainValidator.updateTLDOverride(ArrayType.GENERIC_PLUS, ["gp"])
        DomainValidator.updateTLDOverride(ArrayType.GENERIC_MINUS, ["com"])
        DomainValidator.updateTLDOverride(ArrayType.COUNTRY_CODE_PLUS, ["cp"])
        DomainValidator.updateTLDOverride(ArrayType.COUNTRY_CODE_MINUS, ["ch"])
        validator = DomainValidator.getInstance1(False)
        assert validator.isValidGenericTld("gp")
        assert not validator.isValidGenericTld("com")
        assert validator.isValidCountryCodeTld("cp")
        assert not validator.isValidCountryCodeTld("ch")
        items = [
            DomainValidator.Item(ArrayType.GENERIC_MINUS, [""]),
            DomainValidator.Item(ArrayType.COUNTRY_CODE_MINUS, [""]),
        ]
        validator = DomainValidator.getInstance2(False, items)
        assert validator.isValidGenericTld("gp")
        assert validator.isValidGenericTld("com")  # Should be true again
        assert validator.isValidCountryCodeTld("cp")
        assert validator.isValidCountryCodeTld("ch")  # Should be true again
        validator = DomainValidator.getInstance1(False)
        assert validator.isValidGenericTld("gp")
        assert not validator.isValidGenericTld("com")
        assert validator.isValidCountryCodeTld("cp")
        assert not validator.isValidCountryCodeTld("ch")

    def testCannotUpdate(self) -> None:

        DomainValidator.updateTLDOverride(ArrayType.GENERIC_PLUS, ["ch"])
        dv = DomainValidator.getInstance0()
        self.assertIsNotNone(dv)
        with self.assertRaises(IllegalStateException):
            DomainValidator.updateTLDOverride(ArrayType.GENERIC_PLUS, ["ch"])

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
        self.assertFalse(
            validator.isValidGenericTld("ch")
        )  # show that minus overrides the rest
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
        self.assertFalse(
            validator.isValidCountryCodeTld("com")
        )  # show that minus overrides the rest

    def testUpdateCountryCode1b(self) -> None:

        DomainValidator.updateTLDOverride(ArrayType.COUNTRY_CODE_PLUS, ["com"])
        validator = DomainValidator.getInstance0()
        self.assertTrue(validator.isValidCountryCodeTld("com"))

    def testUpdateCountryCode1a(self) -> None:

        validator = DomainValidator.getInstance0()
        self.assertFalse(validator.isValidCountryCodeTld("com"))

    def testUpdateBaseArrayLocal(self) -> None:

        self.updateTLDOverride(ArrayType.LOCAL_RO, ["com"])

    def testUpdateBaseArrayInfra(self) -> None:

        self.updateTLDOverride(ArrayType.INFRASTRUCTURE_RO, ["com"])

    def testUpdateBaseArrayGeneric(self) -> None:

        self.updateTLDOverride(ArrayType.GENERIC_RO, ["com"])

    def testUpdateBaseArrayCC(self) -> None:

        self.updateTLDOverride(ArrayType.COUNTRY_CODE_RO, ["com"])

    # Class Methods End
