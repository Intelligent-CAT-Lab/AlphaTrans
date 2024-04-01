# Imports Begin
from src.main.org.apache.commons.validator.routines.checkdigit.CheckDigit import *
from src.main.org.apache.commons.validator.routines.checkdigit.CUSIPCheckDigit import *
from src.main.org.apache.commons.validator.routines.checkdigit.AbstractCheckDigitTest import *
import unittest
import typing
from typing import *

# Imports End


class CUSIPCheckDigitTest(unittest.TestCase, AbstractCheckDigitTest):

    # Class Fields Begin
    __invalidCheckDigits: List[str] = ["DUS0421CW", "DUS0421CN", "DUS0421CE"]
    __validCheckDigits: List[str] = ["DUS0421C5"]
    # Class Fields End

    # Class Methods Begin
    def _setUp(self) -> None:

        pass  # LLM could not translate method body

    def testVALIDATOR_336_ValidCheckDigits(self) -> None:

        for validCheckDigit in self.__validCheckDigits:
            assert self.isValid(validCheckDigit)

    def testVALIDATOR_336_InvalidCheckDigits(self) -> None:

        for invalid_check_digit in self.__invalidCheckDigits:
            assert not self.isValid(
                invalid_check_digit
            ), f"Should fail: {invalid_check_digit}"

    def __init__(self, name: str) -> None:

        super().__init__(name)

    # Class Methods End
