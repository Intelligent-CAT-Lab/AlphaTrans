import pytest

from src.main.org.apache.commons.validator.routines.checkdigit.ABANumberCheckDigit import *
from src.test.org.apache.commons.validator.routines.checkdigit.AbstractCheckDigitTest import AbstractCheckDigitTest

class ABANumberCheckDigitTest(AbstractCheckDigitTest):

    __test__ = True

    
    def setUp(self) -> None:
        try:
            super().setUp()
            self._routine = ABANumberCheckDigit.ABAN_CHECK_DIGIT
            self._valid = [
                "123456780",
                "123123123",
                "011000015",
                "111000038",
                "231381116",
                "121181976"
            ]
        except Exception as e:
            self.fail(f"An exception occurred when setting up the test: {e}")

