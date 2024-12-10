from __future__ import annotations

# Imports Begin
import typing
from typing import *
from io import BytesIO
import io
from io import StringIO

# Imports End


class Base64Decoder:

    # Class Fields Begin
    __PADDING: int = None
    __DECODING_TABLE: typing.List[int] = None
    __INVALID_BYTE: int = None
    __PAD_BYTE: int = None
    __MASK_BYTE_UNSIGNED: int = None
    __INPUT_BYTES_PER_CHUNK: int = None
    __ENCODING_TABLE: typing.List[int] = None
    # Class Fields End

    # Class Methods Begin
    @staticmethod
    def decode(
        data: typing.List[int],
        out: typing.Union[io.BytesIO, io.StringIO, io.BufferedWriter],
    ) -> int:
        pass

    def __init__(self) -> None:
        pass

    # Class Methods End
