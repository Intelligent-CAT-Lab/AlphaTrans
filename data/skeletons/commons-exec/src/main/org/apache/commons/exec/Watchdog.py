from __future__ import annotations

# Imports Begin
from src.main.org.apache.commons.exec.TimeoutObserver import *
from src.main.org.apache.commons.exec.ThreadUtil import *
import datetime
import typing
from typing import *
import threading
import io

# Imports End


class Builder:

    # Class Fields Begin
    __threadFactory: threading.Thread = None
    __timeout: datetime.timedelta = None
    # Class Fields End

    # Class Methods Begin
    def get(self) -> Watchdog:
        pass

    def setTimeout(self, timeout: datetime.timedelta) -> Builder:
        pass

    def setThreadFactory(self, threadFactory: threading.Thread) -> Builder:
        pass

    # Class Methods End


class Watchdog:

    # Class Fields Begin
    __observers: typing.List[TimeoutObserver] = None
    __timeoutMillis: int = None
    __stopped: bool = None
    __threadFactory: threading.Thread = None
    # Class Fields End

    # Class Methods Begin
    def run(self) -> None:
        pass

    @staticmethod
    def Watchdog0(timeoutMillis: int) -> Watchdog:
        pass

    def stop(self) -> None:
        pass

    def start(self) -> None:
        pass

    def removeTimeoutObserver(self, to: TimeoutObserver) -> None:
        pass

    def _fireTimeoutOccured(self) -> None:
        pass

    def addTimeoutObserver(self, to: TimeoutObserver) -> None:
        pass

    @staticmethod
    def builder() -> Builder:
        pass

    def __init__(
        self, threadFactory: threading.Thread, timeout: datetime.timedelta
    ) -> None:
        pass

    # Class Methods End
