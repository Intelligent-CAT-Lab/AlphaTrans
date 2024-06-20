import pytest

import unittest
import pickle
from abc import ABC
from io import BytesIO
from decimal import Decimal
from locale import setlocale, LC_NUMERIC
from src.main.org.apache.commons.validator.routines.AbstractNumberValidator import *

class AbstractNumberValidatorTest(unittest.TestCase, ABC):

    __test__ = False
    

    _validator = None
    _strictValidator = None

    _max = None
    _maxPlusOne = None
    _min = None
    _minMinusOne = None
    _invalid = None
    _valid = None
    _validCompare = None

    _invalidStrict = None
    _validStrict = None
    _validStrictCompare = None

    _testPattern = None
    _testNumber = None
    _testZero = None
    _testStringUS = None
    _testStringDE = None

    _localeValue = None
    _localePattern = None
    _testLocale = None
    _localeExpected = None

    
    
    def setUp(self) -> None:
        try:
            super().setUp()

            setlocale(LC_NUMERIC, 'en_US.UTF-8')

        except Exception as e:
            self.fail(f"An exception occurred when setting up the test: {e}")
    
    
    def tearDown(self) -> None:
        try:
            super().tearDown()
            self._validator = None
            self._strictValidator = None
        except Exception as e:
            self.fail(f"An exception occurred when cleaning up the test: {e}")

    
    @pytest.mark.test
    def testFormatType(self) -> None:
        self.assertEqual(0, self._validator.getFormatType(), "Format Type A")
        self.assertEqual(
            AbstractNumberValidator.STANDARD_FORMAT,
            self._validator.getFormatType(),
            "Format Type B"
        )

    
    @pytest.mark.test
    def testValidateMinMax(self) -> None:
        if self._max is not None:
            self.assertEqual(
                self._max,
                self._validator.parse(str(self._max), '#', None),
                "Test Max"
            )
            self.assertIsNone(
                self._validator.parse(str(self._maxPlusOne), '#', None),
                "Test Max + 1"
            )
            self.assertEqual(
                self._min,
                self._validator.parse(str(self._min), '#', None),
                "Test Min"
            )
            self.assertIsNone(
                self._validator.parse(str(self._minMinusOne), '#', None),
                "Test min - 1"
            )

    
    @pytest.mark.test
    def testInvalidStrict(self) -> None:
        for i, val in enumerate(self._invalidStrict):
            text = f"idx=[{i}] value=[{val}]"
            self.assertIsNone(
                self._strictValidator.parse(val, None, 'en_US.UTF-8'),
                f"(A) {text}"
            )
            self.assertFalse(
                self._strictValidator.isValid3(val, None, 'en_US.UTF-8'),
                f"(B) {text}"
            )
            self.assertIsNone(
                self._strictValidator.parse(val, self._testPattern, None),
                f"(C) {text}"
            )
            self.assertFalse(
                self._strictValidator.isValid3(val, self._testPattern, None),
                f"(D) {text}"
            )

    
    @pytest.mark.test
    def testInvalidNotStrict(self) -> None:
        for i, val in enumerate(self._invalid):
            text = f"idx=[{i}] value=[{val}]"
            self.assertIsNone(
                self._validator.parse(val, None, 'en_US.UTF-8'),
                f"(A) {text}"
            )
            self.assertFalse(
                self._validator.isValid3(val, None, 'en_US.UTF-8'),
                f"(B) {text}"
            )
            self.assertIsNone(
                self._validator.parse(val, self._testPattern, None),
                f"(C) {text}"
            )
            self.assertFalse(
                self._validator.isValid3(val, self._testPattern, None),
                f"(D) {text}"
            )

    
    @pytest.mark.test
    def testValidStrict(self) -> None:
        for i, val in enumerate(self._validStrict):
            text = f"idx=[{i}] value=[{self._validStrictCompare[i]}]"
            self.assertEqual(
                self._validStrictCompare[i],
                self._strictValidator.parse(val, None, 'en_US.UTF-8'),
                f"(A) {text}"
            )
            self.assertTrue(
                self._strictValidator.isValid3(val, None, 'en_US.UTF-8'),
                f"(B) {text}"
            )
            self.assertEqual(
                self._validStrictCompare[i],
                self._strictValidator.parse(val, self._testPattern, None),
                f"(C) {text}"
            )
            self.assertTrue(
                self._strictValidator.isValid3(val, self._testPattern, None),
                f"(D) {text}"
            )

    
    @pytest.mark.test
    def testValidNotStrict(self) -> None:
        for i, val in enumerate(self._valid):
            text = f"idx=[{i}] value=[{self._validCompare[i]}]"
            self.assertEqual(
                self._validCompare[i], self._validator.parse(val, None, 'en_US.UTF-8'),
                f"(A) {text}"
            )
            self.assertTrue(
                self._validator.isValid3(val, None, 'en_US.UTF-8'),
                f"(B) {text}"
            )
            self.assertEqual(
                self._validCompare[i], self._validator.parse(val, self._testPattern, None),
                f"(C) {text}"
            )
            self.assertTrue(
                self._validator.isValid3(val, self._testPattern, None),
                f"(D) {text}"
            )

    
    @pytest.mark.test
    def testValidateLocale(self) -> None:
        self.assertEqual(
            self._testNumber,
            self._strictValidator.parse(self._testStringUS, None, 'en_US.UTF-8'),
            "US Locale, US Format"
        )
        self.assertIsNone(
            self._strictValidator.parse(self._testStringDE, None, 'en_US.UTF-8'),
            "US Locale, DE Format"
        )

        self.assertEqual(
            self._testNumber,
            self._strictValidator.parse(self._testStringDE, None, 'de_DE.UTF-8'),
            "DE Locale, DE Format"
        )
        self.assertIsNone(
            self._strictValidator.parse(self._testStringUS, None, 'de_DE.UTF-8'),
            "DE Locale, US Format"
        )

        self.assertEqual(
            self._testNumber,
            self._strictValidator.parse(self._testStringUS, None, None),
            "Default Locale, US Format"
        )
        self.assertIsNone(
            self._strictValidator.parse(self._testStringDE, None, None),
            "Default Locale, DE Format"
        )

    
    @pytest.mark.test
    def testFormat(self) -> None:
        number = Decimal("1234.5")
        self.assertEqual(
            "1,234.5",
            self._strictValidator.format2(number, 'en_US.UTF-8'),
            "US Locale, US Format"
        )
        self.assertEqual(
            "1.234,5",
            self._strictValidator.format2(number, 'de_DE.UTF-8'),
            "DE Locale, DE Format"
        )
        self.assertEqual(
            "12,34.50",
            self._strictValidator.format1(number, "#,#0.00"),
            "Pattern #,#0.00"
        )

    
    @pytest.mark.test
    def testRangeMinMax(self) -> None:
        number9 = 9
        number10 = 10
        number11 = 11
        number19 = 19
        number20 = 20
        number21 = 21

        self.assertFalse(
            self._strictValidator.isInRange(number9, number10, number20),
            "isInRange() < min"
        )
        self.assertTrue(
            self._strictValidator.isInRange(number10, number10, number20),
            "isInRange() = min"
        )
        self.assertTrue(
            self._strictValidator.isInRange(number11, number10, number20),
            "isInRange() in range"
        )
        self.assertTrue(
            self._strictValidator.isInRange(number20, number10, number20),
            "isInRange() = max"
        )
        self.assertFalse(
            self._strictValidator.isInRange(number21, number10, number20),
            "isInRange() > max"
        )

        self.assertFalse(
            self._strictValidator.minValue(number9, number10),
            "minValue() < min"
        )
        self.assertTrue(
            self._strictValidator.minValue(number10, number10),
            "minValue() = min"
        )
        self.assertTrue(
            self._strictValidator.minValue(number11, number10),
            "minValue() > min"
        )

        self.assertTrue(
            self._strictValidator.maxValue(number19, number20),
            "maxValue() < max"
        )
        self.assertTrue(
            self._strictValidator.maxValue(number20, number20),
            "maxValue() = max"
        )
        self.assertFalse(
            self._strictValidator.maxValue(number21, number20),
            "maxValue() > max"
        )

    
    @pytest.mark.test
    def testSerialization(self) -> None:
        baos = BytesIO()
        try:
            pickle.dump(self._validator, baos)
        except Exception as e:
            self.fail(f"{self._validator.__class__.__name__} error during serialization: {e}")

        result = None
        try:
            bais = BytesIO(baos.getvalue())
            result = pickle.load(bais)
        except Exception as e:
            self.fail(
                f"{self._validator.__class__.__name__} error during deserialization: {e}"
            )
        
        self.assertIsNotNone(result)
