from src.main.org.apache.commons.pool2.impl.NoOpCallStack import *
import unittest
from io import StringIO

class NoOpCallStackTest(unittest.TestCase):

    def testprintStackTraceIsNoOp(self) -> None:
        stack = NoOpCallStack.INSTANCE
        stack.fillInStackTrace()
        writer = StringIO()
        stack.printStackTrace(writer)
        self.assertEqual("", writer.getvalue())
