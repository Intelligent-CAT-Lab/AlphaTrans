from __future__ import annotations
import re
from io import BytesIO
from io import StringIO
import io


class Charsets:

    UTF_8: str = "utf-8"
    UTF_16LE: str = "utf-16le"
    UTF_16BE: str = "utf-16be"
    UTF_16: str = "utf-16"
    US_ASCII: str = "us-ascii"
    ISO_8859_1: str = "iso-8859-1"

    @staticmethod
    def toCharset1(charset: str) -> str:
        return charset if charset else io.open(io.StringIO()).encoding

    @staticmethod
    def toCharset0(charset: str) -> str:
        return charset if charset is not None else io.open(io.BytesIO()).encoding
