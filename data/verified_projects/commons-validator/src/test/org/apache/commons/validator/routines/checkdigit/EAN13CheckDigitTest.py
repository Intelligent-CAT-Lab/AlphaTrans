import pytest

from src.main.org.apache.commons.validator.routines.checkdigit.EAN13CheckDigit import *
from src.test.org.apache.commons.validator.routines.checkdigit.AbstractCheckDigitTest import AbstractCheckDigitTest


class EAN13CheckDigitTest(AbstractCheckDigitTest):

    __test__ = True

    
    def setUp(self) -> None:
        try:
            super().setUp()
            self._routine = EAN13CheckDigit.EAN13_CHECK_DIGIT
            self._valid = [
                "9780072129519",
                "9780764558313",
                "4025515373438",
                "0095673400332"
            ]
        except Exception as e:
            self.fail(f"An exception occurred when setting up the test: {e}")
