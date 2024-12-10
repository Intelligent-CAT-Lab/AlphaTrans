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


class InputStreamPumper:

    # Class Fields Begin
    SLEEPING_TIME: int = None
    __is: typing.Union[io.BytesIO, io.StringIO, io.BufferedReader] = None
    __os: typing.Union[io.BytesIO, io.StringIO, io.BufferedWriter] = None
    __stop: bool = None
    # Class Fields End

    # Class Methods Begin
    def run(self) -> None:
        pass

    def stopProcessing(self) -> None:
        pass

    def __init__(
        self,
        is_: typing.Union[io.BytesIO, io.StringIO, io.BufferedReader],
        os: typing.Union[io.BytesIO, io.StringIO, io.BufferedWriter],
    ) -> None:
        pass

    # Class Methods End
