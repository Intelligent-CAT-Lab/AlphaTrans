from __future__ import annotations
from abc import ABC
import io
import typing
from typing import *
from src.main.org.apache.commons.pool2.BaseObject import *
from src.main.org.apache.commons.pool2.PooledObject import *
from src.main.org.apache.commons.pool2.PooledObjectFactory import *


class BasePooledObjectFactory(BaseObject, PooledObjectFactory, ABC):

    def validateObject(self, p: PooledObject[typing.Any]) -> bool:

        return True

    def ivateObject(self, p: PooledObject[typing.Any]) -> None:

        pass

    def makeObject(self) -> PooledObject[typing.Any]:

        try:
            return self.wrap(self.create())
        except Exception as e:
            raise e

    def destroyObject0(self, p: PooledObject[typing.Any]) -> None:

        pass

    def activateObject(self, p: PooledObject[typing.Any]) -> None:

        pass

    def wrap(self, obj: typing.Any) -> PooledObject[typing.Any]:

        # The actual implementation of the method is not provided in the Java code.
        # Therefore, I'm assuming that the method wraps the object into a PooledObject and returns it.
        # If the actual implementation is different, please provide the correct Python code.

        return PooledObject(obj)

    def create(self) -> typing.Any:

        raise NotImplementedError("Subclass must implement abstract method")
