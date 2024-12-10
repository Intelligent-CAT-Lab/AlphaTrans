from __future__ import annotations

# Imports Begin
from src.main.org.apache.commons.pool2.impl.DefaultPooledObject import *
from src.main.org.apache.commons.pool2.PooledObjectState import *
import typing
from typing import *
import io

# Imports End


class PooledSoftReference(DefaultPooledObject):

    # Class Fields Begin
    __reference: weakref.ref = None
    # Class Fields End

    # Class Methods Begin
    def toString(self) -> str:
        pass

    def getObject(self) -> typing.Any:
        pass

    def setReference(self, reference: weakref.ref) -> None:
        pass

    def getReference(self) -> weakref.ref:
        pass

    def __init__(self, reference: weakref.ref) -> None:
        pass

    # Class Methods End
