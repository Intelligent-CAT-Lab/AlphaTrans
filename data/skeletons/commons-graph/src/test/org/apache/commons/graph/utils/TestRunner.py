from __future__ import annotations

# Imports Begin
from src.test.org.apache.commons.graph.utils.MultiThreadedTestRunner import *
import typing
from typing import *
import io
from abc import ABC

# Imports End


class TestRunner(typing.Callable, ABC):

    # Class Fields Begin
    __runner: MultiThreadedTestRunner = None
    # Class Fields End

    # Class Methods Begin
    def setTestRunner(self, runner: MultiThreadedTestRunner) -> None:
        pass

    def run(self) -> None:
        pass

    def runTest(self) -> None:
        pass

    # Class Methods End
