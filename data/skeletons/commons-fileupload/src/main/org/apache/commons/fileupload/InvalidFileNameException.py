from __future__ import annotations

# Imports Begin
import io

# Imports End


class InvalidFileNameException(RuntimeError):

    # Class Fields Begin
    __serialVersionUID: int = None
    __name: str = None
    # Class Fields End

    # Class Methods Begin
    def getName(self) -> str:
        pass

    def __init__(self, pName: str, pMessage: str) -> None:
        pass

    # Class Methods End
