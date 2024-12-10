from __future__ import annotations

# Imports Begin
from src.main.org.apache.commons.exec.util.DebugUtils import *
import os
import typing
from typing import *
from io import BytesIO
import io
from io import StringIO

# Imports End


class StreamPumper:

    # Class Fields Begin
    __DEFAULT_SIZE: int = None
    __is: typing.Union[io.BytesIO, io.StringIO, io.BufferedReader] = None
    __os: typing.Union[io.BytesIO, io.StringIO, io.BufferedWriter] = None
    __size: int = None
    __finished: bool = None
    __closeWhenExhausted: bool = None
    # Class Fields End

    # Class Methods Begin
    def run(self) -> None:
        pass

    def waitFor(self) -> None:
        pass

    def isFinished(self) -> bool:
        pass

    def __init__(
        self,
        is_: typing.Union[io.BytesIO, io.StringIO, io.BufferedReader],
        os: typing.Union[io.BytesIO, io.StringIO, io.BufferedWriter],
        closeWhenExhausted: bool,
        size: int,
    ) -> None:
        pass

    @staticmethod
    def StreamPumper0(
        is_: typing.Union[io.BytesIO, io.StringIO, io.BufferedReader],
        os: typing.Union[io.BytesIO, io.StringIO, io.BufferedWriter],
    ) -> StreamPumper:
        pass

    # Class Methods End
