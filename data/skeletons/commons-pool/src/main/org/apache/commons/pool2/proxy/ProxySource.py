# Imports Begin
from src.main.org.apache.commons.pool2.UsageTracking import *
import typing
from abc import ABC

# Imports End


class ProxySource(ABC):

    # Class Fields Begin
    # Class Fields End

    # Class Methods Begin
    def resolveProxy(self, proxy: typing.Any) -> typing.Any:
        pass

    def createProxy(
        self, pooledObject: typing.Any, usageTracking: UsageTracking[typing.Any]
    ) -> typing.Any:
        pass

    # Class Methods End
