from __future__ import annotations
import locale
import re
import os
import unittest
import pytest
import io
import numbers
from src.main.org.apache.commons.validator.routines.AbstractNumberValidator import *
from src.test.org.apache.commons.validator.routines.AbstractNumberValidatorTest import *
from src.main.org.apache.commons.validator.routines.FloatValidator import *


class FloatValidatorTest(AbstractNumberValidatorTest):

    def _setUp(self) -> None:

        pass  # LLM could not translate this method

    def testFloatRangeMinMax(self) -> None:
        validator: FloatValidator = self._strictValidator
        number9: float = validator.validate1("9", "#")
        number10: float = validator.validate1("10", "#")
        number11: float = validator.validate1("11", "#")
        number19: float = validator.validate1("19", "#")
        number20: float = validator.validate1("20", "#")
        number21: float = validator.validate1("21", "#")

        self.assertFalse("isInRange() < min", validator.isInRange1(number9, 10, 20))
        self.assertTrue("isInRange() = min", validator.isInRange1(number10, 10, 20))
        self.assertTrue("isInRange() in range", validator.isInRange1(number11, 10, 20))
        self.assertTrue("isInRange() = max", validator.isInRange1(number20, 10, 20))
        self.assertFalse("isInRange() > max", validator.isInRange1(number21, 10, 20))

        self.assertFalse("minValue() < min", validator.minValue1(number9, 10))
        self.assertTrue("minValue() = min", validator.minValue1(number10, 10))
        self.assertTrue("minValue() > min", validator.minValue1(number11, 10))

        self.assertTrue("maxValue() < max", validator.maxValue1(number19, 20))
        self.assertTrue("maxValue() = max", validator.maxValue1(number20, 20))
        self.assertFalse("maxValue() > max", validator.maxValue1(number21, 20))

    def testFloatSmallestValues(self) -> None:
        pattern: str = (
            "#.#################################################################"
        )
        fmt: AbstractFormatValidator = AbstractFormatValidator(pattern)

        smallestPositive: float = float(Float.MIN_VALUE)
        strSmallestPositive: str = fmt.format(smallestPositive)
        self.assertEqual(
            "Smallest +ve",
            smallestPositive,
            FloatValidator.getInstance().validate1(strSmallestPositive, pattern),
        )

        smallestNegative: float = float(Float.MIN_VALUE * -1)
        strSmallestNegative: str = fmt.format(smallestNegative)
        self.assertEqual(
            "Smallest -ve",
            smallestNegative,
            FloatValidator.getInstance().validate1(strSmallestNegative, pattern),
        )

        tooSmallPositive: float = float(((float(Float.MIN_VALUE) / float(10))))
        strTooSmallPositive: str = fmt.format(tooSmallPositive)
        self.assertFalse(
            "Too small +ve",
            FloatValidator.getInstance().isValid1(strTooSmallPositive, pattern),
        )

        tooSmallNegative: float = float(tooSmallPositive * -1)
        strTooSmallNegative: str = fmt.format(tooSmallNegative)
        self.assertFalse(
            "Too small -ve",
            FloatValidator.getInstance().isValid1(strTooSmallNegative, pattern),
        )

    def testFloatValidatorMethods(self) -> None:
        locale = Locale.GERMAN
        pattern = "0,00,00"
        patternVal = "1,23,45"
        localeVal = "12.345"
        germanPatternVal = "1.23.45"
        defaultVal = "12,345"
        XXXX = "XXXX"
        expected = Float.valueOf(12345)
        self.assertEqual(
            "validate(A) default",
            expected,
            FloatValidator.getInstance().validate0(defaultVal),
        )
        self.assertEqual(
            "validate(A) locale ",
            expected,
            FloatValidator.getInstance().validate2(localeVal, locale),
        )
        self.assertEqual(
            "validate(A) pattern",
            expected,
            FloatValidator.getInstance().validate1(patternVal, pattern),
        )
        self.assertEqual(
            "validate(A) both",
            expected,
            FloatValidator.getInstance().validate3(
                germanPatternVal, pattern, Locale.GERMAN
            ),
        )

        self.assertTrue(
            "isValid(A) default", FloatValidator.getInstance().isValid0(defaultVal)
        )
        self.assertTrue(
            "isValid(A) locale ",
            FloatValidator.getInstance().isValid2(localeVal, locale),
        )
        self.assertTrue(
            "isValid(A) pattern",
            FloatValidator.getInstance().isValid1(patternVal, pattern),
        )
        self.assertTrue(
            "isValid(A) both",
            FloatValidator.getInstance().isValid3(
                germanPatternVal, pattern, Locale.GERMAN
            ),
        )

        self.assertIsNone(
            "validate(B) default", FloatValidator.getInstance().validate0(XXXX)
        )
        self.assertIsNone(
            "validate(B) locale ", FloatValidator.getInstance().validate2(XXXX, locale)
        )
        self.assertIsNone(
            "validate(B) pattern", FloatValidator.getInstance().validate1(XXXX, pattern)
        )
        self.assertIsNone(
            "validate(B) both",
            FloatValidator.getInstance().validate3(patternVal, pattern, Locale.GERMAN),
        )

        self.assertFalse(
            "isValid(B) default", FloatValidator.getInstance().isValid0(XXXX)
        )
        self.assertFalse(
            "isValid(B) locale ", FloatValidator.getInstance().isValid2(XXXX, locale)
        )
        self.assertFalse(
            "isValid(B) pattern", FloatValidator.getInstance().isValid1(XXXX, pattern)
        )
        self.assertFalse(
            "isValid(B) both",
            FloatValidator.getInstance().isValid3(patternVal, pattern, Locale.GERMAN),
        )

    def __init__(self, name: str) -> None:
        super().__init__(name)
