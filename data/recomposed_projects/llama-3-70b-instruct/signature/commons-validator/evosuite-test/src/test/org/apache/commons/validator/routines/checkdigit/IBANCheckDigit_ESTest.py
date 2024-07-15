from __future__ import annotations
import time
import re
import os
import unittest
import pytest
import io
import unittest
from src.main.org.apache.commons.validator.routines.checkdigit.CheckDigit import *
from src.main.org.apache.commons.validator.routines.checkdigit.IBANCheckDigit import *

# from src.test.org.apache.commons.validator.routines.checkdigit.IBANCheckDigit_ESTest_scaffolding import *
# from src.main.org.evosuite.runtime.EvoAssertions import *
# from src.main.org.evosuite.runtime.EvoRunnerParameters import *


class IBANCheckDigit_ESTest(unittest.TestCase):

    def test12(self) -> None:

        iban_check_digit = IBANCheckDigit()
        boolean0 = iban_check_digit.isValid(None)
        self.assertFalse(boolean0)

    def test11(self) -> None:

        ibanCheckDigit0 = IBANCheckDigit()
        boolean0 = ibanCheckDigit0.isValid("60")
        self.assertFalse(boolean0)

    def test10(self) -> None:

        iban_check_digit0 = IBANCheckDigit()
        boolean0 = iban_check_digit0.isValid("6X00@+kJ@bp:P,")
        self.assertFalse(boolean0)

    def test09(self) -> None:

        iban_check_digit0 = IBANCheckDigit()
        boolean0 = iban_check_digit0.isValid("6X01ok#@p:P,")
        self.assertFalse(boolean0)

    def test08(self) -> None:

        iBANCheckDigit0 = IBANCheckDigit()
        boolean0 = iBANCheckDigit0.isValid("f`99wfb~*:q4Mwj")
        self.assertFalse(boolean0)

    def test07(self) -> None:

        iban_check_digit = IBANCheckDigit()
        boolean0 = iban_check_digit.isValid("ymJ36YtZJhF")
        self.assertFalse(boolean0)

    def test06(self) -> None:

        iBANCheckDigit0 = IBANCheckDigit()
        boolean0 = iBANCheckDigit0.isValid("D9ULRaW")
        self.assertTrue(boolean0)

    def test05(self) -> None:

        iban_check_digit0 = IBANCheckDigit()
        try:
            iban_check_digit0.calculate(None)
            self.fail("Expecting exception: Exception")

        except Exception as e:
            # Invalid Code length=0
            self.verifyException(
                "org.apache.commons.validator.routines.checkdigit.CheckDigitException",
                e,
            )

    def test04(self) -> None:

        iban_check_digit0 = IBANCheckDigit()
        try:
            iban_check_digit0.calculate("-0")
            self.fail("Expecting exception: Exception")

        except Exception as e:
            #
            # Invalid Code length=2
            #
            self.verifyException(
                "org.apache.commons.validator.routines.checkdigit.CheckDigitException",
                e,
            )

    def test03(self) -> None:

        iban_check_digit0 = IBANCheckDigit()
        string0 = iban_check_digit0.calculate("ymJ36YtZJhF")
        self.assertEqual("08", string0)

    def test02(self) -> None:

        iBANCheckDigit0 = IBANCheckDigit()
        boolean0 = iBANCheckDigit0.isValid("] in ")
        self.assertFalse(boolean0)

    def test01(self) -> None:

        iban_check_digit0 = IBANCheckDigit()
        string0 = iban_check_digit0.calculate("cgY]z")
        self.assertEqual("64", string0)

    def test00(self) -> None:

        iban_check_digit0 = IBANCheckDigit()
        string0 = iban_check_digit0.calculate("ymJ36YtZJF")
        self.assertEqual("09", string0)
