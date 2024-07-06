from __future__ import annotations
import re
import io
from src.main.org.apache.commons.validator.routines.checkdigit.CheckDigit import *
from src.main.org.apache.commons.validator.routines.checkdigit.CheckDigitException import *
from src.main.org.apache.commons.validator.routines.checkdigit.EAN13CheckDigit import *
from src.main.org.apache.commons.validator.routines.checkdigit.ISBN10CheckDigit import *


class ISBNCheckDigit(CheckDigit):

    ISBN_CHECK_DIGIT: CheckDigit = ISBN10CheckDigit()
    ISBN13_CHECK_DIGIT: CheckDigit = EAN13CheckDigit.EAN13_CHECK_DIGIT
    ISBN10_CHECK_DIGIT: CheckDigit = ISBN10CheckDigit.ISBN10_CHECK_DIGIT
    __serialVersionUID: int = 1391849166205184558

    def isValid(self, code: str) -> bool:
        if code is None:
            return False
        elif len(code) == 10:
            return ISBN10CheckDigit.ISBN10_CHECK_DIGIT.isValid(code)
        elif len(code) == 13:
            return EAN13CheckDigit.EAN13_CHECK_DIGIT.isValid(code)
        else:
            return False

    def calculate(self, code: str) -> str:

        pass  # LLM could not translate this method
