from __future__ import annotations

# Imports Begin
from src.main.org.fusesource.jansi.internal.Kernel32 import *
import io

# Imports End


class WindowsSupport:

    # Class Fields Begin
    # Class Fields End

    # Class Methods Begin
    @staticmethod
    def getErrorMessage(errorCode: int) -> str:
        pass

    @staticmethod
    def getLastErrorMessage() -> str:
        pass

    # Class Methods End
