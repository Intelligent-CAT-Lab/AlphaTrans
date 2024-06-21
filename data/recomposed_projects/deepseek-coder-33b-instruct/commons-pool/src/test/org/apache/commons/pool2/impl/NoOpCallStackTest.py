from __future__ import annotations
import io
from src.main.org.apache.commons.pool2.impl.CallStack import *
from src.main.org.apache.commons.pool2.impl.NoOpCallStack import *


class NoOpCallStackTest:

    def printStackTraceIsNoOp(self) -> None:

        stack = NoOpCallStack.INSTANCE
        stack.fillInStackTrace()
        writer = io.StringIO()
        stack.printStackTrace(io.TextIOWrapper(writer))
        assert writer.getvalue() == ""
