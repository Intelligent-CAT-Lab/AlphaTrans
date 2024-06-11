from __future__ import annotations
import io
import typing
from typing import *


class Util:

    EMPTY_STRING_ARRAY: typing.List[str] = []

    @staticmethod
    def stripLeadingHyphens(str: str) -> str:

        if str is None:
            return None
        if str.startswith("--"):
            return str[2:]
        if str.startswith("-"):
            return str[1:]

        return str

    @staticmethod
    def stripLeadingAndTrailingQuotes(str: str) -> str:

        length = len(str)
        if (
            length > 1
            and str.startswith('"')
            and str.endswith('"')
            and str[1 : length - 1].find('"') == -1
        ):
            str = str[1 : length - 1]

        return str
