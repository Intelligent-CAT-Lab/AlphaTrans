from __future__ import annotations

# Imports Begin
import typing
from typing import *
import io
from abc import ABC

# Imports End


class DefaultPooledObjectInfoMBean(ABC):

    # Class Fields Begin
    # Class Fields End

    # Class Methods Begin
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
        pass

    def getLastBorrowTime(self) -> int:
        pass

    def getCreateTimeFormatted(self) -> str:
        pass

    def getCreateTime(self) -> int:
        pass

    def getBorrowedCount(self) -> int:
        pass

    # Class Methods End
