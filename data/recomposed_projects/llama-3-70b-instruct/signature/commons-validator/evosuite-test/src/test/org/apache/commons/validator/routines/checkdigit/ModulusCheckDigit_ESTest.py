from __future__ import annotations
import time
import re
import os
import numbers
import unittest
import pytest
import io
import unittest
from src.main.org.apache.commons.validator.routines.checkdigit.ABANumberCheckDigit import *
from src.main.org.apache.commons.validator.routines.checkdigit.CUSIPCheckDigit import *
from src.main.org.apache.commons.validator.routines.checkdigit.CheckDigit import *
from src.main.org.apache.commons.validator.routines.checkdigit.ISBN10CheckDigit import *
from src.main.org.apache.commons.validator.routines.checkdigit.ISINCheckDigit import *
from src.main.org.apache.commons.validator.routines.checkdigit.ISSNCheckDigit import *
from src.main.org.apache.commons.validator.routines.checkdigit.LuhnCheckDigit import *
from src.main.org.apache.commons.validator.routines.checkdigit.ModulusCheckDigit import *

# from src.test.org.apache.commons.validator.routines.checkdigit.ModulusCheckDigit_ESTest_scaffolding import *
from src.main.org.apache.commons.validator.routines.checkdigit.ModulusTenCheckDigit import *
from src.main.org.apache.commons.validator.routines.checkdigit.SedolCheckDigit import *
from src.main.org.apache.commons.validator.routines.checkdigit.VerhoeffCheckDigit import *

# from src.main.org.evosuite.runtime.EvoAssertions import *
# from src.main.org.evosuite.runtime.EvoRunnerParameters import *


class ModulusCheckDigit_ESTest(unittest.TestCase):

    def test30(self) -> None:

        aBANumberCheckDigit0 = ABANumberCheckDigit()
        int0 = aBANumberCheckDigit0.getModulus()
        self.assertEqual(10, int0)

    def test29(self) -> None:

        luhnCheckDigit0 = LuhnCheckDigit()
        boolean0 = luhnCheckDigit0.isValid(None)
        self.assertFalse(boolean0)
        self.assertEqual(10, luhnCheckDigit0.getModulus())

    def test28(self) -> None:

        luhnCheckDigit0 = LuhnCheckDigit()
        boolean0 = luhnCheckDigit0.isValid("2931")
        self.assertTrue(boolean0)
        self.assertEqual(10, luhnCheckDigit0.getModulus())

    def test27(self) -> None:

        luhnCheckDigit0 = LuhnCheckDigit()
        boolean0 = luhnCheckDigit0.isValid("")
        self.assertEqual(10, luhnCheckDigit0.getModulus())
        self.assertFalse(boolean0)

    def test26(self) -> None:

        intArray0 = [0] * 4
        intArray0[0] = -5
        modulusTenCheckDigit0 = ModulusTenCheckDigit.ModulusTenCheckDigit1(
            intArray0, True
        )
        boolean0 = modulusTenCheckDigit0.isValid("9")
        self.assertFalse(boolean0)
        self.assertEqual(10, modulusTenCheckDigit0.getModulus())

    def test25(self) -> None:

        luhnCheckDigit0 = LuhnCheckDigit()
        try:
            luhnCheckDigit0.calculate(None)
            self.fail("Expecting exception: Exception")

        except Exception as e:
            self.assertIsInstance(e, CheckDigitException.CheckDigitException1)

    def test24(self) -> None:

        luhnCheckDigit0 = LuhnCheckDigit()
        string0 = luhnCheckDigit0.calculate("1")
        self.assertEqual("8", string0)

    def test23(self) -> None:

        luhnCheckDigit0 = LuhnCheckDigit()
        try:
            luhnCheckDigit0.calculate("")
            self.fail("Expecting exception: Exception")

        except Exception as e:
            self.verifyException(
                "org.apache.commons.validator.routines.checkdigit.CheckDigitException",
                e,
            )

    def test22(self) -> None:

        luhnCheckDigit0 = LuhnCheckDigit()
        boolean0 = luhnCheckDigit0.isValid("00")
        self.assertEqual(10, luhnCheckDigit0.getModulus())
        self.assertFalse(boolean0)

    def test21(self) -> None:

        luhnCheckDigit0 = LuhnCheckDigit()
        boolean0 = luhnCheckDigit0.isValid("Invalid Character[")
        self.assertFalse(boolean0)
        self.assertEqual(10, luhnCheckDigit0.getModulus())

    def test20(self) -> None:

        iSSNCheckDigit0 = ISSNCheckDigit()
        try:
            iSSNCheckDigit0.toCheckDigit((-857))
            self.fail("Expecting exception: Exception")

        except Exception as e:
            #
            # Invalid Check Digit Value =-857
            #
            self.assertIsInstance(e, CheckDigitException)

    def test19(self) -> None:

        luhnCheckDigit0 = LuhnCheckDigit()
        try:
            luhnCheckDigit0.toCheckDigit(775)
            self.fail("Expecting exception: Exception")

        except Exception as e:
            #
            # Invalid Check Digit Value =775
            #
            self.assertIsInstance(e, CheckDigitException)
            self.assertEqual(str(e), "Invalid Check Digit Value =775")

    def test18(self) -> None:

        int0 = ModulusCheckDigit.sumDigits(9)
        self.assertEqual(9, int0)

    def test17(self) -> None:

        intArray0 = []
        modulusTenCheckDigit0 = ModulusTenCheckDigit.ModulusTenCheckDigit1(
            intArray0, False
        )
        # Undeclared exception in Java
        try:
            modulusTenCheckDigit0.calculate("431")
            self.fail("Expecting exception: ArithmeticException")

        except ArithmeticError as e:
            #
            # / by zero
            #
            self.verifyException(
                "org.apache.commons.validator.routines.checkdigit.ModulusTenCheckDigit",
                e,
            )

    def test16(self) -> None:

        intArray0 = []
        modulusTenCheckDigit0 = ModulusTenCheckDigit.ModulusTenCheckDigit2(intArray0)

        try:
            modulusTenCheckDigit0._calculateModulus("uxpYyvc*qUY[w(K%35S", True)
            self.fail("Expecting exception: ArithmeticException")

        except ArithmeticError as e:
            self.verifyException(
                "org.apache.commons.validator.routines.checkdigit.ModulusTenCheckDigit",
                e,
            )

    def test15(self) -> None:

        aBANumberCheckDigit0 = ABANumberCheckDigit()
        try:
            aBANumberCheckDigit0.calculateModulus(None, True)
            self.fail("Expecting exception: RuntimeError")

        except Exception as e:
            self.verifyException(
                "org.apache.commons.validator.routines.checkdigit.ModulusCheckDigit", e
            )

    def test14(self) -> None:

        iSINCheckDigit0 = ISINCheckDigit()
        # Undeclared exception
        try:
            iSINCheckDigit0.calculateModulus("", True)
            self.fail("Expecting exception: StringIndexOutOfBoundsException")

        except StringIndexOutOfBoundsException:
            pass

    def test13(self) -> None:

        iSBN10CheckDigit0 = ISBN10CheckDigit()
        try:
            iSBN10CheckDigit0.calculateModulus("?5amv8m.>mzR", False)
            self.fail("Expecting exception: Exception")

        except Exception as e:
            #
            # Invalid Character[1] = '?'
            #
            self.verifyException(
                "org.apache.commons.validator.routines.checkdigit.CheckDigitException",
                e,
            )

    def test12(self) -> None:

        verhoeffCheckDigit0 = VerhoeffCheckDigit()
        try:
            verhoeffCheckDigit0.isValid("")
        except ValueError:
            self.fail("Expecting exception: ValueError")

    def test11(self) -> None:

        luhnCheckDigit0 = LuhnCheckDigit()
        try:
            luhnCheckDigit0.toInt("P", "P", "P")
            self.fail("Expecting exception: Exception")

        except Exception as e:
            #
            # Invalid Character[80] = 'P'
            #
            self.verifyException(
                "org.apache.commons.validator.routines.checkdigit.CheckDigitException",
                e,
            )

    def test10(self) -> None:

        intArray0 = [0] * 5
        intArray0[1] = 592
        intArray0[2] = -3243
        modulusTenCheckDigit0 = ModulusTenCheckDigit.ModulusTenCheckDigit1(
            intArray0, True
        )
        int0 = modulusTenCheckDigit0.calculateModulus("zuC", False)
        self.assertEqual(-6, int0)
        self.assertEqual(10, modulusTenCheckDigit0.getModulus())

    def test09(self) -> None:

        iSSNCheckDigit0 = ISSNCheckDigit()
        int0 = iSSNCheckDigit0.calculateModulus("9", True)
        self.assertEqual(6, int0)
        self.assertEqual(11, iSSNCheckDigit0.getModulus())

    def test08(self) -> None:

        sedolCheckDigit0 = SedolCheckDigit()
        int0 = sedolCheckDigit0.calculateModulus("01fq", False)
        self.assertEqual(0, int0)
        self.assertEqual(10, sedolCheckDigit0.getModulus())

    def test07(self) -> None:

        int0 = ModulusCheckDigit.sumDigits(0)
        self.assertEqual(0, int0)

    def test06(self) -> None:

        luhnCheckDigit0 = LuhnCheckDigit()
        string0 = luhnCheckDigit0.toCheckDigit(9)
        self.assertEqual("9", string0)
        self.assertEqual(10, luhnCheckDigit0.getModulus())

    def test05(self) -> None:

        luhnCheckDigit0 = LuhnCheckDigit()
        int0 = luhnCheckDigit0.toInt("4", 55, (-208))
        self.assertEqual(4, int0)
        self.assertEqual(10, luhnCheckDigit0.getModulus())

    def test04(self) -> None:

        luhnCheckDigit0 = LuhnCheckDigit()
        int0 = luhnCheckDigit0.toInt("0", 1, 1)
        self.assertEqual(0, int0)
        self.assertEqual(10, luhnCheckDigit0.getModulus())

    def test03(self) -> None:

        luhnCheckDigit0 = LuhnCheckDigit()
        boolean0 = luhnCheckDigit0.isValid("8")
        self.assertFalse(boolean0)
        self.assertEqual(10, luhnCheckDigit0.getModulus())

    def test02(self) -> None:

        iSSNCheckDigit0 = ISSNCheckDigit()
        string0 = iSSNCheckDigit0.toCheckDigit(0)
        self.assertEqual("0", string0)
        self.assertEqual(11, iSSNCheckDigit0.getModulus())

    def test01(self) -> None:

        cUSIPCheckDigit0 = CUSIPCheckDigit()
        int0 = cUSIPCheckDigit0._weightedValue(-318, -1158, -1158)
        self.assertEqual(0, int0)

    def test00(self) -> None:

        intArray0 = [0, -3373]
        modulusTenCheckDigit0 = ModulusTenCheckDigit(intArray0, True, True)
        int0 = modulusTenCheckDigit0._weightedValue(-3373, -965, 2630)
        self.assertEqual(31, int0)
        self.assertEqual(10, modulusTenCheckDigit0.getModulus())
