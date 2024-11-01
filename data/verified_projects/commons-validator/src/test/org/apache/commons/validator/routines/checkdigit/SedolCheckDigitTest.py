import pytest

from src.main.org.apache.commons.validator.routines.checkdigit.SedolCheckDigit import *
from src.test.org.apache.commons.validator.routines.checkdigit.AbstractCheckDigitTest import AbstractCheckDigitTest


class SedolCheckDigitTest(AbstractCheckDigitTest):

    __invalidCheckDigits = [
        "026349E", # proper check digit is '4', see above
        "087061C", # proper check digit is '2', see above
        "B06LQ9H", # proper check digit is '7', see above
        "343757F", # proper check digit is '5', see above
        "B07LF5F", # proper check digit is '5', see above
    ]

    __test__ = True

    
    def setUp(self) -> None:
        try:
            super().setUp()
            self._routine = SedolCheckDigit.SEDOL_CHECK_DIGIT
            self._valid = [
                "0263494",
                "0870612",
                "B06LQ97",
                "3437575",
                "B07LF55",
            ]
            self._invalid = ["123#567"]
            self._zeroSum = "0000000"
        except Exception as e:
            self.fail(f"An exception occurred when setting up the test: {e}")
    

    @pytest.mark.test
    def testVALIDATOR_346(self) -> None:
        for i in range(len(SedolCheckDigitTest.__invalidCheckDigits)):
            invalidCheckDigit = SedolCheckDigitTest.__invalidCheckDigits[i]
            self.assertFalse(
                self._routine.isValid(invalidCheckDigit),
                "Should fail: " + invalidCheckDigit
            )
