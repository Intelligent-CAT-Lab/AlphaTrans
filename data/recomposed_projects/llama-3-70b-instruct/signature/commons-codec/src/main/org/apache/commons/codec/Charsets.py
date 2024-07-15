from __future__ import annotations
import re
import io


class Charsets:

    UTF_8: str = "UTF_8"
    UTF_16: str = "UTF_16"
    US_ASCII: str = "US-ASCII"
    ISO_8859_1: str = "ISO-8859-1"
    UTF_16LE: str = "UTF_16LE"
    UTF_16BE: str = "UTF_16BE"

    @staticmethod
    def toCharset1(charset: str) -> str:
        return charset if charset is not None else Charset.defaultCharset()

    @staticmethod
    def toCharset0(charset: str) -> str:
        return charset if charset is not None else Charset.defaultCharset()
