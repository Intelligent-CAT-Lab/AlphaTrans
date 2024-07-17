import pytest

from abc import ABC, abstractmethod

class TestRunner(ABC):
    def __init__(self) -> None:
        self.__runner = None

    def run(self) -> None:
        try:
            self.runTest()
        except Exception as e:
            if self.__runner is not None:
                self.__runner.addException(e)

    @abstractmethod
    def runTest(self) -> None:
        pass

    def setTestRunner(self, runner) -> None:
        self.__runner = runner
