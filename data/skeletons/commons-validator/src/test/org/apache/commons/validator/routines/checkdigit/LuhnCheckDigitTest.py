from __future__ import annotations

# Imports Begin
from src.main.org.apache.commons.validator.routines.checkdigit.LuhnCheckDigit import *
from src.main.org.apache.commons.validator.routines.checkdigit.CheckDigit import *
from src.test.org.apache.commons.validator.routines.checkdigit.AbstractCheckDigitTest import *
import io

# Imports End


class LuhnCheckDigitTest(AbstractCheckDigitTest):

    # Class Fields Begin
    __VALID_VISA: str = None
    __VALID_SHORT_VISA: str = None
    __VALID_AMEX: str = None
    __VALID_MASTERCARD: str = None
    __VALID_DISCOVER: str = None
    __VALID_DINERS: str = None
    # Class Fields End

    # Class Methods Begin
    def setUp(self) -> None:
        pass

    def __init__(self, name: str) -> None:
        pass

    # Class Methods End
