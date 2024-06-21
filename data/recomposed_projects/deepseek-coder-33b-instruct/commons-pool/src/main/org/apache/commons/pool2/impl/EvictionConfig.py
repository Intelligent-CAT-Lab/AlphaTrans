from __future__ import annotations
import io
import datetime
from src.main.org.apache.commons.pool2.impl.PoolImplUtils import *


class EvictionConfig:

    __minIdle: int = None
    __idleSoftEvictDuration: datetime.timedelta = None
    __idleEvictDuration: datetime.timedelta = None

    __MAX_DURATION: datetime.timedelta = datetime.timedelta(milliseconds=float("inf"))

    def toString(self) -> str:

        builder = io.StringIO()
        builder.write("EvictionConfig [idleEvictDuration=")
        builder.write(str(self.__idleEvictDuration))
        builder.write(", idleSoftEvictDuration=")
        builder.write(str(self.__idleSoftEvictDuration))
        builder.write(", minIdle=")
        builder.write(str(self.__minIdle))
        builder.write("]")
        return builder.getvalue()

    def getIdleSoftEvictTimeDuration(self) -> datetime.timedelta:

        return self.__idleSoftEvictDuration

    def getIdleSoftEvictTime(self) -> int:

        return int(self.__idleSoftEvictDuration.total_seconds() * 1000)

    def getIdleEvictTimeDuration(self) -> datetime.timedelta:

        return self.__idleEvictDuration

    def getIdleEvictTime(self) -> int:

        return int(self.__idleEvictDuration.total_seconds() * 1000)

    @staticmethod
    def EvictionConfig0(
        poolIdleEvictMillis: int, poolIdleSoftEvictMillis: int, minIdle: int
    ) -> EvictionConfig:

        idleEvictDuration = datetime.timedelta(milliseconds=poolIdleEvictMillis)
        idleSoftEvictDuration = datetime.timedelta(milliseconds=poolIdleSoftEvictMillis)

        return EvictionConfig(idleEvictDuration, idleSoftEvictDuration, minIdle)

    def getMinIdle(self) -> int:

        return self.__minIdle

    def getIdleSoftEvictDuration(self) -> datetime.timedelta:

        return self.__idleSoftEvictDuration

    def getIdleEvictDuration(self) -> datetime.timedelta:

        return self.__idleEvictDuration

    def __init__(
        self,
        idleEvictDuration: datetime.timedelta,
        idleSoftEvictDuration: datetime.timedelta,
        minIdle: int,
    ) -> None:

        self.__MAX_DURATION = datetime.timedelta.max

        self.__idleEvictDuration = (
            idleEvictDuration
            if PoolImplUtils.isPositive(idleEvictDuration)
            else self.__MAX_DURATION
        )
        self.__idleSoftEvictDuration = (
            idleSoftEvictDuration
            if PoolImplUtils.isPositive(idleSoftEvictDuration)
            else self.__MAX_DURATION
        )
        self.__minIdle = minIdle
