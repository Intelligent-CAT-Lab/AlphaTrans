from src.main.org.apache.commons.validator.routines.checkdigit.CUSIPCheckDigit import *
from src.test.org.apache.commons.validator.routines.checkdigit.AbstractCheckDigitTest import AbstractCheckDigitTest
from typing import *


class CUSIPCheckDigitTest(AbstractCheckDigitTest):

    __invalidCheckDigits = ["DUS0421CW", "DUS0421CN", "DUS0421CE"]

    __validCheckDigits = ["DUS0421C5"]


    @classmethod
    def setUpClass(cls):
        pass
    
    
    def __init__(self, methodName='runTest') -> None:
        super().__init__(methodName)

    
    def setUp(self) -> None:
        try:
            super().setUp()
            self._routine = CUSIPCheckDigit.CUSIP_CHECK_DIGIT
            self._valid = [
                "037833100",
                "931142103",
                "837649128",
                "392690QT3",
                "594918104",
                "86770G101",
                "Y8295N109",
                "G8572F100"
            ]
            self._invalid = ["0378#3100"]
        except Exception as e:
            self.fail(f"An exception occurred when setting up the test: {e}")

    
    def test_VALIDATOR_336_InvalidCheckDigits(self) -> None:
        for i in range(len(CUSIPCheckDigitTest.__invalidCheckDigits)):
            invalidCheckDigit = CUSIPCheckDigitTest.__invalidCheckDigits[i]
            self.assertFalse(
                self._routine.isValid(invalidCheckDigit),
                "Should fail: " + invalidCheckDigit
            )

    
    def test_VALIDATOR_336_ValidCheckDigits(self) -> None:
        for i in range(len(CUSIPCheckDigitTest.__validCheckDigits)):
            validCheckDigit = CUSIPCheckDigitTest.__validCheckDigits[i]
            self.assertTrue(
                self._routine.isValid(validCheckDigit),
                "Should fail: " + validCheckDigit
            )

