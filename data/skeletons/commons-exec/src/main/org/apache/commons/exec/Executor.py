from __future__ import annotations

# Imports Begin
from src.main.org.apache.commons.exec.ProcessDestroyer import *
from src.main.org.apache.commons.exec.ExecuteWatchdog import *
from src.main.org.apache.commons.exec.ExecuteStreamHandler import *
from src.main.org.apache.commons.exec.ExecuteResultHandler import *
from src.main.org.apache.commons.exec.ExecuteException import *
from src.main.org.apache.commons.exec.CommandLine import *
import typing
from typing import *
import io
import pathlib
from abc import ABC

# Imports End


class Executor(ABC):

    # Class Fields Begin
    INVALID_EXITVALUE: int = None
    # Class Fields End

    # Class Methods Begin
    def setWorkingDirectory(self, dir_: pathlib.Path) -> None:
        pass

    def setWatchdog(self, watchDog: ExecuteWatchdog) -> None:
        pass

    def setStreamHandler(self, streamHandler: ExecuteStreamHandler) -> None:
        pass

    def setProcessDestroyer(self, processDestroyer: ProcessDestroyer) -> None:
        pass

    def setExitValues(self, values: typing.List[int]) -> None:
        pass

    def setExitValue(self, value: int) -> None:
        pass

    def isFailure(self, exitValue: int) -> bool:
        pass

    def getWorkingDirectory(self) -> pathlib.Path:
        pass

    def getWatchdog(self) -> ExecuteWatchdog:
        pass

    def getStreamHandler(self) -> ExecuteStreamHandler:
        pass

    def getProcessDestroyer(self) -> ProcessDestroyer:
        pass

    def execute3(
        self,
        command: CommandLine,
        environment: typing.Dict[str, str],
        handler: ExecuteResultHandler,
    ) -> None:
        pass

    def execute2(self, command: CommandLine, environment: typing.Dict[str, str]) -> int:
        pass

    def execute1(self, command: CommandLine, handler: ExecuteResultHandler) -> None:
        pass

    def execute0(self, command: CommandLine) -> int:
        pass

    # Class Methods End
