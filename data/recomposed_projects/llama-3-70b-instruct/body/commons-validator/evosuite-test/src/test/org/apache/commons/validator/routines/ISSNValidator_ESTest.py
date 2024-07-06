from __future__ import annotations
import time
import re
import os
import unittest
import pytest
import io
import unittest
from src.main.org.apache.commons.validator.routines.ISSNValidator import *

# from src.test.org.apache.commons.validator.routines.ISSNValidator_ESTest_scaffolding import *
# from src.main.org.evosuite.runtime.EvoAssertions import *
# from src.main.org.evosuite.runtime.EvoRunnerParameters import *


class ISSNValidator_ESTest(unittest.TestCase):

    def test9(self) -> None:

        iSSNValidator0 = ISSNValidator()
        object0 = iSSNValidator0.validate("DFa8n[o!!mzU+B-")
        self.assertIsNone(object0)

    def test8(self) -> None:

        iSSNValidator0 = ISSNValidator()
        boolean0 = iSSNValidator0.isValid(None)
        self.assertFalse(boolean0)

    def test7(self) -> None:

        iSSNValidator0 = ISSNValidator()
        object0 = iSSNValidator0.validateEan("T~wOJr|t9GHP")
        self.assertIsNone(object0)

    def test6(self) -> None:

        iSSNValidator0 = ISSNValidator.getInstance()
        # Undeclared exception in Java
        try:
            iSSNValidator0.convertToEAN13("2UFxk<.Udl", "2UFxk<.Udl")
            self.fail("Expecting exception: ValueError")

        except ValueError as e:
            # Suffix must be two digits: '2UFxk<.Udl'
            self.assertEqual(str(e), "Suffix must be two digits: '2UFxk<.Udl'")

    def test5(self) -> None:

        iSSNValidator0 = ISSNValidator()
        try:
            iSSNValidator0.extractFromEAN13(";WlmbW'T0_cf ")
            self.fail("Expecting exception: ValueError")

        except ValueError as e:
            self.assertTrue(
                "Prefix must be 977 to contain an ISSN: ';WlmbW'T0_cf '" in str(e)
            )

    def test4(self) -> None:

        iSSNValidator0 = ISSNValidator()
        try:
            iSSNValidator0.extractFromEAN13("E@3/HhLeRFq'%O1N[/")
            self.fail("Expecting exception: ValueError")

        except ValueError as e:
            verifyException("org.apache.commons.validator.routines.ISSNValidator", e)

    def test3(self) -> None:

        iSSNValidator0 = ISSNValidator.getInstance()
        # Undeclared exception
        try:
            iSSNValidator0.extractFromEAN13(None)
            self.fail("Expecting exception: RuntimeError")

        except Exception as e:
            # no message in exception (getMessage() returned null)
            self.verifyException(
                "org.apache.commons.validator.routines.ISSNValidator", e
            )

    def test2(self) -> None:

        iSSNValidator0 = ISSNValidator.getInstance()
        string0 = iSSNValidator0.convertToEAN13("X#NFDIn", "00")
        self.assertIsNone(string0)

    def test1(self) -> None:

        iSSNValidator0 = ISSNValidator.getInstance()
        # Undeclared exception in Java
        try:
            iSSNValidator0.convertToEAN13("R>?Vp:25SO][{uFz96", None)
            self.fail("Expecting exception: ValueError")

        except ValueError as e:
            # Suffix must be two digits: 'null'
            self.assertEqual(str(e), "Suffix must be two digits: 'None'")

    def test0(self) -> None:

        iSSNValidator0 = ISSNValidator()
        try:
            iSSNValidator0.extractFromEAN13(" for '")
            self.fail("Expecting exception: ValueError")

        except ValueError as e:
            self.assertTrue("Invalid length 5 for 'for ''" in str(e))
