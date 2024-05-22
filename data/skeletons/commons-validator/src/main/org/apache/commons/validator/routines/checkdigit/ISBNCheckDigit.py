from __future__ import annotations

# Imports Begin
from src.main.org.apache.commons.validator.routines.checkdigit.ISBN10CheckDigit import *
from src.main.org.apache.commons.validator.routines.checkdigit.EAN13CheckDigit import *
from src.main.org.apache.commons.validator.routines.checkdigit.CheckDigitException import *
from src.main.org.apache.commons.validator.routines.checkdigit.CheckDigit import *
import io

# Imports End


class ISBNCheckDigit(CheckDigit):

    # Class Fields Begin
    __serialVersionUID: int = None
    ISBN10_CHECK_DIGIT: CheckDigit = None
    ISBN13_CHECK_DIGIT: CheckDigit = None
    ISBN_CHECK_DIGIT: CheckDigit = None
    # Class Fields End

    # Class Methods Begin
    def isValid(self, code: str) -> bool:
        pass

    def calculate(self, code: str) -> str:
        pass

    # Class Methods End
