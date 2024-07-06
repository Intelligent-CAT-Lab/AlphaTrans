from __future__ import annotations
import re
import io
import typing
from typing import *
from src.main.org.apache.commons.pool2.PooledObjectState import *
from src.main.org.apache.commons.pool2.impl.DefaultPooledObject import *


class PooledSoftReference(DefaultPooledObject):

    __reference: weakref.ref = None

    def toString(self) -> str:

        pass  # LLM could not translate this method

    def getObject(self) -> typing.Any:
        return self.__reference.get()

    def setReference(self, reference: weakref.ref) -> None:
        self.__reference = reference

    def getReference(self) -> weakref.ref:
        return self.__reference

    def __init__(self, reference: weakref.ref) -> None:
        super().__init__(None)
        self.__reference = reference
