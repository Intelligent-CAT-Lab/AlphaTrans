from __future__ import annotations

# Imports Begin
from src.main.org.apache.commons.pool2.proxy.ProxySource import *
from src.main.org.apache.commons.pool2.UsageTracking import *
from src.main.org.apache.commons.pool2.KeyedObjectPool import *
import os
import typing
from typing import *
import io

# Imports End


class ProxiedKeyedObjectPool(KeyedObjectPool):

    # Class Fields Begin
    __pool: KeyedObjectPool[typing.Any, typing.Any] = None
    __proxySource: ProxySource[typing.Any] = None
    # Class Fields End

    # Class Methods Begin
    def toString(self) -> str:
        pass

    def returnObject(self, key: typing.Any, proxy: typing.Any) -> None:
        pass

    def invalidateObject0(self, key: typing.Any, proxy: typing.Any) -> None:
        pass

    def close(self) -> None:
        pass

    def borrowObject(self, key: typing.Any) -> typing.Any:
        pass

    def addObject(self, key: typing.Any) -> None:
        pass

    def getNumIdle1(self, key: typing.Any) -> int:
        pass

    def getNumIdle0(self) -> int:
        pass

    def getNumActive1(self, key: typing.Any) -> int:
        pass

    def getNumActive0(self) -> int:
        pass

    def clear1(self, key: typing.Any) -> None:
        pass

    def clear0(self) -> None:
        pass

    def __init__(
        self,
        pool: KeyedObjectPool[typing.Any, typing.Any],
        proxySource: ProxySource[typing.Any],
    ) -> None:
        pass

    # Class Methods End
