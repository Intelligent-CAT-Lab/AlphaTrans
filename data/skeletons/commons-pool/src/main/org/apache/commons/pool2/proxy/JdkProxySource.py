from __future__ import annotations

# Imports Begin
from src.main.org.apache.commons.pool2.proxy.ProxySource import *
from src.main.org.apache.commons.pool2.proxy.JdkProxyHandler import *
from src.main.org.apache.commons.pool2.UsageTracking import *
import typing
from typing import *
import io

# Imports End


class JdkProxySource(ProxySource):

    # Class Fields Begin
    __classLoader: typing.Any = None
    __interfaces: typing.List[typing.Type[typing.Any]] = None
    # Class Fields End

    # Class Methods Begin
    def toString(self) -> str:
        pass

    def resolveProxy(self, proxy: typing.Any) -> typing.Any:
        pass

    def createProxy(
        self, pooledObject: typing.Any, usageTracking: UsageTracking[typing.Any]
    ) -> typing.Any:
        pass

    def __init__(
        self, classLoader: typing.Any, interfaces: typing.List[typing.Type[typing.Any]]
    ) -> None:
        pass

    # Class Methods End
