from __future__ import annotations
import time
import re
import os
import unittest
import pytest
import io
import unittest
from src.main.org.apache.commons.validator.routines.RegexValidator import *

# from src.test.org.apache.commons.validator.routines.RegexValidator_ESTest_scaffolding import *
# from src.main.org.evosuite.runtime.EvoAssertions import *
# from src.main.org.evosuite.runtime.EvoRunnerParameters import *


class RegexValidator_ESTest(unittest.TestCase):

    def test21(self) -> None:

        stringArray0 = []
        try:
            RegexValidator.RegexValidator1(stringArray0)
            self.fail("Expecting exception: ValueError")

        except ValueError as e:
            verifyException("org.apache.commons.validator.routines.RegexValidator", e)

    def test20(self) -> None:

        # Undeclared exception
        try:
            RegexValidator.RegexValidator2("(vcjCCBL", False)
            self.fail("Expecting exception: PatternSyntaxException")

        except re.error as e:
            # Unclosed group near index 9
            # (vcjCCBL
            #
            self.verifyException("re", e)

    def test19(self) -> None:

        # Undeclared exception
        try:
            RegexValidator.RegexValidator3("")
            self.fail("Expecting exception: ValueError")

        except ValueError as e:
            # Regular expression is missing
            self.assertEqual(str(e), "Regular expression is missing")

    def test18(self) -> None:

        stringArray0 = [None] * 4
        stringArray0[0] = "5<o;P~aV;"
        stringArray0[1] = "D9Ak13,T7ZX"
        stringArray0[2] = "RtvW"
        stringArray0[3] = "jQ/JY'Xg~_w]4< "
        regexValidator0 = RegexValidator(stringArray0, True)
        boolean0 = regexValidator0.isValid("Regular expression[")
        self.assertFalse(boolean0)

    def test17(self) -> None:

        stringArray0 = [None] * 4
        stringArray0[0] = "5<o;P~aV;"
        stringArray0[1] = "D9Ak13,T7ZX"
        stringArray0[2] = "RtvW"
        stringArray0[3] = "jQ/JY'Xg~_w]4< "
        regexValidator0 = RegexValidator(stringArray0, True)
        boolean0 = regexValidator0.isValid(None)
        self.assertFalse(boolean0)

    def test16(self) -> None:

        regexValidator0 = RegexValidator.RegexValidator3('-Ei"GMfjnI~b2X;,')
        boolean0 = regexValidator0.isValid('-Ei"GMfjnI~b2X;,')
        self.assertTrue(boolean0)

    def test15(self) -> None:

        stringArray0 = [None] * 4
        stringArray0[0] = "5<o;P~aV;"
        stringArray0[1] = "D9Ak13,T7ZX"
        stringArray0[2] = "RtvW"
        stringArray0[3] = "jQ/JY'Xg~_w]4< "
        regexValidator0 = RegexValidator(stringArray0, True)
        stringArray1 = regexValidator0.match("iCc")
        self.assertIsNone(stringArray1)

    def test14(self) -> None:

        regexValidator0 = RegexValidator.RegexValidator3('-Ei"GMfjnI~b2X;,')
        stringArray0 = regexValidator0.match(None)
        self.assertIsNone(stringArray0)

    def test13(self) -> None:

        stringArray0 = [None] * 4
        stringArray0[0] = "lr@6&yw^jRv"
        stringArray0[1] = "X#PPioi<bK<Gg_]_v"
        stringArray0[2] = "3"
        stringArray0[3] = '-Ei"GMfjnI~b2X;,'
        regexValidator0 = RegexValidator(stringArray0, True)
        stringArray1 = regexValidator0.match('-Ei"GMfjnI~b2X;,')
        self.assertIsNotNone(stringArray1)
        self.assertEqual(0, len(stringArray1))

    def test12(self) -> None:

        stringArray0 = [None] * 4
        stringArray0[0] = "5<o;P~aV;"
        stringArray0[1] = "D9Ak13,T7ZX"
        stringArray0[2] = "RtvW"
        stringArray0[3] = "jQ/JY'Xg~_w]4< "
        regexValidator0 = RegexValidator(stringArray0, True)
        string0 = regexValidator0.validate("D9Ak13,T7ZX")
        self.assertEqual("", string0)

    def test11(self) -> None:

        regexValidator0 = RegexValidator.RegexValidator3(",")
        string0 = regexValidator0.validate(None)
        self.assertIsNone(string0)

    def test10(self) -> None:

        regexValidator0 = RegexValidator.RegexValidator3("F+6kta]M")
        string0 = regexValidator0.validate("F+6kta]M")
        self.assertIsNone(string0)

    def test09(self) -> None:

        stringArray0 = ['-Ei"GMfjnI~b2X;,', '-Ei"GMfjnI~b2X;,']
        regexValidator0 = RegexValidator.RegexValidator1(stringArray0)
        string0 = regexValidator0.toString()
        self.assertEqual('RegexValidator{-Ei"GMfjnI~b2X;,,-Ei"GMfjnI~b2X;,}', string0)

    def test08(self) -> None:

        stringArray0 = []
        regexValidator0 = None

        try:
            regexValidator0 = RegexValidator(stringArray0, True)
            self.fail("Expecting exception: ValueError")

        except ValueError as e:
            # Regular expressions are missing
            self.assertEqual(str(e), "Regular expressions are missing")

    def test07(self) -> None:

        regexValidator0 = None
        try:
            regexValidator0 = RegexValidator(None, True)
            self.fail("Expecting exception: ValueError")

        except ValueError as e:
            # Regular expressions are missing
            self.assertEqual(str(e), "Regular expressions are missing")

    def test06(self) -> None:

        stringArray0 = [""]
        regexValidator0 = None

        try:
            regexValidator0 = RegexValidator(stringArray0, False)
            self.fail("Expecting exception: ValueError")

        except ValueError as e:
            self.assertEqual(str(e), "Regular expression[0] is missing")

    def test05(self) -> None:

        stringArray0 = [None] * 6
        stringArray0[0] = "] is missing"
        stringArray0[1] = ""
        regexValidator0 = None

        try:
            regexValidator0 = RegexValidator(stringArray0, False)
            self.fail("Expecting exception: ValueError")

        except ValueError as e:
            self.assertEqual(str(e), "Regular expression[1] is missing")

    def test04(self) -> None:

        stringArray0 = [""] * 1
        stringArray0[0] = "(vcjCCBL"
        regexValidator0 = None

        try:
            regexValidator0 = RegexValidator(stringArray0, False)
            self.fail("Expecting exception: PatternSyntaxException")

        except re.error as e:
            # Unclosed group near index 9
            # (vcjCCBL
            #
            self.verifyException("java.util.regex.Pattern", e)

    def test03(self) -> None:

        stringArray0 = [""] * 3
        stringArray0[0] = "C)"

        with pytest.raises(re.error) as e:
            RegexValidator.RegexValidator1(stringArray0)

        assert str(e.value) == "unterminated character set at position 0"

    def test02(self) -> None:

        # Undeclared exception
        try:
            RegexValidator.RegexValidator2("", False)
            self.fail("Expecting exception: ValueError")

        except ValueError as e:
            # Regular expression[0] is missing
            self.assertEqual(str(e), "Regular expression is missing")

    def test01(self) -> None:

        # Undeclared exception
        try:
            RegexValidator.RegexValidator3("#ygk8#)0Ge.")
            self.fail("Expecting exception: PatternSyntaxException")

        except re.error as e:
            # Unmatched closing ')' near index 5
            # #ygk8#)0Ge.
            #      ^
            self.verifyException("re", e)

    def test00(self) -> None:

        regexValidator0 = RegexValidator.RegexValidator2(",", True)
        self.assertIsNotNone(regexValidator0)
