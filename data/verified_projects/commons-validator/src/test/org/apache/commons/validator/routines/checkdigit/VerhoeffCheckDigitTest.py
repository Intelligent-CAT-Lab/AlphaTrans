import pytest

from src.main.org.apache.commons.validator.routines.checkdigit.VerhoeffCheckDigit import *
from src.test.org.apache.commons.validator.routines.checkdigit.AbstractCheckDigitTest import AbstractCheckDigitTest

class VerhoeffCheckDigitTest(AbstractCheckDigitTest):

    __test__ = True

    
    def setUp(self) -> None:
        try:
            super().setUp()
            self._routine = VerhoeffCheckDigit.VERHOEFF_CHECK_DIGIT
            self._valid = [
                "15",
                "1428570",
                "12345678902"
            ]
        except Exception as e:
            self.fail(f"An exception occurred when setting up the test: {e}")


    @pytest.mark.test
    def testZeroSum(self) -> None:
        pass
