# Imports Begin
from src.main.org.apache.commons.graph.utils.MultiThreadedTestRunner import *
from abc import ABC

# Imports End


class TestRunner(Runnable, ABC):

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
