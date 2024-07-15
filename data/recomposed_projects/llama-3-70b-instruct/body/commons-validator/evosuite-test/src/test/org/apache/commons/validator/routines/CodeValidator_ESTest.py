from __future__ import annotations
import time
import re
import os
import numbers
import unittest
import pytest
import io
import unittest
from src.main.org.apache.commons.validator.routines.CodeValidator import *

# from src.test.org.apache.commons.validator.routines.CodeValidator_ESTest_scaffolding import *
from src.main.org.apache.commons.validator.routines.RegexValidator import *
from src.main.org.apache.commons.validator.routines.checkdigit.ABANumberCheckDigit import *
from src.main.org.apache.commons.validator.routines.checkdigit.CUSIPCheckDigit import *
from src.main.org.apache.commons.validator.routines.checkdigit.CheckDigit import *
from src.main.org.apache.commons.validator.routines.checkdigit.EAN13CheckDigit import *
from src.main.org.apache.commons.validator.routines.checkdigit.ISBN10CheckDigit import *
from src.main.org.apache.commons.validator.routines.checkdigit.ISBNCheckDigit import *
from src.main.org.apache.commons.validator.routines.checkdigit.LuhnCheckDigit import *
from src.main.org.apache.commons.validator.routines.checkdigit.ModulusTenCheckDigit import *
from src.main.org.apache.commons.validator.routines.checkdigit.VerhoeffCheckDigit import *

# from src.main.org.evosuite.runtime.EvoAssertions import *
# from src.main.org.evosuite.runtime.EvoRunnerParameters import *


class CodeValidator_ESTest(unittest.TestCase):

    def test27(self) -> None:

        pass  # LLM could not translate this method

    def test26(self) -> None:

        codeValidator0 = CodeValidator.CodeValidator5("", None)
        codeValidator0.getCheckDigit()
        self.assertEqual(-1, codeValidator0.getMaxLength())
        self.assertEqual(-1, codeValidator0.getMinLength())

    def test25(self) -> None:

        codeValidator0 = CodeValidator.CodeValidator5("%d", None)
        int0 = codeValidator0.getMaxLength()
        self.assertEqual(-1, int0)
        self.assertEqual(-1, codeValidator0.getMinLength())

    def test24(self) -> None:

        codeValidator0 = CodeValidator.CodeValidator5("%d", None)
        regexValidator0 = codeValidator0.getRegexValidator()
        self.assertIsNotNone(regexValidator0)
        self.assertEqual(-1, codeValidator0.getMaxLength())
        self.assertEqual(-1, codeValidator0.getMinLength())

    def test23(self) -> None:

        regexValidator0 = RegexValidator(["#_~uw"], False)
        codeValidator0 = CodeValidator.CodeValidator1(
            regexValidator0, -2353, ISBNCheckDigit()
        )
        self.assertEqual(-2353, codeValidator0.getMinLength())
        self.assertEqual(-2353, codeValidator0.getMaxLength())

    def test22(self) -> None:

        verhoeffCheckDigit0 = VerhoeffCheckDigit.VERHOEFF_CHECK_DIGIT
        codeValidator0 = CodeValidator.CodeValidator4("", 3, verhoeffCheckDigit0)
        int0 = codeValidator0.getMinLength()
        self.assertEqual(3, int0)
        self.assertEqual(3, codeValidator0.getMaxLength())

    def test21(self) -> None:

        luhnCheckDigit0 = LuhnCheckDigit()
        codeValidator0 = CodeValidator.CodeValidator5(None, luhnCheckDigit0)
        codeValidator0.validate(None)
        self.assertEqual(-1, codeValidator0.getMaxLength())
        self.assertEqual(-1, codeValidator0.getMinLength())

    def test20(self) -> None:

        iSBNCheckDigit0 = ISBNCheckDigit()
        stringArray0 = ["#_~uw"]
        regexValidator0 = RegexValidator(stringArray0, False)
        codeValidator0 = CodeValidator(
            0,
            iSBNCheckDigit0,
            1,
            regexValidator0,
            0,
            "org.apache.commons.validator.routines.CodeValidator",
        )
        boolean0 = codeValidator0.isValid("#_~uw")
        self.assertEqual(0, codeValidator0.getMinLength())
        self.assertFalse(boolean0)
        self.assertEqual(1, codeValidator0.getMaxLength())

    def test19(self) -> None:

        code_validator0 = CodeValidator.CodeValidator5("%d", None)
        boolean0 = code_validator0.isValid("%d")
        self.assertEqual(-1, code_validator0.getMinLength())
        self.assertEqual(-1, code_validator0.getMaxLength())
        self.assertTrue(boolean0)

    def test18(self) -> None:

        verhoeffCheckDigit0 = VerhoeffCheckDigit()
        codeValidator0 = CodeValidator.CodeValidator5("", verhoeffCheckDigit0)
        object0 = codeValidator0.validate("0")
        self.assertEqual(-1, codeValidator0.getMinLength())
        self.assertIsNotNone(object0)
        self.assertEqual(-1, codeValidator0.getMaxLength())

    def test17(self) -> None:

        iSBNCheckDigit0 = ISBNCheckDigit()
        stringArray0 = ["#_~uw"]
        regexValidator0 = RegexValidator(stringArray0, False)
        codeValidator0 = CodeValidator(
            0,
            iSBNCheckDigit0,
            1,
            regexValidator0,
            0,
            "org.apache.commons.validator.routines.CodeValidator",
        )
        codeValidator0.validate("org.apache.commons.validator.routines.CodeValidator")
        self.assertEqual(1, codeValidator0.getMaxLength())
        self.assertEqual(0, codeValidator0.getMinLength())

    def test16(self) -> None:

        pass  # LLM could not translate this method

    def test15(self) -> None:

        pass  # LLM could not translate this method

    def test14(self) -> None:

        iSBNCheckDigit0 = ISBNCheckDigit()
        codeValidator0 = None
        try:
            codeValidator0 = CodeValidator(
                0, iSBNCheckDigit0, -4376, None, -4376, "9|/)@L"
            )
            self.fail("Expecting exception: PatternSyntaxException")

        except PatternSyntaxException as e:
            self.verifyException("java.util.regex.Pattern", e)

    def test13(self) -> None:

        codeValidator0 = CodeValidator(98, None, 98, None, -153, None)
        self.assertEqual(98, codeValidator0.getMaxLength())
        self.assertEqual(-153, codeValidator0.getMinLength())

    def test12(self) -> None:

        aBANumberCheckDigit0 = ABANumberCheckDigit()
        regexValidator0 = RegexValidator.RegexValidator2("ofA_jvDqiKl]", False)
        codeValidator0 = CodeValidator(
            98, aBANumberCheckDigit0, 98, regexValidator0, 98, ""
        )
        self.assertEqual(98, codeValidator0.getMaxLength())
        self.assertEqual(98, codeValidator0.getMinLength())

    def test11(self) -> None:

        luhnCheckDigit0 = LuhnCheckDigit()
        codeValidator0 = CodeValidator.CodeValidator5("", luhnCheckDigit0)
        codeValidator0.validate("")
        self.assertEqual(-1, codeValidator0.getMinLength())
        self.assertEqual(-1, codeValidator0.getMaxLength())

    def test10(self) -> None:

        codeValidator0 = CodeValidator.CodeValidator5("4<J", None)
        object0 = codeValidator0.validate("4<J")
        self.assertEqual(-1, codeValidator0.getMaxLength())
        self.assertIsNotNone(object0)
        self.assertEqual("", object0)
        self.assertEqual(-1, codeValidator0.getMinLength())

    def test09(self) -> None:

        iSBNCheckDigit0 = ISBNCheckDigit.ISBN_CHECK_DIGIT
        try:
            CodeValidator.CodeValidator4('~"@8 m1+~XkJ)K', 4697, iSBNCheckDigit0)
            self.fail("Expecting exception: PatternSyntaxException")

        except PatternSyntaxException as e:
            verifyException("java.util.regex.Pattern", e)

    def test08(self) -> None:

        iSBNCheckDigit0 = ISBNCheckDigit.ISBN_CHECK_DIGIT
        try:
            CodeValidator.CodeValidator5("Regular expression[", iSBNCheckDigit0)
            self.fail("Expecting exception: PatternSyntaxException")

        except re.error as e:
            self.verifyException("java.util.regex.Pattern", e)

    def test07(self) -> None:

        iSBNCheckDigit0 = ISBNCheckDigit()
        codeValidator0 = CodeValidator.CodeValidator1(None, 0, iSBNCheckDigit0)
        int0 = codeValidator0.getMaxLength()
        self.assertEqual(0, int0)
        self.assertEqual(0, codeValidator0.getMinLength())

    def test06(self) -> None:

        aBANumberCheckDigit0 = ABANumberCheckDigit()
        codeValidator0 = CodeValidator.CodeValidator4(None, -1007, aBANumberCheckDigit0)
        self.assertEqual(-1007, codeValidator0.getMinLength())
        self.assertEqual(-1007, codeValidator0.getMaxLength())

    def test05(self) -> None:

        luhnCheckDigit0 = LuhnCheckDigit()
        codeValidator0 = CodeValidator.CodeValidator1(None, 2959, luhnCheckDigit0)
        codeValidator0.getCheckDigit()
        self.assertEqual(2959, codeValidator0.getMaxLength())
        self.assertEqual(2959, codeValidator0.getMinLength())

    def test04(self) -> None:

        pass  # LLM could not translate this method

    def test03(self) -> None:

        ISBN10CheckDigit0 = ISBN10CheckDigit.ISBN10_CHECK_DIGIT
        codeValidator0 = CodeValidator.CodeValidator5(
            "|nK^Q9LO0;,:i", ISBN10CheckDigit0
        )
        int0 = codeValidator0.getMinLength()
        self.assertEqual((-1), int0)
        self.assertEqual((-1), codeValidator0.getMaxLength())

    def test02(self) -> None:

        pass  # LLM could not translate this method

    def test01(self) -> None:

        code_validator0 = CodeValidator.CodeValidator5("", None)
        code_validator0.getRegexValidator()
        self.assertEqual(-1, code_validator0.getMinLength())
        self.assertEqual(-1, code_validator0.getMaxLength())

    def test00(self) -> None:

        regexValidator0 = RegexValidator.RegexValidator2("Invalid Code Length = ", True)
        eAN13CheckDigit0 = ISBNCheckDigit.ISBN13_CHECK_DIGIT
        codeValidator0 = CodeValidator.CodeValidator2(regexValidator0, eAN13CheckDigit0)
        boolean0 = codeValidator0.isValid("Invalid Code Length = ")
        self.assertEqual(-1, codeValidator0.getMinLength())
        self.assertFalse(boolean0)
        self.assertEqual(-1, codeValidator0.getMaxLength())
