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

        if code is None or len(code) <= self._checkDigitLth:
            return ""
        return code[2:4]

    def _removeCheckDigit(self, code: str) -> str:
        return code[:2] + "00" + code[4:]

    def _createInvalidCodes(self, codes: typing.List[str]) -> typing.List[str]:

        invalid_codes = []

        for code in codes:
            code_no_check = self._removeCheckDigit(code)
            check = self._checkDigit(code)
            for j in range(
                2, 99
            ):  # check digits can be from 02-98 (00 and 01 are not possible)
                curr = str(j) if j > 9 else "0" + str(j)
                if curr != check:
                    invalid_codes.append(code_no_check[:2] + curr + code_no_check[4:])

        return invalid_codes

    def testZeroSum(self) -> None:

        # The Java code for this method is empty, so there's no translation needed.
        pass

    def _setUp(self) -> None:

        pass  # LLM could not translate this method

    def testOther(self) -> None:

        rdr = None
        try:
            rdr = io.open("IBANtests.txt", mode="r", encoding="ASCII")
            line = rdr.readline()
            while line:
                line = line.strip()
                if line and not line.startswith("#"):
                    if line.startswith("-"):
                        line = line[1:]
                        self.assertFalse(
                            self._routine.isValid(line.replace(" ", "")), line
                        )
                    else:
                        self.assertTrue(
                            self._routine.isValid(line.replace(" ", "")), line
                        )
                line = rdr.readline()
        finally:
            if rdr:
                rdr.close()

    def __init__(self, name: str) -> None:
        super().__init__(name)
        self._checkDigitLth = 2
