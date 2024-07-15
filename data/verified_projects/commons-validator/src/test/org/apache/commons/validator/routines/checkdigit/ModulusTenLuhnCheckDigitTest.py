import pytest

from src.main.org.apache.commons.validator.routines.checkdigit.ModulusTenCheckDigit import *
from src.test.org.apache.commons.validator.routines.checkdigit.AbstractCheckDigitTest import AbstractCheckDigitTest


class ModulusTenLuhnCheckDigitTest(AbstractCheckDigitTest):

    __VALID_VISA = "4417123456789113"
    __VALID_SHORT_VISA = "4222222222222"
    __VALID_AMEX = "378282246310005"
    __VALID_MASTERCARD = "5105105105105100"
    __VALID_DISCOVER = "6011000990139424"
    __VALID_DINERS = "30569309025904"

    __test__ = True

    
    def setUp(self) -> None:
        try:
            super().setUp()
            self._routine = ModulusTenCheckDigit([1, 2], True, True)
            self._valid = [
                ModulusTenLuhnCheckDigitTest.__VALID_VISA,
                ModulusTenLuhnCheckDigitTest.__VALID_SHORT_VISA,
                ModulusTenLuhnCheckDigitTest.__VALID_AMEX,
                ModulusTenLuhnCheckDigitTest.__VALID_MASTERCARD,
                ModulusTenLuhnCheckDigitTest.__VALID_DISCOVER,
                ModulusTenLuhnCheckDigitTest.__VALID_DINERS
            ]
        except Exception as e:
            self.fail(f"An exception occurred when setting up the test: {e}")
