from __future__ import annotations
import time
import re
import os
import unittest
import pytest
import io
import unittest
from src.main.org.apache.commons.validator.routines.checkdigit.CheckDigit import *
from src.main.org.apache.commons.validator.routines.checkdigit.EAN13CheckDigit import *

# from src.test.org.apache.commons.validator.routines.checkdigit.EAN13CheckDigit_ESTest_scaffolding import *
# from src.main.org.evosuite.runtime.EvoAssertions import *
# from src.main.org.evosuite.runtime.EvoRunnerParameters import *


class EAN13CheckDigit_ESTest(unittest.TestCase):

    def test3(self) -> None:

        eAN13CheckDigit0 = EAN13CheckDigit.EAN13_CHECK_DIGIT
        int0 = eAN13CheckDigit0._weightedValue(0, 0, 0)
        self.assertEqual(0, int0)

    def test2(self) -> None:

        ean13CheckDigit0 = EAN13CheckDigit()
        try:
            ean13CheckDigit0._weightedValue(4, 7, -1563)
            self.fail("Expecting exception: ArrayIndexOutOfBoundsException")

        except IndexError as e:
            self.assertEqual(str(e), "array index out of bounds")

    def test1(self) -> None:

        eAN13CheckDigit0 = EAN13CheckDigit()
        int0 = eAN13CheckDigit0._weightedValue(-550, 0, 7)
        self.assertEqual(-550, int0)

    def test0(self) -> None:

        eAN13CheckDigit0 = EAN13CheckDigit.EAN13_CHECK_DIGIT
        int0 = eAN13CheckDigit0._weightedValue(610, 0, 0)
        self.assertEqual(1830, int0)
