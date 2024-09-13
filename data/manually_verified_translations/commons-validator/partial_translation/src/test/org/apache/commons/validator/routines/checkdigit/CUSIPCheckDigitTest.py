from __future__ import annotations
import re
import unittest
import pytest
import io
import typing
from typing import *
from src.test.org.apache.commons.validator.routines.checkdigit.AbstractCheckDigitTest import *
from src.main.org.apache.commons.validator.routines.checkdigit.CUSIPCheckDigit import *
from src.main.org.apache.commons.validator.routines.checkdigit.CheckDigit import *


class CUSIPCheckDigitTest(AbstractCheckDigitTest):

    __validCheckDigits: typing.List[str] = ["DUS0421C5"]
    __invalidCheckDigits: typing.List[str] = ["DUS0421CW", "DUS0421CN", "DUS0421CE"]

    def setUp(self) -> None:

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
        self._routine = CUSIPCheckDigit.CUSIP_CHECK_DIGIT

    def testVALIDATOR_336_ValidCheckDigits(self) -> None:

        for validCheckDigit in self._validCheckDigits:
            self.assertTrue(
                self._routine.isValid(validCheckDigit),
                "Should fail: " + validCheckDigit,
            )

    def testVALIDATOR_336_InvalidCheckDigits(self) -> None:

        # Assuming that the CUSIPCheckDigit class has an isValid method that checks the validity of a CUSIP code
        # If it doesn't, you need to implement it
        for invalidCheckDigit in self.__invalidCheckDigits:
            self.assertFalse(
                "Should fail: " + invalidCheckDigit,
                self._routine.isValid(invalidCheckDigit),
            )

    def __init__(self, name: str) -> None:
        super().__init__(name)
