# Imports Begin
import typing
from typing import *
import io

from src.main.org.apache.commons.fileupload.java_handler import java_handler
# Imports End


@java_handler
class Base64Decoder:

    # Class Fields Begin
    __CRLF: str = "\r\n"
    __ENCODING_TABLE: bytes = [0] * (Byte.MAX_VALUE - Byte.MIN_VALUE + 1)
    __MAX_BYTE: int = 63
    __PAD_BYTE: int = -2
    __MASK_BYTE_UNSIGNED: int = 255
    __INPUT_BYTES_PER_CHUNK: int = 4
    __ENCODING_TABLE: typing.List[int] = ""  # LLM could not translate field
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
