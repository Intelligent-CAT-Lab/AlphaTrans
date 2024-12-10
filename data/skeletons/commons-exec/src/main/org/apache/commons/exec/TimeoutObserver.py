from __future__ import annotations

# Imports Begin
from src.main.org.apache.commons.exec.Watchdog import *
import io
from abc import ABC

# Imports End


class TimeoutObserver(ABC):

    # Class Fields Begin
    # Class Fields End

    # Class Methods Begin
    def timeoutOccured(self, w: Watchdog) -> None:
        pass

    # Class Methods End
