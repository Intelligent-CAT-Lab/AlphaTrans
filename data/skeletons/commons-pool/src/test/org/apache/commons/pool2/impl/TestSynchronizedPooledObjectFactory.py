from __future__ import annotations

# Imports Begin
from src.main.org.apache.commons.pool2.PooledObjectFactory import *
from src.main.org.apache.commons.pool2.PooledObject import *
import typing
from typing import *
import threading
import io

# Imports End


class TestSynchronizedPooledObjectFactory(PooledObjectFactory):

    # Class Fields Begin
    __writeLock: typing.Union[threading.RLock, threading.Lock] = None
    __factory: PooledObjectFactory[typing.Any] = None
    # Class Fields End

    # Class Methods Begin
    def validateObject(self, p: PooledObject[typing.Any]) -> bool:
        pass

    def toString(self) -> str:
        pass

    def passivateObject(self, p: PooledObject[typing.Any]) -> None:
        pass

    def makeObject(self) -> PooledObject[typing.Any]:
        pass

    def destroyObject0(self, p: PooledObject[typing.Any]) -> None:
        pass

    def activateObject(self, p: PooledObject[typing.Any]) -> None:
        pass

    def __init__(self, factory: PooledObjectFactory[typing.Any]) -> None:
        pass

    # Class Methods End
