from __future__ import annotations
import re
import unittest
import pytest
import io
from src.test.org.apache.commons.validator.routines.checkdigit.AbstractCheckDigitTest import *
from src.main.org.apache.commons.validator.routines.checkdigit.CheckDigit import *
from src.main.org.apache.commons.validator.routines.checkdigit.ISBNCheckDigit import *


class ISBNCheckDigitTest(AbstractCheckDigitTest):

    def setUp(self) -> None:
        super().setUp()
        self._routine = ISBNCheckDigit.ISBN_CHECK_DIGIT
        self._valid = [
            "9780072129519",
            "9780764558313",
            "1930110995",
            "020163385X",
            "1590596277",  # ISBN-10 Ubuntu Book
            "9781590596272",  # ISBN-13 Ubuntu Book
        ]
        self._missingMessage = "ISBN Code is missing"
        self._zeroSum = "000000000000"

    def testInvalidLength(self) -> None:
        self.assertFalse("isValid() Lth 9 ", self._routine.isValid("123456789"))
        self.assertFalse("isValid() Lth 11", self._routine.isValid("12345678901"))
        self.assertFalse("isValid() Lth 12", self._routine.isValid("123456789012"))
        self.assertFalse("isValid() Lth 14", self._routine.isValid("12345678901234"))

        try:
            self._routine.calculate("12345678")
            self.fail("calculate() Lth 8 - expected exception")
        except Exception as e:
            self.assertEqual(
                "calculate() Lth 8", "Invalid ISBN Length = 8", e.getMessage()
            )

        try:
            self._routine.calculate("1234567890")
            self.fail("calculate() Lth 10 - expected exception")
        except Exception as e:
            self.assertEqual(
                "calculate() Lth 10", "Invalid ISBN Length = 10", e.getMessage()
            )

        try:
            self._routine.calculate("12345678901")
            self.fail("calculate() Lth 11 - expected exception")
        except Exception as e:
            self.assertEqual(
                "calculate() Lth 11", "Invalid ISBN Length = 11", e.getMessage()
            )

        try:
            self._routine.calculate("1234567890123")
            self.fail("calculate() Lth 13 - expected exception")
        except Exception as e:
            self.assertEqual(
                "calculate() Lth 13", "Invalid ISBN Length = 13", e.getMessage()
            )

    def __init__(self, name: str) -> None:
        super().__init__(name)
