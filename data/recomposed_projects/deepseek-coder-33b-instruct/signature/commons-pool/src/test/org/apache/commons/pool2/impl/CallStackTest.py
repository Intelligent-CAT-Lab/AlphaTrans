from __future__ import annotations
import re
import unittest
import pytest
from io import StringIO
import io
from src.main.org.apache.commons.pool2.impl.CallStack import *


class CallStackTest:

    __writer: io.StringIO = io.StringIO()

    @pytest.mark.skip(reason="Ignore")
    def testPrintFilledStackTrace(self, stack: CallStack) -> None:

        stack.fillInStackTrace()
        stack.printStackTrace(io.StringIO(self.__writer))
        stackTrace = self.__writer.getvalue()
        assert getClassName() in stackTrace

    @pytest.mark.skip(reason="Ignore")
    def testPrintClearedStackTraceIsNoOp(self, stack: CallStack) -> None:

        stack.fillInStackTrace()
        stack.clear()
        stack.printStackTrace(io.StringIO(self.__writer))
        stackTrace = self.__writer.getvalue()
        assert stackTrace == ""
