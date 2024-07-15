from __future__ import annotations

# Imports Begin
from src.main.org.apache.commons.exec.Executor import *
from src.main.org.apache.commons.exec.ExecuteResultHandler import *
from src.main.org.apache.commons.exec.ExecuteException import *
import datetime
import io

# Imports End


class DefaultExecuteResultHandler(ExecuteResultHandler):

    # Class Fields Begin
    __SLEEP_TIME_MS: int = None
    __hasResult: bool = None
    __exitValue: int = None
    __exception: ExecuteException = None
    # Class Fields End

    # Class Methods Begin
    def waitFor2(self, timeoutMillis: int) -> None:
        pass

    def onProcessFailed(self, e: ExecuteException) -> None:
        pass

    def onProcessComplete(self, exitValue: int) -> None:
        pass

    def waitFor1(self, timeout: datetime.timedelta) -> None:
        pass

    def waitFor0(self) -> None:
        pass

    def hasResult(self) -> bool:
        pass

    def getExitValue(self) -> int:
        pass

    def getException(self) -> ExecuteException:
        pass

    def __init__(self) -> None:
        pass

    # Class Methods End
