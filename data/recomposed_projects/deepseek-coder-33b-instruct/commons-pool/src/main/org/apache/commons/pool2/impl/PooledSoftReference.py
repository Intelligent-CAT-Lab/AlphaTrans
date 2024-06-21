from __future__ import annotations
import io
import typing
from typing import *
from src.main.org.apache.commons.pool2.PooledObjectState import *
from src.main.org.apache.commons.pool2.impl.DefaultPooledObject import *


class PooledSoftReference(DefaultPooledObject):

    __reference: weakref.ref = None

    def toString(self) -> str:

        result = io.StringIO()
        result.write("Referenced Object: ")
        result.write(str(self.getObject()))
        result.write(", State: ")
        with self:
            result.write(str(self.getState()))
        return result.getvalue()

    def getObject(self) -> typing.Any:

        if self.__reference is not None:
            return self.__reference()
        else:
            return None

    def setReference(self, reference: weakref.ref) -> None:

        self.__reference = reference

    def getReference(self) -> weakref.ref:

        return self.__reference

    def __init__(self, reference: weakref.ref) -> None:

        # Call the superclass's constructor with None as the argument
        super().__init__(None)

        # Set the reference
        self.__reference = reference
