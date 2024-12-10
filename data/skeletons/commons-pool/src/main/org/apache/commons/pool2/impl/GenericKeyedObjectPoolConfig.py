from __future__ import annotations

# Imports Begin
from src.main.org.apache.commons.pool2.impl.BaseObjectPoolConfig import *
import typing
from typing import *
import io
from io import StringIO

# Imports End


class GenericKeyedObjectPoolConfig(BaseObjectPoolConfig):

    # Class Fields Begin
    DEFAULT_MAX_TOTAL_PER_KEY: int = None
    DEFAULT_MAX_TOTAL: int = None
    DEFAULT_MIN_IDLE_PER_KEY: int = None
    DEFAULT_MAX_IDLE_PER_KEY: int = None
    __minIdlePerKey: int = None
    __maxIdlePerKey: int = None
    __maxTotalPerKey: int = None
    __maxTotal: int = None
    # Class Fields End

    # Class Methods Begin
    def _toStringAppendFields(
        self, builder: typing.Union[typing.List[str], io.StringIO]
    ) -> None:
        pass

    def clone(self) -> GenericKeyedObjectPoolConfig:
        pass

    def setMinIdlePerKey(self, minIdlePerKey: int) -> None:
        pass

    def setMaxTotalPerKey(self, maxTotalPerKey: int) -> None:
        pass

    def setMaxTotal(self, maxTotal: int) -> None:
        pass

    def setMaxIdlePerKey(self, maxIdlePerKey: int) -> None:
        pass

    def getMinIdlePerKey(self) -> int:
        pass

    def getMaxTotalPerKey(self) -> int:
        pass

    def getMaxTotal(self) -> int:
        pass

    def getMaxIdlePerKey(self) -> int:
        pass

    def __init__(self) -> None:
        pass

    # Class Methods End
