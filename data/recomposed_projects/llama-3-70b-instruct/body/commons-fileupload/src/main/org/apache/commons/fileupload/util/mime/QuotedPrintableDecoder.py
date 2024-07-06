from __future__ import annotations
import re
from io import StringIO
import io
from io import BytesIO
import typing
from typing import *


class QuotedPrintableDecoder:

    __UPPER_NIBBLE_SHIFT: int = 4

    @staticmethod
    def decode(
        data: typing.List[int],
        out: typing.Union[io.BytesIO, io.StringIO, io.BufferedWriter],
    ) -> int:
        off = 0
        length = len(data)
        endOffset = off + length
        bytesWritten = 0

        while off < endOffset:
            ch = data[off]
            off += 1

            if ch == ord("_"):
                out.write(" ")
            elif ch == ord("="):
                if off + 1 >= endOffset:
                    raise IOException(
                        "Invalid quoted printable encoding; truncated escape sequence"
                    )
                b1 = data[off]
                off += 1
                b2 = data[off]
                off += 1

                if b1 == ord("\r"):
                    if b2 != ord("\n"):
                        raise IOException(
                            "Invalid quoted printable encoding; CR must be followed by LF"
                        )
                else:
                    c1 = QuotedPrintableDecoder.__hexToBinary(b1)
                    c2 = QuotedPrintableDecoder.__hexToBinary(b2)
                    out.write((c1 << QuotedPrintableDecoder.__UPPER_NIBBLE_SHIFT) | c2)
                    bytesWritten += 1
            else:
                out.write(ch)
                bytesWritten += 1

        return bytesWritten

    @staticmethod
    def __hexToBinary(b: int) -> int:
        i = int.from_bytes(b, byteorder="big")
        if i == -1:
            raise IOException(
                "Invalid quoted printable encoding: not a valid hex digit: " + b
            )
        return i

    def __init__(self) -> None:
        pass
