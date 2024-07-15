from __future__ import annotations

# Imports Begin
from src.main.org.apache.commons.exec.ExecuteStreamHandler import *
from src.main.org.apache.commons.exec.DefaultExecutor import *
import typing
from typing import *
import threading
import io
import pathlib

# Imports End


class Builder:

    # Class Fields Begin
    # Class Fields End

    # Class Methods Begin
    def get(self) -> DefaultExecutor:
        pass

    # Class Methods End


class DaemonExecutor(DefaultExecutor):

    # Class Fields Begin
    # Class Fields End

    # Class Methods Begin
    def _createThread(self, runnable: typing.Callable, name: str) -> threading.Thread:
        pass

    @staticmethod
    def builder() -> Builder:
        pass

    def __init__(
        self,
        threadFactory: threading.Thread,
        executeStreamHandler: ExecuteStreamHandler,
        workingDirectory: pathlib.Path,
    ) -> None:
        pass

    # Class Methods End
