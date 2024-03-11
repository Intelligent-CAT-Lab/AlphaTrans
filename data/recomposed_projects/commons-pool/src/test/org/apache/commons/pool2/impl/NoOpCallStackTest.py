# Imports Begin
from src.main.org.apache.commons.pool2.impl.NoOpCallStack import *
from src.main.org.apache.commons.pool2.impl.CallStack import *
import unittest

# Imports End


class NoOpCallStackTest(unittest.TestCase):

    # Class Fields Begin
    # Class Fields End

    # Class Methods Begin
    def printStackTraceIsNoOp(self) -> None:

        stack = NoOpCallStack.INSTANCE
        stack.fillInStackTrace()
        writer = StringWriter()
        stack.printStackTrace(PrintWriter(writer))
        self.assertEqual("", writer.toString())

    # Class Methods End
