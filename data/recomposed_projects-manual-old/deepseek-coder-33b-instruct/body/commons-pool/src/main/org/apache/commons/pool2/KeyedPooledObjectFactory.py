from __future__ import annotations
import re
from abc import ABC
import io
import typing
from typing import *
from src.main.org.apache.commons.pool2.DestroyMode import *
from src.main.org.apache.commons.pool2.PooledObject import *


class KeyedPooledObjectFactory(ABC):

    def validateObject(self, key: typing.Any, p: PooledObject[typing.Any]) -> bool:
        pass

    def ivateObject(self, key: typing.Any, p: PooledObject[typing.Any]) -> None:

        pass

    def makeObject(self, key: typing.Any) -> PooledObject[typing.Any]:
        pass

    def destroyObject0(self, key: typing.Any, p: PooledObject[typing.Any]) -> None:

        # Your implementation here
        pass

    def activateObject(self, key: typing.Any, p: PooledObject[typing.Any]) -> None:

        pass

    def destroyObject1(self) -> None:

        # Your implementation here
        pass
