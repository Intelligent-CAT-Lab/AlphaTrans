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

    def test22(self) -> None:

        emailValidator0 = EmailValidator.getInstance0()
        boolean0 = emailValidator0.isValid(None)
        self.assertFalse(boolean0)

    def test21(self) -> None:

        emailValidator0 = EmailValidator.EmailValidator0(False)
        self.assertIsNotNone(emailValidator0)

    def test20(self) -> None:

        emailValidator0 = EmailValidator.getInstance1(True, True)
        boolean0 = emailValidator0._isValidDomain("0")
        self.assertTrue(boolean0)

    def test19(self) -> None:

        emailValidator0 = EmailValidator.getInstance2(True)
        self.assertIsNotNone(emailValidator0)

    def test18(self) -> None:

        emailValidator0 = EmailValidator.getInstance1(False, True)
        boolean0 = emailValidator0._isValidDomain("-+z|Gh.=ZJ$qY5")
        self.assertFalse(boolean0)

    def test17(self) -> None:

        emailValidator0 = None
        try:
            emailValidator0 = EmailValidator(0, True, False, None)
            self.fail("Expecting exception: ValueError")

        except ValueError as e:
            # DomainValidator cannot be null
            self.assertEqual(str(e), "DomainValidator cannot be null")

    def test16(self) -> None:

        linkedList0 = []
        domainValidator0 = DomainValidator(0, linkedList0, True)
        emailValidator0 = EmailValidator(0, True, True, domainValidator0)

    def test15(self) -> None:

        linkedList0 = []
        domainValidator0 = DomainValidator(0, linkedList0, True)
        emailValidator0 = None
        try:
            emailValidator0 = EmailValidator(0, False, True, domainValidator0)
            self.fail("Expecting exception: ValueError")

        except ValueError as e:
            # DomainValidator must agree with allowLocal setting
            self.verifyException(
                "org.apache.commons.validator.routines.EmailValidator", e
            )

    def test14(self) -> None:

        emailValidator0 = EmailValidator.getInstance1(False, False)
        boolean0 = emailValidator0.isValid("")
        self.assertFalse(boolean0)

    def test13(self) -> None:

        emailValidator0 = EmailValidator.getInstance0()
        boolean0 = emailValidator0.isValid("wang.")
        self.assertFalse(boolean0)

    def test12(self) -> None:

        emailValidator0 = EmailValidator.getInstance0()
        # Undeclared exception in Java, but we can use pytest.raises to handle exceptions in Python
        with pytest.raises(RuntimeError):
            emailValidator0.isValid("(\\.)|[^sp{Cntrl}()<>@,;:'\\\".[]]")
            #  fail("Expecting exception: RuntimeError")
            # Unstable assertion

        # No match found
        #
        # verifyException("java.util.regex.Matcher", e)
        # In Python, we don't have a direct equivalent to verifyException.
        # We can use assert to check if the function raises an exception.
        # However, since we are using pytest.raises, we don't need to check this.

    def test11(self) -> None:

        emailValidator0 = EmailValidator.getInstance1(False, False)
        boolean0 = emailValidator0._isValidDomain("")
        self.assertFalse(boolean0)

    def test10(self) -> None:

        emailValidator0 = EmailValidator.getInstance0()
        # Undeclared exception in Java code
        try:
            emailValidator0._isValidDomain("[]")
            # fail("Expecting exception: RuntimeError")
            # Unstable assertion
        except RuntimeError as e:
            # No match found
            # verifyException("java.util.regex.Matcher", e)
            pass

    def test09(self) -> None:

        emailValidator0 = EmailValidator(1158, True, True, None)
        boolean0 = emailValidator0._isValidDomain(".-+z|Gh.=ZJ$qY5")
        self.assertFalse(boolean0)

    def test08(self) -> None:

        emailValidator0 = EmailValidator.getInstance1(False, True)
        boolean0 = emailValidator0._isValidDomain("barcelona")
        self.assertTrue(boolean0)

    def test07(self) -> None:

        emailValidator0 = EmailValidator.getInstance0()
        boolean0 = emailValidator0._isValidUser(None)
        self.assertFalse(boolean0)

    def test06(self) -> None:

        emailValidator0 = EmailValidator.getInstance1(False, False)
        boolean0 = emailValidator0._isValidUser(
            '^(((\\.)|[^sp{Cntrl}()<>@,;:\'\\".[]]|\')+|("(\\"|[^"])*"))(.(((\\.)|[^sp{Cntrl}()<>@,;:\'\\".[]]|\')+|("(\\"|[^"])*")))*$'
        )
        self.assertFalse(boolean0)

    def test05(self) -> None:

        email_validator0 = EmailValidator(1158, True, True, None)
        boolean0 = email_validator0._isValidUser("")
        self.assertFalse(boolean0)

    def test04(self) -> None:

        emailValidator0 = EmailValidator.getInstance1(True, False)
        self.assertIsNotNone(emailValidator0)

    def test03(self) -> None:

        emailValidator0 = EmailValidator.getInstance0()
        # Undeclared exception in Java code
        try:
            emailValidator0._isValidDomain(None)
            self.fail("Expecting exception: RuntimeError")

        except Exception as e:
            # no message in exception (getMessage() returned null)
            pass

    def test02(self) -> None:

        emailValidator0 = EmailValidator.getInstance1(False, True)
        boolean0 = emailValidator0._isValidUser("J")
        self.assertTrue(boolean0)

    def test01(self) -> None:

        linkedList0 = []
        domainValidator0 = DomainValidator(523, linkedList0, True)
        emailValidator0 = EmailValidator(-725, False, True, domainValidator0)

    def test00(self) -> None:

        emailValidator0 = EmailValidator.getInstance1(True, True)
        boolean0 = emailValidator0._isValidUser(
            '(((\\.)|[^sp{Cntrl}()<>@,;:\'\\".[]]|\')+|("(\\"|[^"])*"))'
        )
        self.assertFalse(boolean0)
