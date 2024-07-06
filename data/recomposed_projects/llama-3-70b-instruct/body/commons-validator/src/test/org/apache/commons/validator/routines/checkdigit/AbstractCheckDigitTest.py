from __future__ import annotations
import re
import os
from io import BytesIO
import unittest
import pytest
from abc import ABC
import io
import typing
from typing import *
import unittest
import logging

# from src.main.org.apache.commons.logging.Log import *
# from src.main.org.apache.commons.logging.LogFactory import *
from src.main.org.apache.commons.validator.routines.checkdigit.CheckDigit import *
from src.main.org.apache.commons.validator.routines.checkdigit.CheckDigitException import *


class AbstractCheckDigitTest(unittest.TestCase, ABC):

    _missingMessage: str = "Code is missing"
    _zeroSum: str = "0000000000"
    _invalid: typing.List[str] = ["12345678A"]
    _valid: typing.List[str] = None

    _routine: CheckDigit = None

    _checkDigitLth: int = 1
    _log: logging.Logger = logging.getLogger(__name__)
    __POSSIBLE_CHECK_DIGITS: str = (
        "0123456789 ABCDEFHIJKLMNOPQRSTUVWXYZ\tabcdefghijklmnopqrstuvwxyz!@£$%^&*()_+"
    )

    def _tearDown(self) -> None:
        super()._tearDown()
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
        return code[0 : len(code) - self._checkDigitLth]

    def _createInvalidCodes(self, codes: typing.List[str]) -> typing.List[str]:
        list: typing.List[str] = []
        for fullCode in codes:
            code = self._removeCheckDigit(fullCode)
            check = self._checkDigit(fullCode)
            for j in range(0, len(self.__POSSIBLE_CHECK_DIGITS)):
                curr = self.__POSSIBLE_CHECK_DIGITS[j : j + 1]
                if not curr == check:
                    list.append(code + curr)
        return list

    def testSerialization(self) -> None:
        baos = io.BytesIO()
        try:
            oos = io.ObjectOutputStream(baos)
            oos.writeObject(self._routine)
            oos.flush()
            oos.close()
        except Exception as e:
            self.fail(
                self._routine.getClass().getName() + " error during serialization: " + e
            )

        result = None
        try:
            bais = io.ByteArrayInputStream(baos.toByteArray())
            ois = io.ObjectInputStream(bais)
            result = ois.readObject()
            bais.close()
        except Exception as e:
            self.fail(
                self._routine.getClass().getName()
                + " error during deserialization: "
                + e
            )
        self.assertNotNull(result)

    def testZeroSum(self) -> None:
        self.assertFalse("isValid() Zero Sum", self._routine.isValid(self._zeroSum))

        try:
            self._routine.calculate(self._zeroSum)
            self.fail("Zero Sum - expected exception")
        except Exception as e:
            self.assertEqual(
                "isValid() Zero Sum", "Invalid code, sum is zero", e.getMessage()
            )

    def testMissingCode(self) -> None:
        self.assertFalse("isValid() Null", self._routine.isValid(None))

        self.assertFalse("isValid() Zero Length", self._routine.isValid(""))

        self.assertFalse("isValid() Length 1", self._routine.isValid("9"))

        try:
            self._routine.calculate(None)
            self.fail("calculate() Null - expected exception")
        except Exception as e:
            self.assertEqual("calculate() Null", self._missingMessage, e.getMessage())

        try:
            self._routine.calculate("")
            self.fail("calculate() Zero Length - expected exception")
        except Exception as e:
            self.assertEqual(
                "calculate() Zero Length", self._missingMessage, e.getMessage()
            )

    def testCalculateInvalid(self) -> None:
        if self._log.isEnabledFor(logging.DEBUG):
            self._log.debug(
                "testCalculateInvalid() for " + self._routine.__class__.__name__
            )
        for i in range(len(self._invalid)):
            try:
                code = self._invalid[i]
                if self._log.isEnabledFor(logging.DEBUG):
                    self._log.debug(
                        "   "
                        + str(i)
                        + " Testing Invalid Check Digit, Code=["
                        + code
                        + "]"
                    )
                expected = self._checkDigit(code)
                actual = self._routine.calculate(self._removeCheckDigit(code))
                if expected == actual:
                    self.fail(
                        "Expected mismatch for "
                        + code
                        + " expected "
                        + expected
                        + " actual "
                        + actual
                    )
            except CheckDigitException as e:
                self.assertTrue(
                    "Invalid Character[" + str(i) + "]=" + e.getMessage(),
                    e.getMessage().startswith("Invalid "),
                )

    def testCalculateValid(self) -> None:
        if self._log.isEnabledFor(logging.DEBUG):
            self._log.debug(
                "testCalculateValid() for " + self._routine.__class__.__name__
            )
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
                    "valid[" + str(i) + "]: " + self._valid[i],
                    expected,
                    self._routine.calculate(code),
                )
            except Exception as e:
                self.fail(
                    "valid[" + str(i) + "]=" + self._valid[i] + " threw " + str(e)
                )

    def testIsValidFalse(self) -> None:
        if self._log.isEnabledFor(logging.DEBUG):
            self._log.debug(
                "testIsValidFalse() for " + self._routine.__class__.__name__
            )
        for i in range(0, len(self._invalid)):
            if self._log.isEnabledFor(logging.DEBUG):
                self._log.debug(
                    "   " + str(i) + " Testing Invalid Code=[" + self._invalid[i] + "]"
                )
            self.assertFalse(
                "invalid[" + str(i) + "]: " + self._invalid[i],
                self._routine.isValid(self._invalid[i]),
            )
        invalidCheckDigits = self._createInvalidCodes(self._valid)
        for i in range(0, len(invalidCheckDigits)):
            if self._log.isEnabledFor(logging.DEBUG):
                self._log.debug(
                    "   "
                    + str(i)
                    + " Testing Invalid Check Digit, Code=["
                    + invalidCheckDigits[i]
                    + "]"
                )
            self.assertFalse(
                "invalid check digit[" + str(i) + "]: " + invalidCheckDigits[i],
                self._routine.isValid(invalidCheckDigits[i]),
            )

    def testIsValidTrue(self) -> None:
        if self._log.isEnabledFor(logging.DEBUG):
            self._log.debug("testIsValidTrue() for " + self._routine.__class__.__name__)

        for i in range(len(self._valid)):
            if self._log.isEnabledFor(logging.DEBUG):
                self._log.debug(
                    "   " + str(i) + " Testing Valid Code=[" + self._valid[i] + "]"
                )

            self.assertTrue(
                "valid[" + str(i) + "]: " + self._valid[i],
                self._routine.isValid(self._valid[i]),
            )

    def __init__(self, name: str) -> None:
        super().__init__(name)
