from __future__ import annotations
import time
import re
import threading
import unittest
import pytest
import io
from src.main.org.apache.commons.pool2.PooledObject import *


class Foo:

    pass


class PooledFooFactory:

    __VALIDATION_WAIT_IN_MILLIS: int = 1000

    def validateObject(self, pooledObject: PooledObject[Foo]) -> bool:

        try:
            time.sleep(self.__VALIDATION_WAIT_IN_MILLIS / 1000)
        except InterruptedError:
            threading.interrupted()

        return False

    def ivateObject(self, pooledObject: PooledObject[Foo]) -> None:
        pass

    def destroyObject(self, pooledObject: PooledObject[Foo]) -> None:
        pass

    def activateObject(self, pooledObject: PooledObject[Foo]) -> None:
        pass


class PoolTest:

    __EVICTION_PERIOD_IN_MILLIS: int = 100
    __COMMONS_POOL_EVICTIONS_TIMER_THREAD_NAME: str = "commons-pool-EvictionTimer"
