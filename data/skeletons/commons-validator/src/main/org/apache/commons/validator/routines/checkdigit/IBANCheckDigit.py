from __future__ import annotations

# Imports Begin
from src.main.org.apache.commons.validator.routines.checkdigit.CheckDigitException import *
from src.main.org.apache.commons.validator.routines.checkdigit.CheckDigit import *
import io

# Imports End


class IBANCheckDigit(CheckDigit):

    # Class Fields Begin
    __MIN_CODE_LEN: int = None
    __serialVersionUID: int = None
    __MAX_ALPHANUMERIC_VALUE: int = None
    IBAN_CHECK_DIGIT: CheckDigit = None
    __MAX: int = None
    __MODULUS: int = None
    # Class Fields End

    # Class Methods Begin
    def calculate(self, code: str) -> str:
        pass

    def isValid(self, code: str) -> bool:
        pass

    def __init__(self) -> None:
        pass

    def __calculateModulus(self, code: str) -> int:
        pass

    # Class Methods End
