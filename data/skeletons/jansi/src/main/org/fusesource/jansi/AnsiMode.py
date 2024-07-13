from __future__ import annotations

# Imports Begin
import io

# Imports End


class AnsiMode:

    # Class Fields Begin
    Strip: AnsiMode = None
    Default: AnsiMode = None
    Force: AnsiMode = None
    __description: str = None
    # Class Fields End

    # Class Methods Begin
    def __init__(self, description: str) -> None:
        pass

    def getDescription(self) -> str:
        pass

    # Class Methods End
