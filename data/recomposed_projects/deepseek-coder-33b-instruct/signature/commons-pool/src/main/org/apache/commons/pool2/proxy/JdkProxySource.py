from __future__ import annotations
import re
import io
import typing
from typing import *
from src.main.org.apache.commons.pool2.UsageTracking import *
from src.main.org.apache.commons.pool2.proxy.JdkProxyHandler import *
from src.main.org.apache.commons.pool2.proxy.ProxySource import *


class JdkProxySource(ProxySource):

    __interfaces: typing.List[typing.Type[typing.Any]] = None

    __classLoader: typing.Any = None

    def toString(self) -> str:
        return f"JdkProxySource [classLoader={self.__classLoader}, interfaces={str(self.__interfaces)}]"

    def resolveProxy(self, proxy: typing.Any) -> typing.Any:
        return (JdkProxyHandler[typing.Any])(
            Proxy.getInvocationHandler(proxy)
        ).disableProxy()

    def createProxy(
        self, pooledObject: typing.Any, usageTracking: UsageTracking[typing.Any]
    ) -> typing.Any:

        return typing.cast(
            typing.Any,
            Proxy.newProxyInstance(
                self.__classLoader,
                self.__interfaces,
                JdkProxyHandler(pooledObject, usageTracking),
            ),
        )

    def __init__(
        self, classLoader: typing.Any, interfaces: typing.List[typing.Type[typing.Any]]
    ) -> None:
        self.__classLoader = classLoader
        self.__interfaces = interfaces
