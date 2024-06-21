from __future__ import annotations
import re
import io
from src.main.org.apache.commons.codec.DecoderException import *


class Utils:

    __RADIX: int = 16

    @staticmethod
    def hexDigit(b: int) -> str:

        return hex(b & 0xF)[2:].upper()

    @staticmethod
    def digit16(b: int) -> int:

        i = int.from_bytes([b], byteorder="big")
        if i < 0 or i > 15:
            raise DecoderException(
                "Invalid URL encoding: not a valid digit (radix "
                + str(Utils.__RADIX)
                + "): "
                + str(b),
                None,
            )
        return i
