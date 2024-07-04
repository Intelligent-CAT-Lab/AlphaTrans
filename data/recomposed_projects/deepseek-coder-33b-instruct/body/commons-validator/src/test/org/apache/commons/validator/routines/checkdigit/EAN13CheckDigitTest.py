from __future__ import annotations
import re
import unittest
import pytest
import io
from src.test.org.apache.commons.validator.routines.checkdigit.AbstractCheckDigitTest import *
from src.main.org.apache.commons.validator.routines.checkdigit.CheckDigit import *
from src.main.org.apache.commons.validator.routines.checkdigit.EAN13CheckDigit import *


class EAN13CheckDigitTest(AbstractCheckDigitTest):

    def _setUp(self) -> None:
        super()._setUp()
        self.routine = EAN13CheckDigit.EAN13_CHECK_DIGIT
        self.valid = [
            "9780072129519",
            "9780764558313",
            "4025515373438",
            "0095673400332",
        ]

    def __init__(self, name: str) -> None:

        super().__init__(name)
