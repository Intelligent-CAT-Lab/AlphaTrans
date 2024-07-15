from __future__ import annotations
import time
import re
import os
import typing
from typing import *
import pathlib
import unittest
import pytest
import io
import unittest
from src.main.org.apache.commons.validator.UrlValidator import *

# from src.test.org.apache.commons.validator.UrlValidator_ESTest_scaffolding import *
# from src.main.org.evosuite.runtime.EvoAssertions import *
# from src.main.org.evosuite.runtime.EvoRunnerParameters import *


class UrlValidator_ESTest(unittest.TestCase):

    def test22(self) -> None:

        urlValidator0 = UrlValidator.UrlValidator1((-9))
        boolean0 = urlValidator0.isValidPath("")
        self.assertTrue(boolean0)

    def test21(self) -> None:

        urlValidator0 = UrlValidator.UrlValidator3()
        # Undeclared exception
        try:
            urlValidator0.isValid("bh")
            # fail("Expecting exception: RuntimeError")
            # Unstable assertion
        except RuntimeError as e:
            # No match found
            # verifyException("java.util.regex.Matcher", e)
            pass

    def test20(self) -> None:

        stringArray0 = [""]
        urlValidator0 = UrlValidator(stringArray0, -2372)
        boolean0 = urlValidator0.isValidScheme("xn--e1a4c")
        self.assertFalse(boolean0)

    def test19(self) -> None:

        urlValidator0 = UrlValidator.UrlValidator3()
        boolean0 = urlValidator0.isValid(None)
        self.assertFalse(boolean0)

    def test18(self) -> None:

        urlValidator0 = UrlValidator.UrlValidator3()
        boolean0 = urlValidator0.isValid("")
        self.assertFalse(boolean0)

    def test17(self) -> None:

        urlValidator0 = UrlValidator.UrlValidator3()
        boolean0 = urlValidator0._isValidScheme(None)
        self.assertFalse(boolean0)

    def test16(self) -> None:

        stringArray0 = [""]
        urlValidator0 = UrlValidator(stringArray0, -2372)
        boolean0 = urlValidator0.isValidScheme("`:")
        self.assertFalse(boolean0)

    def test15(self) -> None:

        urlValidator0 = UrlValidator.UrlValidator1(1)
        boolean0 = urlValidator0._isValidScheme("xn--e1a4c")
        self.assertTrue(boolean0)

    def test14(self) -> None:

        stringArray0 = ["xn--e1a4c"]
        urlValidator0 = UrlValidator(stringArray0, (-2372))
        boolean0 = urlValidator0.isValidScheme("xn--e1a4c")
        self.assertTrue(boolean0)

    def test13(self) -> None:

        urlValidator0 = UrlValidator.UrlValidator3()
        # Undeclared exception
        try:
            urlValidator0._isValidAuthority("")
            # fail("Expecting exception: RuntimeError")
            # Unstable assertion
        except Exception as e:
            # No match found
            # verifyException("java.util.regex.Matcher", e)
            self.assertIsInstance(e, RuntimeError)

    def test12(self) -> None:

        urlValidator0 = UrlValidator.UrlValidator3()
        boolean0 = urlValidator0._isValidAuthority(None)
        self.assertFalse(boolean0)

    def test11(self) -> None:

        urlValidator0 = UrlValidator.UrlValidator3()
        boolean0 = urlValidator0._isValidPath("")
        self.assertTrue(boolean0)

    def test10(self) -> None:

        urlValidator0 = UrlValidator.UrlValidator3()
        boolean0 = urlValidator0._isValidPath(None)
        self.assertFalse(boolean0)

    def test09(self) -> None:

        stringArray0 = ["stringArray0"]
        urlValidator0 = UrlValidator(stringArray0, -2372)
        boolean0 = urlValidator0.isValidPath("xn--e1a4c")
        self.assertFalse(boolean0)

    def test08(self) -> None:

        urlValidator0 = UrlValidator(None, 0)
        boolean0 = urlValidator0._isValidQuery("LpnAp+Bwe")
        self.assertTrue(boolean0)

    def test07(self) -> None:

        urlValidator0 = UrlValidator.UrlValidator3()
        boolean0 = urlValidator0._isValidQuery(None)
        self.assertTrue(boolean0)

    def test06(self) -> None:

        urlValidator0 = UrlValidator(None, 0)
        boolean0 = urlValidator0._isValidFragment(None)
        self.assertTrue(boolean0)

    def test05(self) -> None:

        urlValidator0 = UrlValidator(None, 0)
        int0 = urlValidator0._countToken("N`:C", "N`:C")
        self.assertEqual(1, int0)

    def test04(self) -> None:
        urlValidator0 = UrlValidator.UrlValidator2(None)
        self.assertEqual(2, UrlValidator.ALLOW_2_SLASHES)

    def test03(self) -> None:

        urlValidator0 = UrlValidator.UrlValidator3()
        # Undeclared exception in Java code
        try:
            urlValidator0._countToken(None, None)
            self.fail("Expecting exception: RuntimeError")

        except TypeError as e:
            # no message in exception (getMessage() returned null)
            pass

    def test01(self) -> None:

        urlValidator0 = UrlValidator(None, 697)
        int0 = urlValidator0._countToken("cG$", "q\u00078#Yzdzx")
        self.assertEqual(0, int0)

    def test00(self) -> None:
        urlValidator0 = UrlValidator.UrlValidator1(4)
        boolean0 = urlValidator0._isValidFragment("C.)PG+(ux2DgJjGym(")
        self.assertFalse(boolean0)
