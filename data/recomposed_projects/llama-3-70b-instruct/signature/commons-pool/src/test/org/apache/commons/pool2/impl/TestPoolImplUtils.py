from __future__ import annotations
import time
import re
import unittest
import pytest
from abc import ABC
import io
import typing
from typing import *
import datetime
import unittest
from src.main.org.apache.commons.pool2.impl.PoolImplUtils import *
from src.main.org.apache.commons.pool2.BasePooledObjectFactory import *
from src.main.org.apache.commons.pool2.PooledObject import *


class SimpleFactory(BasePooledObjectFactory):

    def wrap(self, obj: str) -> PooledObject[str]:
        return PooledObject(obj)

    def create(self) -> str:
        return None


class FactoryAB(BasePooledObjectFactory, ABC):

    pass


class FactoryBA(FactoryAB, ABC):

    pass


class FactoryC(FactoryBA, ABC):

    pass


class FactoryDE(FactoryC, ABC):

    pass


class FactoryF(FactoryDE, ABC):

    pass


class NotSimpleFactory(FactoryF):

    def wrap(self, obj: int) -> PooledObject[int]:
        return PooledObject(obj)

    def create(self) -> int:
        return 0


class TestPoolImplUtils(unittest.TestCase):

    __INSTANT_0: datetime.datetime = datetime.datetime.fromtimestamp(0)
    __INSTANT_1: datetime.datetime = datetime.datetime.fromtimestamp(1 / 1000)

    def testToDuration(self) -> None:
        self.assertEqual(
            Duration.ZERO, PoolImplUtils.toDuration(0, TimeUnit.MILLISECONDS)
        )
        self.assertEqual(
            Duration.ofMillis(1), PoolImplUtils.toDuration(1, TimeUnit.MILLISECONDS)
        )
        for tu in TimeUnit.values():
            self.assertEqual(Duration.ZERO, PoolImplUtils.toDuration(0, tu))

    def testToChronoUnit(self) -> None:
        self.assertEqual(
            ChronoUnit.NANOS, PoolImplUtils.toChronoUnit(TimeUnit.NANOSECONDS)
        )
        self.assertEqual(
            ChronoUnit.MICROS, PoolImplUtils.toChronoUnit(TimeUnit.MICROSECONDS)
        )
        self.assertEqual(
            ChronoUnit.MILLIS, PoolImplUtils.toChronoUnit(TimeUnit.MILLISECONDS)
        )
        self.assertEqual(
            ChronoUnit.SECONDS, PoolImplUtils.toChronoUnit(TimeUnit.SECONDS)
        )
        self.assertEqual(
            ChronoUnit.MINUTES, PoolImplUtils.toChronoUnit(TimeUnit.MINUTES)
        )
        self.assertEqual(ChronoUnit.HOURS, PoolImplUtils.toChronoUnit(TimeUnit.HOURS))
        self.assertEqual(ChronoUnit.DAYS, PoolImplUtils.toChronoUnit(TimeUnit.DAYS))

    def testMinInstants(self) -> None:
        self.assertEqual(
            self.__INSTANT_0, PoolImplUtils.min(self.__INSTANT_0, self.__INSTANT_1)
        )
        self.assertEqual(
            self.__INSTANT_0, PoolImplUtils.min(self.__INSTANT_1, self.__INSTANT_0)
        )
        self.assertEqual(
            self.__INSTANT_1, PoolImplUtils.min(self.__INSTANT_1, self.__INSTANT_1)
        )
        self.assertEqual(
            self.__INSTANT_0, PoolImplUtils.min(self.__INSTANT_0, self.__INSTANT_0)
        )

    def testMaxInstants(self) -> None:
        self.assertEqual(
            self.__INSTANT_1, PoolImplUtils.max(self.__INSTANT_0, self.__INSTANT_1)
        )
        self.assertEqual(
            self.__INSTANT_1, PoolImplUtils.max(self.__INSTANT_1, self.__INSTANT_0)
        )
        self.assertEqual(
            self.__INSTANT_1, PoolImplUtils.max(self.__INSTANT_1, self.__INSTANT_1)
        )
        self.assertEqual(
            self.__INSTANT_0, PoolImplUtils.max(self.__INSTANT_0, self.__INSTANT_0)
        )

    def testFactoryTypeSimple(self) -> None:
        result = PoolImplUtils.getFactoryType(SimpleFactory)
        self.assertEqual(String, result)

    def testFactoryTypeNotSimple(self) -> None:
        result = PoolImplUtils.getFactoryType(NotSimpleFactory)
        self.assertEqual(Long, result)
