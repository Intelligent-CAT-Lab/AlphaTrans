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
        stack.printStackTrace(self.__writer)
        stackTrace = self.__writer.getvalue()
        assert stackTrace.find(self.__class__.__name__) != -1

    @pytest.mark.skip(reason="Ignore")
    def testPrintClearedStackTraceIsNoOp(self, stack: CallStack) -> None:
        stack.fillInStackTrace()
        stack.clear()
        stack.printStackTrace(self.__writer)
        stackTrace = self.__writer.getvalue()
        assert stackTrace == ""
