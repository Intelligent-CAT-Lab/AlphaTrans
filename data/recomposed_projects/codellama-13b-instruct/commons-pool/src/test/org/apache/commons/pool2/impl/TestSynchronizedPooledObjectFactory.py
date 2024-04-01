# Imports Begin
from src.main.org.apache.commons.pool2.PooledObjectFactory import *
from src.main.org.apache.commons.pool2.PooledObject import *
import unittest
import typing
from typing import *
# Imports End

class TestSynchronizedPooledObjectFactory(unittest.TestCase, PooledObjectFactory<T>):

    # Class Fields Begin
    __writeLock: typing.Union[threading.RLock, threading.Lock] = "" # LLM could not translate field
    __factory: PooledObjectFactory[typing.Any] = None
    # Class Fields End

    # Class Methods Begin
    def validateObject(self, p: PooledObject[typing.Any]) -> bool:

            with self.__writeLock:
                return self.__factory.validateObject(p)

    def toString(self) -> str:

            return f"SynchronizedPoolableObjectFactory{{factory={self.__factory}}}"

    def passivateObject(self, p: PooledObject[typing.Any]) -> None:


        pass # LLM could not translate method body

    def makeObject(self) -> PooledObject[typing.Any]:

            with self.__writeLock:
                return self.__factory.makeObject()

    def destroyObject0(self, p: PooledObject[typing.Any]) -> None:

            with self.__writeLock:
                self.__factory.destroyObject0(p)

    def activateObject(self, p: PooledObject[typing.Any]) -> None:

            with self.__writeLock:
                self.__factory.activateObject(p)

    def __init__(self, factory: PooledObjectFactory[typing.Any]) -> None:

        if factory is None:
            raise IllegalArgumentException("factory must not be null.")
        self.__factory = factory

    # Class Methods End


