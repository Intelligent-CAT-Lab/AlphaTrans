from src.main.org.apache.commons.validator.routines.checkdigit.ISBNCheckDigit import *
from src.test.org.apache.commons.validator.routines.checkdigit.AbstractCheckDigitTest import AbstractCheckDigitTest

class ISBNCheckDigitTest(AbstractCheckDigitTest):

    @classmethod
    def setUpClass(cls):
        pass

    
    def __init__(self, methodName='runTest') -> None:
        super().__init__(methodName)

    
    def setUp(self) -> None:
        try:
            super().setUp(
                routine = ISBNCheckDigit.ISBN_CHECK_DIGIT,
                valid = [
                    "9780072129519",
                    "9780764558313",
                    "1930110995",
                    "020163385X",
                    "1590596277", # ISBN-10 Ubuntu Book
                    "9781590596272" # ISBN-13 Ubuntu Book
                ],
                missingMessage = "ISBN Code is missing",
                zeroSum = "000000000000"
            )
        except Exception as e:
            self.fail(f"An exception occurred when setting up the test: {e}")
    

    def testInvalidLength(self) -> None:
        self.assertFalse(self._routine.isValid("123456789"), "isValid() Lth 9")
        self.assertFalse(self._routine.isValid("12345678901"), "isValid() Lth 11")
        self.assertFalse(self._routine.isValid("123456789012"), "isValid() Lth 12")
        self.assertFalse(self._routine.isValid("12345678901234"), "isValid() Lth 14")

        try:
            self._routine.calculate("12345678")
            self.fail("calculate() Lth 8 - expected exception")
        except Exception as e:
            self.assertEqual("Invalid ISBN Length = 8", str(e), "calculate() Lth 8")

        try:
            self._routine.calculate("1234567890")
            self.fail("calculate() Lth 10 - expected exception")
        except Exception as e:
            self.assertEqual("Invalid ISBN Length = 10", str(e), "calculate() Lth 10")

        try:
            self._routine.calculate("12345678901")
            self.fail("calculate() Lth 11 - expected exception")
        except Exception as e:
            self.assertEqual("Invalid ISBN Length = 11", str(e), "calculate() Lth 11")

        try:
            self._routine.calculate("1234567890123")
            self.fail("calculate() Lth 13 - expected exception")
        except Exception as e:
            self.assertEqual("Invalid ISBN Length = 13", str(e), "calculate() Lth 13")
