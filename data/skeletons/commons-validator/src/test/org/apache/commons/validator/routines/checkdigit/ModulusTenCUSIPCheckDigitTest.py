from __future__ import annotations

# Imports Begin
from src.main.org.apache.commons.validator.routines.checkdigit.ModulusTenCheckDigit import *
from src.main.org.apache.commons.validator.routines.checkdigit.CheckDigit import *
from src.test.org.apache.commons.validator.routines.checkdigit.AbstractCheckDigitTest import *
import typing
from typing import *
import io

# Imports End


class ModulusTenCUSIPCheckDigitTest(AbstractCheckDigitTest):

    # Class Fields Begin
    __invalidCheckDigits: typing.List[str] = None
    __validCheckDigits: typing.List[str] = None
    # Class Fields End

    # Class Methods Begin
    def _setUp(self) -> None:
        pass

    def testVALIDATOR_336_ValidCheckDigits(self) -> None:
        pass

    def testVALIDATOR_336_InvalidCheckDigits(self) -> None:
        pass

    def __init__(self, name: str) -> None:
        pass

    # Class Methods End
