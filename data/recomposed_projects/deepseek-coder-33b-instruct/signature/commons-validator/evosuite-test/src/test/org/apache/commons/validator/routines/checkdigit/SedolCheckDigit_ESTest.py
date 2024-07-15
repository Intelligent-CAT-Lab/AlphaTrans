from __future__ import annotations
import time
import re
import os
import unittest
import pytest
import io
import unittest
from src.main.org.apache.commons.validator.routines.checkdigit.CUSIPCheckDigit import *
from src.main.org.apache.commons.validator.routines.checkdigit.CheckDigit import *
from src.main.org.apache.commons.validator.routines.checkdigit.SedolCheckDigit import *

# from src.test.org.apache.commons.validator.routines.checkdigit.SedolCheckDigit_ESTest_scaffolding import *
# from src.main.org.evosuite.runtime.EvoAssertions import *
# from src.main.org.evosuite.runtime.EvoRunnerParameters import *


class SedolCheckDigit_ESTest(unittest.TestCase):

    def test13(self) -> None:

        sedolCheckDigit0 = SedolCheckDigit()
        int0 = sedolCheckDigit0._weightedValue(0, 7, 5)
        self.assertEqual(0, int0)

    def test12(self) -> None:

        sedolCheckDigit0 = SedolCheckDigit()
        try:
            sedolCheckDigit0._calculateModulus("7u[Z'O}_CdPT]", True)
            self.fail("Expecting exception: Exception")

        except Exception as e:
            #
            # Invalid Code Length = 13
            #
            self.assertIsInstance(e, CheckDigitException.CheckDigitException1)
            self.assertEqual(str(e), "Invalid Code Length = 13")

    def test11(self) -> None:

        sedolCheckDigit0 = SedolCheckDigit()
        try:
            sedolCheckDigit0.calculate('y-F"Eco')
            self.fail("Expecting exception: Exception")

        except Exception as e:
            #
            # Invalid Character[2,7] = '-1' out of range 0 to 35
            #
            self.verifyException(
                "org.apache.commons.validator.routines.checkdigit.CheckDigitException",
                e,
            )

    def test10(self) -> None:

        sedolCheckDigit0 = SedolCheckDigit()
        try:
            sedolCheckDigit0._calculateModulus("I", True)
            self.fail("Expecting exception: Exception")

        except Exception as e:
            #
            # Invalid Character[1,1] = '18' out of range 0 to 9
            #
            self.verifyException(
                "org.apache.commons.validator.routines.checkdigit.CheckDigitException",
                e,
            )

    def test09(self) -> None:

        sedolCheckDigit0 = SedolCheckDigit()
        # Undeclared exception in Java
        try:
            sedolCheckDigit0.calculateModulus(None, True)
            self.fail("Expecting exception: RuntimeError")

        except Exception as e:
            # no message in exception (getMessage() returned null)
            self.verifyException(
                "org.apache.commons.validator.routines.checkdigit.SedolCheckDigit", e
            )

    def test08(self) -> None:

        cUSIPCheckDigit0 = CUSIPCheckDigit()

        try:
            cUSIPCheckDigit0._toInt("S", 35, 35)
        except CheckDigitException.CheckDigitException1:
            pass

    def test07(self) -> None:

        sedolCheckDigit0 = SedolCheckDigit()
        try:
            sedolCheckDigit0._toInt("-", "-", "-")
            self.fail("Expecting exception: Exception")

        except Exception as e:
            #
            # Invalid Character[45,45] = '-1' out of range 0 to 35
            #
            self.assertIsInstance(e, CheckDigitException.CheckDigitException1)
            self.assertEqual(
                str(e), "Invalid Character[-,-,-] = '--' is not alphanumeric"
            )

    def test06(self) -> None:

        sedolCheckDigit0 = SedolCheckDigit()
        # Undeclared exception in Java
        try:
            sedolCheckDigit0._weightedValue(17, 17, 17)
            self.fail("Expecting exception: ArrayIndexOutOfBoundsException")

        except IndexError as e:
            # Index 16 out of bounds for length 7
            self.assertEqual(str(e), "list index out of range")

    def test05(self) -> None:

        sedolCheckDigit0 = SedolCheckDigit()
        int0 = sedolCheckDigit0._calculateModulus("NA0", True)
        self.assertEqual(int0, 3)

    def test04(self) -> None:

        sedolCheckDigit0 = SedolCheckDigit()
        int0 = sedolCheckDigit0._calculateModulus("a", False)
        self.assertEqual(0, int0)

    def test03(self) -> None:

        sedolCheckDigit0 = SedolCheckDigit()
        int0 = sedolCheckDigit0._toInt("Z", 1, 1)
        self.assertEqual(35, int0)

    def test02(self) -> None:

        sedolCheckDigit0 = SedolCheckDigit()
        int0 = sedolCheckDigit0._toInt("0", -2334, 1383)
        self.assertEqual(0, int0)

    def test01(self) -> None:

        sedolCheckDigit0 = SedolCheckDigit()
        int0 = sedolCheckDigit0._weightedValue(-1489, 6, -1688)
        self.assertEqual(-13401, int0)

    def test00(self) -> None:

        sedolCheckDigit0 = SedolCheckDigit()
        int0 = sedolCheckDigit0._weightedValue(4, 4, 4)
        self.assertEqual(28, int0)
