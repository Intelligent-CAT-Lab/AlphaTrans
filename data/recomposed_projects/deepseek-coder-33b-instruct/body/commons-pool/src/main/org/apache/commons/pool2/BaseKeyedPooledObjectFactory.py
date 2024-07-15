from __future__ import annotations
import re
from abc import ABC
import io
import typing
from typing import *
from src.main.org.apache.commons.pool2.BaseObject import *
from src.main.org.apache.commons.pool2.KeyedPooledObjectFactory import *
from src.main.org.apache.commons.pool2.PooledObject import *


class BaseKeyedPooledObjectFactory(KeyedPooledObjectFactory, BaseObject, ABC):

    def validateObject(self, key: typing.Any, p: PooledObject[typing.Any]) -> bool:
        return True

    def ivateObject(self, key: typing.Any, p: PooledObject[typing.Any]) -> None:

        pass

    def makeObject(self, key: typing.Any) -> PooledObject[typing.Any]:
        return self.wrap(self.create(key))

    def destroyObject0(self, key: typing.Any, p: PooledObject[typing.Any]) -> None:

        pass

    def activateObject(self, key: typing.Any, p: PooledObject[typing.Any]) -> None:

        pass

    def wrap(self, value: typing.Any) -> PooledObject[typing.Any]:
        pass

    def create(self, key: typing.Any) -> typing.Any:
        raise NotImplementedError("Subclass must implement abstract method")
