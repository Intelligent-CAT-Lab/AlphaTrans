from __future__ import annotations

# Imports Begin
import typing
from typing import *
from io import BytesIO
import io
from io import StringIO
from abc import ABC

# Imports End


class ExecuteStreamHandler(ABC):

    # Class Fields Begin
    # Class Fields End

    # Class Methods Begin
    def stop(self) -> None:
        pass

    def start(self) -> None:
        pass

    def setProcessOutputStream(
        self, inputStream: typing.Union[io.BytesIO, io.StringIO, io.BufferedReader]
    ) -> None:
        pass

    def setProcessInputStream(
        self, outputStream: typing.Union[io.BytesIO, io.StringIO, io.BufferedWriter]
    ) -> None:
        pass

    def setProcessErrorStream(
        self, inputStream: typing.Union[io.BytesIO, io.StringIO, io.BufferedReader]
    ) -> None:
        pass

    # Class Methods End
