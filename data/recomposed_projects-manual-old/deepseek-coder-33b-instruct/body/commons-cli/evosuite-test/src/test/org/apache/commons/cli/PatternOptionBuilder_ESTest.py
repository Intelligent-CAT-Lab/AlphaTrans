from __future__ import annotations
import time
import re
import urllib
import os
import datetime
import typing
from typing import *
import unittest
import pytest
import io
import unittest
from src.main.org.apache.commons.cli.Options import *
from src.main.org.apache.commons.cli.PatternOptionBuilder import *

# from src.test.org.apache.commons.cli.PatternOptionBuilder_ESTest_scaffolding import *
# from src.main.org.evosuite.runtime.EvoAssertions import *
# from src.main.org.evosuite.runtime.EvoRunnerParameters import *


class PatternOptionBuilder_ESTest(unittest.TestCase):

    def test47(self) -> None:
        patternOptionBuilder0 = PatternOptionBuilder()

    def test46(self) -> None:

        object0 = PatternOptionBuilder.getValueClass("#")
        self.assertIsNotNone(object0)
        self.assertEqual(str(object0), "<class 'datetime.date'>")

    def test45(self) -> None:

        try:
            PatternOptionBuilder.parsePattern("O*$c2v;Beqc")
            self.fail("Expecting exception: ValueError")

        except ValueError as e:
            verifyException("org.apache.commons.cli.OptionValidator", e)

    def test44(self) -> None:

        object0 = PatternOptionBuilder.getValueClass("$")
        self.assertIsNone(object0)

    def test43(self) -> None:

        class0 = PatternOptionBuilder.getValueClass("%")
        self.assertEqual(1025, class0.getModifiers())
        self.assertIsNotNone(class0)

    def test42(self) -> None:

        object0 = PatternOptionBuilder.getValueClass("&")
        self.assertIsNone(object0)

    def test41(self) -> None:

        object0 = PatternOptionBuilder.getValueClass("'")
        self.assertIsNone(object0)

    def test40(self) -> None:

        object0 = PatternOptionBuilder.getValueClass("(")
        self.assertIsNone(object0)

    def test39(self) -> None:

        object0 = PatternOptionBuilder.getValueClass(")")
        self.assertIsNone(object0)

    def test38(self) -> None:

        object0 = PatternOptionBuilder.getValueClass(",")
        self.assertIsNone(object0)

    def test37(self) -> None:

        object0 = PatternOptionBuilder.getValueClass("-")
        self.assertIsNone(object0)

    def test36(self) -> None:

        object0 = PatternOptionBuilder.getValueClass(".")
        self.assertIsNone(object0)

    def test35(self) -> None:

        options0 = PatternOptionBuilder.parsePattern("BS_q/_/")
        self.assertIsNotNone(options0)

    def test34(self) -> None:

        object0 = PatternOptionBuilder.getValueClass("0")
        self.assertIsNone(object0)

    def test33(self) -> None:

        object0 = PatternOptionBuilder.getValueClass("1")
        self.assertIsNone(object0)

    def test32(self) -> None:

        object0 = PatternOptionBuilder.getValueClass("2")
        self.assertIsNone(object0)

    def test31(self) -> None:

        object0 = PatternOptionBuilder.getValueClass("3")
        self.assertIsNone(object0)

    def test30(self) -> None:

        object0 = PatternOptionBuilder.getValueClass("4")
        self.assertIsNone(object0)

    def test29(self) -> None:

        object0 = PatternOptionBuilder.getValueClass("5")
        self.assertIsNone(object0)

    def test28(self) -> None:

        object0 = PatternOptionBuilder.getValueClass("6")
        self.assertIsNone(object0)

    def test27(self) -> None:

        object0 = PatternOptionBuilder.getValueClass("7")
        self.assertIsNone(object0)

    def test26(self) -> None:

        object0 = PatternOptionBuilder.getValueClass("8")
        self.assertIsNone(object0)

    def test25(self) -> None:

        object0 = PatternOptionBuilder.getValueClass("9")
        self.assertIsNone(object0)

    def test24(self) -> None:

        options0 = PatternOptionBuilder.parsePattern(
            "A CloneNotSupportedException was trown: "
        )
        self.assertIsNotNone(options0)

    def test23(self) -> None:

        object0 = PatternOptionBuilder.getValueClass(";")
        self.assertIsNone(object0)

    def test22(self) -> None:

        object0 = PatternOptionBuilder.getValueClass("=")
        self.assertIsNone(object0)

    def test21(self) -> None:

        object0 = PatternOptionBuilder.getValueClass(">")
        self.assertEqual(str(object0), "class java.io.File")
        self.assertIsNotNone(object0)

    def test20(self) -> None:

        object0 = PatternOptionBuilder.getValueClass("?")
        self.assertIsNone(object0)

    def test19(self) -> None:

        object0 = PatternOptionBuilder.getValueClass("j")
        self.assertIsNone(object0)

    def test18(self) -> None:
        boolean0 = PatternOptionBuilder.isValueCode("%")
        self.assertTrue(boolean0)

    def test17(self) -> None:

        options0 = PatternOptionBuilder.parsePattern("#uw17oo*cb69#R8xL*b")
        self.assertIsNotNone(options0)

    def test16(self) -> None:
        boolean0 = PatternOptionBuilder.isValueCode(">")
        self.assertTrue(boolean0)

    def test15(self) -> None:

        class0 = PatternOptionBuilder.getValueClass("*")
        self.assertTrue(class0 is list)
        self.assertIsNotNone(class0)

    def test14(self) -> None:

        object0 = PatternOptionBuilder.getValueClass("/")
        self.assertIsNotNone(object0)
        self.assertEqual(str(object0), "<class 'urllib.parse.ParseResult'>")

    def test13(self) -> None:

        object0 = PatternOptionBuilder.getValueClass("<")
        self.assertIsNotNone(object0)
        self.assertEqual(str(object0), "<class 'io.FileIO'>")

    def test12(self) -> None:

        object0 = PatternOptionBuilder.getValueClass("+")
        self.assertEqual(str(type(object0)), "<class 'type'>")
        self.assertIsNotNone(object0)

    def test11(self) -> None:

        object0 = PatternOptionBuilder.getValueClass(":")
        self.assertEqual(str(object0), "<class 'str'>")
        self.assertIsNotNone(object0)

    def test10(self) -> None:

        object0 = PatternOptionBuilder.getValueClass("@")
        self.assertEqual(str(object0), "<class 'object'>")
        self.assertIsNotNone(object0)

    def test09(self) -> None:
        boolean0 = PatternOptionBuilder.isValueCode("*")
        self.assertTrue(boolean0)

    def test08(self) -> None:
        boolean0 = PatternOptionBuilder.isValueCode("+")
        self.assertTrue(boolean0)

    def test07(self) -> None:
        boolean0 = PatternOptionBuilder.isValueCode("'")
        self.assertFalse(boolean0)

    def test06(self) -> None:
        boolean0 = PatternOptionBuilder.isValueCode("@")
        self.assertTrue(boolean0)

    def test05(self) -> None:
        boolean0 = PatternOptionBuilder.isValueCode("/")
        self.assertTrue(boolean0)

    def test04(self) -> None:
        boolean0 = PatternOptionBuilder.isValueCode("#")
        self.assertTrue(boolean0)

    def test03(self) -> None:
        boolean0 = PatternOptionBuilder.isValueCode("@")
        self.assertTrue(boolean0)

    def test02(self) -> None:
        boolean0 = PatternOptionBuilder.isValueCode("<")
        self.assertTrue(boolean0)

    def test01(self) -> None:
        boolean0 = PatternOptionBuilder.isValueCode(":")
        self.assertTrue(boolean0)

    def test00(self) -> None:

        try:
            PatternOptionBuilder.parsePattern(None)
            self.fail("Expecting exception: RuntimeError")

        except TypeError as e:
            self.verifyException("org.apache.commons.cli.PatternOptionBuilder", e)
