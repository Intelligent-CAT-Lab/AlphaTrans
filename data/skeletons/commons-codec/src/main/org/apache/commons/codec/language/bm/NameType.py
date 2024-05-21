from __future__ import annotations

# Imports Begin
import typing
from typing import *
import io

# Imports End


class NameType:

    # Class Fields Begin
    ASHKENAZI: NameType = None
    GENERIC: NameType = None
    SEPHARDIC: NameType = None
    __name: str = None
    # Class Fields End

    # Class Methods Begin
    def getName(self) -> str:
        pass

    def __init__(self, name: str) -> None:
        pass

    # Class Methods End
