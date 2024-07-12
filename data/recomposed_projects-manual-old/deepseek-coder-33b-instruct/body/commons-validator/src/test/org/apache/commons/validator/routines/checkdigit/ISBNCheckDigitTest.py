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
        self.routine = ISBNCheckDigit.ISBN_CHECK_DIGIT
        self.valid = [
            "9780072129519",
            "9780764558313",
            "1930110995",
            "020163385X",
            "1590596277",  # ISBN-10 Ubuntu Book
            "9781590596272",  # ISBN-13 Ubuntu Book
        ]
        self.missingMessage = "ISBN Code is missing"
        self.zeroSum = "000000000000"

    def testInvalidLength(self) -> None:

        # Testing isValid method with invalid length
        assert not self.routine.isValid("123456789")
        assert not self.routine.isValid("12345678901")
        assert not self.routine.isValid("123456789012")
        assert not self.routine.isValid("12345678901234")

        # Testing calculate method with invalid length
        try:
            self.routine.calculate("12345678")
            assert False, "calculate() Lth 8 - expected exception"
        except Exception as e:
            assert str(e) == "Invalid ISBN Length = 8", "calculate() Lth 8"

        try:
            self.routine.calculate("1234567890")
            assert False, "calculate() Lth 10 - expected exception"
        except Exception as e:
            assert str(e) == "Invalid ISBN Length = 10", "calculate() Lth 10"

        try:
            self.routine.calculate("12345678901")
            assert False, "calculate() Lth 11 - expected exception"
        except Exception as e:
            assert str(e) == "Invalid ISBN Length = 11", "calculate() Lth 11"

        try:
            self.routine.calculate("1234567890123")
            assert False, "calculate() Lth 13 - expected exception"
        except Exception as e:
            assert str(e) == "Invalid ISBN Length = 13", "calculate() Lth 13"

    def __init__(self, name: str) -> None:

        super().__init__(name)
