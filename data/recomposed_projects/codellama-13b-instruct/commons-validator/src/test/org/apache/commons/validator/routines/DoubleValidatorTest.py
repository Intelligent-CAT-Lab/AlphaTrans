# Imports Begin
from src.main.org.apache.commons.validator.routines.DoubleValidator import *
from src.main.org.apache.commons.validator.routines.AbstractNumberValidatorTest import *
from src.main.org.apache.commons.validator.routines.AbstractNumberValidator import *
import unittest
import numbers

# Imports End


class DoubleValidatorTest(unittest.TestCase, AbstractNumberValidatorTest):

    # Class Fields Begin
    # Class Fields End

    # Class Methods Begin
    def _setUp(self) -> None:

        pass  # LLM could not translate method body

    def testDoubleRangeMinMax(self) -> None:

        pass  # LLM could not translate method body

    def testDoubleValidatorMethods(self) -> None:

        locale = Locale.GERMAN
        pattern = "0,00,00"
        pattern_val = "1,23,45"
        german_pattern_val = "1.23.45"
        locale_val = "12.345"
        default_val = "12,345"
        XXXX = "XXXX"
        expected = Double.valueOf(12345)
        self.assertEqual(
            "validate(A) default",
            expected,
            DoubleValidator.getInstance().validate0(default_val),
        )
        self.assertEqual(
            "validate(A) locale ",
            expected,
            DoubleValidator.getInstance().validate2(locale_val, locale),
        )
        self.assertEqual(
            "validate(A) pattern",
            expected,
            DoubleValidator.getInstance().validate1(pattern_val, pattern),
        )
        self.assertEqual(
            "validate(A) both",
            expected,
            DoubleValidator.getInstance().validate3(
                german_pattern_val, pattern, Locale.GERMAN
            ),
        )
        self.assertTrue(
            "isValid(A) default", DoubleValidator.getInstance().isValid0(default_val)
        )
        self.assertTrue(
            "isValid(A) locale ",
            DoubleValidator.getInstance().isValid2(locale_val, locale),
        )
        self.assertTrue(
            "isValid(A) pattern",
            DoubleValidator.getInstance().isValid1(pattern_val, pattern),
        )
        self.assertTrue(
            "isValid(A) both",
            DoubleValidator.getInstance().isValid3(
                german_pattern_val, pattern, Locale.GERMAN
            ),
        )
        assertNull("validate(B) default", DoubleValidator.getInstance().validate0(XXXX))
        assertNull(
            "validate(B) locale ", DoubleValidator.getInstance().validate2(XXXX, locale)
        )
        assertNull(
            "validate(B) pattern",
            DoubleValidator.getInstance().validate1(XXXX, pattern),
        )
        assertNull(
            "validate(B) both",
            DoubleValidator.getInstance().validate3(
                pattern_val, pattern, Locale.GERMAN
            ),
        )
        self.assertFalse(
            "isValid(B) default", DoubleValidator.getInstance().isValid0(XXXX)
        )
        self.assertFalse(
            "isValid(B) locale ", DoubleValidator.getInstance().isValid2(XXXX, locale)
        )
        self.assertFalse(
            "isValid(B) pattern", DoubleValidator.getInstance().isValid1(XXXX, pattern)
        )
        self.assertFalse(
            "isValid(B) both",
            DoubleValidator.getInstance().isValid3(pattern_val, pattern, Locale.GERMAN),
        )

    def __init__(self, name: str) -> None:

        super().__init__(name)

    # Class Methods End
