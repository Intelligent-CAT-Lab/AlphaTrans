from __future__ import annotations
import time
import re
import os
import unittest
import pytest
import io
import numbers
import unittest
from src.main.org.apache.commons.validator.routines.checkdigit.ABANumberCheckDigit import *

# from src.test.org.apache.commons.validator.routines.checkdigit.ABANumberCheckDigit_ESTest_scaffolding import *
from src.main.org.apache.commons.validator.routines.checkdigit.CheckDigit import *

# from src.main.org.evosuite.runtime.EvoAssertions import *
# from src.main.org.evosuite.runtime.EvoRunnerParameters import *


class ABANumberCheckDigit_ESTest(unittest.TestCase):

    def test3(self) -> None:

        aBANumberCheckDigit0 = ABANumberCheckDigit()
        try:
            aBANumberCheckDigit0._weightedValue(0, 1, -911)
            self.fail("Expecting exception: ArrayIndexOutOfBoundsException")

        except ArrayIndexOutOfBoundsException as e:
            self.verifyException(
                "org.apache.commons.validator.routines.checkdigit.ABANumberCheckDigit",
                e,
            )

    def test2(self) -> None:

        aBANumberCheckDigit0 = ABANumberCheckDigit()
        int0 = aBANumberCheckDigit0._weightedValue(-237, -237, -237)
        self.assertEqual(-711, int0)

    def test1(self) -> None:

        aBANumberCheckDigit0 = ABANumberCheckDigit()
        int0 = aBANumberCheckDigit0._weightedValue(10, 10, 21)
        self.assertEqual(int0, 30)

    def test0(self) -> None:

        aBANumberCheckDigit0 = ABANumberCheckDigit()
        int0 = aBANumberCheckDigit0._weightedValue(0, 5, 98)
        self.assertEqual(0, int0)
