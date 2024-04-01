# Imports Begin
from src.main.org.apache.commons.graph.utils.MultiThreadedTestRunner import *
import unittest
from abc import ABC

# Imports End


class TestRunner(unittest.TestCase, Runnable, ABC):

    # Class Fields Begin
    __runner: MultiThreadedTestRunner = None
    # Class Fields End

    # Class Methods Begin
    def setTestRunner(self, runner: MultiThreadedTestRunner) -> None:

        self.__runner = runner

    def run(self) -> None:

        try:
            self.runTest()
        except Exception as e:
            self.__runner.addException(e)

    def runTest(self) -> None:

        pass

    # Class Methods End
