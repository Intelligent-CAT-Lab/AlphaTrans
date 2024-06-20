import pytest

from src.main.org.apache.commons.validator.CreditCardValidator import *
import unittest

class CreditCardValidatorTest(unittest.TestCase):

    __VALID_VISA = "4417123456789113"
    __VALID_SHORT_VISA = "4222222222222"
    __VALID_AMEX = "378282246310005"
    __VALID_MASTERCARD = "5105105105105100"
    __VALID_DISCOVER = "6011000990139424"
    __VALID_DINERS = "30569309025904"


    @pytest.mark.test
    def testIsValid(self) -> None:
        ccv = CreditCardValidator.CreditCardValidator1()

        self.assertFalse(ccv.isValid(None))
        self.assertFalse(ccv.isValid(""))
        self.assertFalse(ccv.isValid("123456789012")) # too short
        self.assertFalse(ccv.isValid("12345678901234567890")) # too long
        self.assertFalse(ccv.isValid("4417123456789112"))
        self.assertFalse(ccv.isValid("4417q23456w89113"))
        self.assertTrue(ccv.isValid(CreditCardValidatorTest.__VALID_VISA))
        self.assertTrue(ccv.isValid(CreditCardValidatorTest.__VALID_SHORT_VISA))
        self.assertTrue(ccv.isValid(CreditCardValidatorTest.__VALID_AMEX))
        self.assertTrue(ccv.isValid(CreditCardValidatorTest.__VALID_MASTERCARD))
        self.assertTrue(ccv.isValid(CreditCardValidatorTest.__VALID_DISCOVER))

        ccv = CreditCardValidator(CreditCardValidator.AMEX)
        self.assertFalse(ccv.isValid("4417123456789113"))
    

    @pytest.mark.test
    def testAddAllowedCardType(self) -> None:
        ccv = CreditCardValidator(CreditCardValidator.NONE)
        self.assertFalse(ccv.isValid(CreditCardValidatorTest.__VALID_VISA))
        self.assertFalse(ccv.isValid(CreditCardValidatorTest.__VALID_AMEX))
        self.assertFalse(ccv.isValid(CreditCardValidatorTest.__VALID_MASTERCARD))
        self.assertFalse(ccv.isValid(CreditCardValidatorTest.__VALID_DISCOVER))

        ccv.addAllowedCardType(DinersClub())
        self.assertTrue(ccv.isValid(CreditCardValidatorTest.__VALID_DINERS))


class DinersClub(CreditCardValidator.CreditCardType):

    __PREFIX = "300,301,302,303,304,305,"

    def matches(self, card) -> str:
        prefix = card[:3] + ","
        return (prefix in DinersClub.__PREFIX) and (len(card) == 14)
