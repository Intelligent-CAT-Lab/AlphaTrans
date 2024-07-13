from __future__ import annotations

# Imports Begin
from src.main.org.apache.commons.fileupload.util.Closeable import *
import os
import typing
from typing import *
from io import BytesIO
import io
from io import StringIO
from abc import ABC

# Imports End


class LimitedInputStream(ABC):

    # Class Fields Begin
    __sizeMax: int = None
    __count: int = None
    __closed: bool = None
    # Class Fields End

    # Class Methods Begin
    def close(self) -> None:
        pass

    def isClosed(self) -> bool:
        pass

    def read1(self, b: typing.List[int], off: int, len_: int) -> int:
        pass

    def read0(self) -> int:
        pass

    def __init__(
        self,
        inputStream: typing.Union[io.BytesIO, io.StringIO, io.BufferedReader],
        pSizeMax: int,
    ) -> None:
        pass

    def __checkLimit(self) -> None:
        pass

    def _raiseError(self, pSizeMax: int, pCount: int) -> None:
        pass

    # Class Methods End
