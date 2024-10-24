from __future__ import annotations

# Imports Begin
from src.main.org.apache.commons.pool2.impl.BaseObjectPoolConfig import *
import typing
from typing import *
import io
from io import StringIO

# Imports End


class GenericObjectPoolConfig(BaseObjectPoolConfig):

    # Class Fields Begin
    DEFAULT_MAX_TOTAL: int = None
    DEFAULT_MAX_IDLE: int = None
    DEFAULT_MIN_IDLE: int = None
    __maxTotal: int = None
    __maxIdle: int = None
    __minIdle: int = None
    # Class Fields End

    # Class Methods Begin
    def _toStringAppendFields(
        self, builder: typing.Union[typing.List[str], io.StringIO]
    ) -> None:
        pass

    def clone(self) -> GenericObjectPoolConfig:
        pass

    def setMinIdle(self, minIdle: int) -> None:
        pass

    def setMaxTotal(self, maxTotal: int) -> None:
        pass

    def setMaxIdle(self, maxIdle: int) -> None:
        pass

    def getMinIdle(self) -> int:
        pass

    def getMaxTotal(self) -> int:
        pass

    def getMaxIdle(self) -> int:
        pass

    # Class Methods End
