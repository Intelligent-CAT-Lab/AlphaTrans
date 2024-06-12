from src.main.org.apache.commons.validator.routines.ShortValidator import *
from src.test.org.apache.commons.validator.routines.AbstractNumberValidatorTest import AbstractNumberValidatorTest
import sys


class ShortValidatorTest(AbstractNumberValidatorTest):

    @classmethod
    def setUpClass(cls):
        pass

    
    def __init__(self, methodName='runTest') -> None:
        super().__init__(methodName)

    
    def setUp(self) -> None:
        try:
            super().setUp(
                validator = ShortValidator(False, 0),
                strictValidator = ShortValidator.ShortValidator1(),
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
                    "1.2"
                ],
                invalid = [None, "", "X", "X12"],
                testNumber = 1234,
                testZero = 0,
                validStrict = [
                    "0",
                    "1234",
                    "1,234"
                ],
                validStrictCompare = [
                    0, 
                    1234,
                    1234
                ],
                valid = [
                    "0",
                    "1234",
                    "1,234",
                    "1,234.5",
                    "1234X"
                ],
                validCompare = [
                    0,
                    1234,
                    1234,
                    1234,
                    1234
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
    

    def test_ShortValidatorMethods(self) -> None:
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
            ShortValidator.getInstance().validate0(defaultVal), 
            "validate(A) default"
        )
        self.assertEqual(
            expected, 
            ShortValidator.getInstance().validate2(localeVal, locale), 
            "validate(A) locale "
        )
        self.assertEqual(
            expected, 
            ShortValidator.getInstance().validate1(patternVal, pattern), 
            "validate(A) pattern"
        )
        self.assertEqual(
            expected, 
            ShortValidator.getInstance().validate3(germanPatternVal, pattern, 'de_DE.UTF-8'), 
            "validate(A) both"
        )

        self.assertTrue(
            ShortValidator.getInstance().isValid0(defaultVal), 
            "isValid(A) default"
        )
        self.assertTrue(
            ShortValidator.getInstance().isValid2(localeVal, locale), 
            "isValid(A) locale "
        )
        self.assertTrue(
            ShortValidator.getInstance().isValid1(patternVal, pattern), 
            "isValid(A) pattern"
        )
        self.assertTrue(
            ShortValidator.getInstance().isValid3(germanPatternVal, pattern, 'de_DE.UTF-8'), 
            "isValid(A) both"
        )

        self.assertIsNone(
            ShortValidator.getInstance().validate0(XXXX), 
            "validate(B) default"
        )
        self.assertIsNone(
            ShortValidator.getInstance().validate2(XXXX, locale), 
            "validate(B) locale "
        )
        self.assertIsNone(
            ShortValidator.getInstance().validate1(XXXX, pattern), 
            "validate(B) pattern"
        )
        self.assertIsNone(
            ShortValidator.getInstance().validate3(patternVal, pattern, 'de_DE.UTF-8'), 
            "validate(B) both"
        )

        self.assertFalse(
            ShortValidator.getInstance().isValid0(XXXX), 
            "isValid(B) default"
        )
        self.assertFalse(
            ShortValidator.getInstance().isValid2(XXXX, locale), 
            "isValid(B) locale "
        )
        self.assertFalse(
            ShortValidator.getInstance().isValid1(XXXX, pattern), 
            "isValid(B) pattern"
        )
        self.assertFalse(
            ShortValidator.getInstance().isValid3(patternVal, pattern, 'de_DE.UTF-8'), 
            "isValid(B) both"
        )
    

    def testShortRangeMinMax(self) -> None:
        validator = ShortValidator(self._strictValidator)
        number9 = validator.validate1("9", "#")
        number10 = validator.validate1("10", "#")
        number11 = validator.validate1("11", "#")
        number19 = validator.validate1("19", "#")
        number20 = validator.validate1("20", "#")
        number21 = validator.validate1("21", "#")
        min_ = 10
        max_ = 20

        self.assertFalse(
            validator.isInRange1(number9, min_, max_), 
            "isInRange() < min"
        )
        self.assertTrue(
            validator.isInRange1(number10, min_, max_), 
            "isInRange() = min"
        )
        self.assertTrue(
            validator.isInRange1(number11, min_, max_), 
            "isInRange() in range"
        )
        self.assertTrue(
            validator.isInRange1(number20, min_, max_), 
            "isInRange() = max"
        )
        self.assertFalse(
            validator.isInRange1(number21, min_, max_), 
            "isInRange() > max"
        )

        self.assertFalse(
            validator.minValue1(number9, min_), 
            "minValue() < min"
        )
        self.assertTrue(
            validator.minValue1(number10, min_), 
            "minValue() = min"
        )
        self.assertTrue(
            validator.minValue1(number11, min_), 
            "minValue() > min"
        )

        self.assertTrue(
            validator.maxValue1(number19, max_), 
            "maxValue() < max"
        )
        self.assertTrue(
            validator.maxValue1(number20, max_), 
            "maxValue() = max"
        )
        self.assertFalse(
            validator.maxValue1(number21, max_), 
            "maxValue() > max"
        )
