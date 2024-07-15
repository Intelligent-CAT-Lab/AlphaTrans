from __future__ import annotations

# Imports Begin
from src.main.org.apache.commons.codec.binary.BaseNCodec import *
import typing
from typing import *
from io import BytesIO
import io
from io import StringIO

# Imports End


class BaseNCodecInputStream:

    # Class Fields Begin
    __baseNCodec: BaseNCodec = None
    __doEncode: bool = None
    __singleByte: typing.List[int] = None
    __buf: typing.List[int] = None
    __context: Context = None
    # Class Fields End

    # Class Methods Begin
    def skip(self, n: int) -> int:
        pass

    def reset(self) -> None:
        pass

    def markSupported(self) -> bool:
        pass

    def mark(self, readLimit: int) -> None:
        pass

    def available(self) -> int:
        pass

    def read1(self, array: typing.List[int], offset: int, len_: int) -> int:
        pass

    def read0(self) -> int:
        pass

    def isStrictDecoding(self) -> bool:
        pass

    def __init__(
        self,
        input_: typing.Union[io.BytesIO, io.StringIO, io.BufferedReader],
        baseNCodec: BaseNCodec,
        doEncode: bool,
    ) -> None:
        pass

    # Class Methods End
