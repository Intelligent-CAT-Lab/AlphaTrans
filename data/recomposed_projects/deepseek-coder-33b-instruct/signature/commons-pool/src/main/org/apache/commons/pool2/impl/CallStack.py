from __future__ import annotations
import re
from abc import ABC
from io import StringIO
import io
import typing
from typing import *


class CallStack(ABC):

    def printStackTrace(
        self, writer: typing.Union[io.TextIOWrapper, io.StringIO]
    ) -> bool:

        # Here you would implement the logic to print the stack trace
        # For simplicity, let's just return False as a placeholder

        return False

    def fillInStackTrace(self) -> None:

        # Python does not have a direct equivalent to Java's fillInStackTrace method.
        # However, you can simulate the behavior by using the traceback module to print the stack trace.
        # Here is a simple example:

        import traceback

        traceback.print_stack()

    def clear(self) -> None:
        self.stack = []
