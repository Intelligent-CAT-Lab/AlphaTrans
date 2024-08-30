from __future__ import annotations

# Imports Begin
from src.main.org.fusesource.jansi.io.AnsiOutputStream import *
from src.main.org.fusesource.jansi.AnsiType import *
from src.main.org.fusesource.jansi.AnsiMode import *
from src.main.org.fusesource.jansi.AnsiColors import *
import os
import typing
from typing import *
import io

# Imports End


class AnsiPrintStream:

    # Class Fields Begin
    # Class Fields End

    # Class Methods Begin
    def toString(self) -> str:
        pass

    def uninstall(self) -> None:
        pass

    def install(self) -> None:
        pass

    def getTerminalWidth(self) -> int:
        pass

    def setResetAtUninstall(self, resetAtClose: bool) -> None:
        pass

    def isResetAtUninstall(self) -> bool:
        pass

    def setMode(self, ansiMode: AnsiMode) -> None:
        pass

    def getMode(self) -> AnsiMode:
        pass

    def getColors(self) -> AnsiColors:
        pass

    def getType(self) -> AnsiType:
        pass

    def _getOut(self) -> AnsiOutputStream:
        pass

    def __init__(
        self, out: AnsiOutputStream, autoFlush: bool, args: typing.Any
    ) -> None:
        pass

    @staticmethod
    def __determineEncoding(args: typing.Any) -> str:
        pass

    # Class Methods End
