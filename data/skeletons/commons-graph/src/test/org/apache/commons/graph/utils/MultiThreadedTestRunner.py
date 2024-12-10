from __future__ import annotations

# Imports Begin
from src.test.org.apache.commons.graph.utils.TestRunner import *
import typing
from typing import *
import threading
import io

# Imports End


class MultiThreadedTestRunner:

    # Class Fields Begin
    __th: typing.List[threading.Thread] = None
    maxWait: int = None
    __exceptions: typing.List[BaseException] = None
    # Class Fields End

    # Class Methods Begin
    def runRunnables(self) -> None:
        pass

    def addException(self, e: BaseException) -> None:
        pass

    def __init__(self, runnables: typing.List[TestRunner]) -> None:
        pass

    # Class Methods End
