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
from src.main.org.apache.commons.validator.routines.PercentValidator import *

# from src.test.org.apache.commons.validator.routines.PercentValidator_ESTest_scaffolding import *
# from src.main.org.evosuite.runtime.EvoAssertions import *
# from src.main.org.evosuite.runtime.EvoRunnerParameters import *


class PercentValidator_ESTest(unittest.TestCase):

    def test7(self) -> None:
        bigDecimalValidator0 = PercentValidator.getInstance()
        self.assertTrue(bigDecimalValidator0.isAllowFractions())

    def test6(self) -> None:

        percentValidator0 = PercentValidator.PercentValidator1()
        locale0 = Locale.getLocale("de")
        numberFormat0 = NumberFormat.getNumberInstance(locale0)
        percentValidator0.parse("0.01", numberFormat0)
        self.assertTrue(percentValidator0.isStrict())

    def test5(self) -> None:

        percentValidator0 = PercentValidator.PercentValidator1()
        percentValidator0.validate3("(k9w,_vk/}-OK*8XX+j", '%z#~wbJQp*eO"|1', None)
        self.assertTrue(percentValidator0.isStrict())

    def test4(self) -> None:

        percentValidator0 = PercentValidator.PercentValidator1()
        dateFormat0 = DateFormat.getTimeInstance()
        percentValidator0.parse("*nbPg@/Af7", dateFormat0)
        self.assertTrue(percentValidator0.isStrict())

    def test3(self) -> None:

        percentValidator0 = PercentValidator.PercentValidator1()
        locale0 = Locale.getLocale("de")
        numberFormat0 = NumberFormat.getNumberInstance(locale0)
        percentValidator0.parse("", numberFormat0)
        self.assertTrue(percentValidator0.isStrict())

    def test2(self) -> None:

        percentValidator0 = PercentValidator(True)
        decimalFormat0 = NumberFormat.getPercentInstance()
        percentValidator0.parse("0", decimalFormat0)
        self.assertEqual(1, decimalFormat0.getMultiplier())
        self.assertEqual("#,##0", decimalFormat0.toPattern())

    def test1(self) -> None:

        percentValidator0 = PercentValidator.PercentValidator1()
        # Undeclared exception in Java code
        try:
            percentValidator0.parse("c+@4i%ard^t|[b^E`", None)
            self.fail("Expecting exception: RuntimeError")

        except Exception as e:
            # no message in exception (getMessage() returned null)
            self.verifyException(
                "org.apache.commons.validator.routines.AbstractFormatValidator", e
            )

    def test0(self) -> None:

        percentValidator0 = PercentValidator.PercentValidator1()
        numberFormat0 = NumberFormat.getInstance()

        try:
            percentValidator0.parse("0.01", numberFormat0)
            self.fail("Expecting exception: ValueError")

        except ValueError as e:
            verifyException("java.math.BigDecimal", e)
