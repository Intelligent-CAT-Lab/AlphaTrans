import pytest

from src.main.org.apache.commons.validator.routines.CurrencyValidator import *
from src.main.org.apache.commons.validator.routines.BigDecimalValidator import *
from src.main.org.apache.commons.validator.routines.AbstractNumberValidator import *
from locale import getlocale, setlocale, LC_MONETARY, currency
from decimal import Decimal
import unittest
from typing import *


class CurrencyValidatorTest(unittest.TestCase):

    __CURRENCY_SYMBOL = '\u00A4'

    __US_DOLLAR = None
    __UK_POUND = None

    
    def setUp(self) -> None:
        try:
            super().setUp()
            origDefault = getlocale(LC_MONETARY)
            setlocale(LC_MONETARY, 'en_US.UTF-8')
            self.__US_DOLLAR = currency(0, symbol=True, grouping=False)[0]
            setlocale(LC_MONETARY, 'en_GB.UTF-8')
            self.__UK_POUND = currency(0, symbol=True, grouping=False)[0]
            setlocale(LC_MONETARY, origDefault)
        except Exception as e:
            self.fail(f"An exception occurred when setting up the test: {e}")

    
    def tearDown(self) -> None:
        try:
            super().tearDown()
        except Exception as e:
            self.fail(f"An exception occurred when cleaning up the test: {e}")

    
    @pytest.mark.test
    def testFormatType(self) -> None:
        self.assertEqual(
            1,
            CurrencyValidator.getInstance().getFormatType(),
            "Format Type A"
        )
        self.assertEqual(
            AbstractNumberValidator.CURRENCY_FORMAT,
            CurrencyValidator.getInstance().getFormatType(),
            "Format Type B"
        )

    
    @pytest.mark.test
    def testValid(self) -> None:
        origDefault = getlocale(LC_MONETARY)
        setlocale(LC_MONETARY, 'en_GB.UTF-8')

        validator = CurrencyValidator.getInstance()
        expected = Decimal("1234.56")
        negative = Decimal("-1234.56")
        noDecimal = Decimal("1234.00")
        oneDecimal = Decimal("1234.50")

        self.assertEqual(
            expected,
            validator.validate0(self.__UK_POUND + "1,234.56"),
            "Default locale"
        )

        self.assertEqual(
            expected,
            validator.validate2(self.__UK_POUND + "1,234.56", 'en_GB.UTF-8'),
            "UK locale"
        )
        self.assertEqual(
            negative,
            validator.validate2("-" + self.__UK_POUND + "1,234.56", 'en_GB.UTF-8'),
            "UK negative"
        )
        self.assertEqual(
            noDecimal,
            validator.validate2(self.__UK_POUND + "1,234", 'en_GB.UTF-8'),
            "UK no decimal"
        )
        self.assertEqual(
            oneDecimal,
            validator.validate2(self.__UK_POUND + "1,234.5", 'en_GB.UTF-8'),
            "UK 1 decimal"
        )
        self.assertEqual(
            expected,
            validator.validate2(self.__UK_POUND + "1,234.567", 'en_GB.UTF-8'),
            "UK 3 decimal"
        )
        self.assertEqual(
            expected,
            validator.validate2("1,234.56", 'en_GB.UTF-8'),
            "UK no symbol"
        )

        self.assertEqual(
            expected,
            validator.validate2(self.__US_DOLLAR + "1,234.56", 'en_US.UTF-8'),
            "US locale"
        )
        self.assertEqual(
            negative,
            validator.validate2("(" + self.__US_DOLLAR + "1,234.56)", 'en_US.UTF-8'),
            "US negative"
        )
        self.assertEqual(
            noDecimal,
            validator.validate2(self.__US_DOLLAR + "1,234", 'en_US.UTF-8'),
            "US no decimal"
        )
        self.assertEqual(
            oneDecimal,
            validator.validate2(self.__US_DOLLAR + "1,234.5", 'en_US.UTF-8'),
            "US 1 decimal"
        )
        self.assertEqual(
            expected,
            validator.validate2(self.__US_DOLLAR + "1,234.567", 'en_US.UTF-8'),
            "US 3 decimal"
        )
        self.assertEqual(
            expected,
            validator.validate2("1,234.56", 'en_US.UTF-8'),
            "US no symbol"
        )

        setlocale(LC_MONETARY, origDefault)

    
    @pytest.mark.test
    def testInvalid(self) -> None:
        validator = CurrencyValidator.getInstance()

        self.assertFalse(validator.isValid0(None), "isValid() Null Value")
        self.assertFalse(validator.isValid0(""), "isValid() Empty Value")
        self.assertIsNone(validator.validate0(None), "validate() Null Value")
        self.assertIsNone(validator.validate0(""), "validate() Empty Value")

        self.assertFalse(
            validator.isValid2(self.__US_DOLLAR + "1,234.56", 'en_GB.UTF-8'),
            "UK wrong symbol"
        )
        self.assertFalse(
            validator.isValid2("(" + self.__UK_POUND + "1,234.56)", 'en_GB.UTF-8'),
            "UK wrong negative"
        )

        self.assertFalse(
            validator.isValid2(self.__UK_POUND + "1,234.56", 'en_US.UTF-8'),
            "US wrong symbol"
        )
        self.assertFalse(
            validator.isValid2("-" + self.__US_DOLLAR + "1,234.56", 'en_US.UTF-8'),
            "US wrong negative"
        )

    
    @pytest.mark.test
    def testIntegerValid(self) -> None:
        origDefault = getlocale(LC_MONETARY)
        setlocale(LC_MONETARY, 'en_GB.UTF-8')

        validator = CurrencyValidator.CurrencyValidator1()
        expected = Decimal("1234.00")
        negative = Decimal("-1234.00")

        self.assertEqual(
            expected,
            validator.validate0(self.__UK_POUND + "1,234"),
            "Default locale"
        )

        self.assertEqual(
            expected,
            validator.validate2(self.__UK_POUND + "1,234", 'en_GB.UTF-8'),
            "UK locale"
        )
        self.assertEqual(
            negative,
            validator.validate2("-" + self.__UK_POUND + "1,234", 'en_GB.UTF-8'),
            "UK negative"
        )

        self.assertEqual(
            expected,
            validator.validate2(self.__US_DOLLAR + "1,234", 'en_US.UTF-8'),
            "US locale"
        )
        self.assertEqual(
            negative,
            validator.validate2("(" + self.__US_DOLLAR + "1,234)", 'en_US.UTF-8'),
            "US negative"
        )

        setlocale(LC_MONETARY, origDefault)

    
    @pytest.mark.test
    def testIntegerInvalid(self) -> None:
        validator = CurrencyValidator(True, False)

        self.assertFalse(
            validator.isValid2(self.__UK_POUND + "1,234.56", 'en_GB.UTF-8'),
            "UK positive"
        )
        self.assertFalse(
            validator.isValid2("-" + self.__UK_POUND + "1,234.56", 'en_GB.UTF-8'),
            "UK negative"
        )

        self.assertFalse(
            validator.isValid2(self.__US_DOLLAR + "1,234.56", 'en_US.UTF-8'),
            "US positive"
        )
        self.assertFalse(
            validator.isValid2("(" + self.__US_DOLLAR + "1,234.56)", 'en_US.UTF-8'),
            "US negative"
        )

    
    @pytest.mark.test
    def testPattern(self) -> None:
        origDefault = getlocale(LC_MONETARY)
        setlocale(LC_MONETARY, 'en_GB.UTF-8')

        validator = CurrencyValidator.getInstance()
        basicPattern = CurrencyValidatorTest.__CURRENCY_SYMBOL + "#,##0.000"
        pattern = basicPattern + ";[" + basicPattern + "]"
        expected = Decimal("1234.567")
        negative = Decimal("-1234.567")

        self.assertEqual(
            expected,
            validator.validate1(self.__UK_POUND + "1,234.567", pattern),
            "default"
        )
        self.assertEqual(
            negative,
            validator.validate1("[" + self.__UK_POUND + "1,234.567]", pattern),
            "negative"
        )
        self.assertEqual(
            expected,
            validator.validate1("1,234.567", pattern),
            "no symbol +ve"
        )
        self.assertEqual(
            negative,
            validator.validate1("[1,234.567]", pattern),
            "no symbol -ve"
        )

        self.assertEqual(
            expected,
            validator.validate3(self.__US_DOLLAR + "1,234.567", pattern, 'en_US.UTF-8'),
            "default"
        )
        self.assertEqual(
            negative,
            validator.validate3("[" + self.__US_DOLLAR + "1,234.567]", pattern, 'en_US.UTF-8'),
            "negative"
        )
        self.assertEqual(
            expected,
            validator.validate3("1,234.567", pattern, 'en_US.UTF-8'),
            "no symbol +ve"
        )
        self.assertEqual(
            negative,
            validator.validate3("[1,234.567]", pattern, 'en_US.UTF-8'),
            "no symbol -ve"
        )

        self.assertFalse(
            validator.isValid1(self.__US_DOLLAR + "1,234.567", pattern),
            "invalid symbol"
        )
        self.assertFalse(
            validator.isValid3(self.__UK_POUND + "1,234.567", pattern, 'en_US.UTF-8'),
            "invalid symbol"
        )

        setlocale(LC_MONETARY, origDefault)
