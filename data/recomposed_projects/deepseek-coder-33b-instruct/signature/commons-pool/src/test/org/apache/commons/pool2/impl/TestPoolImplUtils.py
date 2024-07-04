from __future__ import annotations
import time
import re
import os
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
        return PooledObject[int](obj)

    def create(self) -> int:
        return None


class TestPoolImplUtils(unittest.TestCase):

    __INSTANT_0: datetime.datetime = datetime.datetime.fromtimestamp(0)
    __INSTANT_1: datetime.datetime = datetime.datetime.fromtimestamp(
        1 / 1000.0, tz=datetime.timezone.utc
    )

    def testToDuration(self) -> None:

        # Test with 0 milliseconds
        self.assertEqual(
            datetime.timedelta(),
            PoolImplUtils.toDuration(0, datetime.timedelta(milliseconds=1)),
        )

        # Test with 1 millisecond
        self.assertEqual(
            datetime.timedelta(milliseconds=1),
            PoolImplUtils.toDuration(1, datetime.timedelta(milliseconds=1)),
        )

        # Test with all TimeUnit values
        for tu in [
            datetime.timedelta(days=1),
            datetime.timedelta(seconds=1),
            datetime.timedelta(microseconds=1000),
            datetime.timedelta(milliseconds=2900),
            datetime.timedelta(minutes=1),
            datetime.timedelta(hours=1),
            datetime.timedelta(weeks=1),
        ]:
            self.assertEqual(datetime.timedelta(), PoolImplUtils.toDuration(0, tu))

    def testToChronoUnit(self) -> None:

        self.assertEqual(
            datetime.timedelta(nanoseconds=1),
            PoolImplUtils.toChronoUnit(datetime.timezone.utc),
        )
        self.assertEqual(
            datetime.timedelta(microseconds=1),
            PoolImplUtils.toChronoUnit(datetime.timezone.utc),
        )
        self.assertEqual(
            datetime.timedelta(milliseconds=1),
            PoolImplUtils.toChronoUnit(datetime.timezone.utc),
        )
        self.assertEqual(
            datetime.timedelta(seconds=1),
            PoolImplUtils.toChronoUnit(datetime.timezone.utc),
        )
        self.assertEqual(
            datetime.timedelta(minutes=1),
            PoolImplUtils.toChronoUnit(datetime.timezone.utc),
        )
        self.assertEqual(
            datetime.timedelta(hours=1),
            PoolImplUtils.toChronoUnit(datetime.timezone.utc),
        )
        self.assertEqual(
            datetime.timedelta(days=1),
            PoolImplUtils.toChronoUnit(datetime.timezone.utc),
        )

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
        self.assertEqual(str, result)

    def testFactoryTypeNotSimple(self) -> None:

        result = PoolImplUtils.getFactoryType(NotSimpleFactory)
        self.assertEqual(long, result)
