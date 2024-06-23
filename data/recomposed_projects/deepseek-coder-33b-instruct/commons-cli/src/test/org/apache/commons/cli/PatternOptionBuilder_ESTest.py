from __future__ import annotations
import re
import urllib
import unittest
import pytest
import io
import unittest
from src.main.org.apache.commons.cli.Options import *
from src.main.org.apache.commons.cli.PatternOptionBuilder import *

# from src.main.org.apache.commons.cli.PatternOptionBuilder_ESTest_scaffolding import *
# from src.main.org.evosuite.runtime.EvoAssertions import *
# from src.main.org.evosuite.runtime.EvoRunnerParameters import *


class PatternOptionBuilder_ESTest(unittest.TestCase):

    @pytest.mark.test
    def test47(self) -> None:
        patternOptionBuilder0 = PatternOptionBuilder()

    @pytest.mark.test
    def test46(self) -> None:

        object0 = PatternOptionBuilder.getValueClass("#")
        self.assertEqual(str(object0), "<class 'datetime.date'>")
        self.assertIsNotNone(object0)

    @pytest.mark.test
    def test45(self) -> None:

        object0 = PatternOptionBuilder.getValueClass("$")
        self.assertIsNone(object0)

    @pytest.mark.test
    def test44(self) -> None:

        object0 = PatternOptionBuilder.getValueClass("&")
        self.assertIsNone(object0)

    @pytest.mark.test
    def test43(self) -> None:

        object0 = PatternOptionBuilder.getValueClass("'")
        self.assertIsNone(object0)

    @pytest.mark.test
    def test42(self) -> None:

        object0 = PatternOptionBuilder.getValueClass("(")
        self.assertIsNone(object0)

    @pytest.mark.test
    def test41(self) -> None:

        object0 = PatternOptionBuilder.getValueClass(")")
        self.assertIsNone(object0)

    @pytest.mark.test
    def test40(self) -> None:

        object0 = PatternOptionBuilder.getValueClass(",")
        self.assertIsNone(object0)

    @pytest.mark.test
    def test39(self) -> None:

        object0 = PatternOptionBuilder.getValueClass("-")
        self.assertIsNone(object0)

    @pytest.mark.test
    def test38(self) -> None:

        object0 = PatternOptionBuilder.getValueClass(".")
        self.assertIsNone(object0)

    @pytest.mark.test
    def test37(self) -> None:

        options0 = PatternOptionBuilder.parsePattern("<nkC/4TA")
        self.assertIsNotNone(options0)

    @pytest.mark.test
    def test36(self) -> None:

        object0 = PatternOptionBuilder.getValueClass("0")
        self.assertIsNone(object0)

    @pytest.mark.test
    def test35(self) -> None:

        object0 = PatternOptionBuilder.getValueClass("1")
        self.assertIsNone(object0)

    @pytest.mark.test
    def test34(self) -> None:

        object0 = PatternOptionBuilder.getValueClass("2")
        self.assertIsNone(object0)

    @pytest.mark.test
    def test33(self) -> None:

        object0 = PatternOptionBuilder.getValueClass("3")
        self.assertIsNone(object0)

    @pytest.mark.test
    def test32(self) -> None:

        object0 = PatternOptionBuilder.getValueClass("4")
        self.assertIsNone(object0)

    @pytest.mark.test
    def test31(self) -> None:

        object0 = PatternOptionBuilder.getValueClass("5")
        self.assertIsNone(object0)

    @pytest.mark.test
    def test30(self) -> None:

        object0 = PatternOptionBuilder.getValueClass("6")
        self.assertIsNone(object0)

    @pytest.mark.test
    def test29(self) -> None:

        object0 = PatternOptionBuilder.getValueClass("7")
        self.assertIsNone(object0)

    @pytest.mark.test
    def test28(self) -> None:

        object0 = PatternOptionBuilder.getValueClass("8")
        self.assertIsNone(object0)

    @pytest.mark.test
    def test27(self) -> None:

        object0 = PatternOptionBuilder.getValueClass("9")
        self.assertIsNone(object0)

    @pytest.mark.test
    def test26(self) -> None:

        object0 = PatternOptionBuilder.getValueClass(";")
        self.assertIsNone(object0)

    @pytest.mark.test
    def test25(self) -> None:

        object0 = PatternOptionBuilder.getValueClass("=")
        self.assertIsNone(object0)

    @pytest.mark.test
    def test24(self) -> None:

        object0 = PatternOptionBuilder.getValueClass("?")
        self.assertIsNone(object0)

    @pytest.mark.test
    def test23(self) -> None:

        object0 = PatternOptionBuilder.getValueClass("o")
        self.assertIsNone(object0)

    @pytest.mark.test
    def test22(self) -> None:

        try:
            PatternOptionBuilder.parsePattern("+#u0J|efG*Qp12iE")
            self.fail("Expecting exception: ValueError")

        except ValueError as e:
            verifyException("org.apache.commons.cli.OptionValidator", e)

    @pytest.mark.test
    def test21(self) -> None:

        options0 = PatternOptionBuilder.parsePattern(
            "A CloneNotSupportedException was thrown: "
        )
        self.assertIsNotNone(options0)

    @pytest.mark.test
    def test20(self) -> None:

        options0 = PatternOptionBuilder.parsePattern("deo9g@")
        self.assertIsNotNone(options0)

    @pytest.mark.test
    def test19(self) -> None:

        object0 = PatternOptionBuilder.getValueClass("*")
        self.assertIsNotNone(object0)
        self.assertEqual(str(object0), "class [Ljava.io.File;")

    @pytest.mark.test
    def test18(self) -> None:

        object0 = PatternOptionBuilder.getValueClass(">")
        self.assertIsNotNone(object0)
        self.assertEqual(str(object0), "<class 'pathlib.Path'>")

    @pytest.mark.test
    def test17(self) -> None:

        object0 = PatternOptionBuilder.getValueClass("/")
        self.assertEqual(str(object0), "<class 'urllib.parse.ParseResult'>")
        self.assertIsNotNone(object0)

    @pytest.mark.test
    def test16(self) -> None:

        object0 = PatternOptionBuilder.getValueClass("<")
        self.assertEqual(str(object0), "<class 'io.FileIO'>")
        self.assertIsNotNone(object0)

    @pytest.mark.test
    def test15(self) -> None:

        object0 = PatternOptionBuilder.getValueClass("+")
        self.assertIsNotNone(object0)
        self.assertEqual(str(type(object0)), "<class 'type'>")

    @pytest.mark.test
    def test14(self) -> None:

        object0 = PatternOptionBuilder.getValueClass("%")
        self.assertIsNotNone(object0)
        self.assertEqual(str(object0), "<class 'numbers.Number'>")

    @pytest.mark.test
    def test13(self) -> None:

        object0 = PatternOptionBuilder.getValueClass(":")
        self.assertEqual(str(object0), "<class 'str'>")
        self.assertIsNotNone(object0)

    @pytest.mark.test
    def test12(self) -> None:

        object0 = PatternOptionBuilder.getValueClass("@")
        self.assertEqual(str(object0), "<class 'object'>")
        self.assertIsNotNone(object0)

    @pytest.mark.test
    def test11(self) -> None:
        boolean0 = PatternOptionBuilder.isValueCode("*")
        self.assertTrue(boolean0)

    @pytest.mark.test
    def test10(self) -> None:
        boolean0 = PatternOptionBuilder.isValueCode("+")
        self.assertTrue(boolean0)

    @pytest.mark.test
    def test09(self) -> None:
        boolean0 = PatternOptionBuilder.isValueCode(")")
        self.assertFalse(boolean0)

    @pytest.mark.test
    def test08(self) -> None:
        boolean0 = PatternOptionBuilder.isValueCode("@")
        self.assertTrue(boolean0)

    @pytest.mark.test
    def test07(self) -> None:
        boolean0 = PatternOptionBuilder.isValueCode("/")
        self.assertTrue(boolean0)

    @pytest.mark.test
    def test06(self) -> None:
        boolean0 = PatternOptionBuilder.isValueCode(">")
        self.assertTrue(boolean0)

    @pytest.mark.test
    def test05(self) -> None:
        boolean0 = PatternOptionBuilder.isValueCode("#")
        self.assertTrue(boolean0)

    @pytest.mark.test
    def test04(self) -> None:
        boolean0 = PatternOptionBuilder.isValueCode("@")
        self.assertTrue(boolean0)

    @pytest.mark.test
    def test03(self) -> None:
        boolean0 = PatternOptionBuilder.isValueCode("<")
        self.assertTrue(boolean0)

    @pytest.mark.test
    def test02(self) -> None:
        boolean0 = PatternOptionBuilder.isValueCode(":")
        self.assertTrue(boolean0)

    @pytest.mark.test
    def test01(self) -> None:
        boolean0 = PatternOptionBuilder.isValueCode("%")
        self.assertTrue(boolean0)

    @pytest.mark.test
    def test00(self) -> None:

        try:
            PatternOptionBuilder.parsePattern(None)
            self.fail("Expecting exception: NullPointerException")

        except TypeError as e:
            self.verifyException("org.apache.commons.cli.PatternOptionBuilder", e)
