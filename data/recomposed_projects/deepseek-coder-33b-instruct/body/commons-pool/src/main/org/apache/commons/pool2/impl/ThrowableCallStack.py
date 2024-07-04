from __future__ import annotations
import time
import re
from io import StringIO
import io
import typing
from typing import *
import datetime
from src.main.org.apache.commons.pool2.impl.CallStack import *


class Snapshot(BaseException):

    __timestampMillis: int = int(datetime.datetime.now().timestamp() * 1000)
    __serialVersionUID: int = 1


class ThrowableCallStack(CallStack):

    __snapshot: Snapshot = None

    __dateFormat: datetime.datetime = None

    __messageFormat: str = ""

    def printStackTrace(
        self, writer: typing.Union[io.TextIOWrapper, io.StringIO]
    ) -> bool:

        snapshot_ref = self.__snapshot
        if snapshot_ref is None:
            return False
        message = self.__messageFormat
        if self.__dateFormat is not None:
            message = self.__dateFormat.strftime("%Y-%m-%d %H:%M:%S")
        writer.write(message + "\n")
        snapshot_ref.printStackTrace(writer)
        return True

    def fillInStackTrace(self) -> None:
        self.__snapshot = Snapshot()

    def clear(self) -> None:
        self.__snapshot = None

    def __init__(self, messageFormat: str, useTimestamp: bool) -> None:

        self.__messageFormat = messageFormat
        self.__dateFormat = datetime.datetime.now() if useTimestamp else None
