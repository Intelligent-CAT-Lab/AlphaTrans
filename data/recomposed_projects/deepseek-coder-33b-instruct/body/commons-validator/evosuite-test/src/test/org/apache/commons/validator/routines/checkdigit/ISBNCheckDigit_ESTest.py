from __future__ import annotations
import time
import re
import os
import unittest
import pytest
import io
import unittest
from src.main.org.apache.commons.validator.routines.checkdigit.CheckDigit import *
from src.main.org.apache.commons.validator.routines.checkdigit.ISBNCheckDigit import *

# from src.test.org.apache.commons.validator.routines.checkdigit.ISBNCheckDigit_ESTest_scaffolding import *
# from src.main.org.evosuite.runtime.EvoAssertions import *
# from src.main.org.evosuite.runtime.EvoRunnerParameters import *


class ISBNCheckDigit_ESTest(unittest.TestCase):

    def test10(self) -> None:

        ISBNCheckDigit0 = ISBNCheckDigit()
        try:
            ISBNCheckDigit0.calculate(None)
            self.fail("Expecting exception: Exception")

        except Exception as e:
            #
            # ISBN Code is missing
            #
            self.assertIsInstance(e, CheckDigitException.CheckDigitException1)
            self.assertEqual(str(e), "ISBN Code is missing")

    def test09(self) -> None:

        ISBNCheckDigit0 = ISBNCheckDigit()
        try:
            ISBNCheckDigit0.calculate("{Il^|idEG")
            self.fail("Expecting exception: Exception")

        except Exception as e:
            # Invalid Character[1] = '{'
            self.assertIsInstance(e, CheckDigitException.CheckDigitException1)

    def test08(self) -> None:

        ISBNCheckDigit0 = ISBNCheckDigit()
        try:
            ISBNCheckDigit0.calculate("")
            self.fail("Expecting exception: Exception")

        except Exception as e:
            # ISBN Code is missing
            self.assertIsInstance(e, CheckDigitException.CheckDigitException1)
            self.assertEqual(str(e), "ISBN Code is missing")

    def test07(self) -> None:

        ISBNCheckDigit0 = ISBNCheckDigit()
        try:
            ISBNCheckDigit0.calculate("oX~n>Vl[UJD")
            self.fail("Expecting exception: Exception")

        except Exception as e:
            self.assertIsInstance(e, CheckDigitException)

    def test06(self) -> None:

        ISBNCheckDigit0 = ISBNCheckDigit()
        try:
            ISBNCheckDigit0.calculate(
                "org.apache.commons.validator.routines.checkdigit.ISBNCheckDigit"
            )
            self.fail("Expecting exception: Exception")

        except Exception as e:
            #
            # Invalid ISBN Length = 63
            #
            self.assertIsInstance(e, CheckDigitException.CheckDigitException1)
            self.assertEqual(str(e), "Invalid ISBN Length = 63")

    def test05(self) -> None:

        ISBNCheckDigit0 = ISBNCheckDigit()
        boolean0 = ISBNCheckDigit0.isValid('1v#[/["o>v4ro')
        self.assertFalse(boolean0)

    def test04(self) -> None:

        ISBNCheckDigit0 = ISBNCheckDigit()
        boolean0 = ISBNCheckDigit0.isValid(None)
        self.assertFalse(boolean0)

    def test03(self) -> None:

        ISBNCheckDigit0 = ISBNCheckDigit()
        boolean0 = ISBNCheckDigit0.isValid("zIO8;%A5\t;")
        self.assertFalse(boolean0)

    def test02(self) -> None:

        iSBNCheckDigit0 = ISBNCheckDigit()
        boolean0 = iSBNCheckDigit0.isValid(
            "org.apache.commons.validator.routines.checkdigit.ModulusTenCheckDigit"
        )
        self.assertFalse(boolean0)

    def test01(self) -> None:

        ISBNCheckDigit0 = ISBNCheckDigit()
        try:
            ISBNCheckDigit0.calculate("YOmVf)F")
            self.fail("Expecting exception: Exception")

        except Exception as e:
            # Invalid ISBN Length = 8
            self.assertIsInstance(e, CheckDigitException.CheckDigitException1)
            self.assertEqual(str(e), "Invalid ISBN Length = 8")

    def test00(self) -> None:

        ISBNCheckDigit0 = ISBNCheckDigit()
        boolean0 = ISBNCheckDigit0.isValid("")
        self.assertFalse(boolean0)
