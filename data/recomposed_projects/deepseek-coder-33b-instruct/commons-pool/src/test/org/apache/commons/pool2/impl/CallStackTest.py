from __future__ import annotations
from io import StringIO
import io
from src.main.org.apache.commons.pool2.impl.CallStack import *


class CallStackTest:

    __writer: io.StringIO = io.StringIO()

    def testPrintFilledStackTrace(self, stack: CallStack) -> None:

        stack.fillInStackTrace()
        writer = io.StringIO()
        stack.printStackTrace(io.TextIOWrapper(writer))
        stackTrace = writer.getvalue()
        assert getClass().getName() in stackTrace

    def testPrintClearedStackTraceIsNoOp(self, stack: CallStack) -> None:

        stack.fillInStackTrace()
        stack.clear()
        self.__writer = io.StringIO()
        stack.printStackTrace(io.PrintWriter(self.__writer))
        stack_trace = self.__writer.getvalue()
        assert stack_trace == ""
