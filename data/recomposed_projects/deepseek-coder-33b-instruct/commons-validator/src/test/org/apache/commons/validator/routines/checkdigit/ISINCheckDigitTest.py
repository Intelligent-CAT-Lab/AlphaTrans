from src.main.org.apache.commons.validator.routines.checkdigit.ISINCheckDigit import *
from src.test.org.apache.commons.validator.routines.checkdigit.AbstractCheckDigitTest import AbstractCheckDigitTest


class ISINCheckDigitTest(AbstractCheckDigitTest):

    __invalidCheckDigits = [
        "US037833100O", # proper check digit is '5', see above
        "BMG8571G109D", # proper check digit is '6', see above
        "AU0000XVGZAD", # proper check digit is '3', see above
        "GB000263494I", # proper check digit is '6', see above
        "FR000402625C", # proper check digit is '0', see above
        "DK000976334H", # proper check digit is '4', see above
    ]


    @classmethod
    def setUpClass(cls):
        pass

    
    def __init__(self, methodName='runTest') -> None:
        super().__init__(methodName)

    
    def setUp(self) -> None:
        try:
            super().setUp()
            self._routine = ISINCheckDigit.ISIN_CHECK_DIGIT
            self._valid = [
                "US0378331005",
                "BMG8571G1096",
                "AU0000XVGZA3",
                "GB0002634946",
                "FR0004026250",
                "3133EHHF3", # see VALIDATOR-422 Valid check-digit, but not valid ISIN
                "DK0009763344",
                "dk0009763344", # TODO lowercase is currently accepted, but is this valid?
                "AU0000xvgza3", # lowercase NSIN
                "EZ0000000003", # Invented; for use in ISINValidatorTest
                "XS0000000009", # ditto
                "AA0000000006", # ditto
            ]
            self._invalid = [
                "0378#3100"
            ]
        except Exception as e:
            self.fail(f"An exception occurred when setting up the test: {e}")
    

    def test_VALIDATOR_345(self) -> None:
        for i in range(len(ISINCheckDigitTest.__invalidCheckDigits)):
            invalidCheckDigit = ISINCheckDigitTest.__invalidCheckDigits[i]
            self.assertFalse(
                self._routine.isValid(invalidCheckDigit),
                "Should fail: " + invalidCheckDigit
            )
