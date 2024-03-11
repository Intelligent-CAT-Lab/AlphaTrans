# Imports Begin
from src.main.org.apache.commons.pool2.impl.CallStack import *
import unittest
import io

# Imports End


class CallStackTest(unittest.TestCase):

    # Class Fields Begin
    __writer: io.StringIO = ""  # LLM could not translate field
    # Class Fields End

    # Class Methods Begin
    def testPrintFilledStackTrace(self, stack: CallStack) -> None:

        stack.fillInStackTrace()
        stack.printStackTrace(io.TextIOWrapper(self.__writer))
        stackTrace = self.__writer.toString()
        self.assertTrue(stackTrace.contains(self.getClass().getName()))

    def testPrintClearedStackTraceIsNoOp(self, stack: CallStack) -> None:

        stack.fillInStackTrace()
        stack.clear()
        stack.printStackTrace(io.TextIOWrapper(self.__writer))
        stackTrace = self.__writer.getvalue()
        self.assertEqual("", stackTrace)

    # Class Methods End
