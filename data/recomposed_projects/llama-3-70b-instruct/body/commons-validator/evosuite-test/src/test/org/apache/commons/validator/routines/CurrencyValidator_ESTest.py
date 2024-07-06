from __future__ import annotations
import math
import time
import locale
import re
import os
import decimal
import numbers
import unittest
import pytest
import io
import unittest
from src.main.org.apache.commons.validator.routines.BigDecimalValidator import *
from src.main.org.apache.commons.validator.routines.CurrencyValidator import *

# from src.test.org.apache.commons.validator.routines.CurrencyValidator_ESTest_scaffolding import *
# from src.main.org.evosuite.runtime.EvoAssertions import *
# from src.main.org.evosuite.runtime.EvoRunnerParameters import *


class CurrencyValidator_ESTest(unittest.TestCase):

    def test7(self) -> None:

        currencyValidator0 = CurrencyValidator.CurrencyValidator1()
        numberFormat0 = NumberFormat.getIntegerInstance()

        with pytest.raises(RuntimeError) as e:
            currencyValidator0.parse(None, numberFormat0)

        assert str(e.value) == "Expecting exception: RuntimeError"
        verifyException("java.text.DecimalFormat", e.value)

    def test6(self) -> None:

        currencyValidator0 = CurrencyValidator.getInstance()
        locale0 = Locale.SIMPLIFIED_CHINESE
        decimalFormat0 = NumberFormat.getIntegerInstance(locale0)
        bigDecimal0 = currencyValidator0.parse("1", decimalFormat0)
        self.assertEqual(1, bigDecimal0.shortValue())

    def test5(self) -> None:

        bigDecimalValidator0 = CurrencyValidator.getInstance()
        bigDecimal0 = bigDecimalValidator0.validate1(
            "org.apache.commons.validator.routines.AbstractFormatValidator",
            "V<6&amp;V:T6v_pX]BTv@",
        )
        self.assertIsNone(bigDecimal0)

    def test4(self) -> None:

        currencyValidator0 = CurrencyValidator.getInstance()
        simpleDateFormat0 = MockDateFormat.getTimeInstance(0)
        object0 = currencyValidator0.parse("yY+YG#PF8*Bv", simpleDateFormat0)
        self.assertIsNone(object0)

    def test3(self) -> None:

        currencyValidator0 = CurrencyValidator.getInstance()
        locale0 = Locale.SIMPLIFIED_CHINESE
        decimalFormat0 = currencyValidator0.getFormat(None, locale0)
        currencyValidator0.parse("", decimalFormat0)
        self.assertEqual("#,##0.00", decimalFormat0.toPattern())
        self.assertEqual("-", decimalFormat0.getNegativePrefix())

    def test2(self) -> None:
        currencyValidator0 = CurrencyValidator(False, True)

    def test1(self) -> None:

        currencyValidator0 = CurrencyValidator.CurrencyValidator1()
        messageFormat0 = MessageFormat("3CHw9")

        with pytest.raises(ValueError):
            currencyValidator0.parse("3CHw9", messageFormat0)
            pytest.fail("Expecting exception: ValueError")

        verifyException("java.math.BigDecimal", e)

    def test0(self) -> None:

        currencyValidator0 = CurrencyValidator.CurrencyValidator1()
        locale0 = Locale.GERMAN
        currencyValidator0.validate3('UBw 5"oCwhV8K3-JW\b', None, locale0)
