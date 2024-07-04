from __future__ import annotations
import time
import re
import os
import typing
from typing import *
import unittest
import pytest
import io
import unittest
from src.main.org.apache.commons.validator.routines.InetAddressValidator import *

# from src.test.org.apache.commons.validator.routines.InetAddressValidator_ESTest_scaffolding import *
# from src.main.org.evosuite.runtime.EvoAssertions import *
# from src.main.org.evosuite.runtime.EvoRunnerParameters import *


class InetAddressValidator_ESTest(unittest.TestCase):

    def test18(self) -> None:

        inetAddressValidator0 = InetAddressValidator.getInstance()
        boolean0 = inetAddressValidator0.isValid("::")
        self.assertTrue(boolean0)

    def test17(self) -> None:

        inetAddressValidator0 = InetAddressValidator.getInstance()
        boolean0 = inetAddressValidator0.isValidInet6Address('2>Od"/X;g/L8JO~9')
        self.assertFalse(boolean0)

    def test16(self) -> None:

        inetAddressValidator0 = InetAddressValidator()
        boolean0 = inetAddressValidator0.isValidInet6Address('%)dID)"/[?wfV}2B7')
        self.assertFalse(boolean0)

    def test15(self) -> None:

        inetAddressValidator0 = InetAddressValidator()
        boolean0 = inetAddressValidator0.isValid("Z]gXJR[/0")
        self.assertFalse(boolean0)

    def test14(self) -> None:

        inetAddressValidator0 = InetAddressValidator.getInstance()
        boolean0 = inetAddressValidator0.isValidInet6Address(":R$BE%%P.u&o>")
        self.assertFalse(boolean0)

    def test13(self) -> None:

        inetAddressValidator0 = InetAddressValidator()
        boolean0 = inetAddressValidator0.isValidInet6Address("]d<I4I%~<e)D@v2{evQ")
        self.assertFalse(boolean0)

    def test12(self) -> None:

        inetAddressValidator0 = InetAddressValidator.getInstance()
        boolean0 = inetAddressValidator0.isValidInet6Address(
            "org.pache.commons.vaidator.routines.RegexValidator:::"
        )
        self.assertFalse(boolean0)

    def test11(self) -> None:

        inetAddressValidator0 = InetAddressValidator()
        boolean0 = inetAddressValidator0.isValidInet6Address("0:")
        self.assertFalse(boolean0)

    def test10(self) -> None:

        inetAddressValidator0 = InetAddressValidator()
        boolean0 = inetAddressValidator0.isValidInet6Address("::jA=$9OV$Stn.e")
        self.assertFalse(boolean0)

    def test09(self) -> None:

        inetAddressValidator0 = InetAddressValidator()
        boolean0 = inetAddressValidator0.isValidInet6Address("+::t")
        self.assertFalse(boolean0)

    def test08(self) -> None:

        inetAddressValidator0 = InetAddressValidator()
        boolean0 = inetAddressValidator0.isValid("0")
        self.assertFalse(boolean0)

    def test07(self) -> None:

        inetAddressValidator0 = InetAddressValidator()
        boolean0 = inetAddressValidator0.isValidInet4Address("C|:UX#,.(t4K")
        self.assertFalse(boolean0)

    def test06(self) -> None:

        inetAddressValidator0 = InetAddressValidator.getInstance()
        boolean0 = inetAddressValidator0.isValidInet6Address("*?v-*/1")
        self.assertFalse(boolean0)

    def test05(self) -> None:

        inetAddressValidator0 = InetAddressValidator()
        boolean0 = inetAddressValidator0.isValidInet6Address(":")
        self.assertFalse(boolean0)

    def test04(self) -> None:

        inetAddressValidator0 = InetAddressValidator()
        boolean0 = inetAddressValidator0.isValidInet6Address("::")
        self.assertTrue(boolean0)

    def test03(self) -> None:

        inetAddressValidator0 = InetAddressValidator.getInstance()
        boolean0 = inetAddressValidator0.isValidInet6Address("-3c")
        self.assertFalse(boolean0)

    def test02(self) -> None:

        inetAddressValidator0 = InetAddressValidator.getInstance()
        boolean0 = inetAddressValidator0.isValidInet6Address("E")
        self.assertFalse(boolean0)

    def test01(self) -> None:

        inetAddressValidator0 = InetAddressValidator()
        # Undeclared exception in Java code
        try:
            inetAddressValidator0.isValid(None)
            self.fail("Expecting exception: RuntimeError")

        except Exception as e:
            # no message in exception (getMessage() returned null)
            self.assertEqual(str(e), "RuntimeError")

    def test00(self) -> None:

        inetAddressValidator0 = InetAddressValidator.getInstance()
        # Undeclared exception in Python is raised as a TypeError
        try:
            inetAddressValidator0.isValidInet6Address(None)
            self.fail("Expecting exception: RuntimeError")

        except TypeError as e:
            # no message in exception (getMessage() returned null)
            # verifyException("org.apache.commons.validator.routines.InetAddressValidator", e)
            # In Python, we don't have a direct equivalent to verifyException.
            # Instead, we can check the type of the exception and its message.
            self.assertIsInstance(e, TypeError)
            self.assertEqual(str(e), "RuntimeError")
