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

        # Here you would implement the logic to print the stack trace.
        # Since the Java method is abstract, it's not clear what the implementation would be.
        # For now, we'll just return False as a placeholder.

        return False

    def fillInStackTrace(self) -> None:

        pass

    def clear(self) -> None:

        self.stack = []
