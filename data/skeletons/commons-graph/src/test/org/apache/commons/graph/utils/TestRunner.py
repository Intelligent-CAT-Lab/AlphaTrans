from __future__ import annotations

# Imports Begin
from src.test.org.apache.commons.graph.utils.MultiThreadedTestRunner import *
import io
from abc import ABC

# Imports End


class TestRunner(ABC):

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
