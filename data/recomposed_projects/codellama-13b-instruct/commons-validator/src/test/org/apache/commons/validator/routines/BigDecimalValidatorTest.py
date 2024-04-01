# Imports Begin
from src.main.org.apache.commons.validator.routines.BigDecimalValidator import *
from src.main.org.apache.commons.validator.routines.AbstractNumberValidatorTest import *
from src.main.org.apache.commons.validator.routines.AbstractNumberValidator import *
import unittest
import numbers

# Imports End


class BigDecimalValidatorTest(unittest.TestCase, AbstractNumberValidatorTest):

    # Class Fields Begin
    # Class Fields End

    # Class Methods Begin
    def _setUp(self) -> None:

        pass  # LLM could not translate method body

    def testBigDecimalRangeMinMax(self) -> None:

        validator = BigDecimalValidator(
            True, AbstractNumberValidator.STANDARD_FORMAT, True
        )
        number9 = BigDecimal("9")
        number10 = BigDecimal("10")
        number11 = BigDecimal("11")
        number19 = BigDecimal("19")
        number20 = BigDecimal("20")
        number21 = BigDecimal("21")
        min = 10
        max = 20
        self.assertFalse("isInRange(A) < min", validator.isInRange(number9, min, max))
        self.assertTrue("isInRange(A) = min", validator.isInRange(number10, min, max))
        self.assertTrue(
            "isInRange(A) in range", validator.isInRange(number11, min, max)
        )
        self.assertTrue("isInRange(A) = max", validator.isInRange(number20, min, max))
        self.assertFalse("isInRange(A) > max", validator.isInRange(number21, min, max))
        self.assertFalse("minValue(A) < min", validator.minValue(number9, min))
        self.assertTrue("minValue(A) = min", validator.minValue(number10, min))
        self.assertTrue("minValue(A) > min", validator.minValue(number11, min))
        self.assertTrue("maxValue(A) < max", validator.maxValue(number19, max))
        self.assertTrue("maxValue(A) = max", validator.maxValue(number20, max))
        self.assertFalse("maxValue(A) > max", validator.maxValue(number21, max))

    def testBigDecimalValidatorMethods(self) -> None:

        locale = Locale.GERMAN
        pattern = "0,00,00"
        pattern_val = "1,23,45"
        german_pattern_val = "1.23.45"
        locale_val = "12.345"
        default_val = "12,345"
        XXXX = "XXXX"
        expected = decimal.Decimal(12345)
        assert expected == BigDecimalValidator.getInstance().validate0(default_val)
        assert expected == BigDecimalValidator.getInstance().validate2(
            locale_val, locale
        )
        assert expected == BigDecimalValidator.getInstance().validate1(
            pattern_val, pattern
        )
        assert expected == BigDecimalValidator.getInstance().validate3(
            german_pattern_val, pattern, Locale.GERMAN
        )
        assert True == BigDecimalValidator.getInstance().isValid0(default_val)
        assert True == BigDecimalValidator.getInstance().isValid2(locale_val, locale)
        assert True == BigDecimalValidator.getInstance().isValid1(pattern_val, pattern)
        assert True == BigDecimalValidator.getInstance().isValid3(
            german_pattern_val, pattern, Locale.GERMAN
        )
        assert None == BigDecimalValidator.getInstance().validate0(XXXX)
        assert None == BigDecimalValidator.getInstance().validate2(XXXX, locale)
        assert None == BigDecimalValidator.getInstance().validate1(XXXX, pattern)
        assert None == BigDecimalValidator.getInstance().validate3(
            pattern_val, pattern, Locale.GERMAN
        )
        assert False == BigDecimalValidator.getInstance().isValid0(XXXX)
        assert False == BigDecimalValidator.getInstance().isValid2(XXXX, locale)
        assert False == BigDecimalValidator.getInstance().isValid1(XXXX, pattern)
        assert False == BigDecimalValidator.getInstance().isValid3(
            pattern_val, pattern, Locale.GERMAN
        )

    def __init__(self, name: str) -> None:

        super().__init__(name)

    # Class Methods End
