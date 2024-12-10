from __future__ import annotations

# Imports Begin
from src.main.org.apache.commons.pool2.impl.CallStack import *
import io
from io import StringIO

# Imports End


class CallStackTest:

    # Class Fields Begin
    __writer: io.StringIO = None
    # Class Fields End

    # Class Methods Begin
    def testPrintFilledStackTrace(self, stack: CallStack) -> None:
        pass

    def testPrintClearedStackTraceIsNoOp(self, stack: CallStack) -> None:
        pass

    # Class Methods End
