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

        self.__validCheckDigits = [
            "037833100",
            "931142103",
            "837649128",
            "392690QT3",
            "594918104",
            "86770G101",
            "Y8295N109",
            "G8572F100",
        ]
        self.__invalidCheckDigits = ["0378#3100"]

    def testVALIDATOR_336_ValidCheckDigits(self) -> None:

        for validCheckDigit in self.__validCheckDigits:
            self.assertTrue(
                self.routine.isValid(validCheckDigit), "Should fail: " + validCheckDigit
            )

    def testVALIDATOR_336_InvalidCheckDigits(self) -> None:

        for invalidCheckDigit in self.__invalidCheckDigits:
            assert not self.routine.isValid(invalidCheckDigit), (
                "Should fail: " + invalidCheckDigit
            )
