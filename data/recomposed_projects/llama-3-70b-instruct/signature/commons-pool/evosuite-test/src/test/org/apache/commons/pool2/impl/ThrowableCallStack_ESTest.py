from __future__ import annotations
import time
import re
import mock
import os
from io import StringIO
import unittest
import pytest
import io
import unittest
from src.main.org.apache.commons.pool2.impl.ThrowableCallStack import *

# from src.test.org.apache.commons.pool2.impl.ThrowableCallStack_ESTest_scaffolding import *
# from src.main.org.evosuite.runtime.EvoAssertions import *
# from src.main.org.evosuite.runtime.EvoRunnerParameters import *


class ThrowableCallStack_ESTest(unittest.TestCase):

    def test5(self) -> None:

        throwableCallStack0 = ThrowableCallStack('Uz*mZ5Zn$8f#H"e +e', False)
        throwableCallStack0.clear()

    def test4(self) -> None:

        throwableCallStack0 = ThrowableCallStack("", True)
        throwableCallStack0.fillInStackTrace()

        try:
            throwableCallStack0.printStackTrace(None)
            self.fail("Expecting exception: RuntimeError")

        except Exception as e:
            self.assertEqual(str(e), "")
            self.assertEqual(type(e).__name__, "RuntimeError")

    def test3(self) -> None:

        throwableCallStack0 = ThrowableCallStack("", False)
        mockPrintWriter0 = io.StringIO()
        boolean0 = throwableCallStack0.printStackTrace(mockPrintWriter0)
        self.assertFalse(boolean0)

    def test2(self) -> None:

        throwableCallStack0 = ThrowableCallStack("", False)
        mockPrintWriter0 = io.StringIO()
        throwableCallStack0.fillInStackTrace()
        boolean0 = throwableCallStack0.printStackTrace(mockPrintWriter0)
        self.assertTrue(boolean0)

    def test1(self) -> None:

        throwableCallStack0 = None
        try:
            throwableCallStack0 = ThrowableCallStack("?;6EJ3", True)
            self.fail("Expecting exception: ValueError")

        except ValueError as e:
            #
            # Illegal pattern character 'J'
            #
            self.verifyException("java.text.SimpleDateFormat", e)

    def test0(self) -> None:

        throwableCallStack0 = None
        try:
            throwableCallStack0 = ThrowableCallStack(None, True)
            self.fail("Expecting exception: RuntimeError")

        except RuntimeError as e:
            # no message in exception (getMessage() returned null)
            self.verifyException("java.text.SimpleDateFormat", e)
