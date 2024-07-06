from __future__ import annotations
import time
import re
import os
import unittest
import pytest
import io
import unittest
from src.main.org.apache.commons.validator.routines.checkdigit.CUSIPCheckDigit import *

# from src.test.org.apache.commons.validator.routines.checkdigit.CUSIPCheckDigit_ESTest_scaffolding import *
from src.main.org.apache.commons.validator.routines.checkdigit.CheckDigit import *

# from src.main.org.evosuite.runtime.EvoAssertions import *
# from src.main.org.evosuite.runtime.EvoRunnerParameters import *


class CUSIPCheckDigit_ESTest(unittest.TestCase):

    def test7(self) -> None:

        cUSIPCheckDigit0 = CUSIPCheckDigit()
        # Undeclared exception in Java code
        try:
            cUSIPCheckDigit0._weightedValue((-1), (-1), (-1))
            self.fail("Expecting exception: ArrayIndexOutOfBoundsException")

        except IndexError as e:
            #
            # Index -1 out of bounds for length 2
            #
            self.assertEqual(str(e), "list index out of range")

    def test6(self) -> None:

        cUSIPCheckDigit0 = CUSIPCheckDigit()
        int0 = cUSIPCheckDigit0._toInt("b", 0, 1721)
        self.assertEqual(11, int0)

    def test5(self) -> None:

        cUSIPCheckDigit0 = CUSIPCheckDigit()
        boolean0 = cUSIPCheckDigit0.isValid("FZg")
        self.assertFalse(boolean0)

    def test4(self) -> None:

        cUSIPCheckDigit0 = CUSIPCheckDigit()
        try:
            cUSIPCheckDigit0.calculateModulus("yK2LZKyCL?LN6bQok2", True)
            self.fail("Expecting exception: Exception")

        except Exception as e:
            # Invalid Character[10,9] = '-1' out of range 0 to 35
            self.verifyException(
                "org.apache.commons.validator.routines.checkdigit.CheckDigitException",
                e,
            )

    def test3(self) -> None:

        cUSIPCheckDigit0 = CUSIPCheckDigit()
        try:
            cUSIPCheckDigit0._toInt("<", "<", "<")
            self.fail("Expecting exception: Exception")

        except Exception as e:
            #
            # Invalid Character[60,60] = '-1' out of range 0 to 35
            #
            self.assertIsInstance(e, CheckDigitException.CheckDigitException1)
            self.assertEqual(
                str(e), "Invalid Character[<,<] = '-1' out of range 0 to 35"
            )

    def test2(self) -> None:

        cUSIPCheckDigit0 = CUSIPCheckDigit()
        int0 = cUSIPCheckDigit0._toInt("0", 1503, 32)
        self.assertEqual(0, int0)

    def test1(self) -> None:

        cUSIPCheckDigit0 = CUSIPCheckDigit()
        int0 = cUSIPCheckDigit0._weightedValue(2302, 2302, 578)
        self.assertEqual(14, int0)

    def test0(self) -> None:

        cUSIPCheckDigit0 = CUSIPCheckDigit()
        int0 = cUSIPCheckDigit0._weightedValue(-493, 2302, 14)
        self.assertEqual(0, int0)
