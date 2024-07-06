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

    def setUp(self) -> None:

        self.__invalidCheckDigits = [
            "US037833100O",
            "BMG8571G109D",
            "AU0000XVGZAD",
            "GB000263494I",
            "FR000402625C",
            "DK000976334H",
        ]

        self.routine = ISINCheckDigit.ISIN_CHECK_DIGIT

        self.valid = [
            "US0378331005",
            "BMG8571G1096",
            "AU0000XVGZA3",
            "GB0002634946",
            "FR0004026250",
            "3133EHHF3",
            "DK0009763344",
            "dk0009763344",
            "AU0000xvgza3",
            "EZ0000000003",
            "XS0000000009",
            "AA0000000006",
        ]

        self.invalid = ["0378#3100"]

    def testVALIDATOR_345(self) -> None:

        for invalidCheckDigit in self.__invalidCheckDigits:
            assert not self.routine.isValid(invalidCheckDigit), (
                "Should fail: " + invalidCheckDigit
            )
