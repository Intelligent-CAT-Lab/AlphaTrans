from __future__ import annotations
import re
import unittest
import pytest
import io
from src.test.org.apache.commons.validator.routines.checkdigit.AbstractCheckDigitTest import *
from src.main.org.apache.commons.validator.routines.checkdigit.CheckDigit import *
from src.main.org.apache.commons.validator.routines.checkdigit.VerhoeffCheckDigit import *


class VerhoeffCheckDigitTest(AbstractCheckDigitTest):

    def testZeroSum(self) -> None:

        # Create an instance of the VerhoeffCheckDigit class
        check_digit = VerhoeffCheckDigit()

        # Define the test data
        test_data = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

        # Iterate over the test data
        for data in test_data:
            # Calculate the check digit
            check_digit_result = check_digit.calculate(data)

            # Assert that the check digit is '0'
            self.assertEqual(check_digit_result, "0")

    def setUp(self) -> None:

        self._valid = ["15", "1428570", "12345678902"]
        self._routine = VerhoeffCheckDigit.VERHOEFF_CHECK_DIGIT

    def __init__(self, name: str) -> None:
        super().__init__(name)
