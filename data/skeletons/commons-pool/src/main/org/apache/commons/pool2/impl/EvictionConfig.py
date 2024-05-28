from __future__ import annotations

# Imports Begin
from src.main.org.apache.commons.pool2.impl.PoolImplUtils import *
import datetime
import io

# Imports End


class EvictionConfig:

    # Class Fields Begin
    __MAX_DURATION: datetime.timedelta = None
    __idleEvictDuration: datetime.timedelta = None
    __idleSoftEvictDuration: datetime.timedelta = None
    __minIdle: int = None
    # Class Fields End

    # Class Methods Begin
    def toString(self) -> str:
        pass

    def getIdleSoftEvictTimeDuration(self) -> datetime.timedelta:
        pass

    def getIdleSoftEvictTime(self) -> int:
        pass

    def getIdleEvictTimeDuration(self) -> datetime.timedelta:
        pass

    def getIdleEvictTime(self) -> int:
        pass

    @staticmethod
    def EvictionConfig0(
        poolIdleEvictMillis: int, poolIdleSoftEvictMillis: int, minIdle: int
    ) -> EvictionConfig:
        pass

    def getMinIdle(self) -> int:
        pass

    def getIdleSoftEvictDuration(self) -> datetime.timedelta:
        pass

    def getIdleEvictDuration(self) -> datetime.timedelta:
        pass

    def __init__(
        self,
        idleEvictDuration: datetime.timedelta,
        idleSoftEvictDuration: datetime.timedelta,
        minIdle: int,
    ) -> None:
        pass

    # Class Methods End
