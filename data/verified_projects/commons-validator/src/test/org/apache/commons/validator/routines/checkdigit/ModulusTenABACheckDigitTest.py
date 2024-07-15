import pytest

from src.main.org.apache.commons.validator.routines.checkdigit.ModulusTenCheckDigit import *
from src.test.org.apache.commons.validator.routines.checkdigit.AbstractCheckDigitTest import AbstractCheckDigitTest


class ModulusTenABACheckDigitTest(AbstractCheckDigitTest):

    __test__ = True

    
    def setUp(self) -> None:
        try:
            super().setUp()
            self._routine = ModulusTenCheckDigit\
                .ModulusTenCheckDigit1([1, 7, 3], True)
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
