from __future__ import annotations
import io
import typing
from typing import *
import os
from src.main.org.apache.commons.pool2.KeyedObjectPool import *
from src.main.org.apache.commons.pool2.UsageTracking import *
from src.main.org.apache.commons.pool2.proxy.ProxySource import *


class ProxiedKeyedObjectPool(KeyedObjectPool):

    __proxySource: ProxySource[typing.Any] = None
    __pool: KeyedObjectPool[typing.Any, typing.Any] = None

    def toString(self) -> str:

        builder = io.StringIO()
        builder.write("ProxiedKeyedObjectPool [pool=")
        builder.write(str(self.__pool))
        builder.write(", proxySource=")
        builder.write(str(self.__proxySource))
        builder.write("]")
        return builder.getvalue()

    def returnObject(self, key: typing.Any, proxy: typing.Any) -> None:

        try:
            self.__pool.returnObject(key, self.__proxySource.resolveProxy(proxy))
        except Exception as e:
            raise e

    def invalidateObject0(self, key: typing.Any, proxy: typing.Any) -> None:

        try:
            self.__pool.invalidateObject0(key, self.__proxySource.resolveProxy(proxy))
        except Exception as e:
            raise e

    def close(self) -> None:

        self.__pool.close()

    def borrowObject(self, key: typing.Any) -> typing.Any:

        usageTracking = None
        if isinstance(self.__pool, UsageTracking):
            usageTracking = typing.cast(UsageTracking, self.__pool)

        return self.__proxySource.createProxy(
            self.__pool.borrowObject(key), usageTracking
        )

    def addObject(self, key: typing.Any) -> None:

        self.__pool.addObject(key)

    def getNumIdle1(self, key: typing.Any) -> int:

        return self.__pool.getNumIdle1(key)

    def getNumIdle0(self) -> int:

        return self.__pool.getNumIdle0()

    def getNumActive1(self, key: typing.Any) -> int:

        return self.__pool.getNumActive1(key)

    def getNumActive0(self) -> int:

        return self.__pool.getNumActive0()

    def clear1(self, key: typing.Any) -> None:

        try:
            self.__pool.clear1(key)
        except Exception as e:
            raise e
        except NotImplementedError as e:
            raise e

    def clear0(self) -> None:

        try:
            self.__pool.clear0()
        except Exception as e:
            raise e
        except NotImplementedError as e:
            raise e

    def __init__(
        self,
        pool: KeyedObjectPool[typing.Any, typing.Any],
        proxySource: ProxySource[typing.Any],
    ) -> None:

        self.__pool = pool
        self.__proxySource = proxySource
