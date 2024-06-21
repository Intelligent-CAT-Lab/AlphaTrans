from __future__ import annotations
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

        builder = io.StringIO()
        builder.write("ProxiedObjectPool [pool=")
        builder.write(str(self.__pool))
        builder.write(", proxySource=")
        builder.write(str(self.__proxySource))
        builder.write("]")
        return builder.getvalue()

    def returnObject(self, proxy: typing.Any) -> None:

        self.__pool.returnObject(self.__proxySource.resolveProxy(proxy))

    def invalidateObject0(self, proxy: typing.Any) -> None:

        try:
            self.__pool.invalidateObject0(self.__proxySource.resolveProxy(proxy))
        except Exception as e:
            raise e

    def getNumIdle(self) -> int:

        if self.__pool is None:
            return 0

        return self.__pool.getNumIdle()

    def getNumActive(self) -> int:

        if self.__pool is None:
            return 0

        return self.__pool.getNumActive()

    def close(self) -> None:

        if self.__pool is not None:
            self.__pool.close()

    def clear(self) -> None:

        try:
            self.__pool.clear()
        except Exception as e:
            raise e
        except NotImplementedError as e:
            raise e

    def borrowObject(self) -> typing.Any:

        usageTracking = None
        if isinstance(self.__pool, UsageTracking):
            usageTracking = typing.cast(UsageTracking[typing.Any], self.__pool)

        return self.__proxySource.createProxy(self.__pool.borrowObject(), usageTracking)

    def addObject(self) -> None:

        try:
            self.__pool.addObject()
        except Exception as e:
            print(f"An exception occurred: {e}")
            raise
        except IllegalStateException as e:
            print(f"IllegalStateException occurred: {e}")
            raise
        except NotImplementedError as e:
            print(f"NotImplementedError occurred: {e}")
            raise

    def __init__(
        self, pool: ObjectPool[typing.Any], proxySource: ProxySource[typing.Any]
    ) -> None:

        self.__pool = pool
        self.__proxySource = proxySource
