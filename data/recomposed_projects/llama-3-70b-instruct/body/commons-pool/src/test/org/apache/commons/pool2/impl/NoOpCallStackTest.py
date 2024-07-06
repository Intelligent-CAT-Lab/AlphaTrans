from __future__ import annotations
import re
from io import StringIO
import unittest
import pytest
import io
import unittest
from src.main.org.apache.commons.pool2.impl.CallStack import *
from src.main.org.apache.commons.pool2.impl.NoOpCallStack import *


class NoOpCallStackTest(unittest.TestCase):

    def testprintStackTraceIsNoOp(self) -> None:
        stack = NoOpCallStack.INSTANCE
        stack.fillInStackTrace()
        writer = io.StringIO()
        stack.printStackTrace(writer)
        self.assertEqual("", writer.getvalue())
