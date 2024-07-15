from __future__ import annotations

# Imports Begin
import typing
from typing import *
import io

# Imports End


class AnsiType:

    # Class Fields Begin
    Native: AnsiType = None
    Unsupported: AnsiType = None
    VirtualTerminal: AnsiType = None
    Emulation: AnsiType = None
    Redirected: AnsiType = None
    __description: str = None
    # Class Fields End

    # Class Methods Begin
    def __init__(self, description: str) -> None:
        pass

    def getDescription(self) -> str:
        pass

    # Class Methods End
