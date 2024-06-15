import pytest

import time
from threading import Thread
import unittest
from asyncio import CancelledError

class PoolTest(unittest.TestCase):

    __COMMONS_POOL_EVICTIONS_TIMER_THREAD_NAME = "commons-pool-EvictionTimer"
    __EVICTION_PERIOD_IN_MILLIS = 100

    @classmethod
    def setUpClass(cls):
        "This test class is disabled."
        raise unittest.SkipTest

    class Foo:
        pass

    class PooledFooFactory:

        __VALIDATION_WAIT_IN_MILLIS = 1000

        def activateObject(self, pooledObject) -> None:
            try:
                pass
            except Exception as e:
                raise e

        
        def destroyObject(self, pooledObject) -> None:
            try:
                pass
            except Exception as e:
                raise e

        
        def passivateObject(self, pooledObject) -> None:
            try:
                pass
            except Exception as e:
                raise e

        def validateObject(self, pooledObject) -> bool:
            try:
                time.sleep(PoolTest.PooledFooFactory.__VALIDATION_WAIT_IN_MILLIS / 1000.0)
            except (InterruptedError, KeyboardInterrupt, CancelledError, BlockingIOError):
                pass
            return False
