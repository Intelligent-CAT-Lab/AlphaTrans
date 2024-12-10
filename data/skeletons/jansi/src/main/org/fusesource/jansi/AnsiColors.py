from __future__ import annotations

# Imports Begin
import io

# Imports End


class AnsiColors:

    # Class Fields Begin
    Colors16: AnsiColors = None
    Colors256: AnsiColors = None
    TrueColor: AnsiColors = None
    __description: str = None
    # Class Fields End

    # Class Methods Begin
    def __init__(self, description: str) -> None:
        pass

    def getDescription(self) -> str:
        pass

    # Class Methods End
