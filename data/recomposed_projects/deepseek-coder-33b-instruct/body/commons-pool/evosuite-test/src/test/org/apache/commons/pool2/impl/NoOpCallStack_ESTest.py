from __future__ import annotations
import time
import re
import mock
import os
from io import BytesIO
import unittest
import pytest
import io
import unittest
from src.main.org.apache.commons.pool2.impl.CallStack import *
from src.main.org.apache.commons.pool2.impl.NoOpCallStack import *

# from src.test.org.apache.commons.pool2.impl.NoOpCallStack_ESTest_scaffolding import *
from src.main.org.apache.commons.pool2.impl.ThrowableCallStack import *

# from src.main.org.evosuite.runtime.EvoRunnerParameters import *


class NoOpCallStack_ESTest(unittest.TestCase):

    def test5(self) -> None:
        noOpCallStack0 = NoOpCallStack.INSTANCE
        noOpCallStack0.fillInStackTrace()

    def test4(self) -> None:

        noOpCallStack0: NoOpCallStack = NoOpCallStack.INSTANCE
        byteArrayOutputStream0 = io.BytesIO()
        mockPrintWriter0 = io.TextIOWrapper(byteArrayOutputStream0)
        boolean0 = noOpCallStack0.printStackTrace(mockPrintWriter0)
        self.assertFalse(boolean0)

    def test3(self) -> None:
        noOpCallStack0 = NoOpCallStack.INSTANCE
        noOpCallStack0.clear()

    def test2(self) -> None:

        throwableCallStack0 = ThrowableCallStack("", False)
        # Undeclared exception
        try:
            throwableCallStack0.clear()
            # fail("Expecting exception: ValueError")
            # Unstable assertion
        except ValueError:
            pass

    def test1(self) -> None:

        throwableCallStack0 = ThrowableCallStack(None, False)
        try:
            throwableCallStack0.fillInStackTrace()
        except ValueError:
            pass

    def test0(self) -> None:

        throwableCallStack0 = ThrowableCallStack(" :``[8:|?W,`2?", False)
        # Undeclared exception translated to pass
        try:
            throwableCallStack0.printStackTrace(None)
            # fail("Expecting exception: ValueError")
            # Unstable assertion translated to pass
        except ValueError:
            pass
