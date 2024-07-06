from __future__ import annotations
import re
import unittest
import pytest
import io
import typing
from typing import *
from src.test.org.apache.commons.validator.routines.checkdigit.AbstractCheckDigitTest import *
from src.main.org.apache.commons.validator.routines.checkdigit.CheckDigit import *
from src.main.org.apache.commons.validator.routines.checkdigit.ModulusTenCheckDigit import *


class ModulusTenSedolCheckDigitTest(AbstractCheckDigitTest):

    __invalidCheckDigits: typing.List[str] = [
        "026349E",
        "087061C",
        "B06LQ9H",
        "343757F",
        "B07LF5F",
    ]

    def setUp(self) -> None:

        self.__invalidCheckDigits = [
            "026349E",
            "087061C",
            "B06LQ9H",
            "343757F",
            "B07LF5F",
        ]

        self.routine = ModulusTenCheckDigit.ModulusTenCheckDigit2([1, 3, 1, 7, 3, 9, 1])
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
