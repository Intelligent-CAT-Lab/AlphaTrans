from __future__ import annotations

# Imports Begin
import typing
from typing import *
import io
from io import StringIO
from io import IOBase

# Imports End


class IOUtils:

    # Class Fields Begin
    DEFAULT_BUFFER_SIZE: int = None
    __EOF: int = None
    # Class Fields End

    # Class Methods Begin
    @staticmethod
    def rethrow(throwable: BaseException) -> RuntimeError:
        pass

    @staticmethod
    def copyLarge1(
        input_: typing.Union[io.TextIOWrapper, io.BufferedReader, io.TextIOBase],
        output: typing.Union[io.TextIOWrapper, io.BufferedWriter, io.TextIOBase],
        buffer: typing.List[str],
    ) -> int:
        pass

    @staticmethod
    def copyLarge0(
        input_: typing.Union[io.TextIOWrapper, io.BufferedReader, io.TextIOBase],
        output: typing.Union[io.TextIOWrapper, io.BufferedWriter, io.TextIOBase],
    ) -> int:
        pass

    @staticmethod
    def copy1(
        input_: typing.Union[io.TextIOWrapper, io.BufferedReader, io.TextIOBase],
        output: typing.Union[typing.List, io.TextIOBase],
        buffer: typing.Union[str, typing.List[str], io.StringIO],
    ) -> int:
        pass

    @staticmethod
    def copy0(
        input_: typing.Union[io.TextIOWrapper, io.BufferedReader, io.TextIOBase],
        output: typing.Union[typing.List, io.TextIOBase],
    ) -> int:
        pass

    def __init__(self) -> None:
        pass

    # Class Methods End
