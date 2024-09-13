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

    def _createInvalidCodes(
        self, codes: typing.List[typing.List[str]]
    ) -> typing.List[typing.List[str]]:

        list_invalid_codes = []

        for code in codes:
            code_str = self._removeCheckDigit(code[0])
            check = self._checkDigit(code[0])
            for j in range(
                2, 99
            ):  # check digits can be from 02-98 (00 and 01 are not possible)
                curr = str(j) if j > 9 else "0" + str(j)
                if curr != check:
                    list_invalid_codes.append(code_str[:2] + curr + code_str[4:])

        return list_invalid_codes

    def testZeroSum(self) -> None:

        # Create an instance of the IBANCheckDigit class
        iban_check_digit = IBANCheckDigit()

        # Define the IBAN number
        iban = "000000000000000000"

        # Call the calculate method
        result = iban_check_digit.calculate(iban)

        # Assert that the result is as expected
        self.assertEqual(result, "00")

    def _setUp(self) -> None:

        pass  # LLM could not translate this method

    def testOther(self) -> None:

        rdr = None
        try:
            rdr = io.open("IBANtests.txt", "r", encoding="ASCII")
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
