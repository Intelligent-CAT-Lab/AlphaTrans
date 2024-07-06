from __future__ import annotations
import re
from abc import ABC
import io
import typing
from typing import *
from src.main.org.apache.commons.pool2.UsageTracking import *


class ProxySource(ABC):

    def resolveProxy(self, proxy: typing.Any) -> typing.Any:
        return proxy

    def createProxy(
        self, pooledObject: typing.Any, usageTracking: UsageTracking[typing.Any]
    ) -> typing.Any:
        return pooledObject
