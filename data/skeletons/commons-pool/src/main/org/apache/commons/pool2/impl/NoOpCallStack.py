from __future__ import annotations

# Imports Begin
from src.main.org.apache.commons.pool2.impl.CallStack import *
import typing
from typing import *
import io
from io import StringIO

# Imports End


class NoOpCallStack(CallStack):

    # Class Fields Begin
    INSTANCE: CallStack = None
    # Class Fields End

    # Class Methods Begin
    def printStackTrace(
        self, writer: typing.Union[io.TextIOWrapper, io.StringIO]
    ) -> bool:
        pass

    def fillInStackTrace(self) -> None:
        pass

    def clear(self) -> None:
        pass

    def __init__(self) -> None:
        pass

    # Class Methods End
