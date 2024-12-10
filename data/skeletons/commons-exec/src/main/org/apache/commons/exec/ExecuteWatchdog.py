from __future__ import annotations

# Imports Begin
from src.main.org.apache.commons.exec.util.DebugUtils import *
from src.main.org.apache.commons.exec.Watchdog import *
from src.main.org.apache.commons.exec.TimeoutObserver import *
import datetime
import threading
import io

# Imports End


class Builder:

    # Class Fields Begin
    __threadFactory: threading.Thread = None
    __timeout: datetime.timedelta = None
    # Class Fields End

    # Class Methods Begin
    def get(self) -> ExecuteWatchdog:
        pass

    def setTimeout(self, timeout: datetime.timedelta) -> Builder:
        pass

    def setThreadFactory(self, threadFactory: threading.Thread) -> Builder:
        pass

    # Class Methods End


class ExecuteWatchdog(TimeoutObserver):

    # Class Fields Begin
    INFINITE_TIMEOUT_DURATION: datetime.timedelta = None
    __process: subprocess.Popen = None
    __hasWatchdog: bool = None
    __watch: bool = None
    __caught: Exception = None
    __killedProcess: bool = None
    __watchdog: Watchdog = None
    __processStarted: bool = None
    __threadFactory: threading.Thread = None
    INFINITE_TIMEOUT: int = None
    # Class Fields End

    # Class Methods Begin
    def timeoutOccured(self, w: Watchdog) -> None:
        pass

    @staticmethod
    def ExecuteWatchdog0(timeoutMillis: int) -> ExecuteWatchdog:
        pass

    def stop(self) -> None:
        pass

    def start(self, processToMonitor: subprocess.Popen) -> None:
        pass

    def killedProcess(self) -> bool:
        pass

    def isWatching(self) -> bool:
        pass

    def failedToStart(self, e: Exception) -> None:
        pass

    def destroyProcess(self) -> None:
        pass

    def _cleanUp(self) -> None:
        pass

    def checkException(self) -> None:
        pass

    @staticmethod
    def builder() -> Builder:
        pass

    def __ensureStarted(self) -> None:
        pass

    def __init__(
        self, threadFactory: threading.Thread, timeout: datetime.timedelta
    ) -> None:
        pass

    def setProcessNotStarted(self) -> None:
        pass

    # Class Methods End
