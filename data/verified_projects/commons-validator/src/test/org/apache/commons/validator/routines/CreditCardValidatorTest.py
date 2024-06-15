import pytest

from src.main.org.apache.commons.validator.routines.checkdigit.LuhnCheckDigit import *
from src.main.org.apache.commons.validator.routines.checkdigit.CheckDigit import *
from src.main.org.apache.commons.validator.routines.RegexValidator import *
from src.main.org.apache.commons.validator.routines.CreditCardValidator import *
from src.main.org.apache.commons.validator.routines.CodeValidator import *
import unittest

class CreditCardValidatorTest(unittest.TestCase):

    __VALID_VISA = "4417123456789113"  # 16
    __ERROR_VISA = "4417123456789112"
    __VALID_SHORT_VISA = "4222222222222"  # 13
    __ERROR_SHORT_VISA = "4222222222229"
    __VALID_AMEX = "378282246310005"  # 15
    __ERROR_AMEX = "378282246310001"
    __VALID_MASTERCARD = "5105105105105100"
    __ERROR_MASTERCARD = "5105105105105105"
    __VALID_DISCOVER = "6011000990139424"
    __ERROR_DISCOVER = "6011000990139421"
    __VALID_DISCOVER65 = "6534567890123458" 
    __ERROR_DISCOVER65 = "6534567890123450"
    __VALID_DINERS = "30569309025904"  # 14
    __ERROR_DINERS = "30569309025901"
    __VALID_VPAY = "4370000000000061"  # 16
    __VALID_VPAY2 = "4370000000000012"
    __ERROR_VPAY = "4370000000000069"

    __VALID_CARDS = [
        __VALID_VISA,
        __VALID_SHORT_VISA,
        __VALID_AMEX,
        __VALID_MASTERCARD,
        __VALID_DISCOVER,
        __VALID_DISCOVER65,
        __VALID_DINERS,
        __VALID_VPAY,
        __VALID_VPAY2,
        "60115564485789458",  # VALIDATOR-403
    ]

    __ERROR_CARDS = [
        __ERROR_VISA,
        __ERROR_SHORT_VISA,
        __ERROR_AMEX,
        __ERROR_MASTERCARD,
        __ERROR_DISCOVER,
        __ERROR_DISCOVER65,
        __ERROR_DINERS,
        __ERROR_VPAY,
        "",
        "12345678901",  # too short (11)
        "12345678901234567890",  # too long (20)
        "4417123456789112",  # invalid check digit
    ]

    
    def __init__(self, methodName='runTest') -> None:
        super().__init__(methodName)

    
    @pytest.mark.test
    def testIsValid(self) -> None:
        ccv = CreditCardValidator.CreditCardValidator0()

        self.assertIsNone(ccv.validate(None))

        self.assertFalse(ccv.isValid(None))
        self.assertFalse(ccv.isValid(""))
        self.assertFalse(ccv.isValid("123456789012"))  # too short
        self.assertFalse(ccv.isValid("12345678901234567890"))  # too long
        self.assertFalse(ccv.isValid("4417123456789112"))
        self.assertFalse(ccv.isValid("4417q23456w89113"))
        self.assertTrue(ccv.isValid(CreditCardValidatorTest.__VALID_VISA))
        self.assertTrue(ccv.isValid(CreditCardValidatorTest.__VALID_SHORT_VISA))
        self.assertTrue(ccv.isValid(CreditCardValidatorTest.__VALID_AMEX))
        self.assertTrue(ccv.isValid(CreditCardValidatorTest.__VALID_MASTERCARD))
        self.assertTrue(ccv.isValid(CreditCardValidatorTest.__VALID_DISCOVER))
        self.assertTrue(ccv.isValid(CreditCardValidatorTest.__VALID_DISCOVER65))

        self.assertFalse(ccv.isValid(CreditCardValidatorTest.__ERROR_VISA))
        self.assertFalse(ccv.isValid(CreditCardValidatorTest.__ERROR_SHORT_VISA))
        self.assertFalse(ccv.isValid(CreditCardValidatorTest.__ERROR_AMEX))
        self.assertFalse(ccv.isValid(CreditCardValidatorTest.__ERROR_MASTERCARD))
        self.assertFalse(ccv.isValid(CreditCardValidatorTest.__ERROR_DISCOVER))
        self.assertFalse(ccv.isValid(CreditCardValidatorTest.__ERROR_DISCOVER65))

        ccv = CreditCardValidator(0, CreditCardValidator.AMEX, None, None)
        self.assertFalse(ccv.isValid("4417123456789113"))


    @pytest.mark.test
    def testAddAllowedCardType(self) -> None:
        ccv = CreditCardValidator(0, CreditCardValidator.NONE, None, None)
        self.assertFalse(ccv.isValid(CreditCardValidatorTest.__VALID_VISA))
        self.assertFalse(ccv.isValid(CreditCardValidatorTest.__VALID_AMEX))
        self.assertFalse(ccv.isValid(CreditCardValidatorTest.__VALID_MASTERCARD))
        self.assertFalse(ccv.isValid(CreditCardValidatorTest.__VALID_DISCOVER))
        self.assertFalse(ccv.isValid(CreditCardValidatorTest.__VALID_DINERS))

    
    @pytest.mark.test
    def testArrayConstructor(self) -> None:
        ccv = CreditCardValidator(
            1,
            0,
            None,
            [
                CreditCardValidator.VISA_VALIDATOR, 
                CreditCardValidator.AMEX_VALIDATOR
            ]
        )

        self.assertTrue(ccv.isValid(CreditCardValidatorTest.__VALID_VISA))
        self.assertTrue(ccv.isValid(CreditCardValidatorTest.__VALID_SHORT_VISA))
        self.assertTrue(ccv.isValid(CreditCardValidatorTest.__VALID_AMEX))
        self.assertFalse(ccv.isValid(CreditCardValidatorTest.__VALID_MASTERCARD))
        self.assertFalse(ccv.isValid(CreditCardValidatorTest.__VALID_DISCOVER))

        self.assertFalse(ccv.isValid(CreditCardValidatorTest.__ERROR_VISA))
        self.assertFalse(ccv.isValid(CreditCardValidatorTest.__ERROR_SHORT_VISA))
        self.assertFalse(ccv.isValid(CreditCardValidatorTest.__ERROR_AMEX))
        self.assertFalse(ccv.isValid(CreditCardValidatorTest.__ERROR_MASTERCARD))
        self.assertFalse(ccv.isValid(CreditCardValidatorTest.__ERROR_DISCOVER))

        try:
            CreditCardValidator(1, 0, None, None)
            self.fail("Expected IllegalArgumentException")
        except ValueError as iae:
            pass

    
    @pytest.mark.test
    def testAmexValidator(self) -> None:
        validator = CreditCardValidator.AMEX_VALIDATOR
        regex = validator.getRegexValidator()

        self.assertFalse(regex.isValid("343456789012"), "Length 12")
        self.assertFalse(regex.isValid("3434567890123"), "Length 13")
        self.assertFalse(regex.isValid("34345678901234"), "Length 14")
        self.assertTrue(regex.isValid("343456789012345"), "Length 15")
        self.assertFalse(regex.isValid("3434567890123456"), "Length 16")
        self.assertFalse(regex.isValid("34345678901234567"), "Length 17")
        self.assertFalse(regex.isValid("343456789012345678"), "Length 18")
        self.assertFalse(regex.isValid("333456789012345"), "Prefix 33")
        self.assertTrue(regex.isValid("343456789012345"), "Prefix 34")
        self.assertFalse(regex.isValid("353456789012345"), "Prefix 35")
        self.assertFalse(regex.isValid("363456789012345"), "Prefix 36")
        self.assertTrue(regex.isValid("373456789012345"), "Prefix 37")
        self.assertFalse(regex.isValid("383456789012345"), "Prefix 38")
        self.assertFalse(regex.isValid("413456789012345"), "Prefix 41")
        self.assertFalse(regex.isValid("3434567x9012345"), "Invalid Char")

        self.assertTrue(regex.isValid(CreditCardValidatorTest.__ERROR_AMEX), "Valid regex")
        self.assertFalse(validator.isValid(CreditCardValidatorTest.__ERROR_AMEX), "Invalid")
        self.assertIsNone(validator.validate(CreditCardValidatorTest.__ERROR_AMEX), "validate()")
        self.assertEqual(
            validator.validate(CreditCardValidatorTest.__VALID_AMEX),
            CreditCardValidatorTest.__VALID_AMEX
        )

        self.assertTrue(validator.isValid(CreditCardValidatorTest.__VALID_AMEX), "Amex")
        self.assertFalse(validator.isValid(CreditCardValidatorTest.__VALID_DINERS), "Diners")
        self.assertFalse(validator.isValid(CreditCardValidatorTest.__VALID_DISCOVER), "Discover")
        self.assertFalse(
            validator.isValid(CreditCardValidatorTest.__VALID_MASTERCARD),
            "Mastercard"
        )
        self.assertFalse(validator.isValid(CreditCardValidatorTest.__VALID_VISA), "Visa")
        self.assertFalse(
            validator.isValid(CreditCardValidatorTest.__VALID_SHORT_VISA),
            "Visa Short"
        )

        self.assertTrue(validator.isValid("371449635398431"), "Valid-A")
        self.assertTrue(validator.isValid("340000000000009"), "Valid-B")
        self.assertTrue(validator.isValid("370000000000002"), "Valid-C")
        self.assertTrue(validator.isValid("378734493671000"), "Valid-D")

    
    @pytest.mark.test
    def testAmexOption(self) -> None:
        validator = CreditCardValidator(0, CreditCardValidator.AMEX, None, None)
        self.assertFalse(validator.isValid(CreditCardValidatorTest.__ERROR_AMEX), "Invalid")
        self.assertIsNone(validator.validate(CreditCardValidatorTest.__ERROR_AMEX), "validate()")
        self.assertEqual(
            validator.validate(CreditCardValidatorTest.__VALID_AMEX),
            CreditCardValidatorTest.__VALID_AMEX
        )

        self.assertTrue(validator.isValid(CreditCardValidatorTest.__VALID_AMEX), "Amex")
        self.assertFalse(validator.isValid(CreditCardValidatorTest.__VALID_DINERS), "Diners")
        self.assertFalse(validator.isValid(CreditCardValidatorTest.__VALID_DISCOVER), "Discover")
        self.assertFalse(
            validator.isValid(CreditCardValidatorTest.__VALID_MASTERCARD),
            "Mastercard"
        )
        self.assertFalse(validator.isValid(CreditCardValidatorTest.__VALID_VISA), "Visa")
        self.assertFalse(
            validator.isValid(CreditCardValidatorTest.__VALID_SHORT_VISA),
            "Visa Short"
        )

    
    @pytest.mark.test
    def testDinersValidator(self) -> None:
        validator = CreditCardValidator.DINERS_VALIDATOR
        regex = validator.getRegexValidator()

        self.assertFalse(regex.isValid("300456789012"), "Length 12-300")
        self.assertFalse(regex.isValid("363456789012"), "Length 12-36")
        self.assertFalse(regex.isValid("3004567890123"), "Length 13-300")
        self.assertFalse(regex.isValid("3634567890123"), "Length 13-36")
        self.assertTrue(regex.isValid("30045678901234"), "Length 14-300")
        self.assertTrue(regex.isValid("36345678901234"), "Length 14-36")
        self.assertFalse(regex.isValid("300456789012345"), "Length 15-300")
        self.assertFalse(regex.isValid("363456789012345"), "Length 15-36")
        self.assertFalse(regex.isValid("3004567890123456"), "Length 16-300")
        self.assertFalse(regex.isValid("3634567890123456"), "Length 16-36")
        self.assertFalse(regex.isValid("30045678901234567"), "Length 17-300")
        self.assertFalse(regex.isValid("36345678901234567"), "Length 17-36")
        self.assertFalse(regex.isValid("300456789012345678"), "Length 18-300")
        self.assertFalse(regex.isValid("363456789012345678"), "Length 18-36")

        self.assertTrue(regex.isValid("30045678901234"), "Prefix 300")
        self.assertTrue(regex.isValid("30145678901234"), "Prefix 301")
        self.assertTrue(regex.isValid("30245678901234"), "Prefix 302")
        self.assertTrue(regex.isValid("30345678901234"), "Prefix 303")
        self.assertTrue(regex.isValid("30445678901234"), "Prefix 304")
        self.assertTrue(regex.isValid("30545678901234"), "Prefix 305")
        self.assertFalse(regex.isValid("30645678901234"), "Prefix 306")
        self.assertFalse(regex.isValid("30945678901234"), "Prefix 3094")
        self.assertTrue(regex.isValid("30955678901234"), "Prefix 3095")
        self.assertFalse(regex.isValid("30965678901234"), "Prefix 3096")
        self.assertFalse(regex.isValid("35345678901234"), "Prefix 35")
        self.assertTrue(regex.isValid("36345678901234"), "Prefix 36")
        self.assertFalse(regex.isValid("37345678901234"), "Prefix 37")
        self.assertTrue(regex.isValid("38345678901234"), "Prefix 38")
        self.assertTrue(regex.isValid("39345678901234"), "Prefix 39")

        self.assertFalse(regex.isValid("3004567x901234"), "Invalid Char-A")
        self.assertFalse(regex.isValid("3634567x901234"), "Invalid Char-B")

        self.assertTrue(regex.isValid(CreditCardValidatorTest.__ERROR_DINERS), "Valid regex")
        self.assertFalse(validator.isValid(CreditCardValidatorTest.__ERROR_DINERS), "Invalid")
        self.assertIsNone(
            validator.validate(CreditCardValidatorTest.__ERROR_DINERS),
            "validate()"
        )
        self.assertEqual(
            validator.validate(CreditCardValidatorTest.__VALID_DINERS),
            CreditCardValidatorTest.__VALID_DINERS
        )

        self.assertFalse(validator.isValid(CreditCardValidatorTest.__VALID_AMEX), "Amex")
        self.assertTrue(validator.isValid(CreditCardValidatorTest.__VALID_DINERS), "Diners")
        self.assertFalse(
            validator.isValid(CreditCardValidatorTest.__VALID_DISCOVER),
            "Discover"
        )
        self.assertFalse(
            validator.isValid(CreditCardValidatorTest.__VALID_MASTERCARD),
            "Mastercard"
        )
        self.assertFalse(validator.isValid(CreditCardValidatorTest.__VALID_VISA), "Visa")
        self.assertFalse(
            validator.isValid(CreditCardValidatorTest.__VALID_SHORT_VISA),
            "Visa Short"
        )

        self.assertTrue(validator.isValid("30000000000004"), "Valid-A")
        self.assertTrue(validator.isValid("30123456789019"), "Valid-B")
        self.assertTrue(validator.isValid("36432685260294"), "Valid-C")


    @pytest.mark.test
    def testDinersOption(self) -> None:
        validator = CreditCardValidator(0, CreditCardValidator.DINERS, None, None)
        self.assertFalse(validator.isValid(CreditCardValidatorTest.__ERROR_DINERS), "Invalid")
        self.assertIsNone(
            validator.validate(CreditCardValidatorTest.__ERROR_DINERS),
            "validate()"
        )
        self.assertEqual(
            validator.validate(CreditCardValidatorTest.__VALID_DINERS),
            CreditCardValidatorTest.__VALID_DINERS
        )

        self.assertFalse(validator.isValid(CreditCardValidatorTest.__VALID_AMEX), "Amex")
        self.assertTrue(validator.isValid(CreditCardValidatorTest.__VALID_DINERS), "Diners")
        self.assertFalse(
            validator.isValid(CreditCardValidatorTest.__VALID_DISCOVER),
            "Discover"
        )
        self.assertFalse(
            validator.isValid(CreditCardValidatorTest.__VALID_MASTERCARD),
            "Mastercard"
        )
        self.assertFalse(validator.isValid(CreditCardValidatorTest.__VALID_VISA), "Visa")
        self.assertFalse(
            validator.isValid(CreditCardValidatorTest.__VALID_SHORT_VISA),
            "Visa Short"
        )

    
    @pytest.mark.test
    def testDiscoverValidator(self) -> None:
        validator = CreditCardValidator.DISCOVER_VALIDATOR
        regex = validator.getRegexValidator()

        self.assertFalse(regex.isValid("601156789012"), "Length 12-6011")
        self.assertFalse(regex.isValid("653456789012"), "Length 12-65")
        self.assertFalse(regex.isValid("6011567890123"), "Length 13-6011")
        self.assertFalse(regex.isValid("6534567890123"), "Length 13-65")
        self.assertFalse(regex.isValid("60115678901234"), "Length 14-6011")
        self.assertFalse(regex.isValid("65345678901234"), "Length 14-65")
        self.assertFalse(regex.isValid("601156789012345"), "Length 15-6011")
        self.assertFalse(regex.isValid("653456789012345"), "Length 15-65")
        self.assertTrue(regex.isValid("6011567890123456"), "Length 16-6011")
        self.assertTrue(regex.isValid("6444567890123456"), "Length 16-644")
        self.assertTrue(regex.isValid("6484567890123456"), "Length 16-648")
        self.assertTrue(regex.isValid("6534567890123456"), "Length 16-65")
        self.assertFalse(regex.isValid("65345678901234567"), "Length 17-65")
        self.assertFalse(regex.isValid("601156789012345678"), "Length 18-6011")
        self.assertFalse(regex.isValid("653456789012345678"), "Length 18-65")

        self.assertFalse(regex.isValid("6404567890123456"), "Prefix 640")
        self.assertFalse(regex.isValid("6414567890123456"), "Prefix 641")
        self.assertFalse(regex.isValid("6424567890123456"), "Prefix 642")
        self.assertFalse(regex.isValid("6434567890123456"), "Prefix 643")
        self.assertFalse(regex.isValid("6010567890123456"), "Prefix 6010")
        self.assertFalse(regex.isValid("6012567890123456"), "Prefix 6012")
        self.assertFalse(regex.isValid("6011567x90123456"), "Invalid Char")

        self.assertTrue(regex.isValid(CreditCardValidatorTest.__ERROR_DISCOVER), "Valid regex")
        self.assertTrue(
            regex.isValid(CreditCardValidatorTest.__ERROR_DISCOVER65),
            "Valid regex65"
        )
        self.assertFalse(validator.isValid(CreditCardValidatorTest.__ERROR_DISCOVER), "Invalid")
        self.assertFalse(
            validator.isValid(CreditCardValidatorTest.__ERROR_DISCOVER65),
            "Invalid65"
        )
        self.assertIsNone(
            validator.validate(CreditCardValidatorTest.__ERROR_DISCOVER),
            "validate()"
        )
        self.assertEqual(
            validator.validate(CreditCardValidatorTest.__VALID_DISCOVER),
            CreditCardValidatorTest.__VALID_DISCOVER
        )
        self.assertEqual(
            validator.validate(CreditCardValidatorTest.__VALID_DISCOVER65),
            CreditCardValidatorTest.__VALID_DISCOVER65
        )

        self.assertFalse(validator.isValid(CreditCardValidatorTest.__VALID_AMEX), "Amex")
        self.assertFalse(validator.isValid(CreditCardValidatorTest.__VALID_DINERS), "Diners")
        self.assertTrue(validator.isValid(CreditCardValidatorTest.__VALID_DISCOVER), "Discover")
        self.assertTrue(
            validator.isValid(CreditCardValidatorTest.__VALID_DISCOVER65),
            "Discover"
        )
        self.assertFalse(
            validator.isValid(CreditCardValidatorTest.__VALID_MASTERCARD),
            "Mastercard"
        )
        self.assertFalse(validator.isValid(CreditCardValidatorTest.__VALID_VISA), "Visa")
        self.assertFalse(
            validator.isValid(CreditCardValidatorTest.__VALID_SHORT_VISA),
            "Visa Short"
        )

        self.assertTrue(validator.isValid("6011111111111117"), "Valid-A")
        self.assertTrue(validator.isValid("6011000000000004"), "Valid-B")
        self.assertTrue(validator.isValid("6011000000000012"), "Valid-C")

    
    @pytest.mark.test
    def testDiscoverOption(self) -> None:
        validator = CreditCardValidator(0, CreditCardValidator.DISCOVER, None, None)
        self.assertFalse(
            validator.isValid(CreditCardValidatorTest.__ERROR_DISCOVER),
            "Invalid"
        )
        self.assertFalse(
            validator.isValid(CreditCardValidatorTest.__ERROR_DISCOVER65),
            "Invalid65"
        )
        self.assertIsNone(
            validator.validate(CreditCardValidatorTest.__ERROR_DISCOVER),
            "validate()"
        )
        self.assertEqual(
            validator.validate(CreditCardValidatorTest.__VALID_DISCOVER),
            CreditCardValidatorTest.__VALID_DISCOVER
        )
        self.assertEqual(
            validator.validate(CreditCardValidatorTest.__VALID_DISCOVER65),
            CreditCardValidatorTest.__VALID_DISCOVER65
        )

        self.assertFalse(validator.isValid(CreditCardValidatorTest.__VALID_AMEX), "Amex")
        self.assertFalse(validator.isValid(CreditCardValidatorTest.__VALID_DINERS), "Diners")
        self.assertTrue(
            validator.isValid(CreditCardValidatorTest.__VALID_DISCOVER),
            "Discover"
        )
        self.assertTrue(
            validator.isValid(CreditCardValidatorTest.__VALID_DISCOVER65),
            "Discover"
        )
        self.assertFalse(
            validator.isValid(CreditCardValidatorTest.__VALID_MASTERCARD),
            "Mastercard"
        )
        self.assertFalse(
            validator.isValid(CreditCardValidatorTest.__VALID_VISA),
            "Visa"
        )
        self.assertFalse(
            validator.isValid(CreditCardValidatorTest.__VALID_SHORT_VISA),
            "Visa Short"
        )
    

    @pytest.mark.test
    def testMastercardValidator(self) -> None:
        validator = CreditCardValidator.MASTERCARD_VALIDATOR
        regex = validator.getRegexValidator()

        self.assertFalse(regex.isValid("513456789012"), "Length 12")
        self.assertFalse(regex.isValid("5134567890123"), "Length 13")
        self.assertFalse(regex.isValid("51345678901234"), "Length 14")
        self.assertFalse(regex.isValid("513456789012345"), "Length 15")
        self.assertTrue(regex.isValid("5134567890123456"), "Length 16")
        self.assertFalse(regex.isValid("51345678901234567"), "Length 17")
        self.assertFalse(regex.isValid("513456789012345678"), "Length 18")
        self.assertFalse(regex.isValid("4134567890123456"), "Prefix 41")
        self.assertFalse(regex.isValid("5034567890123456"), "Prefix 50")
        self.assertTrue(regex.isValid("5134567890123456"), "Prefix 51")
        self.assertTrue(regex.isValid("5234567890123456"), "Prefix 52")
        self.assertTrue(regex.isValid("5334567890123456"), "Prefix 53")
        self.assertTrue(regex.isValid("5434567890123456"), "Prefix 54")
        self.assertTrue(regex.isValid("5534567890123456"), "Prefix 55")
        self.assertFalse(regex.isValid("5634567890123456"), "Prefix 56")
        self.assertFalse(regex.isValid("6134567890123456"), "Prefix 61")
        self.assertFalse(regex.isValid("5134567x90123456"), "Invalid Char")

        self.assertTrue(
            regex.isValid(CreditCardValidatorTest.__ERROR_MASTERCARD),
            "Valid regex"
        )
        self.assertFalse(
            validator.isValid(CreditCardValidatorTest.__ERROR_MASTERCARD),
            "Invalid"
        )
        self.assertIsNone(
            validator.validate(CreditCardValidatorTest.__ERROR_MASTERCARD),
            "validate()"
        )
        self.assertEqual(
            validator.validate(CreditCardValidatorTest.__VALID_MASTERCARD),
            CreditCardValidatorTest.__VALID_MASTERCARD
        )

        self.assertFalse(validator.isValid(CreditCardValidatorTest.__VALID_AMEX), "Amex")
        self.assertFalse(validator.isValid(CreditCardValidatorTest.__VALID_DINERS), "Diners")
        self.assertFalse(
            validator.isValid(CreditCardValidatorTest.__VALID_DISCOVER),
            "Discover"
        )
        self.assertTrue(
            validator.isValid(CreditCardValidatorTest.__VALID_MASTERCARD),
            "Mastercard"
        )
        self.assertFalse(validator.isValid(CreditCardValidatorTest.__VALID_VISA), "Visa")
        self.assertFalse(
            validator.isValid(CreditCardValidatorTest.__VALID_SHORT_VISA),
            "Visa Short"
        )

        self.assertTrue(validator.isValid("5500000000000004"), "Valid-A")
        self.assertTrue(validator.isValid("5424000000000015"), "Valid-B")
        self.assertTrue(validator.isValid("5301250070000191"), "Valid-C")
        self.assertTrue(validator.isValid("5123456789012346"), "Valid-D")
        self.assertTrue(validator.isValid("5555555555554444"), "Valid-E")

        rev = validator.getRegexValidator()
        PAD = "0000000000"
        self.assertFalse(rev.isValid("222099" + PAD), "222099")
        for i in range(222100, 272100):
            j = str(i) + PAD
            self.assertTrue(rev.isValid(j), j)
        self.assertFalse(rev.isValid("272100" + PAD), "272100")

    
    @pytest.mark.test
    def testMastercardOption(self) -> None:
        validator = CreditCardValidator(0, CreditCardValidator.MASTERCARD, None, None)
        self.assertFalse(
            validator.isValid(CreditCardValidatorTest.__ERROR_MASTERCARD),
            "Invalid"
        )
        self.assertIsNone(
            validator.validate(CreditCardValidatorTest.__ERROR_MASTERCARD),
            "validate()"
        )
        self.assertEqual(
            validator.validate(CreditCardValidatorTest.__VALID_MASTERCARD),
            CreditCardValidatorTest.__VALID_MASTERCARD
        )

        self.assertFalse(validator.isValid(CreditCardValidatorTest.__VALID_AMEX), "Amex")
        self.assertFalse(validator.isValid(CreditCardValidatorTest.__VALID_DINERS), "Diners")
        self.assertFalse(
            validator.isValid(CreditCardValidatorTest.__VALID_DISCOVER),
            "Discover"
        )
        self.assertTrue(
            validator.isValid(CreditCardValidatorTest.__VALID_MASTERCARD),
            "Mastercard"
        )
        self.assertFalse(validator.isValid(CreditCardValidatorTest.__VALID_VISA), "Visa")
        self.assertFalse(
            validator.isValid(CreditCardValidatorTest.__VALID_SHORT_VISA),
            "Visa Short"
        )

    @pytest.mark.test
    def testVisaValidator(self) -> None:
        validator = CreditCardValidator.VISA_VALIDATOR
        regex = validator.getRegexValidator()

        self.assertFalse(regex.isValid("423456789012"), "Length 12")
        self.assertTrue(regex.isValid("4234567890123"), "Length 13")
        self.assertFalse(regex.isValid("42345678901234"), "Length 14")
        self.assertFalse(regex.isValid("423456789012345"), "Length 15")
        self.assertTrue(regex.isValid("4234567890123456"), "Length 16")
        self.assertFalse(regex.isValid("42345678901234567"), "Length 17")
        self.assertFalse(regex.isValid("423456789012345678"), "Length 18")
        self.assertFalse(regex.isValid("3234567890123"), "Invalid Pref-A")
        self.assertFalse(regex.isValid("3234567890123456"), "Invalid Pref-B")
        self.assertFalse(regex.isValid("4234567x90123"), "Invalid Char-A")
        self.assertFalse(regex.isValid("4234567x90123456"), "Invalid Char-B")

        self.assertTrue(regex.isValid(CreditCardValidatorTest.__ERROR_VISA), "Valid regex")
        self.assertTrue(
            regex.isValid(CreditCardValidatorTest.__ERROR_SHORT_VISA),
            "Valid regex-S"
        )
        self.assertFalse(validator.isValid(CreditCardValidatorTest.__ERROR_VISA), "Invalid")
        self.assertFalse(
            validator.isValid(CreditCardValidatorTest.__ERROR_SHORT_VISA),
            "Invalid-S"
        )
        self.assertIsNone(
            validator.validate(CreditCardValidatorTest.__ERROR_VISA),
            "validate()"
        )
        self.assertEqual(
            validator.validate(CreditCardValidatorTest.__VALID_VISA),
            CreditCardValidatorTest.__VALID_VISA
        )
        self.assertEqual(
            validator.validate(CreditCardValidatorTest.__VALID_SHORT_VISA),
            CreditCardValidatorTest.__VALID_SHORT_VISA
        )

        self.assertFalse(validator.isValid(CreditCardValidatorTest.__VALID_AMEX), "Amex")
        self.assertFalse(validator.isValid(CreditCardValidatorTest.__VALID_DINERS), "Diners")
        self.assertFalse(
            validator.isValid(CreditCardValidatorTest.__VALID_DISCOVER),
            "Discover"
        )
        self.assertFalse(
            validator.isValid(CreditCardValidatorTest.__VALID_MASTERCARD),
            "Mastercard"
        )
        self.assertTrue(validator.isValid(CreditCardValidatorTest.__VALID_VISA), "Visa")
        self.assertTrue(
            validator.isValid(CreditCardValidatorTest.__VALID_SHORT_VISA),
            "Visa Short"
        )

        self.assertTrue(validator.isValid("4111111111111111"), "Valid-A")
        self.assertTrue(validator.isValid("4543059999999982"), "Valid-C")
        self.assertTrue(validator.isValid("4462000000000003"), "Valid-B")
        self.assertTrue(validator.isValid("4508750000000009"), "Valid-D")  # Electron
        self.assertTrue(validator.isValid("4012888888881881"), "Valid-E")
    

    @pytest.mark.test
    def testVisaOption(self) -> None:
        validator = CreditCardValidator(0, CreditCardValidator.VISA, None, None)
        self.assertFalse(validator.isValid(CreditCardValidatorTest.__ERROR_VISA), "Invalid")
        self.assertFalse(
            validator.isValid(CreditCardValidatorTest.__ERROR_SHORT_VISA),
            "Invalid-S"
        )
        self.assertIsNone(
            validator.validate(CreditCardValidatorTest.__ERROR_VISA),
            "validate()"
        )
        self.assertEqual(
            validator.validate(CreditCardValidatorTest.__VALID_VISA),
            CreditCardValidatorTest.__VALID_VISA
        )
        self.assertEqual(
            validator.validate(CreditCardValidatorTest.__VALID_SHORT_VISA),
            CreditCardValidatorTest.__VALID_SHORT_VISA
        )

        self.assertFalse(validator.isValid(CreditCardValidatorTest.__VALID_AMEX), "Amex")
        self.assertFalse(validator.isValid(CreditCardValidatorTest.__VALID_DINERS), "Diners")
        self.assertFalse(
            validator.isValid(CreditCardValidatorTest.__VALID_DISCOVER),
            "Discover"
        )
        self.assertFalse(
            validator.isValid(CreditCardValidatorTest.__VALID_MASTERCARD),
            "Mastercard"
        )
        self.assertTrue(validator.isValid(CreditCardValidatorTest.__VALID_VISA), "Visa")
        self.assertTrue(
            validator.isValid(CreditCardValidatorTest.__VALID_SHORT_VISA),
            "Visa Short"
        )

    
    @pytest.mark.test
    def testVPayOption(self) -> None:
        validator = CreditCardValidator(0, CreditCardValidator.VPAY, None, None)
        self.assertTrue(validator.isValid(CreditCardValidatorTest.__VALID_VPAY), "Valid")
        self.assertTrue(validator.isValid(CreditCardValidatorTest.__VALID_VPAY2), "Valid")
        self.assertFalse(validator.isValid(CreditCardValidatorTest.__ERROR_VPAY), "Invalid")
        self.assertEqual(
            validator.validate(CreditCardValidatorTest.__VALID_VPAY),
            CreditCardValidatorTest.__VALID_VPAY
        )
        self.assertEqual(
            validator.validate(CreditCardValidatorTest.__VALID_VPAY2),
            CreditCardValidatorTest.__VALID_VPAY2
        )

        self.assertFalse(validator.isValid(CreditCardValidatorTest.__VALID_AMEX), "Amex")
        self.assertFalse(validator.isValid(CreditCardValidatorTest.__VALID_DINERS), "Diners")
        self.assertFalse(
            validator.isValid(CreditCardValidatorTest.__VALID_DISCOVER),
            "Discover"
        )
        self.assertFalse(
            validator.isValid(CreditCardValidatorTest.__VALID_MASTERCARD),
            "Mastercard"
        )
        self.assertTrue(validator.isValid(CreditCardValidatorTest.__VALID_VISA), "Visa")
        self.assertTrue(
            validator.isValid(CreditCardValidatorTest.__VALID_SHORT_VISA),
            "Visa Short"
        )

    
    @pytest.mark.test
    def testMastercardUsingSeparators(self) -> None:
        MASTERCARD_REGEX_SEP =\
            "^(5[1-5]\\d{2})(?:[- ])?(\\d{4})(?:[- ])?(\\d{4})(?:[- ])?(\\d{4})$"
        validator = CodeValidator.CodeValidator5(
            MASTERCARD_REGEX_SEP,
            LuhnCheckDigit.LUHN_CHECK_DIGIT
        )
        regex = validator.getRegexValidator()

        self.assertEqual(regex.validate("5134567890123456"), "5134567890123456", "Number")
        self.assertEqual(regex.validate("5134-5678-9012-3456"), "5134567890123456", "Hyphen")
        self.assertEqual(regex.validate("5134 5678 9012 3456"), "5134567890123456", "Space")
        self.assertEqual(regex.validate("5134-5678 9012-3456"), "5134567890123456", "MixedA")
        self.assertEqual(regex.validate("5134 5678-9012 3456"), "5134567890123456", "MixedB")

        self.assertFalse(regex.isValid("5134.5678.9012.3456"), "Invalid Separator A")
        self.assertFalse(regex.isValid("5134_5678_9012_3456"), "Invalid Separator B")
        self.assertFalse(regex.isValid("513-45678-9012-3456"), "Invalid Grouping A")
        self.assertFalse(regex.isValid("5134-567-89012-3456"), "Invalid Grouping B")
        self.assertFalse(regex.isValid("5134-5678-901-23456"), "Invalid Grouping C")

        self.assertEqual(
            validator.validate("5500-0000-0000-0004"),
            "5500000000000004",
            "Valid-A"
        )
        self.assertEqual(
            validator.validate("5424 0000 0000 0015"),
            "5424000000000015",
            "Valid-B"
        )
        self.assertEqual(
            validator.validate("5301-250070000191"),
            "5301250070000191",
            "Valid-C"
        )
        self.assertEqual(
            validator.validate("5123456789012346"),
            "5123456789012346",
            "Valid-D"
        )

    
    @pytest.mark.test
    def testGeneric(self) -> None:
        ccv = CreditCardValidator.genericCreditCardValidator2()
        for s in CreditCardValidatorTest.__VALID_CARDS:
            self.assertTrue(ccv.isValid(s), s)
        for s in CreditCardValidatorTest.__ERROR_CARDS:
            self.assertFalse(ccv.isValid(s), s)
    

    @pytest.mark.test
    def testRangeGeneratorNoLuhn(self) -> None:
        cv = CreditCardValidator.createRangeValidator(
            [
                CreditCardValidator.CreditCardRange(0, "1", None, 6, 7, None),
                CreditCardValidator.CreditCardRange(0, "644", "65", 8, 8, None)
            ],
            None
        )
        self.assertTrue(cv.isValid("1990000"))
        self.assertTrue(cv.isValid("199000"))
        self.assertFalse(cv.isValid("000000"))
        self.assertFalse(cv.isValid("099999"))
        self.assertFalse(cv.isValid("200000"))

        self.assertFalse(cv.isValid("64399999"))
        self.assertTrue(cv.isValid("64400000"))
        self.assertTrue(cv.isValid("64900000"))
        self.assertTrue(cv.isValid("65000000"))
        self.assertTrue(cv.isValid("65999999"))
        self.assertFalse(cv.isValid("66000000"))

    
    @pytest.mark.test
    def testRangeGenerator(self) -> None:
        ccv = CreditCardValidator(
            3,
            0,
            [
                CreditCardValidator.CreditCardRange(0, "300", "305", 14, 14, None), # Diners
                CreditCardValidator.CreditCardRange(0, "3095", None, 14, 14, None), # Diners
                CreditCardValidator.CreditCardRange(0, "36", None, 14, 14, None), # Diners
                CreditCardValidator.CreditCardRange(0, "38", "39", 14, 14, None) # Diners
            ],
            [
                CreditCardValidator.AMEX_VALIDATOR,
                CreditCardValidator.VISA_VALIDATOR,
                CreditCardValidator.MASTERCARD_VALIDATOR,
                CreditCardValidator.DISCOVER_VALIDATOR
            ]
        )
        for s in CreditCardValidatorTest.__VALID_CARDS:
            self.assertTrue(ccv.isValid(s), s)
        for s in CreditCardValidatorTest.__ERROR_CARDS:
            self.assertFalse(ccv.isValid(s), s)

    
    @pytest.mark.test
    def testValidLength(self) -> None:
        self.assertTrue(
            CreditCardValidator\
                .validLength(14, CreditCardValidator.CreditCardRange(0, "", "", 14, 14, None))
        )
        self.assertFalse(
            CreditCardValidator\
                .validLength(15, CreditCardValidator.CreditCardRange(0, "", "", 14, 14, None))
        )
        self.assertFalse(
            CreditCardValidator\
                .validLength(13, CreditCardValidator.CreditCardRange(0, "", "", 14, 14, None))
        )

        self.assertFalse(
            CreditCardValidator\
                .validLength(14, CreditCardValidator.CreditCardRange(0, "", "", 15, 17, None))
        )
        self.assertTrue(
            CreditCardValidator\
                .validLength(15, CreditCardValidator.CreditCardRange(0, "", "", 15, 17, None))
        )
        self.assertTrue(
            CreditCardValidator\
                .validLength(16, CreditCardValidator.CreditCardRange(0, "", "", 15, 17, None))
        )
        self.assertTrue(
            CreditCardValidator\
                .validLength(17, CreditCardValidator.CreditCardRange(0, "", "", 15, 17, None))
        )
        self.assertFalse(
            CreditCardValidator\
                .validLength(18, CreditCardValidator.CreditCardRange(0, "", "", 15, 17, None))
        )

        self.assertFalse(
            CreditCardValidator\
                .validLength(14, CreditCardValidator.CreditCardRange(1, "", "", 0, 0, [15, 17]))
        )
        self.assertTrue(
            CreditCardValidator\
                .validLength(15, CreditCardValidator.CreditCardRange(1, "", "", 0, 0, [15, 17]))
        )
        self.assertFalse(
            CreditCardValidator\
                .validLength(16, CreditCardValidator.CreditCardRange(1, "", "", 0, 0, [15, 17]))
        )
        self.assertTrue(
            CreditCardValidator\
                .validLength(17, CreditCardValidator.CreditCardRange(1, "", "", 0, 0, [15, 17]))
        )
        self.assertFalse(
            CreditCardValidator\
                .validLength(18, CreditCardValidator.CreditCardRange(1, "", "", 0, 0, [15, 17]))
        )
    

    @pytest.mark.test
    def testDisjointRange(self) -> None:
        ccv = CreditCardValidator(
            2,
            0,
            [
                CreditCardValidator.CreditCardRange(1, "305", "4", 0, 0, [13, 16]),
            ],
            None
        )
        self.assertEqual(13, len(CreditCardValidatorTest.__VALID_SHORT_VISA))
        self.assertEqual(16, len(CreditCardValidatorTest.__VALID_VISA))
        self.assertEqual(14, len(CreditCardValidatorTest.__VALID_DINERS))
        self.assertTrue(ccv.isValid(CreditCardValidatorTest.__VALID_SHORT_VISA))
        self.assertTrue(ccv.isValid(CreditCardValidatorTest.__VALID_VISA))
        self.assertFalse(ccv.isValid(CreditCardValidatorTest.__ERROR_SHORT_VISA))
        self.assertFalse(ccv.isValid(CreditCardValidatorTest.__ERROR_VISA))
        self.assertFalse(ccv.isValid(CreditCardValidatorTest.__VALID_DINERS))
        ccv = CreditCardValidator(
            2,
            0,
            [
                CreditCardValidator.CreditCardRange(1, "305", "4", 0, 0, [13, 14, 16]),
            ],
            None
        )
        self.assertTrue(ccv.isValid(CreditCardValidatorTest.__VALID_DINERS))
