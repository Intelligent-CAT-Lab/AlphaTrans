import pytest

from src.main.org.apache.commons.pool2.impl.CallStack import *
from src.main.org.apache.commons.pool2.impl.ThrowableCallStack import *
import unittest
from io import StringIO

class TestCallStack(unittest.TestCase):

    def __init__(self, methodName='runTest') -> None:
        super().__init__(methodName)
        self.__writer = None

    
    @staticmethod
    def data():
        return [
            ThrowableCallStack("Test", False),
            ThrowableCallStack("yyyy-MM-dd'T'HH:mm:ss.SSSXXX", True)
        ]

    
    def setUp(self) -> None:
        self.__writer = StringIO()

    
    @pytest.mark.test
    def testPrintClearedStackTraceIsNoOp(self) -> None:
        for stack in TestCallStack.data():
            with self.subTest(stack=stack):
                stack.fillInStackTrace()
                stack.clear()
                stack.printStackTrace(self.__writer)
                stackTrace = self.__writer.getvalue()
                self.assertEqual(
                    "",
                    stackTrace,
                    "Stack trace should be empty after clearing"
                )

    
    @pytest.mark.test
    def testPrintFilledStackTrace(self) -> None:
        for stack in TestCallStack.data():
            with self.subTest(stack=stack):
                stack.fillInStackTrace()
                stack.printStackTrace(self.__writer)
                stackTrace = self.__writer.getvalue()
                self.assertTrue(
                    self.__class__.__name__ in stackTrace,
                    "Stack trace should contain the class name"
                )
