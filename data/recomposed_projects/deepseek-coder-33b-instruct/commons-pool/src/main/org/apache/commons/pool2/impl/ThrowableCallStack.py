from __future__ import annotations
from io import StringIO
import io
import typing
from typing import *
import datetime
from src.main.org.apache.commons.pool2.impl.CallStack import *


class Snapshot(BaseException):

    __timestampMillis: int = int(round(datetime.datetime.now().timestamp() * 1000))

    __serialVersionUID: int = 1


class ThrowableCallStack(CallStack):

    __snapshot: Snapshot = None
    __dateFormat: datetime.datetime = None
    __messageFormat: str = None

    def printStackTrace(
        self, writer: typing.Union[io.TextIOWrapper, io.StringIO]
    ) -> bool:

        snapshotRef = self.__snapshot
        if snapshotRef is None:
            return False

        if self.__dateFormat is None:
            message = self.__messageFormat
        else:
            message = self.__dateFormat.strftime("%Y-%m-%d %H:%M:%S")

        writer.write(message + "\n")
        snapshotRef.printStackTrace(writer)
        return True

    def fillInStackTrace(self) -> None:

        self.__snapshot = Snapshot()

    def clear(self) -> None:

        self.__snapshot = None

    def __init__(self, messageFormat: str, useTimestamp: bool) -> None:

        self.__messageFormat = messageFormat
        if useTimestamp:
            self.__dateFormat = datetime.datetime.now()
        else:
            self.__dateFormat = None
