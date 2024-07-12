from __future__ import annotations
import time
import re
import os
import unittest
import pytest
import io
import unittest
from src.main.org.apache.commons.validator.routines.checkdigit.VerhoeffCheckDigit import *

# from src.test.org.apache.commons.validator.routines.checkdigit.VerhoeffCheckDigit_ESTest_scaffolding import *
# from src.main.org.evosuite.runtime.EvoAssertions import *
# from src.main.org.evosuite.runtime.EvoRunnerParameters import *


class VerhoeffCheckDigit_ESTest(unittest.TestCase):

    def test8(self) -> None:

        verhoeffCheckDigit0 = VerhoeffCheckDigit()
        boolean0 = verhoeffCheckDigit0.isValid(None)
        self.assertFalse(boolean0)

    def test7(self) -> None:

        verhoeffCheckDigit0 = VerhoeffCheckDigit()
        boolean0 = verhoeffCheckDigit0.isValid("")
        self.assertFalse(boolean0)

    def test6(self) -> None:

        verhoeffCheckDigit0 = VerhoeffCheckDigit()
        boolean0 = verhoeffCheckDigit0.isValid("0")
        self.assertTrue(boolean0)

    def test5(self) -> None:

        verhoeffCheckDigit0 = VerhoeffCheckDigit()
        try:
            verhoeffCheckDigit0.calculate(None)
            self.fail("Expecting exception: Exception")

        except Exception as e:
            self.assertIsInstance(e, CheckDigitException.CheckDigitException1)
            self.assertEqual(str(e), "Code is missing")

    def test4(self) -> None:

        verhoeffCheckDigit0 = VerhoeffCheckDigit()
        try:
            verhoeffCheckDigit0.calculate("")
            self.fail("Expecting exception: Exception")

        except Exception as e:
            self.assertIsInstance(e, CheckDigitException.CheckDigitException1)

    def test3(self) -> None:

        verhoeffCheckDigit0 = VerhoeffCheckDigit()
        boolean0 = verhoeffCheckDigit0.isValid("3R#0^{>b*Je^FN3")
        self.assertFalse(boolean0)

    def test2(self) -> None:

        verhoeffCheckDigit0 = VerhoeffCheckDigit()
        boolean0 = verhoeffCheckDigit0.isValid("D(9")
        self.assertFalse(boolean0)

    def test1(self) -> None:

        verhoeffCheckDigit0 = VerhoeffCheckDigit()
        boolean0 = verhoeffCheckDigit0.isValid("00")
        self.assertFalse(boolean0)

    def test0(self) -> None:

        verhoeffCheckDigit0 = VerhoeffCheckDigit()
        string0 = verhoeffCheckDigit0.calculate("01")
        self.assertEqual("0", string0)
