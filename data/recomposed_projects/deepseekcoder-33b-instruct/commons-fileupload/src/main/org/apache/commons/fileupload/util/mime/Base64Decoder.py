# Imports Begin
import typing
from typing import *
from io import BytesIO
import io
from abc import ABC

# Imports End


class Base64Decoder:

    # Class Fields Begin
    __PADDING: int = ord("=")
    __DECODING_TABLE: bytes = bytearray(Byte.MAX_VALUE - Byte.MIN_VALUE + 1)
    __INVALID_BYTE: int = -1
    __PAD_BYTE: int = -2
    __MASK_BYTE_UNSIGNED: int = 0xFF
    __INPUT_BYTES_PER_CHUNK: int = 4
    __ENCODING_TABLE: bytes = (
        b"ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"
    )
    # Class Fields End

    # Class Methods Begin
    @staticmethod
    def decode(
        data: typing.List[int],
        out: typing.Union[io.BytesIO, io.StringIO, io.BufferedWriter],
    ) -> int:

        pass  # LLM could not translate method body

    def __init__(self) -> None:

        pass

    # Class Methods End
