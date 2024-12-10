from __future__ import annotations

# Imports Begin
from src.main.org.apache.commons.pool2.DestroyMode import *
import os
import typing
from typing import *
import io
from abc import ABC

# Imports End


class KeyedObjectPool(ABC):

    # Class Fields Begin
    # Class Fields End

    # Class Methods Begin
    def returnObject(self, key: typing.Any, obj: typing.Any) -> None:
        pass

    def invalidateObject0(self, key: typing.Any, obj: typing.Any) -> None:
        pass

    def getNumIdle1(self, key: typing.Any) -> int:
        pass

    def getNumIdle0(self) -> int:
        pass

    def getNumActive1(self, key: typing.Any) -> int:
        pass

    def getNumActive0(self) -> int:
        pass

    def close(self) -> None:
        pass

    def clear1(self, key: typing.Any) -> None:
        pass

    def clear0(self) -> None:
        pass

    def borrowObject(self, key: typing.Any) -> typing.Any:
        pass

    def addObject(self, key: typing.Any) -> None:
        pass

    def invalidateObject1(self) -> None:
        pass

    def addObjects1(self) -> None:
        pass

    def addObjects0(self) -> None:
        pass

    # Class Methods End
