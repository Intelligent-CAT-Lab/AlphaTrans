from __future__ import annotations

# Imports Begin
from src.main.org.apache.commons.exec.launcher.CommandLauncherFactory import *
from src.main.org.apache.commons.exec.launcher.CommandLauncher import *
from src.main.org.apache.commons.exec.ThreadUtil import *
from src.main.org.apache.commons.exec.PumpStreamHandler import *
from src.main.org.apache.commons.exec.ProcessDestroyer import *
from src.main.org.apache.commons.exec.Executor import *
from src.main.org.apache.commons.exec.ExecuteWatchdog import *
from src.main.org.apache.commons.exec.ExecuteStreamHandler import *
from src.main.org.apache.commons.exec.ExecuteResultHandler import *
from src.main.org.apache.commons.exec.ExecuteException import *
from src.main.org.apache.commons.exec.CommandLine import *
import os
import typing
from typing import *
import threading
import io
import pathlib

# Imports End


class Builder:

    # Class Fields Begin
    __threadFactory: threading.Thread = None
    __executeStreamHandler: ExecuteStreamHandler = None
    __workingDirectory: pathlib.Path = None
    # Class Fields End

    # Class Methods Begin
    def get(self) -> DefaultExecutor:
        pass

    def setWorkingDirectory(self, workingDirectory: pathlib.Path) -> typing.Any:
        pass

    def setThreadFactory(self, threadFactory: threading.Thread) -> typing.Any:
        pass

    def setExecuteStreamHandler(
        self, executeStreamHandler: ExecuteStreamHandler
    ) -> typing.Any:
        pass

    def getWorkingDirectory(self) -> pathlib.Path:
        pass

    def getThreadFactory(self) -> threading.Thread:
        pass

    def getExecuteStreamHandler(self) -> ExecuteStreamHandler:
        pass

    def asThis(self) -> typing.Any:
        pass

    # Class Methods End


class DefaultExecutor(Executor):

    # Class Fields Begin
    __executeStreamHandler: ExecuteStreamHandler = None
    __workingDirectory: pathlib.Path = None
    __watchdog: ExecuteWatchdog = None
    __exitValues: typing.List[int] = None
    __launcher: CommandLauncher = None
    __processDestroyer: ProcessDestroyer = None
    __executorThread: threading.Thread = None
    __exceptionCaught: typing.Union[IOError, OSError] = None
    __threadFactory: threading.Thread = None
    # Class Fields End

    # Class Methods Begin
    def setWorkingDirectory(self, workingDirectory: pathlib.Path) -> None:
        pass

    def setWatchdog(self, watchdog: ExecuteWatchdog) -> None:
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

    def DefaultExecutor0(self) -> DefaultExecutor:
        pass

    def __setStreams(
        self, streams: ExecuteStreamHandler, process: subprocess.Popen
    ) -> None:
        pass

    def __closeProcessStreams(self, process: subprocess.Popen) -> None:
        pass

    def _launch(
        self,
        command: CommandLine,
        env: typing.Dict[str, str],
        workingDirectory: pathlib.Path,
    ) -> subprocess.Popen:
        pass

    def _getExecutorThread(self) -> threading.Thread:
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

    def _createThread(self, runnable: typing.Callable, name: str) -> threading.Thread:
        pass

    @staticmethod
    def builder() -> Builder:
        pass

    def __setExceptionCaught(self, e: typing.Union[IOError, OSError]) -> None:
        pass

    def __getExceptionCaught(self) -> typing.Union[IOError, OSError]:
        pass

    def __executeInternal(
        self,
        command: CommandLine,
        environment: typing.Dict[str, str],
        workingDirectory: pathlib.Path,
        streams: ExecuteStreamHandler,
    ) -> int:
        pass

    def __closeCatch(self, closeable: Closeable) -> None:
        pass

    def __checkWorkingDirectory1(self, directory: pathlib.Path) -> None:
        pass

    def __checkWorkingDirectory0(self) -> None:
        pass

    def getThreadFactory(self) -> threading.Thread:
        pass

    def __init__(
        self,
        threadFactory: threading.Thread,
        executeStreamHandler: ExecuteStreamHandler,
        workingDirectory: pathlib.Path,
    ) -> None:
        pass

    # Class Methods End
