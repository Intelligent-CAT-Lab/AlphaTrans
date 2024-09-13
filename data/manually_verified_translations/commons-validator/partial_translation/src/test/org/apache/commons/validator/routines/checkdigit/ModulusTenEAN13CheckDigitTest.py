from __future__ import annotations
import re
import unittest
import pytest
import io
from src.test.org.apache.commons.validator.routines.checkdigit.AbstractCheckDigitTest import *
from src.main.org.apache.commons.validator.routines.checkdigit.CheckDigit import *
from src.main.org.apache.commons.validator.routines.checkdigit.ModulusTenCheckDigit import *


class ModulusTenEAN13CheckDigitTest(AbstractCheckDigitTest):

    def setUp(self) -> None:
        self._routine = ModulusTenCheckDigit.ModulusTenCheckDigit1([1, 3], True)
        self._valid = [
            "9780072129519",
            "9780764558313",
            "4025515373438",
            "0095673400332",
        ]

    def __init__(self, name: str) -> None:
        super().__init__(name)
