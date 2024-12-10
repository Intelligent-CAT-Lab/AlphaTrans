from __future__ import annotations

# Imports Begin
from src.main.org.apache.commons.pool2.PooledObject import *
from src.main.org.apache.commons.pool2.DestroyMode import *
import typing
from typing import *
import io
from abc import ABC

# Imports End


class KeyedPooledObjectFactory(ABC):

    # Class Fields Begin
    # Class Fields End

    # Class Methods Begin
    def validateObject(self, key: typing.Any, p: PooledObject[typing.Any]) -> bool:
        pass

    def passivateObject(self, key: typing.Any, p: PooledObject[typing.Any]) -> None:
        pass

    def makeObject(self, key: typing.Any) -> PooledObject[typing.Any]:
        pass

    def destroyObject0(self, key: typing.Any, p: PooledObject[typing.Any]) -> None:
        pass

    def activateObject(self, key: typing.Any, p: PooledObject[typing.Any]) -> None:
        pass

    def destroyObject1(self) -> None:
        pass

    # Class Methods End
