from __future__ import annotations
import time
import re
import os
import unittest
import pytest
import io
import unittest
from src.main.org.apache.commons.validator.routines.checkdigit.CheckDigit import *
from src.main.org.apache.commons.validator.routines.checkdigit.ISBN10CheckDigit import *

# from src.test.org.apache.commons.validator.routines.checkdigit.ISBN10CheckDigit_ESTest_scaffolding import *
# from src.main.org.evosuite.runtime.EvoAssertions import *
# from src.main.org.evosuite.runtime.EvoRunnerParameters import *


class ISBN10CheckDigit_ESTest(unittest.TestCase):

    def test11(self) -> None:

        iSBN10CheckDigit0 = ISBN10CheckDigit()
        boolean0 = iSBN10CheckDigit0.isValid("0")
        self.assertFalse(boolean0)

    def test10(self) -> None:

        ISBN10CheckDigit0 = ISBN10CheckDigit()
        boolean0 = ISBN10CheckDigit0.isValid("X")
        self.assertFalse(boolean0)

    def test09(self) -> None:
        iSBN10CheckDigit0 = ISBN10CheckDigit()
        string0 = iSBN10CheckDigit0.toCheckDigit(10)
        self.assertEqual("X", string0)

    def test08(self) -> None:

        ISBN10CheckDigit0 = ISBN10CheckDigit()
        try:
            ISBN10CheckDigit0.toCheckDigit((-17))
            self.fail("Expecting exception: Exception")

        except Exception as e:
            # Invalid Check Digit Value =-17
            self.assertIsInstance(e, CheckDigitException)

    def test07(self) -> None:
        iSBN10CheckDigit0 = ISBN10CheckDigit()
        int0 = iSBN10CheckDigit0._toInt("5", 13, 0)
        self.assertEqual(5, int0)

    def test06(self) -> None:
        iSBN10CheckDigit0 = ISBN10CheckDigit()
        int0 = iSBN10CheckDigit0._toInt("0", -1087, 3573)
        self.assertEqual(0, int0)

    def test05(self) -> None:

        ISBN10CheckDigit0 = ISBN10CheckDigit()
        int0 = ISBN10CheckDigit0._weightedValue(3, -858, -858)
        self.assertEqual(-2574, int0)

    def test04(self) -> None:
        iSBN10CheckDigit0 = ISBN10CheckDigit()
        int0 = iSBN10CheckDigit0._weightedValue(-101, -101, -101)
        self.assertEqual(10201, int0)

    def test03(self) -> None:
        iSBN10CheckDigit0 = ISBN10CheckDigit()
        int0 = iSBN10CheckDigit0._weightedValue(0, 0, 0)
        self.assertEqual(0, int0)

    def test02(self) -> None:

        ISBN10CheckDigit0 = ISBN10CheckDigit()
        try:
            ISBN10CheckDigit0.calculateModulus("0", False)
            self.fail("Expecting exception: Exception")

        except Exception as e:
            self.assertIsInstance(e, CheckDigitException)
            self.assertEqual(str(e), "Invalid code, sum is zero")

    def test01(self) -> None:

        ISBN10CheckDigit0 = ISBN10CheckDigit()
        try:
            ISBN10CheckDigit0._toInt("g", 1, 1)
            self.fail("Expecting exception: Exception")

        except Exception as e:
            # Invalid Character[1] = 'g'
            self.assertIsInstance(e, CheckDigitException.CheckDigitException1)
            self.assertEqual(str(e), "Invalid Character[1] = 'g'")

    def test00(self) -> None:

        ISBN10CheckDigit0 = ISBN10CheckDigit()
        try:
            ISBN10CheckDigit0.toCheckDigit(13)
            self.fail("Expecting exception: Exception")

        except Exception as e:
            # Invalid Check Digit Value =13
            self.assertIsInstance(e, CheckDigitException)
