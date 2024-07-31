from __future__ import annotations

# Imports Begin
from src.main.org.apache.commons.exec.ProcessDestroyer import *
import typing
from typing import *
import threading
import io

# Imports End


class ProcessDestroyerThread(threading.Thread):

    # Class Fields Begin
    __shouldDestroy: bool = None
    # Class Fields End

    # Class Methods Begin
    def run(self) -> None:
        pass

    def setShouldDestroy(self, shouldDestroy: bool) -> None:
        pass

    def __init__(self) -> None:
        pass

    # Class Methods End


class ShutdownHookProcessDestroyer(ProcessDestroyer):

    # Class Fields Begin
    __processes: typing.List[subprocess.Popen] = None
    __destroyProcessThread: ProcessDestroyerThread = None
    __added: bool = None
    __running: bool = None
    # Class Fields End

    # Class Methods Begin
    def size(self) -> int:
        pass

    def run(self) -> None:
        pass

    def remove(self, process: subprocess.Popen) -> bool:
        pass

    def add(self, process: subprocess.Popen) -> bool:
        pass

    def isEmpty(self) -> bool:
        pass

    def isAddedAsShutdownHook(self) -> bool:
        pass

    def __init__(self) -> None:
        pass

    def __removeShutdownHook(self) -> None:
        pass

    def __addShutdownHook(self) -> None:
        pass

    # Class Methods End
