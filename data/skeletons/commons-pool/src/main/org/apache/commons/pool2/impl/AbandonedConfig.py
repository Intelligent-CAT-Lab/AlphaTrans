from __future__ import annotations

# Imports Begin
from src.main.org.apache.commons.pool2.impl.PoolImplUtils import *
import datetime
import typing
from typing import *
import io
from io import StringIO

# Imports End


class AbandonedConfig:

    # Class Fields Begin
    __DEFAULT_REMOVE_ABANDONED_TIMEOUT_DURATION: datetime.timedelta = None
    __removeAbandonedOnBorrow: bool = None
    __removeAbandonedOnMaintenance: bool = None
    __removeAbandonedTimeoutDuration: datetime.timedelta = None
    __logAbandoned: bool = None
    __requireFullStackTrace: bool = None
    __logWriter: typing.Union[io.TextIOWrapper, io.StringIO] = None
    __useUsageTracking: bool = None
    # Class Fields End

    # Class Methods Begin
    def toString(self) -> str:
        pass

    def setRemoveAbandonedTimeout1(self, removeAbandonedTimeoutSeconds: int) -> None:
        pass

    def getRemoveAbandonedTimeout(self) -> int:
        pass

    def getLogAbandoned(self) -> bool:
        pass

    def setUseUsageTracking(self, useUsageTracking: bool) -> None:
        pass

    def setRequireFullStackTrace(self, requireFullStackTrace: bool) -> None:
        pass

    def setRemoveAbandonedTimeout0(
        self, removeAbandonedTimeout: datetime.timedelta
    ) -> None:
        pass

    def setRemoveAbandonedOnMaintenance(
        self, removeAbandonedOnMaintenance: bool
    ) -> None:
        pass

    def setRemoveAbandonedOnBorrow(self, removeAbandonedOnBorrow: bool) -> None:
        pass

    def setLogWriter(
        self, logWriter: typing.Union[io.TextIOWrapper, io.StringIO]
    ) -> None:
        pass

    def setLogAbandoned(self, logAbandoned: bool) -> None:
        pass

    def getUseUsageTracking(self) -> bool:
        pass

    def getRequireFullStackTrace(self) -> bool:
        pass

    def getRemoveAbandonedTimeoutDuration(self) -> datetime.timedelta:
        pass

    def getRemoveAbandonedOnMaintenance(self) -> bool:
        pass

    def getRemoveAbandonedOnBorrow(self) -> bool:
        pass

    def getLogWriter(self) -> typing.Union[io.TextIOWrapper, io.StringIO]:
        pass

    def __init__(self, constructorId: int, abandonedConfig: AbandonedConfig) -> None:
        pass

    @staticmethod
    def copy(abandonedConfig: AbandonedConfig) -> AbandonedConfig:
        pass

    # Class Methods End
