# Imports Begin
import typing
from typing import *
import io
from abc import ABC

# Imports End


class Base64Decoder:

    # Class Fields Begin
    __BYTE_MIN_VALUE = 0
    __BYTE_MAX_VALUE = 255
    __PADDING: int = ""  # LLM could not translate field
    __DECODING_TABLE: bytes = bytearray(range(__BYTE_MIN_VALUE, __BYTE_MAX_VALUE + 1))
    __INVALID_BYTE: int = -1
    __PAD_BYTE: int = -2
    __MASK_BYTE_UNSIGNED: int = 255
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
