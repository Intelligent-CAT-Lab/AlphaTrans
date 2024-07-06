from __future__ import annotations
import re
import unittest
import pytest
import io
import typing
from typing import *
from src.test.org.apache.commons.validator.routines.checkdigit.AbstractCheckDigitTest import *
from src.main.org.apache.commons.validator.routines.checkdigit.CheckDigit import *
from src.main.org.apache.commons.validator.routines.checkdigit.ISINCheckDigit import *


class ISINCheckDigitTest(AbstractCheckDigitTest):

    __invalidCheckDigits: typing.List[str] = [
        "US037833100O",
        "BMG8571G109D",
        "AU0000XVGZAD",
        "GB000263494I",
        "FR000402625C",
        "DK000976334H",
    ]

    def _setUp(self) -> None:
        super()._setUp()
        self._routine = ISINCheckDigit.ISIN_CHECK_DIGIT
        self._valid = [
            "US0378331005",
            "BMG8571G1096",
            "AU0000XVGZA3",
            "GB0002634946",
            "FR0004026250",
            "3133EHHF3",  # see VALIDATOR-422 Valid check-digit, but not valid ISIN
            "DK0009763344",
            "dk0009763344",  # TODO lowercase is currently accepted, but is this valid?
            "AU0000xvgza3",  # lowercase NSIN
            "EZ0000000003",  # Invented; for use in ISINValidatorTest
            "XS0000000009",  # ditto
            "AA0000000006",  # ditto
        ]
        self._invalid = ["0378#3100"]

    def testVALIDATOR_345(self) -> None:
        for i in range(len(self.__invalidCheckDigits)):
            invalidCheckDigit = self.__invalidCheckDigits[i]
            self.assertFalse(
                "Should fail: " + invalidCheckDigit,
                self._routine.isValid(invalidCheckDigit),
            )

    def __init__(self, name: str) -> None:
        super().__init__(name)
