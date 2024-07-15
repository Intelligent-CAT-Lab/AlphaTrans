from __future__ import annotations
import re
import unittest
import pytest
import io
import threading
import typing
from typing import *
from src.main.org.apache.commons.pool2.PooledObject import *
from src.main.org.apache.commons.pool2.PooledObjectFactory import *


class TestSynchronizedPooledObjectFactory(PooledObjectFactory):

    __factory: PooledObjectFactory[typing.Any] = None

    __writeLock: typing.Union[threading.RLock, threading.Lock] = threading.RLock()

    def validateObject(self, p: PooledObject[typing.Any]) -> bool:
        with self.__writeLock:
            return self.__factory.validateObject(p)

    def toString(self) -> str:
        sb = StringBuilder()
        sb.append("SynchronizedPoolableObjectFactory")
        sb.append("{factory=").append(self.__factory)
        sb.append("}")
        return sb.toString()

    def passivateObject(self, p: PooledObject[typing.Any]) -> None:
        with self.__writeLock:
            self.__factory.passivateObject(p)

    def makeObject(self) -> PooledObject[typing.Any]:
        with self.__writeLock:
            return self.__factory.makeObject()

    def destroyObject0(self, p: PooledObject[typing.Any]) -> None:
        with self.__writeLock:
            self.__factory.destroyObject0(p)

    def activateObject(self, p: PooledObject[typing.Any]) -> None:
        self.__writeLock.acquire()
        try:
            self.__factory.activateObject(p)
        finally:
            self.__writeLock.release()

    def __init__(self, factory: PooledObjectFactory[typing.Any]) -> None:

        pass  # LLM could not translate this method
