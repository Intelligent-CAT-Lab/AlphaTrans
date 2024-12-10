from __future__ import annotations

# Imports Begin
import typing
from typing import *
import io
from io import IOBase

# Imports End


class MingwSupport:

    # Class Fields Begin
    __sttyCommand: str = None
    __ttyCommand: str = None
    __columnsPatterns: re.Pattern = None
    # Class Fields End

    # Class Methods Begin
    def getTerminalWidth(self, name: str) -> int:
        pass

    def getConsoleName(self, stdout: bool) -> str:
        pass

    def __init__(self) -> None:
        pass

    def __getRedirect(self, fd: io.RawIOBase) -> typing.Any:
        pass

    @staticmethod
    def __waitAndCapture(p: subprocess.Popen) -> str:
        pass

    # Class Methods End
