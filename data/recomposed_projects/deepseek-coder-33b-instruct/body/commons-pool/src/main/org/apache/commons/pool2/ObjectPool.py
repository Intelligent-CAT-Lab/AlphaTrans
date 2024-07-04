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

        # Your implementation here
        pass

    def invalidateObject0(self, obj: typing.Any) -> None:

        # Your implementation here
        pass

    def getNumIdle(self) -> int:
        pass

    def getNumActive(self) -> int:
        pass

    def close(self) -> None:

        pass

    def clear(self) -> None:

        raise NotImplementedError("This operation is not supported.")

    def borrowObject(self) -> typing.Any:

        # Your code here
        pass

    def addObject(self) -> None:

        raise Exception("Method not implemented")

    def invalidateObject1(self) -> None:

        # Your implementation here
        pass

    def addObjects(self) -> None:

        for i in range(count):
            self.addObject()
