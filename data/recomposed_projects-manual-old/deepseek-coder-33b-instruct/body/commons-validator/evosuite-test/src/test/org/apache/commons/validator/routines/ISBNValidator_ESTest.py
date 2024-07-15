from __future__ import annotations
import time
import re
import os
import unittest
import pytest
import io
import unittest
from src.main.org.apache.commons.validator.ISBNValidator import *

# from src.test.org.apache.commons.validator.ISBNValidator_ESTest_scaffolding import *
# from src.main.org.evosuite.runtime.EvoRunnerParameters import *
from src.main.org.apache.commons.validator.routines.ISBNValidator import *

# from src.test.org.apache.commons.validator.routines.ISBNValidator_ESTest_scaffolding import *
# from src.main.org.evosuite.runtime.EvoAssertions import *


class ISBNValidator_ESTest(unittest.TestCase):

    def test10(self) -> None:

        iSBNValidator0 = ISBNValidator.getInstance0()
        string0 = iSBNValidator0.convertToISBN13(None)
        self.assertIsNone(string0)

    def test09(self) -> None:

        ISBNValidator0 = ISBNValidator.ISBNValidator1()
        string0 = ISBNValidator0.validateISBN10("]$KE|h")
        self.assertIsNone(string0)

    def test08(self) -> None:
        iSBNValidator0 = ISBNValidator.getInstance1(True)
        boolean0 = iSBNValidator0.isValid("L&&r7G7F J*w|M_*7")
        self.assertFalse(boolean0)

    def test07(self) -> None:
        iSBNValidator0 = ISBNValidator.getInstance1(False)
        assert iSBNValidator0 is not None

    def test06(self) -> None:

        iSBNValidator0 = ISBNValidator.getInstance1(True)
        string0 = iSBNValidator0.validate("u;Z$EP")
        self.assertIsNone(string0)

    def test05(self) -> None:

        iSBNValidator0 = ISBNValidator.getInstance1(True)
        # Undeclared exception in Java code
        try:
            iSBNValidator0.convertToISBN13("' - ")
            self.fail("Expecting exception: ValueError")

        except ValueError as e:
            # Invalid length 3 for '' -'
            self.verifyException(
                "org.apache.commons.validator.routines.ISBNValidator", e
            )

    def test04(self) -> None:

        iSBNValidator0 = ISBNValidator(False)
        boolean0 = iSBNValidator0.isValidISBN10("`j")
        self.assertFalse(boolean0)

    def test03(self) -> None:

        iSBNValidator0 = ISBNValidator(True)
        boolean0 = iSBNValidator0.isValidISBN13("")
        self.assertFalse(boolean0)

    def test02(self) -> None:
        iSBNValidator0 = ISBNValidator.getInstance0()
        string0 = iSBNValidator0.validateISBN13(",aq2")
        self.assertIsNone(string0)

    def test01(self) -> None:

        ISBNValidator0 = ISBNValidator.ISBNValidator1()

        try:
            ISBNValidator0.convertToISBN13("Check digit error for '")
            self.fail("Expecting exception: ValueError")

        except ValueError as e:
            verifyException("org.apache.commons.validator.routines.ISBNValidator", e)

    def test00(self) -> None:

        iSBNValidator0 = ISBNValidator(True)

        try:
            iSBNValidator0.convertToISBN13("/1b;{)/7N0 ")
            self.fail("Expecting exception: ValueError")

        except ValueError as e:
            # Check digit error for '/1b;{)/7N0' - Invalid Character[4] = '/'
            self.verifyException(
                "org.apache.commons.validator.routines.ISBNValidator", e
            )
