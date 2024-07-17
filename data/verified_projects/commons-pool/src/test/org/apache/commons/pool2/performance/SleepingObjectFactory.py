import pytest

from src.test.org.apache.commons.pool2.Waiter import *
from src.main.org.apache.commons.pool2.PooledObject import *
import threading
import typing


class SleepingObjectFactory:

    def __init__(self) -> None:
        self.__counter = 0
        self.__debug = False

    
    def activateObject(self, obj: PooledObject) -> None:
        try:
            self.__debug("activateObject", obj)
            Waiter.sleepQuietly(10)
        except Exception as e:
            raise e
    
    
    def __debug(self, method: str, obj: typing.Any) -> None:
        if self.__debug:
            thread = "thread" + threading.current_thread().name
            print(thread + ": " + method + " " + str(obj))
    
    
    def destroyObject(self, obj: PooledObject) -> None:
        try:
            self.__debug("destroyObject", obj)
            Waiter.sleepQuietly(250)
        except Exception as e:
            raise e


    def isDebug(self) -> bool:
        return self.__debug


    def passivateObject(self, obj: PooledObject) -> None:
        try:
            self.__debug("passivateObject", obj)
            Waiter.sleepQuietly(10)
        except Exception as e:
            raise e

    
    def setDebug(self, b: bool) -> None:
        self.__debug = b

    
    def validateObject(self, obj: PooledObject) -> bool:
        self.__debug("validateObject", obj)
        Waiter.sleepQuietly(30)
        return True
