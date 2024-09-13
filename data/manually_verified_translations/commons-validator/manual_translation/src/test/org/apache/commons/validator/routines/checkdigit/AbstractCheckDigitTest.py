from __future__ import annotations
import re
import os
import enum
from io import BytesIO
import unittest
import pytest
from abc import ABC
import pickle
import typing
from typing import *
import unittest
import logging

from src.main.org.apache.commons.validator.routines.checkdigit.CheckDigit import *
from src.main.org.apache.commons.validator.routines.checkdigit.CheckDigitException import *


class AbstractCheckDigitTest(unittest.TestCase, ABC):

    _missingMessage: str = "Code is missing"
    _zeroSum: str = "0000000000"
    _invalid: typing.List[str] = ["12345678A"]
    _valid: typing.List[typing.List[str]] = None

    _routine: CheckDigit = None

    _checkDigitLth: int = 1
    _log: logging.Logger = logging.getLogger(__name__)
    __POSSIBLE_CHECK_DIGITS: str = (
        "0123456789 ABCDEFHIJKLMNOPQRSTUVWXYZ\tabcdefghijklmnopqrstuvwxyz!\@£$%^&*()_+"
    )

    def tearDown(self) -> None:

        super().tearDown()
        self._valid = None
        self._routine = None

    def _checkDigit(self, code: str) -> str:

        if code is None or len(code) <= self._checkDigitLth:
            return ""

        start = len(code) - self._checkDigitLth
        return code[start:]

    def _removeCheckDigit(self, code: str) -> str:

        if code is None or len(code) <= self._checkDigitLth:
            return None
        return code[: -self._checkDigitLth]

    def _createInvalidCodes(
        self, codes: typing.List[typing.List[str]]
    ) -> typing.List[typing.List[str]]:

        list_invalid_codes = []

        for fullCode in codes:
            code = self._removeCheckDigit(fullCode)
            check = self._checkDigit(fullCode)
            for j in range(len(self.__POSSIBLE_CHECK_DIGITS)):
                curr = self.__POSSIBLE_CHECK_DIGITS[j]
                if curr != check:
                    list_invalid_codes.append(code + curr)

        return list_invalid_codes

    def testSerialization(self) -> None:

        baos = BytesIO()
        try:
            pickle.dump(self._routine, baos)
        except Exception as e:
            self.fail(f"{self._routine.__class__.__name__} error during serialization: {e}")

        result = None
        try:
            bais = BytesIO(baos.getvalue())
            result = pickle.load(bais)
        except Exception as e:
            self.fail(f"{self._routine.__class__.__name__} error during deserialization: {e}")
        
        self.assertIsNotNone(result)

    def testZeroSum(self) -> None:

        self.assertFalse(self._routine.isValid(self._zeroSum), "isValid() Zero Sum")

        try:
            self._routine.calculate(self._zeroSum)
            pytest.fail("Zero Sum - expected exception")
        except Exception as e:
            self.assertIn("Invalid code, sum is zero", str(e), "isValid() Zero Sum")

    def testMissingCode(self) -> None:

        self.assertFalse(self._routine.isValid(None), "isValid() Null")
        self.assertFalse(self._routine.isValid(""), "isValid() Zero Length")
        self.assertFalse(self._routine.isValid("9"), "isValid() Length 1")

        try:
            self._routine.calculate(None)
            pytest.fail("calculate() Null - expected exception")
        except Exception as e:
            self.assertIn(self._missingMessage, str(e), "calculate() Null")

        try:
            self._routine.calculate("")
            pytest.fail("calculate() Zero Length - expected exception")
        except Exception as e:
            self.assertIn(
                self._missingMessage, str(e), "calculate() Zero Length"
            )

    def testCalculateInvalid(self) -> None:

        for i, code in enumerate(self._invalid):
            if self._log.isEnabledFor(logging.DEBUG):
                self._log.debug(
                    f"testCalculateInvalid() for {self._routine.__class__.__name__}"
                )
                self._log.debug(f"   {i} Testing Invalid Check Digit, Code=[{code}]")

            try:
                expected = self._checkDigit(code)
                actual = self._routine.calculate(self._removeCheckDigit(code))
                if expected == actual:
                    pytest.fail(
                        f"Expected mismatch for {code}, expected {expected}, actual {actual}"
                    )
            except CheckDigitException as e:
                self.assertTrue(
                    e.args[0].startswith("Invalid "),
                    f"Invalid Character[{i}]={e}",
                )

    def testCalculateValid(self) -> None:

        if self._log.isEnabledFor(logging.DEBUG):
            self._log.debug("testCalculateValid() for " + type(self._routine).__name__)

        for i in range(len(self._valid)):
            code = self._removeCheckDigit(self._valid[i])
            expected = self._checkDigit(self._valid[i])
            try:
                if self._log.isEnabledFor(logging.DEBUG):
                    self._log.debug(
                        "   "
                        + str(i)
                        + " Testing Valid Check Digit, Code=["
                        + code
                        + "] expected=["
                        + expected
                        + "]"
                    )
                self.assertEqual(
                    expected,
                    self._routine.calculate(code),
                    "valid[" + str(i) + "]: " + self._valid[i],
                )
            except Exception as e:
                pytest.fail(
                    "valid[" + str(i) + "]=" + self._valid[i] + " threw " + str(e)
                )

    def testIsValidFalse(self) -> None:

        for i, invalid_code in enumerate(self._invalid):
            if self._log.isEnabledFor(logging.DEBUG):
                self._log.debug(f"Testing Invalid Code=[{invalid_code}]")
            self.assertFalse(
                self._routine.isValid(invalid_code), f"invalid[{i}]: {invalid_code}"
            )

        invalid_check_digits = self._createInvalidCodes(self._valid)
        for i, invalid_check_digit in enumerate(invalid_check_digits):
            if self._log.isEnabledFor(logging.DEBUG):
                self._log.debug(
                    f"Testing Invalid Check Digit, Code=[{invalid_check_digit}]"
                )
            self.assertFalse(
                self._routine.isValid(invalid_check_digit),
                f"invalid check digit[{i}]: {invalid_check_digit}",
            )

    def testIsValidTrue(self) -> None:

        if self._log.isEnabledFor(logging.DEBUG):
            self._log.debug("testIsValidTrue() for " + type(self._routine).__name__)

        for i in range(len(self._valid)):
            if self._log.isEnabledFor(logging.DEBUG):
                self._log.debug(
                    "   " + str(i) + " Testing Valid Code=[" + self._valid[i] + "]"
                )
            self.assertTrue(
                self._routine.isValid(self._valid[i]),
                "valid[" + str(i) + "]: " + self._valid[i],
            )

    def __init__(self, name: str) -> None:
        super().__init__(name)
