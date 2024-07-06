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
from src.main.org.apache.commons.validator.EmailValidator import *

# from src.test.org.apache.commons.validator.EmailValidator_ESTest_scaffolding import *
# from src.main.org.evosuite.runtime.EvoAssertions import *
# from src.main.org.evosuite.runtime.EvoRunnerParameters import *
from src.main.org.apache.commons.validator.routines.DomainValidator import *
from src.main.org.apache.commons.validator.routines.EmailValidator import *

# from src.test.org.apache.commons.validator.routines.EmailValidator_ESTest_scaffolding import *


class EmailValidator_ESTest(unittest.TestCase):

    def test16(self) -> None:

        email_validator = EmailValidator()

        try:
            email_validator._isValidDomain("[]")
            self.fail("Expecting exception: RuntimeError")
        except RuntimeError as e:
            self.verifyException("java.util.regex.Matcher", e)

    def test15(self) -> None:

        emailValidator0 = EmailValidator.getInstance()
        boolean0 = emailValidator0.isValid("5#_3F.z 5")
        self.assertFalse(boolean0)

    def test14(self) -> None:
        emailValidator0 = EmailValidator.getInstance()
        boolean0 = emailValidator0._isValidUser(
            "m" + "!" + ";" + '"' + "/" + "YWY" + "/" + "!" + "`" + "2" + "=" + "?"
        )
        self.assertFalse(boolean0)

    def test13(self) -> None:

        email_validator0 = EmailValidator.getInstance()

        with pytest.raises(ArrayIndexOutOfBoundsException):
            email_validator0.isValidDomain("g2")

    def test12(self) -> None:

        email_validator0 = EmailValidator.getInstance()
        boolean0 = email_validator0._isValidDomain("b[]")
        self.assertFalse(boolean0)

    def test11(self) -> None:

        email_validator0 = EmailValidator()
        # Undeclared exception
        try:
            email_validator0.isValidIpAddress("`l")
            self.fail("Expecting exception: RuntimeError")

        except RuntimeError as e:
            # No match found
            self.verifyException("java.util.regex.Matcher", e)

    def test10(self) -> None:

        email_validator0 = EmailValidator.getInstance()
        # Undeclared exception handling
        try:
            email_validator0._isValidDomain("?zP-^cj.U$?rt")
        except Exception as e:
            print(f"Exception occurred: {e}")

    def test09(self) -> None:

        emailValidator0 = EmailValidator.getInstance()
        string0 = emailValidator0._stripComments("u|R]lU |#8E&u`-V}[9")
        self.assertEqual("u|R]lU |#8E&u`-V}[9", string0)

    def test08(self) -> None:

        email_validator = EmailValidator()

        try:
            email_validator._isValidDomain(None)
            self.fail("Expecting exception: RuntimeError")

        except TypeError as e:
            # no message in exception (getMessage() returned null)
            pass

    def test07(self) -> None:

        email_validator0 = EmailValidator()
        # Undeclared exception in Java code
        try:
            email_validator0.isValidIpAddress(None)
            self.fail("Expecting exception: RuntimeError")

        except Exception as e:
            # no message in exception (getMessage() returned null)
            pass

    def test06(self) -> None:

        email_validator0 = EmailValidator()
        # Undeclared exception in Java code
        try:
            email_validator0._isValidSymbolicDomain("cool")
            self.fail("Expecting exception: ArrayIndexOutOfBoundsException")

        except IndexError:
            # no message in exception (getMessage() returned null)
            pass

    def test05(self) -> None:

        email_validator0 = EmailValidator.getInstance()
        # Undeclared exception in Java code
        try:
            email_validator0._isValidSymbolicDomain(None)
            self.fail("Expecting exception: RuntimeError")

        except Exception as e:
            # no message in exception (getMessage() returned null)
            pass

    def test04(self) -> None:

        email_validator0 = EmailValidator()
        # Undeclared exception handling is not necessary in Python.
        email_validator0._isValidSymbolicDomain('"<Ja4p.bwv{&&v3$')

    def test03(self) -> None:
        email_validator0 = EmailValidator()
        try:
            email_validator0._isValidUser(None)
            self.fail("Expecting exception: RuntimeError")
        except TypeError as e:
            # no message in exception (getMessage() returned null)
            pass

    def test02(self) -> None:

        emailValidator0 = EmailValidator()
        # Undeclared exception in Java code
        try:
            emailValidator0._stripComments(None)
            self.fail("Expecting exception: RuntimeError")

        except TypeError as e:
            # no message in exception (getMessage() returned null)
            pass

    def test01(self) -> None:
        email_validator0 = EmailValidator()
        boolean0 = email_validator0._isValidUser("'_7K=")
        self.assertTrue(boolean0)

    def test00(self) -> None:

        emailValidator0 = EmailValidator.getInstance()
        string0 = emailValidator0._stripComments("")
        self.assertEqual("", string0)
