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

        # Assuming that the routine is an instance of ISBNCheckDigit
        routine = ISBNCheckDigit()

        self.assertFalse(routine.isValid("123456789"))
        self.assertFalse(routine.isValid("12345678901"))
        self.assertFalse(routine.isValid("123456789012"))
        self.assertFalse(routine.isValid("12345678901234"))

        try:
            routine.calculate("12345678")
            pytest.fail("calculate() Lth 8 - expected exception")
        except Exception as e:
            self.assertEqual("Invalid ISBN Length = 8", e.args[0])

        try:
            routine.calculate("1234567890")
            pytest.fail("calculate() Lth 10 - expected exception")
        except Exception as e:
            self.assertEqual("Invalid ISBN Length = 10", e.args[0])

        try:
            routine.calculate("12345678901")
            pytest.fail("calculate() Lth 11 - expected exception")
        except Exception as e:
            self.assertEqual("Invalid ISBN Length = 11", e.args[0])

        try:
            routine.calculate("1234567890123")
            pytest.fail("calculate() Lth 13 - expected exception")
        except Exception as e:
            self.assertEqual("Invalid ISBN Length = 13", e.args[0])

    def __init__(self, name: str) -> None:
        super().__init__(name)
