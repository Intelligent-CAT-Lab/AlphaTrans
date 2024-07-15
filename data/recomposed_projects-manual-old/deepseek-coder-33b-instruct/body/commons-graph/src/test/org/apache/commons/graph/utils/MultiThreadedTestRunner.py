from __future__ import annotations
import re
import unittest
import pytest
import io
import threading
import typing
from typing import *
from src.test.org.apache.commons.graph.utils.TestRunner import *


class MultiThreadedTestRunner:

    __exceptions: typing.List[BaseException] = None

    __th: typing.List[threading.Thread] = None

    maxWait: int = 60 * 60 * 1000

    def runRunnables(self) -> None:

        for t in self.__th:
            t.start()

        for t in self.__th:
            t.join(maxWait)

        if len(self.__exceptions) > 0:
            raise self.__exceptions[0]

    def addException(self, e: BaseException) -> None:
        self.__exceptions.append(e)

    def __init__(self, runnables: typing.List[TestRunner]) -> None:
        self.__th = []
        self.__exceptions = []
        for i in range(len(runnables)):
            runnables[i].setTestRunner(self)
            self.__th.append(threading.Thread(target=runnables[i].run))
