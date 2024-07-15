from __future__ import annotations
import time
import re
import os
import typing
from typing import *
import unittest
import pytest
import io
import unittest
from src.main.org.apache.commons.validator.routines.checkdigit.ModulusTenCheckDigit import *

# from src.test.org.apache.commons.validator.routines.checkdigit.ModulusTenCheckDigit_ESTest_scaffolding import *
# from src.main.org.evosuite.runtime.EvoAssertions import *
# from src.main.org.evosuite.runtime.EvoRunnerParameters import *


class ModulusTenCheckDigit_ESTest(unittest.TestCase):

    def test18(self) -> None:

        intArray0 = [0, 0, 0, 0]
        modulusTenCheckDigit0 = ModulusTenCheckDigit.ModulusTenCheckDigit1(
            intArray0, False
        )
        string0 = modulusTenCheckDigit0.toString()
        self.assertEqual(
            "ModulusTenCheckDigit[postitionWeight=[0, 0, 0, 0], useRightPos=False, sumWeightedDigits=False]",
            string0,
        )

    def test17(self) -> None:

        intArray0 = [0] * 17
        modulusTenCheckDigit0 = ModulusTenCheckDigit.ModulusTenCheckDigit2(intArray0)
        boolean0 = modulusTenCheckDigit0.isValid(None)
        self.assertFalse(boolean0)

    def test16(self) -> None:

        intArray0 = [0]
        modulusTenCheckDigit0 = ModulusTenCheckDigit.ModulusTenCheckDigit1(
            intArray0, False
        )
        boolean0 = modulusTenCheckDigit0.isValid("")
        self.assertFalse(boolean0)

    def test15(self) -> None:

        intArray0 = [0] * 5
        modulusTenCheckDigit0 = ModulusTenCheckDigit.ModulusTenCheckDigit1(
            intArray0, False
        )
        boolean0 = modulusTenCheckDigit0.isValid("11L'u%")
        self.assertFalse(boolean0)

    def test14(self) -> None:

        intArray0 = [0] * 10
        modulusTenCheckDigit0 = ModulusTenCheckDigit(intArray0, True, True)
        boolean0 = modulusTenCheckDigit0.isValid("37")
        self.assertFalse(boolean0)

    def test13(self) -> None:

        modulusTenCheckDigit0 = None
        try:
            modulusTenCheckDigit0 = ModulusTenCheckDigit(None, True, True)
            self.fail("Expecting exception: RuntimeError")

        except Exception as e:
            # no message in exception (getMessage() returned null)
            # verifyException("org.apache.commons.validator.routines.checkdigit.ModulusTenCheckDigit", e)
            self.assertIsInstance(e, TypeError)

    def test12(self) -> None:

        with pytest.raises(RuntimeError):
            ModulusTenCheckDigit.ModulusTenCheckDigit1(None, True)

    def test11(self) -> None:

        with pytest.raises(RuntimeError):
            ModulusTenCheckDigit.ModulusTenCheckDigit2(None)

    def test10(self) -> None:

        intArray0 = []
        modulusTenCheckDigit0 = ModulusTenCheckDigit.ModulusTenCheckDigit2(intArray0)

        try:
            modulusTenCheckDigit0.isValid("eH;x%=j7qBnzBs7")
            self.fail("Expecting exception: ArithmeticException")

        except ArithmeticError as e:
            self.verifyException(
                "org.apache.commons.validator.routines.checkdigit.ModulusTenCheckDigit",
                e,
            )

    def test09(self) -> None:

        intArray0 = [0] * 4
        modulusTenCheckDigit0 = ModulusTenCheckDigit.ModulusTenCheckDigit1(
            intArray0, False
        )
        try:
            modulusTenCheckDigit0._toInt("~", 118, -1)
            self.fail("Expecting exception: Exception")

        except Exception as e:
            #
            # Invalid Character[118] = '~'
            #
            self.assertIsInstance(e, CheckDigitException.CheckDigitException)

    def test08(self) -> None:

        intArray0 = []
        modulusTenCheckDigit0 = ModulusTenCheckDigit.ModulusTenCheckDigit2(intArray0)

        with pytest.raises(ArithmeticException):
            modulusTenCheckDigit0.weightedValue(33, 33, 33)

    def test07(self) -> None:

        intArray0 = [0] * 10
        modulusTenCheckDigit0 = ModulusTenCheckDigit.ModulusTenCheckDigit2(intArray0)

        with self.assertRaises(ArrayIndexOutOfBoundsException):
            modulusTenCheckDigit0.weightedValue(-3218, -3218, -3218)

    def test06(self) -> None:

        intArray0 = [0] * 9
        intArray0[0] = 133
        modulusTenCheckDigit0 = ModulusTenCheckDigit.ModulusTenCheckDigit2(intArray0)
        boolean0 = modulusTenCheckDigit0.isValid("k1")
        self.assertTrue(boolean0)

    def test05(self) -> None:

        intArray0 = [0] * 4
        modulusTenCheckDigit0 = ModulusTenCheckDigit.ModulusTenCheckDigit1(
            intArray0, False
        )
        int0 = modulusTenCheckDigit0._toInt("r", 1, 118)
        self.assertEqual(27, int0)

    def test04(self) -> None:

        intArray0 = [0] * 13
        modulusTenCheckDigit0 = ModulusTenCheckDigit.ModulusTenCheckDigit2(intArray0)
        int0 = modulusTenCheckDigit0._toInt("0", 10, -600)
        self.assertEqual(0, int0)

    def test03(self) -> None:

        intArray0 = [0] * 7
        intArray0[1] = -446
        modulusTenCheckDigit0 = ModulusTenCheckDigit(intArray0, True, False)
        int0 = modulusTenCheckDigit0._weightedValue(1871, 4315, 1871)
        self.assertEqual(-834466, int0)

    def test02(self) -> None:

        intArray0 = [1]
        modulusTenCheckDigit0 = ModulusTenCheckDigit.ModulusTenCheckDigit1(
            intArray0, False
        )
        int0 = modulusTenCheckDigit0._weightedValue(1, 1, 1599)
        self.assertEqual(1, int0)

    def test01(self) -> None:

        intArray0 = [0] * 4
        modulusTenCheckDigit0 = ModulusTenCheckDigit.ModulusTenCheckDigit1(
            intArray0, False
        )
        int0 = modulusTenCheckDigit0._weightedValue(3301, 701, 9)
        self.assertEqual(0, int0)

    def test00(self) -> None:

        intArray0 = [0] * 8
        intArray0[0] = -4465
        modulusTenCheckDigit0 = ModulusTenCheckDigit(intArray0, True, True)
        int0 = modulusTenCheckDigit0._weightedValue(21, -1538, 1465)
        self.assertEqual(0, int0)
