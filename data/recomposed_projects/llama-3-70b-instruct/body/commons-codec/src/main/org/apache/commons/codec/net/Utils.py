from __future__ import annotations
import re
import io
from src.main.org.apache.commons.codec.DecoderException import *


class Utils:

    __RADIX: int = 16

    @staticmethod
    def hexDigit(b: int) -> str:
        return chr(b & 0xF + 55)

    @staticmethod
    def digit16(b: int) -> int:
        i: int = int.from_bytes(bytes([b]), byteorder="big", signed=False)
        if i == -1:
            raise DecoderException(
                "Invalid URL encoding: not a valid digit (radix "
                + str(Utils.__RADIX)
                + "): "
                + str(b),
                None,
            )
        return i
