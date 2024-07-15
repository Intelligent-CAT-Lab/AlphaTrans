from __future__ import annotations
import re
from abc import ABC
import io
import typing
from typing import *
from src.main.org.apache.commons.pool2.DestroyMode import *
from src.main.org.apache.commons.pool2.PooledObject import *


class PooledObjectFactory(ABC):

    def validateObject(self, p: PooledObject[typing.Any]) -> bool:
        return True

    def passivateObject(self, p: PooledObject[typing.Any]) -> None:
        pass

    def makeObject(self) -> PooledObject[typing.Any]:
        return PooledObject[typing.Any]()

    def destroyObject0(self, p: PooledObject[typing.Any]) -> None:
        pass

    def activateObject(self, p: PooledObject[typing.Any]) -> None:
        pass

    def destroyObject1(self) -> None:
        self.destroyObject0(p)
