from __future__ import annotations
import io
import typing
from typing import *
from src.main.org.apache.commons.pool2.PooledObject import *
from src.test.org.apache.commons.pool2.Waiter import *


class SleepingObjectFactory:

    __debug: bool = None
    __counter: int = None

    def validateObject(self, obj: PooledObject[int]) -> bool:

        self.__debug("validateObject", obj)
        Waiter.sleepQuietly(30)
        return True

    def setDebug(self, b: bool) -> None:

        self.__debug = b

    def ivateObject(self, obj: PooledObject[int]) -> None:

        self.__debug("passivateObject", obj)
        Waiter.sleepQuietly(10)

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
            thread = "thread" + threading.current_thread().getName()
            print(thread + ": " + method + " " + str(obj))
