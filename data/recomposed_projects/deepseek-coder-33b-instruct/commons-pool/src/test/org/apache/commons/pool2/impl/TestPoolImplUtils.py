from __future__ import annotations
from abc import ABC
import io
import typing
from typing import *
import datetime
from src.main.org.apache.commons.pool2.impl.PoolImplUtils import *
from src.main.org.apache.commons.pool2.BasePooledObjectFactory import *
from src.main.org.apache.commons.pool2.PooledObject import *


class SimpleFactory(BasePooledObjectFactory):

    def wrap(self, obj: str) -> PooledObject[str]:

        # The actual implementation of the method is not provided in the Java code.
        # Therefore, I'm assuming that the method returns a PooledObject object.
        # If the actual implementation is different, please provide the correct implementation.

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


class TestPoolImplUtils:

    __INSTANT_0: datetime.datetime = datetime.datetime.fromtimestamp(0)

    __INSTANT_1: datetime.datetime = datetime.datetime.fromtimestamp(
        1 / 1000.0, tz=datetime.timezone.utc
    )

    def testToDuration(self) -> None:

        assert Duration.ZERO == PoolImplUtils.toDuration(0, TimeUnit.MILLISECONDS)
        assert Duration.ofMillis(1) == PoolImplUtils.toDuration(
            1, TimeUnit.MILLISECONDS
        )
        for tu in TimeUnit.values():
            assert Duration.ZERO == PoolImplUtils.toDuration(0, tu)

    def testToChronoUnit(self) -> None:

        assert (
            PoolImplUtils.toChronoUnit(datetime.timeunit.NANOSECONDS)
            == datetime.timeunit.NANOSECONDS
        )
        assert (
            PoolImplUtils.toChronoUnit(datetime.timeunit.MICROSECONDS)
            == datetime.timeunit.MICROSECONDS
        )
        assert (
            PoolImplUtils.toChronoUnit(datetime.timeunit.MILLISECONDS)
            == datetime.timeunit.MILLISECONDS
        )
        assert (
            PoolImplUtils.toChronoUnit(datetime.timeunit.SECONDS)
            == datetime.timeunit.SECONDS
        )
        assert (
            PoolImplUtils.toChronoUnit(datetime.timeunit.MINUTES)
            == datetime.timeunit.MINUTES
        )
        assert (
            PoolImplUtils.toChronoUnit(datetime.timeunit.HOURS)
            == datetime.timeunit.HOURS
        )
        assert (
            PoolImplUtils.toChronoUnit(datetime.timeunit.DAYS) == datetime.timeunit.DAYS
        )

    def testMinInstants(self) -> None:

        assert self.__INSTANT_0 == PoolImplUtils.min(self.__INSTANT_0, self.__INSTANT_1)
        assert self.__INSTANT_0 == PoolImplUtils.min(self.__INSTANT_1, self.__INSTANT_0)
        assert self.__INSTANT_1 == PoolImplUtils.min(self.__INSTANT_1, self.__INSTANT_1)
        assert self.__INSTANT_0 == PoolImplUtils.min(self.__INSTANT_0, self.__INSTANT_0)

    def testMaxInstants(self) -> None:

        assert self.__INSTANT_0 == PoolImplUtils.max(self.__INSTANT_0, self.__INSTANT_1)
        assert self.__INSTANT_1 == PoolImplUtils.max(self.__INSTANT_1, self.__INSTANT_0)
        assert self.__INSTANT_1 == PoolImplUtils.max(self.__INSTANT_1, self.__INSTANT_1)
        assert self.__INSTANT_0 == PoolImplUtils.max(self.__INSTANT_0, self.__INSTANT_0)

    def testFactoryTypeSimple(self) -> None:

        class SimpleFactory(BasePooledObjectFactory):
            def create(self) -> typing.Any:
                pass

            def destroyObject(self, p: PooledObject) -> None:
                pass

            def wrap(self, obj: typing.Any) -> PooledObject:
                pass

            def passivateObject(self, p: PooledObject) -> None:
                pass

            def activateObject(self, p: PooledObject) -> None:
                pass

            def validateObject(self, p: PooledObject) -> bool:
                pass

        result = PoolImplUtils.getFactoryType(SimpleFactory)
        assert result == str

    def testFactoryTypeNotSimple(self) -> None:

        class NotSimpleFactory(BasePooledObjectFactory):
            def create(self) -> typing.Any:
                pass

            def destroyObject(self, p: PooledObject) -> None:
                pass

            def activateObject(self, p: PooledObject) -> None:
                pass

            def passivateObject(self, p: PooledObject) -> None:
                pass

            def validateObject(self, p: PooledObject) -> bool:
                pass

        result = PoolImplUtils.getFactoryType(NotSimpleFactory)
        assert result == long
