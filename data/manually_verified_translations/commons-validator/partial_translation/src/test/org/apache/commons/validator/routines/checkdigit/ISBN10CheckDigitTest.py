from __future__ import annotations
import re
import unittest
import pytest
import io
from src.test.org.apache.commons.validator.routines.checkdigit.AbstractCheckDigitTest import *
from src.main.org.apache.commons.validator.routines.checkdigit.CheckDigit import *
from src.main.org.apache.commons.validator.routines.checkdigit.ISBN10CheckDigit import *


class ISBN10CheckDigitTest(AbstractCheckDigitTest):

    def setUp(self) -> None:

        self._valid = ["1930110995", "020163385X", "1932394354", "1590596277"]
        self._routine = ISBN10CheckDigit.ISBN10_CHECK_DIGIT

    def __init__(self, name: str) -> None:
        super().__init__(name)
