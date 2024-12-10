from __future__ import annotations

# Imports Begin
import typing
from typing import *
from io import BytesIO
import io
from io import StringIO

# Imports End


class QuotedPrintableDecoder:

    # Class Fields Begin
    __UPPER_NIBBLE_SHIFT: int = None
    # Class Fields End

    # Class Methods Begin
    @staticmethod
    def decode(
        data: typing.List[int],
        out: typing.Union[io.BytesIO, io.StringIO, io.BufferedWriter],
    ) -> int:
        pass

    @staticmethod
    def __hexToBinary(b: int) -> int:
        pass

    def __init__(self) -> None:
        pass

    # Class Methods End
