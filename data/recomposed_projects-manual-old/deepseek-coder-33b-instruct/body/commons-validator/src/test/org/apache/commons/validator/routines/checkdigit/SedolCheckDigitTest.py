from __future__ import annotations
import re
import unittest
import pytest
import io
import typing
from typing import *
from src.test.org.apache.commons.validator.routines.checkdigit.AbstractCheckDigitTest import *
from src.main.org.apache.commons.validator.routines.checkdigit.CheckDigit import *
from src.main.org.apache.commons.validator.routines.checkdigit.SedolCheckDigit import *


class SedolCheckDigitTest(AbstractCheckDigitTest):

    __invalidCheckDigits: typing.List[str] = [
        "026349E",  # proper check digit is '4', see above
        "087061C",  # proper check digit is '2', see above
        "B06LQ9H",  # proper check digit is '7', see above
        "343757F",  # proper check digit is '5', see above
        "B07LF5F",  # proper check digit is '5', see above
    ]

    def setUp(self) -> None:

        self.__invalidCheckDigits = [
            "026349E",
            "087061C",
            "B06LQ9H",
            "343757F",
            "B07LF5F",
        ]

        self.routine = SedolCheckDigit.SEDOL_CHECK_DIGIT

        self.valid = [
            "0263494",
            "0870612",
            "B06LQ97",
            "3437575",
            "B07LF55",
        ]

        self.invalid = ["123#567"]

        self.zeroSum = "0000000"

    def testVALIDATOR_346(self) -> None:

        for invalidCheckDigit in self.__invalidCheckDigits:
            assert not self.routine.isValid(invalidCheckDigit), (
                "Should fail: " + invalidCheckDigit
            )

    # def __init__(self, name: str) -> None:
    #
    #     pass  # LLM could not translate this method
