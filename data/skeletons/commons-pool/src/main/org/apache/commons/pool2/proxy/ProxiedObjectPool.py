from __future__ import annotations

# Imports Begin
from src.main.org.apache.commons.pool2.proxy.ProxySource import *
from src.main.org.apache.commons.pool2.UsageTracking import *
from src.main.org.apache.commons.pool2.ObjectPool import *
import os
import typing
from typing import *
import io

# Imports End


class ProxiedObjectPool(ObjectPool):

    # Class Fields Begin
    __pool: ObjectPool[typing.Any] = None
    __proxySource: ProxySource[typing.Any] = None
    # Class Fields End

    # Class Methods Begin
    def toString(self) -> str:
        pass

    def returnObject(self, proxy: typing.Any) -> None:
        pass

    def invalidateObject0(self, proxy: typing.Any) -> None:
        pass

    def getNumIdle(self) -> int:
        pass

    def getNumActive(self) -> int:
        pass

    def close(self) -> None:
        pass

    def clear(self) -> None:
        pass

    def borrowObject(self) -> typing.Any:
        pass

    def addObject(self) -> None:
        pass

    def __init__(
        self, pool: ObjectPool[typing.Any], proxySource: ProxySource[typing.Any]
    ) -> None:
        pass

    # Class Methods End
