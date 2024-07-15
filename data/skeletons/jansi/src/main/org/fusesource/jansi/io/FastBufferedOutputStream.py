from __future__ import annotations

# Imports Begin
import typing
from typing import *
from io import BytesIO
import io
from io import StringIO

# Imports End


class FastBufferedOutputStream:

    # Class Fields Begin
    _buf: typing.List[int] = None
    _count: int = None
    # Class Fields End

    # Class Methods Begin
    def flush(self) -> None:
        pass

    def write1(self, b: typing.List[int], off: int, len_: int) -> None:
        pass

    def write0(self, b: int) -> None:
        pass

    def __init__(
        self, out: typing.Union[io.BytesIO, io.StringIO, io.BufferedWriter]
    ) -> None:
        pass

    def __flushBuffer(self) -> None:
        pass

    # Class Methods End
