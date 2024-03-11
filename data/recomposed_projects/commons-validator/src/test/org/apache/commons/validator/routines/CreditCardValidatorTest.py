# Imports Begin
from src.main.org.apache.commons.validator.routines.checkdigit.LuhnCheckDigit import *
from src.main.org.apache.commons.validator.routines.checkdigit.CheckDigit import *
from src.main.org.apache.commons.validator.routines.RegexValidator import *
from src.main.org.apache.commons.validator.routines.CreditCardValidator import *
from src.main.org.apache.commons.validator.routines.CodeValidator import *
from src.main.org.apache.commons.validator.CreditCardValidator import *
import unittest
import typing
from typing import *

# Imports End


class CreditCardValidatorTest(unittest.TestCase, TestCase):

    # Class Fields Begin
    __VALID_VISA: str = ""  # LLM could not translate field
    __ERROR_VISA: str = ""  # LLM could not translate field
    __VALID_SHORT_VISA: str = ""  # LLM could not translate field
    __ERROR_SHORT_VISA: str = "4222222222229"
    __VALID_AMEX: str = "378282246310005"
    __ERROR_AMEX: str = "378282246310001"
    __VALID_MASTERCARD: str = ""  # LLM could not translate field
    __ERROR_MASTERCARD: str = ""  # LLM could not translate field
    __VALID_DISCOVER: str = ""  # LLM could not translate field
    __ERROR_DISCOVER: str = "6011000990139421"
    __VALID_DISCOVER65: str = ""  # LLM could not translate field
    __ERROR_DISCOVER65: str = "6534567890123450"
    __VALID_DINERS: str = "30569309025904"
    __ERROR_DINERS: str = "30569309025901"
    __VALID_VPAY: str = "4370000000000061"
    __VALID_VPAY2: str = "4370000000000012"
    __ERROR_VPAY: str = "4370000000000069"
    __VALID_CARDS: typing.List[str] = ""  # LLM could not translate field
    __ERROR_CARDS: List[str] = [
        ERROR_VISA,
        ERROR_SHORT_VISA,
        ERROR_AMEX,
        ERROR_MASTERCARD,
        ERROR_DISCOVER,
        ERROR_DISCOVER65,
        ERROR_DINERS,
        ERROR_VPAY,
        "",
        "12345678901",  # too short (11)
        "12345678901234567890",  # too long (20)
        "4417123456789112",  # invalid check digit
    ]
    # Class Fields End

    # Class Methods Begin
    def testDisjointRange(self) -> None:

        ccv = CreditCardValidator(
            2, 0, [CreditCardRange(1, "305", "4", 0, 0, [13, 16])], None
        )
        assert len(VALID_SHORT_VISA) == 13
        assert len(VALID_VISA) == 16
        assert len(VALID_DINERS) == 14
        assert ccv.isValid(VALID_SHORT_VISA)
        assert ccv.isValid(VALID_VISA)
        assert not ccv.isValid(ERROR_SHORT_VISA)
        assert not ccv.isValid(ERROR_VISA)
        assert not ccv.isValid(VALID_DINERS)
        ccv = CreditCardValidator(
            2, 0, [CreditCardRange(1, "305", "4", 0, 0, [13, 14, 16])], None
        )
        assert ccv.isValid(VALID_DINERS)

    def testValidLength(self) -> None:

        assert True == CreditCardValidator.validLength(
            14, CreditCardRange(0, "", "", 14, 14, None)
        )
        assert False == CreditCardValidator.validLength(
            15, CreditCardRange(0, "", "", 14, 14, None)
        )
        assert False == CreditCardValidator.validLength(
            13, CreditCardRange(0, "", "", 14, 14, None)
        )
        assert False == CreditCardValidator.validLength(
            14, CreditCardRange(0, "", "", 15, 17, None)
        )
        assert True == CreditCardValidator.validLength(
            15, CreditCardRange(0, "", "", 15, 17, None)
        )
        assert True == CreditCardValidator.validLength(
            16, CreditCardRange(0, "", "", 15, 17, None)
        )
        assert True == CreditCardValidator.validLength(
            17, CreditCardRange(0, "", "", 15, 17, None)
        )
        assert False == CreditCardValidator.validLength(
            18, CreditCardRange(0, "", "", 15, 17, None)
        )
        assert False == CreditCardValidator.validLength(
            14, CreditCardRange(1, "", "", 0, 0, [15, 17])
        )
        assert True == CreditCardValidator.validLength(
            15, CreditCardRange(1, "", "", 0, 0, [15, 17])
        )
        assert False == CreditCardValidator.validLength(
            16, CreditCardRange(1, "", "", 0, 0, [15, 17])
        )
        assert True == CreditCardValidator.validLength(
            17, CreditCardRange(1, "", "", 0, 0, [15, 17])
        )
        assert False == CreditCardValidator.validLength(
            18, CreditCardRange(1, "", "", 0, 0, [15, 17])
        )

    def testRangeGenerator(self) -> None:

        ccv = CreditCardValidator(
            3,
            0,
            [
                CreditCardRange(0, "300", "305", 14, 14, None),  # Diners
                CreditCardRange(0, "3095", None, 14, 14, None),  # Diners
                CreditCardRange(0, "36", None, 14, 14, None),  # Diners
                CreditCardRange(0, "38", "39", 14, 14, None),  # Diners
            ],
            [
                CreditCardValidator.AMEX_VALIDATOR,
                CreditCardValidator.VISA_VALIDATOR,
                CreditCardValidator.MASTERCARD_VALIDATOR,
                CreditCardValidator.DISCOVER_VALIDATOR,
            ],
        )
        for card in VALID_CARDS:
            assert ccv.isValid(card)
        for card in ERROR_CARDS:
            assert not ccv.isValid(card)

    def testRangeGeneratorNoLuhn(self) -> None:

        cv = CreditCardValidator.createRangeValidator(
            [
                CreditCardRange(0, "1", None, 6, 7, None),
                CreditCardRange(0, "644", "65", 8, 8, None),
            ],
            None,
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

    def testGeneric(self) -> None:

        pass  # LLM could not translate method body

    def testMastercardUsingSeparators(self) -> None:

        MASTERCARD_REGEX_SEP = (
            r"^(5[1-5]\d{2})(?:[- ])?(\d{4})(?:[- ])?(\d{4})(?:[- ])?(\d{4})$"
        )
        validator = CodeValidator.CodeValidator5(
            MASTERCARD_REGEX_SEP, LuhnCheckDigit.LUHN_CHECK_DIGIT
        )
        regex = validator.getRegexValidator()
        assert regex.validate("5134567890123456") == "5134567890123456"
        assert regex.validate("5134-5678-9012-3456") == "5134567890123456"
        assert regex.validate("5134 5678 9012 3456") == "5134567890123456"
        assert regex.validate("5134-5678 9012-3456") == "5134567890123456"
        assert regex.validate("5134 5678-9012 3456") == "5134567890123456"
        assert not regex.isValid("5134.5678.9012.3456")
        assert not regex.isValid("5134_5678_9012_3456")
        assert not regex.isValid("513-45678-9012-3456")
        assert not regex.isValid("5134-567-89012-3456")
        assert not regex.isValid("5134-5678-901-23456")
        assert validator.validate("5500-0000-0000-0004") == "5500000000000004"
        assert validator.validate("5424 0000 0000 0015") == "5424000000000015"
        assert validator.validate("5301-250070000191") == "5301250070000191"
        assert validator.validate("5123456789012346") == "5123456789012346"

    def testVPayOption(self) -> None:

        validator = CreditCardValidator(0, CreditCardValidator.VPAY, None, None)
        self.assertTrue("Valid", validator.isValid(VALID_VPAY))
        self.assertTrue("Valid", validator.isValid(VALID_VPAY2))
        self.assertFalse("Invalid", validator.isValid(ERROR_VPAY))
        self.assertEqual(VALID_VPAY, validator.validate(VALID_VPAY))
        self.assertEqual(VALID_VPAY2, validator.validate(VALID_VPAY2))
        self.assertFalse("Amex", validator.isValid(VALID_AMEX))
        self.assertFalse("Diners", validator.isValid(VALID_DINERS))
        self.assertFalse("Discover", validator.isValid(VALID_DISCOVER))
        self.assertFalse("Mastercard", validator.isValid(VALID_MASTERCARD))
        self.assertTrue("Visa", validator.isValid(VALID_VISA))
        self.assertTrue("Visa Short", validator.isValid(VALID_SHORT_VISA))

    def testVisaOption(self) -> None:

        validator = CreditCardValidator(0, CreditCardValidator.VISA, None, None)
        self.assertFalse("Invalid", validator.isValid(self.__ERROR_VISA))
        self.assertFalse("Invalid-S", validator.isValid(self.__ERROR_SHORT_VISA))
        assertNull("validate()", validator.validate(self.__ERROR_VISA))
        self.assertEqual(self.__VALID_VISA, validator.validate(self.__VALID_VISA))
        self.assertEqual(
            self.__VALID_SHORT_VISA, validator.validate(self.__VALID_SHORT_VISA)
        )
        self.assertFalse("Amex", validator.isValid(self.__VALID_AMEX))
        self.assertFalse("Diners", validator.isValid(self.__VALID_DINERS))
        self.assertFalse("Discover", validator.isValid(self.__VALID_DISCOVER))
        self.assertFalse("Mastercard", validator.isValid(self.__VALID_MASTERCARD))
        self.assertTrue("Visa", validator.isValid(self.__VALID_VISA))
        self.assertTrue("Visa Short", validator.isValid(self.__VALID_SHORT_VISA))

    def testVisaValidator(self) -> None:

        pass  # LLM could not translate method body

    def testMastercardOption(self) -> None:

        pass  # LLM could not translate method body

    def testMastercardValidator(self) -> None:

        pass  # LLM could not translate method body

    def testDiscoverOption(self) -> None:

        validator = CreditCardValidator(0, CreditCardValidator.DISCOVER, None, None)
        assert not validator.isValid(self.__ERROR_DISCOVER)
        assert not validator.isValid(self.__ERROR_DISCOVER65)
        assert validator.validate(self.__ERROR_DISCOVER) is None
        assert validator.validate(self.__VALID_DISCOVER) == self.__VALID_DISCOVER
        assert validator.validate(self.__VALID_DISCOVER65) == self.__VALID_DISCOVER65
        assert not validator.isValid(self.__VALID_AMEX)
        assert not validator.isValid(self.__VALID_DINERS)
        assert validator.isValid(self.__VALID_DISCOVER)
        assert validator.isValid(self.__VALID_DISCOVER65)
        assert not validator.isValid(self.__VALID_MASTERCARD)
        assert not validator.isValid(self.__VALID_VISA)
        assert not validator.isValid(self.__VALID_SHORT_VISA)

    def testDiscoverValidator(self) -> None:

        pass  # LLM could not translate method body

    def testDinersOption(self) -> None:

        validator = CreditCardValidator(0, CreditCardValidator.DINERS, None, None)
        self.assertFalse("Invalid", validator.isValid(self.__ERROR_DINERS))
        assertNull("validate()", validator.validate(self.__ERROR_DINERS))
        self.assertEqual(self.__VALID_DINERS, validator.validate(self.__VALID_DINERS))
        self.assertFalse("Amex", validator.isValid(self.__VALID_AMEX))
        self.assertTrue("Diners", validator.isValid(self.__VALID_DINERS))
        self.assertFalse("Discover", validator.isValid(self.__VALID_DISCOVER))
        self.assertFalse("Mastercard", validator.isValid(self.__VALID_MASTERCARD))
        self.assertFalse("Visa", validator.isValid(self.__VALID_VISA))
        self.assertFalse("Visa Short", validator.isValid(self.__VALID_SHORT_VISA))

    def testDinersValidator(self) -> None:

        pass  # LLM could not translate method body

    def testAmexOption(self) -> None:

        pass  # LLM could not translate method body

    def testAmexValidator(self) -> None:

        pass  # LLM could not translate method body

    def testArrayConstructor(self) -> None:

        ccv = CreditCardValidator(
            1,
            0,
            None,
            [CreditCardValidator.VISA_VALIDATOR, CreditCardValidator.AMEX_VALIDATOR],
        )
        assert ccv.isValid(VALID_VISA)
        assert ccv.isValid(VALID_SHORT_VISA)
        assert ccv.isValid(VALID_AMEX)
        assert not ccv.isValid(VALID_MASTERCARD)
        assert not ccv.isValid(VALID_DISCOVER)
        assert not ccv.isValid(ERROR_VISA)
        assert not ccv.isValid(ERROR_SHORT_VISA)
        assert not ccv.isValid(ERROR_AMEX)
        assert not ccv.isValid(ERROR_MASTERCARD)
        assert not ccv.isValid(ERROR_DISCOVER)
        try:
            CreditCardValidator(1, 0, None, None)
            fail("Expected IllegalArgumentException")
        except IllegalArgumentException:
            pass

    def testAddAllowedCardType(self) -> None:

        ccv = CreditCardValidator(0, CreditCardValidator.NONE, None, None)
        self.assertFalse(ccv.isValid(VALID_VISA))
        self.assertFalse(ccv.isValid(VALID_AMEX))
        self.assertFalse(ccv.isValid(VALID_MASTERCARD))
        self.assertFalse(ccv.isValid(VALID_DISCOVER))
        self.assertFalse(ccv.isValid(VALID_DINERS))

    def testIsValid(self) -> None:

        pass  # LLM could not translate method body

    def __init__(self, name: str) -> None:

        super().__init__(name)

    # Class Methods End
