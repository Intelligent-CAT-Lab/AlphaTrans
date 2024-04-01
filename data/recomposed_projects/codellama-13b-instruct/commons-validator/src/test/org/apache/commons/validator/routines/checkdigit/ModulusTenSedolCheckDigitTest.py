# Imports Begin
from src.main.org.apache.commons.validator.routines.checkdigit.ModulusTenCheckDigit import *
from src.main.org.apache.commons.validator.routines.checkdigit.CheckDigit import *
from src.main.org.apache.commons.validator.routines.checkdigit.AbstractCheckDigitTest import *
import unittest
import typing
from typing import *

# Imports End


class ModulusTenSedolCheckDigitTest(unittest.TestCase, AbstractCheckDigitTest):

    # Class Fields Begin
    __invalidCheckDigits: List[str] = [
        "026349E",
        "087061C",
        "B06LQ9H",
        "343757F",
        "B07LF5F",
    ]
    # Class Fields End

    # Class Methods Begin
    def _setUp(self) -> None:

        pass  # LLM could not translate method body

    def testVALIDATOR_346(self) -> None:

        for invalidCheckDigit in self.__invalidCheckDigits:
            assert not self.isValid(
                invalidCheckDigit
            ), f"Should fail: {invalidCheckDigit}"

    def __init__(self, name: str) -> None:

        super().__init__(name)

    # Class Methods End
