from __future__ import annotations
from abc import ABC
import io
import typing
from typing import *
from src.main.org.apache.commons.pool2.DestroyMode import *
from src.main.org.apache.commons.pool2.PooledObject import *


class PooledObjectFactory(ABC):

    def validateObject(self, p: PooledObject[typing.Any]) -> bool:

        # Your code here
        pass

    def ivateObject(self, p: PooledObject[typing.Any]) -> None:

        pass

    def makeObject(self) -> PooledObject[typing.Any]:

        # Your code here
        pass

    def destroyObject0(self, p: PooledObject[typing.Any]) -> None:

        # The Java method is void, so it doesn't return anything.
        # If the method throws an exception, it should be handled in the calling code.
        # The Python equivalent of the Java method would be:

        try:
            # Insert code here to destroy the object
            pass
        except Exception as e:
            raise e

    def activateObject(self, p: PooledObject[typing.Any]) -> None:

        # Your code here
        pass

    def destroyObject1(self) -> None:

        def destroyObject0(self, p: PooledObject[typing.Any]) -> None:
            pass
