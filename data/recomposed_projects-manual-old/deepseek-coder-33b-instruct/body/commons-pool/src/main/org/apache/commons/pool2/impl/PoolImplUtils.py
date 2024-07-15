from __future__ import annotations
import time
import re
import enum
import io
import typing
from typing import *
import datetime
import os
from src.main.org.apache.commons.pool2.PooledObjectFactory import *


class PoolImplUtils:

    @staticmethod
    def getFactoryType(
        factoryClass: typing.Type[PooledObjectFactory[typing.Any]],
    ) -> typing.Type[typing.Any]:

        type = PooledObjectFactory
        genericType = PoolImplUtils.__getGenericType(type, factoryClass)
        if isinstance(genericType, int):
            pi = PoolImplUtils.__getParameterizedType(type, factoryClass)
            if pi is not None:
                bounds = pi.__args__[0].__bounds__
                if bounds is not None and len(bounds) > 0:
                    bound0 = bounds[0]
                    if isinstance(bound0, typing.Type):
                        return bound0
            return object
        return genericType

    @staticmethod
    def toDuration(amount: int, timeUnit: datetime.timedelta) -> datetime.timedelta:

        if timeUnit is None:
            raise ValueError("timeUnit cannot be None")

        if timeUnit == datetime.timedelta(microseconds=1):
            return datetime.timedelta(microseconds=amount)
        elif timeUnit == datetime.timedelta(milliseconds=1):
            return datetime.timedelta(milliseconds=amount)
        elif timeUnit == datetime.timedelta(seconds=1):
            return datetime.timedelta(seconds=amount)
        elif timeUnit == datetime.timedelta(minutes=1):
            return datetime.timedelta(minutes=amount)
        elif timeUnit == datetime.timedelta(hours=1):
            return datetime.timedelta(hours=amount)
        elif timeUnit == datetime.timedelta(days=1):
            return datetime.timedelta(days=amount)
        else:
            raise ValueError(f"Unsupported timeUnit: {timeUnit}")

    @staticmethod
    def nonNull(
        value: datetime.timedelta, defaultValue: datetime.timedelta
    ) -> datetime.timedelta:
        return value if value is not None else defaultValue

    @staticmethod
    def toChronoUnit(timeUnit: datetime.timedelta) -> datetime.timedelta:

        if timeUnit is None:
            raise ValueError("timeUnit cannot be None")

        if timeUnit == datetime.timedelta(microseconds=1):
            return datetime.timedelta(microseconds=1)
        elif timeUnit == datetime.timedelta(milliseconds=1):
            return datetime.timedelta(milliseconds=1)
        elif timeUnit == datetime.timedelta(seconds=1):
            return datetime.timedelta(seconds=1)
        elif timeUnit == datetime.timedelta(minutes=1):
            return datetime.timedelta(minutes=1)
        elif timeUnit == datetime.timedelta(hours=1):
            return datetime.timedelta(hours=1)
        elif timeUnit == datetime.timedelta(days=1):
            return datetime.timedelta(days=1)
        else:
            raise ValueError(f"Unsupported timeUnit: {timeUnit}")

    @staticmethod
    def min(a: datetime.datetime, b: datetime.datetime) -> datetime.datetime:
        return a if a < b else b

    @staticmethod
    def max(a: datetime.datetime, b: datetime.datetime) -> datetime.datetime:
        return a if a > b else b

    @staticmethod
    def isPositive(delay: datetime.timedelta) -> bool:
        return delay is not None and delay.total_seconds() > 0

    @staticmethod
    def __getTypeParameter(
        clazz: typing.Type[typing.Any], argType: typing.Type
    ) -> typing.Any:

        if isinstance(argType, typing._GenericAlias):
            return argType

        tvs = typing.get_type_hints(clazz).keys()
        for i, tv in enumerate(tvs):
            if tv == argType:
                return i

        return None

    @staticmethod
    def __getParameterizedType(
        type: typing.Type[typing.Any], clazz: typing.Type[typing.Any]
    ) -> typing.Generic[typing.TypeVar("T")]:

        for iface in clazz.__orig_bases__:
            if isinstance(iface, typing._GenericAlias):
                pi = iface
                if isinstance(pi.__origin__, type) and type.is_assignable_from(
                    pi.__origin__
                ):
                    return pi
        return None

    @staticmethod
    def __getGenericType(
        type: typing.Type[typing.Any], clazz: typing.Type[typing.Any]
    ) -> typing.Any:

        if type is None or clazz is None:
            return None

        pi = PoolImplUtils.__getParameterizedType(type, clazz)
        if pi is not None:
            return PoolImplUtils.__getTypeParameter(clazz, pi.__args__[0])

        superClass = typing.get_origin(clazz)

        result = PoolImplUtils.__getGenericType(type, superClass)
        if isinstance(result, typing.Type):
            return result
        if isinstance(result, int):
            superClassType = typing.get_args(clazz)[0]
            return PoolImplUtils.__getTypeParameter(
                clazz, superClassType.__args__[result]
            )
        return None
