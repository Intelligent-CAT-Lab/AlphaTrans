import pytest

from src.test.org.apache.commons.graph.utils.TestRunner import TestRunner
import typing
from typing import *

import threading

class MultiThreadedTestRunner:
    def __init__(self, runnables: typing.List[TestRunner]) -> None:
        self.__th = []
        self.maxWait = 60 * 60 * 1000
        self.__exceptions = []
        for i in range(len(runnables)):
            runnables[i].setTestRunner(self)
            self.__th.append(threading.Thread(target=runnables[i].run))

    def addException(self, e: BaseException) -> None:
        self.__exceptions.append(e)

    def runRunnables(self) -> None:
        for t in self.__th:
            t.start()

        for t in self.__th:
            t.join(self.maxWait / 1000)

        if len(self.__exceptions) > 0:
            raise self.__exceptions[0]
