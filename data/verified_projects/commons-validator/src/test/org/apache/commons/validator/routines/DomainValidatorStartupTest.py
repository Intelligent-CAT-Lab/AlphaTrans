import pytest

from src.main.org.apache.commons.validator.routines.DomainValidator import *
import unittest
from typing import *

class DomainValidatorStartupTest(unittest.TestCase):

    @pytest.mark.test
    def testUpdateBaseArrayCC(self) -> None:
        with self.assertRaises(ValueError):
            DomainValidator.updateTLDOverride(
                DomainValidator.ArrayType.COUNTRY_CODE_RO,
                ["com"]
            )

    
    @pytest.mark.test
    def testUpdateBaseArrayGeneric(self) -> None:
        with self.assertRaises(ValueError):
            DomainValidator.updateTLDOverride(
                DomainValidator.ArrayType.GENERIC_RO,
                ["com"]
            )

    
    @pytest.mark.test
    def testUpdateBaseArrayInfra(self) -> None:
        with self.assertRaises(ValueError):
            DomainValidator.updateTLDOverride(
                DomainValidator.ArrayType.INFRASTRUCTURE_RO,
                ["com"]
            )

    
    @pytest.mark.test
    def testUpdateBaseArrayLocal(self) -> None:
        with self.assertRaises(ValueError):
            DomainValidator.updateTLDOverride(
                DomainValidator.ArrayType.LOCAL_RO,
                ["com"]
            )

    
    @pytest.mark.test
    def testUpdateCountryCode1a(self) -> None:
        validator = DomainValidator.getInstance0()
        self.assertFalse(validator.isValidCountryCodeTld("com"))  # cannot be valid

    
    @pytest.mark.test
    def testUpdateCountryCode1b(self) -> None:
        DomainValidator.updateTLDOverride(
            DomainValidator.ArrayType.COUNTRY_CODE_PLUS,
            ["com"]
        )
        validator = DomainValidator.getInstance0()
        self.assertTrue(validator.isValidCountryCodeTld("com"))  # it is now!

    
    @pytest.mark.test
    def testUpdateCountryCode2(self) -> None:
        DomainValidator.updateTLDOverride(
            DomainValidator.ArrayType.COUNTRY_CODE_PLUS,
            ["com"]
        )
        DomainValidator.updateTLDOverride(
            DomainValidator.ArrayType.COUNTRY_CODE_MINUS,
            ["com"]
        )
        validator = DomainValidator.getInstance0()
        self.assertFalse(
            validator.isValidCountryCodeTld("com")
        )  # show that minus overrides the rest

    
    @pytest.mark.test
    def testUpdateCountryCode3a(self) -> None:
        validator = DomainValidator.getInstance0()
        self.assertTrue(validator.isValidCountryCodeTld("ch"))

    
    @pytest.mark.test
    def testUpdateCountryCode3b(self) -> None:
        DomainValidator.updateTLDOverride(
            DomainValidator.ArrayType.COUNTRY_CODE_MINUS,
            ["ch"]
        )
        validator = DomainValidator.getInstance0()
        self.assertFalse(validator.isValidCountryCodeTld("ch"))

    
    @pytest.mark.test
    def testUpdateCountryCode3c(self) -> None:
        DomainValidator.updateTLDOverride(
            DomainValidator.ArrayType.COUNTRY_CODE_MINUS,
            ["ch"]
        )
        DomainValidator.updateTLDOverride(
            DomainValidator.ArrayType.COUNTRY_CODE_MINUS,
            ["xx"]
        )
        validator = DomainValidator.getInstance0()
        self.assertTrue(validator.isValidCountryCodeTld("ch"))

    
    @pytest.mark.test
    def testUpdateGeneric1(self) -> None:
        validator = DomainValidator.getInstance0()
        self.assertFalse(validator.isValidGenericTld("ch"))  # cannot be valid

    
    @pytest.mark.test
    def testUpdateGeneric2(self) -> None:
        DomainValidator.updateTLDOverride(
            DomainValidator.ArrayType.GENERIC_PLUS,
            ["ch"]
        )
        validator = DomainValidator.getInstance0()
        self.assertTrue(validator.isValidGenericTld("ch"))  # it is now!

    
    @pytest.mark.test
    def testUpdateGeneric3(self) -> None:
        DomainValidator.updateTLDOverride(
            DomainValidator.ArrayType.GENERIC_PLUS,
            ["ch"]
        )
        DomainValidator.updateTLDOverride(
            DomainValidator.ArrayType.GENERIC_MINUS,
            ["ch"]
        )
        validator = DomainValidator.getInstance0()
        self.assertFalse(
            validator.isValidGenericTld("ch")
        )  # show that minus overrides the rest

        self.assertTrue(validator.isValidGenericTld("com"))

    
    @pytest.mark.test
    def testUpdateGeneric4(self) -> None:
        DomainValidator.updateTLDOverride(
            DomainValidator.ArrayType.GENERIC_PLUS,
            ["ch"]
        )
        DomainValidator.updateTLDOverride(
            DomainValidator.ArrayType.GENERIC_MINUS,
            ["ch"]
        )
        DomainValidator.updateTLDOverride(
            DomainValidator.ArrayType.GENERIC_MINUS,
            ["com"]
        )
        validator = DomainValidator.getInstance0()
        self.assertFalse(validator.isValidGenericTld("com"))

    
    @pytest.mark.test
    def testUpdateGeneric5(self) -> None:
        DomainValidator.updateTLDOverride(
            DomainValidator.ArrayType.GENERIC_PLUS,
            ["ch"]
        )
        DomainValidator.updateTLDOverride(
            DomainValidator.ArrayType.GENERIC_MINUS,
            ["ch"]
        )
        DomainValidator.updateTLDOverride(
            DomainValidator.ArrayType.GENERIC_MINUS,
            ["com"]
        )
        DomainValidator.updateTLDOverride(
            DomainValidator.ArrayType.GENERIC_MINUS,
            ["xx"]
        )  # change the minus list

        validator = DomainValidator.getInstance0()
        self.assertTrue(validator.isValidGenericTld("com"))

    
    @pytest.mark.test
    def testVALIDATOR_412a(self) -> None:
        validator = DomainValidator.getInstance0()
        self.assertFalse(validator.isValidGenericTld("local"))
        self.assertFalse(validator.isValid("abc.local"))
        self.assertFalse(validator.isValidGenericTld("pvt"))
        self.assertFalse(validator.isValid("abc.pvt"))

    
    @pytest.mark.test
    def testVALIDATOR_412b(self) -> None:
        DomainValidator.updateTLDOverride(
            DomainValidator.ArrayType.GENERIC_PLUS,
            ["local", "pvt"]
        )
        validator = DomainValidator.getInstance0()
        self.assertTrue(validator.isValidGenericTld("local"))
        self.assertTrue(validator.isValid("abc.local"))
        self.assertTrue(validator.isValidGenericTld("pvt"))
        self.assertTrue(validator.isValid("abc.pvt"))

    
    @pytest.mark.test
    def testVALIDATOR_412c(self) -> None:
        validator = DomainValidator.getInstance1(True)
        self.assertFalse(validator.isValidLocalTld("local"))
        self.assertFalse(validator.isValid("abc.local"))
        self.assertFalse(validator.isValidLocalTld("pvt"))
        self.assertFalse(validator.isValid("abc.pvt"))

    
    @pytest.mark.test
    def testVALIDATOR_412d(self) -> None:
        DomainValidator.updateTLDOverride(
            DomainValidator.ArrayType.LOCAL_PLUS,
            ["local", "pvt"]
        )
        validator = DomainValidator.getInstance1(True)
        self.assertTrue(validator.isValidLocalTld("local"))
        self.assertTrue(validator.isValidLocalTld("pvt"))
        self.assertTrue(validator.isValid("abc.local"))
        self.assertTrue(validator.isValid("abc.pvt"))

    @pytest.mark.test
    def testCannotUpdate(self) -> None:
        DomainValidator.updateTLDOverride(
            DomainValidator.ArrayType.GENERIC_PLUS,
            ["ch"]
        )  # OK

        dv = DomainValidator.getInstance0()
        self.assertIsNotNone(dv)
        try:
            DomainValidator.updateTLDOverride(
                DomainValidator.ArrayType.GENERIC_PLUS,
                ["ch"]
            )
            self.fail("Expected IllegalStateException")
        except RuntimeError as e:
            pass
            

    @pytest.mark.test
    def testInstanceOverride(self) -> None:
        # Show that the instance picks up static values
        DomainValidator.updateTLDOverride(
            DomainValidator.ArrayType.GENERIC_PLUS,
            ["gp"]
        )
        DomainValidator.updateTLDOverride(
            DomainValidator.ArrayType.GENERIC_MINUS,
            ["com"]
        )
        DomainValidator.updateTLDOverride(
            DomainValidator.ArrayType.COUNTRY_CODE_PLUS,
            ["cp"]
        )
        DomainValidator.updateTLDOverride(
            DomainValidator.ArrayType.COUNTRY_CODE_MINUS,
            ["ch"]
        )
        validator = DomainValidator.getInstance1(False)
        self.assertTrue(validator.isValidGenericTld("gp"))
        self.assertFalse(validator.isValidGenericTld("com"))
        self.assertTrue(validator.isValidCountryCodeTld("cp"))
        self.assertFalse(validator.isValidCountryCodeTld("ch"))

        items = [
            DomainValidator.Item(DomainValidator.ArrayType.GENERIC_MINUS, [""]),
            DomainValidator.Item(DomainValidator.ArrayType.COUNTRY_CODE_MINUS, [""])
        ]
        validator = DomainValidator.getInstance2(False, items)
        self.assertTrue(validator.isValidGenericTld("gp"))
        self.assertTrue(validator.isValidGenericTld("com"))  # Should be true again
        self.assertTrue(validator.isValidCountryCodeTld("cp"))
        self.assertTrue(validator.isValidCountryCodeTld("ch"))  # Should be true again

        validator = DomainValidator.getInstance1(False)
        self.assertTrue(validator.isValidGenericTld("gp"))
        self.assertFalse(validator.isValidGenericTld("com"))
        self.assertTrue(validator.isValidCountryCodeTld("cp"))
        self.assertFalse(validator.isValidCountryCodeTld("ch"))
