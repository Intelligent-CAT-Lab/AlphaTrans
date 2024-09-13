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

        pass

    def setUp(self) -> None:

        self._valid = ["15", "1428570", "12345678902"]
        self._routine = VerhoeffCheckDigit.VERHOEFF_CHECK_DIGIT

    def __init__(self, name: str) -> None:
        super().__init__(name)
