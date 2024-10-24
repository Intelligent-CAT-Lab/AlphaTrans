from __future__ import annotations

# Imports Begin
from src.main.org.apache.commons.validator.routines.checkdigit.ModulusTenCheckDigit import *
from src.main.org.apache.commons.validator.routines.checkdigit.CheckDigit import *
from src.test.org.apache.commons.validator.routines.checkdigit.AbstractCheckDigitTest import *
import unittest
import os
import typing
from typing import *
import io

# Imports End


class ModulusTenCUSIPCheckDigitTest(AbstractCheckDigitTest, unittest.TestCase):

    # Class Fields Begin
    __invalidCheckDigits: typing.List[typing.List[str]] = None
    __validCheckDigits: typing.List[typing.List[str]] = None
    # Class Fields End

    # Class Methods Begin
    def testVALIDATOR_336_ValidCheckDigits_test0_decomposed(self) -> None:
        pass

    def testVALIDATOR_336_InvalidCheckDigits_test0_decomposed(self) -> None:
        pass

    def setUp(self) -> None:
        pass

    def __init__(self, name: str) -> None:
        pass

    # Class Methods End
