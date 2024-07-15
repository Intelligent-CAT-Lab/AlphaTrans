from __future__ import annotations
import re
import io
import typing
from typing import *
import os
from src.main.org.apache.commons.pool2.ObjectPool import *
from src.main.org.apache.commons.pool2.UsageTracking import *
from src.main.org.apache.commons.pool2.proxy.ProxySource import *


class ProxiedObjectPool(ObjectPool):

    __proxySource: ProxySource[typing.Any] = None

    __pool: ObjectPool[typing.Any] = None

    def toString(self) -> str:
        return (
            f"ProxiedObjectPool [pool={self.__pool}, proxySource={self.__proxySource}]"
        )

    def returnObject(self, proxy: typing.Any) -> None:
        self.__pool.returnObject(self.__proxySource.resolveProxy(proxy))

    def invalidateObject0(self, proxy: typing.Any) -> None:
        self.__pool.invalidateObject0(self.__proxySource.resolveProxy(proxy))

    def getNumIdle(self) -> int:
        return self.__pool.getNumIdle()

    def getNumActive(self) -> int:
        return self.__pool.getNumActive()

    def close(self) -> None:
        self.__pool.close()

    def clear(self) -> None:
        self.__pool.clear()

    def borrowObject(self) -> typing.Any:

        usageTracking = None
        if isinstance(self.__pool, UsageTracking):
            usageTracking = typing.cast(UsageTracking[typing.Any], self.__pool)

        return self.__proxySource.createProxy(self.__pool.borrowObject(), usageTracking)

    def addObject(self) -> None:
        self.__pool.addObject()

    def __init__(
        self, pool: ObjectPool[typing.Any], proxySource: ProxySource[typing.Any]
    ) -> None:
        self.__pool = pool
        self.__proxySource = proxySource
