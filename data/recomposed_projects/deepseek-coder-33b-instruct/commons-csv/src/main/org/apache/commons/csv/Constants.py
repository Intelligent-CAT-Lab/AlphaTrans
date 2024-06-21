from __future__ import annotations
import re
import io
import typing
from typing import *


class Constants:

    US: str = "\x1f"
    UNDEFINED: int = -2
    TAB: str = "\t"
    SQL_NULL_STRING: str = "\\N"
    SP: str = " "
    RS: str = "\x1e"
    PIPE: str = "|"
    PARAGRAPH_SEPARATOR: str = "\u2029"
    NEXT_LINE: str = "\u0085"
    LINE_SEPARATOR: str = "\u2028"
    LF: str = "\n"
    FF: str = "\f"
    END_OF_STREAM: int = -1
    EMPTY_STRING_ARRAY: typing.List[str] = []

    EMPTY: str = ""
    DOUBLE_QUOTE_CHAR: str = '"'
    CRLF: str = "\r\n"
    CR: str = "\r"
    COMMENT: str = "#"
    COMMA: str = ","
    BACKSPACE: str = "\b"
    BACKSLASH: str = "\\"

    def __init__(self) -> None:
        pass
