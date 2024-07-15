import pytest

from src.main.org.apache.commons.pool2.impl.CallStack import *
from src.main.org.apache.commons.pool2.impl.ThrowableCallStack import *
import unittest
from io import StringIO

class TestCallStack(unittest.TestCase):

    __writer = None

    
    def getWriter(self) -> StringIO:
        return self.__writer
    
    
    @staticmethod
    def data():
        return [
            ThrowableCallStack("Test", False),
            ThrowableCallStack("yyyy-MM-dd'T'HH:mm:ss.SSSXXX", True)
        ]

    
    def setUp(self) -> None:
        self.__writer = StringIO()

    
@pytest.mark.parametrize("stack", TestCallStack.data())
def testPrintClearedStackTraceIsNoOp(stack) -> None:
    callStackTestCase = TestCallStack()
    stack.fillInStackTrace()
    stack.clear()
    stack.printStackTrace(callStackTestCase.getWriter())
    stackTrace = callStackTestCase.getWriter().getvalue()
    unittest.TestCase().assertEqual(
        "",
        stackTrace,
        "Stack trace should be empty after clearing"
    )


@pytest.mark.parametrize("stack", TestCallStack.data())
def testPrintFilledStackTrace(stack) -> None:
    callStackTestCase = TestCallStack()
    stack.fillInStackTrace()
    stack.printStackTrace(callStackTestCase.getWriter())
    stackTrace = callStackTestCase.getWriter().getvalue()
    unittest.TestCase().assertTrue(
        callStackTestCase.__class__.__name__ in stackTrace,
        "Stack trace should contain the class name"
    )
