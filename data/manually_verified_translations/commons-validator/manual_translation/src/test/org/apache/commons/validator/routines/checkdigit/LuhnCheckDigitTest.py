from __future__ import annotations
import re
import unittest
import pytest
import io
from src.test.org.apache.commons.validator.routines.checkdigit.AbstractCheckDigitTest import *
from src.main.org.apache.commons.validator.routines.checkdigit.CheckDigit import *
from src.main.org.apache.commons.validator.routines.checkdigit.LuhnCheckDigit import *


class LuhnCheckDigitTest(AbstractCheckDigitTest):

    __VALID_DINERS: str = "30569309025904"
    __VALID_DISCOVER: str = "6011000990139424"
    __VALID_MASTERCARD: str = "5105105105105100"
    __VALID_AMEX: str = "378282246310005"
    __VALID_SHORT_VISA: str = "4222222222222"
    __VALID_VISA: str = "4417123456789113"

    def setUp(self) -> None:

        self._routine = LuhnCheckDigit.LUHN_CHECK_DIGIT

        self._valid = [
            self.__VALID_VISA,
            self.__VALID_SHORT_VISA,
            self.__VALID_AMEX,
            self.__VALID_MASTERCARD,
            self.__VALID_DISCOVER,
            self.__VALID_DINERS,
        ]

    def __init__(self, name: str) -> None:
        super().__init__(name)
