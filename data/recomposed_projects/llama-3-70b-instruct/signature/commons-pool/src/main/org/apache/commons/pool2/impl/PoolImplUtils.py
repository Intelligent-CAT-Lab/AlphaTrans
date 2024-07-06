from __future__ import annotations
import time
import re
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
        type: typing.Type[PooledObjectFactory[typing.Any]] = PooledObjectFactory[
            typing.Any
        ]
        genericType: typing.Any = PoolImplUtils.__getGenericType(type, factoryClass)
        if isinstance(genericType, int):
            pi: typing.Generic[typing.TypeVar("T")] = (
                PoolImplUtils.__getParameterizedType(type, factoryClass)
            )
            if pi is not None:
                bounds: typing.List[typing.Type[typing.Any]] = (
                    pi.getActualTypeArguments()[(genericType)]
                ).getBounds()
                if bounds is not None and len(bounds) > 0:
                    bound0: typing.Type[typing.Any] = bounds[0]
                    if isinstance(bound0, type):
                        return bound0
            return Object
        return genericType

    @staticmethod
    def toDuration(amount: int, timeUnit: datetime.timedelta) -> datetime.timedelta:
        return datetime.timedelta(amount, PoolImplUtils.toChronoUnit(timeUnit))

    @staticmethod
    def nonNull(
        value: datetime.timedelta, defaultValue: datetime.timedelta
    ) -> datetime.timedelta:
        return value if value is not None else defaultValue

    @staticmethod
    def toChronoUnit(timeUnit: datetime.timedelta) -> datetime.timedelta:
        if timeUnit == datetime.timedelta(seconds=1):
            return datetime.timedelta(seconds=1)
        elif timeUnit == datetime.timedelta(microseconds=1):
            return datetime.timedelta(microseconds=1)
        elif timeUnit == datetime.timedelta(milliseconds=1):
            return datetime.timedelta(milliseconds=1)
        elif timeUnit == datetime.timedelta(microseconds=1):
            return datetime.timedelta(microseconds=1)
        elif timeUnit == datetime.timedelta(minutes=1):
            return datetime.timedelta(minutes=1)
        elif timeUnit == datetime.timedelta(hours=1):
            return datetime.timedelta(hours=1)
        elif timeUnit == datetime.timedelta(days=1):
            return datetime.timedelta(days=1)
        else:
            raise ValueError(timeUnit)

    @staticmethod
    def min(a: datetime.datetime, b: datetime.datetime) -> datetime.datetime:
        return a if a < b else b

    @staticmethod
    def max(a: datetime.datetime, b: datetime.datetime) -> datetime.datetime:
        return a if a > b else b

    @staticmethod
    def isPositive(delay: datetime.timedelta) -> bool:
        return (
            delay != None
            and not delay < datetime.timedelta(0)
            and not delay == datetime.timedelta(0)
        )

    @staticmethod
    def __getTypeParameter(
        clazz: typing.Type[typing.Any], argType: typing.Type
    ) -> typing.Any:
        if isinstance(argType, type):
            return argType
        tvs = clazz.__type_parameters__
        for i in range(len(tvs)):
            if tvs[i] == argType:
                return i
        return None

    @staticmethod
    def __getParameterizedType(
        type: typing.Type[typing.Any], clazz: typing.Type[typing.Any]
    ) -> typing.Generic[typing.TypeVar("T")]:

        pass  # LLM could not translate this method

    @staticmethod
    def __getGenericType(
        type: typing.Type[typing.Any], clazz: typing.Type[typing.Any]
    ) -> typing.Any:
        if type is None or clazz is None:
            return None

        pi: ParameterizedType = PoolImplUtils.__getParameterizedType(type, clazz)
        if pi is not None:
            return PoolImplUtils.__getTypeParameter(
                clazz, pi.getActualTypeArguments()[0]
            )

        superClass: typing.Type[typing.Any] = clazz.getSuperclass()
        result: typing.Any = PoolImplUtils.__getGenericType(type, superClass)
        if isinstance(result, Class):
            return result
        if isinstance(result, int):
            superClassType: ParameterizedType = clazz.getGenericSuperclass()
            return PoolImplUtils.__getTypeParameter(
                clazz, superClassType.getActualTypeArguments()[result]
            )
        return None
