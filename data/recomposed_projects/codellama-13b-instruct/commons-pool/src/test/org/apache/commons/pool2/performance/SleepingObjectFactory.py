# Imports Begin
from src.main.org.apache.commons.pool2.Waiter import *
from src.main.org.apache.commons.pool2.PooledObject import *
import unittest
import typing
from typing import *

# Imports End


class SleepingObjectFactory(unittest.TestCase):

    # Class Fields Begin
    __counter: int = None
    __debug: bool = None
    # Class Fields End

    # Class Methods Begin
    def validateObject(self, obj: PooledObject[int]) -> bool:

        self.__debug("validateObject", obj)
        Waiter.sleepQuietly(30)
        return True

    def setDebug(self, b: bool) -> None:

        self.__debug = b

    def passivateObject(self, obj: PooledObject[int]) -> None:

        pass  # LLM could not translate method body

    def isDebug(self) -> bool:

        return self.__debug

    def destroyObject(self, obj: PooledObject[int]) -> None:

        self.__debug("destroyObject", obj)
        Waiter.sleepQuietly(250)

    def activateObject(self, obj: PooledObject[int]) -> None:

        self.__debug("activateObject", obj)
        Waiter.sleepQuietly(10)

    def __debug(self, method: str, obj: typing.Any) -> None:

        if self.__debug:
            thread = "thread" + threading.current_thread().name
            print(thread + ": " + method + " " + str(obj))

    # Class Methods End
