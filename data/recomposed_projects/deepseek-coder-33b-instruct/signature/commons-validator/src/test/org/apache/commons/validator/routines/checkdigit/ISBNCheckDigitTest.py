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

        # Testing isValid() method with invalid length
        assert not self._routine.isValid("123456789")
        assert not self._routine.isValid("12345678901")
        assert not self._routine.isValid("123456789012")
        assert not self._routine.isValid("12345678901234")

        # Testing calculate() method with invalid length
        try:
            self._routine.calculate("12345678")
            pytest.fail("calculate() Lth 8 - expected exception")
        except Exception as e:
            assert str(e) == "Invalid ISBN Length = 8"

        try:
            self._routine.calculate("1234567890")
            pytest.fail("calculate() Lth 10 - expected exception")
        except Exception as e:
            assert str(e) == "Invalid ISBN Length = 10"

        try:
            self._routine.calculate("12345678901")
            pytest.fail("calculate() Lth 11 - expected exception")
        except Exception as e:
            assert str(e) == "Invalid ISBN Length = 11"

        try:
            self._routine.calculate("1234567890123")
            pytest.fail("calculate() Lth 13 - expected exception")
        except Exception as e:
            assert str(e) == "Invalid ISBN Length = 13"

    def __init__(self, name: str) -> None:
        super().__init__(name)
