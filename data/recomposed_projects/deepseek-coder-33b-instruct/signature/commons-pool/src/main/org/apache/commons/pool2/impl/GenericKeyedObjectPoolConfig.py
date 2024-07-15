from __future__ import annotations
import copy
import re
import io
from src.main.org.apache.commons.pool2.impl.BaseObjectPoolConfig import *


class GenericKeyedObjectPoolConfig(BaseObjectPoolConfig):

    DEFAULT_MAX_IDLE_PER_KEY: int = 8
    DEFAULT_MIN_IDLE_PER_KEY: int = 0
    DEFAULT_MAX_TOTAL: int = -1
    DEFAULT_MAX_TOTAL_PER_KEY: int = 8
    __maxTotal: int = DEFAULT_MAX_TOTAL
    __maxTotalPerKey: int = DEFAULT_MAX_TOTAL_PER_KEY
    __maxIdlePerKey: int = DEFAULT_MAX_IDLE_PER_KEY
    __minIdlePerKey: int = DEFAULT_MIN_IDLE_PER_KEY

    def _toStringAppendFields(self, builder: str) -> None:

        super()._toStringAppendFields(builder)
        builder += ", minIdlePerKey=" + str(self.__minIdlePerKey)
        builder += ", maxIdlePerKey=" + str(self.__maxIdlePerKey)
        builder += ", maxTotalPerKey=" + str(self.__maxTotalPerKey)
        builder += ", maxTotal=" + str(self.__maxTotal)

    def clone(self) -> GenericKeyedObjectPoolConfig:
        return copy.deepcopy(self)

    def setMinIdlePerKey(self, minIdlePerKey: int) -> None:
        self.__minIdlePerKey = minIdlePerKey

    def setMaxTotalPerKey(self, maxTotalPerKey: int) -> None:
        self.__maxTotalPerKey = maxTotalPerKey

    def setMaxTotal(self, maxTotal: int) -> None:
        self.__maxTotal = maxTotal

    def setMaxIdlePerKey(self, maxIdlePerKey: int) -> None:
        self.__maxIdlePerKey = maxIdlePerKey

    def getMinIdlePerKey(self) -> int:
        return self.__minIdlePerKey

    def getMaxTotalPerKey(self) -> int:
        return self.__maxTotalPerKey

    def getMaxTotal(self) -> int:
        return self.__maxTotal

    def getMaxIdlePerKey(self) -> int:
        return self.__maxIdlePerKey

    def __init__(self) -> None:
        pass
