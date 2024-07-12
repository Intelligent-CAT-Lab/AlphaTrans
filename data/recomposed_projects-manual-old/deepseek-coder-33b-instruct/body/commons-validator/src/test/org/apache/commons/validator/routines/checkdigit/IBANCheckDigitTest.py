from __future__ import annotations
import re
import os
import unittest
import pytest
import io
import typing
from typing import *
from src.test.org.apache.commons.validator.routines.checkdigit.AbstractCheckDigitTest import *
from src.main.org.apache.commons.validator.routines.checkdigit.CheckDigit import *
from src.main.org.apache.commons.validator.routines.checkdigit.IBANCheckDigit import *


class IBANCheckDigitTest(AbstractCheckDigitTest):

    def _checkDigit(self, code: str) -> str:

        if code is None or len(code) <= self.checkDigitLth:
            return ""
        return code[2:4]

    def _removeCheckDigit(self, code: str) -> str:
        return code[:2] + "00" + code[4:]

    def _createInvalidCodes(self, codes: typing.List[str]) -> typing.List[str]:

        list_codes = []

        for code in codes:
            code = self._removeCheckDigit(code)
            check = self._checkDigit(code)
            for j in range(
                2, 99
            ):  # check digits can be from 02-98 (00 and 01 are not possible)
                curr = str(j) if j > 9 else "0" + str(j)
                if curr != check:
                    list_codes.append(code[:2] + curr + code[4:])

        return list_codes

    def testZeroSum(self) -> None:
        pass

    def _setUp(self) -> None:

        pass  # LLM could not translate this method

    def testOther(self) -> None:

        # Create a routine object of CheckDigit class
        routine = CheckDigit()

        # Open the file IBANtests.txt
        with open("IBANtests.txt", "r") as rdr:
            for line in rdr:
                line = line.strip()
                if line and not line.startswith("#"):
                    if line.startswith("-"):
                        line = line[1:]
                        assert not routine.isValid(line.replace(" ", "")), line
                    else:
                        assert routine.isValid(line.replace(" ", "")), line

    def __init__(self, name: str) -> None:

        super().__init__(name)
        self._checkDigitLth = 2
