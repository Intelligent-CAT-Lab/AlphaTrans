from __future__ import annotations

# Imports Begin
import os
import typing
from typing import *
import io
from abc import ABC

# Imports End


class ByteArrayOutputStreamX:

    # Class Fields Begin
    # Class Fields End

    # Class Methods Begin
    def toString(self, charset: str) -> str:
        pass

    def __init__(self, size: int) -> None:
        pass

    # Class Methods End


class LogOutputStream(ABC):

    # Class Fields Begin
    __INTIAL_SIZE: int = None
    __CR: int = None
    __LF: int = None
    __buffer: ByteArrayOutputStreamX = None
    __skip: bool = None
    __level: int = None
    __charset: str = None
    # Class Fields End

    # Class Methods Begin
    def flush(self) -> None:
        pass

    def close(self) -> None:
        pass

    def write1(self, cc: int) -> None:
        pass

    def write0(self, b: typing.List[int], off: int, len_: int) -> None:
        pass

    def _processLine0(self, line: str) -> None:
        pass

    def _processBuffer(self) -> None:
        pass

    def getMessageLevel(self) -> int:
        pass

    def __init__(self, constructorId: int, level: int, charset: str) -> None:
        pass

    def _processLine1(self, line: str, logLevel: int) -> None:
        pass

    # Class Methods End
