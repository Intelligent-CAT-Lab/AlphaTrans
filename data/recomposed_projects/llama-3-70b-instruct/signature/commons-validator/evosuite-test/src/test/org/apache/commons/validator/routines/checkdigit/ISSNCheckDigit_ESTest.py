from __future__ import annotations
import time
import re
import os
import unittest
import pytest
import io
import unittest
from src.main.org.apache.commons.validator.routines.checkdigit.CheckDigit import *
from src.main.org.apache.commons.validator.routines.checkdigit.ISSNCheckDigit import *

# from src.test.org.apache.commons.validator.routines.checkdigit.ISSNCheckDigit_ESTest_scaffolding import *
# from src.main.org.evosuite.runtime.EvoAssertions import *
# from src.main.org.evosuite.runtime.EvoRunnerParameters import *


class ISSNCheckDigit_ESTest(unittest.TestCase):

    def test9(self) -> None:

        iSSNCheckDigit0 = ISSNCheckDigit()
        string0 = iSSNCheckDigit0.toCheckDigit(10)
        self.assertEqual("X", string0)

    def test8(self) -> None:

        iSSNCheckDigit0 = ISSNCheckDigit()
        boolean0 = iSSNCheckDigit0.isValid("00")
        self.assertFalse(boolean0)

    def test7(self) -> None:

        iSSNCheckDigit0 = ISSNCheckDigit.ISSN_CHECK_DIGIT
        try:
            iSSNCheckDigit0.toCheckDigit((-269))
            self.fail("Expecting exception: Exception")

        except Exception as e:
            # Invalid Check Digit Value =-269
            self.verifyException(
                "org.apache.commons.validator.routines.checkdigit.CheckDigitException",
                e,
            )

    def test6(self) -> None:

        iSSNCheckDigit0 = ISSNCheckDigit()
        try:
            iSSNCheckDigit0._toInt("e", 9, 1)
            self.fail("Expecting exception: Exception")

        except Exception as e:
            #
            # Invalid Character[9] = 'e'
            #
            self.assertIsInstance(e, CheckDigitException.CheckDigitException1)
            self.assertEqual(str(e), "Invalid Character[9] = 'e'")

    def test5(self) -> None:

        iSSNCheckDigit0 = ISSNCheckDigit()
        int0 = iSSNCheckDigit0._toInt("X", 1, 1)
        self.assertEqual(10, int0)

    def test4(self) -> None:
        iSSNCheckDigit0 = ISSNCheckDigit.ISSN_CHECK_DIGIT
        int0 = iSSNCheckDigit0._toInt("0", 0, 10)
        self.assertEqual(0, int0)

    def test3(self) -> None:

        iSSNCheckDigit0 = ISSNCheckDigit()
        int0 = iSSNCheckDigit0._weightedValue(-490, -490, -490)
        self.assertEqual(-244510, int0)

    def test2(self) -> None:

        iSSNCheckDigit0 = ISSNCheckDigit.ISSN_CHECK_DIGIT
        int0 = iSSNCheckDigit0._weightedValue(1, 1, 1)
        self.assertEqual(8, int0)

    def test1(self) -> None:

        iSSNCheckDigit0 = ISSNCheckDigit()
        int0 = iSSNCheckDigit0._weightedValue(0, 2011, 0)
        self.assertEqual(0, int0)

    def test0(self) -> None:

        iSSNCheckDigit0 = ISSNCheckDigit()
        try:
            iSSNCheckDigit0.toCheckDigit(11)
            self.fail("Expecting exception: Exception")

        except Exception as e:
            # Invalid Check Digit Value =11
            self.assertIsInstance(e, CheckDigitException)
