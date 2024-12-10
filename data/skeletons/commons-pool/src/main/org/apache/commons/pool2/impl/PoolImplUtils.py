from __future__ import annotations

# Imports Begin
from src.main.org.apache.commons.pool2.PooledObjectFactory import *
import os
import datetime
import typing
from typing import *
import io

# Imports End


class PoolImplUtils:

    # Class Fields Begin
    # Class Fields End

    # Class Methods Begin
    @staticmethod
    def getFactoryType(
        factoryClass: typing.Type[PooledObjectFactory[typing.Any]],
    ) -> typing.Type[typing.Any]:
        pass

    @staticmethod
    def toDuration(amount: int, timeUnit: datetime.timedelta) -> datetime.timedelta:
        pass

    @staticmethod
    def nonNull(
        value: datetime.timedelta, defaultValue: datetime.timedelta
    ) -> datetime.timedelta:
        pass

    @staticmethod
    def toChronoUnit(timeUnit: datetime.timedelta) -> datetime.timedelta:
        pass

    @staticmethod
    def min_(a: datetime.datetime, b: datetime.datetime) -> datetime.datetime:
        pass

    @staticmethod
    def max_(a: datetime.datetime, b: datetime.datetime) -> datetime.datetime:
        pass

    @staticmethod
    def isPositive(delay: datetime.timedelta) -> bool:
        pass

    @staticmethod
    def __getTypeParameter(
        clazz: typing.Type[typing.Any], argType: typing.Type
    ) -> typing.Any:
        pass

    @staticmethod
    def __getParameterizedType(
        type_: typing.Type[typing.Any], clazz: typing.Type[typing.Any]
    ) -> typing.Generic[typing.TypeVar("T")]:
        pass

    @staticmethod
    def __getGenericType(
        type_: typing.Type[typing.Any], clazz: typing.Type[typing.Any]
    ) -> typing.Any:
        pass

    # Class Methods End
