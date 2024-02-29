# Imports Begin
import typing
from typing import *
import io

from src.main.org.apache.commons.fileupload.java_handler import java_handler
# Imports End


@java_handler
class QuotedPrintableDecoder:

    # Class Fields Begin
    __UPPER_NIBBLE_SHIFT: int = Byte.SIZE / 2
    # Class Fields End

    # Class Methods Begin
    @staticmethod
    def decode(
        data: typing.List[int],
        out: typing.Union[io.BytesIO, io.StringIO, io.BufferedWriter],
    ) -> int:

        pass  # LLM could not translate method body

    @staticmethod
    def __hexToBinary(b: int) -> int:

        i = int(b, 16)
        if i == -1:
            raise ValueError(
                "Invalid quoted printable encoding: not a valid hex digit: " + str(b)
            )
        return i

    def __init__(self) -> None:

        pass

    # Class Methods End
