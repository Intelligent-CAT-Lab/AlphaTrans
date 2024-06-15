import pytest

import unittest
from datetime import datetime, timedelta
from abc import ABC
import typing
from src.main.org.apache.commons.pool2.BasePooledObjectFactory import *
from src.main.org.apache.commons.pool2.impl.PoolImplUtils import *

class TestPoolImplUtils(unittest.TestCase):

    __INSTANT_1 = datetime.fromtimestamp(1)
    __INSTANT_0 = datetime.fromtimestamp(0)

    
    A = typing.TypeVar('A')
    B = typing.TypeVar('B')
    C = typing.TypeVar('C')
    D = typing.TypeVar('D')
    E = typing.TypeVar('E')
    F = typing.TypeVar('F')


    
    class FactoryAB(typing.Generic[A, B], BasePooledObjectFactory[B], ABC):
        pass

    
    class FactoryBA(typing.Generic[A, B], FactoryAB[B, A], ABC):
        pass

    
    class FactoryC(typing.Generic[C], FactoryBA[C, str], ABC):
        pass

    
    class FactoryDE(typing.Generic[D, E], FactoryC[D], ABC):
        pass

    
    class FactoryF(typing.Generic[F], FactoryDE[int, F], ABC):
        pass

    
    class NotSimpleFactory(FactoryF[int]):
        
        def create(self):
            try:
                return None
            except Exception as e:
                TestPoolImplUtils.fail(f"An exception occurred: {e}")

        
        def wrap(self, obj):
            return None

    
    class SimpleFactory(BasePooledObjectFactory[str]):
        
        def create(self):
            try:
                return None
            except Exception as e:
                TestPoolImplUtils.fail(f"An exception occurred: {e}")

        
        def wrap(self, obj):
            return None

    
    @pytest.mark.test
    def testFactoryTypeNotSimple(self) -> None:
        result = PoolImplUtils.getFactoryType(
            TestPoolImplUtils.NotSimpleFactory().__class__
        )
        self.assertEqual(result, int)

    
    @pytest.mark.test
    def testFactoryTypeSimple(self) -> None:
        result = PoolImplUtils.getFactoryType(
            TestPoolImplUtils.SimpleFactory().__class__
        )
        self.assertEqual(result, str)

    
    @pytest.mark.test
    def testMaxInstants(self) -> None:
        self.assertEqual(
            PoolImplUtils.max(
                TestPoolImplUtils.__INSTANT_1,
                TestPoolImplUtils.__INSTANT_0
            ),
            TestPoolImplUtils.__INSTANT_1
        )
        self.assertEqual(
            PoolImplUtils.max(
                TestPoolImplUtils.__INSTANT_1,
                TestPoolImplUtils.__INSTANT_0
            ),
            TestPoolImplUtils.__INSTANT_1
        )
        self.assertEqual(
            PoolImplUtils.max(
                TestPoolImplUtils.__INSTANT_1,
                TestPoolImplUtils.__INSTANT_1
            ),
            TestPoolImplUtils.__INSTANT_1
        )
        self.assertEqual(
            PoolImplUtils.max(
                TestPoolImplUtils.__INSTANT_0,
                TestPoolImplUtils.__INSTANT_0
            ),
            TestPoolImplUtils.__INSTANT_0
        )

    
    @pytest.mark.test
    def testMinInstants(self) -> None:
        self.assertEqual(
            PoolImplUtils.min(
                TestPoolImplUtils.__INSTANT_0,
                TestPoolImplUtils.__INSTANT_1
            ),
            TestPoolImplUtils.__INSTANT_0
        )
        self.assertEqual(
            PoolImplUtils.min(
                TestPoolImplUtils.__INSTANT_1,
                TestPoolImplUtils.__INSTANT_0
            ),
            TestPoolImplUtils.__INSTANT_0
        )
        self.assertEqual(
            PoolImplUtils.min(
                TestPoolImplUtils.__INSTANT_1,
                TestPoolImplUtils.__INSTANT_1
            ),
            TestPoolImplUtils.__INSTANT_1
        )
        self.assertEqual(
            PoolImplUtils.min(
                TestPoolImplUtils.__INSTANT_0,
                TestPoolImplUtils.__INSTANT_0
            ),
            TestPoolImplUtils.__INSTANT_0
        )

    
    @pytest.mark.test
    def testToChronoUnit(self) -> None:
        self.assertEqual(
            PoolImplUtils.toChronoUnit(timedelta(microseconds=1) / 1000),
            timedelta(microseconds=1) / 1000
        )
        self.assertEqual(
            PoolImplUtils.toChronoUnit(timedelta(microseconds=1)),
            timedelta(microseconds=1)
        )
        self.assertEqual(
            PoolImplUtils.toChronoUnit(timedelta(milliseconds=1)),
            timedelta(milliseconds=1)
        )
        self.assertEqual(
            PoolImplUtils.toChronoUnit(timedelta(seconds=1)),
            timedelta(seconds=1)
        )
        self.assertEqual(
            PoolImplUtils.toChronoUnit(timedelta(minutes=1)),
            timedelta(minutes=1)
        )
        self.assertEqual(
            PoolImplUtils.toChronoUnit(timedelta(hours=1)),
            timedelta(hours=1)
        )
        self.assertEqual(
            PoolImplUtils.toChronoUnit(timedelta(days=1)),
            timedelta(days=1)
        )

    
    @pytest.mark.test
    def testToDuration(self) -> None:
        self.assertEqual(
            PoolImplUtils.toDuration(0, timedelta(milliseconds=1)),
            timedelta(0)
        )
        self.assertEqual(
            PoolImplUtils.toDuration(1, timedelta(milliseconds=1)),
            timedelta(milliseconds=1)
        )
        amount = 0
        timeUnits = {
            "NANOSECONDS": timedelta(microseconds=amount / 1000),
            "MICROSECONDS": timedelta(microseconds=amount),
            "MILLISECONDS": timedelta(milliseconds=amount),
            "SECONDS": timedelta(seconds=amount),
            "MINUTES": timedelta(minutes=amount),
            "HOURS": timedelta(hours=amount),
            "DAYS": timedelta(days=amount)
        }
        for timeUnit in timeUnits.values():
             self.assertEqual(
                PoolImplUtils.toDuration(0, timeUnit),
                timedelta(0)
            )
