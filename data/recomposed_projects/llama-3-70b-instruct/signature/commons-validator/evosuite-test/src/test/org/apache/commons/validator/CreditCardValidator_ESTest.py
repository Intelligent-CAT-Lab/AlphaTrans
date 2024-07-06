from __future__ import annotations
import time
import re
import mock
import os
import typing
from typing import *
import numbers
import unittest
import pytest
import io
import unittest
from src.main.org.apache.commons.validator.CreditCardValidator import *

# from src.test.org.apache.commons.validator.CreditCardValidator_ESTest_scaffolding import *
# from src.main.org.evosuite.runtime.EvoAssertions import *
# from src.main.org.evosuite.runtime.EvoRunnerParameters import *
# from src.main.org.evosuite.runtime.ViolatedAssumptionAnswer import *
# from src.main.org.evosuite.shaded.org.mockito.Mockito import *
# from src.main.org.evosuite.shaded.org.mockito.stubbing.Answer import *
from src.main.org.apache.commons.validator.routines.CodeValidator import *
from src.main.org.apache.commons.validator.routines.CreditCardValidator import *

# from src.test.org.apache.commons.validator.routines.CreditCardValidator_ESTest_scaffolding import *
from src.main.org.apache.commons.validator.routines.checkdigit.ABANumberCheckDigit import *
from src.main.org.apache.commons.validator.routines.checkdigit.CheckDigit import *
from src.main.org.apache.commons.validator.routines.checkdigit.EAN13CheckDigit import *
from src.main.org.apache.commons.validator.routines.checkdigit.ISBNCheckDigit import *


class CreditCardValidator_ESTest(unittest.TestCase):

    def test12(self) -> None:

        creditCardValidator0 = CreditCardValidator.CreditCardValidator1()
        creditCardValidator_CreditCardType0 = unittest.mock.Mock(
            spec=CreditCardValidator.CreditCardType
        )
        creditCardValidator0.addAllowedCardType(creditCardValidator_CreditCardType0)
        self.assertEqual(4, CreditCardValidator.MASTERCARD)

    def test11(self) -> None:

        creditCardValidator0 = CreditCardValidator(9)
        boolean0 = creditCardValidator0.isValid('Lo0;EKEUBmN&."3F./]')
        self.assertFalse(boolean0)

    def test10(self) -> None:

        creditCardValidator0 = CreditCardValidator(0)
        self.assertEqual(4, CreditCardValidator.MASTERCARD)

    def test09(self) -> None:

        creditCardValidator0 = CreditCardValidator(1107)
        boolean0 = creditCardValidator0.isValid(None)
        self.assertFalse(boolean0)

    def test08(self) -> None:

        creditCardValidator0 = CreditCardValidator.CreditCardValidator1()
        boolean0 = creditCardValidator0.isValid("Couldn't clone Flags object.")
        self.assertFalse(boolean0)

    def test07(self) -> None:

        creditCardValidator0 = CreditCardValidator.CreditCardValidator1()
        boolean0 = creditCardValidator0.isValid("50")
        self.assertFalse(boolean0)

    def test06(self) -> None:

        creditCardValidator0 = CreditCardValidator.CreditCardValidator1()
        boolean0 = creditCardValidator0.isValid("51,52,53,54,55,")
        self.assertFalse(boolean0)

    def test05(self) -> None:

        creditCardValidator0 = CreditCardValidator.CreditCardValidator1()
        boolean0 = creditCardValidator0._luhnCheck("6011")
        self.assertFalse(boolean0)

    def test04(self) -> None:

        creditCardValidator0 = CreditCardValidator.CreditCardValidator1()
        boolean0 = creditCardValidator0._luhnCheck("")
        self.assertFalse(boolean0)

    def test03(self) -> None:

        creditCardValidator0 = CreditCardValidator.CreditCardValidator1()
        boolean0 = creditCardValidator0._luhnCheck("91")
        self.assertTrue(boolean0)

    def test02(self) -> None:

        creditCardValidator0 = CreditCardValidator(-1283)
        self.assertEqual(0, CreditCardValidator.NONE)

    def test01(self) -> None:

        creditCardValidator0 = CreditCardValidator.CreditCardValidator1()
        # Undeclared exception in Java, so we use a try-except block
        try:
            creditCardValidator0.luhnCheck(None)
            self.fail("Expecting exception: RuntimeError")

        except Exception as e:
            # no message in exception (getMessage() returned null)
            # verifyException("org.apache.commons.validator.CreditCardValidator", e)
            # In Python, we can use assert to verify the exception type
            assert isinstance(e, TypeError), "Expecting exception: RuntimeError"

    def test00(self) -> None:

        creditCardValidator0 = CreditCardValidator((-1167))
        boolean0 = creditCardValidator0.isValid("HASa~KzKe`FDv")
        self.assertFalse(boolean0)
