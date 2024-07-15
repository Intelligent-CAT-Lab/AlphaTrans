from __future__ import annotations
import re
from abc import ABC
import io
import typing
from typing import *
import os
from src.main.org.apache.commons.pool2.DestroyMode import *


class ObjectPool(ABC):

    def returnObject(self, obj: typing.Any) -> None:
        pass

    def invalidateObject0(self, obj: typing.Any) -> None:
        pass

    def getNumIdle(self) -> int:
        return self.getNumIdle()

    def getNumActive(self) -> int:
        return self.getNumActive()

    def close(self) -> None:
        pass

    def clear(self) -> None:
        pass

    def borrowObject(self) -> typing.Any:
        return self._borrowObject()

    def addObject(self) -> None:
        pass

    def invalidateObject1(self) -> None:
        self.invalidateObject0(obj)

    def addObjects(self) -> None:
        for i in range(count):
            self.addObject()
