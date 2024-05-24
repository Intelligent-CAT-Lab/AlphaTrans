from __future__ import annotations

# Imports Begin
from src.main.org.apache.commons.pool2.UsageTracking import *
import typing
from typing import *
import io

# Imports End


class BaseProxyHandler:

    # Class Fields Begin
    __pooledObject: typing.Any = None
    __usageTracking: UsageTracking[typing.Any] = None
    # Class Fields End

    # Class Methods Begin
    def toString(self) -> str:
        pass

    def validateProxiedObject(self) -> None:
        pass

    def getPooledObject(self) -> typing.Any:
        pass

    def doInvoke(
        self,
        method: typing.Union[inspect.Signature, typing.Callable],
        args: typing.List[typing.Any],
    ) -> typing.Any:
        pass

    def disableProxy(self) -> typing.Any:
        pass

    def __init__(
        self, pooledObject: typing.Any, usageTracking: UsageTracking[typing.Any]
    ) -> None:
        pass

    # Class Methods End
