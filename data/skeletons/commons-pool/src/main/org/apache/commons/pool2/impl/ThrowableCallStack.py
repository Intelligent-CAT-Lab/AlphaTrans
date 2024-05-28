from __future__ import annotations

# Imports Begin
from src.main.org.apache.commons.pool2.impl.CallStack import *
import datetime
import typing
from typing import *
import io
from io import StringIO

# Imports End


class Snapshot(BaseException):

    # Class Fields Begin
    __serialVersionUID: int = None
    __timestampMillis: int = None
    # Class Fields End

    # Class Methods Begin
    # Class Methods End


class ThrowableCallStack(CallStack):

    # Class Fields Begin
    __messageFormat: str = None
    __dateFormat: datetime.datetime = None
    __snapshot: Snapshot = None
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

    def __init__(self, messageFormat: str, useTimestamp: bool) -> None:
        pass

    # Class Methods End
