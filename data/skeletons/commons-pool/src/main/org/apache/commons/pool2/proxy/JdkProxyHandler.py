from __future__ import annotations

# Imports Begin
from src.main.org.apache.commons.pool2.proxy.BaseProxyHandler import *
from src.main.org.apache.commons.pool2.UsageTracking import *
import typing
from typing import *
import io

# Imports End


class JdkProxyHandler(BaseProxyHandler):

    # Class Fields Begin
    # Class Fields End

    # Class Methods Begin
    def invoke(
        self,
        proxy: typing.Any,
        method: typing.Union[inspect.Signature, typing.Callable],
        args: typing.List[typing.Any],
    ) -> typing.Any:
        pass

    def __init__(
        self, pooledObject: typing.Any, usageTracking: UsageTracking[typing.Any]
    ) -> None:
        pass

    # Class Methods End
