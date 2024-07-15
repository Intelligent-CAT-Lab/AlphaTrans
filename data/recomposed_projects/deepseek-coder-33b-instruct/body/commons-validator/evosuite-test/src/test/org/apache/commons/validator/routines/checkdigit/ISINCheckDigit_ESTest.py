from __future__ import annotations
import time
import re
import os
import unittest
import pytest
import io
import unittest
from src.main.org.apache.commons.validator.routines.checkdigit.CheckDigit import *
from src.main.org.apache.commons.validator.routines.checkdigit.ISINCheckDigit import *

# from src.test.org.apache.commons.validator.routines.checkdigit.ISINCheckDigit_ESTest_scaffolding import *
# from src.main.org.evosuite.runtime.EvoAssertions import *
# from src.main.org.evosuite.runtime.EvoRunnerParameters import *


class ISINCheckDigit_ESTest(unittest.TestCase):

    def test9(self) -> None:

        iSINCheckDigit0 = ISINCheckDigit()
        try:
            iSINCheckDigit0.calculateModulus("N94IBfDd;Jq]uk]9", True)
            self.fail("Expecting exception: Exception")

        except Exception as e:
            #
            # Invalid Character[9] = '-1'
            #
            self.verifyException(
                "org.apache.commons.validator.routines.checkdigit.CheckDigitException",
                e,
            )

    def test8(self) -> None:

        iSINCheckDigit0 = ISINCheckDigit()
        try:
            iSINCheckDigit0._calculateModulus(",(9t", True)
            self.fail("Expecting exception: Exception")

        except Exception as e:
            #
            # Invalid checkdigit[t] in ,(9t
            #
            self.verifyException(
                "org.apache.commons.validator.routines.checkdigit.CheckDigitException",
                e,
            )

    def test7(self) -> None:

        iSINCheckDigit0 = ISINCheckDigit()
        # Undeclared exception in Java code
        try:
            iSINCheckDigit0.calculateModulus(None, True)
            self.fail("Expecting exception: RuntimeError")

        except RuntimeError as e:
            # no message in exception (getMessage() returned null)
            self.verifyException(
                "org.apache.commons.validator.routines.checkdigit.ISINCheckDigit", e
            )

    def test6(self) -> None:

        iSINCheckDigit0 = ISINCheckDigit()
        # Undeclared exception
        try:
            iSINCheckDigit0._calculateModulus("", True)
            self.fail("Expecting exception: StringIndexOutOfBoundsException")

        except StringIndexOutOfBoundsException:
            pass

    def test5(self) -> None:

        iSINCheckDigit0 = ISINCheckDigit()
        # Undeclared exception in Java code
        try:
            iSINCheckDigit0._weightedValue(4760, 88, (-4127))
            self.fail("Expecting exception: ArrayIndexOutOfBoundsException")

        except IndexError as e:
            # Index -1 out of bounds for length 2
            self.assertEqual(str(e), "list index out of range")

    def test4(self) -> None:

        iSINCheckDigit0 = ISINCheckDigit()
        int0 = iSINCheckDigit0._calculateModulus("Z", False)
        self.assertEqual(int0, 4)

    def test3(self) -> None:

        iSINCheckDigit0 = ISINCheckDigit()
        int0 = iSINCheckDigit0._calculateModulus("j", False)
        self.assertEqual(0, int0)

    def test2(self) -> None:

        iSINCheckDigit0 = ISINCheckDigit.ISIN_CHECK_DIGIT
        int0 = iSINCheckDigit0._weightedValue(546, -1322, -1352)
        self.assertEqual(12, int0)

    def test1(self) -> None:

        iSINCheckDigit0 = ISINCheckDigit()
        int0 = iSINCheckDigit0._weightedValue(0, 0, 0)
        self.assertEqual(0, int0)

    def test0(self) -> None:

        iSINCheckDigit0 = ISINCheckDigit()
        try:
            iSINCheckDigit0.calculate("00")
            self.fail("Expecting exception: Exception")

        except Exception as e:
            self.assertIsInstance(e, CheckDigitException)
