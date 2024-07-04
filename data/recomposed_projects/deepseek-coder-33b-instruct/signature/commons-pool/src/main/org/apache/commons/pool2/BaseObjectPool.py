from __future__ import annotations
import re
from abc import ABC
import io
import typing
from typing import *
import os
from src.main.org.apache.commons.pool2.BaseObject import *
from src.main.org.apache.commons.pool2.ObjectPool import *


class BaseObjectPool(BaseObject, ObjectPool, ABC):

    __closed: bool = False

    def _toStringAppendFields(self, builder: str) -> None:
        builder += "closed="
        builder += str(self.__closed)

    def getNumIdle(self) -> int:
        return -1

    def getNumActive(self) -> int:
        return -1

    def close(self) -> None:
        self.__closed = True

    def clear(self) -> None:
        raise NotImplementedError()

    def addObject(self) -> None:
        raise NotImplementedError()

    def isClosed(self) -> bool:
        return self.__closed

    def _assertOpen(self) -> None:
        if self.isClosed():
            raise RuntimeError("Pool not open")

    def returnObject(self, obj: typing.Any) -> None:
        raise NotImplementedError("Subclass must implement abstract method")

    def invalidateObject0(self, obj: typing.Any) -> None:
        raise NotImplementedError("Subclass must implement abstract method")

    def borrowObject(self) -> typing.Any:
        raise NotImplementedError("Subclass must implement abstract method")
