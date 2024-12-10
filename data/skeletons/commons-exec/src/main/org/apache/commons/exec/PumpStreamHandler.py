from __future__ import annotations

# Imports Begin
from src.main.org.apache.commons.exec.util.DebugUtils import *
from src.main.org.apache.commons.exec.ThreadUtil import *
from src.main.org.apache.commons.exec.StreamPumper import *
from src.main.org.apache.commons.exec.InputStreamPumper import *
from src.main.org.apache.commons.exec.Executor import *
from src.main.org.apache.commons.exec.ExecuteStreamHandler import *
from src.main.org.apache.commons.exec.ExecuteException import *
import os
import datetime
import typing
from typing import *
from io import BytesIO
import threading
import io
from io import StringIO

# Imports End


class PumpStreamHandler(ExecuteStreamHandler):

    # Class Fields Begin
    __STOP_TIMEOUT_ADDITION: datetime.timedelta = None
    __outputThread: threading.Thread = None
    __errorThread: threading.Thread = None
    __inputThread: threading.Thread = None
    __outputStream: typing.Union[io.BytesIO, io.StringIO, io.BufferedWriter] = None
    __errorOutputStream: typing.Union[io.BytesIO, io.StringIO, io.BufferedWriter] = None
    __inputStream: typing.Union[io.BytesIO, io.StringIO, io.BufferedReader] = None
    __inputStreamPumper: InputStreamPumper = None
    __stopTimeout: datetime.timedelta = None
    __caught: typing.Union[IOError, OSError] = None
    __threadFactory: threading.Thread = None
    # Class Fields End

    # Class Methods Begin
    def setStopTimeout1(self, timeout: int) -> None:
        pass

    def setProcessOutputStream(
        self, is_: typing.Union[io.BytesIO, io.StringIO, io.BufferedReader]
    ) -> None:
        pass

    def setProcessInputStream(
        self, os: typing.Union[io.BytesIO, io.StringIO, io.BufferedWriter]
    ) -> None:
        pass

    def setProcessErrorStream(
        self, is_: typing.Union[io.BytesIO, io.StringIO, io.BufferedReader]
    ) -> None:
        pass

    def _stopThread(self, thread: threading.Thread, timeoutMillis: int) -> None:
        pass

    def stop0(self) -> None:
        pass

    def stop(self) -> None:
        pass

    def start0(self) -> None:
        pass

    def start(self) -> None:
        pass

    def setStopTimeout0(self, timeout: datetime.timedelta) -> None:
        pass

    def _getOut(self) -> typing.Union[io.BytesIO, io.StringIO, io.BufferedWriter]:
        pass

    def _getErr(self) -> typing.Union[io.BytesIO, io.StringIO, io.BufferedWriter]:
        pass

    def _createPump1(
        self,
        is_: typing.Union[io.BytesIO, io.StringIO, io.BufferedReader],
        os: typing.Union[io.BytesIO, io.StringIO, io.BufferedWriter],
        closeWhenExhausted: bool,
    ) -> threading.Thread:
        pass

    def _createPump0(
        self,
        is_: typing.Union[io.BytesIO, io.StringIO, io.BufferedReader],
        os: typing.Union[io.BytesIO, io.StringIO, io.BufferedWriter],
    ) -> threading.Thread:
        pass

    def _createProcessOutputPump(
        self,
        is_: typing.Union[io.BytesIO, io.StringIO, io.BufferedReader],
        os: typing.Union[io.BytesIO, io.StringIO, io.BufferedWriter],
    ) -> None:
        pass

    def _createProcessErrorPump(
        self,
        is_: typing.Union[io.BytesIO, io.StringIO, io.BufferedReader],
        os: typing.Union[io.BytesIO, io.StringIO, io.BufferedWriter],
    ) -> None:
        pass

    @staticmethod
    def PumpStreamHandler3(
        outputStream: typing.Union[io.BytesIO, io.StringIO, io.BufferedWriter],
        errorOutputStream: typing.Union[io.BytesIO, io.StringIO, io.BufferedWriter],
        inputStream: typing.Union[io.BytesIO, io.StringIO, io.BufferedReader],
    ) -> PumpStreamHandler:
        pass

    @staticmethod
    def PumpStreamHandler2(
        outputStream: typing.Union[io.BytesIO, io.StringIO, io.BufferedWriter],
        errorOutputStream: typing.Union[io.BytesIO, io.StringIO, io.BufferedWriter],
    ) -> PumpStreamHandler:
        pass

    @staticmethod
    def PumpStreamHandler1(
        allOutputStream: typing.Union[io.BytesIO, io.StringIO, io.BufferedWriter]
    ) -> PumpStreamHandler:
        pass

    @staticmethod
    def PumpStreamHandler0() -> PumpStreamHandler:
        pass

    def __stop1(self, thread: threading.Thread, timeout: datetime.timedelta) -> None:
        pass

    def __start1(self, thread: threading.Thread) -> None:
        pass

    def __createSystemInPump(
        self,
        is_: typing.Union[io.BytesIO, io.StringIO, io.BufferedReader],
        os: typing.Union[io.BytesIO, io.StringIO, io.BufferedWriter],
    ) -> threading.Thread:
        pass

    def __init__(
        self,
        threadFactory: threading.Thread,
        outputStream: typing.Union[io.BytesIO, io.StringIO, io.BufferedWriter],
        errorOutputStream: typing.Union[io.BytesIO, io.StringIO, io.BufferedWriter],
        inputStream: typing.Union[io.BytesIO, io.StringIO, io.BufferedReader],
    ) -> None:
        pass

    def getStopTimeout(self) -> datetime.timedelta:
        pass

    # Class Methods End
