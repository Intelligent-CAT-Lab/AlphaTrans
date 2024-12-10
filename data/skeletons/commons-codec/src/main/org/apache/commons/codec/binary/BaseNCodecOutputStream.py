from __future__ import annotations

# Imports Begin
from src.main.org.apache.commons.codec.binary.BaseNCodec import *
import os
import typing
from typing import *
from io import BytesIO
import io
from io import StringIO

# Imports End


class BaseNCodecOutputStream:

    # Class Fields Begin
    __doEncode: bool = None
    __baseNCodec: BaseNCodec = None
    __singleByte: typing.List[int] = None
    __context: Context = None
    # Class Fields End

    # Class Methods Begin
    def write(self, i: int) -> None:
        pass

    def close(self) -> None:
        pass

    def write1(self, i: int) -> None:
        pass

    def write0(self, array: typing.List[int], offset: int, len_: int) -> None:
        pass

    def isStrictDecoding(self) -> bool:
        pass

    def flush0(self) -> None:
        pass

    def eof(self) -> None:
        pass

    def __init__(
        self,
        output: typing.Union[io.BytesIO, io.StringIO, io.BufferedWriter],
        basedCodec: BaseNCodec,
        doEncode: bool,
    ) -> None:
        pass

    def __flush1(self, propagate: bool) -> None:
        pass

    # Class Methods End
