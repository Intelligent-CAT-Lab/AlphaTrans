# Imports Begin
import typing
from typing import *
import io

# Imports End


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

        off = 0
        length = len(data)
        endOffset = off + length
        bytesWritten = 0
        while off < endOffset:
            ch = data[off]
            off += 1
            if ch == ord("_"):
                out.write(ord(" "))
            elif ch == ord("="):
                if off + 1 >= endOffset:
                    raise IOError(
                        "Invalid quoted printable encoding; truncated escape sequence"
                    )
                b1 = data[off]
                b2 = data[off + 1]
                off += 2
                if b1 == ord("\r"):
                    if b2 != ord("\n"):
                        raise IOError(
                            "Invalid quoted printable encoding; CR must be followed by LF"
                        )
                else:
                    c1 = QuotedPrintable.__hexToBinary(b1)
                    c2 = QuotedPrintable.__hexToBinary(b2)
                    out.write((c1 << QuotedPrintable.UPPER_NIBBLE_SHIFT) | c2)
                    bytesWritten += 1
            else:
                out.write(ch)
                bytesWritten += 1
        return bytesWritten

    @staticmethod
    def __hexToBinary(b: int) -> int:

        pass  # LLM could not translate method body

    def __init__(self) -> None:

        pass

    # Class Methods End
