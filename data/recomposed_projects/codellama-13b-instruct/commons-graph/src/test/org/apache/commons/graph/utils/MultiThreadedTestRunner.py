# Imports Begin
from src.main.org.apache.commons.graph.utils.TestRunner import *
import unittest
import typing
from typing import *

# Imports End


class MultiThreadedTestRunner(unittest.TestCase):

    # Class Fields Begin
    __th: typing.List[threading.Thread] = None
    __exceptions: typing.List[BaseException] = None
    # Class Fields End

    # Class Methods Begin
    def runRunnables(self) -> None:

        for t in self.th:
            t.start()
        for t in self.th:
            t.join(self.maxWait)
        if len(self.exceptions) > 0:
            raise self.exceptions[0]

    def addException(self, e: BaseException) -> None:

        self.__exceptions.append(e)

    def __init__(self, runnables: typing.List[TestRunner]) -> None:

        self.th = []
        self.exceptions = []
        for i in range(len(runnables)):
            runnables[i].setTestRunner(self)
            self.th.append(threading.Thread(target=runnables[i]))

    # Class Methods End
