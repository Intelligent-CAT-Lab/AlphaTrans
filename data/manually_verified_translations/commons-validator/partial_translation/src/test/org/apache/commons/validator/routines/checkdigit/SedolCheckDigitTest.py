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
        "026349E",
        "087061C",
        "B06LQ9H",
        "343757F",
        "B07LF5F",
    ]

    def setUp(self) -> None:

        self._valid = [
            ["0263494", "0870612", "B06LQ97", "3437575", "B07LF55"],
        ]
        self._invalid = ["123#567"]
        self._zeroSum = "0000000"
        self._routine = SedolCheckDigit.SEDOL_CHECK_DIGIT

    def testVALIDATOR_346(self) -> None:

        for invalidCheckDigit in self.__invalidCheckDigits:
            self.assertFalse(
                f"Should fail: {invalidCheckDigit}",
                self._routine.isValid(invalidCheckDigit),
            )

    def __init__(self, name: str) -> None:
        super().__init__(name)
