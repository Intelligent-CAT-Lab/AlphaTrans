import pytest

from src.main.org.apache.commons.validator.routines.ByteValidator import *
from src.test.org.apache.commons.validator.routines.AbstractNumberValidatorTest import AbstractNumberValidatorTest
from decimal import Decimal

class ByteValidatorTest(AbstractNumberValidatorTest):

    __BYTE_MIN_VAL = -128
    __BYTE_MAX_VAL = 127
    __BYTE_MAX = "127"
    __BYTE_MAX_0 = "127.99999999999999999999999"  # force double rounding
    __BYTE_MAX_1 = "128"
    __BYTE_MIN = "-128"
    __BYTE_MIN_0 = "-128.99999999999999999999999"  # force double rounding
    __BYTE_MIN_1 = "-129"
    
    __test__ = True

    
    def setUp(self) -> None:
        try:
            super().setUp()
            self._validator = ByteValidator(False, 0)
            self._strictValidator = ByteValidator.ByteValidator1()
            self._testPattern = "#,###"
            self._max = ByteValidatorTest.__BYTE_MAX_VAL
            self._maxPlusOne = ByteValidatorTest.__BYTE_MAX_VAL + 1
            self._min = ByteValidatorTest.__BYTE_MIN_VAL
            self._minMinusOne = ByteValidatorTest.__BYTE_MIN_VAL - 1
            self._invalidStrict = [
                None,
                "",
                "X",
                "X12",
                "12X",
                "1X2",
                "1.2",
                ByteValidatorTest.__BYTE_MAX_1,
                ByteValidatorTest.__BYTE_MIN_1,
                ByteValidatorTest.__BYTE_MAX_0,
                ByteValidatorTest.__BYTE_MIN_0
            ]
            self._invalid = [
                None,
                "",
                "X",
                "X12",
                ByteValidatorTest.__BYTE_MAX_1,
                ByteValidatorTest.__BYTE_MIN_1
            ]
            self._testNumber = Decimal("123")
            self._testZero = Decimal("0")
            self._validStrict = [
                "0",
                "123",
                ",123",
                ByteValidatorTest.__BYTE_MAX,
                ByteValidatorTest.__BYTE_MIN
            ]
            self._validStrictCompare = [
                Decimal("0"),
                Decimal("123"),
                Decimal("123"),
                ByteValidatorTest.__BYTE_MAX_VAL,
                ByteValidatorTest.__BYTE_MIN_VAL
            ]
            self._valid = [
                "0",
                "123",
                ",123",
                ",123.5",
                "123X",
                ByteValidatorTest.__BYTE_MAX,
                ByteValidatorTest.__BYTE_MIN,
                ByteValidatorTest.__BYTE_MAX_0,
                ByteValidatorTest.__BYTE_MIN_0
            ]
            self._validCompare = [
                Decimal("0"),
                Decimal("123"),
                Decimal("123"),
                Decimal("123"),
                Decimal("123"),
                ByteValidatorTest.__BYTE_MAX_VAL,
                ByteValidatorTest.__BYTE_MIN_VAL,
                ByteValidatorTest.__BYTE_MAX_VAL,
                ByteValidatorTest.__BYTE_MIN_VAL
            ]
            self._testStringUS = ",123"
            self._testStringDE = ".123"
            self._localeValue = ".123"
            self._localePattern = "#.###"
            self._testLocale = 'de_DE.UTF-8'
            self._localeExpected = Decimal("123")
        except Exception as e:
            self.fail(f"An exception occurred when setting up the test: {e}")
    

    @pytest.mark.test
    def testByteValidatorMethods(self) -> None:
        locale = 'de_DE.UTF-8'
        pattern = "0,00"
        patternVal = "1,23"
        germanPatternVal = "1.23"
        localeVal = ".123"
        defaultVal = ",123"
        XXXX = "XXXX"
        expected = 123

        self.assertEqual(
            expected,
            ByteValidator.getInstance().validate0(defaultVal),
            "validate(A) default"
        )
        self.assertEqual(
            expected,
            ByteValidator.getInstance().validate2(localeVal, locale),
            "validate(A) locale "
        )
        self.assertEqual(
            expected,
            ByteValidator.getInstance().validate1(patternVal, pattern),
            "validate(A) pattern"    
        )
        self.assertEqual(
            expected,
            ByteValidator.getInstance()\
                .validate3(germanPatternVal, pattern, 'de_DE.UTF-8'),
            "validate(A) both"    
        )

        self.assertTrue(
            ByteValidator.getInstance().isValid0(defaultVal),
            "isValid(A) default"    
        )
        self.assertTrue(
            ByteValidator.getInstance().isValid2(localeVal, locale),
            "isValid(A) locale "
        )
        self.assertTrue(
            ByteValidator.getInstance().isValid1(patternVal, pattern),
            "isValid(A) pattern"    
        )
        self.assertTrue(
            ByteValidator.getInstance()\
                .isValid3(germanPatternVal, pattern, 'de_DE.UTF-8'),
            "isValid(A) both"
        )

        self.assertIsNone(
            ByteValidator.getInstance().validate0(XXXX),
            "validate(B) default"
        )
        self.assertIsNone(
            ByteValidator.getInstance().validate2(XXXX, locale),
            "validate(B) locale "    
        )
        self.assertIsNone(
            ByteValidator.getInstance().validate1(XXXX, pattern),
            "validate(B) pattern"
        )
        self.assertIsNone(
            ByteValidator.getInstance()\
                .validate3(patternVal, pattern, 'de_DE.UTF-8'),
            "validate(B) both"
        )

        self.assertFalse(
            ByteValidator.getInstance().isValid0(XXXX),
            "isValid(B) default"
        )
        self.assertFalse(
            ByteValidator.getInstance().isValid2(XXXX, locale),
            "isValid(B) locale "    
        )
        self.assertFalse(
            ByteValidator.getInstance().isValid1(XXXX, pattern),
            "isValid(B) pattern"    
        )
        self.assertFalse(
            ByteValidator.getInstance()\
                .isValid3(patternVal, pattern, 'de_DE.UTF-8'),
            "isValid(B) both"
        )
    

    @pytest.mark.test
    def testByteRangeMinMax(self) -> None:
        validator = self._strictValidator
        number9 = validator.validate1("9", "#")
        number10 = validator.validate1("10", "#")
        number11 = validator.validate1("11", "#")
        number19 = validator.validate1("19", "#")
        number20 = validator.validate1("20", "#")
        number21 = validator.validate1("21", "#")
        minVal = 10
        maxVal = 20

        self.assertFalse(
            validator.isInRange1(number9, minVal, maxVal),
            "isInRange() < min"   
        )
        self.assertTrue(
            validator.isInRange1(number10, minVal, maxVal),
            "isInRange() = min"
        )
        self.assertTrue(
            validator.isInRange1(number11, minVal, maxVal),
            "isInRange() in range"
        )
        self.assertTrue(
            validator.isInRange1(number20, minVal, maxVal),
            "isInRange() = max"
        )
        self.assertFalse(
            validator.isInRange1(number21, minVal, maxVal),
            "isInRange() > max"
        )

        self.assertFalse(
            validator.minValue1(number9, minVal),
            "minValue() < min"
        )
        self.assertTrue(
            validator.minValue1(number10, minVal),
            "minValue() = min"
        )
        self.assertTrue(
            validator.minValue1(number11, minVal),
            "minValue() > min"
        )

        self.assertTrue(
            validator.maxValue1(number19, maxVal),
            "maxValue() < max"
        )
        self.assertTrue(
            validator.maxValue1(number20, maxVal),
            "maxValue() = max"
        )
        self.assertFalse(
            validator.maxValue1(number21, maxVal),
            "maxValue() > max"
        )
