from __future__ import annotations

# Imports Begin
from src.main.org.apache.commons.pool2.DestroyMode import *
import os
import typing
from typing import *
import io
from abc import ABC

# Imports End


class ObjectPool(ABC):

    # Class Fields Begin
    # Class Fields End

    # Class Methods Begin
    def returnObject(self, obj: typing.Any) -> None:
        pass

    def invalidateObject0(self, obj: typing.Any) -> None:
        pass

    def getNumIdle(self) -> int:
        pass

    def getNumActive(self) -> int:
        pass

    def close(self) -> None:
        pass

    def clear(self) -> None:
        pass

    def borrowObject(self) -> typing.Any:
        pass

    def addObject(self) -> None:
        pass

    def invalidateObject1(self) -> None:
        pass

    def addObjects(self) -> None:
        pass

    # Class Methods End
