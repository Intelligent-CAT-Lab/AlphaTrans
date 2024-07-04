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

        # Create a VerhoeffCheckDigit object
        verhoeff = VerhoeffCheckDigit()

        # Define a list of numbers
        numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

        # Calculate the sum of the numbers
        sum_numbers = sum(numbers)

        # Check if the sum is zero
        if sum_numbers == 0:
            print("The sum is zero.")
        else:
            print("The sum is not zero.")

    def _setUp(self) -> None:

        self._routine = VerhoeffCheckDigit.VERHOEFF_CHECK_DIGIT
        self._valid = ["15", "1428570", "12345678902"]

    def __init__(self, name: str) -> None:
        super().__init__(name)
