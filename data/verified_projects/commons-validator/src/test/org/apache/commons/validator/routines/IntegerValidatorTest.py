import pytest

from src.main.org.apache.commons.validator.routines.IntegerValidator import *
from src.test.org.apache.commons.validator.routines.AbstractNumberValidatorTest import AbstractNumberValidatorTest
import sys


class FloatValidatorTest(AbstractNumberValidatorTest):

    __INT_MIN_VAL = -sys.maxsize - 1
    __INT_MAX_VAL = sys.maxsize
    __INT_MAX = str(sys.maxsize)
    __INT_MAX_0 = str(sys.maxsize) + ".99999999999999999999999"
    __INT_MAX_1 = str(sys.maxsize + 1)
    __INT_MIN = str(-sys.maxsize - 1)
    __INT_MIN_0 = str(-sys.maxsize - 1) + ".99999999999999999999999"
    __INT_MIN_1 = str(-sys.maxsize - 1 - 1)
    
    @classmethod
    def setUpClass(cls):
        pass

    
    def __init__(self, methodName='runTest') -> None:
        super().__init__(methodName)

    
    def setUp(self) -> None:
        try:
            super().setUp(
                validator = IntegerValidator(False, 0),
                strictValidator = IntegerValidator.IntegerValidator1(),
                testPattern = "#,###",
                _max = sys.maxsize,
                maxPlusOne = sys.maxsize + 1,
                _min = -sys.maxsize - 1,
                minMinusOne = -sys.maxsize - 1 - 1,
                invalidStrict = [
                    None,
                    "",
                    "X",
                    "X12",
                    "12X",
                    "1X2",
                    "1.2",
                    FloatValidatorTest.__INT_MAX_1,
                    FloatValidatorTest.__INT_MIN_1
                ],
                invalid = [
                    None,
                    "",
                    "X",
                    "X12",
                    FloatValidatorTest.__INT_MAX_1,
                    FloatValidatorTest.__INT_MIN_1
                ],
                testNumber = 1234,
                testZero = 0,
                validStrict = [
                    "0",
                    "1234",
                    "1,234",
                    FloatValidatorTest.__INT_MAX,
                    FloatValidatorTest.__INT_MIN
                ],
                validStrictCompare = [
                    0,
                    1234,
                    1234,
                    FloatValidatorTest.__INT_MAX_VAL,
                    FloatValidatorTest.__INT_MIN_VAL
                ],
                valid = [
                    "0",
                    "1234",
                    "1,234",
                    "1,234.5",
                    "1234X",
                    FloatValidatorTest.__INT_MAX,
                    FloatValidatorTest.__INT_MIN,
                    FloatValidatorTest.__INT_MAX_0,
                    FloatValidatorTest.__INT_MIN_0
                ],
                validCompare = [
                    0,
                    1234,
                    1234,
                    1234,
                    1234,
                    FloatValidatorTest.__INT_MAX_VAL,
                    FloatValidatorTest.__INT_MIN_VAL,
                    FloatValidatorTest.__INT_MAX_VAL,
                    FloatValidatorTest.__INT_MIN_VAL
                ],
                testStringUS = "1,234",
                testStringDE = "1.234",
                localeValue = "1.234",
                localePattern = "#.###",
                testLocale = 'de_DE.UTF-8',
                localeExpected = 1234
            )
        except Exception as e:
            self._fail(f"An exception occurred when setting up the test: {e}")
    

    @pytest.mark.test
    def testIntegerValidatorMethods(self) -> None:
        locale = 'de_DE.UTF-8'
        pattern = "0,00,00"
        patternVal = "1,23,45"
        germanPatternVal = "1.23.45"
        localeVal = "12.345"
        defaultVal = "12,345"
        XXXX = "XXXX"
        expected = 12345
        self.assertEqual(
            expected,
            IntegerValidator.getInstance().validate0(defaultVal),
            "validate(A) default"
        )
        self.assertEqual(
            expected,
            IntegerValidator.getInstance().validate2(localeVal, locale),
            "validate(A) locale"
        )
        self.assertEqual(
            expected,
            IntegerValidator.getInstance().validate1(patternVal, pattern),
            "validate(A) pattern"
        )
        self.assertEqual(
            expected,
            IntegerValidator.getInstance().validate3(germanPatternVal, pattern, 'de_DE.UTF-8'),
            "validate(A) both"
        )

        self.assertTrue(
            IntegerValidator.getInstance().isValid0(defaultVal),
            "isValid(A) default"
        )
        self.assertTrue(
            IntegerValidator.getInstance().isValid2(localeVal, locale),
            "isValid(A) locale"
        )
        self.assertTrue(
            IntegerValidator.getInstance().isValid1(patternVal, pattern),
            "isValid(A) pattern"
        )
        self.assertTrue(
            IntegerValidator.getInstance().isValid3(germanPatternVal, pattern, 'de_DE.UTF-8'),
            "isValid(A) both"
        )

        self.assertIsNone(
            IntegerValidator.getInstance().validate0(XXXX),
            "validate(B) default"
        )
        self.assertIsNone(
            IntegerValidator.getInstance().validate2(XXXX, locale),
            "validate(B) locale"
        )
        self.assertIsNone(
            IntegerValidator.getInstance().validate1(XXXX, pattern),
            "validate(B) pattern"
        )
        self.assertIsNone(
            IntegerValidator.getInstance().validate3(patternVal, pattern, 'de_DE.UTF-8'),
            "validate(B) both"
        )

        self.assertFalse(
            IntegerValidator.getInstance().isValid0(XXXX),
            "isValid(B) default"
        )
        self.assertFalse(
            IntegerValidator.getInstance().isValid2(XXXX, locale),
            "isValid(B) locale"
        )
        self.assertFalse(
            IntegerValidator.getInstance().isValid1(XXXX, pattern),
            "isValid(B) pattern"
        )
        self.assertFalse(
            IntegerValidator.getInstance().isValid3(patternVal, pattern, 'de_DE.UTF-8'),
            "isValid(B) both"
        )

    
    @pytest.mark.test
    def testIntegerRangeMinMax(self) -> None:
        validator = IntegerValidator(self._strictValidator)
        number9 = validator.validate1("9", "#")
        number10 = validator.validate1("10", "#")
        number11 = validator.validate1("11", "#")
        number19 = validator.validate1("19", "#")
        number20 = validator.validate1("20", "#")
        number21 = validator.validate1("21", "#")

        self.assertFalse(
            validator.isInRange1(number9, 10, 20),
            "isInRange() < min"
        )
        self.assertTrue(
            validator.isInRange1(number10, 10, 20),
            "isInRange() = min"
        )
        self.assertTrue(
            validator.isInRange1(number11, 10, 20),
            "isInRange() in range"
        )
        self.assertTrue(
            validator.isInRange1(number20, 10, 20),
            "isInRange() = max"
        )
        self.assertFalse(
            validator.isInRange1(number21, 10, 20),
            "isInRange() > max"
        )

        self.assertFalse(
            validator.minValue1(number9, 10),
            "minValue() < min"
        )
        self.assertTrue(
            validator.minValue1(number10, 10),
            "minValue() = min"
        )
        self.assertTrue(
            validator.minValue1(number11, 10),
            "minValue() > min"
        )

        self.assertTrue(
            validator.maxValue1(number19, 20),
            "maxValue() < max"
        )
        self.assertTrue(
            validator.maxValue1(number20, 20),
            "maxValue() = max"
        )
        self.assertFalse(
            validator.maxValue1(number21, 20),
            "maxValue() > max"
        )
    

    @pytest.mark.test
    def testMinMaxValues(self) -> None:
        self.assertTrue(
            self._validator.isValid0("2147483647"),
            "2147483647 is max integer"
        )
        self.assertFalse(
            self._validator.isValid0("2147483648"),
            "2147483648 > max integer"
        )
        self.assertTrue(
            self._validator.isValid0("-2147483648"),
            "-2147483648 is min integer"
        )
        self.assertFalse(
            self._validator.isValid0("-2147483649"),
            "-2147483649 < min integer"
        )
