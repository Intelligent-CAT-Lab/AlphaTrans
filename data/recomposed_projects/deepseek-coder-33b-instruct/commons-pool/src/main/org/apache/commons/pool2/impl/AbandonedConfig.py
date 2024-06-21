from __future__ import annotations
import sys
from io import StringIO
import io
import typing
from typing import *
import datetime
from src.main.org.apache.commons.pool2.impl.PoolImplUtils import *


class AbandonedConfig:

    __useUsageTracking: bool = None

    __logWriter: typing.Union[io.TextIOWrapper, io.StringIO] = io.TextIOWrapper(
        sys.stdout.buffer, encoding="utf-8"
    )

    __requireFullStackTrace: bool = True
    __logAbandoned: bool = None

    __removeAbandonedTimeoutDuration: datetime.timedelta = datetime.timedelta(
        seconds=DEFAULT_REMOVE_ABANDONED_TIMEOUT_DURATION
    )
    __removeAbandonedOnMaintenance: bool = None
    __removeAbandonedOnBorrow: bool = None

    __DEFAULT_REMOVE_ABANDONED_TIMEOUT_DURATION: datetime.timedelta = (
        datetime.timedelta(minutes=5)
    )

    def toString(self) -> str:

        builder = "AbandonedConfig [removeAbandonedOnBorrow="
        builder += str(self.__removeAbandonedOnBorrow)
        builder += ", removeAbandonedOnMaintenance="
        builder += str(self.__removeAbandonedOnMaintenance)
        builder += ", removeAbandonedTimeoutDuration="
        builder += str(self.__removeAbandonedTimeoutDuration)
        builder += ", logAbandoned="
        builder += str(self.__logAbandoned)
        builder += ", logWriter="
        builder += str(self.__logWriter)
        builder += ", useUsageTracking="
        builder += str(self.__useUsageTracking)
        builder += "]"
        return builder

    def setRemoveAbandonedTimeout1(self, removeAbandonedTimeoutSeconds: int) -> None:

        self.setRemoveAbandonedTimeout0(
            datetime.timedelta(seconds=removeAbandonedTimeoutSeconds)
        )

    def getRemoveAbandonedTimeout(self) -> int:

        return int(self.__removeAbandonedTimeoutDuration.total_seconds())

    def getLogAbandoned(self) -> bool:

        return self.__logAbandoned

    def setUseUsageTracking(self, useUsageTracking: bool) -> None:

        self.__useUsageTracking = useUsageTracking

    def setRequireFullStackTrace(self, requireFullStackTrace: bool) -> None:

        self.__requireFullStackTrace = requireFullStackTrace

    def setRemoveAbandonedTimeout0(
        self, removeAbandonedTimeout: datetime.timedelta
    ) -> None:

        self.__removeAbandonedTimeoutDuration = nonNull(
            removeAbandonedTimeout, self.__DEFAULT_REMOVE_ABANDONED_TIMEOUT_DURATION
        )

    def setRemoveAbandonedOnMaintenance(
        self, removeAbandonedOnMaintenance: bool
    ) -> None:

        self.__removeAbandonedOnMaintenance = removeAbandonedOnMaintenance

    def setRemoveAbandonedOnBorrow(self, removeAbandonedOnBorrow: bool) -> None:

        self.__removeAbandonedOnBorrow = removeAbandonedOnBorrow

    def setLogWriter(
        self, logWriter: typing.Union[io.TextIOWrapper, io.StringIO]
    ) -> None:

        self.__logWriter = logWriter

    def setLogAbandoned(self, logAbandoned: bool) -> None:

        self.__logAbandoned = logAbandoned

    def getUseUsageTracking(self) -> bool:

        return self.__useUsageTracking

    def getRequireFullStackTrace(self) -> bool:

        return self.__requireFullStackTrace

    def getRemoveAbandonedTimeoutDuration(self) -> datetime.timedelta:

        return self.__removeAbandonedTimeoutDuration

    def getRemoveAbandonedOnMaintenance(self) -> bool:

        return self.__removeAbandonedOnMaintenance

    def getRemoveAbandonedOnBorrow(self) -> bool:

        return self.__removeAbandonedOnBorrow

    def getLogWriter(self) -> typing.Union[io.TextIOWrapper, io.StringIO]:

        return self.__logWriter

    def __init__(self, constructorId: int, abandonedConfig: AbandonedConfig) -> None:

        if constructorId == 0:
            self.setLogAbandoned(abandonedConfig.getLogAbandoned())
            self.setLogWriter(abandonedConfig.getLogWriter())
            self.setRemoveAbandonedOnBorrow(
                abandonedConfig.getRemoveAbandonedOnBorrow()
            )
            self.setRemoveAbandonedOnMaintenance(
                abandonedConfig.getRemoveAbandonedOnMaintenance()
            )
            self.setRemoveAbandonedTimeout0(
                abandonedConfig.getRemoveAbandonedTimeoutDuration()
            )
            self.setUseUsageTracking(abandonedConfig.getUseUsageTracking())
            self.setRequireFullStackTrace(abandonedConfig.getRequireFullStackTrace())

    @staticmethod
    def copy(abandonedConfig: AbandonedConfig) -> AbandonedConfig:

        if abandonedConfig is None:
            return None
        else:
            return AbandonedConfig(0, abandonedConfig)
