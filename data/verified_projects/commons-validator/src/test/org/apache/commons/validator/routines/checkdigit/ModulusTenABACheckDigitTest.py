import pytest

from src.main.org.apache.commons.validator.routines.checkdigit.ModulusTenCheckDigit import *
from src.test.org.apache.commons.validator.routines.checkdigit.AbstractCheckDigitTest import AbstractCheckDigitTest


class ModulusTenABACheckDigitTest(AbstractCheckDigitTest):

    @classmethod
    def setUpClass(cls):
        pass

    
    def __init__(self, methodName='runTest') -> None:
        super().__init__(methodName)

    
    def setUp(self) -> None:
        try:
            super().setUp(
                routine = ModulusTenCheckDigit\
                    .ModulusTenCheckDigit1([1, 7, 3], True),
                valid = [
                    "123456780",
                    "123123123",
                    "011000015",
                    "111000038",
                    "231381116",
                    "121181976"
                ]
            )
        except Exception as e:
            self.fail(f"An exception occurred when setting up the test: {e}")
