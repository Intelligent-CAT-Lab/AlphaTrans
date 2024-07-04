from __future__ import annotations
import time
import re
import os
import unittest
import pytest
import io
import unittest
from src.main.org.apache.commons.validator.routines.checkdigit.CheckDigit import *
from src.main.org.apache.commons.validator.routines.checkdigit.LuhnCheckDigit import *

# from src.test.org.apache.commons.validator.routines.checkdigit.LuhnCheckDigit_ESTest_scaffolding import *
# from src.main.org.evosuite.runtime.EvoAssertions import *
# from src.main.org.evosuite.runtime.EvoRunnerParameters import *


class LuhnCheckDigit_ESTest(unittest.TestCase):

    def test4(self) -> None:

        luhnCheckDigit0 = LuhnCheckDigit()
        int0 = luhnCheckDigit0._weightedValue(0, 0, 0)
        self.assertEqual(0, int0)

    def test3(self) -> None:

        luhnCheckDigit0 = LuhnCheckDigit.LUHN_CHECK_DIGIT
        int0 = luhnCheckDigit0.weightedValue(12, 793, 952)
        self.assertEqual(15, int0)

    def test2(self) -> None:

        luhnCheckDigit0 = LuhnCheckDigit.LUHN_CHECK_DIGIT
        try:
            luhnCheckDigit0.weightedValue(3475, 9, -99)
            self.fail("Expecting exception: ArrayIndexOutOfBoundsException")

        except ArrayIndexOutOfBoundsException as e:
            self.verifyException(
                "org.apache.commons.validator.routines.checkdigit.LuhnCheckDigit", e
            )

    def test1(self) -> None:

        luhnCheckDigit0 = LuhnCheckDigit()
        int0 = luhnCheckDigit0._weightedValue(-742, -742, 2548)
        self.assertEqual(-1484, int0)

    def test0(self) -> None:

        luhnCheckDigit0 = LuhnCheckDigit.LUHN_CHECK_DIGIT
        int0 = luhnCheckDigit0.weightedValue(9, 0, 9)
        self.assertEqual(9, int0)
