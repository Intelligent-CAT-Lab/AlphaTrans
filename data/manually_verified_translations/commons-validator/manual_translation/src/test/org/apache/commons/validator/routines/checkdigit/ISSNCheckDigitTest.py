from __future__ import annotations
import re
import unittest
import pytest
import io
from src.test.org.apache.commons.validator.routines.checkdigit.AbstractCheckDigitTest import *
from src.main.org.apache.commons.validator.routines.checkdigit.CheckDigit import *
from src.main.org.apache.commons.validator.routines.checkdigit.ISSNCheckDigit import *


class ISSNCheckDigitTest(AbstractCheckDigitTest):

    def setUp(self) -> None:

        self._routine = ISSNCheckDigit.ISSN_CHECK_DIGIT
        self._valid = [
            "03178471",
            "1050124X",
            "15626865",
            "10637710",
            "17487188",
            "02642875",
            "17500095",
            "11881534",
            "19111479",
            "19111460",
            "00016772",
            "1365201X",
        ]

        self._invalid = [
            "03178472",  # wrong check
            "1050-124X",  # format char
            " 1365201X",
            "1365201X ",
            " 1365201X ",
        ]

        self._missingMessage = "Code is missing"
        self._zeroSum = "00000000"

    def __init__(self, name: str) -> None:
        super().__init__(name)
