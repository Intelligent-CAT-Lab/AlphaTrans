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

    __writeLock: typing.Union[threading.RLock, threading.Lock] = threading.Lock()

    def validateObject(self, p: PooledObject[typing.Any]) -> bool:

        self.__writeLock.acquire()
        try:
            return self.__factory.validateObject(p)
        finally:
            self.__writeLock.release()

    def toString(self) -> str:
        return f"SynchronizedPoolableObjectFactory{{factory={self.__factory}}}"

    def passivateObject(self, p: PooledObject[typing.Any]) -> None:

        self.__writeLock.acquire()
        try:
            self.__factory.passivateObject(p)
        finally:
            self.__writeLock.release()

    def makeObject(self) -> PooledObject[typing.Any]:
        with self.__writeLock:
            return self.__factory.makeObject()

    def destroyObject0(self, p: PooledObject[typing.Any]) -> None:

        self.__writeLock.acquire()
        try:
            self.__factory.destroyObject0(p)
        finally:
            self.__writeLock.release()

    def activateObject(self, p: PooledObject[typing.Any]) -> None:

        self.__writeLock.acquire()
        try:
            self.__factory.activateObject(p)
        finally:
            self.__writeLock.release()

    def __init__(self, factory: PooledObjectFactory[typing.Any]) -> None:
        if factory is None:
            raise ValueError("factory must not be null.")
        self.__factory = factory
