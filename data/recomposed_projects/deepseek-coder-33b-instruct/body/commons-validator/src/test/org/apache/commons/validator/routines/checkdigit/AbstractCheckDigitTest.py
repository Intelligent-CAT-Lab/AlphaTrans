from __future__ import annotations
import re
import pickle
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
        "0123456789 ABCDEFHIJKLMNOPQRSTUVWXYZ\tabcdefghijklmnopqrstuvwxyz¡¢£¤¥¦§¨©ª«¬­®¯°±²³´µ¶·¸¹º»¼½¾¿��ÂÃÄÅÆÇÈÉÊËÌÍÎÏÐÑÒÓÔÕÖ×ØÙÚÛÜÝÞßàáâãäåæçèéêëìíîïðñòóô�����������"
    )

    def _tearDown(self) -> None:

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

    def _createInvalidCodes(self, codes: typing.List[str]) -> typing.List[str]:

        list = []

        for fullCode in codes:
            code = self._removeCheckDigit(fullCode)
            check = self._checkDigit(fullCode)
            for j in range(len(self.__POSSIBLE_CHECK_DIGITS)):
                curr = self.__POSSIBLE_CHECK_DIGITS[j]
                if curr != check:
                    list.append(code + curr)

        return list

    def testSerialization(self) -> None:

        baos = io.BytesIO()
        try:
            oos = pickle.Pickler(baos)
            oos.dump(self._routine)
            oos.flush()
            oos.clear()
        except Exception as e:
            self.fail(
                self._routine.__class__.__name__
                + " error during serialization: "
                + str(e)
            )

        result = None
        try:
            bais = io.BytesIO(baos.getvalue())
            ois = pickle.Unpickler(bais)
            result = ois.load()
            bais.close()
        except Exception as e:
            self.fail(
                self._routine.__class__.__name__
                + " error during deserialization: "
                + str(e)
            )
        self.assertIsNotNone(result)

    def testZeroSum(self) -> None:

        assert not self._routine.isValid(self._zeroSum), "isValid() Zero Sum"

        try:
            self._routine.calculate(self._zeroSum)
            self.fail("Zero Sum - expected exception")
        except Exception as e:
            self.assertEqual(str(e), "Invalid code, sum is zero", "isValid() Zero Sum")

    def testMissingCode(self) -> None:

        self.assertFalse("isValid() Null", self._routine.isValid(None))

        self.assertFalse("isValid() Zero Length", self._routine.isValid(""))

        self.assertFalse("isValid() Length 1", self._routine.isValid("9"))

        try:
            self._routine.calculate(None)
            self.fail("calculate() Null - expected exception")
        except Exception as e:
            self.assertEqual("calculate() Null", self._missingMessage, str(e))

        try:
            self._routine.calculate("")
            self.fail("calculate() Zero Length - expected exception")
        except Exception as e:
            self.assertEqual("calculate() Zero Length", self._missingMessage, str(e))

    def testCalculateInvalid(self) -> None:

        if self._log.isDebugEnabled():
            self._log.debug(
                "testCalculateInvalid() for " + self._routine.__class__.__name__
            )

        for i in range(len(self._invalid)):
            try:
                code = self._invalid[i]
                if self._log.isDebugEnabled():
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

        if self._log.isDebugEnabled():
            self._log.debug(
                "testCalculateValid() for " + self._routine.__class__.__name__
            )

        for i in range(len(self._valid)):
            code = self._removeCheckDigit(self._valid[i])
            expected = self._checkDigit(self._valid[i])
            try:
                if self._log.isDebugEnabled():
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

        for i in range(len(self._invalid)):
            if self._log.isDebugEnabled():
                self._log.debug(
                    "   " + str(i) + " Testing Invalid Code=[" + self._invalid[i] + "]"
                )
            self.assertFalse(
                self._routine.isValid(self._invalid[i]),
                "invalid[" + str(i) + "]: " + self._invalid[i],
            )

        invalidCheckDigits = self._createInvalidCodes(self._valid)
        for i in range(len(invalidCheckDigits)):
            if self._log.isDebugEnabled():
                self._log.debug(
                    "   "
                    + str(i)
                    + " Testing Invalid Check Digit, Code=["
                    + invalidCheckDigits[i]
                    + "]"
                )
            self.assertFalse(
                self._routine.isValid(invalidCheckDigits[i]),
                "invalid check digit[" + str(i) + "]: " + invalidCheckDigits[i],
            )

    def testIsValidTrue(self) -> None:

        if self._log.isDebugEnabled():
            self._log.debug("testIsValidTrue() for " + self._routine.__class__.__name__)

        for i in range(len(self._valid)):
            if self._log.isDebugEnabled():
                self._log.debug(
                    "   " + str(i) + " Testing Valid Code=[" + self._valid[i] + "]"
                )
            self.assertTrue(
                self._routine.isValid(self._valid[i]),
                "valid[" + str(i) + "]: " + self._valid[i],
            )

    def __init__(self, name: str) -> None:

        super().__init__(name)
