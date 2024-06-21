from __future__ import annotations
from abc import ABC
import io
import typing
from typing import *


class DefaultPooledObjectInfoMBean(ABC):

    def getPooledObjectType(self) -> str:

        pass

    def getPooledObjectToString(self) -> str:

        pass

    def getLastReturnTimeFormatted(self) -> str:

        pass

    def getLastReturnTime(self) -> int:

        pass

    def getLastBorrowTrace(self) -> str:

        pass

    def getLastBorrowTimeFormatted(self) -> str:

        # Your code here
        pass

    def getLastBorrowTime(self) -> int:

        pass

    def getCreateTimeFormatted(self) -> str:

        pass

    def getCreateTime(self) -> int:

        pass

    def getBorrowedCount(self) -> int:

        pass
