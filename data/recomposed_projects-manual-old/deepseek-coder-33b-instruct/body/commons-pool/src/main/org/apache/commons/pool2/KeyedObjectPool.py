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

        # Your implementation here
        pass

    def invalidateObject0(self, key: typing.Any, obj: typing.Any) -> None:

        # Your implementation here
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

        raise NotImplementedError(
            "This method is not supported in this implementation."
        )

    def clear0(self) -> None:

        raise NotImplementedError(
            "This method is not supported in this implementation."
        )

    def borrowObject(self, key: typing.Any) -> typing.Any:

        # Your implementation here
        pass

    def addObject(self, key: typing.Any) -> None:

        raise Exception("Method not implemented")
        raise RuntimeError("Method not implemented")
        raise NotImplementedError("Method not implemented")

    def invalidateObject1(self) -> None:

        # Your implementation here
        pass

    def addObjects1(self) -> None:

        if key is None:
            raise ValueError(PoolUtils.MSG_NULL_KEY)
        for i in range(count):
            self.addObject(key)

    def addObjects0(self) -> None:

        if keys is None:
            raise ValueError(PoolUtils.MSG_NULL_KEYS)
        iter = keys.__iter__()
        while iter.__next__():
            self.addObjects1(iter.next(), count)
