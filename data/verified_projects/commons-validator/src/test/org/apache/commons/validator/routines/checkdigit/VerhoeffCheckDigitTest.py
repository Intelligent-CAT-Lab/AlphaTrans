from src.main.org.apache.commons.validator.routines.checkdigit.VerhoeffCheckDigit import *
from src.test.org.apache.commons.validator.routines.checkdigit.AbstractCheckDigitTest import AbstractCheckDigitTest

class VerhoeffCheckDigitTest(AbstractCheckDigitTest):

    @classmethod
    def setUpClass(cls):
        pass

    
    def __init__(self, methodName='runTest') -> None:
        super().__init__(methodName)

    
    def setUp(self) -> None:
        try:
            super().setUp(
                routine = VerhoeffCheckDigit.VERHOEFF_CHECK_DIGIT,
                valid = [
                    "15",
                    "1428570",
                    "12345678902"
                ]
            )
        except Exception as e:
            self.fail(f"An exception occurred when setting up the test: {e}")


    def test_ZeroSum(self) -> None:
        pass
