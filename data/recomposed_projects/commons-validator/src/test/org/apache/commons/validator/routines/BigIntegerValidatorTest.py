# Imports Begin
from src.main.org.apache.commons.validator.routines.BigIntegerValidator import *
from src.main.org.apache.commons.validator.routines.AbstractNumberValidatorTest import *
from src.main.org.apache.commons.validator.routines.AbstractNumberValidator import *
import unittest
import numbers

# Imports End


class BigIntegerValidatorTest(unittest.TestCase, AbstractNumberValidatorTest):

    # Class Fields Begin
    # Class Fields End

    # Class Methods Begin
    def _setUp(self) -> None:

        pass  # LLM could not translate method body

    def testBigIntegerRangeMinMax(self) -> None:

        validator = self.strictValidator
        number9 = validator.validate1("9", "#")
        number10 = validator.validate1("10", "#")
        number11 = validator.validate1("11", "#")
        number19 = validator.validate1("19", "#")
        number20 = validator.validate1("20", "#")
        number21 = validator.validate1("21", "#")
        assert not validator.isInRange(number9, 10, 20)
        assert validator.isInRange(number10, 10, 20)
        assert validator.isInRange(number11, 10, 20)
        assert validator.isInRange(number20, 10, 20)
        assert not validator.isInRange(number21, 10, 20)
        assert not validator.minValue(number9, 10)
        assert validator.minValue(number10, 10)
        assert validator.minValue(number11, 10)
        assert validator.maxValue(number19, 20)
        assert validator.maxValue(number20, 20)
        assert not validator.maxValue(number21, 20)

    def testBigIntegerValidatorMethods(self) -> None:

        locale = Locale.GERMAN
        pattern = "0,00,00"
        pattern_val = "1,23,45"
        german_pattern_val = "1.23.45"
        locale_val = "12.345"
        default_val = "12,345"
        XXXX = "XXXX"
        expected = BigInteger("12345")
        self.assertEqual(
            "validate(A) default",
            expected,
            BigIntegerValidator.getInstance().validate0(default_val),
        )
        self.assertEqual(
            "validate(A) locale ",
            expected,
            BigIntegerValidator.getInstance().validate2(locale_val, locale),
        )
        self.assertEqual(
            "validate(A) pattern",
            expected,
            BigIntegerValidator.getInstance().validate1(pattern_val, pattern),
        )
        self.assertEqual(
            "validate(A) both",
            expected,
            BigIntegerValidator.getInstance().validate3(
                german_pattern_val, pattern, Locale.GERMAN
            ),
        )
        self.assertTrue(
            "isValid(A) default",
            BigIntegerValidator.getInstance().isValid0(default_val),
        )
        self.assertTrue(
            "isValid(A) locale ",
            BigIntegerValidator.getInstance().isValid2(locale_val, locale),
        )
        self.assertTrue(
            "isValid(A) pattern",
            BigIntegerValidator.getInstance().isValid1(pattern_val, pattern),
        )
        self.assertTrue(
            "isValid(A) both",
            BigIntegerValidator.getInstance().isValid3(
                german_pattern_val, pattern, Locale.GERMAN
            ),
        )
        assertNull(
            "validate(B) default", BigIntegerValidator.getInstance().validate0(XXXX)
        )
        assertNull(
            "validate(B) locale ",
            BigIntegerValidator.getInstance().validate2(XXXX, locale),
        )
        assertNull(
            "validate(B) pattern",
            BigIntegerValidator.getInstance().validate1(XXXX, pattern),
        )
        assertNull(
            "validate(B) both",
            BigIntegerValidator.getInstance().validate3(
                pattern_val, pattern, Locale.GERMAN
            ),
        )
        self.assertFalse(
            "isValid(B) default", BigIntegerValidator.getInstance().isValid0(XXXX)
        )
        self.assertFalse(
            "isValid(B) locale ",
            BigIntegerValidator.getInstance().isValid2(XXXX, locale),
        )
        self.assertFalse(
            "isValid(B) pattern",
            BigIntegerValidator.getInstance().isValid1(XXXX, pattern),
        )
        self.assertFalse(
            "isValid(B) both",
            BigIntegerValidator.getInstance().isValid3(
                pattern_val, pattern, Locale.GERMAN
            ),
        )

    def __init__(self, name: str) -> None:

        super().__init__(name)

    # Class Methods End
