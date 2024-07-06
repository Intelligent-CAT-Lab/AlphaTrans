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


class ModulusTenCUSIPCheckDigitTest(AbstractCheckDigitTest):

    __validCheckDigits: typing.List[str] = ["DUS0421C5"]
    __invalidCheckDigits: typing.List[str] = ["DUS0421CW", "DUS0421CN", "DUS0421CE"]

    def _setUp(self) -> None:
        super()._setUp()
        self._routine = ModulusTenCheckDigit([1, 2], True, True)
        self._valid = [
            "037833100",
            "931142103",
            "837649128",
            "392690QT3",
            "594918104",
            "86770G101",
            "Y8295N109",
            "G8572F100",
        ]
        self._invalid = ["0378#3100"]

    def testVALIDATOR_336_ValidCheckDigits(self) -> None:
        for i in range(len(self.__validCheckDigits)):
            validCheckDigit = self.__validCheckDigits[i]
            self.assertTrue(
                "Should fail: " + validCheckDigit,
                self._routine.isValid(validCheckDigit),
            )

    def testVALIDATOR_336_InvalidCheckDigits(self) -> None:
        for i in range(len(self.__invalidCheckDigits)):
            invalidCheckDigit = self.__invalidCheckDigits[i]
            self.assertFalse(
                "Should fail: " + invalidCheckDigit,
                self._routine.isValid(invalidCheckDigit),
            )

    def __init__(self, name: str) -> None:
        super().__init__(name)
