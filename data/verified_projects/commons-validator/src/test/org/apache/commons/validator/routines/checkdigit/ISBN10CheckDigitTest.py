import pytest

from src.main.org.apache.commons.validator.routines.checkdigit.ISBN10CheckDigit import *
from src.test.org.apache.commons.validator.routines.checkdigit.AbstractCheckDigitTest import AbstractCheckDigitTest


class ISBN10CheckDigitTest(AbstractCheckDigitTest):

    __test__ = True

    
    def setUp(self) -> None:
        try:
            super().setUp()
            self._routine = ISBN10CheckDigit.ISBN10_CHECK_DIGIT
            self._valid = [
                "1930110995",
                "020163385X",
                "1932394354",
                "1590596277"
            ]
        except Exception as e:
            self.fail(f"An exception occurred when setting up the test: {e}")
