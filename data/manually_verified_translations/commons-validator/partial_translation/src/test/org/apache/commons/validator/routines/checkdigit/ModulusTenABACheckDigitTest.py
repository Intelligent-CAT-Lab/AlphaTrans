from __future__ import annotations
import re
import unittest
import pytest
import io
from src.test.org.apache.commons.validator.routines.checkdigit.AbstractCheckDigitTest import *
from src.main.org.apache.commons.validator.routines.checkdigit.CheckDigit import *
from src.main.org.apache.commons.validator.routines.checkdigit.ModulusTenCheckDigit import *


class ModulusTenABACheckDigitTest(AbstractCheckDigitTest):

    def setUp(self) -> None:
        self._routine = ModulusTenCheckDigit.ModulusTenCheckDigit1([1, 7, 3], True)
        self._valid = [
            "123456780",
            "123123123",
            "011000015",
            "111000038",
            "231381116",
            "121181976",
        ]

    def __init__(self, name: str) -> None:
        super().__init__(name)
