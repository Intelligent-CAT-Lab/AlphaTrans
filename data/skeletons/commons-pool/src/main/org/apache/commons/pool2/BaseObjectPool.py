from __future__ import annotations

# Imports Begin
from src.main.org.apache.commons.pool2.ObjectPool import *
from src.main.org.apache.commons.pool2.BaseObject import *
import os
import typing
from typing import *
import io
from io import StringIO
from abc import ABC

# Imports End


class BaseObjectPool(BaseObject, ObjectPool, ABC):

    # Class Fields Begin
    __closed: bool = None
    # Class Fields End

    # Class Methods Begin
    def _toStringAppendFields(
        self, builder: typing.Union[typing.List[str], io.StringIO]
    ) -> None:
        pass

    def getNumIdle(self) -> int:
        pass

    def getNumActive(self) -> int:
        pass

    def close(self) -> None:
        pass

    def clear(self) -> None:
        pass

    def addObject(self) -> None:
        pass

    def isClosed(self) -> bool:
        pass

    def _assertOpen(self) -> None:
        pass

    def returnObject(self, obj: typing.Any) -> None:
        pass

    def invalidateObject0(self, obj: typing.Any) -> None:
        pass

    def borrowObject(self) -> typing.Any:
        pass

    # Class Methods End
