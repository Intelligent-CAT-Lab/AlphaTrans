from __future__ import annotations
import time
import re
from abc import ABC
import io
import typing
from typing import *


class DefaultPooledObjectInfoMBean(ABC):

    def getPooledObjectType(self) -> str:
        return "PooledObject"

    def getPooledObjectToString(self) -> str:
        return str(self)

    def getLastReturnTimeFormatted(self) -> str:
        return str(self.getLastReturnTime())

    def getLastReturnTime(self) -> int:
        return self._lastReturnTime

    def getLastBorrowTrace(self) -> str:
        return self._pooledObject.getLastBorrowTrace()

    def getLastBorrowTimeFormatted(self) -> str:
        return str(self.getLastBorrowTime())

    def getLastBorrowTime(self) -> int:
        return self._lastBorrowTime

    def getCreateTimeFormatted(self) -> str:
        return self.getCreateTime().toString()

    def getCreateTime(self) -> int:
        return self._create_time

    def getBorrowedCount(self) -> int:
        return self._borrowedCount
