from __future__ import annotations
import re
from abc import ABC
import io
import typing
from typing import *
import os
from src.main.org.apache.commons.pool2.DestroyMode import *


class KeyedObjectPool(ABC):

    def returnObject(self, key: typing.Any, obj: typing.Any) -> None:
        pass

    def invalidateObject0(self, key: typing.Any, obj: typing.Any) -> None:
        pass

    def getNumIdle1(self, key: typing.Any) -> int:
        return self.getNumIdle(key)

    def getNumIdle0(self) -> int:
        return self.getNumIdle()

    def getNumActive1(self, key: typing.Any) -> int:
        return self._activeCount.get(key)

    def getNumActive0(self) -> int:
        return self._numActive.get()

    def close(self) -> None:
        self.close(ALL)

    def clear1(self, key: typing.Any) -> None:
        pass

    def clear0(self) -> None:
        pass

    def borrowObject(self, key: typing.Any) -> typing.Any:
        raise NotImplementedError()

    def addObject(self, key: typing.Any) -> None:
        pass

    def invalidateObject1(self) -> None:
        self.invalidateObject0(key, obj)

    def addObjects1(self) -> None:

        pass  # LLM could not translate this method

    def addObjects0(self) -> None:
        if keys == None:
            raise ValueError(PoolUtils.MSG_NULL_KEYS)
        iter = keys.iterator()
        while iter.hasNext():
            addObjects1(iter.next(), count)
