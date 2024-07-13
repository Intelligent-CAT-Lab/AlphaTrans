from __future__ import annotations

# Imports Begin
from src.main.org.apache.commons.exec.ExecuteException import *
import io
from abc import ABC

# Imports End


class ExecuteResultHandler(ABC):

    # Class Fields Begin
    # Class Fields End

    # Class Methods Begin
    def onProcessFailed(self, e: ExecuteException) -> None:
        pass

    def onProcessComplete(self, exitValue: int) -> None:
        pass

    # Class Methods End
