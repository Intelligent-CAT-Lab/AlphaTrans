from __future__ import annotations
import re
import io
import typing
from typing import *


class Util:

    EMPTY_STRING_ARRAY: List[str] = []

    @staticmethod
    def stripLeadingHyphens(str_: str) -> str:

        if str_ is None:
            return None
        if str_.startswith("--"):
            return str_[2:]
        if str_.startswith("-"):
            return str_[1:]

        return str_

    @staticmethod
    def stripLeadingAndTrailingQuotes(str_: str) -> str:

        length = len(str_)
        if (
            length > 1
            and str_.startswith('"')
            and str_.endswith('"')
            and str_[1 : length - 1].find('"') == -1
        ):
            str_ = str_[1 : length - 1]

        return str_
