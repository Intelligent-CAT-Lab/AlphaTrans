from src.main.org.apache.commons.validator.routines.checkdigit.LuhnCheckDigit import *
from src.test.org.apache.commons.validator.routines.checkdigit.AbstractCheckDigitTest import AbstractCheckDigitTest


class LuhnCheckDigitTest(AbstractCheckDigitTest):

    __VALID_VISA = "4417123456789113"
    __VALID_SHORT_VISA = "4222222222222"
    __VALID_AMEX = "378282246310005"
    __VALID_MASTERCARD = "5105105105105100"
    __VALID_DISCOVER = "6011000990139424"
    __VALID_DINERS = "30569309025904"
    
    @classmethod
    def setUpClass(cls):
        pass

    
    def __init__(self, methodName='runTest') -> None:
        super().__init__(methodName)

    
    def setUp(self) -> None:
        try:
            super().setUp()

            self._routine = LuhnCheckDigit.LUHN_CHECK_DIGIT
            
            self._valid = [
                LuhnCheckDigitTest.__VALID_VISA,
                LuhnCheckDigitTest.__VALID_SHORT_VISA,
                LuhnCheckDigitTest.__VALID_AMEX,
                LuhnCheckDigitTest.__VALID_MASTERCARD,
                LuhnCheckDigitTest.__VALID_DISCOVER,
                LuhnCheckDigitTest.__VALID_DINERS
            ]
        except Exception as e:
            self.fail(f"An exception occurred when setting up the test: {e}")