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

    __timestampMillis: int = int(round(time.time() * 1000))
    __serialVersionUID: int = 1


class ThrowableCallStack(CallStack):

    __snapshot: Snapshot = None

    __dateFormat: datetime.datetime = None

    __messageFormat: str = ""

    def printStackTrace(
        self, writer: typing.Union[io.TextIOWrapper, io.StringIO]
    ) -> bool:
        snapshotRef = self.__snapshot
        if snapshotRef is None:
            return False
        message = self.__messageFormat
        if self.__dateFormat is None:
            message = self.__messageFormat
        else:
            message = self.__dateFormat.format(
                datetime.datetime.fromtimestamp(snapshotRef.__timestampMillis / 1000)
            )
        writer.write(message)
        snapshotRef.printStackTrace(writer)
        return True

    def fillInStackTrace(self) -> None:
        self.__snapshot = Snapshot()

    def clear(self) -> None:
        self.__snapshot = None

    def __init__(self, messageFormat: str, useTimestamp: bool) -> None:
        self.__messageFormat = messageFormat
        self.__dateFormat = datetime.datetime.now() if useTimestamp else None
