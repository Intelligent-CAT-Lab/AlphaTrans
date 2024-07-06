from __future__ import annotations
import re
import io
from src.main.org.apache.commons.pool2.impl.BaseObjectPoolConfig import *


class GenericObjectPoolConfig(BaseObjectPoolConfig):

    DEFAULT_MIN_IDLE: int = 0
    DEFAULT_MAX_IDLE: int = 8
    DEFAULT_MAX_TOTAL: int = 8
    __minIdle: int = DEFAULT_MIN_IDLE
    __maxIdle: int = DEFAULT_MAX_IDLE
    __maxTotal: int = DEFAULT_MAX_TOTAL

    def _toStringAppendFields(self, builder: str) -> None:
        super()._toStringAppendFields(builder)
        builder.append(", maxTotal=")
        builder.append(self.__maxTotal)
        builder.append(", maxIdle=")
        builder.append(self.__maxIdle)
        builder.append(", minIdle=")
        builder.append(self.__minIdle)

    def clone(self) -> GenericObjectPoolConfig:
        return super().clone()

    def setMinIdle(self, minIdle: int) -> None:
        self.__minIdle = minIdle

    def setMaxTotal(self, maxTotal: int) -> None:
        self.__maxTotal = maxTotal

    def setMaxIdle(self, maxIdle: int) -> None:
        self.__maxIdle = maxIdle

    def getMinIdle(self) -> int:
        return self.__minIdle

    def getMaxTotal(self) -> int:
        return self.__maxTotal

    def getMaxIdle(self) -> int:
        return self.__maxIdle
