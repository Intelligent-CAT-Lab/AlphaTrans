from __future__ import annotations
import re
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

    def passivateObject(self, p: PooledObject[typing.Any]) -> None:
        pass

    def makeObject(self) -> PooledObject[typing.Any]:
        return self.wrap(self.create())

    def destroyObject0(self, p: PooledObject[typing.Any]) -> None:
        pass

    def activateObject(self, p: PooledObject[typing.Any]) -> None:
        pass

    def wrap(self, obj: typing.Any) -> PooledObject[typing.Any]:
        return PooledObject(obj)

    def create(self) -> typing.Any:
        return T()
